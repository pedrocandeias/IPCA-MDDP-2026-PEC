#!/usr/bin/env python3
"""Delimita a citação de Krahe et al. (2020) no texto introdutório sobre IA."""

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

OLD = (
    "Dentro deste campo, a aprendizagem automática designa as abordagens em que o "
    "sistema aprende a partir de dados, em vez de depender exclusivamente de regras "
    "explicitamente escritas. A aprendizagem profunda corresponde a um subconjunto "
    "desta família e baseia-se em redes neuronais artificiais com múltiplas camadas, "
    "particularmente adequadas para tratar dados complexos, como imagens, texto ou som. "
    "Já a IA generativa refere-se a modelos capazes de produzir novos conteúdos — por "
    "exemplo, texto, imagens, composições formais ou variantes de projecto — com base "
    "nos padrões que aprenderam. Esta distinção é particularmente importante para o "
    "design, pois diferentes tipos de IA apoiam diferentes tipos de tarefas: algumas "
    "ajudam a analisar, outras a prever, outras a optimizar e outras ainda a gerar "
    "alternativas (Khanolkar et al., 2023; Krahe et al., 2020; Li et al., 2021)."
)

NEW_BEFORE_DESIGN = (
    "Dentro deste campo, a aprendizagem automática designa as abordagens em que o "
    "sistema aprende a partir de dados, em vez de depender exclusivamente de regras "
    "explicitamente escritas. A aprendizagem profunda corresponde a um subconjunto "
    "desta família e baseia-se em redes neuronais artificiais com múltiplas camadas, "
    "particularmente adequadas para tratar dados complexos, como imagens e texto. Já a "
    "IA generativa refere-se a modelos capazes de produzir novos conteúdos — por "
    "exemplo, texto, imagens, composições formais ou variantes de projecto — com base "
    "nos padrões que aprenderam. Esta distinção é particularmente importante para o "
)
NEW_AFTER_DESIGN = (
    ", pois diferentes tipos de IA apoiam diferentes tarefas: algumas ajudam a analisar "
    "informação, outras a prever resultados, outras a optimizar soluções e outras ainda "
    "a gerar alternativas (Khanolkar et al., 2023; Li et al., 2021). No desenvolvimento "
    "de produtos, por exemplo, estas técnicas podem identificar padrões em modelos "
    "tridimensionais e gerar novas variantes de forma a partir de requisitos previamente "
    "definidos (Krahe et al., 2020)."
)
NEW_DOCX = NEW_BEFORE_DESIGN + "design" + NEW_AFTER_DESIGN
NEW_MD = NEW_BEFORE_DESIGN + "*design*" + NEW_AFTER_DESIGN


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


def replace_paragraph(paragraph: etree._Element) -> None:
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    footnote_runs = [
        deepcopy(run)
        for run in paragraph.xpath("./w:r[w:footnoteReference]", namespaces=NS)
    ]
    if len(footnote_runs) != 1:
        raise RuntimeError(
            f"Esperava uma nota de rodapé no parágrafo; encontrei {len(footnote_runs)}"
        )
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    marker = "redes neuronais artificiais"
    before_note, after_note = NEW_BEFORE_DESIGN.split(marker, 1)
    add_run(paragraph, before_note + marker)
    paragraph.append(footnote_runs[0])
    add_run(paragraph, after_note)
    add_run(paragraph, "design", italic=True)
    add_run(paragraph, NEW_AFTER_DESIGN)


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
    old_md = OLD.replace("para o design,", "para o *design*,", 1)
    if markdown.count("Versão do documento: 0.4.80") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(old_md) != 1:
        raise RuntimeError("O parágrafo original não é único no Markdown")
    markdown = markdown.replace(
        "Versão do documento: 0.4.80", "Versão do documento: 0.4.81", 1
    )
    return markdown.replace(old_md, NEW_MD, 1)


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
        if text_of(paragraph) == OLD
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo no DOCX; encontrei {len(matches)}")
    before = state(root)
    replace_paragraph(matches[0])
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    if text_of(root).count(NEW_DOCX) != 1 or text_of(root).count(OLD) != 0:
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
        "Krahe et al. delimitado; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
