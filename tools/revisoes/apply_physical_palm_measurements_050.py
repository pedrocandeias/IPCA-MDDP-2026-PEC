#!/usr/bin/env python3
"""Integra no DOCX canónico as medições físicas das palmas em PLA e PETG."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_approved_questions_annex_d import import_fragment, replace_range
from integrate_annexes_bc import (
    NS,
    W,
    element_text,
    paragraph_style,
    qn,
    replace_paragraph_text,
)


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
VERSION = "0.4.50"

FRAGMENTS = (
    (
        "### 3.3 Estrutura metodológica do projecto",
        "### 3.4 Métodos de recolha e análise de dados",
        "3.3 Estrutura metodológica do projecto",
        "3.4 Métodos de recolha e análise de dados",
        "050_metodologia_33",
    ),
    (
        "### 8.4 Discussão dos resultados face aos objectivos",
        "## Capítulo 9 — Conclusões e Trabalhos Futuros",
        "8.4 Discussão dos resultados face aos objectivos",
        "Capítulo 9 — Conclusões e Trabalhos Futuros",
        "050_discussao_84",
    ),
    (
        "## Capítulo 9 — Conclusões e Trabalhos Futuros",
        "## Bibliografia",
        "Capítulo 9 — Conclusões e Trabalhos Futuros",
        "Referências Bibliográficas",
        "050_capitulo_9",
    ),
    (
        "## D.1 Finalidade",
        "## D.3 Variáveis, controlos e materiais",
        "D.1 Finalidade",
        "D.3 Variáveis, controlos e materiais",
        "050_anexo_d_1_2",
    ),
    (
        "### D.4.4 Comparação entre entrada, malha e peça física",
        "### D.4.5 Registo fotográfico dos protótipos",
        "D.4.4 Comparação entre entrada, malha e peça física",
        "D.4.5 Registo fotográfico dos protótipos",
        "050_anexo_d_44",
    ),
)

END_FRAGMENT = (
    "## D.6 Limites de comparabilidade",
    "## D.9 Registo fotográfico dos protótipos impressos",
    "D.6 Limites de comparabilidade",
    "050_anexo_d_6_8",
)

PARAGRAPH_REPLACEMENTS = (
    (
        "A análise dimensional digital incidiu nas palmas isoladas dos mesmos doze casos. Foram extraídas 36 extensões exteriores — X, Y e Z — a partir das malhas 3MF. Estes valores descrevem a caixa envolvente da peça. Não são automaticamente equivalentes a larguras, comprimentos ou espessuras anatómicas, porque as geometrias podem incluir abas, interfaces e margens de montagem. O desvio dimensional é, por isso, reservado à comparação futura entre a malha e a peça física medidas no mesmo referencial, e não à diferença directa entre parâmetro antropométrico e caixa exterior.",
        "A análise dimensional incidiu nas palmas isoladas dos mesmos doze casos. Foram extraídas 36 extensões exteriores — X, Y e Z — a partir das malhas 3MF. Estes valores descrevem a caixa envolvente da peça. Não são automaticamente equivalentes a larguras, comprimentos ou espessuras anatómicas, porque as geometrias podem incluir abas, interfaces e margens de montagem. As mesmas extensões foram medidas nas palmas produzidas em PLA e PETG, à temperatura ambiente, num total de 72 valores físicos. O desvio dimensional foi calculado entre cada valor físico e a extensão correspondente da malha, no mesmo referencial, e não entre o parâmetro antropométrico e a caixa exterior.",
    ),
    (
        "A materialização recorreu a uma Bambu Lab A1 com sistema AMS e a uma Prusa MINI, ambas baseadas em fabrico por filamento fundido. As fotografias confirmam a existência das peças e permitem observar diferenças de escala entre os perfis. Os diagnósticos dos programas e a inspecção geométrica independente usam critérios diferentes e foram conservados separadamente: a aceitação pelo programa de preparação não implica uma malha fechada e sem faces degeneradas. Sem medições físicas sistemáticas, ensaios de carga ou registos completos de montagem, esta evidência sustenta a produção observacional das peças mostradas; não sustenta precisão dimensional, resistência, conforto, segurança ou durabilidade.",
        "A materialização recorreu a uma Bambu Lab A1 com sistema AMS e a uma Prusa MINI, ambas baseadas em fabrico por filamento fundido. As fotografias confirmam a existência das peças e permitem observar diferenças de escala entre os perfis. Os diagnósticos dos programas e a inspecção geométrica independente usam critérios diferentes e foram conservados separadamente: a aceitação pelo programa de preparação não implica uma malha fechada e sem faces degeneradas. As medições físicas sustentam a comparação dimensional das palmas nos eixos X, Y e Z. Porém, a ausência de leituras repetidas, ensaios de carga e registos completos de montagem impede estimar a incerteza de medição e não permite inferir resistência, conforto, segurança ou durabilidade.",
    ),
    (
        "Foram preparados dois protocolos físicos para execução posterior. O primeiro prevê três leituras independentes com paquímetro nas extensões X, Y e Z de cada palma, com cálculo da média, amplitude e desvio entre malha e peça. O segundo prevê o registo da compatibilidade entre componentes e, apenas nos protótipos integralmente montados, cinco ciclos de articulação, observação de colisões, fecho e retorno. Enquanto as folhas permanecerem sem valores, estes procedimentos não integram os resultados e não podem ser usados para afirmar adequação anatómica ou funcional.",
        "O registo dimensional reúne um valor por eixo e por palma, obtido com paquímetro nas extensões X, Y e Z, à temperatura ambiente. Este conjunto permite calcular o desvio entre a malha e a peça, mas não a média, a amplitude entre repetições ou a incerteza associada ao reposicionamento do instrumento. O protocolo de três leituras independentes mantém-se como procedimento futuro de confirmação metrológica. O protocolo de montagem prevê o registo da compatibilidade entre componentes e, apenas nos protótipos integralmente montados, cinco ciclos de articulação, observação de colisões, fecho e retorno; estes resultados permanecem por recolher e não podem ser usados para afirmar adequação anatómica ou funcional.",
    ),
    (
        "As limitações principais são a ausência de participantes, dados clínicos, medições directas da mão, medições dimensionais sistemáticas das peças, ensaios biomecânicos, protocolos normalizados de resistência, montagem funcional completa, estudo longitudinal de desgaste e avaliação de usabilidade. Os dados populacionais apresentam diferenças de população, idade, sexo, lateralidade e método de medição. Os casos simulados representam situações de teste e não pessoas. A plataforma é um protótipo de investigação em staging, sem certificação como dispositivo médico e sem prontidão demonstrada para utilização clínica ou doméstica. Estas limitações delimitam a força das conclusões, sem invalidar o estudo técnico que foi efectivamente realizado.",
        "As limitações principais são a ausência de participantes, dados clínicos, medições directas da mão, repetições controladas das medições dimensionais, ensaios biomecânicos, protocolos normalizados de resistência, montagem funcional completa, estudo longitudinal de desgaste e avaliação de usabilidade. Os dados populacionais apresentam diferenças de população, idade, sexo, lateralidade e método de medição. Os casos simulados representam situações de teste e não pessoas. A plataforma é um protótipo de investigação em staging, sem certificação como dispositivo médico e sem prontidão demonstrada para utilização clínica ou doméstica. Estas limitações delimitam a força das conclusões, sem invalidar o estudo técnico que foi efectivamente realizado.",
    ),
    (
        "A comparação dimensional digital reuniu 36 extensões X, Y e Z das palmas exportadas. No Phoenix, a largura de entrada e a extensão X da malha ficaram próximas; no Flexy Beast e no Paraglider, a extensão exterior inclui interfaces e margens decorrentes da geometria-base. Por isso, a diferença entre parâmetro e caixa exterior descreve a transformação projectual e não é tratada como erro. O Anexo D apresenta os valores completos, a compatibilidade delimitada com as orientações de escala e as folhas ainda vazias para medição física e montagem.",
        "A comparação dimensional reuniu 36 extensões X, Y e Z das palmas exportadas e 72 valores medidos nas peças correspondentes, metade em PLA e metade em PETG. No Phoenix, a largura de entrada e a extensão X da malha ficaram próximas; no Flexy Beast e no Paraglider, a extensão exterior inclui interfaces e margens decorrentes da geometria-base. Por isso, a diferença entre parâmetro e caixa exterior descreve a transformação projectual e não é tratada como erro. Nas peças físicas, todos os valores ficaram abaixo das extensões das malhas: os desvios percentuais variaram entre −0,321% e −0,274% em PLA e entre −0,425% e −0,369% em PETG. O Anexo D apresenta os resultados completos e a compatibilidade delimitada com as orientações de escala. Como existe uma única leitura registada por eixo, os resultados não permitem quantificar a dispersão ou a incerteza de medição.",
    ),
    (
        "Foram produzidos exemplares em PLA e PETG, e os projectos preservados identificam o material atribuído às peças preparadas. No caso da UnLimbited Phoenix, o projecto PETG atribui os oito conjuntos de peças ao perfil Bambu PETG Basic. Esta evidência documenta duas condições de produção, mas não constitui uma comparação controlada entre materiais, porque não foram definidos corpos de prova equivalentes, repetições, medições dimensionais ou ensaios mecânicos comparáveis. Não se retiram, portanto, conclusões sobre resistência, fragilidade ou durabilidade relativas de PLA e PETG.",
        "Foram produzidos exemplares em PLA e PETG, e as configurações analisadas identificam o material atribuído às peças preparadas. No caso da UnLimbited Phoenix, a configuração PETG atribui os oito conjuntos de peças ao perfil Bambu PETG Basic. As medições permitem uma comparação dimensional emparelhada das palmas produzidas nos dois materiais: nos exemplares registados, o PETG apresentou desvios negativos ligeiramente superiores aos do PLA. Como não existem leituras repetidas nem uma série experimental destinada a isolar o efeito do material, esta diferença não deve ser generalizada como taxa própria de contracção. Também não se retiram conclusões sobre resistência, fragilidade ou durabilidade relativas de PLA e PETG sem ensaios mecânicos comparáveis.",
    ),
    (
        "Este registo confirma a existência material dos componentes fotografados e permite observar diferenças de escala, estados de montagem e relações visuais entre peças. Como não inclui escala métrica comum, pontos de medição assinalados, repetições controladas ou aplicação de carga, não é usado para calcular desvios dimensionais nem para inferir resistência, conforto, adequação anatómica ou desempenho funcional. A medição física mantém-se dependente do protocolo definido na Secção D.4.4.",
        "Este registo confirma a existência material dos componentes fotografados e permite observar diferenças de escala, estados de montagem e relações visuais entre peças. Como não inclui escala métrica comum, pontos de medição assinalados, repetições controladas ou aplicação de carga, as fotografias não são usadas para calcular os desvios dimensionais nem para inferir resistência, conforto, adequação anatómica ou desempenho funcional. Os desvios apresentados na Secção D.4.4 resultam dos valores medidos nas peças, e não da interpretação das imagens.",
    ),
)


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}"
        )
    return matches[0]


def replace_exact_paragraphs(document: etree._Element) -> int:
    changed = 0
    for old, new in PARAGRAPH_REPLACEMENTS:
        paragraph = find_body_paragraph(document, old)
        replace_paragraph_text(paragraph, new)
        changed += 1
    return changed


def replace_to_body_end(
    document: etree._Element,
    start: etree._Element,
    replacements: list[etree._Element],
) -> None:
    body = document.find(".//w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("O corpo do documento não foi localizado")
    section_properties = body.find("w:sectPr", namespaces=NS)
    if section_properties is None:
        raise RuntimeError("As propriedades finais de secção não foram localizadas")
    current = start
    while current is not None and current is not section_properties:
        following = current.getnext()
        body.remove(current)
        current = following
    if current is None:
        raise RuntimeError("O fim do corpo não sucede ao início do Anexo D")
    for element in replacements:
        section_properties.addprevious(element)


def update_version(document: etree._Element) -> int:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph).startswith("Versão do documento:")
    ]
    if not matches:
        return 0
    if len(matches) != 1:
        raise RuntimeError(f"Esperada uma linha de versão; encontradas {len(matches)}")
    replace_paragraph_text(matches[0], f"Versão do documento: {VERSION}")
    return 1


def update_table_index_entry(document: etree._Element) -> int:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph).startswith("ndice")
        and element_text(paragraph).startswith("Tabela D.3")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperada uma entrada de índice para a Tabela D.3; encontradas {len(matches)}"
        )
    text_nodes = matches[0].xpath(".//w:t", namespaces=NS)
    if len(text_nodes) < 2:
        raise RuntimeError("A entrada da Tabela D.3 não conserva título e página separados")
    text_nodes[0].text = (
        "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG"
    )
    return 1


def keep_table_caption_with_table(document: etree._Element) -> int:
    caption = find_body_paragraph(
        document,
        "Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG",
    )
    properties = caption.find(qn(W, "pPr"))
    if properties is None:
        properties = etree.Element(qn(W, "pPr"))
        caption.insert(0, properties)
    if properties.find(qn(W, "keepNext")) is None:
        properties.append(etree.Element(qn(W, "keepNext")))
        return 1
    return 0


def write_package(path: Path, files: dict[str, bytes], original_mode: int) -> None:
    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


def apply(path: Path) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    imported = 0
    for md_start, md_end, docx_start, docx_end, label in FRAGMENTS:
        elements = import_fragment(
            markdown,
            md_start,
            md_end,
            label,
            document,
            relationships,
            files,
        )
        replace_range(
            find_body_paragraph(document, docx_start),
            find_body_paragraph(document, docx_end),
            elements,
        )
        imported += len(elements)

    md_start, md_end, docx_start, label = END_FRAGMENT
    end_elements = import_fragment(
        markdown,
        md_start,
        md_end,
        label,
        document,
        relationships,
        files,
    )
    replace_to_body_end(
        document,
        find_body_paragraph(document, docx_start),
        end_elements,
    )
    imported += len(end_elements)

    exact = replace_exact_paragraphs(document)
    version = update_version(document)
    index = update_table_index_entry(document)
    layout = keep_table_caption_with_table(document)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    write_package(path, files, original_mode)

    return {
        "elements": imported,
        "paragraphs": exact,
        "version": version,
        "index": index,
        "layout": layout,
    }


def apply_layout_only(path: Path) -> int:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}
    document = etree.fromstring(files["word/document.xml"])
    changed = keep_table_caption_with_table(document)
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    write_package(path, files, original_mode)
    return changed


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--layout-only", action="store_true")
    args = parser.parse_args()
    if args.layout_only:
        changed = apply_layout_only(args.docx.resolve())
        print(f"DOCX actualizado: {args.docx.resolve()}")
        print(f"Legendas mantidas com a tabela: {changed}")
        return
    result = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Elementos importados: {result['elements']}")
    print(f"Parágrafos substituídos: {result['paragraphs']}")
    print(f"Linha de versão actualizada: {result['version']}")
    print(f"Entrada da Tabela D.3 actualizada: {result['index']}")
    print(f"Legendas mantidas com a tabela: {result['layout']}")


if __name__ == "__main__":
    main()
