#!/usr/bin/env python3
"""Actualiza o DOCX canónico para a revisão conceptual e o fecho da P04 (0.4.53)."""

from __future__ import annotations

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
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS)).strip()


def set_paragraph_text(paragraph: etree._Element, value: str) -> None:
    properties = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not properties:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value


REPLACEMENTS = {
    "Tabela 8.4 — Entradas utilizadas nos cenários de avaliação da IA":
        "Tabela 8.4 — Descrições submetidas nos cenários de avaliação da IA",
    "Máximo de 1024 tokens; o código não fixa a temperatura na chamada ao claude-sonnet-4-6. O percurso OpenAI fixa temperatura de 0,7, mas não integra a avaliação reportada.":
        "Resposta limitada a 1024 tokens; o código não fixa a temperatura na chamada ao claude-sonnet-4-6, pelo que fica em vigor a configuração do fornecedor. O percurso OpenAI fixa a temperatura em 0,7, mas não integra a avaliação reportada.",
    "Objecto JSON simples no formato parâmetro–valor. A lateralidade é ignorada e os campos desconhecidos não são aplicados. Os testes revelaram que a verificação de tipos e intervalos ainda não é uniforme em todas as entradas.":
        "Objecto JSON simples no formato parâmetro–valor. A lateralidade é ignorada e os campos desconhecidos não são aplicados. Os testes revelaram que a verificação de tipos e intervalos ainda não é uniforme em todos os percursos de submissão.",
    "A avaliação inicial incidiu sobre a versão 14.67.0. A série complementar de ensaios de controlo da interface e das entradas foi executada na versão 14.69.0.":
        "A avaliação inicial incidiu sobre a versão 14.67.0. A série complementar de controlo da interface e dos dados submetidos foi executada na versão 14.69.0.",
    "O protocolo executado em 28 e 29 de Junho de 2026 usou o fornecedor Anthropic e o modelo claude-sonnet-4-6. A chamada admitia 1024 tokens e não fixava a temperatura. O pedido incluía a descrição do caso, o identificador do modelo, nomes exactos dos parâmetros, tipos, limites, valores correntes, etiquetas explicativas e, quando existia correspondência, uma referência populacional. O pedido exigia um objecto JSON com pares parâmetro–valor. Foram conservados o modelo utilizado, as condições da chamada, as entradas, as saídas e as decisões de correcção relevantes.":
        "A avaliação utilizou o fornecedor Anthropic e o modelo claude-sonnet-4-6. A resposta estava limitada a 1024 tokens e o código não fixava a temperatura. O pedido incluía a descrição do cenário, o identificador do modelo, os nomes exactos dos parâmetros, os respectivos tipos, limites e valores correntes, etiquetas explicativas e, quando existia correspondência, uma referência populacional. O pedido exigia um objecto JSON com pares parâmetro–valor. Foram conservados o modelo utilizado, as condições da chamada, as descrições submetidas, as respostas e as decisões de correcção relevantes.",
    "Foram usados cinco perfis baseados em indicadores demográficos e três cenários de ausência unilateral com diferentes níveis de detalhe: medidas completas da mão contralateral, uma medida directa e descrição demográfica. Uma bateria complementar reuniu 15 cenários de entrada vaga, comparativa, multilingue ou sem medidas. Para examinar a lateralidade, foram ainda arquivadas 12 execuções antes da correcção, correspondentes a pedidos de mão esquerda e direita repetidos quatro vezes. Os cenários simulam entradas possíveis e não constituem avaliação centrada no utilizador, porque nenhuma pessoa participou no estudo.":
        "Foram usados cinco perfis baseados em indicadores demográficos e três cenários de ausência unilateral com diferentes níveis de detalhe: medidas completas da mão contralateral, uma medida directa e descrição demográfica. Uma bateria complementar reuniu 15 cenários construídos a partir de descrições vagas, comparativas, multilingues ou sem medidas. Para examinar a lateralidade, foram ainda arquivadas 12 execuções antes da correcção, correspondentes a pedidos de mão esquerda e direita repetidos quatro vezes. Os cenários representam descrições hipotéticas que poderiam ser submetidas ao sistema e não constituem avaliação centrada no utilizador, porque nenhuma pessoa participou no estudo.",
    "Em 14 de Julho de 2026 foi executada uma série complementar de ensaios com respostas de IA simuladas e previamente controladas. Esta série de ensaios não contactou um modelo de linguagem e, por isso, não mede variação, consistência entre repetições ou precisão da IA. Serviu para observar o comportamento da plataforma perante uma resposta válida, JSON inválido, campos de lateralidade, valores fora do intervalo e nova tentativa após erro. A lateralidade foi preservada e uma resposta inválida não alterou o último estado válido. Em contrapartida, um valor acima do máximo foi detectado pelo ensaio, mas permaneceu no estado interno; foi também aceite por pedido directo um texto num campo definido como numérico. Estes dois casos são registados como fragilidades de controlo, não como respostas válidas.":
        "Numa série complementar de ensaios foram usadas respostas de IA simuladas e previamente controladas. Esta série não contactou um modelo de linguagem e, por isso, não mede a variação, a consistência entre repetições ou a precisão da IA. Serviu para observar o comportamento da plataforma perante uma resposta válida, JSON inválido, campos de lateralidade, valores fora do intervalo e nova tentativa após erro. A lateralidade foi preservada e uma resposta inválida não alterou o último estado válido. Em contrapartida, um valor acima do máximo foi detectado pelo ensaio, mas permaneceu no estado interno; foi também aceite por pedido directo um texto num campo definido como numérico. Estes dois casos são registados como fragilidades de controlo, não como respostas válidas.",
    "O espaço de configuração apresentado não é ilimitado. A interface expõe apenas os campos declarados para o modelo, apresenta os intervalos existentes e exclui decisões como a lateralidade do pedido enviado à IA. Esta contenção orienta a configuração, mas não garante, por si só, que todas as entradas respeitem as mesmas regras. Os testes complementares mostraram que um valor acima do intervalo podia permanecer no estado interno da aplicação e que um campo numérico podia receber texto através de um pedido directo. Assim, o controlo visual deve ser acompanhado pela verificação do valor antes de este ser aplicado, guardado ou enviado para a geometria.":
        "O espaço de configuração apresentado não é ilimitado. A interface expõe apenas os campos declarados para o modelo, apresenta os intervalos existentes e exclui decisões como a lateralidade do pedido enviado à IA. Esta contenção orienta a configuração, mas não garante, por si só, que todos os percursos de submissão respeitem as mesmas regras. Os testes complementares mostraram que um valor acima do intervalo podia permanecer no estado interno da aplicação e que um campo numérico podia receber texto através de um pedido directo. Assim, o controlo visual deve ser acompanhado pela verificação do valor antes de este ser aplicado, guardado ou enviado para a geometria.",
    "A separação entre sugestão, configuração e geometria constitui uma decisão projectual observável. Uma resposta de IA inválida preservou o último estado válido e permitiu nova tentativa, mostrando capacidade de recuperação nesse percurso. Contudo, a aplicação de um valor acima do intervalo revelou que a reversibilidade e a limitação do espaço paramétrico ainda não estão asseguradas em todas as entradas. A aprendizagem resultante é que mensagens, limites e regras devem permanecer coerentes para além dos controlos visíveis da interface.":
        "A separação entre sugestão, configuração e geometria constitui uma decisão projectual observável. Uma resposta de IA inválida preservou o último estado válido e permitiu nova tentativa, mostrando capacidade de recuperação nesse percurso. Contudo, a aplicação de um valor acima do intervalo revelou que a reversibilidade e a limitação do espaço paramétrico ainda não estão asseguradas em todos os percursos de submissão. A aprendizagem resultante é que mensagens, limites e regras devem permanecer coerentes para além dos controlos visíveis da interface.",
    "Os cenários de recuperação abrangeram valores nos limites, entradas inválidas, ausência de cobertura populacional directa, incompatibilidade entre perfil e modelo, indisponibilidade do serviço de IA, falha de renderização e tentativa de exportação sem geometria. A maioria dos percursos rejeitou a entrada, preservou o último estado válido ou permitiu nova tentativa. Foram, contudo, identificadas duas fragilidades relevantes para o design do controlo: uma sugestão simulada de IA acima do limite foi detectável pelo esquema, mas chegou a ser aplicada ao valor interno; e a interface rejeitou texto num campo numérico enquanto o pedido directo à plataforma aceitou esse mesmo tipo de valor. Estes resultados mostram que a protecção não deve depender apenas do controlo visual e que as mesmas regras têm de actuar antes de qualquer valor ser guardado ou enviado para a geometria.":
        "Os cenários de recuperação abrangeram valores nos limites, dados inválidos, ausência de cobertura populacional directa, incompatibilidade entre perfil e modelo, indisponibilidade do serviço de IA, falha de renderização e tentativa de exportação sem geometria. A maioria dos percursos rejeitou os dados inválidos, preservou o último estado válido ou permitiu nova tentativa. Foram, contudo, identificadas duas fragilidades relevantes para o design do controlo: uma sugestão simulada de IA acima do limite foi detectável pelo esquema, mas chegou a ser aplicada ao valor interno; e a interface rejeitou texto num campo numérico enquanto o pedido directo à plataforma aceitou esse mesmo tipo de valor. Estes resultados mostram que a protecção não deve depender apenas do controlo visual e que as mesmas regras têm de actuar antes de qualquer valor ser guardado ou enviado para a geometria.",
    "Descrição usada como entrada": "Descrição submetida",
    "Entrada completa com medições da mão intacta": "Perfil com medições completas da mão intacta",
    "Entrada parcial com dados demográficos e uma medição directa": "Perfil com dados demográficos e uma medição directa",
    "Entrada apenas demográfica": "Perfil apenas demográfico",
    "A leitura dos registos mostra respostas distintas consoante o detalhe da entrada. Nos perfis adultos, os valores sugeridos permaneceram dentro dos intervalos usados pelo sistema. No perfil infantil, os comprimentos e os parâmetros das articulações flexíveis foram reduzidos. Este comportamento corresponde às instruções presentes nas legendas do esquema; não constitui demonstração de ajuste anatómico. No perfil adolescente, uma regra preliminar assinalou a palma como excessiva. A comparação posterior com o intervalo de referência usado no ensaio mostrou que o limite do teste era demasiado rígido. A regra foi corrigida, mas a ausência de uma medição individual impede classificar a sugestão como exacta.":
        "A leitura dos registos mostra respostas distintas consoante o detalhe da descrição submetida. Nos perfis adultos, os valores sugeridos permaneceram dentro dos intervalos usados pelo sistema. No perfil infantil, os comprimentos e os parâmetros das articulações flexíveis foram reduzidos. Este comportamento corresponde às instruções presentes nas legendas do esquema; não constitui demonstração de ajuste anatómico. No perfil adolescente, uma regra preliminar assinalou a palma como excessiva. A comparação posterior com o intervalo de referência usado no ensaio mostrou que o limite do teste era demasiado rígido. A regra foi corrigida, mas a ausência de uma medição individual impede classificar a sugestão como exacta.",
    "Entradas completas": "Descrições com medições completas",
    "A IA preservou os valores directamente declarados pelo utilizador":
        "Na resposta arquivada, a IA preservou os valores directamente declarados",
    "Entradas parciais": "Descrições com uma medição directa",
    "O sistema combinou dados explícitos com referências populacionais":
        "Na resposta arquivada, o sistema combinou o dado explícito com referências populacionais",
    "Entradas apenas demográficas": "Descrições apenas demográficas",
    "O fluxo gerou um ponto de partida que requer confirmação por medição ou por um profissional competente":
        "Nos casos examinados, o fluxo gerou um ponto de partida que requer confirmação por medição ou por um profissional competente",
    "A bateria complementar reuniu 15 cenários com descrições vagas, comparativas, multilingues, sem medidas ou com valores fora dos limites. Os ficheiros preservam as entradas e as respostas, mas o estudo não reuniu extracções suficientes para estimar estatisticamente a estabilidade do modelo de linguagem. Em algumas execuções, parâmetros de hardware foram incluídos; noutras, permaneceram nos valores correntes. Assim, a conclusão limita-se à conformidade dos casos registados e ao valor das salvaguardas determinísticas. Entradas equivalentes podem originar números ou conjuntos de campos diferentes, pelo que cada sugestão exige revisão antes de ser aplicada.":
        "A bateria complementar reuniu 15 cenários com descrições vagas, comparativas, multilingues, sem medidas ou com valores fora dos limites. Os registos preservam as descrições submetidas e as respostas, mas o estudo não reuniu extracções suficientes para estimar estatisticamente a estabilidade do modelo de linguagem. Em algumas execuções, parâmetros de hardware foram incluídos; noutras, permaneceram nos valores correntes. Assim, a conclusão limita-se à conformidade dos casos registados e ao valor das salvaguardas determinísticas. Descrições equivalentes podem originar números ou conjuntos de campos diferentes, pelo que cada sugestão exige revisão antes de ser aplicada.",
    "A primeira prioridade experimental futura deve alargar os ensaios da IA. Cada cenário deve ser executado várias vezes, com registo do modelo, parâmetros de geração, resposta completa, erros, campos omitidos e taxa de cumprimento de cada regra. A interface deve mostrar a fonte populacional usada, os dados em falta e avisos quando a dimensão estimada fica fora da gama do modelo escolhido. A validação do esquema JSON deve ocorrer no servidor antes de a sugestão chegar à interface.":
        "Uma eventual extensão orientada para a estabilidade do modelo de linguagem poderá executar cada cenário várias vezes, com registo do modelo, dos parâmetros de geração, da resposta completa, dos erros, dos campos omitidos e da taxa de cumprimento de cada regra. Esta extensão permitiria caracterizar a dispersão entre chamadas, mas não é necessária para as conclusões delimitadas apresentadas nesta dissertação. Independentemente dessa campanha, a interface deverá mostrar a fonte populacional usada, os dados em falta e avisos quando a dimensão estimada fica fora da gama do modelo escolhido. A validação do esquema JSON deverá ocorrer no servidor antes de a sugestão chegar à interface.",
    "Limites equivalentes devem actuar em todas as entradas que conduzem à mesma transformação":
        "Limites equivalentes devem actuar em todos os percursos que conduzem à mesma transformação",
}


