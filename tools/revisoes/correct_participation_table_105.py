#!/usr/bin/env python3
"""Corrige a atribuição bibliográfica da participação na Tabela 8.8."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import NS, qn, sensitive_state, set_space, text_of


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD_MD = (
    "A documentação do percurso reforça o registo metodológico, mas não responde à "
    "insuficiência de participação e de métodos qualitativos identificada por Hafner e "
    "Sawers (2016), Richardson e Dillon (2017) e Walker et al. (2020)"
)
NEW_MD = (
    "A documentação torna o percurso rastreável, mas não substitui o envolvimento de "
    "utilizadores. Walker et al. (2020) recomendam metodologias qualitativas e maior "
    "consulta ou *co-design* para integrar as perspectivas e os contextos de utilização "
    "no desenvolvimento de próteses do membro superior."
)
NEW_PARTS = (
    (
        "A documentação torna o percurso rastreável, mas não substitui o envolvimento "
        "de utilizadores. Walker et al. (2020) recomendam metodologias qualitativas e "
        "maior consulta ou ",
        False,
    ),
    ("co-design", True),
    (
        " para integrar as perspectivas e os contextos de utilização no desenvolvimento "
        "de próteses do membro superior.",
        False,
    ),
)


def add_run(paragraph: etree._Element, value: str, *, italic: bool) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_paragraph(root: etree._Element) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD_MD
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Célula da Tabela 8.8 inesperada no DOCX: {len(matches)}")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("A célula da Tabela 8.8 contém estrutura sensível")
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
    for value, expected in (
        ("Versão do documento: 0.4.104", 1),
        (OLD_MD, 1),
        (NEW_MD, 0),
    ):
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada: {actual} != {expected} para {value[:80]!r}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.104", "Versão do documento: 0.4.105", 1
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
    replace_paragraph(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    paragraphs = [text_of(p) for p in root.xpath("//w:p", namespaces=NS)]
    new_docx = NEW_MD.replace("*", "")
    if OLD_MD in paragraphs or paragraphs.count(new_docx) != 1:
        raise RuntimeError("A correcção não ficou íntegra no DOCX")

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
        "Participação da Tabela 8.8 corrigida; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
