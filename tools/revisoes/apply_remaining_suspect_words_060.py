#!/usr/bin/env python3
"""Substitui as três formas lexicais restantes na versão 0.4.60."""

from __future__ import annotations

import os
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}

MARKDOWN_REPLACEMENTS = [
    ("Versão do documento: 0.4.59", "Versão do documento: 0.4.60"),
    ("prática investigativa", "prática de investigação"),
    (
        "reforçando a integração formal de avaliações formativas, realizadas durante o desenvolvimento para orientar melhorias, e de avaliações sumativas, destinadas a verificar o resultado final",
        "reforçando a integração formal de avaliações formativas, realizadas durante o desenvolvimento para orientar melhorias, e de avaliações finais de validação, destinadas a verificar o resultado do processo",
    ),
    (
        "todas as exportações concluídas produziram ficheiros binariamente idênticos e conservaram as mesmas dimensões e métricas geométricas",
        "todas as exportações concluídas produziram ficheiros exactamente iguais ao nível dos dados binários, isto é, com a mesma sequência de zeros e uns que constitui o seu conteúdo digital, e conservaram as mesmas dimensões e métricas geométricas",
    ),
]

DOCX_REPLACEMENTS = MARKDOWN_REPLACEMENTS[1:]
TARGETS = re.compile(r"\b(?:binariamente|investigativa|sumativas)\b", re.IGNORECASE)


def replace_in_element(element: etree._Element, old: str, new: str) -> int:
    count = 0
    while True:
        nodes = element.xpath(".//w:t", namespaces=NS)
        full_text = "".join(node.text or "" for node in nodes)
        start = full_text.find(old)
        if start < 0:
            return count
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
        count += 1


def update_markdown() -> int:
    text = MARKDOWN.read_text(encoding="utf-8")
    if "Versão do documento: 0.4.60" in text and not TARGETS.search(text):
        return 0
    count = 0
    for old, new in MARKDOWN_REPLACEMENTS:
        occurrences = text.count(old)
        text = text.replace(old, new)
        count += occurrences
    if count != 5:
        raise RuntimeError(f"Esperavam-se cinco substituições no Markdown; foram feitas {count}")
    if TARGETS.search(text) or text.count("Versão do documento: 0.4.60") != 1:
        raise RuntimeError("A validação final do Markdown falhou")
    MARKDOWN.write_text(text, encoding="utf-8")
    return count


def update_docx() -> int:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}
    document = etree.fromstring(files["word/document.xml"])
    count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        for old, new in DOCX_REPLACEMENTS:
            count += replace_in_element(paragraph, old, new)
    full_text = "".join(document.xpath("//w:t/text()", namespaces=NS))
    if count != 5 or TARGETS.search(full_text):
        raise RuntimeError(f"A validação do DOCX falhou após {count} substituições")
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, DOCX)
    return count


def main() -> None:
    print(f"Markdown: {update_markdown()} substituições")
    print(f"DOCX: {update_docx()} substituições")


if __name__ == "__main__":
    main()
