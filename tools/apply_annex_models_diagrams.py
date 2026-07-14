#!/usr/bin/env python3
"""Synchronise the Annex A, model inventory and Chapter 5 diagrams in the DOCX.

The script edits the existing OOXML package in place so the IPCA template,
styles, pagination settings and pre-existing media remain intact.
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
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS = {"w": W, "r": R, "wp": WP, "a": A}


def qn(namespace: str, name: str) -> str:
    return f"{{{namespace}}}{name}"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_paragraph_text(paragraph: etree._Element, text: str, *, bold: bool = False, size: int | None = None) -> None:
    p_pr = paragraph.find(qn(W, "pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn(W, "r"))
    if bold or size:
        r_pr = etree.SubElement(run, qn(W, "rPr"))
        if bold:
            etree.SubElement(r_pr, qn(W, "b"))
        if size:
            etree.SubElement(r_pr, qn(W, "sz")).set(qn(W, "val"), str(size))
            etree.SubElement(r_pr, qn(W, "szCs")).set(qn(W, "val"), str(size))
    node = etree.SubElement(run, qn(W, "t"))
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


def cell_text(cell: etree._Element) -> str:
    return "".join(cell.xpath(".//w:t/text()", namespaces=NS))


def set_cell_text(cell: etree._Element, text: str, *, bold: bool = False, size: int | None = None) -> None:
    paragraphs = cell.findall(qn(W, "p"))
    template = paragraphs[0] if paragraphs else etree.Element(qn(W, "p"))
    for paragraph in paragraphs:
        cell.remove(paragraph)
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, text, bold=bold, size=size)
    cell.append(paragraph)


def find_row(root: etree._Element, first_cell: str) -> etree._Element:
    matches = []
    for row in root.xpath(".//w:tr", namespaces=NS):
        cells = row.findall(qn(W, "tc"))
        if cells and cell_text(cells[0]) == first_cell:
            matches.append(row)
    if len(matches) != 1:
        raise RuntimeError(f"Expected one row beginning {first_cell!r}; found {len(matches)}")
    return matches[0]


def replace_body_reference(root: etree._Element, prefix: str, old: str, new: str) -> None:
    paragraph = find_paragraph_prefix(root, prefix)
    text = paragraph_text(paragraph)
    if old not in text:
        raise RuntimeError(f"{old!r} not found in paragraph {text!r}")
    set_paragraph_text(paragraph, text.replace(old, new, 1))


def make_table(old_table: etree._Element, rows: list[list[str]], widths: list[int]) -> etree._Element:
    table = etree.Element(qn(W, "tbl"))
    old_pr = old_table.find(qn(W, "tblPr"))
    table_pr = deepcopy(old_pr) if old_pr is not None else etree.Element(qn(W, "tblPr"))
    layout = table_pr.find(qn(W, "tblLayout"))
    if layout is None:
        layout = etree.SubElement(table_pr, qn(W, "tblLayout"))
    layout.set(qn(W, "type"), "fixed")
    table.append(table_pr)

    grid = etree.SubElement(table, qn(W, "tblGrid"))
    for width in widths:
        etree.SubElement(grid, qn(W, "gridCol")).set(qn(W, "w"), str(width))

    for row_index, row_values in enumerate(rows):
        row = etree.SubElement(table, qn(W, "tr"))
        if row_index == 0:
            row_pr = etree.SubElement(row, qn(W, "trPr"))
            etree.SubElement(row_pr, qn(W, "tblHeader"))
        for value, width in zip(row_values, widths, strict=True):
            cell = etree.SubElement(row, qn(W, "tc"))
            cell_pr = etree.SubElement(cell, qn(W, "tcPr"))
            cell_width = etree.SubElement(cell_pr, qn(W, "tcW"))
            cell_width.set(qn(W, "w"), str(width))
            cell_width.set(qn(W, "type"), "dxa")
            paragraph = etree.SubElement(cell, qn(W, "p"))
            set_paragraph_text(paragraph, value, bold=row_index == 0, size=15)
    return table


def add_image_relationship(rels_root: etree._Element, target: str) -> str:
    ids = []
    for rel in rels_root.findall(qn(REL, "Relationship")):
        rel_id = rel.get("Id", "")
        if rel_id.startswith("rId") and rel_id[3:].isdigit():
            ids.append(int(rel_id[3:]))
    rel_id = f"rId{max(ids, default=0) + 1}"
    relationship = etree.SubElement(rels_root, qn(REL, "Relationship"))
    relationship.set("Id", rel_id)
    relationship.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
    relationship.set("Target", target)
    return rel_id


def prepare_image_paragraph(template: etree._Element, rel_id: str, root: etree._Element) -> etree._Element:
    image_paragraph = deepcopy(template)
    blips = image_paragraph.xpath(".//a:blip", namespaces=NS)
    if len(blips) != 1:
        raise RuntimeError(f"Expected one image in Figure 5.2 paragraph; found {len(blips)}")
    blips[0].set(qn(R, "embed"), rel_id)

    width = 5_303_520  # 5.8 inches
    height = 4_607_000  # preserves the 1809 × 1572 source ratio
    for extent in image_paragraph.xpath(".//wp:extent | .//a:xfrm/a:ext", namespaces=NS):
        extent.set("cx", str(width))
        extent.set("cy", str(height))

    existing_ids = [int(value) for value in root.xpath(".//wp:docPr/@id", namespaces=NS) if str(value).isdigit()]
    next_id = max(existing_ids, default=0) + 1
    for doc_pr in image_paragraph.xpath(".//wp:docPr", namespaces=NS):
        doc_pr.set("id", str(next_id))
        doc_pr.set("name", "Diagrama de sequência perfil-IA-OpenSCAD-exportação")
        doc_pr.set("descr", "Sequência desde o perfil antropométrico até à exportação da geometria")
    for c_nv_pr in image_paragraph.xpath(".//a:cNvPr", namespaces=NS):
        c_nv_pr.set("id", str(next_id))
        c_nv_pr.set("name", "sequencia_perfil_ia_openscad_exportacao.png")
    return image_paragraph


def apply_changes(document_xml: bytes, rels_xml: bytes, image_bytes: bytes) -> tuple[bytes, bytes, str]:
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(document_xml, parser)
    rels_root = etree.fromstring(rels_xml, parser)

    # Version and list entries.
    version_paragraphs = [
        p for p in root.xpath(".//w:p", namespaces=NS)
        if paragraph_text(p) == "Versão do documento: 0.4.27"
    ]
    if len(version_paragraphs) > 1:
        raise RuntimeError("More than one manuscript version paragraph found")
    if version_paragraphs:
        set_paragraph_text(version_paragraphs[0], "Versão do documento: 0.4.28")

    def set_index_entry(paragraph: etree._Element, label: str, description: str, page: str) -> None:
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if len(text_nodes) != 2:
            raise RuntimeError(f"Unexpected index paragraph structure: {paragraph_text(paragraph)!r}")
        text_nodes[0].text = f"{label} — {description}"
        text_nodes[1].text = page

    table_52_index = find_paragraph(root, "Tabela 5.2 — Estado dos modelos no fecho do estudo71")
    set_index_entry(table_52_index, "Tabela 5.2", "Inventário consolidado dos modelos no fecho do estudo", "71")

    figure_52_index = find_paragraph(
        root,
        "Figura 5.2 — Arquitectura e sequência principal entre interface, configuração, Web Worker, OpenSCAD em WebAssembly, visualização, serviços do servidor, IA externa e fabrico.64",
    )
    figure_53_index = find_paragraph(
        root,
        "Figura 5.3 — Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo.65",
    )
    figure_54_index = find_paragraph(
        root,
        "Figura 5.4 — Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso.69",
    )
    set_index_entry(figure_54_index, "Figura 5.5", "Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso.", "69")
    set_index_entry(figure_53_index, "Figura 5.4", "Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo.", "65")
    set_index_entry(figure_52_index, "Figura 5.2", "Arquitectura da plataforma e fronteiras entre navegador, servidor, serviço externo de IA e preparação do fabrico.", "63")
    new_figure_index = deepcopy(figure_53_index)
    set_index_entry(new_figure_index, "Figura 5.3", "Sequência de dados e decisões desde o perfil ou descrição até à sugestão, confirmação, geração determinística e exportação.", "64")
    figure_52_index.addnext(new_figure_index)

    # Keep the static table of contents aligned with the two new Annex A subsections.
    def set_tabbed_entry(paragraph: etree._Element, title: str, page: str) -> None:
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if len(text_nodes) != 2:
            raise RuntimeError(f"Unexpected contents paragraph structure: {paragraph_text(paragraph)!r}")
        text_nodes[0].text = title
        text_nodes[1].text = page

    toc_a1 = find_paragraph(root, "A.1 Contexto e Objectivo115")
    toc_a21 = find_paragraph(root, "A.2.1 Pesquisa bibliográfica orientada115")
    toc_a8 = find_paragraph(root, "A.8 Escrita do Código de Geração123")
    toc_a9 = find_paragraph(root, "A.9 Resultado Final123")
    toc_a10 = find_paragraph(root, "A.10 Cobertura Global da Base de Dados e Lacunas123")
    toc_a11 = deepcopy(toc_a21)
    set_tabbed_entry(toc_a11, "A.1.1 Localização, versão e integridade dos ficheiros", "115")
    toc_a1.addnext(toc_a11)
    toc_a81 = deepcopy(toc_a21)
    set_tabbed_entry(toc_a81, "A.8.1 Correspondência entre os CSV e os parâmetros da plataforma", "124")
    toc_a8.addnext(toc_a81)
    set_tabbed_entry(toc_a9, "A.9 Resultado Final", "124")
    set_tabbed_entry(toc_a10, "A.10 Cobertura Global da Base de Dados e Lacunas", "125")

    # Existing Figure 5.3 and 5.4 become Figure 5.4 and 5.5.
    replace_body_reference(root, "A Figura 5.4 ilustra", "A Figura 5.4", "A Figura 5.5")
    replace_body_reference(root, "Figura 5.4 — Ferramenta", "Figura 5.4", "Figura 5.5")
    replace_body_reference(root, "A Figura 5.3 apresenta", "A Figura 5.3", "A Figura 5.4")
    replace_body_reference(root, "Figura 5.3 — Fluxo", "Figura 5.3", "Figura 5.4")

    figure_52_caption = find_paragraph(
        root,
        "Figura 5.2 — Arquitectura e sequência principal entre interface, configuração, Web Worker, OpenSCAD em WebAssembly, visualização, serviços do servidor, IA externa e fabrico.",
    )
    set_paragraph_text(
        figure_52_caption,
        "Figura 5.2 — Arquitectura da plataforma e fronteiras entre navegador, servidor, serviço externo de IA e preparação do fabrico.",
    )
    figure_52_source = figure_52_caption.getnext()
    while figure_52_source is not None and paragraph_text(figure_52_source) != "Fonte: produção própria.":
        figure_52_source = figure_52_source.getnext()
    if figure_52_source is None:
        raise RuntimeError("Could not locate Figure 5.2 source paragraph")
    figure_52_image = figure_52_caption.getprevious()
    while figure_52_image is not None and not figure_52_image.xpath(".//w:drawing", namespaces=NS):
        figure_52_image = figure_52_image.getprevious()
    if figure_52_image is None:
        raise RuntimeError("Could not locate Figure 5.2 image paragraph")

    rel_id = add_image_relationship(rels_root, "media/sequencia_perfil_ia_openscad_exportacao.png")
    narrative_template = find_paragraph_prefix(root, "A Figura 5.4 apresenta")
    narrative = clone_paragraph(
        narrative_template,
        "A Figura 5.3 detalha a sequência operacional que a representação arquitectural não explicita. O perfil ou a descrição é primeiro relacionado, no servidor, com uma referência antropométrica; a IA externa apenas sugere valores iniciais condicionados pelo esquema do modelo; o servidor filtra a resposta; e a configuração só é aplicada após revisão humana. A geração da geometria permanece determinística no OpenSCAD executado no navegador, sendo a exportação uma decisão posterior à pré-visualização.",
    )
    sequence_image = prepare_image_paragraph(figure_52_image, rel_id, root)
    sequence_caption = clone_paragraph(
        figure_52_caption,
        "Figura 5.3 — Sequência de dados e decisões desde o perfil ou descrição até à sugestão, confirmação, geração determinística e exportação.",
    )
    sequence_source = clone_paragraph(figure_52_source, "Fonte: produção própria.")
    insertion_point = figure_52_source
    for element in (narrative, sequence_image, sequence_caption, sequence_source):
        insertion_point.addnext(element)
        insertion_point = element

    # Replace the minimal model-state table with the consolidated inventory.
    model_caption = find_paragraph(root, "Tabela 5.2 — Estado dos modelos no fecho do estudo")
    set_paragraph_text(model_caption, "Tabela 5.2 — Inventário consolidado dos modelos no fecho do estudo")
    old_model_table = model_caption.getnext()
    while old_model_table is not None and old_model_table.tag != qn(W, "tbl"):
        old_model_table = old_model_table.getnext()
    if old_model_table is None:
        raise RuntimeError("Could not locate Table 5.2")
    inventory_rows = [
        ["Modelo, versão e estado", "Origem e licença", "Parâmetros configuráveis", "Mecanismo de escala implementado", "Ensaios e evidência no estudo"],
        ["Flexy Beast; plataforma 14.67.0; activo", "Flexy-Beast de daprice; CC BY-SA 4.0", "51 declarações; 15 numéricas: palma, dedos, articulações, braçadeira e pino", "(largura da palma + 5) / 55; dedos independentes", "Dimensional, IA, exportação, malha, projecto Bambu A1 e série física"],
        ["Paraglider/Flexible Flyer; plataforma 14.67.0; activo", "M. Mendenhall (2020), CC BY-SA 4.0; dependências CC BY 3.0 e CC BY-NC-SA 4.0", "42 declarações; 15 numéricas: palma, dedos, canais e braço", "Palma uniforme para preservar furos; dedos independentes", "Dimensional, IA, exportação, malha, projecto Prusa MINI e série física"],
        ["UnLimbited Phoenix V1.0; plataforma 14.67.0; activo", "UnLimbited/e-NABLE; CC BY-NC-SA 4.0", "31 declarações; 12 numéricas: palma, escala e segmentos digitais", "Referência de 82 mm; escala uniforme limitada a 100%–160%", "Dimensional, IA, exportação, malha e projecto Bambu A1"],
        ["Cyborg Beast; plataforma 14.67.0; activo", "MakerBlock/e-NABLE; licença não explicitada no pacote local", "50 declarações; 17 numéricas: palma, dedos, punho, braçadeira e pino", "(largura da palma + 5) / 55; segmentos digitais independentes", "Integração e renderização; excluído da comparação e das séries físicas"],
        ["pec Phoenix hand; desenvolvimento; não registado", "Reconstrução baseada na linhagem Phoenix; licença do derivado não formalizada", "Sem contrato consolidado em models-config.json", "Mecanismo não estabilizado na configuração comum", "Material exploratório; excluído dos ensaios comparativos"],
    ]
    old_model_table.addnext(make_table(old_model_table, inventory_rows, [1500, 1800, 1850, 1850, 2200]))
    old_model_table.getparent().remove(old_model_table)
    model_followup = find_paragraph_prefix(root, "A integração consistiu em traduzir")
    model_followup.addprevious(
        clone_paragraph(
            model_followup,
            "As contagens referem-se às declarações presentes em models/models-config.json no estado versionado da plataforma 14.67.0. O total inclui selectores, opções de visualização e controlos não geométricos; a contagem numérica identifica os campos do tipo number, sem pressupor que todos representam medidas antropométricas. A ausência de licença explícita no pacote local do Cyborg Beast é registada como lacuna documental e não como afirmação de inexistência de licença na fonte original.",
        )
    )

    # Annex A: deposit/version/integrity record.
    a2_heading = find_paragraph(root, "A.2 Estratégia de Pesquisa Bibliográfica")
    normal_template = find_paragraph_prefix(root, "O desenvolvimento de um gerador paramétrico")
    heading_template = a2_heading
    annex_intro = [
        clone_paragraph(heading_template, "A.1.1 Localização, versão e integridade dos ficheiros"),
        clone_paragraph(normal_template, "Os três CSV e os dois scripts de geração foram depositados com a dissertação em sources/manuscript/annexes/dados_antropometricos_v14.67.0/. O suplemento corresponde ao estado versionado da plataforma HandFab 14.67.0, confirmação Git bcef0db, anterior às alterações experimentais posteriores. A pasta inclui README.md, com a origem e o procedimento de regeneração, e SHA256SUMS, para verificar a integridade dos cinco artefactos."),
    ]
    checksum_lines = [
        "• ansur_1988_complete.csv — 88575ef62771f8be1abefeba070426d4eab3d6a4005618b064df603024ccff4d",
        "• ansur_1988_hand_arm.csv — 82a010b2b38579b11c0eaa3d9488895350807647220c30c78650331297f8c503",
        "• multi_population_hand.csv — 65b7e8b88e7d1abb3460342179f7360f2b69df8b77c8f6a992881eb496999a8f",
        "• generate_ansur_csv.py — 63eae7b39a9e47054be1ae2cec8a8035f419cb50a78c818eb296f640eb9639d3",
        "• generate_multi_population_hand_csv.py — 5ab4fcba62a4c001ff8347c8858b28631537aadc0ad4bf8aa4cb75b96a949ae3",
    ]
    annex_intro.extend(clone_paragraph(normal_template, line) for line in checksum_lines)
    annex_intro.append(
        clone_paragraph(normal_template, "Em 13 de Julho de 2026, os dois scripts foram executados novamente dentro da pasta suplementar. A regeneração produziu 2.726 linhas de dados no ficheiro ANSUR completo, 696 no subconjunto mão–braço e 1.790 na base multipopulacional; a verificação com sha256sum -c SHA256SUMS confirmou correspondência integral dos cinco ficheiros. Estes resultados demonstram repetibilidade técnica no mesmo ambiente e estado de código, não reprodução independente por outra equipa.")
    )
    for element in annex_intro:
        a2_heading.addprevious(element)

    anomaly = find_paragraph_prefix(root, "Notas: o código regista oito anomalias")
    set_paragraph_text(
        anomaly,
        "Notas: a auditoria ao código e ao documento de origem identificou oito células anómalas, classificadas como seis normalizações ou correcções e dois valores preservados com advertência. Esta enumeração substitui a formulação imprecisa de «sete correcções». Cinco valores em centímetros foram corrigidos com apoio na coluna em polegadas ou na sequência estatística: página 8, percentil 40 feminino, 74,93 para 71,93 cm; página 37, percentil 1 feminino, 35,55 para 53,55 cm; página 42, percentil 65 masculino, 507,19 para 207,19 cm; página 44, percentil 95 feminino, 1143,33 para 114,33 cm; e página 45, percentil 2 masculino, 35,31 para 25,31 cm. Na página 25, a impressão «59397» na coluna em polegadas foi normalizada para 59,97 in apenas para apresentação, porque o valor de 152,32 cm já estava correcto. Na página 40, o mínimo feminino de 11,70 cm foi mantido e assinalado como provável erro; na página 46, o desvio-padrão masculino de 0,52 cm foi igualmente mantido e marcado como incerto, pois a coluna em polegadas indica cerca de 3,53 cm. Cada caso fica descrito no campo dataqualitynote, permitindo distinguir alterações efectuadas de valores apenas sinalizados.",
    )

    a9_heading = find_paragraph(root, "A.9 Resultado Final")
    mapping_elements = [
        clone_paragraph(heading_template, "A.8.1 Correspondência entre os CSV e os parâmetros da plataforma"),
        clone_paragraph(normal_template, "Os CSV não são enviados directamente ao modelo OpenSCAD nem constituem registos individuais. O importador agrega as linhas estatísticas por população, sexo, grupo etário e tipo de estatística, guarda os perfis normalizados na base app.db e organiza as medidas numa árvore measurements. A correspondência posterior é executada pelo serviço determinístico server/services/profileMapping.js, no estado versionado da plataforma 14.67.0. Este serviço é partilhado pela aplicação da configuração de referência e pela construção do contexto antropométrico enviado à IA."),
        clone_paragraph(normal_template, "O mapeamento canónico liga palm.width_mm, palm.length_mm e palm.thickness_mm aos parâmetros da palma; os comprimentos totais e proximais dos cinco dedos aos parâmetros *_finger_length_mm e *_base_length_mm; e wrist.circumference_mm a wrist_circumference_mm. Um valor só é aplicado quando o parâmetro existe no modelo activo, é numérico, pertence a este mapa e contém uma medida finita e positiva. O valor é arredondado a uma casa decimal e limitado ao mínimo e ao máximo declarados em models/models-config.json; parâmetros em falta permanecem por configurar e parâmetros mecânicos, de visualização ou de lateralidade não são alterados."),
        clone_paragraph(normal_template, "Quando a entrada é uma descrição textual, a selecção da referência populacional usa uma pontuação determinística baseada em sexo, categoria e proximidade etária, menção explícita do país e qualidade do subconjunto, aceitando apenas resultados acima do limiar codificado. Se o país descrito não estiver presente na base, não é atribuído qualquer ponto de correspondência nacional; o sistema pode seleccionar um grupo pelos restantes campos, mas essa escolha é apenas uma referência aproximada. As médias orientam a configuração inicial e o contexto da IA, sem substituir medidas directas nem demonstrar ajuste anatómico individual."),
        clone_paragraph(normal_template, "Este encadeamento separa a linha estatística do CSV, o perfil populacional agregado, os parâmetros compatíveis com o modelo activo e a geometria gerada após confirmação humana. A rastreabilidade pode, assim, ser reconstruída desde a fonte e página registadas no CSV até ao caminho antropométrico, ao nome do parâmetro e ao limite aplicado pelo modelo."),
    ]
    for element in mapping_elements:
        a9_heading.addprevious(element)

    result_header = find_paragraph(root, "FicheiroLinhas (dados)PaísesEstudosDimensões distintas") if False else None
    result_table = a9_heading.getnext()
    while result_table is not None and result_table.tag != qn(W, "tbl"):
        result_table = result_table.getnext()
    if result_table is None:
        raise RuntimeError("Could not locate Annex A result table")
    result_rows = result_table.findall(qn(W, "tr"))
    header_cells = result_rows[0].findall(qn(W, "tc"))
    set_cell_text(header_cells[3], "Fontes ou subconjuntos")
    multi_cells = result_rows[3].findall(qn(W, "tc"))
    if cell_text(multi_cells[0]) != "data/multi_population_hand.csv":
        raise RuntimeError("Unexpected Annex A result table layout")
    set_cell_text(multi_cells[3], "12")
    result_table.addnext(
        clone_paragraph(normal_template, "Estes totais foram confirmados pela regeneração do suplemento dados_antropometricos_v14.67.0, associado à confirmação Git bcef0db. A contagem de 12 corresponde a documentos-fonte ou subconjuntos identificados pelo gerador e não implica 12 estudos primários independentes.")
    )

    return (
        etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes"),
        etree.tostring(rels_root, xml_declaration=True, encoding="UTF-8", standalone="yes"),
        rel_id,
    )


def rewrite_docx(docx_path: Path, image_path: Path) -> None:
    with ZipFile(docx_path, "r") as source:
        entries = {info.filename: (info, source.read(info.filename)) for info in source.infolist()}

    document_xml, rels_xml, _ = apply_changes(
        entries["word/document.xml"][1],
        entries["word/_rels/document.xml.rels"][1],
        image_path.read_bytes(),
    )
    entries["word/document.xml"] = (entries["word/document.xml"][0], document_xml)
    entries["word/_rels/document.xml.rels"] = (entries["word/_rels/document.xml.rels"][0], rels_xml)
    media_name = "word/media/sequencia_perfil_ia_openscad_exportacao.png"
    if media_name in entries:
        raise RuntimeError(f"Media entry already exists: {media_name}")

    fd, temporary_name = tempfile.mkstemp(prefix="docx-update-", suffix=".docx", dir=docx_path.parent)
    os.close(fd)
    temporary_path = Path(temporary_name)
    try:
        with ZipFile(temporary_path, "w", compression=ZIP_DEFLATED) as target:
            for filename, (info, data) in entries.items():
                target.writestr(info, data)
            target.writestr(media_name, image_path.read_bytes())
        os.replace(temporary_path, docx_path)
    finally:
        temporary_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("image", type=Path)
    args = parser.parse_args()
    rewrite_docx(args.docx.resolve(), args.image.resolve())


if __name__ == "__main__":
    main()
