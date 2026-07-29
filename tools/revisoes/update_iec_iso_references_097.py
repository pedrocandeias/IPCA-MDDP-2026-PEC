#!/usr/bin/env python3
"""Alinha as referências IEC/ISO do manuscrito com as fontes verificadas localmente."""

from __future__ import annotations

import os
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

OLD_SCOPE_MD = (
    "O comité técnico ISO/TC 168 normaliza aspectos como o desempenho, a segurança e a "
    "compatibilidade entre componentes de próteses e ortóteses (ISO, n.d.)."
)
NEW_SCOPE_MD = (
    "O comité técnico ISO/TC 168 normaliza aspectos como o desempenho, a segurança, os factores "
    "ambientais e a possibilidade de intercâmbio entre componentes de próteses e ortóteses "
    "(ISO, n.d.)."
)

OLD_IEC_SENTENCE_MD = (
    "A norma IEC 62366-1:2015+A1:2020 estabelece um processo de engenharia de usabilidade para "
    "analisar, especificar, desenvolver e avaliar a utilização segura de dispositivos médicos "
    "(International Electrotechnical Commission [IEC], 2020)."
)
NEW_IEC_SENTENCE_MD = (
    "A norma IEC 62366-1:2015 estabelece um processo de engenharia de usabilidade para analisar, "
    "especificar, desenvolver e avaliar a utilização segura de dispositivos médicos "
    "(International Electrotechnical Commission [IEC], 2015)."
)

OLD_IEC_BIB_MD = (
    '<a id="ref-iec-62366-1-2020"></a> International Electrotechnical Commission. (2020). '
    "*Medical devices—Part 1: Application of usability engineering to medical devices* "
    "(IEC Standard No. 62366-1:2015+AMD1:2020 CSV). "
    "https://webstore.iec.ch/en/publication/67220"
)
NEW_IEC_BIB_MD = (
    '<a id="ref-iec-62366-1-2015"></a> International Electrotechnical Commission. (2015). '
    "*Medical devices—Part 1: Application of usability engineering to medical devices* "
    "(IEC Standard No. 62366-1:2015). https://webstore.iec.ch/en/publication/21863"
)


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def replace_text_node(
    root: etree._Element, old: str, new: str, *, substring: bool = False
) -> None:
    nodes = []
    for node in root.xpath("//w:t", namespaces=NS):
        value = node.text or ""
        if (old in value) if substring else (value == old):
            nodes.append(node)
    if len(nodes) != 1:
        raise RuntimeError(f"Ocorrências DOCX inesperadas para {old!r}: {len(nodes)}")
    nodes[0].text = (nodes[0].text or "").replace(old, new, 1)
    set_space(nodes[0])


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "comment_starts": len(root.xpath("//w:commentRangeStart", namespaces=NS)),
        "comment_ends": len(root.xpath("//w:commentRangeEnd", namespaces=NS)),
        "comment_refs": len(root.xpath("//w:commentReference", namespaces=NS)),
        "footnote_refs": len(root.xpath("//w:footnoteReference", namespaces=NS)),
        "drawings": len(root.xpath("//w:drawing", namespaces=NS)),
        "tables": len(root.xpath("//w:tbl", namespaces=NS)),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    replacements = (
        ("Versão do documento: 0.4.96", "Versão do documento: 0.4.97"),
        (OLD_SCOPE_MD, NEW_SCOPE_MD),
        (OLD_IEC_SENTENCE_MD, NEW_IEC_SENTENCE_MD),
        (OLD_IEC_BIB_MD, NEW_IEC_BIB_MD),
    )
    for old, _ in replacements:
        count = markdown.count(old)
        if count != 1:
            raise RuntimeError(f"Ocorrências Markdown inesperadas para {old[:70]!r}: {count}")
    for old, new in replacements:
        markdown = markdown.replace(old, new, 1)
    return markdown


def update_docx(root: etree._Element) -> None:
    replace_text_node(
        root,
        " normaliza aspetos como o desempenho, a segurança e a compatibilidade entre componentes "
        "de próteses e ortóteses (ISO, n.d.).",
        " normaliza aspetos como o desempenho, a segurança, os fatores ambientais e a "
        "possibilidade de intercâmbio entre componentes de próteses e ortóteses (ISO, n.d.).",
        substring=True,
    )
    replace_text_node(root, "IEC 62366-1:2015+A1:2020", "IEC 62366-1:2015")
    replace_text_node(
        root,
        "(International Electrotechnical Commission [IEC], 2020)",
        "(International Electrotechnical Commission [IEC], 2015)",
        substring=True,
    )
    replace_text_node(
        root,
        "International Electrotechnical Commission. (2020). ",
        "International Electrotechnical Commission. (2015). ",
    )
    replace_text_node(
        root,
        " (IEC Standard No. 62366-1:2015+AMD1:2020 CSV). "
        "https://webstore.iec.ch/en/publication/67220",
        " (IEC Standard No. 62366-1:2015). https://webstore.iec.ch/en/publication/21863",
    )


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
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    for required in (
        "ISO/TC 168 normaliza aspetos como o desempenho, a segurança, os fatores ambientais",
        "IEC 62366-1:2015 estabelece um processo de engenharia de usabilidade",
        "International Electrotechnical Commission. (2015). Medical devices",
        "https://webstore.iec.ch/en/publication/21863",
    ):
        if required not in body:
            raise RuntimeError(f"Conteúdo DOCX em falta: {required}")
    for obsolete in (
        "IEC 62366-1:2015+A1:2020",
        "62366-1:2015+AMD1:2020 CSV",
        "International Electrotechnical Commission. (2020).",
    ):
        if obsolete in body:
            raise RuntimeError(f"Conteúdo DOCX obsoleto conservado: {obsolete}")

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
        "Referências IEC/ISO alinhadas; "
        f"notas={after['footnote_refs']}, comentários={after['comment_refs']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
