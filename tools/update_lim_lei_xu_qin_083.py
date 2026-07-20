#!/usr/bin/env python3
"""Integra Lim, Lei e Xu/Qin na contextualização do design generativo."""

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
    "Em contextos médicos e de tecnologias de apoio, estudos demonstram a integração "
    "de modelos paramétricos com análises de elementos finitos (FEM) para validar o "
    "desempenho estrutural, bem como a utilização de algoritmos generativos capazes de "
    "adaptar padrões e estruturas superficiais a geometrias individualizadas. (Lei et "
    "al., 2016; Lim et al., 2018)."
)
NEW_BEFORE_DESIGN = (
    "Em próteses impressas em 3D, a parametrização permite ajustar de modo independente "
    "dimensões como o comprimento e a largura dos componentes, evitando as limitações "
    "do escalonamento uniforme (Lim et al., 2018). Em famílias de produtos destinadas ao "
    "fabrico aditivo, a optimização topológica permite gerar geometrias a partir de "
    "requisitos e restrições, que podem depois ser avaliadas pelo método dos elementos "
    "finitos (FEM) e por critérios de custo (Lei et al., 2016). No domínio específico das "
    "próteses de membros, Xu e Qin (2022) identificam aplicações de "
)
NEW_AFTER_DESIGN = (
    " generativo que utilizam optimização topológica para reduzir o peso e FEM para "
    "validar o desempenho estrutural. Esta passagem de parâmetros explicitamente "
    "definidos para a geração e avaliação algorítmica de alternativas estabelece uma "
    "ligação conceptual com as abordagens de inteligência artificial discutidas nas "
    "secções seguintes."
)
NEW_DOCX = NEW_BEFORE_DESIGN + "design" + NEW_AFTER_DESIGN
NEW_MD = NEW_BEFORE_DESIGN + "*design*" + NEW_AFTER_DESIGN

YAO_ENTRY = (
    "Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for "
    "additive manufactured variable platforms in product families. Journal of "
    "Mechanical Design, 138(4), 041701. https://doi.org/10.1115/1.4032504"
)
XU_BEFORE_PROCEEDINGS = (
    "Xu, K., & Qin, S.-F. (2022). 3D printing, limb prosthetics and generative design: "
    "A scoping review. In "
)
XU_PROCEEDINGS = (
    "2022 27th International Conference on Automation and Computing (ICAC)"
)
XU_AFTER_PROCEEDINGS = (
    " (pp. 1–6). IEEE. https://doi.org/10.1109/ICAC55051.2022.9911138"
)
XU_DOCX = XU_BEFORE_PROCEEDINGS + XU_PROCEEDINGS + XU_AFTER_PROCEEDINGS
XU_MD = XU_BEFORE_PROCEEDINGS + "*" + XU_PROCEEDINGS + "*" + XU_AFTER_PROCEEDINGS
XU_MD_BLOCK = '<a id="ref-xu-qin-2022"></a> ' + XU_MD + "\n\n"


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


def rebuild_paragraph(
    paragraph: etree._Element, runs: list[tuple[str, bool]]
) -> None:
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo a substituir contém uma estrutura sensível")
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in runs:
        add_run(paragraph, value, italic=italic)


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
    if markdown.count("Versão do documento: 0.4.82") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(OLD) != 1:
        raise RuntimeError("Parágrafo original não localizado de forma única no Markdown")
    if "ref-xu-qin-2022" in markdown or XU_DOCX in markdown:
        raise RuntimeError("A referência de Xu e Qin já existe no Markdown")
    yao_block = '<a id="ref-yao-2016"></a> ' + YAO_ENTRY
    if markdown.count(yao_block) != 1:
        raise RuntimeError("Entrada de Yao não localizada para inserção alfabética")
    markdown = markdown.replace(
        "Versão do documento: 0.4.82", "Versão do documento: 0.4.83", 1
    )
    markdown = markdown.replace(OLD, NEW_MD, 1)
    markdown = markdown.replace(yao_block, XU_MD_BLOCK + yao_block, 1)
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

    old_matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD
    ]
    if len(old_matches) != 1:
        raise RuntimeError(
            f"Esperava um parágrafo original no DOCX; encontrei {len(old_matches)}"
        )
    rebuild_paragraph(
        old_matches[0],
        [(NEW_BEFORE_DESIGN, False), ("design", True), (NEW_AFTER_DESIGN, False)],
    )

    yao_matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == YAO_ENTRY
    ]
    if len(yao_matches) != 1:
        raise RuntimeError(
            f"Esperava uma entrada Yao no DOCX; encontrei {len(yao_matches)}"
        )
    yao_paragraph = yao_matches[0]
    parent = yao_paragraph.getparent()
    xu_paragraph = etree.Element(qn("p"), nsmap=yao_paragraph.nsmap)
    properties = yao_paragraph.find(qn("pPr"))
    if properties is not None:
        xu_paragraph.append(deepcopy(properties))
    add_run(xu_paragraph, XU_BEFORE_PROCEEDINGS)
    add_run(xu_paragraph, XU_PROCEEDINGS, italic=True)
    add_run(xu_paragraph, XU_AFTER_PROCEEDINGS)
    parent.insert(parent.index(yao_paragraph), xu_paragraph)

    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if body.count(OLD) != 0 or body.count(NEW_DOCX) != 1:
        raise RuntimeError("A substituição do parágrafo no DOCX não ficou íntegra")
    if body.count(XU_DOCX) != 1:
        raise RuntimeError("A entrada bibliográfica de Xu e Qin não ficou íntegra")

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
        "Lim, Lei e Xu/Qin integrados; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
