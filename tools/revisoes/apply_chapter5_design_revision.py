#!/usr/bin/env python3
"""Apply the Design and Product Development revision of Chapter 5 to the DOCX."""

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


def set_paragraph_text(paragraph: etree._Element, value: str) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value


def clone_paragraph(template: etree._Element, value: str) -> etree._Element:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, value)
    return paragraph


def find_paragraph(root: etree._Element, prefix: str) -> etree._Element:
    matches = [
        p for p in root.xpath("//w:body/w:p", namespaces=NS)
        if text(p).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one body paragraph beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def find_exact_paragraph(root: etree._Element, value: str) -> etree._Element:
    matches = [
        p for p in root.xpath("//w:body/w:p", namespaces=NS)
        if text(p) == value
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one body paragraph equal to {value!r}; found {len(matches)}")
    return matches[0]


def replace(root: etree._Element, prefix: str, value: str) -> etree._Element:
    paragraph = find_paragraph(root, prefix)
    set_paragraph_text(paragraph, value)
    return paragraph


def keep_with_next(paragraph: etree._Element) -> None:
    p_pr = paragraph.find(qn("pPr"))
    if p_pr is None:
        p_pr = etree.Element(qn("pPr"))
        paragraph.insert(0, p_pr)
    if p_pr.find(qn("keepNext")) is None:
        etree.SubElement(p_pr, qn("keepNext"))


def set_cell_text(cell: etree._Element, value: str, *, bold: bool = False) -> None:
    tc_pr = cell.find(qn("tcPr"))
    for child in list(cell):
        if child is not tc_pr:
            cell.remove(child)
    paragraph = etree.SubElement(cell, qn("p"))
    p_pr = etree.SubElement(paragraph, qn("pPr"))
    justification = etree.SubElement(p_pr, qn("jc"))
    justification.set(qn("val"), "left")
    run = etree.SubElement(paragraph, qn("r"))
    if bold:
        run_pr = etree.SubElement(run, qn("rPr"))
        etree.SubElement(run_pr, qn("b"))
    node = etree.SubElement(run, qn("t"))
    node.text = value


def set_list_entry(paragraph: etree._Element, identifier: str, description: str, page: str) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    for index, value in enumerate((identifier, description, page)):
        if index:
            run = etree.SubElement(paragraph, qn("r"))
            etree.SubElement(run, qn("tab"))
        run = etree.SubElement(paragraph, qn("r"))
        node = etree.SubElement(run, qn("t"))
        node.text = value


def rewrite_table(table: etree._Element, rows: list[list[str]]) -> None:
    existing = table.findall(qn("tr"))
    if not existing:
        raise RuntimeError("Table has no rows")
    template = existing[-1]
    while len(existing) < len(rows):
        row = deepcopy(template)
        table.append(row)
        existing.append(row)
    while len(existing) > len(rows):
        table.remove(existing.pop())
    for row_index, (row, values) in enumerate(zip(existing, rows)):
        cells = row.findall(qn("tc"))
        if len(cells) != len(values):
            raise RuntimeError(f"Expected {len(values)} cells; found {len(cells)}")
        row_pr = row.find(qn("trPr"))
        if row_pr is None:
            row_pr = etree.Element(qn("trPr"))
            row.insert(0, row_pr)
        if row_pr.find(qn("cantSplit")) is None:
            etree.SubElement(row_pr, qn("cantSplit"))
        if row_index == 0 and row_pr.find(qn("tblHeader")) is None:
            etree.SubElement(row_pr, qn("tblHeader"))
        for cell, value in zip(cells, values):
            set_cell_text(cell, value, bold=row_index == 0)


def format_table_52(root: etree._Element) -> None:
    caption = find_exact_paragraph(root, "Tabela 5.2 — Componentes, versões e limites do protótipo examinado")
    table = caption.getnext()
    while table is not None and table.tag != qn("tbl"):
        table = table.getnext()
    if table is None:
        raise RuntimeError("Could not locate Table 5.2")
    widths = [1500, 2600, 2200, 2700]
    grid = table.find(qn("tblGrid"))
    if grid is None:
        grid = etree.Element(qn("tblGrid"))
        table.insert(1 if table.find(qn("tblPr")) is not None else 0, grid)
    for child in list(grid):
        grid.remove(child)
    for width in widths:
        column = etree.SubElement(grid, qn("gridCol"))
        column.set(qn("w"), str(width))
    tbl_pr = table.find(qn("tblPr"))
    if tbl_pr is None:
        tbl_pr = etree.Element(qn("tblPr"))
        table.insert(0, tbl_pr)
    layout = tbl_pr.find(qn("tblLayout"))
    if layout is None:
        layout = etree.SubElement(tbl_pr, qn("tblLayout"))
    layout.set(qn("type"), "fixed")
    for row in table.findall(qn("tr")):
        for cell in row.findall(qn("tc")):
            if "demonstração pública em https://handfab.pedrocandeias.net/" in text(cell):
                set_cell_text(
                    cell,
                    "Aplicação web com visualizador tridimensional; demonstração pública em "
                    "handfab.pedrocandeias.net",
                )
            if text(cell).strip() == "Persistência":
                set_cell_text(cell, "Dados guardados")
        for cell, width in zip(row.findall(qn("tc")), widths):
            tc_pr = cell.find(qn("tcPr"))
            if tc_pr is None:
                tc_pr = etree.Element(qn("tcPr"))
                cell.insert(0, tc_pr)
            tc_width = tc_pr.find(qn("tcW"))
            if tc_width is None:
                tc_width = etree.SubElement(tc_pr, qn("tcW"))
            tc_width.set(qn("w"), str(width))
            tc_width.set(qn("type"), "dxa")
            for paragraph in cell.findall(qn("p")):
                p_pr = paragraph.find(qn("pPr"))
                if p_pr is None:
                    p_pr = etree.Element(qn("pPr"))
                    paragraph.insert(0, p_pr)
                justification = p_pr.find(qn("jc"))
                if justification is None:
                    justification = etree.SubElement(p_pr, qn("jc"))
                justification.set(qn("val"), "left")


INTRO = (
    "A plataforma web desenvolvida no âmbito deste projecto constitui a camada de mediação entre o "
    "modelo paramétrico, os dados de entrada e a configuração digital da mão protésica. É um protótipo "
    "funcional de investigação e não um produto preparado para utilização clínica. A versão pública "
    "pode ser consultada em https://handfab.pedrocandeias.net/; a sua disponibilidade permite observar "
    "o artefacto, mas não demonstra usabilidade, acessibilidade global, segurança clínica ou aptidão "
    "para utilização autónoma."
)

STATE = (
    "O estado actual examinado corresponde à versão 14.72.0, em 14 de Julho de 2026. Os ensaios "
    "principais incidiram na versão 14.67.0 e a campanha "
    "complementar de interface na versão 14.69.0. Esta separação temporal é mantida porque a plataforma "
    "continuou a evoluir depois dos ensaios, nomeadamente na organização e nomenclatura dos controlos, "
    "sem que essas alterações posteriores possam ser apresentadas como parte dos resultados anteriores."
)

DESIGN_ROLE = (
    "Do ponto de vista do Design e Desenvolvimento de Produto, a plataforma não constitui um fim "
    "autónomo: organiza a passagem entre intenção, dados, parâmetros, forma visualizada e ficheiro "
    "destinado ao fabrico. A interface expõe uma parte controlada do espaço de variação e evita que a "
    "configuração dependa da edição directa do código OpenSCAD. Esta leitura é coerente com os estudos "
    "sobre personalização digital e personalização em massa, que descrevem os configuradores como "
    "sistemas capazes de disponibilizar variação sem comprometer as relações do modelo-base (Ozdemir, "
    "Verlinden, & Cascini, 2022; Stralen, 2018)."
)

FUNCTIONAL_SCOPE = (
    "Do ponto de vista funcional, a plataforma foi concebida para suportar um processo progressivo de "
    "configuração, no qual a definição geométrica resulta da articulação entre a recolha de dados, a "
    "selecção do modelo, o ajustamento de parâmetros, a visualização do resultado e a eventual exportação "
    "para prototipagem. Esta organização aproxima etapas anteriormente dispersas num único percurso "
    "projectual; não permite concluir que pessoas sem formação técnica o executam com menor esforço."
)

INTERFACE_SCOPE = (
    "Em vez de exigir contacto directo com a estrutura interna do ficheiro OpenSCAD, o sistema "
    "disponibiliza controlos paramétricos, pré-visualização tridimensional e gestão de configurações. "
    "Neste capítulo, esta característica é descrita como uma decisão de interface; a sua facilidade de "
    "aprendizagem e a redução efectiva da dependência técnica permanecem por avaliar com participantes."
)

TABLE_52 = [
    ["Elemento do percurso", "Implementação e estado examinado", "Função no processo de design", "Limite da evidência"],
    ["Protótipo HandFab", "Versão actual 14.72.0; ensaios principais em 14.67.0 e complementares em 14.69.0", "Reunir configuração, pré-visualização, conservação de variantes e exportação", "A evolução entre versões impede atribuir retroactivamente funções novas aos ensaios anteriores"],
    ["Interface no navegador", "Aplicação web com visualizador tridimensional; demonstração pública em handfab.pedrocandeias.net", "Tornar visível a relação entre parâmetros, forma e decisão de exportar", "Chromium e Firefox produziram o mesmo resultado no caso comparado; WebKit permaneceu inconclusivo; não foi demonstrada compatibilidade universal"],
    ["Geração geométrica", "OpenSCAD executado em WebAssembly num Web Worker", "Aplicar as relações paramétricas e produzir a geometria sem instalação local de CAD", "O tempo e a conclusão dependem do modelo e dos recursos do equipamento; não houve estudo comparativo de desempenho"],
    ["Servidor e acesso", "Node.js 22.14.0, Express 4.18.3 e autenticação por perfis", "Guardar contas e configurações e intermediar os pedidos externos", "O funcionamento foi examinado em casos delimitados; não foram avaliados carga, acessos simultâneos ou segurança integral"],
    ["Dados guardados", "SQLite integrado no Node.js", "Conservar perfis, configurações e relações de atribuição", "Adequado ao protótipo examinado; não foi comparado com outras soluções nem testado em utilização intensiva"],
    ["Serviço externo de IA", "Anthropic ou OpenAI, seleccionável; claude-sonnet-4-6 no ensaio reportado", "Sugerir valores iniciais condicionados pelo modelo activo", "Depende da disponibilidade externa e da qualidade do pedido; não gera nem aprova a geometria"],
]

TABLE_INTRO = (
    "A Tabela 5.2 identifica o estado técnico necessário para interpretar o artefacto sem converter esta "
    "dissertação numa descrição exaustiva da implementação. As versões são registadas porque condicionam "
    "a leitura dos ensaios; a sua enumeração não constitui comparação entre tecnologias."
)

DATA_BOUNDARIES = (
    "A distribuição da informação segue as mesmas fronteiras. O navegador conserva o estado corrente "
    "da configuração, executa o modelo OpenSCAD e prepara a pré-visualização e os ficheiros de exportação. "
    "O servidor guarda contas, perfis e configurações e recebe os pedidos de sugestão. O fornecedor de IA "
    "recebe a descrição introduzida, o identificador e o esquema do modelo, os valores correntes e, quando "
    "existe, a referência populacional seleccionada; não recebe os ficheiros OpenSCAD, a malha gerada ou o "
    "ficheiro final de fabrico. Esta delimitação permite perceber quais as decisões locais, persistidas ou "
    "externas sem expor contratos internos irrelevantes para a argumentação projectual."
)

FAILURE_STATES = (
    "Os estados de espera e falha foram igualmente tratados como parte do percurso. Durante a geração é "
    "apresentado um estado de processamento; um novo pedido de pré-visualização termina o cálculo anterior "
    "e cada geração ou exportação possui um limite temporal de 120 segundos. Uma falha da IA preserva a "
    "possibilidade de configuração manual; uma resposta inválida conserva o último estado válido; e uma "
    "falha de geração impede a obtenção do ficheiro até existir nova geometria válida. Os ensaios "
    "complementares confirmaram a recuperação após uma falha de geração, mas também revelaram controlos "
    "incompletos para tipos e valores fora do intervalo. Estes resultados são discutidos no Capítulo 8 e "
    "no Anexo B. Não foram executados ensaios de acessos simultâneos ou de desempenho sob carga."
)


REPLACEMENTS = {
    "Deste modo, o enquadramento conceptual da plataforma articula três objectivos complementares": (
        "Deste modo, o enquadramento conceptual articula três objectivos: tornar a lógica paramétrica "
        "operável em ambiente web, estruturar a configuração como uma sequência explícita e distribuir o "
        "acesso segundo papéis diferenciados. A plataforma implementa estas condições e permite conservar "
        "estados do processo; a compreensão da sequência e a adequação dos papéis permanecem por avaliar. "
        "É nesta articulação entre configuração, interface e responsabilidades que se fundamenta a "
        "arquitectura apresentada na secção seguinte."
    ),
    "No plano da segurança e do controlo de acesso": (
        "O controlo de acesso diferencia administrador, técnico e utilizador através de autenticação por "
        "JSON Web Token (JWT). Para a presente investigação, estes mecanismos interessam enquanto suporte "
        "da distribuição de papéis e da conservação das configurações, não como contributo autónomo de "
        "segurança informática. Os ensaios confirmam autenticação, permissões e recuperação de configurações "
        "nos casos documentados, mas não constituem avaliação integral de segurança. A sua pertinência "
        "projectual reside em impedir que todas as decisões e operações sejam apresentadas indistintamente "
        "a todos os perfis (Quintero et al., 2018; Bai et al., 2024)."
    ),
    "A integração do OpenSCAD por meio de WebAssembly, como referido anteriormente": (
        "A integração do OpenSCAD por meio de WebAssembly permite executar localmente, no navegador, um "
        "modelo paramétrico baseado em código, sem depender de um serviço externo de geração contínua. O "
        "OpenSCAD define a geometria através de instruções, parâmetros e relações explícitas; o WebAssembly "
        "(WASM) permite executar esse núcleo no ambiente web. Para esta investigação, a articulação preserva "
        "a lógica do modelo e disponibiliza os seus controlos através da interface, sem demonstrar, por si "
        "só, acessibilidade ou facilidade de utilização (Machado et al., 2019; Nilsiam & Pearce, 2017)."
    ),
    "Do ponto de vista técnico, o uso de Web Workers": (
        "O Web Worker separa o cálculo da tarefa principal da interface. Nos casos observados, esta decisão "
        "manteve os controlos disponíveis enquanto a geração decorria e permitiu terminar um cálculo anterior "
        "quando era iniciada uma nova pré-visualização. Não foram medidos tempos percebidos nem estabilidade "
        "em diferentes equipamentos. A geração permanece no navegador, enquanto o servidor conserva "
        "autenticação, persistência e mediação com serviços externos."
    ),
    "Não obstante as vantagens, esta solução introduz limitações": (
        "Esta solução introduz um compromisso projectual. O desempenho depende da complexidade do modelo, "
        "dos valores escolhidos e dos recursos do equipamento, podendo prolongar a espera ou interromper a "
        "geração. O valor demonstrado não é um desempenho superior ao CAD instalado, mas a possibilidade de "
        "relacionar, no mesmo percurso, parâmetros, forma visualizada e exportação a partir de um núcleo "
        "geométrico explícito."
    ),
    "A estrutura funcional da plataforma organiza-se": (
        "A estrutura funcional da plataforma organiza-se num conjunto de módulos interligados que suportam "
        "o ciclo de configuração paramétrica: selecção do modelo, introdução e edição de parâmetros, "
        "visualização tridimensional, sugestões apoiadas por IA, gestão de configurações e administração "
        "multiutilizador. Esta organização distribui as funções segundo a sequência projectada para o "
        "processo; a clareza dessa sequência para diferentes perfis não foi avaliada com participantes."
    ),
    "O ponto de entrada do sistema é o módulo de selecção de modelos": (
        "O ponto de entrada do sistema é o módulo de selecção de modelos. Cada modelo é descrito por um "
        "ficheiro de configuração que inclui o identificador, a descrição, o ficheiro OpenSCAD associado e "
        "a lista de parâmetros editáveis. A partir dessa estrutura, a interface gera os controlos "
        "correspondentes, incluindo campos numéricos, selectores, caixas de selecção e campos de texto. Esta "
        "opção permite acomodar famílias distintas sem desenhar manualmente um ecrã exclusivo para cada "
        "modelo. Em termos funcionais, o módulo converte a biblioteca e os respectivos parâmetros num conjunto "
        "visível de decisões de configuração."
    ),
    "Esta arquitectura corrige uma fragilidade identificada numa versão anterior": (
        "Esta arquitectura corrige uma fragilidade identificada numa versão anterior, em que o pedido à IA "
        "permanecia associado a um modelo já removido e podia devolver nomes de parâmetros inexistentes. Ao "
        "condicionar a sugestão pelo esquema actual, a IA passa a operar sobre os mesmos campos que a interface "
        "e o modelo OpenSCAD. O módulo propõe um ponto de partida editável; não foi medido se reduz tempo, "
        "esforço ou dificuldade de configuração. A IA permanece um apoio sob controlo humano e não gera "
        "autonomamente a prótese."
    ),
    "Por fim, a plataforma inclui um módulo administrativo": (
        "Por fim, o módulo administrativo suporta a criação de contas, a diferenciação de permissões e a "
        "atribuição de utilizadores a técnicos. A sua presença permite representar diferentes níveis de "
        "intervenção no protótipo; não confirma que esta distribuição corresponda às práticas profissionais "
        "ou às necessidades dos futuros utilizadores. Os resultados funcionais disponíveis são apresentados "
        "na Secção 8.1 e no Anexo B."
    ),
    "A biblioteca organiza diferentes famílias como modelos registados": (
        "A biblioteca organiza diferentes famílias como modelos registados, cada uma com parâmetros, "
        "dependências, limites e modos de visualização próprios. Na versão 14.67.0, quatro modelos surgem no "
        "ficheiro de configuração: Flexy Beast, UnLimbited Phoenix Hand, Paraglider Hand e Cyborg Beast. Os "
        "ensaios dimensionais comparativos abrangem os três primeiros; o Cyborg Beast foi integrado "
        "posteriormente e não entra nas séries comparativas. Os quatro permanecem registados na versão "
        "14.72.0. A reconstrução designada pec Phoenix hand continua como material de desenvolvimento e não "
        "integra a plataforma. Esta distinção separa biblioteca actual, conjunto avaliado e trabalhos "
        "exploratórios."
    ),
    "Controlar parâmetros constitui uma das condições centrais": (
        "Controlar parâmetros constitui uma das condições centrais para transformar um modelo paramétrico "
        "num sistema configurável e persistente. Os ficheiros de configuração descrevem cada parâmetro "
        "segundo nome, tipo, valor inicial, limites, incrementos e grupo temático. Esta estrutura liga o "
        "código OpenSCAD ao espaço de alteração apresentado na interface. Em termos metodológicos, aproxima-se "
        "da lógica dos configuradores e das famílias de produto, nas quais a variação depende da preservação "
        "das relações do modelo-base (Ozdemir et al., 2022; Lei et al., 2016)."
    ),
    "Quanto à capacidade de expansão": (
        "Quanto à expansão, a separação entre modelos, parâmetros, interface, autenticação e persistência "
        "permite acrescentar modelos OpenSCAD sem redesenhar todo o percurso. A experiência com o Paraglider, "
        "o Phoenix, o Flexy Beast e o Cyborg Beast mostrou, contudo, que não basta adicionar um ficheiro .scad: "
        "é necessário declarar parâmetros, dependências, limites e modos de visualização e, em alguns casos, "
        "corrigir incompatibilidades ou preservar interfaces mecânicas herdadas. A expansão é, portanto, uma "
        "actividade de adaptação projectual controlada, e não uma importação automática de geometrias (Lei et "
        "al., 2016; Ozdemir et al., 2022)."
    ),
    "O recurso ao SQLite é adequado": (
        "Esta lógica permanece limitada pelas condições do protótipo. A persistência em SQLite não foi "
        "ensaiada com utilização intensiva ou acessos simultâneos, e a geração local depende dos recursos do "
        "equipamento e da complexidade geométrica. A integração de novas funções e modelos exige, por isso, "
        "nova verificação do percurso, dos limites apresentados e dos ficheiros exportados."
    ),
    "Neste sentido, a secção confirma uma conclusão importante": (
        "O contributo deste capítulo reside no desenho de um percurso integrado entre dados, configuração, "
        "visualização e preparação para fabrico. A arquitectura torna explícito onde cada transformação ocorre "
        "e permite conservar variantes do processo. Os ensaios sustentam o funcionamento técnico nas condições "
        "documentadas; não demonstram prontidão de produto, facilidade de utilização, redução de carga "
        "cognitiva, segurança clínica ou funcionamento em escala."
    ),
}


def update_list_of_tables(root: etree._Element) -> None:
    matches = [
        p for p in root.xpath("//w:body/w:p", namespaces=NS)
        if text(p).startswith("Tabela 5.2") and "Inventário consolidado dos modelos" in text(p)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one list entry for the model inventory; found {len(matches)}")
    old = matches[0]
    set_list_entry(old, "Tabela 5.3", "Inventário consolidado dos modelos no fecho do estudo", "68")
    new = deepcopy(old)
    set_list_entry(new, "Tabela 5.2", "Componentes, versões e limites do protótipo examinado", "62")
    old.addprevious(new)


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(text(p).startswith("A Tabela 5.2 identifica o estado técnico necessário") for p in root.xpath("//w:body/w:p", namespaces=NS)):
        format_table_52(root)
        return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")

    first = replace(root, "A plataforma web desenvolvida no âmbito deste projecto", INTRO)
    next_old = find_paragraph(root, "Do ponto de vista funcional, a plataforma foi concebida")
    next_old.addprevious(clone_paragraph(next_old, STATE))
    next_old.addprevious(clone_paragraph(next_old, DESIGN_ROLE))
    set_paragraph_text(next_old, FUNCTIONAL_SCOPE)
    replace(root, "Em vez de exigir que cada interveniente compreenda", INTERFACE_SCOPE)

    # Insert the version/component table after Figure 5.3 and before the Figure 5.4 discussion.
    reference = find_paragraph(root, "A Figura 5.4 apresenta um precedente")
    caption_51 = find_exact_paragraph(root, "Tabela 5.1 — Fluxo de dados e responsabilidades da plataforma")
    table_51 = caption_51.getnext()
    while table_51 is not None and table_51.tag != qn("tbl"):
        table_51 = table_51.getnext()
    if table_51 is None:
        raise RuntimeError("Could not locate Table 5.1")
    table_52 = deepcopy(table_51)
    rewrite_table(table_52, TABLE_52)
    caption_52 = clone_paragraph(caption_51, "Tabela 5.2 — Componentes, versões e limites do protótipo examinado")
    keep_with_next(caption_52)
    normal = find_paragraph(root, "A Figura 5.3 detalha a sequência operacional")
    for element in [
        clone_paragraph(normal, TABLE_INTRO),
        caption_52,
        table_52,
        clone_paragraph(normal, DATA_BOUNDARIES),
        clone_paragraph(normal, FAILURE_STATES),
    ]:
        reference.addprevious(element)

    # Remove a duplicated standalone citation before Figure 5.5 when present.
    orphan = [p for p in root.xpath("//w:body/w:p", namespaces=NS) if text(p).strip() == "(Li & Aflatoony, 2025)."]
    for paragraph in orphan:
        paragraph.getparent().remove(paragraph)

    # Replace the selected design-focused paragraphs and remove superseded follow-ups.
    for prefix, value in REPLACEMENTS.items():
        replace(root, prefix, value)

    old_security_followup = find_paragraph(root, "Estes mecanismos integram o desenho do sistema")
    old_security_followup.getparent().remove(old_security_followup)
    old_admin_followup = find_paragraph(root, "A sua presença confirma que a estrutura funcional")
    old_admin_followup.getparent().remove(old_admin_followup)
    old_expansion_heading = find_paragraph(root, "Todavia, esta lógica de expansão deve ser analisada criticamente")
    old_expansion_heading.getparent().remove(old_expansion_heading)
    old_wasm_followup = find_paragraph(root, "De forma semelhante, a renderização local através de WASM")
    old_wasm_followup.getparent().remove(old_wasm_followup)

    # Renumber the model inventory table and its references.
    old_inventory_caption = find_exact_paragraph(root, "Tabela 5.2 — Inventário consolidado dos modelos no fecho do estudo")
    set_paragraph_text(old_inventory_caption, "Tabela 5.3 — Inventário consolidado dos modelos no fecho do estudo")
    counts = find_paragraph(root, "As contagens referem-se às declarações presentes")
    set_paragraph_text(
        counts,
        "As contagens da Tabela 5.3 referem-se às declarações presentes em models/models-config.json no "
        "estado versionado da plataforma 14.67.0. O total inclui selectores, opções de visualização e "
        "controlos não geométricos; a contagem numérica identifica os campos do tipo number, sem pressupor "
        "que todos representam medidas antropométricas. A ausência de uma licença explícita no pacote local "
        "do Cyborg Beast é registada como lacuna documental e não como afirmação de inexistência de licença "
        "na fonte original."
    )
    replace(root, "A biblioteca examinada compreende quatro modelos registados", text(find_paragraph(root, "A biblioteca examinada compreende quatro modelos registados")).replace("Tabela 5.2", "Tabela 5.3"))
    update_list_of_tables(root)
    format_table_52(root)

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
