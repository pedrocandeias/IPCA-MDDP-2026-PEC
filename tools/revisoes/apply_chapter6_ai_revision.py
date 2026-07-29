#!/usr/bin/env python3
"""Apply the evidence-aligned Chapter 6 revision to the thesis DOCX.

The transformation edits only Chapter 6 in the OOXML package, preserving the
IPCA template, Figure 6.1, existing styles and document relationships.
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


def clone_paragraph(template: etree._Element, text: str) -> etree._Element:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, text)
    return paragraph


def keep_with_next(paragraph: etree._Element) -> None:
    p_pr = paragraph.find(qn("pPr"))
    if p_pr is None:
        p_pr = etree.Element(qn("pPr"))
        paragraph.insert(0, p_pr)
    if p_pr.find(qn("keepNext")) is None:
        etree.SubElement(p_pr, qn("keepNext"))


def find_body_paragraph(root: etree._Element, text: str) -> etree._Element:
    matches = [
        p for p in root.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_text(p) == text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one body paragraph {text!r}; found {len(matches)}")
    return matches[0]


def elements_between(start: etree._Element, end: etree._Element) -> list[etree._Element]:
    elements: list[etree._Element] = []
    current = start.getnext()
    while current is not None and current is not end:
        elements.append(current)
        current = current.getnext()
    if current is None:
        raise RuntimeError("Section end is not a following sibling of its start")
    return elements


def replace_section(start: etree._Element, end: etree._Element, elements: list[etree._Element]) -> None:
    for old in elements_between(start, end):
        old.getparent().remove(old)
    for element in elements:
        end.addprevious(element)


def normal_elements(template: etree._Element, texts: list[str]) -> list[etree._Element]:
    return [clone_paragraph(template, text) for text in texts]


def set_cell_text(cell: etree._Element, text: str, *, bold: bool = False) -> None:
    tc_pr = cell.find(qn("tcPr"))
    for child in list(cell):
        if child is not tc_pr:
            cell.remove(child)
    paragraph = etree.SubElement(cell, qn("p"))
    run = etree.SubElement(paragraph, qn("r"))
    if bold:
        run_pr = etree.SubElement(run, qn("rPr"))
        etree.SubElement(run_pr, qn("b"))
    node = etree.SubElement(run, qn("t"))
    node.text = text


def rewrite_table(table: etree._Element, rows: list[list[str]]) -> None:
    existing = table.findall(qn("tr"))
    if not existing:
        raise RuntimeError("Table has no rows")
    template = existing[-1]
    while len(existing) < len(rows):
        new_row = deepcopy(template)
        table.append(new_row)
        existing.append(new_row)
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


SECTION_61 = [
    "No sistema desenvolvido, a IA desempenha uma função diferente da que predomina nos estudos sobre próteses de membro superior. Em vez de interpretar biosinais, reconhecer gestos ou controlar o dispositivo, o modelo de linguagem sugere valores iniciais para uma configuração geométrica já formalizada (Cordella et al., 2016; Marinelli et al., 2022; Peerdeman et al., 2011).",
    "Esta aplicação responde à fragmentação identificada entre referências antropométricas, modelos paramétricos e interfaces de configuração. A plataforma reúne esses componentes, mas não atribui à IA a geração da geometria, a selecção autónoma do dispositivo ou a validação do resultado. Os precedentes de modelação ajustável e de métodos orientados por dados sustentam esta articulação sem constituírem equivalentes directos do sistema implementado (Gu et al., 2024; da Silveira Romero et al., 2025; Saldarriaga et al., 2024).",
    "O fluxo organiza-se em três camadas. A primeira é determinística: identifica idade e sexo quando estão explicitamente descritos, procura uma referência populacional disponível, selecciona o esquema do modelo activo e preserva decisões fixadas na interface, como a lateralidade. A segunda é probabilística: o modelo de linguagem recebe a descrição textual e o contexto paramétrico, propondo valores para os campos autorizados. A terceira verifica e aplica a resposta: interpreta o objecto JSON, confronta os campos com o modelo seleccionado, apresenta os valores na interface e permite a sua revisão antes da geração geométrica.",
    "A geometria não é produzida pela IA. Depois de aceite ou corrigida a configuração, o OpenSCAD executa relações geométricas previamente codificadas e gera a forma correspondente. Esta separação permite localizar a origem de cada decisão: dados e regras definem o espaço de configuração; a IA propõe um ponto de partida; e o designer ou técnico decide se a proposta deve ser mantida, alterada ou rejeitada.",
    "Os testes complementares mostraram que esta terceira camada ainda não aplica todas as restrições de modo uniforme. A lateralidade permaneceu protegida, mas um valor numérico acima do intervalo foi detectado sem ser impedido de chegar ao estado interno da aplicação. Por isso, os limites declarados são tratados neste capítulo como restrições pretendidas e parcialmente verificadas, e não como garantia integral. A discussão ética geral permanece na Secção 2.6; o presente capítulo concentra-se na forma como esses princípios foram concretizados e nos limites observados.",
]

SECTION_62_BEFORE_TABLE = [
    "À luz das distinções estabelecidas nos Capítulos 2 e 4, a personalização apoiada por IA não designa variação livre da forma. No protótipo, designa a proposta de valores para parâmetros previamente definidos, com relações geométricas, intervalos e campos protegidos. A independência entre dimensões dos dedos e a insuficiência do escalonamento uniforme fundamentam o espaço paramétrico; não são decisões tomadas pelo modelo de linguagem (Lim et al., 2018; Saldarriaga et al., 2024; da Silveira Romero et al., 2025).",
    "A operacionalização desta lógica ocorre em dois objectos distintos. O primeiro é um vector numérico de parâmetros geométricos, consumido directamente pela interface e pelos modelos OpenSCAD. O segundo é um contexto semântico para a IA, que descreve a origem das medições, campos em falta, incerteza, valores atípicos, tolerâncias, componentes de montagem seleccionados e notas sobre parâmetros derivados. Esta separação é importante porque impede confundir cálculo geométrico com raciocínio apoiado: os parâmetros numéricos alimentam o modelo; o contexto semântico ajuda a IA a explicar, ponderar ou sugerir ajustes, mas não substitui as regras determinísticas que geram a geometria.",
    "No protótipo implementado, esta separação é materializada pela construção dinâmica do pedido enviado ao modelo de linguagem. O pedido inclui a descrição livre do utilizador, o esquema do modelo seleccionado, os nomes exactos dos parâmetros, as respectivas legendas, os tipos de dados, os limites declarados e os valores correntes. Quando existe correspondência com um perfil populacional importado, inclui também as médias desse grupo como referência explícita. O pedido determina ainda que a resposta contenha apenas um objecto JSON, sem texto adicional, e exclui os campos de lateralidade e cor.",
    "As legendas influenciam a sugestão porque explicam ao modelo de linguagem a função de cada parâmetro. Nos parâmetros antropométricos, a legenda identifica a medida e a unidade. Nos componentes mecânicos, como folgas, diâmetros ou elementos de montagem, uma sugestão só possui fundamento determinístico quando existe uma regra codificada. Na ausência dessa regra, o valor resulta do intervalo, da legenda, do valor corrente e da inferência do modelo de linguagem; deve, portanto, ser entendido como proposta inicial a confirmar tecnicamente, e não como cálculo de engenharia.",
    "A correspondência com os perfis populacionais também segue uma regra explícita. O sistema atribui maior peso à coincidência de sexo e de grupo etário, acrescenta a proximidade da idade e a referência ao país quando esta existe no texto, e usa a presença de medidas da mão e de estatísticas centrais como critérios secundários. Só é seleccionado um perfil quando a pontuação mínima é atingida. Caso contrário, o pedido é enviado sem referência populacional, ficando a sugestão assinalada como não apoiada por essa base. Mesmo quando existe correspondência, os dados populacionais constituem uma aproximação e não substituem medidas individuais.",
    "Neste enquadramento, a IA pode interpretar descrições incompletas, propor valores iniciais para campos autorizados e preencher lacunas com apoio das referências disponíveis. Não pode escolher autonomamente o modelo protésico, definir a lateralidade, ultrapassar deliberadamente os limites do modelo, confirmar adequação anatómica ou clínica, gerar a forma final, nem aprovar a exportação ou o fabrico. Estas decisões permanecem nas regras do sistema e na intervenção humana.",
    "A designação «modelo» é usada, nesta investigação, em dois sentidos técnicos distintos: o modelo de linguagem responsável pela sugestão paramétrica e o modelo CAD paramétrico ao qual essa sugestão é aplicada. Para evitar ambiguidade metodológica, a Tabela 6.1 explicita a configuração de IA efectivamente implementada no protótipo e a sua relação com os modelos paramétricos disponibilizados na plataforma.",
]

TABLE_61 = [
    ["Elemento", "Especificação no protótipo"],
    ["Função da IA", "Sugestão inicial de parâmetros antropométricos e geométricos a partir de descrições em linguagem natural; não gera autonomamente a geometria final nem valida clinicamente a prótese."],
    ["Ponto de integração", "POST /api/ai/suggest, através de chamada autenticada e limitada por frequência, com as chaves de API mantidas no servidor."],
    ["Fornecedor e modelo usados na avaliação inicial", "Anthropic, com o modelo claude-sonnet-4-6, definido como opção predefinida no servidor do protótipo."],
    ["Modelo alternativo disponibilizado", "OpenAI, com o modelo gpt-4, acessível através do mesmo percurso de sugestão paramétrica."],
    ["Selecção do fornecedor", "A interface permite escolher entre Anthropic (Claude) e OpenAI (GPT-4); o pedido enviado ao servidor identifica o fornecedor."],
    ["Condições da chamada avaliada", "Máximo de 1024 tokens; o código não fixa a temperatura na chamada ao claude-sonnet-4-6. O percurso OpenAI fixa temperatura de 0,7, mas não integra a avaliação reportada."],
    ["Contrato de resposta", "Objecto JSON simples no formato parâmetro–valor. A lateralidade é ignorada e os campos desconhecidos não são aplicados. Os testes revelaram que a verificação de tipos e intervalos ainda não é uniforme em todas as entradas."],
    ["Enquadramento dos dados", "O pedido inclui o esquema do modelo, limites mínimos e máximos, valores correntes, legendas dos parâmetros e, quando disponível, médias de perfis antropométricos populacionais."],
    ["Versões examinadas", "A avaliação inicial incidiu sobre a versão 14.67.0. A campanha complementar de controlo da interface e das entradas foi executada na versão 14.69.0."],
    ["Modelos CAD abrangidos", "Flexy Beast, Paraglider Hand, UnLimbited Phoenix e Cyborg Beast estavam registados; a avaliação dimensional e de geração repetida abrangeu os três primeiros."],
]

SECTION_62_AFTER_TABLE = [
    "Neste estudo, «apoio à decisão» tem um alcance operacional restrito: produzir uma configuração inicial editável e tornar explícitos os dados considerados. Não foi implementada uma função objectivo nem uma comparação automática de robustez, peso, montagem ou adequação anatómica. Por esse motivo, o processo é designado como sugestão inicial condicionada e não como optimização. A aceitação, correcção ou rejeição dos valores ocorre fora do modelo de linguagem e antecede a geração e a exportação da geometria.",
]

SECTION_63_BEFORE_TABLE = [
    "A avaliação desta componente verifica a coerência das sugestões face ao esquema e aos intervalos de referência adoptados. O termo «antropométrica» descreve a origem dos campos e das referências; não significa que exista confirmação anatómica individual. Os resultados são apresentados no Capítulo 8, mantendo esta secção dedicada ao protocolo.",
    "O protocolo executado em 28 e 29 de Junho de 2026 usou o fornecedor Anthropic e o modelo claude-sonnet-4-6. A chamada admitia 1024 tokens e não fixava a temperatura. O pedido incluía a descrição do caso, o identificador do modelo, nomes exactos dos parâmetros, tipos, limites, valores correntes, etiquetas explicativas e, quando existia correspondência, uma referência populacional. O pedido exigia um objecto JSON com pares parâmetro–valor. Foram conservados o modelo utilizado, as condições da chamada, as entradas, as saídas e as decisões de correcção relevantes.",
    "Foram usados cinco perfis baseados em indicadores demográficos e três cenários de ausência unilateral com diferentes níveis de detalhe: medidas completas da mão contralateral, uma medida directa e descrição demográfica. Uma bateria complementar reuniu 15 cenários de entrada vaga, comparativa, multilingue ou sem medidas. Para examinar a lateralidade, foram ainda arquivadas 12 execuções antes da correcção, correspondentes a pedidos de mão esquerda e direita repetidos quatro vezes. Os cenários simulam entradas possíveis e não constituem avaliação centrada no utilizador, porque nenhuma pessoa participou no estudo.",
    "Os critérios foram: JSON interpretável; chaves pertencentes ao esquema; valores dentro dos intervalos; preservação das medidas fornecidas; ordem relativa dos dedos definida no protocolo; resposta diferenciada a idade e sexo quando a base continha referência compatível; e propagação dos valores para a geometria. Países ausentes da base, como Brasil, Japão e Alemanha, funcionaram como testes de resposta a cobertura incompleta. Nesses casos, o país não sustenta uma correspondência nacional: o mecanismo selecciona o perfil disponível com melhor pontuação noutros atributos ou prossegue sem referência quando a pontuação mínima não é atingida.",
    "Em 14 de Julho de 2026 foi executada uma campanha complementar com respostas de IA simuladas e previamente controladas. Esta campanha não contactou um modelo de linguagem e, por isso, não mede variabilidade, repetibilidade ou precisão da IA. Serviu para observar o comportamento da plataforma perante uma resposta válida, JSON inválido, campos de lateralidade, valores fora do intervalo e nova tentativa após erro. A lateralidade foi preservada e uma resposta inválida não alterou o último estado válido. Em contrapartida, um valor acima do máximo foi detectado pelo ensaio, mas permaneceu no estado interno; foi também aceite por pedido directo um texto num campo definido como numérico. Estes dois casos são registados como fragilidades de controlo, não como respostas válidas.",
    "A cadeia contém operações determinísticas e uma operação gerada por modelo de linguagem. A distinção é sintetizada na Tabela 6.2.",
]

TABLE_62 = [
    ["Tarefa", "Mecanismo", "Resultado"],
    ["Identificar sexo e idade explícitos", "Analisador de texto e, quando faltam campos, extracção opcional por claude-haiku-4-5-20251001 a temperatura 0", "Atributos para procurar uma referência populacional"],
    ["Escolher o perfil disponível mais próximo", "Pontuação por sexo, grupo etário, idade e país, com critérios secundários de qualidade", "Referência quantitativa; não corresponde a diagnóstico nem a correspondência nacional garantida"],
    ["Sugerir campos em falta", "claude-sonnet-4-6", "Ponto de partida sujeito a alterações entre execuções"],
    ["Declarar tipos e limites", "Ficheiro de configuração do modelo", "Intervalos e tipos disponíveis para a interface, para o pedido e para a verificação"],
    ["Verificar a resposta antes da aplicação", "Interpretação do JSON e confronto com o modelo activo", "Campos desconhecidos e lateralidade excluídos; controlo de tipos e intervalos ainda incompleto na versão avaliada"],
    ["Definir lateralidade", "Controlo da interface com a função laterality", "Escolha fixa excluída das sugestões"],
    ["Gerar a geometria", "Regras OpenSCAD executadas em WebAssembly", "Forma determinística para um mesmo conjunto de parâmetros e versão de código"],
    ["Aceitar, corrigir ou rejeitar a configuração", "Designer ou técnico responsável", "Decisão humana antes da exportação e de qualquer utilização posterior"],
]

SECTION_63_AFTER_TABLE = [
    "O protocolo não mede exactidão clínica da IA, porque não existe uma referência individual para cada cenário. Também não compara fornecedores, modelos de linguagem, temperaturas ou estratégias de pedido. Como a campanha complementar utilizou respostas simuladas, esta também não sustenta conclusões sobre estabilidade do claude-sonnet-4-6. A interpretação limita-se ao comportamento observado nas execuções iniciais e à resposta da plataforma nos casos de controlo documentados. Os resultados consolidados são apresentados no Capítulo 8 e a matriz integral de casos consta do Anexo B.",
]

SECTION_64_BEFORE_FIGURE = [
    "Para interpretar as saídas do sistema, distinguem-se três estados: sugestão produzida pelo modelo de linguagem; configuração aceite ou corrigida na interface; e resultado submetido a verificação geométrica e de fabrico. A passagem entre estes estados não demonstra ajuste anatómico, conforto, segurança estrutural ou validade clínica.",
    "Os riscos técnicos relevantes são respostas plausíveis para perfis pouco representados, campos sem fundamento suficiente e combinações que parecem respeitar parâmetros isolados, mas falham na geometria completa. A versão avaliada reduz parte destes riscos através do esquema activo, da exclusão de campos desconhecidos, do controlo determinístico da lateralidade e da inspecção posterior da malha. Contudo, os testes demonstraram que declarar um intervalo não basta: a mesma verificação deve actuar antes de o valor entrar no estado da aplicação, ser guardado ou seguir para a geração geométrica. As salvaguardas existentes tornam alguns erros localizáveis, mas não garantem adequação do resultado (Panchal et al., 2019; Yüksel et al., 2023).",
    "A Figura 6.1 sintetiza esta tensão entre desafios de explicabilidade e princípios de IA responsável. No contexto desta investigação, a figura mostra que a responsabilidade depende do desempenho preditivo e de condições como transparência, possibilidade de examinar as decisões, privacidade, justiça e prestação de contas. Estes princípios reforçam a opção do sistema por uma IA de apoio, limitada por regras e sujeita a revisão humana (Barredo Arrieta et al., 2020).",
]

SECTION_64_AFTER_FIGURE = [
    "No plano ético, a arquitectura examinada usa referências antropométricas não clínicas e cenários simulados, mantém as chaves dos fornecedores no servidor e diferencia acessos. Permanecem por implementar ou avaliar a apresentação sistemática da origem das referências, a comunicação da incerteza, a minimização de dados num eventual uso com pessoas e a compreensão dos avisos pelos diferentes perfis. Estes requisitos correspondem às dimensões de transparência, privacidade e prestação de contas sintetizadas na Figura 6.1 (Barredo Arrieta et al., 2020).",
    "Consequentemente, a evidência permite avaliar a integração e as salvaguardas técnicas da IA, mas não autoriza classificá-la como autoridade clínica nem como mecanismo autónomo de personalização. A qualidade das sugestões continua condicionada pela cobertura dos dados, pelo esquema do modelo e pela verificação das geometrias produzidas.",
]


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(
        paragraph_text(p).startswith("O fluxo organiza-se em três camadas")
        for p in root.xpath("//w:body/w:p", namespaces=NS)
    ):
        raise RuntimeError("The Chapter 6 AI revision is already present")

    # Section 6.1 contains prose only.
    start = find_body_paragraph(root, "6.1 Papel da IA no sistema proposto")
    end = find_body_paragraph(root, "6.2 IA na parametrização, personalização e apoio à decisão")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p"))
    replace_section(start, end, normal_elements(template, SECTION_61))

    # Section 6.2 preserves and updates Table 6.1.
    start = find_body_paragraph(root, "6.2 IA na parametrização, personalização e apoio à decisão")
    end = find_body_paragraph(root, "6.3 Avaliação das sugestões paramétricas apoiadas por IA")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p"))
    caption = find_body_paragraph(root, "Tabela 6.1 — Especificação técnica dos modelos de IA e do contrato de sugestão paramétrica")
    table = caption.getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("Table 6.1 was not found after its caption")
    caption_copy = deepcopy(caption)
    keep_with_next(caption_copy)
    table_copy = deepcopy(table)
    rewrite_table(table_copy, TABLE_61)
    replacement = normal_elements(template, SECTION_62_BEFORE_TABLE)
    replacement.extend([caption_copy, table_copy])
    replacement.extend(normal_elements(template, SECTION_62_AFTER_TABLE))
    replace_section(start, end, replacement)

    # Section 6.3 preserves and updates Table 6.2.
    start = find_body_paragraph(root, "6.3 Avaliação das sugestões paramétricas apoiadas por IA")
    end = find_body_paragraph(root, "6.4 Ajuste, verificação e limitações éticas e técnicas")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p"))
    caption = find_body_paragraph(root, "Tabela 6.2 — Distribuição de tarefas entre regras, IA e supervisão humana")
    table = caption.getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("Table 6.2 was not found after its caption")
    caption_copy = deepcopy(caption)
    keep_with_next(caption_copy)
    table_copy = deepcopy(table)
    rewrite_table(table_copy, TABLE_62)
    replacement = normal_elements(template, SECTION_63_BEFORE_TABLE)
    replacement.extend([caption_copy, table_copy])
    replacement.extend(normal_elements(template, SECTION_63_AFTER_TABLE))
    replace_section(start, end, replacement)

    # Section 6.4 preserves Figure 6.1 and its source line.
    start = find_body_paragraph(root, "6.4 Ajuste, verificação e limitações éticas e técnicas")
    end = find_body_paragraph(root, "Capítulo 7 — Princípios de Interface e Decisões de Interacção")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p") and paragraph_text(element))
    caption = find_body_paragraph(root, "Figura 6.1 — Relação entre desafios de explicabilidade e princípios de IA responsável.")
    image = caption.getprevious()
    source = caption.getnext()
    if image is None or not image.xpath(".//w:drawing", namespaces=NS):
        raise RuntimeError("Figure 6.1 drawing was not found")
    replacement = normal_elements(template, SECTION_64_BEFORE_FIGURE)
    replacement.extend([deepcopy(image), deepcopy(caption), deepcopy(source)])
    replacement.extend(normal_elements(template, SECTION_64_AFTER_FIGURE))
    replace_section(start, end, replacement)

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
