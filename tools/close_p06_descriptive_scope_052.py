#!/usr/bin/env python3
"""Fecha a P06 no âmbito descritivo e actualiza os DOCX da versão 0.4.52."""

from __future__ import annotations

import os
import tempfile
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


ROOT_REPLACEMENTS = {
    "Eficácia protésica, usabilidade com participantes, durabilidade, ensaios mecânicos, repetição metrológica e montagem funcional completa":
        "Eficácia protésica, usabilidade com participantes, durabilidade, ensaios mecânicos, estimativa da incerteza de medição e montagem funcional completa",
    "O registo dimensional reúne um valor por eixo e por palma, obtido com paquímetro nas extensões X, Y e Z, à temperatura ambiente. Este conjunto permite calcular o desvio entre a malha e a peça, mas não a média, a amplitude entre repetições ou a incerteza associada ao reposicionamento do instrumento. O protocolo de três leituras independentes mantém-se como procedimento futuro de confirmação metrológica. O protocolo de montagem prevê o registo da compatibilidade entre componentes e, apenas nos protótipos integralmente montados, cinco ciclos de articulação, observação de colisões, fecho e retorno; estes resultados permanecem por recolher e não podem ser usados para afirmar adequação anatómica ou funcional.":
        "O registo dimensional reúne um valor por eixo e por palma, obtido com paquímetro nas extensões X, Y e Z, à temperatura ambiente. Este conjunto permite calcular o desvio entre a malha e a peça, mas não a média, a amplitude entre repetições ou a incerteza associada ao reposicionamento do instrumento. A comparação é, por isso, assumida como descritiva. Três leituras independentes apenas seriam necessárias numa futura caracterização metrológica da dispersão e da incerteza, que não integra o âmbito deste estudo. A montagem sistemática também ficou fora da avaliação; consequentemente, os resultados não são usados para afirmar adequação anatómica ou funcional.",
    "Esta distinção permite interpretar os resultados em três níveis. Foi demonstrada tecnicamente a capacidade de configurar dimensões, controlar parâmetros, gerar e exportar geometrias e preparar variantes para fabrico. A materialização das peças foi observada e as dimensões X, Y e Z das palmas foram comparadas com as malhas, permanecendo a confirmação por leituras repetidas, a montagem e a articulação dependentes dos protocolos próprios. Conforto, usabilidade com participantes, adequação funcional em utilização, aceitação, dignidade e autonomia constituem efeitos projectuais potenciais, sustentados como relevantes pela literatura, mas ainda não confirmados junto de utilizadores.":
        "Esta distinção permite interpretar os resultados em três níveis. Foi demonstrada tecnicamente a capacidade de configurar dimensões, controlar parâmetros, gerar e exportar geometrias e preparar variantes para fabrico. A materialização das peças foi observada e as dimensões X, Y e Z das palmas foram comparadas com as malhas. Como existe uma leitura por eixo e peça, a interpretação dimensional permanece descritiva e não inclui estimativa da incerteza; montagem e articulação também ficaram fora do âmbito avaliado. Conforto, usabilidade com participantes, adequação funcional em utilização, aceitação, dignidade e autonomia constituem efeitos projectuais potenciais, sustentados como relevantes pela literatura, mas ainda não confirmados junto de utilizadores.",
    "Quanto à segunda pergunta aprovada, a combinação de ciclos de Research Through Design, ensaios unitários, cenários simulados, inspecção de respostas JSON, medição de malhas, exportação, preparação para impressão, observação e medição de peças físicas permitiu avaliar parcialmente a coerência e a repetição técnica de diferentes etapas. A Série B acrescentou uma comparação digital sob condição comum; a análise dimensional reuniu 36 extensões X/Y/Z das malhas e 72 medições das palmas em PLA e PETG. Estes métodos não avaliaram eficácia protésica, usabilidade com participantes ou durabilidade. A repetição controlada das medições, a montagem completa e os ensaios de utilização permanecem por executar.":
        "Quanto à segunda pergunta aprovada, a combinação de ciclos de Research Through Design, ensaios unitários, cenários simulados, inspecção de respostas JSON, medição de malhas, exportação, preparação para impressão, observação e medição de peças físicas permitiu avaliar parcialmente a coerência e a repetição técnica de diferentes etapas. A Série B acrescentou uma comparação digital sob condição comum; a análise dimensional reuniu 36 extensões X/Y/Z das malhas e 72 medições das palmas em PLA e PETG. Estes métodos não avaliaram eficácia protésica, usabilidade com participantes ou durabilidade. A comparação dimensional permanece descritiva e não estima a incerteza de medição; montagem completa e ensaios de utilização ficaram igualmente fora do âmbito avaliado.",
    "Coerência do percurso, repetição técnica, preparação digital e comparação dimensional entre malhas e palmas em PLA e PETG":
        "Coerência do percurso, repetição técnica, preparação digital e comparação dimensional descritiva entre malhas e palmas em PLA e PETG",
    "Eficácia protésica, usabilidade com participantes, resistência, desgaste e durabilidade":
        "Eficácia protésica, usabilidade com participantes, resistência, desgaste, durabilidade e incerteza de medição",
    "Repetição metrológica, montagem, ensaios mecânicos delimitados e avaliação com participantes":
        "Montagem, ensaios mecânicos delimitados e avaliação com participantes",
    "A primeira etapa futura deve confirmar a comparação dimensional já realizada. As medidas de entrada, as extensões X/Y/Z das malhas e um valor físico por eixo para as palmas em PLA e PETG encontram-se registados no Anexo D. Deve repetir-se a medição com três leituras independentes por eixo, reposicionando o paquímetro entre leituras, para calcular média, amplitude e incerteza associada ao procedimento. Estes pontos são extremos geométricos reproduzíveis e não devem ser apresentados como pontos anatómicos sem demonstração da sua equivalência.":
        "Uma eventual extensão metrológica poderá aprofundar a comparação dimensional já realizada. As medidas de entrada, as extensões X/Y/Z das malhas e um valor físico por eixo para as palmas em PLA e PETG encontram-se registados no Anexo D. Caso um estudo futuro pretenda calcular média, amplitude e incerteza associada ao reposicionamento do paquímetro, deverá efectuar três leituras independentes por eixo. Esta extensão é opcional e não é necessária para a comparação descritiva nem para as conclusões apresentadas nesta dissertação. Os pontos usados correspondem a extremos geométricos e não são apresentados como pontos anatómicos sem demonstração da sua equivalência.",
    "Como existe apenas um valor registado por eixo e por peça, não são calculadas a média entre repetições, a amplitude ou a incerteza de medição. A repetição com reposicionamento do paquímetro permanece necessária para caracterizar essas componentes metrológicas.":
        "Como existe apenas um valor registado por eixo e por peça, não são calculadas a média entre repetições, a amplitude ou a incerteza de medição. Esta limitação é assumida na interpretação descritiva. Uma eventual caracterização metrológica futura exigiria o reposicionamento do paquímetro e leituras independentes, mas não é necessária para a comparação apresentada nesta dissertação.",
    "O fatiamento converte a geometria numa sequência de camadas e trajectórias de deposição, definindo altura de camada, paredes, enchimento, suportes, temperaturas e orientação. A Série A constitui uma verificação técnica complementar da fase empírica aprovada e documenta quatro projectos tal como foram preparados: três projectos Bambu Lab A1, processados no Bambu Studio 01.10.02.76 — Flexy Beast em PLA e UnLimbited Phoenix em PLA e PETG —, e um projecto Paraglider Hand para Prusa MINI, processado no PrusaSlicer 2.8.1. Os projectos Bambu usam camada de 0,24 mm, duas paredes, enchimento de 15% em grelha e suporte em árvore orgânica; o projecto Prusa usa camada de 0,20 mm, dois perímetros, enchimento de 15% e suporte desactivado. Como geometria, programa, impressora, material e condições não são equivalentes, esta série descreve cada preparação e não permite comparar desempenho entre equipamentos ou materiais.":
        "A preparação para impressão converte a geometria numa sequência de camadas e trajectórias de deposição, definindo altura de camada, paredes, enchimento, suportes, temperaturas e orientação. A Série A constitui uma verificação técnica complementar da fase empírica aprovada e documenta quatro projectos tal como foram preparados: três projectos Bambu Lab A1, processados no Bambu Studio 01.10.02.76 — Flexy Beast em PLA e UnLimbited Phoenix em PLA e PETG —, e um projecto Paraglider Hand para Prusa MINI, processado no PrusaSlicer 2.8.1. Os projectos Bambu usam camada de 0,24 mm, duas paredes, enchimento de 15% em grelha e suporte em árvore orgânica; o projecto Prusa usa camada de 0,20 mm, dois perímetros, enchimento de 15% e suporte desactivado. Como geometria, programa, impressora, material e condições não são equivalentes, esta série descreve cada preparação e não permite comparar desempenho entre equipamentos ou materiais.",
    "A utilização da Bambu Lab A1 e da Prusa MINI documenta a execução do fluxo em dois ambientes de fabrico, mas não constitui uma comparação entre equipamentos. Os modelos, os programas de fatiamento e parte das definições de preparação diferem entre os projectos, e nenhuma geometria equivalente foi repetida nas duas impressoras sob condições controladas. Não é, por isso, possível isolar o efeito da impressora, comparar qualidade ou velocidade, nem concluir que o fluxo exige dois equipamentos.":
        "A utilização da Bambu Lab A1 e da Prusa MINI documenta a execução do fluxo em dois ambientes de fabrico, mas não constitui uma comparação entre equipamentos. Os modelos, os programas de preparação para impressão e parte das definições usadas diferem entre os projectos, e nenhuma geometria equivalente foi repetida nas duas impressoras sob condições controladas. Não é, por isso, possível isolar o efeito da impressora, comparar qualidade ou velocidade, nem concluir que o fluxo exige dois equipamentos.",
    "Uma inspecção complementar com trimesh, arquivada com os cenários de 29 de Junho de 2026, examinou peças da configuração infantil. Os critérios foram fecho da superfície, carácter múltiplo da geometria, número de corpos e faces de área nula. A Tabela 8.3 mostra que a preparação aceite pelo programa de fatiamento não implica que a malha de origem seja um sólido fechado sem defeitos.":
        "Uma inspecção complementar com trimesh, arquivada com os cenários de 29 de Junho de 2026, examinou peças da configuração infantil. Os critérios foram fecho da superfície, carácter múltiplo da geometria, número de corpos e faces de área nula. A Tabela 8.3 mostra que a preparação aceite pelo programa não implica que a malha de origem seja um sólido fechado sem defeitos.",
    "O fatiamento pode aceitar a peça, mas a malha contém faces degeneradas":
        "A preparação pode aceitar a peça, mas a malha contém faces degeneradas",
    "O contributo metodológico é a documentação dos ciclos de Research Through Design que ligam situação, artefacto, ensaio, resultado e alteração. A passagem sucessiva pela resposta numérica, geometria exportada, projecto de fatiamento e peça física revelou falhas que ficariam ocultas num único nível de análise.":
        "O contributo metodológico é a documentação dos ciclos de Research Through Design que ligam situação, artefacto, ensaio, resultado e alteração. A passagem sucessiva pela resposta numérica, geometria exportada, projecto de preparação para impressão e peça física revelou falhas que ficariam ocultas num único nível de análise.",
    "A segunda etapa deve alargar os ensaios da IA. Cada cenário deve ser executado várias vezes, com registo do modelo, parâmetros de geração, resposta completa, erros, campos omitidos e taxa de cumprimento de cada regra. A interface deve mostrar a fonte populacional usada, os dados em falta e avisos quando a dimensão estimada fica fora da gama do modelo escolhido. A validação do esquema JSON deve ocorrer no servidor antes de a sugestão chegar à interface.":
        "A primeira prioridade experimental futura deve alargar os ensaios da IA. Cada cenário deve ser executado várias vezes, com registo do modelo, parâmetros de geração, resposta completa, erros, campos omitidos e taxa de cumprimento de cada regra. A interface deve mostrar a fonte populacional usada, os dados em falta e avisos quando a dimensão estimada fica fora da gama do modelo escolhido. A validação do esquema JSON deve ocorrer no servidor antes de a sugestão chegar à interface.",
    "A terceira etapa deve executar separadamente os protocolos de montagem e os ensaios mecânicos futuros. A folha do Anexo D permite começar pela compatibilidade dos componentes, colisões e cinco ciclos de articulação nos protótipos completos. Comparações de materiais e impressoras exigem corpos de prova ou componentes equivalentes, condições controladas e medições próprias; carga, fadiga e desgaste requerem procedimentos adequados ao uso previsto. No Flexy Beast, esta etapa deve incluir a produção e caracterização das juntas em filamento flexível ou silicone, bem como a verificação do retorno dos dedos e da aderência das almofadas previstas no modelo original. Só depois desta caracterização deve avançar uma avaliação com participantes e profissionais, mediante enquadramento ético e clínico apropriado.":
        "Uma segunda linha de trabalho futuro deve executar separadamente os protocolos de montagem e os ensaios mecânicos. A folha do Anexo D permite começar pela compatibilidade dos componentes, colisões e cinco ciclos de articulação nos protótipos completos. Comparações de materiais e impressoras exigem corpos de prova ou componentes equivalentes, condições controladas e medições próprias; carga, fadiga e desgaste requerem procedimentos adequados ao uso previsto. No Flexy Beast, esta etapa deve incluir a produção e caracterização das juntas em filamento flexível ou silicone, bem como a verificação do retorno dos dedos e da aderência das almofadas previstas no modelo original. Só depois desta caracterização deve avançar uma avaliação com participantes e profissionais, mediante enquadramento ético e clínico apropriado.",
    "A quarta etapa deve estudar a interface com os grupos de utilizadores previstos. As tarefas, erros, tempo, compreensão das sugestões, confiança e distribuição de responsabilidade devem ser avaliados com pessoas amputadas, designers, técnicos e profissionais de saúde. Esta etapa permitirá verificar se o fluxo facilita a configuração e se os avisos e controlos apoiam decisões informadas.":
        "Uma terceira linha de trabalho futuro deve estudar a interface com os grupos de utilizadores previstos. As tarefas, erros, tempo, compreensão das sugestões, confiança e distribuição de responsabilidade devem ser avaliados com pessoas amputadas, designers, técnicos e profissionais de saúde. Esta etapa permitirá verificar se o fluxo facilita a configuração e se os avisos e controlos apoiam decisões informadas.",
}


