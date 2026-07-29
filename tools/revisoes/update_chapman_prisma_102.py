#!/usr/bin/env python3
"""Delimita Chapman et al. e preserva a nota de rodapé nativa do PRISMA."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import (
    NS,
    XML_SPACE,
    qn,
    sensitive_state,
    set_space,
    text_of,
)


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD_MD = (
    "A avaliação da evidência tem sido igualmente reforçada através do uso de "
    "protocolos sistemáticos, como o PRISMA, que orienta a identificação, selecção e "
    "apresentação transparente dos estudos analisados, bem como de instrumentos de "
    "avaliação crítica. Esta evolução reflecte uma preocupação crescente em fundamentar "
    "decisões de *design* numa base empírica robusta. (Chapman et al., 2025)."
)
OLD_DOCX = OLD_MD.replace("*", "")
NEW_MD = (
    "Chapman et al. (2025) tornam explícitas as etapas de identificação e selecção dos "
    "estudos incluídos na sua revisão, recorrendo a uma adaptação das orientações "
    "PRISMA. Este registo permite compreender como foi constituído o conjunto de estudos "
    "analisados e torna mais clara a fundamentação bibliográfica utilizada para apoiar "
    "decisões de *design*."
)
PREFIX = (
    "Chapman et al. (2025) tornam explícitas as etapas de identificação e selecção dos "
    "estudos incluídos na sua revisão, recorrendo a uma adaptação das orientações PRISMA"
)
MIDDLE = (
    ". Este registo permite compreender como foi constituído o conjunto de estudos "
    "analisados e torna mais clara a fundamentação bibliográfica utilizada para apoiar "
    "decisões de "
)
END = "."
NEW_DOCX = PREFIX + MIDDLE + "design" + END


def add_run(paragraph: etree._Element, value: str, *, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def add_footnote_reference(paragraph: etree._Element, footnote_id: str) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    properties = etree.SubElement(run, qn("rPr"))
    style = etree.SubElement(properties, qn("rStyle"))
    style.set(qn("val"), "FootnoteReference")
    reference = etree.SubElement(run, qn("footnoteReference"))
    reference.set(qn("id"), footnote_id)


def replace_docx_paragraph(root: etree._Element) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD_DOCX
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo PRISMA inesperado no DOCX: {len(matches)} ocorrências")
    paragraph = matches[0]
    references = paragraph.xpath(".//w:footnoteReference/@w:id", namespaces=NS)
    if references != ["2"]:
        raise RuntimeError(f"Referência de nota PRISMA inesperada: {references}")
    if paragraph.xpath(
        ".//w:commentReference | .//w:commentRangeStart | .//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo PRISMA contém outra estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    add_run(paragraph, PREFIX)
    add_footnote_reference(paragraph, "2")
    add_run(paragraph, MIDDLE)
    add_run(paragraph, "design", italic=True)
    add_run(paragraph, END)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    for value, expected in (
        ("Versão do documento: 0.4.101", 1),
        (OLD_MD, 1),
        (NEW_MD, 0),
    ):
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada: {actual} != {expected} para {value[:70]!r}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.101", "Versão do documento: 0.4.102", 1
    )
    return markdown.replace(OLD_MD, NEW_MD, 1)


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
    replace_docx_paragraph(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if OLD_DOCX in body or body.count(NEW_DOCX) != 1:
        raise RuntimeError("A actualização não ficou íntegra no DOCX")
    if root.xpath("count(//w:footnoteReference[@w:id='2'])", namespaces=NS) != 1:
        raise RuntimeError("A nota de rodapé PRISMA deixou de ter uma referência única")

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
        "Passagem PRISMA delimitada; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
