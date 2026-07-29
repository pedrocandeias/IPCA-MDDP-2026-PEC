#!/usr/bin/env python3
"""Apply the Flexy Beast material-scope and printer-comparison clarification.

The revised thesis DOCX is edited in place at OOXML level so the institutional
template, figures, tables, styles and section settings remain unchanged.
"""

from __future__ import annotations

import argparse
import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_paragraph_text(paragraph: etree._Element, text: str) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = text


def body_paragraphs(root: etree._Element) -> list[etree._Element]:
    return root.xpath("//w:body//w:p", namespaces=NS)


def find_exact(root: etree._Element, text: str) -> etree._Element:
    matches = [p for p in body_paragraphs(root) if paragraph_text(p) == text]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph {text!r}; found {len(matches)}")
    return matches[0]


def find_prefix(root: etree._Element, prefix: str) -> etree._Element:
    matches = [p for p in body_paragraphs(root) if paragraph_text(p).startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def replace_prefix(root: etree._Element, prefix: str, replacement: str) -> etree._Element:
    paragraph = find_prefix(root, prefix)
    set_paragraph_text(paragraph, replacement)
    return paragraph


def prevent_table_row_splitting(root: etree._Element, caption_text: str) -> None:
    caption = find_exact(root, caption_text)
    table = caption.getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError(f"Expected a table after {caption_text!r}")
    for row in table.findall(qn("tr")):
        row_pr = row.find(qn("trPr"))
        if row_pr is None:
            row_pr = etree.Element(qn("trPr"))
            row.insert(0, row_pr)
        if row_pr.find(qn("cantSplit")) is None:
            etree.SubElement(row_pr, qn("cantSplit"))


METHOD = (
    "Os modelos foram preparados no PrusaSlicer e no Bambu Studio. O fatiamento converte a geometria "
    "numa sequência de camadas e trajectórias de deposição, definindo altura de camada, paredes, "
    "enchimento, suportes, temperaturas e orientação. Existem dois projectos Bambu Lab A1, para Flexy "
    "Beast e UnLimbited Phoenix, gerados no Bambu Studio 1.10.02.76, e um projecto Prusa MINI para "
    "Paraglider Hand, gerado no PrusaSlicer 2.8.1. Os dois projectos Bambu registam camada de 0,24 mm, "
    "duas paredes, 15% de enchimento em grelha, suporte em árvore automático e aba de 5 mm. O projecto "
    "Prusa regista camada de 0,20 mm, duas paredes, 15% de enchimento em grelha, PLA, bico de 0,4 mm, "
    "mesa a 60 °C e suporte desactivado. Os parâmetros comparáveis foram mantidos nas restantes "
    "impressões, segundo o registo do projecto, embora não exista um ficheiro de configuração individual "
    "para cada peça produzida. A distribuição dos modelos pelos dois programas e equipamentos decorreu "
    "da disponibilidade dos projectos de preparação e das condições operacionais de cada impressão. Não "
    "foi desenhado um ensaio comparativo: a mesma geometria não foi produzida em condições equivalentes "
    "nos dois sistemas, pelo que estes registos não permitem inferir superioridade ou equivalência entre "
    "os programas de fatiamento ou entre as impressoras."
)

FLEXY_ORIGIN = (
    "Na documentação original, o Flexy Beast é apresentado como uma combinação do Parametric Cyborg "
    "Beast, de MakerBlock, com o Flexy Hand, de Steve Wood/Gyrobot. Herda deste último juntas flexíveis "
    "que substituem os parafusos Chicago e os elásticos de retorno presentes em modelos anteriores. A "
    "fonte recomenda Filaflex ou silicone moldado para essas juntas e prevê almofadas removíveis de "
    "silicone nos dedos para aumentar a aderência. Trata-se, assim, de uma arquitectura material concebida "
    "para combinar componentes estruturais rígidos com elementos flexíveis funcionalmente diferenciados "
    "(daprice, n.d.). As vantagens de peso, custo, adaptação a escalas menores e facilidade de montagem "
    "referidas na documentação de origem são características declaradas pelo autor do modelo, não "
    "resultados avaliados nesta dissertação."
)

MATERIAL_SCOPE = (
    "Os dois projectos Bambu contêm três materiais disponíveis na configuração, mas as peças presentes "
    "estão atribuídas ao extrusor 1, identificado como PLA. Embora a documentação de origem do Flexy Beast "
    "preveja juntas em filamento flexível ou silicone moldado, os segmentos testados nesta investigação "
    "foram produzidos com filamento rígido, registado no projecto como PLA. Não foram produzidas as juntas "
    "flexíveis nem as almofadas de silicone dos dedos. Por conseguinte, não foram avaliados o comportamento "
    "elástico das juntas, o retorno dos dedos, a aderência das almofadas ou a influência desses componentes "
    "na montagem e no funcionamento do dispositivo. A documentação disponível também não permite uma "
    "comparação controlada entre PLA e PETG; não se retiram, portanto, conclusões sobre resistência, "
    "fragilidade ou durabilidade relativas dos materiais."
)

PRINTER_SCOPE = (
    "A utilização da Bambu Lab A1 e da Prusa MINI documenta a execução do fluxo em dois ambientes de "
    "fabrico, mas não constitui uma comparação entre equipamentos. Os modelos, os programas de fatiamento "
    "e parte das definições de preparação diferem entre os projectos, e nenhuma geometria equivalente foi "
    "repetida nas duas impressoras sob condições controladas. Não é, por isso, possível isolar o efeito da "
    "impressora, comparar qualidade ou velocidade, nem concluir que o fluxo exige dois equipamentos."
)

FUTURE = (
    "A terceira etapa deve avaliar fabrico e função por protocolos separados. Os ensaios devem comparar "
    "materiais e impressoras com corpos de prova e componentes equivalentes, medir folgas e montagem, e "
    "aplicar testes de carga, fadiga e desgaste adequados ao uso previsto. No Flexy Beast, esta etapa deve "
    "incluir a produção e caracterização das juntas em filamento flexível ou silicone, bem como a "
    "verificação do retorno dos dedos e da aderência das almofadas previstas no modelo original. Só depois "
    "desta caracterização deve avançar uma avaliação com participantes e profissionais, mediante "
    "enquadramento ético e clínico apropriado."
)

BIBLIOGRAPHY = (
    "daprice. (n.d.). Flexy Beast [README file]. GitHub. Retrieved July 13, 2026, from "
    "https://github.com/daprice/Flexy-Beast/blob/master/README.md"
)


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(paragraph_text(p) == FLEXY_ORIGIN for p in body_paragraphs(root)):
        for caption_text in [
            "Tabela 8.2 — Projectos de preparação digital para impressão 3D com configuração analisada",
            "Tabela 8.3 — Inspecção computacional de malhas na configuração infantil",
        ]:
            prevent_table_row_splitting(root, caption_text)
        return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")

    version_paragraphs = [
        p for p in body_paragraphs(root) if paragraph_text(p) == "Versão do documento: 0.4.30"
    ]
    if len(version_paragraphs) > 1:
        raise RuntimeError("Found more than one DOCX version paragraph")
    if version_paragraphs:
        set_paragraph_text(version_paragraphs[0], "Versão do documento: 0.4.31")
    replace_prefix(root, "Os modelos foram preparados no PrusaSlicer", METHOD)

    origin_cell = find_prefix(root, "Flexy-Beast de daprice")
    set_paragraph_text(
        origin_cell,
        "Adaptação do Flexy-Beast de daprice, combinação do Parametric Cyborg Beast e do Flexy Hand; "
        "CC BY-SA 4.0, indicada no ficheiro-fonte",
    )

    counts = find_prefix(root, "As contagens referem-se às declarações presentes")
    origin_paragraph = deepcopy(counts)
    set_paragraph_text(origin_paragraph, FLEXY_ORIGIN)
    counts.addprevious(origin_paragraph)

    material = replace_prefix(root, "Os dois projectos Bambu contêm três materiais", MATERIAL_SCOPE)
    printer = deepcopy(material)
    set_paragraph_text(printer, PRINTER_SCOPE)
    material.addnext(printer)

    replace_prefix(root, "A terceira etapa deve avaliar fabrico e função", FUTURE)

    bibliography_anchor = find_prefix(root, "da Silveira Romero, R. C.")
    bibliography_entry = deepcopy(bibliography_anchor)
    set_paragraph_text(bibliography_entry, BIBLIOGRAPHY)
    bibliography_anchor.addnext(bibliography_entry)

    for caption_text in [
        "Tabela 8.2 — Projectos de preparação digital para impressão 3D com configuração analisada",
        "Tabela 8.3 — Inspecção computacional de malhas na configuração infantil",
    ]:
        prevent_table_row_splitting(root, caption_text)

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()

    source = args.docx.resolve()
    if not source.exists():
        raise SystemExit(f"DOCX not found: {source}")

    with ZipFile(source, "r") as archive:
        document_xml = archive.read("word/document.xml")
        updated_xml = apply(document_xml)

        fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=source.parent)
        os.close(fd)
        temp_path = Path(temp_name)
        try:
            with ZipFile(temp_path, "w", ZIP_DEFLATED) as output:
                for item in archive.infolist():
                    data = updated_xml if item.filename == "word/document.xml" else archive.read(item.filename)
                    output.writestr(item, data)
            temp_path.replace(source)
        finally:
            temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