ANNEX_REPLACEMENTS = {
    key: value
    for key, value in ROOT_REPLACEMENTS.items()
    if key.startswith("Como existe apenas um valor")
}
ANNEX_REPLACEMENTS.update(
    {
        "As imagens seguintes documentam impressões físicas reais dos modelos, obtidas na impressora Bambu Lab A1. Complementam as estimativas digitais das secções anteriores como evidência visual e qualitativa da preparação e do fabrico: mostram que os ficheiros gerados pela plataforma foram impressos, montados e articulados. As imagens não acrescentam medições quantitativas. As dimensões X, Y e Z apresentadas em D.4.4 foram obtidas por medição directa das palmas; a repetição metrológica e a verificação sistemática da montagem seguem os protocolos próprios e permanecem por executar.":
            "As imagens seguintes documentam impressões físicas reais dos modelos, obtidas na impressora Bambu Lab A1. Complementam as estimativas digitais das secções anteriores como evidência visual e qualitativa da preparação e do fabrico: mostram que os ficheiros gerados pela plataforma foram impressos, montados e articulados. As imagens não acrescentam medições quantitativas. As dimensões X, Y e Z apresentadas em D.4.4 foram obtidas por medição directa das palmas. Uma caracterização metrológica com leituras independentes e a verificação sistemática da montagem constituem extensões possíveis, mas não integram o âmbito descritivo adoptado nesta dissertação."
    }
)


