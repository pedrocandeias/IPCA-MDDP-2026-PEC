#!/usr/bin/env python3
"""Synchronise static DOCX indexes with the printed pages of a PDF export.

The IPCA document contains static contents, table and figure lists. This tool
matches each index title against the body text extracted with ``pdftotext
-layout`` and writes the printed page number back to the two-run index entry.
It also applies the final widths to Table 4.9.
"""

from __future__ import annotations

import argparse
import os
import re
import tempfile
import unicodedata
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

TITLE_ALIASES = {
    "A.4.4 Registo fiel do contexto da medição": (
        "A.4.4 REGISTO DO CONTEXTO DA MEDIÇÃO",
        "first",
    ),
    "B.1 Finalidade": ("B.1 FINALIDADE", "first"),
    "C.4.3 Divisão proximal–distal": (
        "A divisão entre segmentos proximais e distais é calculada",
        "first",
    ),
    "C.4.4 Braçadeira, folgas e parâmetros fixos": (
        "C.4.4 COMPONENTE DE FIXAÇÃO AO PUNHO, FOLGAS E PARÂMETROS FIXOS",
        "first",
    ),
    "C.6.4 Dependência entre comprimento digital e escala global": (
        "C.6.4 DEPENDÊNCIA ENTRE COMPRIMENTO DOS DEDOS E ESCALA GLOBAL",
        "first",
    ),
}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).casefold()
    value = "".join(character for character in text if character.isalnum())
    # O índice recebido usa pontualmente o Acordo Ortográfico de 1990,
    # enquanto o corpo da dissertação conserva a grafia europeia anterior.
    # Estas equivalências impedem que a diferença meramente ortográfica torne
    # uma entrada impossível de localizar no PDF.
    for modern, manuscript in (
        ("projeto", "projecto"),
        ("atividade", "actividade"),
        ("respetiv", "respectiv"),
        ("selecao", "seleccao"),
        ("arquitet", "architect"),
        ("otimiz", "optimiz"),
        ("adocao", "adopcao"),
        ("interacao", "interaccao"),
        ("extracao", "extraccao"),
        ("direta", "directa"),
        ("detet", "detect"),
        ("excec", "excepc"),
    ):
        value = value.replace(modern, manuscript)
    return value


def is_index_style(style: str) -> bool:
    """Aceita os estilos locais em português e os estilos TOC do modelo IPCA."""
    return style.startswith("ndice") or style.startswith("TOC")


def stable_identifier(title: str) -> str | None:
    """Obtém o identificador estável de uma legenda ou título numerado."""
    for pattern in (
        r"((?:Tabela|Figura) [A-D0-9]+\.[0-9]+)\b",
        r"(Capítulo [0-9]+)\b",
        r"([A-D]\.[0-9]+(?:\.[0-9]+)*)\b",
        r"([0-9]+(?:\.[0-9]+)+)\b",
        r"(Lacuna [0-9]+)\b",
    ):
        match = re.search(pattern, title)
        if match:
            return normalise(match.group(1))
    return None


def update_parameter_dictionary_widths(root: etree._Element) -> None:
    """Keep the parameter-dictionary table widths after page synchronisation.

    The caption was originally numbered by chapter (Table 4.9) and is now
    numbered sequentially (Table 15 after the RTD table was restored). Accept
    the transitional cached number 14 as well so older exports remain
    reproducible.
    """

    accepted_captions = {
        "Tabela 4.9 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados",
        "Tabela 14 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados",
        "Tabela 15 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados",
    }
    captions = [
        p for p in root.xpath(".//w:p", namespaces=NS)
        if text_of(p) in accepted_captions
    ]
    if len(captions) != 1:
        raise RuntimeError(
            "Expected one parameter-dictionary table caption; "
            f"found {len(captions)}"
        )
    table = captions[0].getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("Parameter-dictionary table does not follow its caption")
    widths = [1650, 1950, 900, 1500, 3100]
    grid_columns = table.xpath("./w:tblGrid/w:gridCol", namespaces=NS)
    if len(grid_columns) != len(widths):
        raise RuntimeError("Unexpected Table 4.9 column count")
    for column, width in zip(grid_columns, widths, strict=True):
        column.set(qn("w"), str(width))
    for row in table.xpath("./w:tr", namespaces=NS):
        cells = row.xpath("./w:tc", namespaces=NS)
        if len(cells) != len(widths):
            raise RuntimeError("Unexpected Table 4.9 row shape")
        for cell, width in zip(cells, widths, strict=True):
            cell_width = cell.find("./w:tcPr/w:tcW", namespaces=NS)
            if cell_width is None:
                raise RuntimeError("Missing Table 4.9 cell width")
            cell_width.set(qn("w"), str(width))


def static_page_map(document_xml: bytes) -> dict[str, str]:
    root = etree.fromstring(document_xml)
    pages: dict[str, str] = {}
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        style = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if not style or not is_index_style(style[0]) or len(text_nodes) != 2:
            continue
        title = text_nodes[0].text or ""
        page = text_nodes[1].text or ""
        match = re.match(r"((?:Tabela|Figura) [A-D0-9]+\.[0-9]+)\b", title)
        if match and page.isdigit():
            pages.setdefault(match.group(1), page)
    return pages


