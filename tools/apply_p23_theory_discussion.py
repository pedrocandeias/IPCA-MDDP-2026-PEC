#!/usr/bin/env python3
"""Fecha a P23 no DOCX institucional e sincroniza as Secções 2.8 e 8.4."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_approved_questions_annex_d import import_fragment, replace_range
from integrate_annexes_bc import (
    NS,
    W,
    element_text,
    make_static_entry,
    paragraph_style,
    qn,
    replace_paragraph_text,
)


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"

FRAGMENTS = (
    (
        "### 2.8 Análise crítica do estado da arte e lacunas identificadas",
        "## Capítulo 3 — Metodologia de Investigação",
        "2.8 Análise crítica do estado da arte e lacunas identificadas",
        "Capítulo 3 — Metodologia de Investigação",
        "p23_chapter2",
    ),
    (
        "### 8.4 Discussão dos resultados face aos objectivos",
        "## Capítulo 9 — Conclusões e Trabalhos Futuros",
        "8.4 Discussão dos resultados face aos objectivos",
        "Capítulo 9 — Conclusões e Trabalhos Futuros",
        "p23_chapter8",
    ),
)

TABLE_ENTRIES = (
    (
        "Tabela 2.2",
        "Tabela 2.3 — Correspondência entre lacunas do estado da arte, resposta da investigação e limites de avaliação",
    ),
    (
        "Tabela 8.7",
        "Tabela 8.8 — Discussão dos resultados face às lacunas seleccionadas do estado da arte",
    ),
)


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}")
    return matches[0]


def find_index_entry(document: etree._Element, prefix: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph).startswith("ndice")
        and element_text(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperada uma entrada de índice {prefix!r}; encontradas {len(matches)}")
    return matches[0]


def add_table_entry(document: etree._Element, anchor_prefix: str, title: str) -> bool:
    prefix = title.split(" — ", 1)[0]
    existing = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph).startswith("ndice")
        and element_text(paragraph).startswith(prefix)
    ]
    if existing:
        if len(existing) != 1:
            raise RuntimeError(f"Entradas duplicadas na lista de tabelas: {prefix}")
        return False
    anchor = find_index_entry(document, anchor_prefix)
    entry = make_static_entry(anchor, title, "—")
    anchor.addnext(entry)
    return True


def update_version(document: etree._Element) -> int:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph).startswith("Versão do documento:")
    ]
    if not matches:
        return 0
    if len(matches) != 1:
        raise RuntimeError(f"Esperada uma linha de versão; encontradas {len(matches)}")
    replace_paragraph_text(matches[0], "Versão do documento: 0.4.42")
    return 1


def apply(path: Path) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    imported = 0
    for md_start, md_end, docx_start, docx_end, label in FRAGMENTS:
        elements = import_fragment(
            markdown,
            md_start,
            md_end,
            label,
            document,
            relationships,
            files,
        )
        replace_range(
            find_body_paragraph(document, docx_start),
            find_body_paragraph(document, docx_end),
            elements,
        )
        imported += len(elements)

    entries_added = sum(
        int(add_table_entry(document, anchor, title))
        for anchor, title in TABLE_ENTRIES
    )
    version_lines = update_version(document)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temp_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return {
        "elements": imported,
        "table_entries": entries_added,
        "version_lines": version_lines,
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    result = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Elementos importados: {result['elements']}")
    print(f"Entradas de tabelas acrescentadas: {result['table_entries']}")
    print(f"Linhas de versão actualizadas no DOCX: {result['version_lines']}")


if __name__ == "__main__":
    main()
