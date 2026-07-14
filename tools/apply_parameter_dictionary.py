#!/usr/bin/env python3
"""Insert the Chapter 4 parameter dictionary and numerical trace into the DOCX.

The existing OOXML package is edited in place so the IPCA template, styles,
section settings and media remain intact. The operation is intentionally
specific to manuscript version 0.4.28/0.4.29 and fails if the expected anchors
are absent or if the new sections already exist.
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


def set_paragraph_text(
    paragraph: etree._Element,
    text: str,
    *,
    bold: bool = False,
    size: int | None = None,
    italic: bool = False,
) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    if bold or size or italic:
        r_pr = etree.SubElement(run, qn("rPr"))
        if bold:
            etree.SubElement(r_pr, qn("b"))
        if italic:
            etree.SubElement(r_pr, qn("i"))
        if size:
            etree.SubElement(r_pr, qn("sz")).set(qn("val"), str(size))
            etree.SubElement(r_pr, qn("szCs")).set(qn("val"), str(size))
    node = etree.SubElement(run, qn("t"))
    if text.startswith(" ") or text.endswith(" "):
        node.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    node.text = text


def clone_paragraph(template: etree._Element, text: str) -> etree._Element:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, text)
    return paragraph


def find_paragraph(root: etree._Element, text: str) -> etree._Element:
    matches = [p for p in root.xpath(".//w:p", namespaces=NS) if paragraph_text(p) == text]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph {text!r}; found {len(matches)}")
    return matches[0]


def find_paragraph_prefix(root: etree._Element, prefix: str) -> etree._Element:
    matches = [p for p in root.xpath(".//w:p", namespaces=NS) if paragraph_text(p).startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def set_tabbed_entry(paragraph: etree._Element, title: str, page: str) -> None:
    text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if len(text_nodes) != 2:
        raise RuntimeError(f"Unexpected index paragraph structure: {paragraph_text(paragraph)!r}")
    text_nodes[0].text = title
    text_nodes[1].text = page


def set_cell_text(cell: etree._Element, text: str, *, bold: bool, size: int) -> None:
    paragraph = etree.SubElement(cell, qn("p"))
    p_pr = etree.SubElement(paragraph, qn("pPr"))
    spacing = etree.SubElement(p_pr, qn("spacing"))
    spacing.set(qn("before"), "0")
    spacing.set(qn("after"), "0")
    spacing.set(qn("line"), "220")
    spacing.set(qn("lineRule"), "auto")
    set_paragraph_text(paragraph, text, bold=bold, size=size)


def make_table(template: etree._Element, rows: list[list[str]], widths: list[int], *, size: int) -> etree._Element:
    table = etree.Element(qn("tbl"))
    old_pr = template.find(qn("tblPr"))
    table_pr = deepcopy(old_pr) if old_pr is not None else etree.Element(qn("tblPr"))
    layout = table_pr.find(qn("tblLayout"))
    if layout is None:
        layout = etree.SubElement(table_pr, qn("tblLayout"))
    layout.set(qn("type"), "fixed")
    table.append(table_pr)

    grid = etree.SubElement(table, qn("tblGrid"))
    for width in widths:
        etree.SubElement(grid, qn("gridCol")).set(qn("w"), str(width))

    for row_index, values in enumerate(rows):
        row = etree.SubElement(table, qn("tr"))
        row_pr = etree.SubElement(row, qn("trPr"))
        if row_index == 0:
            etree.SubElement(row_pr, qn("tblHeader"))
        etree.SubElement(row_pr, qn("cantSplit"))
        for value, width in zip(values, widths, strict=True):
            cell = etree.SubElement(row, qn("tc"))
            cell_pr = etree.SubElement(cell, qn("tcPr"))
            cell_width = etree.SubElement(cell_pr, qn("tcW"))
            cell_width.set(qn("w"), str(width))
            cell_width.set(qn("type"), "dxa")
            set_cell_text(cell, value, bold=row_index == 0, size=size)
    return table


DICTIONARY_ROWS = [
    ["Modelo e parâmetro", "Significado e origem", "Inicial", "Intervalo; incremento", "Regra ou efeito geométrico"],
    ["Flexy Beast — palm_breadth_mm", "Largura metacarpal; palm.width_mm", "83", "55–110; 1", "Escala uniforme: xScaleFactor = (valor + 5) / 55"],
    ["Flexy Beast — middle_finger_length_mm", "Dobra MCP à ponta do dedo médio; digits.middle.total_length_mm", "72", "40–120; 1", "Comprimento mestre: fingerLength = valor / (37 × xScaleFactor)"],
    ["Flexy Beast — index_finger_length_mm; ring_finger_length_mm", "Comprimento total do indicador e anelar", "68; 68", "40–120; 1", "Proporção de cada dedo relativamente ao médio"],
    ["Flexy Beast — pinky_finger_length_mm; thumb_length_mm", "Comprimento total do mindinho e polegar", "55; 65", "30–100; 1; 35–100; 1", "Proporção local relativamente ao dedo médio"],
    ["Flexy Beast — joint_dia; joint_thick", "Diâmetro do furo e espessura da ranhura da junta flexível", "7; 4", "4–10; 0,5; 1–6; 0,5", "Dimensionam furos, ranhuras e conectores flexíveis; não são medidas corporais"],
    ["Flexy Beast — gauntlet_width_mm; gauntlet_length_mm; gauntlet_wall_mm", "Largura, comprimento e parede da braçadeira", "60; 108; 3", "40–90; 1; 70–150; 1; 2–5; 0,5", "Escala e espessura da braçadeira; a largura pode derivar do punho com folga"],
    ["Flexy Beast — gauntlet_pos_adjust; strap_splay_adjust", "Ajuste longitudinal e afastamento das abas", "0; 0", "−25–25; 1; −8–8; 0,5", "Correcções locais de posição e compatibilidade; introdução manual"],
    ["Flexy Beast — wrist_pin_dia; wrist_pin_clearance", "Diâmetro do pino do punho e folga de rotação", "7; 0,35", "3–8; 0,5; 0,10–0,80; 0,05", "Dimensionam a interface articulada entre palma e braçadeira"],
    ["Paraglider — palm_breadth_mm", "Largura metacarpal; palm.width_mm", "83", "55–110; 1", "overall_scale = valor / 66,4; palma escalada uniformemente"],
    ["Paraglider — palm_length_mm; palm_thickness_mm", "Comprimento e espessura da palma", "95; 32", "60–140; 1; 18–50; 1", "Informação contextual para a IA; não deforma independentemente a palma"],
    ["Paraglider — index_finger_length_mm; middle_finger_length_mm; ring_finger_length_mm", "Comprimentos totais do indicador, médio e anelar", "68; 72; 68", "40–120; 1", "Escalas próprias dos dedos; o médio define a escala-base digital"],
    ["Paraglider — pinky_finger_length_mm; thumb_length_mm", "Comprimentos totais do mindinho e polegar", "55; 65", "30–100; 1; 35–100; 1", "O mindinho recebe escala própria; o polegar acompanha a escala-base"],
    ["Paraglider — string_channel_scale; elastic_channel_scale", "Escala relativa dos canais de tracção e de elástico", "0,9; 0,9", "0,50–1,00; 0,05; 0,50–1,50; 0,05", "Razões adimensionais aplicadas aos canais mecânicos"],
    ["Paraglider — ARM_HandLen; ARM_ForearmLen; ARM_BicepCircum; ARM_CuffLength", "Mão, antebraço, circunferência do braço e braçadeira", "135; 140; 160; 65", "135–230; 120–315; 110–350; 65–90; inc. 1", "Dimensionam a extensão opcional do braço; não entraram na comparação da mão"],
    ["Paraglider — ARM_PinHoleDia", "Diâmetro dos furos das articulações do braço", "3", "3–6; 1", "Interface mecânica da extensão opcional do braço"],
    ["UnLimbited Phoenix — palm_breadth_mm", "Largura metacarpal; palm.width_mm", "82", "82–131; 1", "HandPerc = valor / 82 × 100, limitado a 100%–160%"],
    ["UnLimbited Phoenix — HandPerc_override", "Substituição manual da percentagem de escala", "0", "0–160; 1", "Zero deriva a escala; valores positivos continuam sujeitos ao piso de 100%"],
    ["UnLimbited Phoenix — index_; middle_; ring_; pinky_finger_length_mm", "Comprimentos totais dos quatro dedos", "72 cada", "55–115; 1", "Alongamento dos segmentos, preservando a circularidade dos furos"],
    ["UnLimbited Phoenix — index_; middle_; ring_; pinky_base_length_mm", "Comprimentos dos segmentos proximais", "31 cada", "18–55; 1", "Divide o comprimento total entre segmento proximal e ponta"],
    ["UnLimbited Phoenix — thumb_length_mm; thumb_base_length_mm", "Comprimento total e proximal do polegar", "72; 31", "45–80; 1; 18–50; 1", "Alongamento do polegar e divisão proximal–distal"],
]


TRACE_ROWS = [
    ["Etapa", "Operação ou evidência", "Valor obtido"],
    ["1. Vector aplicado", "Palma; indicador; médio; anelar; mindinho; polegar", "64; 57; 60; 57; 46; 50 mm"],
    ["2. Verificação pelo esquema", "Comparação com os intervalos da Tabela 4.9", "Seis valores dentro dos intervalos; sem limitação"],
    ["3. Escala global", "xScaleFactor = (64 + 5) / 55", "1,254545"],
    ["4. Multiplicador mestre", "fingerLength = 60 / (37 × 1,254545)", "1,292597"],
    ["5. Proporções digitais", "Indicador/60; médio/60; anelar/60; mindinho/60; polegar/60", "0,950000; 1,000000; 0,950000; 0,766667; 0,833333"],
    ["6. Parâmetros mecânicos", "joint_dia; joint_thick; braçadeira L × C × parede; wrist_pin_dia", "5 mm; 2 mm; 47 × 80 × 2 mm; 5 mm; dentro dos limites"],
    ["7. Malha da palma", "Caixa XYZ; volume; faces; estanquidade", "97,385 × 80,103 × 37,123 mm; 51,381 cm³; 11.186 faces; fechada"],
    ["8. Proximal do dedo médio", "Caixa XYZ; volume; faces; estanquidade", "37,451 × 14,913 × 14,775 mm; 5,225 cm³; 888 faces; fechada"],
    ["9. Distal do dedo médio", "Caixa XYZ; faces; estanquidade", "52,183 × 14,913 × 22,697 mm; 1.198 faces; aberta"],
]


INTRO_49 = (
    "Para tornar auditável a passagem entre dados, configuração e geometria, a Tabela 4.9 consolida os "
    "parâmetros numéricos com efeito antropométrico, geométrico ou mecânico nos três modelos comparados. "
    "O dicionário corresponde à versão 14.67.0 da plataforma. A unidade é o milímetro, "
    "excepto quando a tabela indica percentagem ou razão adimensional. Os valores iniciais constituem a "
    "configuração de referência do modelo; os intervalos são limites de implementação, não limites clínicos."
)

SUPPLEMENT_49 = (
    "O suplemento sources/manuscript/annexes/dicionario_parametros_v14.67.0/parameter_dictionary.csv "
    "preserva as 42 declarações numéricas sem agrupamento, incluindo incremento, grupo funcional, designação "
    "e descrição em português, papel determinístico e exclusão da IA. A tabela no corpo agrupa apenas "
    "variáveis com a mesma origem, intervalo e transformação para manter a legibilidade."
)

AFTER_49 = (
    "O dicionário separa três categorias. Os parâmetros antropométricos podem receber medidas directas ou "
    "referências populacionais; os parâmetros derivados transformam essas entradas segundo fórmulas do "
    "modelo; e os parâmetros mecânicos representam escolhas de projecto, folgas ou interfaces que não devem "
    "ser inferidas como características anatómicas. Parâmetros booleanos de visibilidade, cores, disposição "
    "para impressão e lateralidade permanecem no ficheiro de configuração completo, mas não integram a "
    "Tabela 4.9 por não serem grandezas numéricas."
)

INTRO_410 = (
    "A Tabela 4.10 apresenta um percurso integral preservado na campanha de 8 de Julho de 2026. Para isolar "
    "a transformação geométrica, a entrada efectiva é o vector de medidas aplicado ao modelo, e não a "
    "nacionalidade ou a escolha da referência populacional. O perfil de ensaio descrevia um rapaz de oito "
    "anos, 26 kg, 128 cm de altura, do Brasil e com mãos pequenas. A base não contém uma população brasileira; "
    "embora o registo indique grounded: true, este caso não permite inferir adequação à população indicada. "
    "A sua função é demonstrar como valores aceites pelo esquema chegam a malhas mensuráveis."
)

AFTER_410 = [
    "A ponta do dedo médio é uma casca aberta porque a configuração finger_pads=true reserva a cavidade "
    "destinada à almofada de aderência. Neste caso, a ausência de estanquidade não deve ser ocultada nem "
    "classificada automaticamente como falha de exportação; deve ser interpretada face à intenção construtiva "
    "da peça. A palma e o segmento proximal são sólidos fechados segundo a inspecção computacional realizada.",
    "O percurso evidencia ainda que palm_breadth_mm = 64 não pretende produzir uma caixa envolvente com "
    "exactamente 64 mm. O valor alimenta a fórmula herdada do Cyborg Beast e gera uma escala global aplicada "
    "a uma geometria-base; a caixa envolvente transversal medida foi 80,103 mm. Esta diferença é uma "
    "propriedade explícita da transformação implementada e mostra por que razão a correspondência entre nome "
    "antropométrico e dimensão final deve ser calibrada antes de qualquer afirmação de ajuste anatómico.",
    "Os ficheiros params.json, palm.3mf, middle_base.3mf, middle_tip.3mf e trace.json, os respectivos valores "
    "SHA-256 e o dicionário completo encontram-se em sources/manuscript/annexes/"
    "dicionario_parametros_v14.67.0/. O percurso é reproduzível ao nível do artefacto arquivado e do cálculo; "
    "permanece uma verificação técnica com perfil de ensaio, sem avaliação de conforto, função, segurança ou "
    "validade clínica.",
]


def apply(document_xml: bytes) -> bytes:
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(document_xml, parser)

    if any(paragraph_text(p).startswith("4.3.4 Dicionário operacional") for p in root.xpath(".//w:p", namespaces=NS)):
        raise RuntimeError("The parameter dictionary is already present in the DOCX")

    index_48 = find_paragraph(root, "Tabela 4.8 — Relações paramétricas dos modelos avaliados56")
    index_49 = deepcopy(index_48)
    set_tabbed_entry(index_49, "Tabela 4.9 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados", "57")
    index_410 = deepcopy(index_48)
    set_tabbed_entry(index_410, "Tabela 4.10 — Percurso numérico do vector antropométrico até às malhas do Flexy Beast", "60")
    index_48.addnext(index_410)
    index_48.addnext(index_49)

    toc_433 = find_paragraph(root, "4.3.3 Relações implementadas nos modelos avaliados56")
    toc_434 = deepcopy(toc_433)
    set_tabbed_entry(toc_434, "4.3.4 Dicionário operacional de parâmetros", "57")
    toc_435 = deepcopy(toc_433)
    set_tabbed_entry(toc_435, "4.3.5 Exemplo numérico completo: perfil infantil no Flexy Beast", "60")
    toc_433.addnext(toc_435)
    toc_433.addnext(toc_434)

    heading_template = find_paragraph(root, "4.3.3 Relações implementadas nos modelos avaliados")
    normal_template = find_paragraph_prefix(root, "Os parâmetros de lateralidade constituem uma classe separada.")
    caption_template = find_paragraph(root, "Tabela 4.8 — Relações paramétricas dos modelos avaliados")
    table_template = caption_template.getnext()
    if table_template is None or table_template.tag != qn("tbl"):
        raise RuntimeError("Table 4.8 was not found after its caption")

    heading_44 = find_paragraph(root, "4.4 Iterações, refinamento e discussão intermédia")
    items: list[etree._Element] = [
        clone_paragraph(heading_template, "4.3.4 Dicionário operacional de parâmetros"),
        clone_paragraph(normal_template, INTRO_49),
        clone_paragraph(normal_template, SUPPLEMENT_49),
        clone_paragraph(caption_template, "Tabela 4.9 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados"),
        make_table(table_template, DICTIONARY_ROWS, [1700, 2050, 650, 1450, 3250], size=14),
        clone_paragraph(normal_template, AFTER_49),
        clone_paragraph(heading_template, "4.3.5 Exemplo numérico completo: perfil infantil no Flexy Beast"),
        clone_paragraph(normal_template, INTRO_410),
        clone_paragraph(caption_template, "Tabela 4.10 — Percurso numérico do vector antropométrico até às malhas do Flexy Beast"),
        make_table(table_template, TRACE_ROWS, [1350, 3650, 4100], size=16),
    ]
    items.extend(clone_paragraph(normal_template, text) for text in AFTER_410)

    for item in items:
        heading_44.addprevious(item)

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    path = args.docx.resolve()
    with ZipFile(path, "r") as archive:
        document_xml = archive.read("word/document.xml")
    updated = apply(document_xml)

    fd, temporary = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    try:
        with ZipFile(path, "r") as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                data = updated if item.filename == "word/document.xml" else source.read(item.filename)
                target.writestr(item, data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


if __name__ == "__main__":
    main()
