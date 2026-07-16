#!/usr/bin/env python3
"""Substitui «protesistas» por «técnicos de ortoprotesia» na versão 0.4.59."""

from __future__ import annotations

import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}

OLD = "médicos, protesistas, terapeutas"
NEW = "médicos, técnicos de ortoprotesia, terapeutas"


def replace_in_paragraph(paragraph: etree._Element, old: str, new: str) -> int:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    full_text = "".join(node.text or "" for node in nodes)
    start = full_text.find(old)
    if start < 0:
        return 0
    end = start + len(old)
    offset = 0
    inserted = False
    for node in nodes:
        value = node.text or ""
        node_start, node_end = offset, offset + len(value)
        overlap_start = max(start, node_start)
        overlap_end = min(end, node_end)
        if overlap_start < overlap_end:
            local_start = overlap_start - node_start
            local_end = overlap_end - node_start
            prefix = value[:local_start]
            suffix = value[local_end:]
            if not inserted:
                node.text = prefix + new + suffix
                inserted = True
            else:
                node.text = prefix + suffix
            if node.text.startswith(" ") or node.text.endswith(" "):
                node.set(f"{{{XML}}}space", "preserve")
        offset = node_end
    return 1


def update_markdown() -> None:
    text = MARKDOWN.read_text(encoding="utf-8")
    if text.count(OLD) != 1:
        raise RuntimeError("A expressão inicial não ocorre exactamente uma vez no Markdown")
    text = text.replace("Versão do documento: 0.4.58", "Versão do documento: 0.4.59")
    text = text.replace(OLD, NEW)
    if "protesistas" in text or text.count(NEW) != 1:
        raise RuntimeError("A substituição não ficou estável no Markdown")
    MARKDOWN.write_text(text, encoding="utf-8")


def update_docx() -> None:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}
    document = etree.fromstring(files["word/document.xml"])
    count = sum(
        replace_in_paragraph(paragraph, OLD, NEW)
        for paragraph in document.xpath("//w:p", namespaces=NS)
    )
    full_text = "".join(document.xpath("//w:t/text()", namespaces=NS))
    if count != 1 or "protesistas" in full_text or full_text.count(NEW) != 1:
        raise RuntimeError("A substituição não ficou estável no DOCX")
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, DOCX)


def main() -> None:
    update_markdown()
    update_docx()
    print("Substituição concluída no Markdown e no DOCX")


if __name__ == "__main__":
    main()
