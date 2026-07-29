#!/usr/bin/env python3
"""Insere uma linha vazia estrutural em torno dos elementos principais do DOCX."""

from __future__ import annotations

import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def style_of(paragraph: etree._Element) -> str:
    node = paragraph.find("./w:pPr/w:pStyle", NS)
    return node.get(qn("val")) if node is not None else ""


def is_blank(element: etree._Element | None) -> bool:
    if element is None or element.tag != qn("p") or text_of(element):
        return False
    return not element.xpath(
        ".//w:drawing | .//w:object | .//w:pict | .//w:br[@w:type='page']",
        namespaces=NS,
    )


def empty_paragraph(*, keep_with_next: bool = False) -> etree._Element:
    paragraph = etree.Element(qn("p"))
    properties = etree.SubElement(paragraph, qn("pPr"))
    etree.SubElement(properties, qn("pStyle")).set(qn("val"), "TextoNormal-IPCA")
    if keep_with_next:
        etree.SubElement(properties, qn("keepNext"))
    etree.SubElement(paragraph, qn("r"))
    return paragraph


def ensure_keep_with_next(paragraph: etree._Element) -> bool:
    properties = paragraph.find(qn("pPr"))
    if properties is None:
        properties = etree.Element(qn("pPr"))
        paragraph.insert(0, properties)
    if properties.find(qn("keepNext")) is None:
        etree.SubElement(properties, qn("keepNext"))
        return True
    return False


def ensure_before(element: etree._Element, *, keep_with_next: bool) -> bool:
    previous = element.getprevious()
    if is_blank(previous):
        if keep_with_next:
            ensure_keep_with_next(previous)
        return False
    element.addprevious(empty_paragraph(keep_with_next=keep_with_next))
    return True


def ensure_after(element: etree._Element, *, keep_with_next: bool) -> bool:
    following = element.getnext()
    if is_blank(following):
        if keep_with_next:
            ensure_keep_with_next(following)
        return False
    element.addnext(empty_paragraph(keep_with_next=keep_with_next))
    return True


def is_source_or_note(paragraph: etree._Element | None) -> bool:
    if paragraph is None or paragraph.tag != qn("p") or is_blank(paragraph):
        return False
    value = text_of(paragraph).casefold()
    if style_of(paragraph) == "Nota-IPCA":
        return True
    return value.startswith(
        (
            "adaptado ",
            "reproduzido ",
            "fonte:",
            "nota:",
            "produção própria",
            "elaboração própria",
        )
    )


def last_note_after(element: etree._Element) -> etree._Element:
    last = element
    following = last.getnext()
    while is_source_or_note(following):
        last = following
        following = last.getnext()
    return last


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
    }


def main() -> None:
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
    body = root.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("Corpo do documento não localizado")
    original_children = list(body)
    starts = [
        element
        for element in original_children
        if element.tag == qn("p") and text_of(element) == "Capítulo 1 — Introdução"
    ]
    if len(starts) != 1:
        raise RuntimeError(f"Início do corpo inesperado: {len(starts)} ocorrências")
    start_index = original_children.index(starts[0])
    scoped = original_children[start_index:]

    inserted = {
        "after_heading": 0,
        "before_figure": 0,
        "after_figure": 0,
        "before_table_title": 0,
        "after_table": 0,
        "keep_with_next": 0,
    }

    # Títulos do corpo e dos anexos. A bibliografia é deliberadamente excluída.
    for element in scoped:
        if element.tag != qn("p") or not text_of(element):
            continue
        style = style_of(element)
        value = text_of(element)
        is_heading = style in {"Heading1", "Heading2", "Heading3", "Heading4"}
        is_annex_title = style == "TtulosPrembulo-IPCA" and value.startswith("Anexo ")
        if (is_heading or is_annex_title) and value != "Referências Bibliográficas":
            inserted["keep_with_next"] += int(ensure_keep_with_next(element))
            inserted["after_heading"] += int(
                ensure_after(element, keep_with_next=True)
            )

    # Imagens guardadas em parágrafos e a montagem da Figura 5.8 guardada numa tabela.
    for element in scoped:
        is_drawing_paragraph = element.tag == qn("p") and bool(
            element.xpath(".//w:drawing", namespaces=NS)
        )
        is_drawing_table = element.tag == qn("tbl") and bool(
            element.xpath(".//w:drawing", namespaces=NS)
        )
        if is_drawing_paragraph or is_drawing_table:
            inserted["before_figure"] += int(
                ensure_before(element, keep_with_next=True)
            )
            if is_drawing_paragraph:
                inserted["keep_with_next"] += int(ensure_keep_with_next(element))
            else:
                table_paragraphs = element.xpath(".//w:p", namespaces=NS)
                if table_paragraphs:
                    inserted["keep_with_next"] += int(
                        ensure_keep_with_next(table_paragraphs[-1])
                    )

    # Legenda e eventual fonte constituem um único bloco gráfico.
    for element in scoped:
        if (
            element.tag == qn("p")
            and style_of(element) == "Caption"
            and text_of(element).startswith("Figura ")
        ):
            last = last_note_after(element)
            current = element
            while current is not last:
                inserted["keep_with_next"] += int(ensure_keep_with_next(current))
                current = current.getnext()
            inserted["after_figure"] += int(ensure_after(last, keep_with_next=False))

    # O título da tabela fica ligado à tabela por uma linha vazia com keepNext.
    for element in scoped:
        if (
            element.tag == qn("p")
            and style_of(element) == "Caption"
            and text_of(element).startswith("Tabela ")
        ):
            inserted["keep_with_next"] += int(ensure_keep_with_next(element))
            inserted["before_table_title"] += int(
                ensure_before(element, keep_with_next=True)
            )

    # As tabelas de dados recebem uma linha depois da tabela ou da respectiva nota.
    # A tabela com imagens da Figura 5.8 é tratada como figura, não como tabela de dados.
    for element in scoped:
        if element.tag != qn("tbl") or element.xpath(".//w:drawing", namespaces=NS):
            continue
        last = last_note_after(element)
        if last is not element:
            table_paragraphs = element.xpath(".//w:p", namespaces=NS)
            if table_paragraphs:
                inserted["keep_with_next"] += int(
                    ensure_keep_with_next(table_paragraphs[-1])
                )
            current = element.getnext()
            while current is not last:
                inserted["keep_with_next"] += int(ensure_keep_with_next(current))
                current = current.getnext()
        inserted["after_table"] += int(ensure_after(last, keep_with_next=False))

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
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    total_lines = sum(
        value for key, value in inserted.items() if key != "keep_with_next"
    )
    print(f"Linhas vazias inseridas: {total_lines}")
    for key, value in inserted.items():
        print(f"  {key}: {value}")
    print(
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