def rewrite(path: Path, replacements: dict[str, str], update_version: bool = False) -> int:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])
    paragraphs = document.xpath("//w:p", namespaces=NS)
    changed = 0

    for old, new in replacements.items():
        matches = [paragraph for paragraph in paragraphs if paragraph_text(paragraph) == old]
        if len(matches) == 1:
            set_paragraph_text(matches[0], new)
            changed += 1
            continue
        completed = [paragraph for paragraph in paragraphs if paragraph_text(paragraph) == new]
        if not matches and len(completed) == 1:
            continue
        if len(matches) != 1:
            raise RuntimeError(
                f"{path.name}: esperado um parágrafo antigo ou novo para {old[:80]!r}; "
                f"encontrados {len(matches)} antigos e {len(completed)} novos"
            )

    if update_version:
        matches = [
            paragraph
            for paragraph in paragraphs
            if paragraph_text(paragraph).startswith("Versão do documento:")
        ]
        if len(matches) > 1:
            raise RuntimeError(
                f"{path.name}: esperada no máximo uma linha de versão; encontradas {len(matches)}"
            )
        if matches:
            set_paragraph_text(matches[0], "Versão do documento: 0.4.52")
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

    return changed


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    canonical = root / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
    annex = (
        root
        / "sources/manuscript/annexes/testes_preparacao_impressao"
        / "anexo_d_preparacao_impressao.docx"
    )
    print(f"DOCX canónico: {rewrite(canonical, ROOT_REPLACEMENTS, update_version=True)} alterações")
    print(f"DOCX do Anexo D: {rewrite(annex, ANNEX_REPLACEMENTS)} alterações")


if __name__ == "__main__":
    main()