EXPLANATION_ANCHOR = (
    "O funcionamento básico da maioria dos sistemas actuais de IA pode ser explicado em quatro etapas: "
    "dados, treino, inferência e, em certos casos, geração. Em primeiro lugar, o sistema necessita de "
    "dados de entrada, isto é, exemplos a partir dos quais possa aprender padrões. Em segundo lugar, "
    "durante o treino, o modelo ajusta os seus parâmetros internos para captar padrões recorrentes nos "
    "dados. Em terceiro lugar, após o treino, o modelo passa a realizar inferência, produzindo previsões, "
    "classificações, recomendações ou respostas a novos casos. Em modelos generativos, há ainda um quarto "
    "momento: a produção de novos conteúdos compatíveis com os padrões aprendidos, em vez de simples "
    "classificação ou previsão (Ao et al., 2025; Menaka et al., 2025; Panchal et al., 2019)."
)

EXPLANATION = (
    "Nos modelos de linguagem, o texto é processado em unidades designadas por tokens. Um token pode "
    "corresponder a uma palavra completa, a parte de uma palavra, a um número ou a um sinal de pontuação. "
    "O limite de tokens define a extensão máxima da resposta que o modelo pode produzir, não a sua qualidade "
    "ou exactidão. A temperatura é um parâmetro de geração que condiciona a distribuição usada na escolha de "
    "cada unidade seguinte: valores mais baixos concentram a selecção nas alternativas mais prováveis e tendem "
    "a reduzir a variação, enquanto valores mais elevados admitem alternativas menos prováveis e tendem a "
    "produzir respostas mais diversas. A temperatura não representa confiança, qualidade ou precisão, e o "
    "valor zero não garante, por si só, respostas integralmente idênticas."
)


