#!/usr/bin/env python3
"""Corrige a proveniência da Figura 1.1 no Markdown e no DOCX canónicos."""

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

OLD_SOURCE_MD = (
    "Reproduzido de Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, "
    "D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing "
    "technology in the field of prosthetics: Past, present, and future. International "
    "Journal of Environmental Research and Public Health, 16, 1641. "
    "https://doi.org/10.3390/ijerph16091641"
)
OLD_SOURCE_PREFIX = "Reproduzido de Manero, A., Smith, P., Sparkman, J."
NEW_SOURCE_PARTS = (
    ("Fonte: produção própria, a partir de imagens publicadas no sítio ", False),
    ("Enabling the Future", True),
    (", nas páginas ", False),
    ("Wrist Powered", True),
    (" e ", False),
    ("Introducing the New 3D Printed Kinetic Hand Design", True),
    (
        " (consultadas em 20 de julho de 2026). "
        "https://enablingthefuture.org/wrist-powered/; "
        "https://enablingthefuture.org/2020/11/13/"
        "introducing-the-new-3d-printed-kinetic-hand-design/",
        False,
    ),
)
NEW_SOURCE_MD = "".join(
    f"*{value}*" if italic else value for value, italic in NEW_SOURCE_PARTS
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


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
    }


def replace_docx_source(root: etree._Element) -> None:
    candidates = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph).startswith(OLD_SOURCE_PREFIX)
    ]
    matches = []
    for paragraph in candidates:
        previous = paragraph.getprevious()
        while previous is not None and not text_of(previous).strip():
            previous = previous.getprevious()
        if previous is not None and text_of(previous).startswith("Figura 1.1 —"):
            matches.append(paragraph)
    if len(matches) != 1:
        raise RuntimeError(
            "Fonte antiga da Figura 1.1 inesperada no DOCX: "
            f"{len(matches)} ocorrências em {len(candidates)} candidatas"
        )
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("A fonte da Figura 1.1 contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in NEW_SOURCE_PARTS:
        add_run(paragraph, value, italic=italic)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = {
        "Versão do documento: 0.4.89": 1,
        OLD_SOURCE_MD: 2,
        NEW_SOURCE_MD: 0,
    }
    for value, expected in checks.items():
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada para {value[:70]!r}: "
                f"{actual} != {expected}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.89", "Versão do documento: 0.4.90", 1
    )
    return markdown.replace(OLD_SOURCE_MD, NEW_SOURCE_MD, 1)


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
    replace_docx_source(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    new_source = "".join(value for value, _ in NEW_SOURCE_PARTS)
    if body.count(OLD_SOURCE_PREFIX) != 1 or body.count(new_source) != 1:
        raise RuntimeError("A substituição da fonte não ficou íntegra no DOCX")

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
        "Fonte da Figura 1.1 corrigida para montagem de produção própria; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
