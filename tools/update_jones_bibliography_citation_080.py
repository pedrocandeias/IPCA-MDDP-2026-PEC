#!/usr/bin/env python3
"""Corrige Jones et al. (2023) e reposiciona a citação no manuscrito."""

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

OLD_EVIDENCE = (
    "A predominância de estudos com amostras reduzidas, curta duração e validação "
    "limitada dificulta a comparação entre soluções, a generalização de conclusões e "
    "a tradução de melhorias laboratoriais em benefícios consistentes na vida "
    "quotidiana. (Hafner & Sawers, 2016; Samuelsson et al., 2012)."
)
NEW_EVIDENCE = (
    "A predominância de estudos com amostras reduzidas, curta duração e validação "
    "limitada dificulta a comparação entre soluções, a generalização de conclusões e "
    "a tradução de melhorias laboratoriais em benefícios consistentes na vida "
    "quotidiana (Hafner & Sawers, 2016; Jones et al., 2023; Samuelsson et al., 2012)."
)
OLD_METHOD = (
    "A definição destes limites transforma a adaptação numa configuração condicionada "
    "por relações explícitas entre medidas, componentes e restrições de fabrico. Cada "
    "condição necessita de um critério próprio e deve ser confrontada com a geometria "
    "efectivamente gerada, não apenas com o nome do parâmetro ou com o intervalo "
    "apresentado na interface (Brack & Amalu, 2021; Herneth et al., 2024; Jones et al., "
    "2023)."
)
NEW_METHOD = (
    "No âmbito deste projecto, os limites de adaptação foram formalizados como relações "
    "explícitas entre medidas, componentes e restrições de fabrico. A verificação foi "
    "definida para incidir sobre a geometria efectivamente gerada, e não apenas sobre o "
    "nome do parâmetro ou o intervalo apresentado na interface."
)
OLD_ENTRY = (
    "Jones, M. L. H., Vrieling, A. H., Steadman, J., & Kyberd, P. J. (2023). "
    "Evidencing the effectiveness of upper limb prostheses: A multi-stakeholder "
    "perspective on study requirements. Frontiers in Health Services, 3, 1123682. "
    "https://doi.org/10.3389/frhs.2023.1123682"
)
ENTRY_PREFIX = (
    "Jones, H., Chadwell, A., & Dyson, M. (2023). Evidencing the effectiveness of upper "
    "limb prostheses: A multi-stakeholder perspective on study requirements. "
)
ENTRY_JOURNAL = "Frontiers in Health Services, 3"
ENTRY_SUFFIX = ", Article 1213752. https://doi.org/10.3389/frhs.2023.1213752"
NEW_ENTRY_DOCX = ENTRY_PREFIX + ENTRY_JOURNAL + ENTRY_SUFFIX
NEW_ENTRY_MD = ENTRY_PREFIX + f"*{ENTRY_JOURNAL}*" + ENTRY_SUFFIX


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


def find_exact(root: etree._Element, value: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == value]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo para {value[:70]!r}; encontrei {len(matches)}")
    return matches[0]


def replace_text(paragraph: etree._Element, value: str) -> None:
    ppr = paragraph.find(qn("pPr"))
    ppr_copy = deepcopy(ppr) if ppr is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if ppr_copy is not None:
        paragraph.append(ppr_copy)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def add_run(paragraph: etree._Element, value: str, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        rpr = etree.SubElement(run, qn("rPr"))
        etree.SubElement(rpr, qn("i"))
        etree.SubElement(rpr, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_bibliography(paragraph: etree._Element) -> None:
    ppr = paragraph.find(qn("pPr"))
    ppr_copy = deepcopy(ppr) if ppr is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if ppr_copy is not None:
        paragraph.append(ppr_copy)
    add_run(paragraph, ENTRY_PREFIX)
    add_run(paragraph, ENTRY_JOURNAL, italic=True)
    add_run(paragraph, ENTRY_SUFFIX)


def state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "jones_citations": text_of(root).count("Jones et al., 2023"),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    replacements = [
        ("Versão do documento: 0.4.79", "Versão do documento: 0.4.80"),
        (OLD_EVIDENCE, NEW_EVIDENCE),
        (OLD_METHOD, NEW_METHOD),
        (OLD_ENTRY, NEW_ENTRY_MD),
    ]
    for old, new in replacements:
        if markdown.count(old) != 1:
            raise RuntimeError(f"Ocorrência Markdown inesperada para {old[:70]!r}")
        markdown = markdown.replace(old, new, 1)
    if markdown.count("Jones et al., 2023") != 1:
        raise RuntimeError("A citação de Jones não ficou única no Markdown")
    return markdown


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
    before = state(root)
    if before["jones_citations"] != 1:
        raise RuntimeError(f"Contagem inicial inesperada: {before}")

    replace_text(find_exact(root, OLD_EVIDENCE), NEW_EVIDENCE)
    replace_text(find_exact(root, OLD_METHOD), NEW_METHOD)
    replace_bibliography(find_exact(root, OLD_ENTRY))
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível ou citações alteradas: {before} -> {after}")
    body = text_of(root)
    if body.count(NEW_ENTRY_DOCX) != 1:
        raise RuntimeError("A nova entrada bibliográfica não ficou íntegra no DOCX")
    if "10.3389/frhs.2023.1123682" in body:
        raise RuntimeError("O DOI incorrecto permaneceu no DOCX")

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
        "Jones et al. corrigido e reposicionado; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, citações={after['jones_citations']}"
    )


if __name__ == "__main__":
    main()