def apply(path: Path) -> tuple[int, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])
    paragraphs = document.xpath("//w:p", namespaces=NS)
    changed = 0

    for old, new in REPLACEMENTS.items():
        matches = [paragraph for paragraph in paragraphs if paragraph_text(paragraph) == old]
        completed = [paragraph for paragraph in paragraphs if paragraph_text(paragraph) == new]
        if len(matches) == 1:
            set_paragraph_text(matches[0], new)
            changed += 1
        elif not matches and len(completed) == 1:
            continue
        else:
            raise RuntimeError(
                f"{path.name}: esperado um parágrafo antigo ou novo para {old[:90]!r}; "
                f"encontrados {len(matches)} antigos e {len(completed)} novos"
            )

    index_old = "Entradas utilizadas nos cenários de avaliação da IA"
    index_new = "Descrições submetidas nos cenários de avaliação da IA"
    index_nodes = [
        node
        for node in document.xpath("//w:t", namespaces=NS)
        if node.text and index_old in node.text
    ]
    if len(index_nodes) == 1:
        index_nodes[0].text = index_nodes[0].text.replace(index_old, index_new)
        changed += 1
    elif not index_nodes:
        completed_nodes = [
            node
            for node in document.xpath("//w:t", namespaces=NS)
            if node.text and index_new in node.text
        ]
        if len(completed_nodes) != 2:
            raise RuntimeError(
                f"Entrada do índice da Tabela 8.4 encontrada {len(completed_nodes)} vezes"
            )
    else:
        raise RuntimeError(f"Entrada antiga do índice da Tabela 8.4 encontrada {len(index_nodes)} vezes")

    paragraphs = document.xpath("//w:p", namespaces=NS)
    explanations = [p for p in paragraphs if paragraph_text(p) == EXPLANATION]
    if not explanations:
        anchors = [p for p in paragraphs if paragraph_text(p) == EXPLANATION_ANCHOR]
        if len(anchors) != 1:
            raise RuntimeError(f"Âncora da explicação encontrada {len(anchors)} vezes")
        inserted = deepcopy(anchors[0])
        set_paragraph_text(inserted, EXPLANATION)
        anchors[0].addnext(inserted)
        changed += 1
    elif len(explanations) != 1:
        raise RuntimeError(f"Explicação encontrada {len(explanations)} vezes")

    paragraphs = document.xpath("//w:p", namespaces=NS)
    versions = [p for p in paragraphs if paragraph_text(p).startswith("Versão do documento:")]
    if len(versions) > 1:
        raise RuntimeError(f"Linha de versão encontrada {len(versions)} vezes")
    if versions and paragraph_text(versions[0]) != "Versão do documento: 0.4.53":
        set_paragraph_text(versions[0], "Versão do documento: 0.4.53")
        changed += 1

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for item in items:
                output.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return changed, len(REPLACEMENTS)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    path = root / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
    changed, expected = apply(path)
    print(f"DOCX actualizado: {changed} alterações; {expected} substituições verificadas")
