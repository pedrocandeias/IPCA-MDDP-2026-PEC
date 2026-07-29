#!/usr/bin/env python3
"""Aumenta para 13 pt o corpo tipográfico da Tabela 2.1."""

from __future__ import annotations

import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
CAPTION = "Tabela 2.1 — Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos"
FONT_HALF_POINTS = "26"


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
        "rows": int(root.xpath("count(//w:tr)", namespaces=NS)),
        "cells": int(root.xpath("count(//w:tc)", namespaces=NS)),
    }


def set_font_size(run: etree._Element) -> None:
    properties = run.find(qn("rPr"))
    if properties is None:
        properties = etree.Element(qn("rPr"))
        run.insert(0, properties)
    for name in ("sz", "szCs"):
        node = properties.find(qn(name))
        if node is None:
            node = etree.SubElement(properties, qn(name))
        node.set(qn("val"), FONT_HALF_POINTS)


def update_table(root: etree._Element) -> int:
    captions = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == CAPTION
    ]
    if len(captions) != 1:
        raise RuntimeError(f"Legenda da Tabela 2.1 inesperada: {len(captions)} ocorrências")
    table = captions[0].getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("A Tabela 2.1 não sucede imediatamente à legenda")
    rows = table.xpath("./w:tr", namespaces=NS)
    if len(rows) != 5:
        raise RuntimeError(f"Estrutura inesperada da Tabela 2.1: {len(rows)} linhas")
    runs = table.xpath(".//w:r[w:t]", namespaces=NS)
    if len(runs) != 17:
        raise RuntimeError(f"Número inesperado de segmentos de texto: {len(runs)}")
    for run in runs:
        set_font_size(run)
    return len(runs)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    old = "Versão do documento: 0.4.94"
    new = "Versão do documento: 0.4.95"
    if markdown.count(old) != 1 or new in markdown:
        raise RuntimeError("Versão Markdown inesperada")
    return markdown.replace(old, new, 1)


def main() -> None:
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    before = sensitive_state(root)
    updated_runs = update_table(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        f"Tabela 2.1 actualizada para 13 pt em {updated_runs} segmentos; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
