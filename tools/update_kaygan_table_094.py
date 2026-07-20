#!/usr/bin/env python3
"""Alinha a Tabela 2.1 com os quatro papéis de Kaygan e Kaygan (2025)."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

CAPTION = "Tabela 2.1 — Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos"
OLD_TEXT = (
    "Esta posição intermédia do design torna-se mais clara perante a multiplicidade de papéis "
    "que os profissionais de saúde podem assumir nos processos de desenvolvimento. Em vez de "
    "contribuírem apenas como validadores de soluções, estes agentes podem ser intervenientes "
    "do seu sector, utilizadores peritos, mediadores entre domínios e profissionais clínicos "
    "ou investigadores, como sintetiza a Tabela 2.1."
)
OLD_MD = OLD_TEXT.replace("posição intermédia do design", "posição intermédia do *design*")
NEW_PARTS = (
    ("Esta posição intermédia do ", False),
    ("design", True),
    (
        " torna-se mais clara perante a multiplicidade de papéis que os profissionais de saúde "
        "podem assumir nos processos de desenvolvimento. Para além de validarem soluções, os "
        "profissionais de saúde podem participar como parceiros empresariais, utilizadores "
        "peritos, mediadores entre as áreas clínica e tecnológica, ou profissionais clínicos e "
        "investigadores, como sintetiza a Tabela 2.1.",
        False,
    ),
)
NEW_TEXT = "".join(value for value, _ in NEW_PARTS)
NEW_MD = "".join(f"*{value}*" if italic else value for value, italic in NEW_PARTS)

OLD_TABLE = """| Papel | Contributo no desenvolvimento | Domínio principal de decisão |

| --- | --- | --- |

| Utilizadores peritos | Fornecem experiência clínica situada e problemas de uso | Experiência do utilizador e adequação funcional |"""
NEW_TABLE = """| Papel | Contributo no desenvolvimento | Domínio principal de decisão |

| --- | --- | --- |

| Parceiros empresariais | Actuam como clientes ou defensores da equipa de *design*, identificam oportunidades, definem especificações e facilitam o acesso a outros intervenientes | Oportunidades de negócio, mercado, concorrência, regulamentação e certificação |

| Utilizadores peritos | Fornecem experiência clínica situada e problemas de uso | Experiência do utilizador e adequação funcional |"""

NEW_ROW_PARTS = (
    (("Parceiros empresariais", False),),
    (
        ("Actuam como clientes ou defensores da equipa de ", False),
        ("design", True),
        (
            ", identificam oportunidades, definem especificações e facilitam o acesso a "
            "outros intervenientes",
            False,
        ),
    ),
    (("Oportunidades de negócio, mercado, concorrência, regulamentação e certificação", False),),
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def add_run(paragraph: etree._Element, value: str, *, italic: bool) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_paragraph_content(
    paragraph: etree._Element, parts: tuple[tuple[str, bool], ...]
) -> None:
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


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


def update_docx(root: etree._Element) -> None:
    paragraphs = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD_TEXT
    ]
    if len(paragraphs) != 1:
        raise RuntimeError(f"Parágrafo introdutório inesperado: {len(paragraphs)} ocorrências")
    paragraph = paragraphs[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo introdutório contém uma estrutura sensível")
    replace_paragraph_content(paragraph, NEW_PARTS)

    captions = [
        candidate
        for candidate in root.xpath("//w:p", namespaces=NS)
        if text_of(candidate) == CAPTION
    ]
    if len(captions) != 1:
        raise RuntimeError(f"Legenda da Tabela 2.1 inesperada: {len(captions)} ocorrências")
    table = captions[0].getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("A Tabela 2.1 não sucede imediatamente à legenda")
    rows = table.xpath("./w:tr", namespaces=NS)
    if len(rows) != 4:
        raise RuntimeError(f"Estrutura inesperada da Tabela 2.1: {len(rows)} linhas")
    if text_of(rows[1]).startswith("Parceiros empresariais"):
        raise RuntimeError("A linha de parceiros empresariais já existe")

    new_row = deepcopy(rows[1])
    cells = new_row.xpath("./w:tc", namespaces=NS)
    if len(cells) != 3:
        raise RuntimeError(f"Número inesperado de células no modelo de linha: {len(cells)}")
    for cell, parts in zip(cells, NEW_ROW_PARTS, strict=True):
        cell_paragraphs = cell.xpath("./w:p", namespaces=NS)
        if not cell_paragraphs:
            raise RuntimeError("Célula sem parágrafo na linha-modelo")
        replace_paragraph_content(cell_paragraphs[0], parts)
        for extra in cell_paragraphs[1:]:
            cell.remove(extra)
    rows[0].addnext(new_row)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = {
        "Versão do documento: 0.4.93": 1,
        OLD_MD: 1,
        NEW_MD: 0,
        OLD_TABLE: 1,
        NEW_TABLE: 0,
    }
    for value, expected in checks.items():
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada para {value[:70]!r}: "
                f"{actual} != {expected}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.93", "Versão do documento: 0.4.94", 1
    )
    markdown = markdown.replace(OLD_MD, NEW_MD, 1)
    return markdown.replace(OLD_TABLE, NEW_TABLE, 1)


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
    update_docx(root)
    after = sensitive_state(root)
    expected = dict(before)
    expected["rows"] += 1
    expected["cells"] += 3
    if after != expected:
        raise RuntimeError(f"Estrutura alterada de forma inesperada: {before} -> {after}")
    body = text_of(root)
    if OLD_TEXT in body or body.count(NEW_TEXT) != 1:
        raise RuntimeError("O parágrafo corrigido não ficou íntegro no DOCX")
    if body.casefold().count("parceiros empresariais") != 2:
        raise RuntimeError("A designação do quarto papel não ficou presente no texto e na tabela")

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
        "Tabela 2.1 alinhada com os quatro papéis; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}, "
        f"linhas={before['rows']}->{after['rows']}"
    )


if __name__ == "__main__":
    main()
