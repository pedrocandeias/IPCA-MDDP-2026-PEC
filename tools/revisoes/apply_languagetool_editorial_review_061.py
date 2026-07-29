#!/usr/bin/env python3
"""Aplica a revisão humana das propostas do LanguageTool na versão 0.4.61."""

from __future__ import annotations

import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


REPLACEMENTS = [
    # Concordância e gramática: apenas erros reais ou ambiguidades relevantes.
    ("pela comportamento mecânico", "pelo comportamento mecânico"),
    ("definido pela Regulamento", "definido pelo Regulamento"),
    (
        "como parte de um sistema estruturado de variáveis capaz de descrever",
        "como componentes de um sistema estruturado capaz de descrever",
    ),
    ("não são medida da robustez", "não constituem uma medida da robustez"),
    ("sem pressupor que todos representam", "sem pressupor que todos representem"),
    ("não equivalem a avaliação clínica", "não equivalem a uma avaliação clínica"),
    ("O estado final da plataforma foi inspeccionada", "O estado final da plataforma foi inspeccionado"),

    # Clareza: relações espaciais ou operacionais tornadas explícitas.
    ("maior controlo dimensional dentro de margens reduzidas", "maior controlo dimensional em intervalos reduzidos"),
    ("ajustar dimensões ou características dentro de intervalos válidos", "ajustar dimensões ou características nos intervalos válidos"),
    ("modificar dimensões dentro das relações e limites codificados", "modificar dimensões segundo as relações e os limites codificados"),
    ("manter os valores dentro da gama declarada", "manter os valores na gama declarada"),
    ("verificações dentro da transformação geométrica", "verificações na própria transformação geométrica"),
    ("analisar o processo dentro da plataforma", "analisar o processo na plataforma"),
    ("valores dentro dos intervalos", "valores nos intervalos"),
    ("permaneceram dentro dos intervalos", "permaneceram nos intervalos"),
    ("permanecem dentro dos intervalos", "permanecem nos intervalos"),

    # Redundância: apenas quando a expressão não transporta uma distinção temporal ou quantitativa.
    ("classificadas de acordo com a fonte de energia", "classificadas segundo a fonte de energia"),
    ("com o objectivo de assegurar", "para assegurar"),
    ("com o objetivo de assegurar", "para assegurar"),
    ("dentro de um espaço", "num espaço"),
    ("organizados de acordo com a anatomia disponível", "organizados em função da anatomia disponível"),
    ("na medida em que a adequação geométrica", "porque a adequação geométrica"),
    ("pode alterar o resultado final", "pode alterar o resultado"),
    ("os resultados finais desejáveis", "os resultados desejáveis"),
    ("o resultado final pode depender", "o resultado pode depender"),

    # Registo formal: a alternativa explicita o mecanismo, o critério ou a relação.
    ("essa mediação através de um protótipo", "essa mediação por meio de um protótipo"),
    ("captados através de", "captados por"),
    ("avaliado através de critérios", "avaliado segundo critérios"),
    ("ou através de uma encomenda", "ou por meio de uma encomenda"),
    ("A digitalização 3D, através de", "A digitalização 3D por"),
    ("validação através de métricas", "validação com métricas"),
    ("consistência da medição através de posturas", "consistência da medição mediante posturas"),
    (
        "a personalização é obtida através da combinação de módulos interoperáveis, permitindo adaptar a funcionalidade através de combinações e substituições",
        "a personalização resulta da combinação de módulos interoperáveis, permitindo adaptar a funcionalidade pela recombinação ou substituição dos módulos",
    ),
    ("materializar-se através de módulos", "materializar-se em módulos"),
    ("configurado através de parâmetros", "configurado por parâmetros"),
    ("documentada através de episódios", "documentada com base em episódios"),
    ("ocorrem localmente no navegador, através de uma versão", "ocorrem localmente no navegador, por meio de uma versão"),
    ("utilizador através de autenticação", "utilizador por autenticação"),
    ("define a geometria através de instruções", "define a geometria a partir de instruções"),
    ("da operação através de uma plataforma", "da sua operação numa plataforma"),
    ("Depois de aceite ou corrigida a configuração", "Após a aceitação ou correcção da configuração"),
    ("receber texto através de um pedido directo", "receber texto por meio de um pedido directo"),
    ("Depois de corrigida essa configuração", "Após a correcção dessa configuração"),
    ("modelos de mão protésica através de parâmetros", "modelos de mão protésica com parâmetros"),
    ("a personalização através de funções distintas", "a personalização por meio de funções distintas"),
    ("foi conduzida através de pesquisas bibliográficas", "recorreu a consultas bibliográficas"),
    ("gerada depois de confirmação humana", "gerada após confirmação humana"),
    ("referência populacional através de uma pontuação", "referência populacional com base numa pontuação"),

    # Pontuação e precisão combinadas.
    ("por exemplo através da medição", "por exemplo, pela medição"),
    ("informação interna, por exemplo sobre", "informação interna, por exemplo, sobre"),

    # Concisão: só se adopta quando a nova construção permanece natural e inequívoca.
    ("De modo recorrente, a literatura sublinha", "A literatura sublinha recorrentemente"),
    ("A literatura associa, de forma recorrente,", "A literatura associa recorrentemente"),
    (
        "Esta persistência do abandono é sintetizada de forma clara na Figura 2.2, que relaciona uso, rejeição primária e rejeição secundária, reforçando que o problema não é marginal, mas estrutural no campo das próteses de membro superior.",
        "A Figura 2.2 sintetiza claramente esta persistência do abandono ao relacionar o uso, a rejeição primária e a rejeição secundária. Esta relação mostra que o problema não é marginal, mas estrutural no campo das próteses de membro superior.",
    ),
    ("torna-se mais clara quando se observa a multiplicidade", "torna-se mais clara perante a multiplicidade"),
    ("podem representar de forma limitada as alterações reais de volume", "podem representar apenas parcialmente as alterações reais de volume"),
    ("De forma ampla, a IA pode ser entendida", "Em termos gerais, a IA pode ser entendida"),
    ("acomodar diferenças individuais de forma controlada", "acomodar diferenças individuais segundo regras definidas"),
    ("torna-se particularmente visível quando se analisam os níveis", "torna-se particularmente visível na análise dos níveis"),
    ("devem ser considerados de forma articulada", "devem ser considerados em conjunto"),
    (
        "A Figura 4.1 mostra um exemplo de decomposição paramétrica em comprimentos, larguras e secções articulares, o que clarifica o tipo de estrutura dimensional que sustenta a transição da antropometria para a geometria configurável.",
        "A Figura 4.1 mostra um exemplo de decomposição paramétrica em comprimentos, larguras e secções articulares e torna explícita a estrutura dimensional que sustenta a transição da antropometria para a geometria configurável.",
    ),
    ("apresentam correlações imperfeitas entre si e variam de forma desigual", "apresentam correlações imperfeitas entre si e não variam de modo uniforme"),
    ("gerar múltiplas variantes de forma controlada", "gerar múltiplas variantes segundo regras explícitas"),
    ("não variam necessariamente de forma proporcional", "não variam necessariamente na mesma proporção"),
    ("Essa experiência foi útil para clarificar", "Essa experiência permitiu clarificar"),
    ("não aplica todas as restrições de modo uniforme", "não aplica uniformemente todas as restrições"),
    (
        "aspectos que dificilmente são detectados de forma suficiente apenas através do modelo digital",
        "aspectos que dificilmente podem ser avaliados adequadamente apenas com o modelo digital",
    ),
    ("responderam de forma semelhante aos mesmos perfis", "apresentaram respostas semelhantes aos mesmos perfis"),
    ("tinha produzido um factor de escala", "produziu um factor de escala"),
    ("não estava a responder corretamente", "não respondia corretamente"),
    ("Os modelos integrados respondem de forma distinta aos mesmos perfis", "Os modelos integrados apresentam respostas distintas aos mesmos perfis"),
    ("o método é documentado de forma rigorosa", "o método dispõe de documentação rigorosa"),
    (
        "A Série A serve para documentar os projectos tal como foram preparados, não para os comparar entre si.",
        "A Série A documenta os projectos tal como foram preparados; não os compara entre si.",
    ),

    # Estilo: divisão de frases longas e eliminação de formulações vagas.
    (
        ", a passagem de processos participativos para contextos de implementação e a integração de factores sociais e culturais na investigação e no desenvolvimento",
        ". Somam-se a passagem de processos participativos para contextos de implementação e a integração de factores sociais e culturais na investigação e no desenvolvimento",
    ),
    (
        "O Cyborg Beast, o Raptor Reloaded, a Flexy Hand, o Flexy Beast, o Paraglider Hand/Flexible Flyer, a Phoenix Hand e a Unlimbited Phoenix Hand não devem ser entendidos como objectos isolados, mas como variações de um ecossistema e-NABLE em que cada modelo traduz compromissos diferentes entre simplicidade de impressão, facilidade de montagem, robustez, custo, aparência e adequação anatómica.",
        "Entre eles encontram-se Cyborg Beast, Raptor Reloaded, Flexy Hand, Flexy Beast, Paraglider Hand/Flexible Flyer, Phoenix Hand e Unlimbited Phoenix Hand. Estes modelos não devem ser entendidos como objectos isolados, mas como variações de um ecossistema e-NABLE em que cada modelo traduz compromissos diferentes entre simplicidade de impressão, facilidade de montagem, robustez, custo, aparência e adequação anatómica.",
    ),
    ("redimensionada de forma proporcional como um todo", "redimensionada segundo uma única proporção em todas as suas partes"),
    (
        "controlo técnico supervisionado, evitando a opacidade excessiva e a transferência imprudente de responsabilidade para agentes sem formação específica",
        "controlo técnico supervisionado. Esta distinção procura evitar a opacidade excessiva e a transferência imprudente de responsabilidade para agentes sem formação específica",
    ),
    (
        "componentes com funções distintas, o que está de acordo com a literatura sobre configuradores digitais, segundo a qual a eficácia da personalização depende, em grande medida, da clareza com que o sistema delimita o espaço de acção disponível e articula",
        "componentes com funções distintas. Esta organização é coerente com a literatura sobre configuradores digitais. Segundo essa literatura, a eficácia da personalização depende, em grande medida, da clareza com que o sistema delimita o espaço de acção disponível e articula",
    ),
    (
        "Os cenários de controlo abrangeram valores nos limites, valores abaixo e acima dos limites, campos obrigatórios ausentes, texto num campo numérico, contradição entre idade e descrição, país sem correspondência directa na base, perfil inferior ao limite de um modelo, indisponibilidade da sugestão de IA, resposta inválida, falha de geração e tentativa de exportação sem geometria.",
        "Os cenários de controlo abrangeram valores nos limites, abaixo deles e acima deles; campos obrigatórios ausentes; texto num campo numérico; contradição entre idade e descrição; país sem correspondência directa na base; e perfil inferior ao limite de um modelo. Abrangeram também indisponibilidade da sugestão de IA, resposta inválida, falha de geração e tentativa de exportação sem geometria.",
    ),

    # Ajustes após a releitura das primeiras reformulações.
    (
        "Entre eles encontram-se Cyborg Beast, Raptor Reloaded, Flexy Hand, Flexy Beast, Paraglider Hand/Flexible Flyer, Phoenix Hand e Unlimbited Phoenix Hand.",
        "Este conjunto inclui Cyborg Beast, Raptor Reloaded, Flexy Hand, Flexy Beast, Paraglider Hand/Flexible Flyer, Phoenix Hand e Unlimbited Phoenix Hand.",
    ),
    ("A literatura associa estas taxas, de forma recorrente,", "A literatura associa recorrentemente estas taxas"),
    (
        "A modelação paramétrica exige, por isso, a definição de parametros independentes que permitem derivar proporções locais sem pressupor uma homotetia global do modelo, isto é, sem assumir que a prótese deve ser redimensionada segundo uma única proporção em todas as suas partes, mantendo invariáveis todas as relações geométricas entre as suas partes.",
        "A modelação paramétrica exige, por isso, parâmetros independentes que permitam derivar proporções locais sem pressupor uma homotetia global. Isto significa que as partes da prótese não são redimensionadas segundo uma proporção única nem mantêm invariáveis todas as relações geométricas entre si.",
    ),
    ("modelos de mão protésica com parâmetros", "modelos de mão protésica com base em parâmetros"),
]


