#!/usr/bin/env python3
"""Substitui Yao et al. (2016) por Lei, Moon e Rosen (2015) no DOCX 0.4.112."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
MENDELEY_PREFIX = "MENDELEY_CITATION_v3_"
PARETO_FOOTNOTE_ID = "4"
PARETO_FOOTNOTE_START = (
    " A fronteira de Pareto corresponde ao conjunto de soluções em que não é possível "
    "melhorar um critério"
)


OLD_OPTIMISATION = (
    "A parametrização é frequentemente combinada com métodos de otimização topológica, "
    "de geração de estruturas reticuladas e de abordagens multiobjetivo. Estas estratégias "
    "permitem gerir compromissos entre peso, resistência, custo e tempo de fabrico, "
    "explorando fronteiras de Pareto para selecionar soluções alinhadas com objetivos "
    "específicos (Lei et al., 2016)."
)
NEW_OPTIMISATION_PARTS = (
    (
        "Em famílias de produtos destinadas ao fabrico aditivo, a parametrização pode "
        "definir o espaço de personalização através de variáveis dimensionais e dos "
        "respetivos intervalos. Lei et al. (2015) aplicaram esta lógica a uma família de "
        "bombas de deslocamento positivo destinada a equipamentos portáteis de hemodiálise "
        "domiciliária. Nestas bombas, duas filas de elementos mecânicos, designados ",
        False,
    ),
    ("fingers", True),
    (
        " no artigo, impulsionam separadamente o sangue e o dialisante; o seu deslocamento "
        "é comandado por uma árvore de cames acionada por um motor elétrico. O modelo "
        "variou cinco parâmetros para produzir caudais entre 100 e 600 ml/min e otimizou "
        "conjuntamente a eficiência, o volume da bomba e o custo de fabrico por "
        "sinterização seletiva a laser (SLS). Outro modelo para famílias de produtos "
        "partiu de requisitos e restrições, recorreu à otimização topológica e comparou "
        "as alternativas através de análise por elementos finitos e análise de custos ",
        False,
    ),
)

OLD_INTEGRATION = (
    "Este cruzamento entre parametrização, simulação e FA evidencia um ecossistema digital "
    "integrado que sustenta personalização técnica com base quantitativa (Lei et al., 2016)."
)
NEW_INTEGRATION_BEFORE_CITATION = (
    "O modelo de Lei et al. (2015) torna explícito um fluxo de decisão no qual os "
    "parâmetros delimitam variantes admissíveis e a otimização procura configurações de "
    "melhor desempenho segundo objetivos de eficiência, volume e custo. O trabalho "
    "complementar acrescenta a este fluxo a otimização topológica e a análise por "
    "elementos finitos "
)
NEW_INTEGRATION_AFTER_CITATION = (
    ". Em conjunto, estas abordagens articulam parametrização, simulação e FA numa base "
    "quantitativa para a personalização, embora os resultados dependam das "
    "funções-objetivo, dos pressupostos de custo e do processo de fabrico adotado."
)

OLD_ECONOMICS = (
    "Em termos económicos, o fabrico aditivo pode reduzir os sobrecustos tradicionalmente "
    "associados à produção de variantes. Estudos orientados para famílias de produto "
    "indicam que a integração de modelos paramétricos com análises de custo e desempenho "
    "pode manter os custos relativamente estáveis mesmo com elevada diversidade geométrica "
    "(Lei et al., 2016)."
)
NEW_ECONOMICS = (
    "Em termos económicos, o estudo de Lei et al. (2015) não demonstra que qualquer "
    "variação geométrica seja economicamente neutra. No caso analisado, porém, o custo por "
    "unidade manteve-se baixo mesmo para pequenos volumes de produção e tendeu a "
    "estabilizar nas três ou quatro bombas de maior dimensão. Comparativamente ao método "
    "convencional usado como referência, a otimização de onze variantes para diferentes "
    "caudais produziu um aumento médio de 25,02% na eficiência e uma redução média de "
    "26,12% no volume da bomba. Estes resultados mostram, apenas para as condições e o "
    "modelo de custos estudados, que o fabrico aditivo pode ampliar a variedade de uma "
    "família de produtos sem impor automaticamente um aumento proporcional do custo."
)

LEI_2016_ENTRY = (
    "Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process "
    "model for product family design. Journal of Engineering Design, 27(11), 751–767. "
    "https://doi.org/10.1080/09544828.2016.1228101"
)
LEI_2015_ENTRY_PARTS = (
    (
        "Lei, N., Moon, S. K., & Rosen, D. W. (2015). Redefining product family design "
        "for additive manufacturing. In ",
        False,
    ),
    (
        "DS 80-4: Proceedings of the 20th International Conference on Engineering Design "
        "(ICED 15), Vol. 4: Design for X, Design to X",
        True,
    ),
    (
        " (pp. 267–278). The Design Society. "
        "https://iced.designsociety.org/publication/37778/"
        "redefining_product_family_design_for_additive_manufacturing",
        False,
    ),
)
LEI_2015_ENTRY = "".join(value for value, _ in LEI_2015_ENTRY_PARTS)
YAO_ENTRY = (
    "Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive "
    "manufactured variable platforms in product families. Journal of Mechanical Design, "
    "138(4), 041701. https://doi.org/10.1115/1.4032504"
)


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


def find_paragraph(root: etree._Element, text: str, label: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"{label}: esperava um parágrafo; encontrei {len(matches)}")
    return matches[0]


def mendeley_citation(paragraph: etree._Element) -> etree._Element:
    matches = [
        control
        for control in paragraph.xpath(".//w:sdt", namespaces=NS)
        if any(
            tag.startswith(MENDELEY_PREFIX)
            for tag in control.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
        )
    ]
    if len(matches) != 1 or text_of(matches[0]) != "(Lei et al., 2016)":
        raise RuntimeError("A citação viva de Lei et al. (2016) não corresponde ao esperado")
    return deepcopy(matches[0])


def clear_paragraph(paragraph: etree._Element) -> None:
    if paragraph.xpath(
        ".//w:commentReference | .//w:commentRangeStart | .//w:commentRangeEnd | "
        ".//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo a substituir contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)


def replace_with_preserved_citation(
    paragraph: etree._Element,
    before_parts: tuple[tuple[str, bool], ...],
    after_text: str,
) -> None:
    citation = mendeley_citation(paragraph)
    clear_paragraph(paragraph)
    for value, italic in before_parts:
        add_run(paragraph, value, italic=italic)
    paragraph.append(citation)
    add_run(paragraph, after_text)


def replace_plain(paragraph: etree._Element, text: str) -> None:
    clear_paragraph(paragraph)
    add_run(paragraph, text)


def insert_bibliography_entry(
    root: etree._Element,
    anchor: etree._Element,
) -> None:
    if any(text_of(p) == LEI_2015_ENTRY for p in root.xpath("//w:p", namespaces=NS)):
        raise RuntimeError("A referência de Lei, Moon e Rosen (2015) já existe no DOCX")
    paragraph = etree.Element(qn("p"), nsmap=anchor.nsmap)
    properties = anchor.find(qn("pPr"))
    if properties is not None:
        paragraph.append(deepcopy(properties))
    for value, italic in LEI_2015_ENTRY_PARTS:
        add_run(paragraph, value, italic=italic)
    parent = anchor.getparent()
    parent.insert(parent.index(anchor), paragraph)


def state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
        "mendeley_citations": len(
            [
                tag
                for tag in root.xpath("//w:sdtPr/w:tag/@w:val", namespaces=NS)
                if tag.startswith(MENDELEY_PREFIX)
            ]
        ),
    }


def remove_pareto_footnote(entries: dict[str, bytes]) -> None:
    parser = etree.XMLParser(remove_blank_text=False)
    footnotes = etree.fromstring(entries["word/footnotes.xml"], parser)
    matches = footnotes.xpath(
        f"//w:footnote[@w:id='{PARETO_FOOTNOTE_ID}']",
        namespaces=NS,
    )
    if len(matches) != 1 or not text_of(matches[0]).startswith(PARETO_FOOTNOTE_START):
        raise RuntimeError("A nota de rodapé sobre a fronteira de Pareto não corresponde ao esperado")
    matches[0].getparent().remove(matches[0])
    entries["word/footnotes.xml"] = etree.tostring(
        footnotes, xml_declaration=True, encoding="UTF-8", standalone=True
    )


def main() -> None:
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name not in {"word/document.xml", "word/footnotes.xml"}
    }

    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    before = state(root)

    optimisation = find_paragraph(root, OLD_OPTIMISATION, "Optimização")
    integration = find_paragraph(root, OLD_INTEGRATION, "Integração")
    economics = find_paragraph(root, OLD_ECONOMICS, "Economia")
    lei_2016 = find_paragraph(root, LEI_2016_ENTRY, "Referência Lei 2016")
    yao = find_paragraph(root, YAO_ENTRY, "Referência Yao 2016")

    replace_with_preserved_citation(
        optimisation,
        NEW_OPTIMISATION_PARTS,
        ".",
    )
    replace_with_preserved_citation(
        integration,
        ((NEW_INTEGRATION_BEFORE_CITATION, False),),
        NEW_INTEGRATION_AFTER_CITATION,
    )
    replace_plain(economics, NEW_ECONOMICS)
    insert_bibliography_entry(root, lei_2016)
    yao.getparent().remove(yao)
    remove_pareto_footnote(entries)

    after = state(root)
    expected = dict(before)
    expected["mendeley_citations"] -= 1
    expected["footnotes"] -= 1
    if after != expected:
        raise RuntimeError(f"Estrutura sensível alterada: esperado {expected}; obtido {after}")

    body = text_of(root)
    paragraphs = [text_of(p) for p in root.xpath("//w:p", namespaces=NS)]
    expected_paragraphs = (
        LEI_2015_ENTRY,
        LEI_2016_ENTRY,
        NEW_ECONOMICS,
        "".join(value for value, _ in NEW_OPTIMISATION_PARTS) + "(Lei et al., 2016).",
        NEW_INTEGRATION_BEFORE_CITATION
        + "(Lei et al., 2016)"
        + NEW_INTEGRATION_AFTER_CITATION,
    )
    for value in expected_paragraphs:
        if paragraphs.count(value) != 1:
            raise RuntimeError(f"Validação final inesperada para {value[:80]!r}")
    for value in (OLD_OPTIMISATION, OLD_INTEGRATION, OLD_ECONOMICS, YAO_ENTRY):
        if value in body:
            raise RuntimeError(f"Texto antigo ainda presente: {value[:80]!r}")

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
                if info.filename not in {"word/document.xml", "word/footnotes.xml"}
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Yao et al. (2016) substituído por Lei, Moon e Rosen (2015); "
        f"citações Mendeley={after['mendeley_citations']}, "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