def synchronise_markdown(path: Path, document_xml: bytes) -> int:
    pages = static_page_map(document_xml)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    updated = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith(("| Tabela ", "| Figura ")):
            continue
        cells = line.rstrip("\r\n").split("|")
        if len(cells) != 5:
            continue
        identifier = cells[1].strip()
        page = pages.get(identifier)
        if page is None or cells[3].strip() == page:
            continue
        cells[3] = f" {page} "
        newline = "\n" if line.endswith("\n") else ""
        lines[index] = "|".join(cells) + newline
        updated += 1
    if updated:
        path.write_text("".join(lines), encoding="utf-8")
    return updated


def apply(document_xml: bytes, extracted_pdf: str, page_offset: int) -> tuple[bytes, int, list[str]]:
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(document_xml, parser)
    pages = extracted_pdf.split("\f")
    normalised_pages = [normalise(page) for page in pages]
    body_titles: dict[str, list[str]] = {}
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        styles = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if styles and is_index_style(styles[0]) and len(text_nodes) == 2:
            continue
        title = text_of(paragraph)
        identifier = stable_identifier(title)
        if identifier:
            body_titles.setdefault(identifier, []).append(title)

    updated = 0
    unmatched: list[str] = []
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        style = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if not style or not is_index_style(style[0]) or len(text_nodes) != 2:
            continue
        title = text_nodes[0].text or ""
        old_page = text_nodes[1].text or ""
        # Newly inserted static entries may use an em dash until the first
        # provisional PDF is available. They must participate in that first
        # synchronisation just like entries carrying an older page number.
        if not old_page.isdigit() and old_page not in {"—", "A DEFINIR"}:
            continue
        needle = normalise(title)
        used_body_fallback = False
        forced_selection: str | None = None
        if title in TITLE_ALIASES:
            alias, forced_selection = TITLE_ALIASES[title]
            alias_needle = normalise(alias)
            hits = [
                physical_page
                for physical_page, page in enumerate(normalised_pages, start=1)
                if physical_page > page_offset and alias_needle in page
            ]
        else:
            hits = [
                physical_page
                for physical_page, page in enumerate(normalised_pages, start=1)
                if physical_page > page_offset and needle and needle in page
            ]
        if not hits:
            identifier = stable_identifier(title)
            candidates = body_titles.get(identifier or "", [])
            for candidate in candidates:
                candidate_needle = normalise(candidate)
                candidate_hits = [
                    physical_page
                    for physical_page, page in enumerate(normalised_pages, start=1)
                    if physical_page > page_offset
                    and candidate_needle
                    and candidate_needle in page
                ]
                if candidate_hits:
                    hits = candidate_hits
                    used_body_fallback = True
                    break
        if not hits:
            # The title page and Chapter 1 heading are visually present but are
            # not emitted as searchable PDF text; their existing page 1 is valid.
            unmatched.append(title)
            continue
        if forced_selection == "second":
            if len(hits) < 2:
                unmatched.append(title)
                continue
            physical_page = hits[1]
        elif forced_selection == "first":
            physical_page = min(hits)
        elif style[0].startswith(("ndiceAnexo", "ndicedoAnexo")) and not used_body_fallback:
            # A local annex index repeats the title before the body heading.
            # The first hit is therefore the local index itself and the second
            # hit is the section heading whose page must be reported.
            if len(hits) < 2:
                unmatched.append(title)
                continue
            physical_page = hits[1]
        else:
            physical_page = min(hits)
        printed_page = physical_page - page_offset
        if printed_page < 1:
            raise RuntimeError(f"Invalid printed page for {title!r}: {printed_page}")
        value = str(printed_page)
        if text_nodes[1].text != value:
            text_nodes[1].text = value
            updated += 1

    update_parameter_dictionary_widths(root)
    return (
        etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes"),
        updated,
        unmatched,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("pdf_text", type=Path, help="Output of pdftotext -layout")
    parser.add_argument("--page-offset", type=int, default=19)
    parser.add_argument(
        "--markdown",
        type=Path,
        help="Optional canonical Markdown whose table and figure lists should receive the same pages",
    )
    args = parser.parse_args()
    path = args.docx.resolve()
    with ZipFile(path, "r") as archive:
        document_xml = archive.read("word/document.xml")
    updated_xml, count, unmatched = apply(
        document_xml,
        args.pdf_text.read_text(encoding="utf-8", errors="replace"),
        args.page_offset,
    )

    fd, temporary = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    try:
        with ZipFile(path, "r") as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                data = updated_xml if item.filename == "word/document.xml" else source.read(item.filename)
                target.writestr(item, data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

    print(f"Updated index entries: {count}")
    print("Unmatched entries retained:")
    for title in unmatched:
        print(f"- {title}")
    if args.markdown is not None:
        markdown_count = synchronise_markdown(args.markdown.resolve(), updated_xml)
        print(f"Updated Markdown list entries: {markdown_count}")


if __name__ == "__main__":
    main()
