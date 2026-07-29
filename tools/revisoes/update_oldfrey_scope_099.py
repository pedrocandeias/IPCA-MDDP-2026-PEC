#!/usr/bin/env python3
"""Delimita a utilização de Oldfrey et al. (2024) na Secção 2.2."""

from __future__ import annotations

import os
from copy import deepcopy
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
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

OLD_MD = (
    "Entre os principais desafios identificados destacam-se a articulação entre "
    "normalização e personalização em dispositivos médicos regulamentados, a distância "
    "entre modelos teóricos de UCD e as restrições institucionais da prática em saúde. "
    "Somam-se a passagem de processos participativos para contextos de implementação e "
    "a integração de factores sociais e culturais na investigação e no desenvolvimento "
    "(Fisher & Johansen, 2020; Oldfrey et al., 2024; Shah & Robinson, 2006)."
)
OLD_DOCX = OLD_MD.replace("Somam-se", "Soma-se").replace("*", "")
NEW_MD = (
    "Entre os desafios identificados destacam-se o desfasamento entre os princípios do "
    "*design* centrado no utilizador e as condições institucionais em que os dispositivos "
    "médicos são desenvolvidos, bem como a necessidade de atender à diversidade de "
    "necessidades, competências e contextos de utilização (Fisher & Johansen, 2020; "
    "Shah & Robinson, 2006). Na passagem da investigação para a aplicação, persistem "
    "limitações da evidência disponível e da colaboração entre equipas académicas, "
    "industriais e clínicas ao longo do percurso de desenvolvimento e introdução das "
    "tecnologias no mercado (Oldfrey et al., 2024)."
)
NEW_PARTS = (
    (
        "Entre os desafios identificados destacam-se o desfasamento entre os princípios do ",
        False,
    ),
    ("design", True),
    (
        " centrado no utilizador e as condições institucionais em que os dispositivos "
        "médicos são desenvolvidos, bem como a necessidade de atender à diversidade de "
        "necessidades, competências e contextos de utilização (Fisher & Johansen, 2020; "
        "Shah & Robinson, 2006). Na passagem da investigação para a aplicação, persistem "
        "limitações da evidência disponível e da colaboração entre equipas académicas, "
        "industriais e clínicas ao longo do percurso de desenvolvimento e introdução das "
        "tecnologias no mercado (Oldfrey et al., 2024).",
        False,
    ),
)
NEW_DOCX = "".join(value for value, _ in NEW_PARTS)


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


def replace_paragraph(root: etree._Element, old: str, parts: tuple[tuple[str, bool], ...]) -> None:
    matches = [paragraph for paragraph in root.xpath("//w:p", namespaces=NS) if text_of(paragraph) == old]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo Oldfrey inesperado no DOCX: {len(matches)} ocorrências")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo Oldfrey contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


def replace_version(root: etree._Element) -> None:
    old = "Versão do documento: 0.4.98"
    new = "Versão do documento: 0.4.99"
    matches = [paragraph for paragraph in root.xpath("//w:p", namespaces=NS) if text_of(paragraph) == old]
    if len(matches) > 1:
        raise RuntimeError(f"Versão inesperada no DOCX: {len(matches)} ocorrências")
    if matches:
        replace_paragraph(root, old, ((new, False),))


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    for value, expected in (
        ("Versão do documento: 0.4.98", 1),
        (OLD_MD, 1),
        (NEW_MD, 0),
    ):
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(f"Contagem Markdown inesperada: {actual} != {expected} para {value[:70]!r}")
    markdown = markdown.replace("Versão do documento: 0.4.98", "Versão do documento: 0.4.99", 1)
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
    replace_paragraph(root, OLD_DOCX, NEW_PARTS)
    replace_version(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if OLD_DOCX in body or body.count(NEW_DOCX) != 1:
        raise RuntimeError("A actualização não ficou íntegra no DOCX")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False) as stream:
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
        "Citação de Oldfrey delimitada; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
