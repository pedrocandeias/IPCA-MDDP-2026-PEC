#!/usr/bin/env python3
"""Retira Story (2006) depois de integrar as fontes primárias acessíveis."""

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

OLD_MD = (
    "Na área da saúde, o *design* universal é associado a abordagens centradas na pessoa e "
    "avaliado segundo critérios orientados a resultados, como a participação, a inclusão e a "
    "igualdade de acesso. A convergência entre *design* inclusivo e *design* universal revela-se "
    "particularmente evidente na ênfase comum na redução de barreiras ambientais e na ampliação do "
    "conceito de usabilidade para uma população mais ampla (Story, 2006; White & Mosca, 2022)."
)
NEW_MD = (
    "Na área da saúde, os critérios usados para operacionalizar o *design* universal incluem "
    "usabilidade, funcionalidade, segurança, orientação espacial, compreensão, factores "
    "ambientais, bem-estar e inclusão social (White & Mosca, 2022). Nesta dissertação, esta "
    "aplicação é interpretada como um ponto de convergência entre *design* universal e *design* "
    "inclusivo, por relacionar a redução de barreiras com a usabilidade e a inclusão."
)
STORY_MD = (
    '<a id="ref-story-2006"></a> Story, M. F. (2006). Applying the principles of universal design '
    "to medical devices. In J. M. Winters & M. F. Story (Eds.), Medical instrumentation: "
    "Accessibility and usability considerations (pp. 83-92). CRC Press. "
    "https://doi.org/10.1201/9781420006223-6"
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def add_run(paragraph: etree._Element, value: str, *, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")


def find_paragraph(root: etree._Element, exact: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == exact]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo DOCX inesperado para {exact[:80]!r}: {len(matches)}")
    return matches[0]


def replace_paragraph(
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


def main() -> None:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count(OLD_MD) != 1 or markdown.count(STORY_MD) != 1:
        raise RuntimeError("Estado Markdown inesperado para a retirada de Story (2006)")
    markdown = markdown.replace(OLD_MD, NEW_MD, 1)
    markdown = markdown.replace(f"\n\n{STORY_MD}", "", 1)

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    parser = etree.XMLParser(remove_blank_text=False)
    document = etree.fromstring(entries["word/document.xml"], parser)
    before = {
        "footnotes": len(document.xpath("//w:footnoteReference", namespaces=NS)),
        "drawings": len(document.xpath("//w:drawing", namespaces=NS)),
        "tables": len(document.xpath("//w:tbl", namespaces=NS)),
    }

    old_docx = OLD_MD.replace("*", "").replace("factores", "fatores")
    paragraph = find_paragraph(document, old_docx)
    replace_paragraph(
        paragraph,
        (
            ("Na área da saúde, os critérios usados para operacionalizar o ", False),
            ("design", True),
            (" universal incluem usabilidade, funcionalidade, segurança, orientação espacial, compreensão, fatores ambientais, bem-estar e inclusão social (White & Mosca, 2022). Nesta dissertação, esta aplicação é interpretada como um ponto de convergência entre ", False),
            ("design", True),
            (" universal e ", False),
            ("design", True),
            (" inclusivo, por relacionar a redução de barreiras com a usabilidade e a inclusão.", False),
        ),
    )

    story_docx = STORY_MD.split("></a> ", 1)[1]
    story_paragraph = find_paragraph(document, story_docx)
    story_paragraph.getparent().remove(story_paragraph)

    body = text_of(document)
    if "Story, M. F. (2006)" in body or "(Story, 2006" in body:
        raise RuntimeError("A referência de Story (2006) permaneceu no DOCX")
    after = {
        "footnotes": len(document.xpath("//w:footnoteReference", namespaces=NS)),
        "drawings": len(document.xpath("//w:drawing", namespaces=NS)),
        "tables": len(document.xpath("//w:tbl", namespaces=NS)),
    }
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")

    entries["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone=True
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
        "Story (2006) retirado após substituição por fontes locais; "
        f"notas={after['footnotes']}, imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
