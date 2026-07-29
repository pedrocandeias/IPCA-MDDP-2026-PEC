#!/usr/bin/env python3
"""Integrate the evidence-aligned Chapter 4 revision into the thesis DOCX."""

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


def text(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_text(paragraph: etree._Element, value: str, *, bold: bool = False, size: int | None = None) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    if bold or size:
        r_pr = etree.SubElement(run, qn("rPr"))
        if bold:
            etree.SubElement(r_pr, qn("b"))
        if size:
            etree.SubElement(r_pr, qn("sz")).set(qn("val"), str(size))
            etree.SubElement(r_pr, qn("szCs")).set(qn("val"), str(size))
    node = etree.SubElement(run, qn("t"))
    node.text = value


def clone_paragraph(template: etree._Element, value: str) -> etree._Element:
    paragraph = deepcopy(template)
    set_text(paragraph, value)
    return paragraph


def find_exact(root: etree._Element, value: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text(p) == value]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph {value!r}; found {len(matches)}")
    return matches[0]


def find_prefix(root: etree._Element, prefix: str, *, body_only: bool = False) -> etree._Element:
    path = "//w:body/w:p" if body_only else "//w:p"
    matches = [p for p in root.xpath(path, namespaces=NS) if text(p).startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def remove_between(start: etree._Element, end: etree._Element, *, include_start: bool = True) -> None:
    parent = start.getparent()
    if parent is None or end.getparent() is not parent:
        raise RuntimeError("Range anchors do not share the same parent")
    current = start if include_start else start.getnext()
    while current is not None and current is not end:
        following = current.getnext()
        parent.remove(current)
        current = following
    if current is None:
        raise RuntimeError("End anchor was not reached")


def insert_many_before(reference: etree._Element, elements: list[etree._Element]) -> None:
    for element in elements:
        reference.addprevious(element)


def set_tabbed_entry(paragraph: etree._Element, title: str, page: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if len(nodes) != 2:
        raise RuntimeError(f"Unexpected index entry structure: {text(paragraph)!r}")
    nodes[0].text = title
    nodes[1].text = page


def set_cell_text(cell: etree._Element, value: str, *, bold: bool, size: int) -> None:
    paragraph = etree.SubElement(cell, qn("p"))
    p_pr = etree.SubElement(paragraph, qn("pPr"))
    etree.SubElement(p_pr, qn("jc")).set(qn("val"), "left")
    spacing = etree.SubElement(p_pr, qn("spacing"))
    spacing.set(qn("before"), "0")
    spacing.set(qn("after"), "0")
    spacing.set(qn("line"), "210")
    spacing.set(qn("lineRule"), "auto")
    set_text(paragraph, value, bold=bold, size=size)


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


def format_existing_table(root: etree._Element, caption: str, widths: list[int]) -> None:
    paragraph = find_exact(root, caption)
    table = paragraph.getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError(f"Table does not follow {caption!r}")
    columns = table.xpath("./w:tblGrid/w:gridCol", namespaces=NS)
    if len(columns) != len(widths):
        raise RuntimeError(f"Unexpected column count for {caption!r}")
    for column, width in zip(columns, widths, strict=True):
        column.set(qn("w"), str(width))
    for row_index, row in enumerate(table.xpath("./w:tr", namespaces=NS)):
        row_pr = row.find(qn("trPr"))
        if row_pr is None:
            row_pr = etree.Element(qn("trPr"))
            row.insert(0, row_pr)
        if row_index == 0 and row_pr.find(qn("tblHeader")) is None:
            etree.SubElement(row_pr, qn("tblHeader"))
        if row_pr.find(qn("cantSplit")) is None:
            etree.SubElement(row_pr, qn("cantSplit"))
        cells = row.xpath("./w:tc", namespaces=NS)
        for cell, width in zip(cells, widths, strict=True):
            cell_width = cell.find("./w:tcPr/w:tcW", namespaces=NS)
            if cell_width is not None:
                cell_width.set(qn("w"), str(width))
            for p_pr in cell.xpath("./w:p/w:pPr", namespaces=NS):
                alignment = p_pr.find(qn("jc"))
                if alignment is None:
                    alignment = etree.SubElement(p_pr, qn("jc"))
                alignment.set(qn("val"), "left")


OPENING = [
    "Este capítulo trata um subconjunto delimitado do problema das próteses de membro superior: a adaptação paramétrica de modelos mecânicos passivos de mão destinados à exploração técnica e à prototipagem por fabrico aditivo. O trabalho implementado não inclui actuadores, sensores, fontes de energia, controlo mioeléctrico, desenho clínico de encaixes ou avaliação funcional com utilizadores. Estes temas permanecem no enquadramento geral da literatura, mas não constituem propriedades demonstradas pelo artefacto.",
    "A biblioteca examinada compreende quatro modelos registados na plataforma: Flexy Beast, Paraglider Hand, UnLimbited Phoenix Hand e Cyborg Beast. Os três primeiros integram a comparação dimensional e os ensaios descritos no Capítulo 8. O Cyborg Beast foi integrado posteriormente e é analisado como evolução projectual, sem ser incluído nas séries comparativas ou físicas. A reconstrução pec Phoenix hand permanece material de desenvolvimento e fica fora do âmbito deste capítulo. O inventário consolidado dos modelos, com origem, licença, versão, estratégia de escala e evidência disponível, é apresentado na Tabela 5.2.",
    "A unidade de análise é a relação entre um vector de parâmetros, a regra geométrica específica de cada modelo e a malha gerada. «Adaptação paramétrica» designa aqui a capacidade de modificar dimensões dentro das relações e limites codificados. Não designa ajuste anatómico validado, conforto, eficácia protésica ou segurança clínica.",
]

SECTION_41 = [
    "A literatura descreve requisitos funcionais, ergonómicos, técnicos, produtivos e psicossociais que devem convergir num dispositivo protésico (Biddiss et al., 2007; Brack & Amalu, 2021; Henao et al., 2025; Walker et al., 2019). Neste estudo, porém, apenas três grupos foram traduzidos em propriedades observáveis do protótipo: dimensões e relações geométricas; preservação de interfaces mecânicas herdadas; e preparação preliminar para fabrico aditivo. Conforto, usabilidade, força, amplitude funcional, durabilidade, segurança, aceitação e incorporação corporal não foram operacionalizados nem avaliados.",
    "Os requisitos implementados foram, assim, formulados como condições de projecto: aceitar um conjunto explícito de entradas; aplicar relações determinísticas; preservar furos, eixos e zonas de montagem quando a geometria varia; manter os valores dentro da gama declarada; permitir isolar e exportar componentes; e tornar visíveis as situações em que um perfil ultrapassa a cobertura do modelo. Estas condições permitem examinar coerência e comportamento geométrico, mas não substituem requisitos clínicos ou funcionais.",
    "A definição destes limites transforma a adaptação numa configuração condicionada por relações explícitas entre medidas, componentes e restrições de fabrico. Cada condição necessita de um critério próprio e deve ser confrontada com a geometria efectivamente gerada, não apenas com o nome do parâmetro ou com o intervalo apresentado na interface (Brack & Amalu, 2021; Herneth et al., 2024; Jones et al., 2023).",
]

BASE_PARAGRAPHS = [
    "A configuração recorre a uma base local em formato longo, na qual cada linha representa uma estatística associada a uma medida e a um grupo, e não uma pessoa. O conjunto combina fontes populacionais heterogéneas quanto a idade, sexo, país, amostra, protocolo e estatísticas disponíveis. Por esse motivo, os valores funcionam como referências iniciais e não como substitutos da medição individual.",
    "Para a modelação, a base cumpre três funções: identificar medidas recorrentes; apoiar a definição de intervalos de configuração; e fornecer casos populacionais para examinar a propagação dos parâmetros. A origem documental, a população, a unidade e as notas de qualidade permanecem associadas a cada valor, permitindo regressar à fonte quando surgem incompatibilidades.",
    "A extracção, a selecção das fontes, a normalização para milímetros, a cobertura populacional e as limitações documentais são apresentadas integralmente no Anexo A. No corpo do capítulo conservam-se apenas as regras que alteram decisões geométricas: medidas disponíveis, correspondência com os campos do modelo, tratamento de ausência e limites de utilização.",
    "A maior parte dos dados descreve pessoas sem amputação e não representa a forma do membro residual, a deformação dos tecidos ou a interface corpo–dispositivo. Uma referência populacional pode apoiar uma configuração inicial; uma adaptação individual exige medidas directas, eventual digitalização tridimensional e avaliação própria.",
]

BASE_ROWS = [
    ["Função no projecto", "Dados utilizados", "Limite de interpretação"],
    ["Identificar medidas recorrentes", "Designações, regiões corporais e protocolos das fontes", "Medidas com o mesmo nome podem usar pontos anatómicos diferentes"],
    ["Definir intervalos iniciais", "Médias, dispersões e percentis disponíveis", "Os intervalos populacionais não constituem limites clínicos"],
    ["Construir casos de ensaio", "Idade, sexo, país, grupo e estatística", "O perfil agregado não representa uma pessoa nem assegura correspondência nacional"],
    ["Preencher parâmetros disponíveis", "Valores positivos ligados ao mapa canónico do modelo", "Os campos ausentes permanecem por preencher e não devem ser inventados"],
]

RELATIONS_ROWS = [
    ["Modelo", "Entradas activas principais", "Transformação implementada", "Limitação que deve acompanhar a leitura"],
    ["Flexy Beast", "Largura da palma; comprimentos dos cinco dedos; circunferência do punho", "xScaleFactor = (palm_breadth_mm + 5) / 55; o médio define o multiplicador digital; a braçadeira deriva de circunferência/π mais folga", "A largura introduzida alimenta uma fórmula herdada e não coincide directamente com a extensão transversal da malha"],
    ["Cyborg Beast", "Largura da palma; comprimentos totais e proximais; circunferência do punho", "Escala global pela fórmula Cyborg Beast; curvas calibradas para os segmentos; braçadeira independente da mão", "As curvas são calibrações da geometria e possuem limites internos; o modelo não integrou a comparação principal"],
    ["Paraglider Hand", "Largura da palma; comprimentos dos dedos; opções de componentes", "overall_scale = palm_breadth_mm / 66,4; correcção overall_scale / 1,25 na palma Reborn; escalas próprias para quatro dedos", "A palma mantém escala uniforme; comprimento e espessura são contextuais; o polegar ainda usa a escala do médio"],
    ["UnLimbited Phoenix Hand", "Largura da palma; comprimentos totais e proximais dos dedos", "HandPerc limitado a 100%–160%; alongamento localizado das zonas sem furos", "Perfis inferiores a 82 mm atingem o limite mínimo; os comprimentos digitais são novamente afectados pela escala global"],
]

RELATIONS_TEXT = [
    "As relações gerais das Tabelas 4.5 e 4.6 foram concretizadas de forma diferente em cada família. A versão 14.67.0 corresponde ao fecho dos ensaios principais e ao dicionário suplementar arquivado. A versão 14.71.0 acrescentou a braçadeira comum do Flexy Beast e relações mais completas do Cyborg Beast. A versão 14.72.0 uniformizou a organização dos grupos e os nomes dos controlos de lateralidade e disposição, sem alterar as relações geométricas avaliadas. Estes desenvolvimentos posteriores não são retroactivamente apresentados como parte dos ensaios concluídos na versão 14.67.0. As fórmulas descrevem a implementação; não representam relações anatómicas universais.",
    "O escalonamento uniforme não foi eliminado em todos os modelos. Foi mantido onde a arquitectura herdada exigia preservar furos circulares, espaçamentos e componentes montados como conjunto. No Paraglider, esta opção protege a palma e os pinos enquanto parte dos dedos recebe escalas próprias. No Phoenix, a montagem completa conserva uma escala uniforme e os dedos são alongados apenas em faixas sem furos; como o alongamento antecede a escala global, o comprimento final depende das duas operações.",
    "A crítica ao escalonamento proporcional aplica-se, portanto, ao seu uso como substituto de todas as diferenças antropométricas. Uma transformação uniforme local pode constituir uma restrição mecânica legítima, desde que o texto identifique o que preserva, o que deixa de adaptar e como afecta as restantes dimensões.",
    "Os parâmetros de lateralidade constituem uma classe separada. Na versão 14.72.0, os quatro modelos registados usam o campo booleano mirrored; a designação anterior LeftRight do Phoenix foi eliminada. Estes campos possuem o papel laterality, ficam fora do pedido de sugestões e são descartados caso surjam na resposta da IA. A regra geométrica permanece determinística e independente do texto gerado pelo modelo de linguagem.",
]

ANNEX_DICTIONARY = "O Anexo C complementa o dicionário da versão 14.67.0 com as adaptações posteriores, as relações internas do Cyborg Beast, os valores de folga e espessura confirmáveis, as excepções da escala uniforme e os campos que ainda não produzem uma transformação geométrica própria. O anexo distingue valores directos, derivados, fixos e contextuais e assinala expressamente as propriedades que não podem ser confirmadas pelos ficheiros examinados."
ANNEX_EXAMPLES = "Os exemplos complementares do Anexo C mostram duas dependências que este percurso não cobre: o parâmetro de comprimento do polegar do Paraglider ainda não controla uma escala própria e, no Phoenix, a escala global volta a multiplicar os comprimentos definidos localmente."

ITERATION_ROWS = [
    ["Data e versão", "Problema observado", "Decisão introduzida", "Aprendizagem de projecto"],
    ["15–16 Jun. 2026; 14.10–14.11", "Ficheiros Paraglider dispersos e nomes incompatíveis com a plataforma", "Consolidação da família num modelo com componentes e duas palmas", "Integrar um modelo aberto exige declarar dependências, variantes e campos comuns antes de expor parâmetros"],
    ["28 Jun. 2026; 14.16–14.17", "A palma Reborn permanecia no tamanho médio apesar de variar palm_breadth_mm", "Compensação da escala 1,25 preservada no módulo carregado por use", "A resposta de um controlo não pode ser inferida pelo nome; deve ser confirmada na malha gerada"],
    ["29 Jun. 2026; 14.18", "HandPerc_override permitia ao Phoenix contornar o limite mínimo de 100%", "Aplicação do mesmo intervalo de 100%–160% aos dois percursos", "Limites equivalentes devem actuar em todas as entradas que conduzem à mesma transformação"],
    ["29 Jun. 2026; 14.19", "A IA alterava a lateralidade apesar de esta ser uma decisão binária do projecto", "Lateralidade transferida para a interface determinística e excluída das sugestões", "Decisões inequívocas e críticas não devem permanecer num processo probabilístico"],
    ["9–10 Jul. 2026; 14.32–14.37", "Cyborg Beast sem controlo independente dos segmentos e com desalinhamentos", "Calibração do alcance, divisão proximal–distal e reposicionamento sobre os eixos MCP/PIP", "A adaptação paramétrica exige preservar interfaces articulares enquanto se altera o alcance dos segmentos"],
    ["10 Jul. 2026; 14.40–14.44", "Braçadeira desligada da circunferência do punho e polegar sem correspondência estável", "Braçadeira dimensionada por circunferência/π, assentamento automático no pino e calibração do polegar", "Mão, punho e antebraço não devem depender de uma única escala global"],
    ["10–11 Jul. 2026; 14.48", "Dedos Phoenix constituídos por malhas fixas", "Divisão das colunas e alongamento apenas das faixas sem furos", "Modelos de malha podem receber variação local se as zonas funcionais forem isoladas"],
    ["14 Jul. 2026; 14.71", "Braçadeira Flexy sem ligação directa ao mapa do punho", "Adopção da braçadeira comum do Cyborg e de wrist_circumference_mm", "Uma gramática comum deve ligar a mesma medida corporal a funções equivalentes entre modelos"],
    ["14 Jul. 2026; 14.72", "Grupos e nomes de controlos equivalentes variavam entre modelos", "Ordem comum; LeftRight passou a mirrored no Phoenix e show_assembled passou a print_layout no Paraglider", "A coerência da interface beneficia de nomes comuns para decisões equivalentes, sem uniformizar diferenças geométricas legítimas"],
]

ITERATION_TEXT = [
    "A evolução dos modelos foi documentada através de episódios em que uma configuração, uma malha ou uma montagem tornou visível uma limitação e conduziu a uma alteração específica. A Tabela 4.11 resume os episódios com maior influência na estrutura paramétrica. As versões posteriores ao fecho da comparação principal são apresentadas como desenvolvimento subsequente e não como resultados retroactivos dos ensaios anteriores.",
    "Estes episódios produziram quatro conclusões circunscritas. Primeiro, a integração de um modelo aberto exige examinar o âmbito das variáveis dentro de cada ficheiro, e não apenas os controlos apresentados. Segundo, preservar uma interface mecânica pode justificar escala uniforme local ou alongamento selectivo. Terceiro, um intervalo declarado na interface não substitui verificações dentro da transformação geométrica. Quarto, a equivalência nominal entre uma medida e um parâmetro deve ser confirmada na malha, porque fórmulas herdadas e escalas sucessivas podem alterar a dimensão final.",
    "A iteração funcionou, assim, como instrumento de investigação através do design: cada falha alterou a compreensão do objecto configurável e conduziu a uma regra mais explícita. O resultado não é uma metodologia universal de personalização protésica, mas um conjunto documentado de decisões para integrar modelos heterogéneos, preservar as suas interfaces e tornar visíveis os respectivos limites.",
]


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(text(p).startswith("A evolução dos modelos foi documentada através de episódios") for p in root.xpath("//w:body/w:p", namespaces=NS)):
        set_text(find_prefix(root, "As relações gerais das Tabelas 4.5 e 4.6", body_only=True), RELATIONS_TEXT[0])
        set_text(find_prefix(root, "Os parâmetros de lateralidade constituem uma classe separada", body_only=True), RELATIONS_TEXT[3])
        iteration_caption = find_exact(root, "Tabela 4.11 — Cronologia das principais iterações paramétricas")
        iteration_table = iteration_caption.getnext()
        if iteration_table is None or iteration_table.tag != qn("tbl"):
            raise RuntimeError("Table 4.11 was not found")
        if "14.72" not in text(iteration_table):
            row = etree.SubElement(iteration_table, qn("tr"))
            row_pr = etree.SubElement(row, qn("trPr"))
            etree.SubElement(row_pr, qn("cantSplit"))
            for value, width in zip(ITERATION_ROWS[-1], [1500, 2450, 2650, 2500], strict=True):
                cell = etree.SubElement(row, qn("tc"))
                cell_pr = etree.SubElement(cell, qn("tcPr"))
                cell_width = etree.SubElement(cell_pr, qn("tcW"))
                cell_width.set(qn("w"), str(width))
                cell_width.set(qn("type"), "dxa")
                set_cell_text(cell, value, bold=False, size=16)
        format_existing_table(root, "Tabela 4.4 — Funções e limites da base antropométrica na configuração", [2150, 3150, 3800])
        format_existing_table(root, "Tabela 4.8 — Síntese das relações implementadas e respectivas limitações", [1450, 2100, 2800, 2750])
        format_existing_table(root, "Tabela 4.11 — Cronologia das principais iterações paramétricas", [1500, 2450, 2650, 2500])
        return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")

    normal = find_prefix(root, "Como referido anteriormente, o desenvolvimento de próteses", body_only=True)
    h41 = find_exact(root, "4.1 Definição do problema de design e requisitos")
    h42 = find_exact(root, "4.2 Parâmetros antropométricos e estrutura do modelo")
    intro_third = find_prefix(root, "Neste contexto, a definição de requisitos", body_only=True)
    insert_many_before(h41, [clone_paragraph(normal, value) for value in OPENING])
    remove_between(intro_third, h42)
    insert_many_before(h42, [clone_paragraph(normal, value) for value in SECTION_41])

    base_heading = find_exact(root, "Bases de dados antropométricas, extracção e normalização")
    correspondence = find_exact(root, "Correspondência entre perfil populacional e parâmetros do modelo")
    base_caption = find_exact(root, "Tabela 4.4 — Fontes integradas na base local de dados antropométricos")
    base_table = base_caption.getnext()
    if base_table is None or base_table.tag != qn("tbl"):
        raise RuntimeError("Table 4.4 was not found")
    base_heading_template = deepcopy(base_heading)
    base_caption_template = deepcopy(base_caption)
    table_template = deepcopy(base_table)
    remove_between(base_heading, correspondence)
    insert_many_before(correspondence, [
        clone_paragraph(base_heading_template, "Bases de dados antropométricas, extracção e normalização"),
        *[clone_paragraph(normal, value) for value in BASE_PARAGRAPHS],
        clone_paragraph(base_caption_template, "Tabela 4.4 — Funções e limites da base antropométrica na configuração"),
        make_table(table_template, BASE_ROWS, [2150, 3150, 3800], size=16),
    ])

    h433 = find_exact(root, "4.3.3 Relações implementadas nos modelos avaliados")
    h434 = find_exact(root, "4.3.4 Dicionário operacional de parâmetros")
    relation_caption = find_exact(root, "Tabela 4.8 — Relações paramétricas dos modelos avaliados")
    relation_table = relation_caption.getnext()
    if relation_table is None or relation_table.tag != qn("tbl"):
        raise RuntimeError("Table 4.8 was not found")
    h433_template = deepcopy(h433)
    relation_caption_template = deepcopy(relation_caption)
    relation_table_template = deepcopy(relation_table)
    remove_between(h433, h434)
    insert_many_before(h434, [
        clone_paragraph(h433_template, "4.3.3 Relações implementadas nos modelos avaliados"),
        clone_paragraph(normal, RELATIONS_TEXT[0]),
        clone_paragraph(relation_caption_template, "Tabela 4.8 — Síntese das relações implementadas e respectivas limitações"),
        make_table(relation_table_template, RELATIONS_ROWS, [1250, 2200, 2850, 2800], size=16),
        *[clone_paragraph(normal, value) for value in RELATIONS_TEXT[1:]],
    ])

    h435 = find_exact(root, "4.3.5 Exemplo numérico completo: perfil infantil no Flexy Beast")
    h44 = find_exact(root, "4.4 Iterações, refinamento e discussão intermédia")
    h435.addprevious(clone_paragraph(normal, ANNEX_DICTIONARY))
    h44.addprevious(clone_paragraph(normal, ANNEX_EXAMPLES))

    chapter5 = find_exact(root, "Capítulo 5 — Plataforma Web e Integração Digital")
    h44_template = deepcopy(h44)
    remove_between(h44, chapter5)
    insert_many_before(chapter5, [
        clone_paragraph(h44_template, "4.4 Iterações e decisões de projecto"),
        clone_paragraph(normal, ITERATION_TEXT[0]),
        clone_paragraph(relation_caption_template, "Tabela 4.11 — Cronologia das principais iterações paramétricas"),
        make_table(relation_table_template, ITERATION_ROWS, [1450, 2500, 2700, 2450], size=16),
        clone_paragraph(normal, ITERATION_TEXT[1]),
        clone_paragraph(normal, ITERATION_TEXT[2]),
    ])

    set_tabbed_entry(find_exact(root, "Tabela 4.4 — Fontes integradas na base local de dados antropométricos46"), "Tabela 4.4 — Funções e limites da base antropométrica na configuração", "46")
    set_tabbed_entry(find_exact(root, "Tabela 4.8 — Relações paramétricas dos modelos avaliados56"), "Tabela 4.8 — Síntese das relações implementadas e respectivas limitações", "56")
    index_410 = find_exact(root, "Tabela 4.10 — Percurso numérico do vector antropométrico até às malhas do Flexy Beast59")
    index_411 = deepcopy(index_410)
    set_tabbed_entry(index_411, "Tabela 4.11 — Cronologia das principais iterações paramétricas", "60")
    index_410.addnext(index_411)
    set_tabbed_entry(find_exact(root, "4.4 Iterações, refinamento e discussão intermédia60"), "4.4 Iterações e decisões de projecto", "60")

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    path = args.docx.resolve()
    with ZipFile(path, "r") as archive:
        updated = apply(archive.read("word/document.xml"))
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
