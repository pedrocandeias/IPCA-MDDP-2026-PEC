#!/usr/bin/env python3
"""Integrar a avaliação manual no Anexo B e converter o Anexo D para A4 vertical.

A alteração é aplicada directamente a ``word/document.xml`` para preservar as
restantes partes do DOCX, incluindo notas de rodapé, comentários, relações e
imagens. As duas tabelas mais largas do Anexo D são reorganizadas para caberem
nas margens da página vertical sem reduzir a informação quantitativa.
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
PROTECTED_PARTS = (
    "word/footnotes.xml",
    "word/comments.xml",
    "word/_rels/document.xml.rels",
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def reference_ids(document_xml: bytes, kind: str) -> tuple[str, ...]:
    root = etree.fromstring(document_xml)
    return tuple(root.xpath(f"//w:{kind}Reference/@w:id", namespaces=NS))


def set_paragraph_text(paragraph: etree._Element, value: str) -> None:
    paragraph_properties = paragraph.find(qn("pPr"))
    first_run_properties = paragraph.find("./w:r/w:rPr", namespaces=NS)
    leading_markers = [
        deepcopy(child)
        for child in paragraph
        if child.tag in (qn("commentRangeStart"), qn("bookmarkStart"))
    ]
    trailing_markers = [
        deepcopy(child)
        for child in paragraph
        if child.tag in (qn("commentRangeEnd"), qn("bookmarkEnd"))
    ]
    reference_runs = [
        deepcopy(run)
        for run in paragraph.findall(qn("r"))
        if run.find(qn("commentReference")) is not None
        or run.find(qn("footnoteReference")) is not None
    ]
    for child in list(paragraph):
        if child is not paragraph_properties:
            paragraph.remove(child)
    for marker in leading_markers:
        paragraph.append(marker)
    run = etree.SubElement(paragraph, qn("r"))
    if first_run_properties is not None:
        run.append(deepcopy(first_run_properties))
    text_node = etree.SubElement(run, qn("t"))
    text_node.text = value
    for marker in trailing_markers:
        paragraph.append(marker)
    for reference_run in reference_runs:
        paragraph.append(reference_run)


def set_cell_text(cell: etree._Element, value: str) -> None:
    paragraphs = cell.xpath("./w:p", namespaces=NS)
    if not paragraphs:
        paragraph = etree.SubElement(cell, qn("p"))
    else:
        paragraph = paragraphs[0]
    set_paragraph_text(paragraph, value)
    for extra in paragraphs[1:]:
        cell.remove(extra)


def find_paragraph(root: etree._Element, value: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:body/w:p", namespaces=NS)
        if text_of(paragraph) == value
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo {value!r}: encontrados {len(matches)}; esperado 1")
    return matches[0]


def find_paragraph_prefix(root: etree._Element, prefix: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:body/w:p", namespaces=NS)
        if text_of(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Prefixo {prefix!r}: encontrados {len(matches)}; esperado 1")
    return matches[0]


def replace_index_title(root: etree._Element, old: str, new: str) -> None:
    matches = []
    # Alguns índices locais do modelo institucional estão dentro de controlos
    # de conteúdo; por isso, a pesquisa não pode limitar-se aos parágrafos que
    # são filhos directos de ``w:body``.
    for paragraph in root.xpath("//w:p", namespaces=NS):
        styles = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        if not styles or not (styles[0].startswith("ndice") or styles[0].startswith("TOC")):
            continue
        matches.extend(paragraph.xpath(".//w:t[text()=$value]", namespaces=NS, value=old))
    if len(matches) != 1:
        raise RuntimeError(f"Entrada de índice {old!r}: encontradas {len(matches)}; esperado 1")
    matches[0].text = new


def set_index_page(root: etree._Element, title: str, page: int) -> int:
    """Actualizar todas as remissões de índice para um título do Anexo D."""
    matches = []
    for paragraph in root.xpath("//w:p", namespaces=NS):
        styles = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        if not styles or not (styles[0].startswith("ndice") or styles[0].startswith("TOC")):
            continue
        if text_of(paragraph).casefold().startswith(title.casefold()):
            matches.append(paragraph)
    if not matches:
        raise RuntimeError(f"Entrada de índice {title!r} não localizada")

    for paragraph in matches:
        numeric_nodes = [
            node
            for node in paragraph.xpath(".//w:t", namespaces=NS)
            if (node.text or "").strip().isdigit()
        ]
        if not numeric_nodes:
            raise RuntimeError(f"Entrada de índice {title!r} sem número de página")
        numeric_nodes[-1].text = str(page)
    return len(matches)


ANNEX_D_INDEX_PAGES = (
    ("D.1 Finalidade", 159),
    ("D.2 Distinção entre estimativa e medição real", 160),
    ("D.3 Variáveis, controlos e materiais", 160),
    ("D.3.1 Série A — Projectos de preparação digital para impressão 3D com configuração analisada", 160),
    ("D.3.2 Série B — Comparação digital controlada", 161),
    ("D.4 Resultados", 161),
    ("D.4.1 Série A", 162),
    ("D.4.2 Série B (condição comum)", 162),
    ("D.4.3 Geometria — tamanho do conjunto vs tamanho da peça", 163),
    ("D.4.4 Comparação entre entrada, malha e peça física", 164),
    ("D.4.5 Registo fotográfico dos protótipos", 165),
    ("D.5 Compatibilidade com orientações de dimensionamento", 166),
    ("D.6 Limites de comparabilidade", 166),
    ("D.7 Campos que não puderam ser obtidos", 167),
    ("D.8 O que pode e não pode ser afirmado na dissertação", 167),
    ("Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada", 162),
    ("Tabela D.2 — Estimativas de preparação para impressão na condição digital comum", 162),
    ("Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG", 164),
)


ANNEX_B_INDEX_PAGES = (
    ("B.1 Finalidade", 137),
    ("B.2 Âmbito e limites", 138),
    ("B.3 Procedimento", 138),
    ("B.4 Resultados de consistência da geração", 138),
    ("B.4.1 Repetição da mesma configuração", 138),
    ("B.4.2 Comparação entre navegadores", 139),
    ("B.5 Resultados de recuperação e controlo", 139),
    ("B.6 Resultados da verificação de acessibilidade digital", 140),
    ("B.6.1 Percurso local autenticado", 140),
    ("B.6.2 Superfície pública", 141),
    ("B.6.3 Verificação manual complementar", 141),
    ("B.7 Aprendizagens para o Design Industrial", 142),
    ("B.8 Conclusão", 142),
    ("B.9 Referências normativas", 143),
    ("Tabela B.1 — Resultados da repetição da mesma configuração por modelo", 138),
    ("Tabela B.2 — Resultados do percurso examinado em três navegadores", 139),
    ("Tabela B.3 — Comportamento observado perante limites, entradas inválidas e falhas previstas", 139),
    ("Tabela B.4 — Categorias de problemas de acessibilidade digital detectadas automaticamente", 140),
    ("Tabela B.5 — Resultados da verificação manual complementar de acessibilidade", 141),
)


def update_annex_index_pages(root: etree._Element) -> int:
    entries = (*ANNEX_B_INDEX_PAGES, *ANNEX_D_INDEX_PAGES)
    return sum(set_index_page(root, title, page) for title, page in entries)


def table_after_caption(root: etree._Element, caption: str) -> etree._Element:
    paragraph = find_paragraph(root, caption)
    element = paragraph.getnext()
    while element is not None and element.tag != qn("tbl"):
        element = element.getnext()
    if element is None:
        raise RuntimeError(f"Tabela não localizada após {caption!r}")
    return element


def prevent_row_split(row: etree._Element) -> None:
    properties = row.find(qn("trPr"))
    if properties is None:
        properties = etree.Element(qn("trPr"))
        row.insert(0, properties)
    if properties.find(qn("cantSplit")) is None:
        properties.append(etree.Element(qn("cantSplit")))


def keep_with_next(paragraph: etree._Element) -> None:
    properties = paragraph.find(qn("pPr"))
    if properties is None:
        properties = etree.Element(qn("pPr"))
        paragraph.insert(0, properties)
    if properties.find(qn("keepNext")) is None:
        properties.append(etree.Element(qn("keepNext")))


def set_table_widths(table: etree._Element, widths: list[int]) -> None:
    grid = table.find(qn("tblGrid"))
    if grid is None:
        grid = etree.Element(qn("tblGrid"))
        properties = table.find(qn("tblPr"))
        table.insert(1 if properties is not None else 0, grid)
    for child in list(grid):
        grid.remove(child)
    for width in widths:
        column = etree.SubElement(grid, qn("gridCol"))
        column.set(qn("w"), str(width))

    properties = table.find(qn("tblPr"))
    if properties is None:
        properties = etree.Element(qn("tblPr"))
        table.insert(0, properties)
    table_width = properties.find(qn("tblW"))
    if table_width is None:
        table_width = etree.SubElement(properties, qn("tblW"))
    table_width.set(qn("w"), str(sum(widths)))
    table_width.set(qn("type"), "dxa")
    layout = properties.find(qn("tblLayout"))
    if layout is None:
        layout = etree.SubElement(properties, qn("tblLayout"))
    layout.set(qn("type"), "fixed")

    for row in table.xpath("./w:tr", namespaces=NS):
        cells = row.xpath("./w:tc", namespaces=NS)
        if len(cells) != len(widths):
            raise RuntimeError(
                f"Tabela com {len(cells)} células numa linha; esperadas {len(widths)}"
            )
        for cell, width in zip(cells, widths, strict=True):
            cell_properties = cell.find(qn("tcPr"))
            if cell_properties is None:
                cell_properties = etree.Element(qn("tcPr"))
                cell.insert(0, cell_properties)
            cell_width = cell_properties.find(qn("tcW"))
            if cell_width is None:
                cell_width = etree.SubElement(cell_properties, qn("tcW"))
            cell_width.set(qn("w"), str(width))
            cell_width.set(qn("type"), "dxa")
        prevent_row_split(row)


def rebuild_table(
    table: etree._Element, rows: list[list[str]], widths: list[int]
) -> None:
    existing_rows = table.xpath("./w:tr", namespaces=NS)
    if not existing_rows:
        raise RuntimeError("Tabela sem linhas")
    header_template = deepcopy(existing_rows[0])
    body_template = deepcopy(existing_rows[1] if len(existing_rows) > 1 else existing_rows[0])
    for row in existing_rows:
        table.remove(row)

    for row_index, values in enumerate(rows):
        row = deepcopy(header_template if row_index == 0 else body_template)
        cells = row.xpath("./w:tc", namespaces=NS)
        while len(cells) > len(values):
            row.remove(cells.pop())
        while len(cells) < len(values):
            new_cell = deepcopy(cells[-1])
            row.append(new_cell)
            cells.append(new_cell)
        for cell, value in zip(cells, values, strict=True):
            set_cell_text(cell, value)
        table.append(row)
    set_table_widths(table, widths)


def insert_manual_accessibility_results(root: etree._Element) -> None:
    replace_index_title(
        root,
        "B.6 Resultados da verificação automática de acessibilidade digital",
        "B.6 Resultados da verificação de acessibilidade digital",
    )
    replace_index_title(
        root,
        "B.6.3 Verificação manual pendente",
        "B.6.3 Verificação manual complementar",
    )
    replace_index_title(
        root,
        "Tabela B.5 — Identificação das séries complementares de avaliação da plataforma",
        "Tabela B.5 — Resultados da verificação manual complementar de acessibilidade",
    )
    replace_index_title(root, "B.10 Referências normativas", "B.9 Referências normativas")

    find_paragraph(root, "B.6 Resultados da verificação de acessibilidade digital")
    set_paragraph_text(
        find_paragraph(root, "B.6.3 Verificação manual pendente"),
        "B.6.3 Verificação manual complementar",
    )
    set_paragraph_text(
        find_paragraph(root, "B.10 Referências normativas"),
        "B.9 Referências normativas",
    )

    dimension = find_paragraph_prefix(
        root, "3. verificação automática de regras selecionadas de acessibilidade digital"
    )
    set_paragraph_text(
        dimension,
        "3. verificação automática e manual de regras seleccionadas de acessibilidade digital, "
        "entendida como a identificação de barreiras nos estados examinados, sem a confundir "
        "com usabilidade, acessibilidade percebida por participantes ou conformidade global "
        "com as WCAG.",
    )

    procedure = find_paragraph_prefix(
        root, "A acessibilidade foi examinada automaticamente em oito estados do percurso local"
    )
    set_paragraph_text(
        procedure,
        "A acessibilidade foi examinada automaticamente em oito estados do percurso local: "
        "autenticação, painel principal, perfil inicial, perfil com erro, parâmetros, sugestão "
        "antes e depois da resposta e geometria apresentada. A página pública de entrada foi "
        "examinada separadamente. A verificação manual complementar foi realizada em 2 de julho "
        "de 2026, às 16:02, em Linux e Firefox 152.0.6 (64-bit), na instância local em "
        "localhost:3000 e na plataforma pública handfab.pedrocandeias.net. O percurso com leitor "
        "de ecrã usou o Orca; a reformulação do conteúdo foi examinada com ampliação a 400% e "
        "largura equivalente a 320 píxeis CSS.",
    )

    heading = find_paragraph(root, "B.6.3 Verificação manual complementar")
    old_body = heading.getnext()
    if old_body is None or not text_of(old_body).startswith("Permanecem por avaliar manualmente"):
        raise RuntimeError("Parágrafo pendente de B.6.3 não localizado")

    method = (
        "A grelha manual compreendeu doze verificações. Sete foram classificadas como conformes "
        "e cinco como não conformes. O protocolo preenchido e a sua representação editável são "
        "conservados no material suplementar como evidências ANNEX-B-014 e ANNEX-B-015."
    )
    set_paragraph_text(old_body, method)

    caption_template = find_paragraph(
        root, "Tabela B.4 — Categorias de problemas de acessibilidade digital detectadas automaticamente"
    )
    caption = deepcopy(caption_template)
    set_paragraph_text(
        caption, "Tabela B.5 — Resultados da verificação manual complementar de acessibilidade"
    )
    keep_with_next(caption)

    table_template = table_after_caption(
        root, "Tabela B.3 — Comportamento observado perante limites, entradas inválidas e falhas previstas"
    )
    table = deepcopy(table_template)
    rows = [
        ["Verificação", "Resultado", "Observação"],
        ["Navegação por teclado (2.1.1 e 2.1.2)", "Conforme", "O percurso essencial foi executado apenas com o teclado, sem bloqueio do foco."],
        ["Visibilidade do foco (2.4.7 e 2.4.11)", "Conforme", "O indicador de foco permaneceu visível e não oculto nos estados examinados."],
        ["Ordem do foco (2.4.3)", "Não conforme", "Com o Orca, a ordenação dos campos não foi sempre suficientemente clara para orientar a sequência de interacção."],
        ["Nome, função e valor (4.1.2 e 1.3.1)", "Não conforme", "Com o Orca, algumas descrições de campos necessitavam de maior especificidade e clareza."],
        ["Identificação e sugestão de correcção de erros (3.3.1 e 3.3.3)", "Conforme", "Os erros examinados foram apresentados por texto e acompanhados por indicação de correcção."],
        ["Mensagens de estado (4.1.3)", "Conforme", "As mensagens dinâmicas examinadas foram anunciadas sem deslocação indevida do foco."],
        ["Contraste e utilização da cor (1.4.3 e 1.4.1)", "Conforme na observação manual", "A classificação manual não elimina as 47 ocorrências de contraste insuficiente detectadas automaticamente em oito estados."],
        ["Reformulação e ampliação (1.4.10 e 1.4.4)", "Não conforme", "A 400% e com largura equivalente a 320 píxeis CSS, a interface permaneceu apenas parcialmente utilizável."],
        ["Dimensão mínima dos alvos (2.5.8)", "Conforme", "Os elementos interactivos examinados apresentaram dimensão ou espaçamento suficiente."],
        ["Autenticação acessível (3.3.8)", "Conforme", "A autenticação permitiu colar a palavra-passe e usar um gestor de palavras-passe."],
        ["Alternativa ao visualizador tridimensional (1.1.1 e 1.3.1)", "Não conforme", "Com o Orca, o visualizador não foi identificado como imagem nem foi anunciada uma alternativa textual."],
        ["Percurso com leitor de ecrã", "Não conforme", "O percurso com o Orca revelou limitações na ordenação e na clareza das descrições dos campos."],
    ]
    rebuild_table(table, rows, [2500, 1650, 4637])

    caveat = deepcopy(procedure)
    set_paragraph_text(
        caveat,
        "A classificação manual do contraste como conforme descreve apenas a observação efectuada "
        "nessa sessão e não substitui a medição automática, que identificou 47 elementos com "
        "contraste insuficiente. Como a versão, o ramo e o identificador da revisão da sessão "
        "manual não foram registados, os dois resultados são apresentados lado a lado e o "
        "contraste permanece uma prioridade de correcção. A avaliação manual complementa a "
        "verificação automática, mas não permite emitir uma declaração global de conformidade "
        "com as WCAG 2.2 nem substitui avaliação com participantes.",
    )

    parent = old_body.getparent()
    position = parent.index(old_body) + 1
    for element in (caption, table, caveat):
        parent.insert(position, element)
        position += 1

    chapter_7 = find_paragraph_prefix(
        root, "A avaliação automática de acessibilidade examinou oito estados do percurso autenticado"
    )
    set_paragraph_text(
        chapter_7,
        "A avaliação de acessibilidade combinou uma verificação automática de oito estados do "
        "percurso autenticado com uma verificação manual complementar. A análise automática "
        "identificou contraste insuficiente, ausência de associação programática entre alguns "
        "rótulos e controlos, elementos interactivos aninhados e falta de nome acessível num "
        "elemento de selecção. Na grelha manual, sete das doze verificações foram classificadas "
        "como conformes e cinco como não conformes. O percurso com o Orca revelou limitações na "
        "ordem e na descrição dos campos; a interface permaneceu apenas parcialmente utilizável "
        "com ampliação a 400%; e o visualizador tridimensional não apresentou uma alternativa "
        "textual reconhecível. A classificação manual do contraste como conforme não elimina as "
        "ocorrências detectadas automaticamente. Estes resultados localizam decisões de interface "
        "a rever, mas não demonstram a experiência de pessoas com diferentes capacidades nem "
        "conformidade global com as WCAG 2.2.",
    )

    chapter_8 = find_paragraph_prefix(
        root, "A auditoria automática de acessibilidade examinou oito estados do percurso local autenticado"
    )
    set_paragraph_text(
        chapter_8,
        "A auditoria automática de acessibilidade examinou oito estados do percurso local "
        "autenticado e identificou quatro categorias de barreira: contraste de cor insuficiente, "
        "ausência de associação programática entre rótulos e controlos, elementos interactivos "
        "aninhados e falta de nome acessível num elemento de selecção. A página pública não "
        "autenticada não apresentou violações automáticas nos elementos examinados, mas incluiu "
        "uma verificação inconclusiva e não representa os percursos internos. Na verificação "
        "manual complementar, sete das doze verificações foram classificadas como conformes e "
        "cinco como não conformes. O percurso com o Orca revelou problemas na ordenação e na "
        "descrição dos campos; a interface foi apenas parcialmente utilizável com ampliação a "
        "400%; e o visualizador tridimensional não disponibilizou uma alternativa textual "
        "reconhecível. A classificação manual do contraste como conforme não invalida as "
        "ocorrências automáticas. Em conjunto, os resultados definem prioridades concretas de "
        "revisão, mas não demonstram conformidade global com as WCAG 2.2 nem acessibilidade "
        "percebida por utilizadores.",
    )

    conclusion = find_paragraph_prefix(
        root, "As séries de ensaios fornecem evidência parcial de que o núcleo paramétrico"
    )
    set_paragraph_text(
        conclusion,
        "As séries de ensaios fornecem evidência parcial de que o núcleo paramétrico produz "
        "resultados consistentes nas execuções concluídas e de que vários estados de erro "
        "preservam o trabalho anterior ou permitem recuperação. Também revelam fragilidades "
        "concretas na aplicação uniforme dos limites, na aceitação de tipos de dados e na "
        "acessibilidade da interface. A verificação manual classificou sete de doze critérios "
        "como conformes e cinco como não conformes, acrescentando problemas de ordem e descrição "
        "dos campos, reformulação em ampliação elevada e ausência de alternativa textual ao "
        "visualizador tridimensional.",
    )


TABLE_D1 = [
    ["Modelo e perfil", "Material", "Equipamento", "Configuração", "Tempo estimado", "Material e custo estimados"],
    ["Flexy Beast — teen_15", "PLA", "Bambu Lab A1; bico 0,4 mm", "Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica", "2 h 21 min 50 s", "18 645,87 mm; 56,51 g; 2,05 €"],
    ["UnLimbited Phoenix — teen_15", "PLA", "Bambu Lab A1; bico 0,4 mm", "Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica", "5 h 12 min 44 s", "40 756,68 mm; 123,52 g; 4,48 €"],
    ["UnLimbited Phoenix — teen_15", "PETG", "Bambu Lab A1; bico 0,4 mm", "Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica", "5 h 51 min 52 s", "39 094,09 mm; 117,54 g; 4,27 €"],
    ["Paraglider Hand — teen_15", "PLA", "Prusa MINI; bico 0,4 mm", "Camada 0,20 mm; enchimento 15%, grelha; sem suportes", "2 h 32 min 11 s", "12 727,61 mm; 37,96 g; 1,38 €"],
]


TABLE_D2 = [
    ["Modelo", "Perfil", "Tempo estimado", "Filamento estimado", "Massa estimada", "Custo estimado", "Placas A1"],
    ["Flexy Beast", "child_8", "6 h 39 min 34 s", "27 387,6 mm", "83,00 g", "3,01 €", "1"],
    ["Flexy Beast", "teen_15", "9 h 51 min 52 s", "43 180,9 mm", "130,87 g", "4,75 €", "1"],
    ["Flexy Beast", "adult_28", "12 h 34 min 14 s", "55 811,9 mm", "169,15 g", "6,14 €", "2"],
    ["Flexy Beast", "elderly_70", "10 h 52 min 57 s", "47 602,0 mm", "144,27 g", "5,24 €", "2"],
    ["Paraglider Hand", "child_8", "4 h 22 min 47 s", "16 522,2 mm", "50,07 g", "1,82 €", "1"],
    ["Paraglider Hand", "teen_15", "6 h 45 min 18 s", "27 695,5 mm", "83,94 g", "3,05 €", "1"],
    ["Paraglider Hand", "adult_28", "8 h 55 min 41 s", "38 449,4 mm", "116,53 g", "4,23 €", "1"],
    ["Paraglider Hand", "elderly_70", "7 h 09 min 05 s", "29 627,5 mm", "89,79 g", "3,26 €", "1"],
    ["UnLimbited Phoenix", "child_8", "7 h 29 min 44 s", "30 673,7 mm", "92,96 g", "3,37 €", "2"],
    ["UnLimbited Phoenix", "teen_15", "8 h 30 min 45 s", "36 335,2 mm", "110,12 g", "4,00 €", "2"],
    ["UnLimbited Phoenix", "adult_28", "8 h 56 min 20 s", "38 179,8 mm", "115,71 g", "4,20 €", "2"],
    ["UnLimbited Phoenix", "elderly_70", "7 h 49 min 09 s", "32 412,0 mm", "98,23 g", "3,56 €", "2"],
]


def make_annex_d_portrait(root: etree._Element) -> None:
    final_section = root.find("./w:body/w:sectPr", namespaces=NS)
    if final_section is None:
        raise RuntimeError("Propriedades da secção final não localizadas")
    page_size = final_section.find(qn("pgSz"))
    if page_size is None:
        page_size = etree.SubElement(final_section, qn("pgSz"))
    page_size.set(qn("w"), "11906")
    page_size.set(qn("h"), "16838")
    page_size.attrib.pop(qn("orient"), None)

    margins = final_section.find(qn("pgMar"))
    if margins is None:
        margins = etree.SubElement(final_section, qn("pgMar"))
    for name, value in {
        "left": "1701",
        "right": "1418",
        "top": "1985",
        "bottom": "1985",
        "header": "709",
        "footer": "709",
        "gutter": "0",
    }.items():
        margins.set(qn(name), value)

    table_d1 = table_after_caption(
        root, "Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada"
    )
    table_d2 = table_after_caption(
        root, "Tabela D.2 — Estimativas de preparação para impressão na condição digital comum"
    )
    rebuild_table(table_d1, TABLE_D1, [1450, 900, 1350, 2200, 1250, 1637])
    rebuild_table(table_d2, TABLE_D2, [1350, 1050, 1350, 1450, 1200, 1250, 1137])

    table_d3 = table_after_caption(
        root, "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG"
    )
    set_table_widths(table_d3, [1700, 1000, 1217, 1217, 1217, 1217, 1219])

    for caption_text in (
        "Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada",
        "Tabela D.2 — Estimativas de preparação para impressão na condição digital comum",
        "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG",
    ):
        keep_with_next(find_paragraph(root, caption_text))

    annex_heading = find_paragraph(root, "Anexo D — Preparação para fabrico e verificação dos protótipos")
    siblings = list(annex_heading.getparent())
    start = siblings.index(annex_heading)
    for element in siblings[start + 1 :]:
        if element.tag != qn("tbl") or element in (table_d1, table_d2):
            continue
        grid_columns = element.xpath("./w:tblGrid/w:gridCol", namespaces=NS)
        if not grid_columns:
            continue
        widths = [int(column.get(qn("w"), "0")) for column in grid_columns]
        total = sum(widths)
        if total <= 8787:
            continue
        scaled = [max(1, round(width * 8787 / total)) for width in widths]
        scaled[-1] += 8787 - sum(scaled)
        set_table_widths(element, scaled)


def apply(
    path: Path, captions_only: bool = False, annex_indexes_only: bool = False
) -> None:
    original_mode = path.stat().st_mode
    with ZipFile(path, "r") as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    missing = [name for name in ("word/document.xml", *PROTECTED_PARTS) if name not in files]
    if missing:
        raise RuntimeError(f"Partes obrigatórias em falta: {missing}")
    protected_before = {name: files[name] for name in PROTECTED_PARTS}
    footnote_refs = reference_ids(files["word/document.xml"], "footnote")
    comment_refs = reference_ids(files["word/document.xml"], "comment")

    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(files["word/document.xml"], parser)
    if annex_indexes_only:
        update_annex_index_pages(root)
    elif captions_only:
        for caption_text in (
            "Tabela B.5 — Resultados da verificação manual complementar de acessibilidade",
            "Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada",
            "Tabela D.2 — Estimativas de preparação para impressão na condição digital comum",
            "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG",
        ):
            keep_with_next(find_paragraph(root, caption_text))
        set_table_widths(
            table_after_caption(
                root, "Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada"
            ),
            [1450, 900, 1350, 2200, 1250, 1637],
        )
        set_table_widths(
            table_after_caption(
                root, "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG"
            ),
            [1700, 1000, 1217, 1217, 1217, 1217, 1219],
        )
    else:
        insert_manual_accessibility_results(root)
        make_annex_d_portrait(root)

    final_text = text_of(root)
    if not captions_only:
        for forbidden in (
            "B.6.3 Verificação manual pendente",
            "Permanecem por avaliar manualmente a navegação por teclado",
            "As verificações manuais por teclado, foco, ampliação",
            "As verificações manuais por teclado, ampliação",
            "B.10 Referências normativas",
        ):
            if forbidden in final_text:
                raise RuntimeError(f"Formulação obsoleta ainda presente: {forbidden!r}")

    updated_document = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    if reference_ids(updated_document, "footnote") != footnote_refs:
        raise RuntimeError("As referências às notas de rodapé foram alteradas")
    if reference_ids(updated_document, "comment") != comment_refs:
        raise RuntimeError(
            "As referências aos comentários foram alteradas: "
            f"antes={comment_refs!r}; depois={reference_ids(updated_document, 'comment')!r}"
        )
    files["word/document.xml"] = updated_document

    for name, data in protected_before.items():
        if files[name] != data:
            raise RuntimeError(f"A parte protegida {name} foi alterada")

    descriptor, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in items:
                target.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "docx",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[2]
        / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx",
    )
    parser.add_argument(
        "--captions-only",
        action="store_true",
        help="Aplicar apenas os ajustes finais de legendas e larguras ao DOCX já actualizado.",
    )
    parser.add_argument(
        "--annex-indexes-only",
        action="store_true",
        help="Actualizar apenas as páginas dos índices internos dos Anexos B e D.",
    )
    args = parser.parse_args()
    if args.captions_only and args.annex_indexes_only:
        parser.error("--captions-only e --annex-indexes-only são mutuamente exclusivos")
    apply(
        args.docx.resolve(),
        captions_only=args.captions_only,
        annex_indexes_only=args.annex_indexes_only,
    )
    print(f"DOCX actualizado: {args.docx}")


if __name__ == "__main__":
    main()
