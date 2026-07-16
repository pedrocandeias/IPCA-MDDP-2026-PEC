#!/usr/bin/env python3
"""Integra as alternativas portuguesas para «projectual» no manuscrito 0.4.57."""

from __future__ import annotations

import os
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


REPLACEMENTS = [
    ("Versão do documento: 0.4.56", "Versão do documento: 0.4.57"),
    ("processo de investigação projectual", "processo de investigação através do projecto"),
    ("mediação projectual", "mediação no desenvolvimento do projecto"),
    ("mantendo a acessibilidade e o controlo projectual?", "mantendo a acessibilidade e o controlo sobre as decisões de projecto?"),
    ("mecanismos projectuais", "mecanismos de projecto"),
    ("decisões projectuais", "decisões de projecto"),
    ("articuladas com a decisão projectual", "articuladas com a decisão de projecto"),
    ("processo projectual", "processo de projecto"),
    ("instrumento projectual", "instrumento ao serviço do projecto"),
    ("formulação projectual", "formulação do projecto"),
    ("acessibilidade e controlo projectual", "acessibilidade e controlo sobre o projecto"),
    ("evolução projectual", "evolução do projecto"),
    ("domínio técnico e projectual", "domínio técnico e de desenvolvimento do projecto"),
    ("técnico-projectual", "técnico e de projecto"),
    ("percurso projectual", "percurso de projecto"),
    ("argumentação projectual", "argumentação do projecto"),
    ("pertinência projectual", "pertinência para o projecto"),
    ("compromisso projectual", "compromisso de projecto"),
    ("actividade de adaptação projectual controlada", "actividade controlada de adaptação do projecto"),
    ("especificação projectual", "especificação de projecto"),
    ("constitui uma decisão projectual observável", "constitui uma decisão de projecto observável"),
    ("a diferença entre parâmetro e caixa exterior descreve a transformação projectual", "a diferença entre parâmetro e caixa exterior descreve a transformação decorrente do projecto"),
    ("constituem respostas projectuais concretas", "constituem respostas concretas ao problema de projecto"),
    ("constituem efeitos projectuais potenciais", "constituem efeitos potencialmente decorrentes das decisões de projecto"),
    ("conhecimento projectual surgiu", "conhecimento sobre o projecto surgiu"),
    ("conhecimento projectual documentado", "conhecimento de projecto documentado"),
    ("mecanismos orientados para ajuste, acessibilidade do processo e controlo projectual", "mecanismos orientados para o ajuste, a acessibilidade do processo e o controlo das decisões de projecto"),
    ("O contributo projectual é", "O contributo no domínio do projecto é"),
    ("actividade projectual", "actividade de projecto"),
    ("A decisão projectual resultante", "A decisão de projecto resultante"),
    ("trabalho projectual", "trabalho de projecto"),
    ("O contributo é projectual e técnico", "O contributo é técnico e de projecto"),
    ("a diferença entre entrada e malha descreve a transformação projectual", "a diferença entre entrada e malha descreve a transformação resultante do projecto"),
]


TARGET = re.compile(r"\bprojectuais?\b", re.IGNORECASE)


def replace_in_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        occurrences = text.count(old)
        if occurrences:
            text = text.replace(old, new)
            count += occurrences
    return text, count


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
    original = MARKDOWN.read_text(encoding="utf-8")
    updated, count = replace_in_text(original)
    remaining = TARGET.findall(updated)
    if remaining:
        raise RuntimeError(f"Termos ainda presentes no Markdown: {remaining}")
    MARKDOWN.write_text(updated, encoding="utf-8")
    return count


def update_docx() -> int:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])
    count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        for old, new in REPLACEMENTS:
            count += replace_in_element(paragraph, old, new)

    full_text = "".join(document.xpath("//w:t/text()", namespaces=NS))
    remaining = TARGET.findall(full_text)
    if remaining:
        raise RuntimeError(f"Termos ainda presentes no DOCX: {remaining}")

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
    markdown_changes = update_markdown()
    docx_changes = update_docx()
    print(f"Markdown: {markdown_changes} substituições")
    print(f"DOCX: {docx_changes} substituições")


if __name__ == "__main__":
    main()
