#!/usr/bin/env python3
"""Revê a descrição do catálogo e-NABLE na Secção 2.4."""

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
    "O projecto e-NABLE é o exemplo mais influente deste movimento. A comunidade "
    "consolidou-se em torno da criação e partilha de dispositivos de assistência para "
    "diferenças de membro superior, em especial mãos mecânicas accionadas pelo corpo e "
    "braços impressos em 3D para crianças. O seu catálogo reúne modelos de mão, braço, "
    "dedos, polegares e dispositivos terminais, organizados em função da anatomia "
    "disponível e o tipo de acionamento. Nos modelos de mão accionados pelo punho, a "
    "flexão dos dedos depende normalmente da flexão activa do punho e de uma palma "
    "parcialmente preservada; quando essa condição anatómica não existe, a solução tende "
    "a deslocar-se para braços ou mecanismos accionados pelo cotovelo (Wendo et al., 2022)."
)
OLD_DOCX = OLD_MD.replace("dispositivos de assistência", "dispositivos de apoio", 1)

NEW_PARTS = (
    ("O projecto e-NABLE constitui um exemplo relevante deste movimento e enquadra "
     "directamente vários dos modelos analisados nesta investigação. Na revisão do "
     "catálogo e-NABLE, Wendo et al. (2022) agruparam os dispositivos em duas categorias: "
     "modelos de mão e modelos de braço. Todos os modelos de mão incluídos na revisão "
     "eram accionados pelo corpo através do movimento de um punho funcional. Entre os "
     "modelos de braço analisados, o ", False),
    ("Unlimbited Arm v2.1", True),
    (" e o ", False),
    ("Kwawu Arm", True),
    (" eram accionados pelo movimento do cotovelo, enquanto o ", False),
    ("El Medallo Bionic Arm", True),
    (" utilizava accionamento eléctrico controlado por sinais musculares. Para o ", False),
    ("design", True),
    (" de próteses de membro superior, esta distinção é importante porque evidencia a "
     "necessidade de relacionar o tipo de dispositivo e o respectivo mecanismo de "
     "accionamento com o movimento que a pessoa conserva.", False),
)
NEW_DOCX = "".join(value for value, _ in NEW_PARTS)
NEW_MD = "".join(f"*{value}*" if italic else value for value, italic in NEW_PARTS)


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
    if markdown.count("Versão do documento: 0.4.84") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(OLD_MD) != 1:
        raise RuntimeError("Parágrafo original não localizado de forma única no Markdown")
    markdown = markdown.replace(
        "Versão do documento: 0.4.84", "Versão do documento: 0.4.85", 1
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
    for value, italic in NEW_PARTS:
        add_run(paragraph, value, italic=italic)
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
        "Catálogo e-NABLE revisto; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
