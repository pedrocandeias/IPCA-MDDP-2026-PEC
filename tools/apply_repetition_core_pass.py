#!/usr/bin/env python3
"""Apply the focused repetition-reduction pass to the revised thesis DOCX.

The script replaces only Sections 3.2, 6.1, 6.2, 6.4 and 7.1–7.3. Existing
tables, figures, captions, sources and document styles are preserved by editing
the OOXML package in place.
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
    if text.startswith(" ") or text.endswith(" "):
        node.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    node.text = text


def clone_paragraph(template: etree._Element, text: str) -> etree._Element:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, text)
    return paragraph


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


def replace_section(
    start: etree._Element,
    end: etree._Element,
    elements: list[etree._Element],
) -> None:
    for old in elements_between(start, end):
        old.getparent().remove(old)
    for element in elements:
        end.addprevious(element)


SECTION_32 = [
    "Com base no enquadramento do Capítulo 2, o design industrial é operacionalizado como prática investigativa através da explicitação e do ensaio das traduções entre fontes antropométricas, parâmetros editáveis, regras geométricas, estados da interface e peças fabricadas. Esta opção relaciona-se com os designerly ways of knowing, que reconhecem a experimentação material e a formulação projectual como modos de produção de conhecimento (Cross, 1982). A unidade de análise é, portanto, a cadeia de decisões e transformações do protótipo, e não a experiência de uma pessoa utilizadora.",
    "O contributo é examinado pela capacidade de localizar a origem de cada valor, observar a sua propagação e documentar falhas e alterações. Desempenho clínico e efeitos na experiência de pessoas amputadas não foram avaliados; a dimensão humana funciona neste estudo como requisito e limite ético fundamentado na literatura.",
    "A hipótese principal sustenta que a articulação entre dados antropométricos, design paramétrico, plataforma web e apoio de inteligência artificial permite estabelecer um fluxo técnico coerente para configurar, gerar, exportar e materializar variantes dos modelos seleccionados.",
    "Três hipóteses secundárias orientam a avaliação: relações geométricas e limites explícitos oferecem maior controlo do que o escalonamento uniforme; sugestões de inteligência artificial limitadas pelo esquema do modelo podem fornecer pontos de partida úteis, desde que decisões críticas permaneçam sob regras e supervisão humana; e a passagem por malha, preparação para impressão e protótipo físico revela falhas que a análise isolada dos valores numéricos pode ocultar. Estas hipóteses dizem respeito ao protótipo e aos casos estudados. Adequação anatómica individual, usabilidade, conforto, aceitação, redução da dependência de especialistas e impacto em contextos com poucos recursos ficaram fora da avaliação.",
]

SECTION_61 = [
    "No sistema desenvolvido, a IA desempenha uma função diferente da que predomina nos estudos sobre próteses de membro superior. Em vez de interpretar biosinais, reconhecer gestos ou controlar o dispositivo, o modelo de linguagem sugere valores iniciais para uma configuração geométrica já formalizada (Cordella et al., 2016; Marinelli et al., 2022; Peerdeman et al., 2011).",
    "Esta aplicação responde à fragmentação identificada entre referências antropométricas, modelos paramétricos e interfaces de configuração. A plataforma reúne esses componentes, mas não atribui à IA a geração da geometria, a selecção autónoma do dispositivo ou a validação do resultado. Os precedentes de modelação ajustável e de métodos orientados por dados sustentam esta articulação sem constituírem equivalentes directos do sistema implementado (Gu et al., 2024; da Silveira Romero et al., 2025; Saldarriaga et al., 2024).",
    "Concretamente, o serviço recebe uma descrição textual, o esquema do modelo activo, os valores correntes, os limites declarados e, quando disponível, uma referência populacional. A sua saída é um conjunto de pares parâmetro–valor que funciona como ponto de partida. A aplicação filtra os campos recebidos; a interface apresenta os valores; e o OpenSCAD gera a geometria segundo regras independentes do modelo de linguagem.",
    "A fronteira entre estas operações corresponde à arquitectura descrita na Secção 5.2: a chamada externa produz uma sugestão probabilística, enquanto a aplicação dos valores, a lateralidade e a construção geométrica permanecem em componentes identificáveis. O princípio de supervisão fundamentado na Secção 2.6 é, assim, materializado por limites, filtragem, revisão da configuração e decisão humana antes da exportação. As regras concretas e o protocolo de ensaio são apresentados nas Secções 6.2 e 6.3.",
]

SECTION_62_BEFORE_TABLE = [
    "À luz das distinções estabelecidas nos Capítulos 2 e 4, a personalização apoiada por IA não designa variação livre da forma. No protótipo, designa a proposta de valores para parâmetros previamente definidos, com relações geométricas, intervalos e campos protegidos. A independência entre dimensões dos dedos e a insuficiência do escalonamento uniforme fundamentam o espaço paramétrico; não são decisões tomadas pelo modelo de linguagem (Lim et al., 2018; Saldarriaga et al., 2024; da Silveira Romero et al., 2025).",
    "A operacionalização desta lógica ocorre em dois objectos distintos. O primeiro é um vector numérico de parâmetros geométricos, consumido directamente pela interface e pelos modelos OpenSCAD. O segundo é um contexto semântico para a IA, que descreve a origem das medições, campos em falta, incerteza, valores atípicos, tolerâncias, hardware seleccionado e notas sobre parâmetros derivados. Esta separação é importante porque impede confundir cálculo geométrico com raciocínio apoiado: os parâmetros numéricos alimentam o modelo; o contexto semântico ajuda a IA a explicar, ponderar ou sugerir ajustes, mas não substitui as regras determinísticas que geram a geometria.",
    "No protótipo implementado, esta separação é materializada pela construção dinâmica do pedido enviado ao modelo de linguagem. O pedido inclui a descrição livre do utilizador, o esquema vivo do modelo seleccionado, os nomes exactos dos parâmetros, as legendas, os tipos, os limites e os valores correntes. Quando existe correspondência com um perfil populacional importado, inclui também as médias medidas desse grupo como referência explícita. Deste modo, a IA não infere valores num espaço aberto: opera dentro de uma gramática paramétrica previamente declarada, limitada pelo modelo activo e sujeita a filtragem posterior pela aplicação.",
    "A designação «modelo» é usada, nesta investigação, em dois sentidos técnicos distintos: o modelo de linguagem responsável pela sugestão paramétrica e o modelo CAD paramétrico ao qual essa sugestão é aplicada. Para evitar ambiguidade metodológica, a Tabela 6.1 explicita a configuração de IA efectivamente implementada no protótipo e a sua relação com os modelos paramétricos disponibilizados na plataforma.",
]

SECTION_62_AFTER_TABLE = [
    "Neste estudo, «apoio à decisão» tem um alcance operacional restrito: produzir uma configuração inicial editável e tornar explícitos os dados considerados. Não foi implementada uma função objectivo nem uma comparação automática de robustez, peso, montagem ou adequação anatómica. A aceitação, correcção ou rejeição dos valores ocorre fora do modelo de linguagem e antecede a geração e a exportação da geometria.",
]

SECTION_64_BEFORE_FIGURE = [
    "Para interpretar as saídas do sistema, distinguem-se três estados: sugestão produzida pelo modelo de linguagem; configuração aceite ou corrigida na interface; e resultado submetido a verificação geométrica e de fabrico. A passagem entre estes estados não demonstra ajuste anatómico, conforto, segurança estrutural ou validade clínica.",
    "Os riscos técnicos relevantes são respostas plausíveis para perfis pouco representados, campos sem fundamento suficiente e combinações que respeitam limites isolados, mas falham na geometria completa. A versão avaliada reduz estes riscos através do esquema activo, limitação de intervalos, rejeição de chaves desconhecidas, controlo determinístico da lateralidade e inspecção posterior da malha. Estas salvaguardas tornam erros localizáveis, mas não garantem adequação do resultado (Panchal et al., 2019; Yüksel et al., 2023).",
    "A Figura 6.1 sintetiza esta tensão entre desafios de explicabilidade e princípios de IA responsável. No contexto desta investigação, a figura mostra que a responsabilidade depende do desempenho preditivo e de condições como transparência, possibilidade de examinar as decisões, privacidade, justiça e prestação de contas. Estes princípios reforçam a opção do sistema por uma IA de apoio, limitada por regras e sujeita a revisão humana (Barredo Arrieta et al., 2020).",
]

SECTION_64_AFTER_FIGURE = [
    "No plano ético, a arquitectura examinada usa referências antropométricas não clínicas e cenários simulados, mantém as chaves dos fornecedores no servidor e diferencia acessos. Permanecem por implementar ou avaliar a apresentação sistemática da proveniência, a comunicação da incerteza, a minimização de dados num eventual uso com pessoas e a compreensão dos avisos pelos diferentes perfis. Estes requisitos correspondem às dimensões de transparência, privacidade e prestação de contas sintetizadas na Figura 6.1 (Barredo Arrieta et al., 2020).",
    "Consequentemente, a evidência permite avaliar a integração e as salvaguardas técnicas da IA, mas não autoriza classificá-la como autoridade clínica nem como mecanismo autónomo de personalização. A qualidade das sugestões continua condicionada pela cobertura dos dados, pelo esquema do modelo e pela verificação das geometrias produzidas.",
]

SECTION_71 = [
    "A interface organiza o fluxo implementado em seis operações: seleccionar um modelo, introduzir ou obter valores iniciais, ajustar parâmetros, gerar e observar a geometria, guardar a configuração e exportar ficheiros. Esta sequência traduz a arquitectura técnica em tarefas visíveis; a sua facilidade de utilização não foi avaliada com participantes.",
    "A composição é modular e orientada por tarefa. A selecção do modelo define o esquema activo; os controlos apresentam parâmetros editáveis e respectivos intervalos; a pré-visualização mostra a geometria efectivamente produzida; e as acções de guardar, recuperar e exportar preservam estados distintos. Esta organização procura manter uma relação identificável entre valor, acção e consequência formal (Colombo et al., 2015; Peixoto et al., 2025).",
    "O espaço de configuração apresentado não é ilimitado. A interface expõe apenas os campos declarados para o modelo, aplica os intervalos existentes e exclui decisões como a lateralidade do pedido enviado à IA. Esta contenção corresponde a uma salvaguarda implementada; o seu efeito na compreensão ou na confiança permanece por medir.",
    "A pré-visualização é calculada localmente por OpenSCAD em WebAssembly. O Web Worker separa essa execução da tarefa principal da interface, evitando o bloqueio directo durante o cálculo. Não foram medidos o tempo percebido, a compreensão dos estados nem a qualidade da interacção (Abbas Alili et al., 2023; Quintero et al., 2018).",
    "Assim, esta secção descreve uma especificação projectual e as funções efectivamente disponíveis. Clareza, carga cognitiva, aprendizagem e adequação aos diferentes perfis permanecem hipóteses para avaliação futura.",
]

SECTION_72_BEFORE_FIGURE = [
    "Os fundamentos de participação e de distribuição de autoridade foram discutidos na Secção 2.7. Na implementação, traduzem-se em três perfis de acesso — administrador, técnico e utilizador — cuja adequação às práticas profissionais ainda não foi avaliada.",
    "O administrador gere contas, permissões e relações de atribuição. O perfil técnico pode criar, editar, guardar e acompanhar configurações sob a sua responsabilidade. O utilizador dispõe de consulta, visualização e acompanhamento das configurações que lhe estão associadas. Esta distribuição descreve permissões do protótipo, não competências clínicas verificadas.",
    "Os parâmetros apresentados dependem do modelo activo e do perfil de acesso. Valores geométricos editáveis são limitados pelo esquema; a lateralidade é controlada pela interface; e a aceitação de sugestões permanece uma acção distinta da sua geração. A plataforma não implementa decisões clínicas sobre encaixe, tolerância dos tecidos ou adequação funcional.",
    "Esta separação materializa uma colaboração assimétrica: o perfil técnico possui maior capacidade de intervenção e o utilizador final acompanha o processo. Não foram medidos os efeitos desta distribuição sobre compreensão, confiança, rapidez ou qualidade da decisão (Bai et al., 2024; Colombo et al., 2015; Quintero et al., 2018).",
    "A Figura 7.1 evidencia a importância de analisar a utilização concreta do dispositivo, para além da sua configuração digital. A avaliação com utilizadores permite identificar problemas relacionados com o ajuste ao corpo, o modo de activação, o conforto e a adequação funcional, aspectos que dificilmente são detectados de forma suficiente apenas através do modelo digital. Para esta investigação, a imagem constitui um ponto de referência metodológico: embora a plataforma possa tornar o processo mais claro e configurável, a validação futura continua a depender da observação do uso em contexto real (Silva et al., 2018).",
]

SECTION_73 = [
    "A mediação fundamentada no Capítulo 2 torna-se observável, no protótipo, na sequência entre leitura dos dados, proposta de valores, geração da geometria, revisão e exportação. A interface não acrescenta uma nova teoria de personalização; materializa decisões sobre o que é mostrado, editado, guardado ou reservado.",
    "Quatro mecanismos concretizam essa função: exposição selectiva dos parâmetros; apresentação dos respectivos limites; diferenciação de permissões; e separação visual entre sugestão, configuração e geometria gerada. Em conjunto, estes mecanismos tornam parte das dependências auditável, mas também condicionam o conjunto de alternativas que pode ser explorado (Bai et al., 2024; Peixoto et al., 2025; Quintero et al., 2018).",
    "Esta condição impede considerar a interface neutra. Um valor apresentado como sugestão pode adquirir aparência de validade, mesmo quando resulta de uma referência populacional incompleta ou de uma saída probabilística. Por isso, a proveniência, a incerteza e o estatuto de cada valor devem permanecer visíveis; a versão avaliada implementa apenas parte dessa comunicação.",
    "A evidência disponível permite descrever a organização das decisões e identificar as salvaguardas incorporadas. Não permite concluir que os diferentes perfis compreendem os limites, tomam melhores decisões ou utilizam a plataforma com menor esforço. Essas questões exigem observação de tarefas com participantes.",
    "O contributo desta camada de interface é, portanto, tornar operacional e discutível a distribuição de informação e controlo no fluxo técnico. A responsabilidade pela adequação da configuração e a validação do dispositivo permanecem fora da interface e do alcance demonstrado pelo estudo.",
]


def normal_elements(template: etree._Element, texts: list[str]) -> list[etree._Element]:
    return [clone_paragraph(template, text) for text in texts]


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(
        paragraph_text(p).startswith("A mediação fundamentada no Capítulo 2 torna-se observável")
        for p in root.xpath("//w:body/w:p", namespaces=NS)
    ):
        raise RuntimeError("The repetition-core pass is already present")

    # Simple prose-only sections.
    for start_text, end_text, replacement in [
        ("3.2 O design industrial como prática investigativa", "3.3 Estrutura metodológica do projecto", SECTION_32),
        ("6.1 Papel da IA no sistema proposto", "6.2 IA na parametrização, personalização e apoio à decisão", SECTION_61),
        ("7.1 Estratégia de interacção e decisões de UI/UX", "7.2 Papéis previstos e distribuição de decisões", SECTION_71),
        ("7.3 Mediação do processo de design e reflexão crítica", "Capítulo 8 — Avaliação e Discussão", SECTION_73),
    ]:
        start = find_body_paragraph(root, start_text)
        end = find_body_paragraph(root, end_text)
        old = elements_between(start, end)
        template = next((element for element in old if element.tag == qn("p")), None)
        if template is None:
            raise RuntimeError(f"No normal paragraph in section {start_text}")
        replace_section(start, end, normal_elements(template, replacement))

    # Section 6.2 preserves Table 6.1.
    start = find_body_paragraph(root, "6.2 IA na parametrização, personalização e apoio à decisão")
    end = find_body_paragraph(root, "6.3 Avaliação das sugestões paramétricas apoiadas por IA")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p"))
    caption = find_body_paragraph(root, "Tabela 6.1 — Especificação técnica dos modelos de IA e do contrato de sugestão paramétrica")
    table = caption.getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("Table 6.1 is not after its caption")
    replacement = normal_elements(template, SECTION_62_BEFORE_TABLE)
    replacement.extend([deepcopy(caption), deepcopy(table)])
    replacement.extend(normal_elements(template, SECTION_62_AFTER_TABLE))
    replace_section(start, end, replacement)

    # Section 6.4 preserves Figure 6.1 and its source.
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

    # Section 7.2 preserves Figure 7.1 and its source.
    start = find_body_paragraph(root, "7.2 Papéis previstos e distribuição de decisões")
    end = find_body_paragraph(root, "7.3 Mediação do processo de design e reflexão crítica")
    old = elements_between(start, end)
    template = next(element for element in old if element.tag == qn("p") and paragraph_text(element))
    caption = find_body_paragraph(
        root,
        "Figura 7.1 — Exemplo publicado de teste de uma prótese impressa em 3D com um utilizador; esta actividade não integrou a avaliação da presente dissertação.",
    )
    image = caption.getprevious()
    source = caption.getnext()
    if image is None or not image.xpath(".//w:drawing", namespaces=NS):
        raise RuntimeError("Figure 7.1 drawing was not found")
    replacement = normal_elements(template, SECTION_72_BEFORE_FIGURE)
    replacement.extend([deepcopy(image), deepcopy(caption), deepcopy(source)])
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
