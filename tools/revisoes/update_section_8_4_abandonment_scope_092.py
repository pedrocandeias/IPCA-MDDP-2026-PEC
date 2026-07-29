#!/usr/bin/env python3
"""Delimita a discussão da Secção 8.4 sobre factores de abandono protésico."""

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

OLD_TEXT = (
    "A literatura identifica desconforto, ajuste inadequado, limitações funcionais, peso, "
    "dificuldade de controlo, manutenção e insatisfação estética como factores associados "
    "à utilização descontínua ou ao abandono de próteses (Biddiss et al., 2007; Fink & "
    "Diamond, 2023; Smail et al., 2021). Estes factores foram tratados como requisitos do "
    "processo de design. A configuração dimensional, a visualização, a escolha formal e "
    "cromática, a edição dos parâmetros e a possibilidade de aceitar, alterar ou rejeitar "
    "sugestões de IA constituem respostas concretas ao problema de projecto. Os ensaios "
    "verificaram a presença e o funcionamento técnico destes mecanismos, mas não mediram "
    "o seu efeito no conforto percebido, na aceitação ou na utilização continuada."
)
OLD_MD = OLD_TEXT.replace("processo de design", "processo de *design*")
NEW_PARTS = (
    (
        "A literatura sobre próteses de membro superior agrupa as razões de abandono "
        "principalmente em problemas de conforto e de função, incluindo o peso, a "
        "temperatura e a transpiração (Smail et al., 2021). Biddiss et al. (2007) "
        "identificam o peso, o conforto e o controlo como prioridades expressas pelos "
        "utilizadores, enquanto Fink e Diamond (2023) destacam o ajuste do encaixe, o "
        "controlo, o peso, a facilidade de reparação e a estética entre os aspectos a "
        "considerar na escolha e no acompanhamento da prótese. Nesta investigação, estas "
        "preocupações foram traduzidas em requisitos de referência para o processo de ",
        False,
    ),
    ("design", True),
    (
        ". A configuração dimensional, a visualização, a escolha formal e cromática, a "
        "edição dos parâmetros e a possibilidade de aceitar, alterar ou rejeitar sugestões "
        "de IA constituem respostas concretas a esses requisitos. Os ensaios confirmaram a "
        "presença e o funcionamento técnico destes mecanismos, mas não mediram os seus "
        "efeitos no conforto percebido, na aceitação ou na utilização continuada.",
        False,
    ),
)
NEW_TEXT = "".join(value for value, _ in NEW_PARTS)
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


def replace_docx_paragraph(root: etree._Element) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD_TEXT
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo antigo inesperado no DOCX: {len(matches)} ocorrências")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in NEW_PARTS:
        add_run(paragraph, value, italic=italic)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = {
        "Versão do documento: 0.4.91": 1,
        OLD_MD: 1,
        NEW_MD: 0,
    }
    for value, expected in checks.items():
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada para {value[:70]!r}: "
                f"{actual} != {expected}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.91", "Versão do documento: 0.4.92", 1
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
    if OLD_TEXT in body or body.count(NEW_TEXT) != 1:
        raise RuntimeError("A reformulação não ficou íntegra no DOCX")

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
        "Discussão da Secção 8.4 delimitada; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
