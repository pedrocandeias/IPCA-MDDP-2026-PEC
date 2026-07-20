#!/usr/bin/env python3
"""Delimita a caracterização do ecossistema protésico aberto na Secção 2.4."""

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

OLD_DOCX = (
    "As próteses open source de membro superior passíveis de impressão 3D constituem um "
    "caso particularmente relevante para esta investigação, porque tornam visível a "
    "articulação entre fabrico aditivo, partilha digital de ficheiros, produção distribuída "
    "e adaptação local. Ao contrário dos dispositivos comerciais desenvolvidos em cadeias "
    "industriais fechadas, estes modelos circulam frequentemente como ficheiros editáveis "
    "e/ou imprimíveis, acompanhados por instruções de montagem, listas de componentes e "
    "documentação comunitária. A partilha destes recursos reduz barreiras de acesso aos "
    "ficheiros e demonstra a capacidade de comunidades distribuídas para produzir e "
    "adaptar soluções fora dos canais tradicionais da indústria médica; a qualidade "
    "funcional de cada dispositivo continua dependente de avaliação própria (Manero et "
    "al., 2019; Wendo et al., 2022)."
)
OLD_MD = OLD_DOCX.replace("open source", "*open source*", 1).replace(
    "ficheiros editáveis e/ou imprimíveis", "ficheiros editáveis ou imprimíveis", 1
)

NEW_BEFORE_OPEN = "As próteses "
NEW_AFTER_OPEN = (
    " de membro superior passíveis de impressão 3D constituem um caso particularmente "
    "relevante para esta investigação, porque articulam fabrico aditivo, partilha digital "
    "de ficheiros, reprodução distribuída e adaptação local. Estes modelos circulam "
    "frequentemente sob a forma de ficheiros digitais editáveis ou imprimíveis, "
    "acompanhados por documentação comunitária, como instruções de fabrico e montagem. A "
    "disponibilização de modelos tridimensionais através da Internet favoreceu a formação "
    "de comunidades de criadores capazes de reproduzir e avaliar estes dispositivos "
    "(Manero et al., 2019). Nas soluções abertas analisadas por Wendo et al. (2022), a "
    "disponibilidade dos ficheiros de desenho e impressão e de instruções claras de "
    "fabrico e montagem constitui um requisito essencial. Estes recursos facilitam a "
    "reprodução, o redimensionamento e a adaptação dos dispositivos, mas não garantem, "
    "por si só, a qualidade funcional de cada solução, que continua a exigir avaliação."
)
NEW_DOCX = NEW_BEFORE_OPEN + "open source" + NEW_AFTER_OPEN
NEW_MD = NEW_BEFORE_OPEN + "*open source*" + NEW_AFTER_OPEN


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


def add_run(paragraph: etree._Element, value: str, *, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count("Versão do documento: 0.4.83") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(OLD_MD) != 1:
        raise RuntimeError("Parágrafo original não localizado de forma única no Markdown")
    markdown = markdown.replace(
        "Versão do documento: 0.4.83", "Versão do documento: 0.4.84", 1
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
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD_DOCX
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo no DOCX; encontrei {len(matches)}")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo contém uma estrutura sensível")
    before = state(root)
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    add_run(paragraph, NEW_BEFORE_OPEN)
    add_run(paragraph, "open source", italic=True)
    add_run(paragraph, NEW_AFTER_OPEN)
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if body.count(OLD_DOCX) != 0 or body.count(NEW_DOCX) != 1:
        raise RuntimeError("A substituição no DOCX não ficou íntegra")

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
        "Ecossistema aberto delimitado; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
