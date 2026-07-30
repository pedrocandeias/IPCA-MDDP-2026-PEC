#!/usr/bin/env python3
"""Integrate Annexes B and C into the canonical Markdown and IPCA DOCX.

The annexes remain editable in ``anexos``.  This tool
mechanically appends their content to the consolidated Markdown, imports their
DOCX bodies into the formatted IPCA document, copies the Annex C figure, and
adds provisional static index entries.  Printed page numbers are synchronised
after PDF generation with ``tools/manutencao/synchronise_docx_pagination.py``.
"""

from __future__ import annotations

import argparse
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "r": R, "a": A, "wp": WP, "pic": PIC, "rel": REL}

ANNEX_B_MD = Path(
    "anexos/testes_plataforma/"
    "anexo_b_avaliacao_processo_interface_handfab.md"
)
ANNEX_B_DOCX = ANNEX_B_MD.with_suffix(".docx")
ANNEX_C_MD = Path(
    "anexos/adaptacao_parametrica_modelos/"
    "anexo_c_adaptacao_parametrica_modelos.md"
)
ANNEX_C_DOCX = ANNEX_C_MD.with_suffix(".docx")


def qn(namespace: str, name: str) -> str:
    return f"{{{namespace}}}{name}"


def element_text(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def replace_paragraph_text(paragraph: etree._Element, value: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if not nodes:
        run = etree.SubElement(paragraph, qn(W, "r"))
        node = etree.SubElement(run, qn(W, "t"))
        node.text = value
        return
    nodes[0].text = value
    for node in nodes[1:]:
        node.text = ""


def paragraph_style(paragraph: etree._Element) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return values[0] if values else ""


def ensure_ppr(paragraph: etree._Element) -> etree._Element:
    ppr = paragraph.find(qn(W, "pPr"))
    if ppr is None:
        ppr = etree.Element(qn(W, "pPr"))
        paragraph.insert(0, ppr)
    return ppr


def set_paragraph_style(paragraph: etree._Element, style: str) -> None:
    ppr = ensure_ppr(paragraph)
    old = ppr.find(qn(W, "pStyle"))
    if old is not None:
        ppr.remove(old)
    node = etree.Element(qn(W, "pStyle"))
    node.set(qn(W, "val"), style)
    ppr.insert(0, node)


def set_page_break_before(paragraph: etree._Element) -> None:
    ppr = ensure_ppr(paragraph)
    if ppr.find(qn(W, "pageBreakBefore")) is None:
        ppr.append(etree.Element(qn(W, "pageBreakBefore")))


def suppress_automatic_numbering(paragraph: etree._Element, level: int) -> None:
    ppr = ensure_ppr(paragraph)
    old = ppr.find(qn(W, "numPr"))
    if old is not None:
        ppr.remove(old)
    numpr = etree.SubElement(ppr, qn(W, "numPr"))
    ilvl = etree.SubElement(numpr, qn(W, "ilvl"))
    ilvl.set(qn(W, "val"), str(max(0, level - 1)))
    numid = etree.SubElement(numpr, qn(W, "numId"))
    numid.set(qn(W, "val"), "0")


def format_paragraph(paragraph: etree._Element, first_heading: bool = False) -> None:
    source_style = paragraph_style(paragraph)
    text = element_text(paragraph)
    style_map = {
        "Heading1": "TtulosPrembulo-IPCA",
        "Heading2": "Cabealho2",
        "Heading3": "Cabealho3",
        "Heading4": "Cabealho4",
        "ListBullet": "TextoNormal-IPCA",
        "ListNumber": "TextoNormal-IPCA",
        "CodeBlock": "TextoNormal-IPCA",
        "Quote": "TextoNormal-IPCA",
        "Normal": "TextoNormal-IPCA",
        "": "TextoNormal-IPCA",
    }
    if text.startswith(("Tabela B.", "Tabela C.", "Figura C.")):
        target_style = "Legenda"
    else:
        target_style = style_map.get(source_style, "TextoNormal-IPCA")
    set_paragraph_style(paragraph, target_style)
    if source_style.startswith("Heading"):
        level_text = source_style.removeprefix("Heading")
        suppress_automatic_numbering(paragraph, int(level_text) if level_text.isdigit() else 1)
    if first_heading:
        set_page_break_before(paragraph)
    if source_style == "CodeBlock":
        for run in paragraph.xpath(".//w:r", namespaces=NS):
            rpr = run.find(qn(W, "rPr"))
            if rpr is None:
                rpr = etree.Element(qn(W, "rPr"))
                run.insert(0, rpr)
            fonts = rpr.find(qn(W, "rFonts"))
            if fonts is None:
                fonts = etree.SubElement(rpr, qn(W, "rFonts"))
            for attribute in ("ascii", "hAnsi", "cs"):
                fonts.set(qn(W, attribute), "Liberation Mono")
            size = rpr.find(qn(W, "sz"))
            if size is None:
                size = etree.SubElement(rpr, qn(W, "sz"))
            size.set(qn(W, "val"), "18")


def format_table(table: etree._Element) -> None:
    tblpr = table.find(qn(W, "tblPr"))
    if tblpr is None:
        tblpr = etree.Element(qn(W, "tblPr"))
        table.insert(0, tblpr)
    old_style = tblpr.find(qn(W, "tblStyle"))
    if old_style is not None:
        tblpr.remove(old_style)
    style = etree.Element(qn(W, "tblStyle"))
    style.set(qn(W, "val"), "Tabelacomgrelha")
    tblpr.insert(0, style)

    rows = table.findall(qn(W, "tr"))
    for index, row in enumerate(rows):
        trpr = row.find(qn(W, "trPr"))
        if trpr is None:
            trpr = etree.Element(qn(W, "trPr"))
            row.insert(0, trpr)
        if trpr.find(qn(W, "cantSplit")) is None:
            trpr.append(etree.Element(qn(W, "cantSplit")))
        if index == 0 and trpr.find(qn(W, "tblHeader")) is None:
            trpr.append(etree.Element(qn(W, "tblHeader")))
        for paragraph in row.xpath(".//w:p", namespaces=NS):
            set_paragraph_style(paragraph, "TextoNormal-IPCA")
            for run in paragraph.xpath(".//w:r", namespaces=NS):
                rpr = run.find(qn(W, "rPr"))
                if rpr is None:
                    rpr = etree.Element(qn(W, "rPr"))
                    run.insert(0, rpr)
                size = rpr.find(qn(W, "sz"))
                if size is None:
                    size = etree.SubElement(rpr, qn(W, "sz"))
                size.set(qn(W, "val"), "16")
                size_cs = rpr.find(qn(W, "szCs"))
                if size_cs is None:
                    size_cs = etree.SubElement(rpr, qn(W, "szCs"))
                size_cs.set(qn(W, "val"), "16")
                if index == 0 and rpr.find(qn(W, "b")) is None:
                    rpr.append(etree.Element(qn(W, "b")))


def next_relationship_id(rels: etree._Element) -> str:
    values = []
    for relationship in rels:
        match = re.fullmatch(r"rId(\d+)", relationship.get("Id", ""))
        if match:
            values.append(int(match.group(1)))
    return f"rId{max(values, default=0) + 1}"


def next_drawing_id(document: etree._Element) -> int:
    values: list[int] = []
    for value in document.xpath("//wp:docPr/@id | //pic:cNvPr/@id", namespaces=NS):
        if str(value).isdigit():
            values.append(int(value))
    return max(values, default=0) + 1


def import_annex(
    source_path: Path,
    target_document: etree._Element,
    target_rels: etree._Element,
    target_files: dict[str, bytes],
    media_prefix: str,
) -> tuple[list[etree._Element], list[tuple[str, int]], list[str], list[str]]:
    with ZipFile(source_path) as source:
        source_document = etree.fromstring(source.read("word/document.xml"))
        source_rels = etree.fromstring(source.read("word/_rels/document.xml.rels"))
        relationship_by_id = {item.get("Id"): item for item in source_rels}
        body = source_document.find(".//w:body", NS)
        if body is None:
            raise RuntimeError(f"No document body in {source_path}")

        imported: list[etree._Element] = []
        headings: list[tuple[str, int]] = []
        tables: list[str] = []
        figures: list[str] = []
        first_heading = True
        relationship_map: dict[str, str] = {}

        for child in body:
            if child.tag == qn(W, "sectPr"):
                continue
            clone = deepcopy(child)
            if clone.tag == qn(W, "p"):
                original_style = paragraph_style(clone)
                title = element_text(clone)
                if original_style.startswith("Heading"):
                    level = int(original_style.removeprefix("Heading"))
                    headings.append((title, level))
                if title.startswith(("Tabela B.", "Tabela C.")):
                    tables.append(title)
                if title.startswith("Figura C."):
                    figures.append(title)
                format_paragraph(clone, first_heading and original_style == "Heading1")
                if original_style == "Heading1":
                    first_heading = False
            elif clone.tag == qn(W, "tbl"):
                format_table(clone)

            for blip in clone.xpath(".//a:blip[@r:embed]", namespaces=NS):
                source_id = blip.get(qn(R, "embed"))
                if source_id not in relationship_map:
                    relationship = relationship_by_id.get(source_id)
                    if relationship is None:
                        raise RuntimeError(f"Missing relationship {source_id} in {source_path}")
                    target_id = next_relationship_id(target_rels)
                    source_target = PurePosixPath(relationship.get("Target", ""))
                    source_member = str(PurePosixPath("word") / source_target)
                    extension = source_target.suffix or ".bin"
                    target_member = (
                        f"word/media/{media_prefix}_{len(relationship_map) + 1}{extension}"
                    )
                    target_files[target_member] = source.read(source_member)
                    new_rel = etree.SubElement(target_rels, qn(REL, "Relationship"))
                    new_rel.set("Id", target_id)
                    new_rel.set("Type", relationship.get("Type"))
                    new_rel.set("Target", str(PurePosixPath(target_member).relative_to("word")))
                    relationship_map[source_id] = target_id
                blip.set(qn(R, "embed"), relationship_map[source_id])

            for node in clone.xpath(".//wp:docPr | .//pic:cNvPr", namespaces=NS):
                drawing_id = next_drawing_id(target_document)
                node.set("id", str(drawing_id))
            imported.append(clone)

    return imported, headings, tables, figures


def find_static_entry(root: etree._Element, prefix: str) -> etree._Element:
    matches = []
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        style = paragraph_style(paragraph)
        nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if style.startswith("ndice") and nodes and (nodes[0].text or "").startswith(prefix):
            matches.append(paragraph)
    if len(matches) != 1:
        raise RuntimeError(f"Expected one static entry beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def make_static_entry(template: etree._Element, title: str, page: str = "125") -> etree._Element:
    entry = deepcopy(template)
    nodes = entry.xpath(".//w:t", namespaces=NS)
    if len(nodes) < 2:
        raise RuntimeError("Static index template does not contain title and page runs")
    nodes[0].text = title
    nodes[1].text = page
    for extra in nodes[2:]:
        extra.text = ""
    return entry


def insert_static_entries(
    root: etree._Element,
    headings: list[tuple[str, int]],
    tables: list[str],
    figures: list[str],
) -> None:
    heading_anchor = find_static_entry(root, "A.10.3.3 Pertinência directa")
    heading_templates = {
        level: next(
            paragraph
            for paragraph in root.xpath("//w:body/w:p", namespaces=NS)
            if paragraph_style(paragraph) == f"ndice{level}"
            and len(paragraph.xpath(".//w:t", namespaces=NS)) >= 2
        )
        for level in (1, 2, 3, 4)
    }
    for title, level in headings:
        entry = make_static_entry(heading_templates[min(level, 4)], title)
        heading_anchor.addnext(entry)
        heading_anchor = entry

    table_anchor = find_static_entry(root, "Tabela 8.7")
    for title in tables:
        entry = make_static_entry(table_anchor, title)
        table_anchor.addnext(entry)
        table_anchor = entry

    figure_anchor = find_static_entry(root, "Figura 8.4")
    for title in figures:
        entry = make_static_entry(figure_anchor, title)
        figure_anchor.addnext(entry)
        figure_anchor = entry


def integrate_docx(target_path: Path, annex_b: Path, annex_c: Path) -> None:
    original_mode = target_path.stat().st_mode
    with ZipFile(target_path) as target:
        files = {item.filename: target.read(item.filename) for item in target.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    if any(
        element_text(paragraph).startswith(("Anexo B —", "Anexo C —"))
        and paragraph_style(paragraph) == "TtulosPrembulo-IPCA"
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        raise RuntimeError("The target DOCX already contains Annex B or Annex C")
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])

    version_paragraphs = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph).startswith("Versão do documento:")
    ]
    if len(version_paragraphs) > 1:
        raise RuntimeError("More than one manuscript version paragraph was found")
    if version_paragraphs:
        replace_paragraph_text(version_paragraphs[0], "Versão do documento: 0.4.38")

    imported_b, headings_b, tables_b, figures_b = import_annex(
        annex_b, document, relationships, files, "annex_b_image"
    )
    imported_c, headings_c, tables_c, figures_c = import_annex(
        annex_c, document, relationships, files, "annex_c_figure_c1"
    )
    insert_static_entries(
        document,
        headings_b + headings_c,
        tables_b + tables_c,
        figures_b + figures_c,
    )

    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("Target document has no body")
    sectpr = body.find(qn(W, "sectPr"))
    if sectpr is None:
        raise RuntimeError("Target document has no final section properties")
    position = body.index(sectpr)
    for element in imported_b + imported_c:
        body.insert(position, element)
        position += 1

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=target_path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(target_path)
        os.chmod(target_path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


def caption_row(caption: str) -> str:
    identification, description = caption.split(" — ", 1)
    return f"| {identification} | {description} | — |"


def integrate_markdown(main_path: Path, annex_b: Path, annex_c: Path) -> None:
    text = main_path.read_text(encoding="utf-8")
    if "# Anexo B —" in text or "# Anexo C —" in text:
        raise RuntimeError("The consolidated Markdown already contains Annex B or Annex C")
    text = re.sub(
        r"Versão do documento:\s*\d+\.\d+\.\d+",
        "Versão do documento: 0.4.38",
        text,
        count=1,
    )
    b_text = annex_b.read_text(encoding="utf-8").strip()
    c_text = annex_c.read_text(encoding="utf-8").strip().replace(
        "](../../../../figuras/figura_c1_fluxo_adaptacao_parametrica.png)",
        "](figuras/figura_c1_fluxo_adaptacao_parametrica.png)",
    )

    table_captions = re.findall(r"^(Tabela [BC]\.\d+ — .+)$", b_text + "\n" + c_text, re.M)
    figure_captions = re.findall(r"^(Figura [BC]\.\d+ — .+)$", b_text + "\n" + c_text, re.M)
    table_rows = "\n".join(caption_row(value) for value in table_captions)
    figure_rows = "\n".join(caption_row(value) for value in figure_captions)
    text = text.replace(
        "| Tabela 8.7 | Rácio adimensional da maior dimensão da palma exportada face ao valor de referência | 94 |",
        "| Tabela 8.7 | Rácio adimensional da maior dimensão da palma exportada face ao valor de referência | 94 |\n"
        + table_rows,
        1,
    )
    text = text.replace(
        "| Figura 8.4 | Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior. | 90 |",
        "| Figura 8.4 | Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior. | 90 |\n"
        + figure_rows,
        1,
    )
    text = text.rstrip() + "\n\n" + b_text + "\n\n" + c_text + "\n"
    main_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", required=True, type=Path)
    parser.add_argument("--docx", required=True, type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    markdown = (root / args.markdown).resolve()
    docx = (root / args.docx).resolve()
    annex_b_md = root / ANNEX_B_MD
    annex_c_md = root / ANNEX_C_MD
    annex_b_docx = root / ANNEX_B_DOCX
    annex_c_docx = root / ANNEX_C_DOCX
    for path in (markdown, docx, annex_b_md, annex_c_md, annex_b_docx, annex_c_docx):
        if not path.exists():
            raise SystemExit(f"Required file not found: {path}")

    integrate_markdown(markdown, annex_b_md, annex_c_md)
    integrate_docx(docx, annex_b_docx, annex_c_docx)
    print(f"Updated Markdown: {markdown}")
    print(f"Updated DOCX: {docx}")


if __name__ == "__main__":
    main()
