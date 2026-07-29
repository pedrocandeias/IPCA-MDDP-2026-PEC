#!/usr/bin/env python3
"""Sincroniza a estimativa dimensional teórica da P06 com o DOCX canónico."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_approved_questions_annex_d import import_fragment, replace_range
from integrate_annexes_bc import (
    NS,
    element_text,
    paragraph_style,
    replace_paragraph_text,
)


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
VERSION = "0.4.43"


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}"
        )
    return matches[0]


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
    replace_paragraph_text(matches[0], f"Versão do documento: {VERSION}")
    return 1


def update_table_index_entry(document: etree._Element) -> int:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph).startswith("ndice")
        and element_text(paragraph).startswith("Tabela D.3")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperada uma entrada de índice para a Tabela D.3; encontradas {len(matches)}"
        )
    text_nodes = matches[0].xpath(".//w:t", namespaces=NS)
    if len(text_nodes) < 2:
        raise RuntimeError("A entrada da Tabela D.3 não conserva título e página separados")
    text_nodes[0].text = (
        "Tabela D.3 — Cenário de estimativa dimensional teórica da palma no eixo X"
    )
    return 1


def apply(path: Path) -> int:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    elements = import_fragment(
        markdown,
        "### D.4.4 Comparação entre entrada, malha e peça física",
        "### D.4.5 Registo fotográfico dos protótipos",
        "p06_estimativa_dimensional_teorica",
        document,
        relationships,
        files,
    )
    replace_range(
        find_body_paragraph(
            document, "D.4.4 Comparação entre entrada, malha e peça física"
        ),
        find_body_paragraph(document, "D.4.5 Registo fotográfico dos protótipos"),
        elements,
    )
    update_version(document)
    update_table_index_entry(document)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return len(elements)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    count = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Elementos importados para D.4.4: {count}")


if __name__ == "__main__":
    main()