def replace_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        occurrences = text.count(old)
        if occurrences:
            text = text.replace(old, new)
            count += occurrences
    return text, count


def replace_in_element(element: etree._Element, old: str, new: str) -> int:
    count = 0
    while True:
        nodes = element.xpath(".//w:t", namespaces=NS)
        full_text = "".join(node.text or "" for node in nodes)
        start = full_text.find(old)
        if start < 0:
            return count
        end = start + len(old)
        offset = 0
        inserted = False
        for node in nodes:
            value = node.text or ""
            node_start, node_end = offset, offset + len(value)
            overlap_start = max(start, node_start)
            overlap_end = min(end, node_end)
            if overlap_start < overlap_end:
                local_start = overlap_start - node_start
                local_end = overlap_end - node_start
                prefix = value[:local_start]
                suffix = value[local_end:]
                if not inserted:
                    node.text = prefix + new + suffix
                    inserted = True
                else:
                    node.text = prefix + suffix
                if node.text.startswith(" ") or node.text.endswith(" "):
                    node.set(f"{{{XML}}}space", "preserve")
            offset = node_end
        count += 1


def update_markdown() -> int:
    text = MARKDOWN.read_text(encoding="utf-8")
    initial_version = "Versão do documento: 0.4.60" in text
    if not initial_version and "Versão do documento: 0.4.61" not in text:
        raise RuntimeError("Não foi encontrada uma versão compatível com esta revisão")
    text, count = replace_text(text)
    if initial_version:
        text = text.replace("Versão do documento: 0.4.60", "Versão do documento: 0.4.61")
    MARKDOWN.write_text(text, encoding="utf-8")
    return count


def update_docx() -> int:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}
    document = etree.fromstring(files["word/document.xml"])
    count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        for old, new in REPLACEMENTS:
            count += replace_in_element(paragraph, old, new)
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, DOCX)
    return count


def main() -> None:
    markdown_changes = update_markdown()
    docx_changes = update_docx()
    print(f"Markdown: {markdown_changes} substituições")
    print(f"DOCX: {docx_changes} substituições")


if __name__ == "__main__":
    main()
