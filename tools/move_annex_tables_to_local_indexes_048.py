#!/usr/bin/env python3
"""Move Annex B–D table entries from the general list to local annex indexes."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

ANNEX_TABLES = {
    "B": [f"Tabela B.{number}" for number in range(1, 6)],
    "C": [f"Tabela C.{number}" for number in range(1, 5)],
    "D": [f"Tabela D.{number}" for number in range(1, 4)],
}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def style_of(paragraph: etree._Element) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return values[0] if values else ""


def set_style(paragraph: etree._Element, style_id: str) -> None:
    ppr = paragraph.find(qn("pPr"))
    if ppr is None:
        ppr = etree.Element(qn("pPr"))
        paragraph.insert(0, ppr)
    style = ppr.find(qn("pStyle"))
    if style is None:
        style = etree.Element(qn("pStyle"))
        ppr.insert(0, style)
    style.set(qn("val"), style_id)


def body_caption(body: etree._Element, identifier: str) -> str:
    matches = [
        paragraph
        for paragraph in body.findall(qn("p"))
        if not style_of(paragraph).startswith("ndice")
        and text_of(paragraph).startswith(f"{identifier} —")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperada uma legenda no corpo para {identifier}; encontradas: {len(matches)}"
        )
    return text_of(matches[0])


def general_entry(body: etree._Element, identifier: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in body.findall(qn("p"))
        if style_of(paragraph).startswith("ndice")
        and not style_of(paragraph).startswith("ndiceAnexo")
        and text_of(paragraph).startswith(f"{identifier} —")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperada uma entrada geral para {identifier}; encontradas: {len(matches)}"
        )
    return matches[0]


def prepare_entry(
    body: etree._Element,
    paragraph: etree._Element,
    identifier: str,
) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if len(nodes) != 2:
        raise RuntimeError(
            f"A entrada de {identifier} não possui os dois campos esperados"
        )
    nodes[0].text = body_caption(body, identifier)
    nodes[1].text = "—"
    set_style(paragraph, "ndiceAnexo2")


def local_index_end(body: etree._Element, letter: str) -> int:
    titles = [
        paragraph
        for paragraph in body.findall(qn("p"))
        if text_of(paragraph) == f"Índice do Anexo {letter}"
    ]
    if len(titles) != 1:
        raise RuntimeError(
            f"Esperado um índice local para o Anexo {letter}; encontrados: {len(titles)}"
        )
    position = body.index(titles[0]) + 1
    while position < len(body):
        element = body[position]
        if element.tag != qn("p") or not style_of(element).startswith("ndiceAnexo"):
            break
        position += 1
    return position


def apply(path: Path) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path, "r") as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    parser = etree.XMLParser(remove_blank_text=False)
    document = etree.fromstring(files["word/document.xml"], parser)
    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("O DOCX não contém corpo de documento")

    moved: dict[str, int] = {}
    for letter, identifiers in ANNEX_TABLES.items():
        entries: list[etree._Element] = []
        for identifier in identifiers:
            entry = general_entry(body, identifier)
            prepare_entry(body, entry, identifier)
            body.remove(entry)
            entries.append(entry)

        position = local_index_end(body, letter)
        for entry in entries:
            body.insert(position, entry)
            position += 1
        moved[letter] = len(entries)

    files["word/document.xml"] = etree.tostring(
        document,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in items:
                target.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return moved


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    target = root / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
    result = apply(target)
    for annex, count in result.items():
        print(f"Anexo {annex}: {count} entradas transferidas")
