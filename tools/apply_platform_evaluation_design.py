#!/usr/bin/env python3
"""Integrate the design-oriented HandFab evaluation into the thesis DOCX.

The transformation edits the OOXML package in place, preserving the IPCA
template, figures, comments, styles, section settings and existing tables.
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


def paragraph_style(paragraph: etree._Element) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return values[0] if values else ""


def set_paragraph_text(paragraph: etree._Element, text: str) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = text


def paragraphs(root: etree._Element) -> list[etree._Element]:
    return root.xpath("//w:body//w:p", namespaces=NS)


def find_prefix(root: etree._Element, prefix: str, style: str | None = None) -> etree._Element:
    matches = [
        p for p in paragraphs(root)
        if paragraph_text(p).startswith(prefix) and (style is None or paragraph_style(p) == style)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph beginning {prefix!r} (style={style!r}); found {len(matches)}")
    return matches[0]


def replace_prefix(root: etree._Element, prefix: str, replacement: str, style: str | None = None) -> etree._Element:
    paragraph = find_prefix(root, prefix, style)
    set_paragraph_text(paragraph, replacement)
    return paragraph


def insert_normal_paragraphs(reference: etree._Element, template: etree._Element, texts: list[str]) -> None:
    for text in texts:
        paragraph = deepcopy(template)
        set_paragraph_text(paragraph, text)
        reference.addprevious(paragraph)


METHOD = (
    "Os modelos foram preparados no PrusaSlicer e no Bambu Studio. O fatiamento converte a geometria "
    "numa sequência de camadas e trajectórias de deposição, definindo altura de camada, paredes, "
    "enchimento, suportes, temperaturas e orientação. Foram arquivados três projectos Bambu Lab A1, "
    "gerados no Bambu Studio 1.10.02.76: um projecto PLA para o Flexy Beast e dois projectos, "
    "respectivamente em PLA e PETG, para a UnLimbited Phoenix. Foi ainda preservado um projecto Prusa "
    "MINI para o Paraglider Hand, gerado no PrusaSlicer 2.8.1. Os projectos Bambu registam camada de "
    "0,24 mm, duas paredes, 15% de enchimento em grelha, suporte em árvore automático e aba de 5 mm. "
    "No projecto PETG, as oito peças da UnLimbited Phoenix estão atribuídas ao perfil Bambu PETG Basic, "
    "com temperaturas nominais de 255 °C no bico e 70 °C na mesa. O projecto Prusa regista camada de "
    "0,20 mm, duas paredes, 15% de enchimento em grelha, PLA, bico de 0,4 mm, mesa a 60 °C e suporte "
    "desactivado. Os parâmetros comparáveis foram mantidos nas restantes impressões, segundo os "
    "registos disponíveis, embora não exista um ficheiro de configuração individual para cada peça "
    "produzida. A distribuição dos modelos pelos dois programas, materiais e equipamentos decorreu da "
    "disponibilidade dos projectos de preparação e das condições operacionais de cada impressão. Não foi "
    "desenhado um ensaio comparativo: a mesma geometria não foi produzida em condições equivalentes nos "
    "diferentes sistemas e materiais, pelo que estes registos não permitem inferir superioridade ou "
    "equivalência entre programas, impressoras, PLA e PETG."
)

METHOD_COMPLEMENT = (
    "Como complemento à avaliação inicial, foram executadas, em 13 e 14 de Julho de 2026, campanhas "
    "automatizadas orientadas para três qualidades relevantes do processo de design: previsibilidade da "
    "geração paramétrica, capacidade de recuperação perante valores ou falhas previsíveis e acessibilidade "
    "técnica da interacção. Os ensaios locais decorreram numa instância isolada, com perfis sintéticos, para "
    "não alterar os dados de desenvolvimento ou da plataforma pública. A versão pública, disponível em "
    "https://handfab.pedrocandeias.net/, foi examinada apenas na superfície não autenticada. O protocolo, "
    "os casos, os resultados completos e os registos que permitem reconstruir as execuções são apresentados "
    "no Anexo B. Estes ensaios avaliam o comportamento técnico do protótipo; não constituem avaliação de "
    "usabilidade com participantes nem certificação de acessibilidade."
)

NEW_HEADING = "8.1.2 Avaliação complementar da previsibilidade, recuperação e acessibilidade"

RESULT_PARAGRAPHS = [
    (
        "Na repetição de configurações congeladas foram concluídas sete exportações do Flexy Beast, cinco "
        "do Paraglider Hand e cinco da UnLimbited Phoenix. Dentro de cada modelo, todas as exportações "
        "concluídas produziram ficheiros binariamente idênticos e conservaram as mesmas dimensões e métricas "
        "geométricas. O critério previamente definido exigia dez conclusões por modelo; como algumas "
        "execuções foram interrompidas por bloqueios e tempos-limite no ambiente de ensaio, o resultado é "
        "parcial. A evidência sustenta consistência nas execuções concluídas, mas não autoriza declarar "
        "cumprido o critério integral de repetibilidade."
    ),
    (
        "A mesma configuração da UnLimbited Phoenix produziu resultados idênticos no Chromium e no Firefox. "
        "Uma primeira tentativa com WebKit foi invalidada por uma opção de arranque aplicada incorrectamente "
        "pelo próprio instrumento de ensaio. Depois de corrigida essa configuração, o navegador iniciou, mas "
        "o percurso parou na autenticação e não chegou à geração da geometria. A compatibilidade com WebKit "
        "permanece, por isso, inconclusiva; a falha não é classificada como incompatibilidade da plataforma."
    ),
    (
        "Os cenários de recuperação abrangeram valores nos limites, entradas inválidas, ausência de cobertura "
        "populacional directa, incompatibilidade entre perfil e modelo, indisponibilidade do serviço de IA, "
        "falha de renderização e tentativa de exportação sem geometria. A maioria dos percursos rejeitou a "
        "entrada, preservou o último estado válido ou permitiu nova tentativa. Foram, contudo, identificadas "
        "duas fragilidades relevantes para o design do controlo: uma sugestão simulada de IA acima do limite "
        "foi detectável pelo esquema, mas chegou a ser aplicada ao valor interno; e a interface rejeitou texto "
        "num campo numérico enquanto o pedido directo à plataforma aceitou esse mesmo tipo de valor. Estes "
        "resultados mostram que a protecção não deve depender apenas do controlo visual e que as mesmas regras "
        "têm de actuar antes de qualquer valor ser guardado ou enviado para a geometria."
    ),
    (
        "A auditoria automática de acessibilidade examinou oito estados do percurso local autenticado. Foram "
        "identificadas quatro categorias de barreira: contraste de cor insuficiente, ausência de associação "
        "programática entre rótulos e controlos, elementos interactivos aninhados e falta de nome acessível "
        "num elemento de selecção. A página pública não autenticada não apresentou violações automáticas nos "
        "elementos examinados, mas incluiu uma verificação inconclusiva e não representa os percursos internos. "
        "As verificações manuais por teclado, foco, ampliação, leitor de ecrã e alternativa ao visualizador "
        "tridimensional não foram executadas. Assim, os resultados definem prioridades concretas de revisão da "
        "interface, mas não demonstram conformidade global com as WCAG 2.2 nem acessibilidade percebida por "
        "utilizadores."
    ),
    (
        "Em termos de Design Industrial, estas campanhas acrescentam três aprendizagens ao desenvolvimento "
        "do artefacto. A previsibilidade depende de regras geométricas explícitas e de condições de execução "
        "suficientemente estáveis; a robustez exige que limites e mensagens sejam coerentes em todas as etapas "
        "do fluxo; e a acessibilidade deve ser tratada como qualidade verificável da interface, e não apenas "
        "como intenção inclusiva. O Anexo B conserva a matriz de casos, os resultados por execução e a ficha "
        "técnica mínima necessária para permitir a sua revisão crítica."
    ),
]

FABRICATION_EVIDENCE = (
    "A evidência de fabrico inclui 116 ficheiros 3MF gerados para três modelos e quatro idades, quatro "
    "projectos com parâmetros de preparação e fotografias de peças físicas. Os 116 ficheiros representam "
    "exportações digitais, distribuídas por placas combinadas e peças individuais; esse total não corresponde "
    "a 116 impressões físicas. Os quatro projectos encontram-se em "
    "docs/print-validation/bambulaba1_flexy_beast_teen_15_print.3mf, "
    "docs/print-validation/bambulaba1_unlimbed_phoenix_hand_teen_15_print_project.3mf, "
    "docs/print-validation/unlimbed_phoenix_hand_teen_15_print_project_PETG.3mf e "
    "docs/print-validation/prusa_mini_paraglider_15_teen_print_profile.3mf. Cada projecto identifica um caso "
    "adolescente de 15 anos, o material configurado e a impressora usada. Os parâmetros comparáveis foram "
    "mantidos nas restantes impressões, segundo os registos disponíveis."
)

MATERIAL = (
    "Foram produzidos exemplares em PLA e PETG, e os projectos preservados identificam o material atribuído "
    "às peças preparadas. No caso da UnLimbited Phoenix, o projecto PETG atribui os oito conjuntos de peças "
    "ao perfil Bambu PETG Basic. Esta evidência documenta duas condições de produção, mas não constitui uma "
    "comparação controlada entre materiais, porque não foram definidos corpos de prova equivalentes, "
    "repetições, medições dimensionais ou ensaios mecânicos comparáveis. Não se retiram, portanto, conclusões "
    "sobre resistência, fragilidade ou durabilidade relativas de PLA e PETG."
)

FLEXY_LIMIT = (
    "Embora a documentação de origem do Flexy Beast preveja juntas em filamento flexível ou silicone moldado, "
    "não foram produzidas juntas flexíveis nem almofadas de silicone dos dedos. Os exemplares rígidos em PLA "
    "ou PETG não substituem esses componentes. Por conseguinte, não foram avaliados o comportamento elástico "
    "das juntas, o retorno dos dedos, a aderência das almofadas ou a influência desses elementos na montagem "
    "e no funcionamento do dispositivo."
)

ANNEX_A_LINK = (
    "Este encadeamento separa quatro unidades que não devem ser confundidas: a linha estatística do CSV, o "
    "perfil populacional agregado na base de dados, o conjunto de parâmetros compatíveis com o modelo activo "
    "e a geometria gerada depois de confirmação humana. O percurso pode, assim, ser reconstruído desde a "
    "fonte e a página registadas no CSV até ao caminho antropométrico, ao nome do parâmetro e ao limite "
    "aplicado pelo modelo."
)


def update_toc(root: etree._Element) -> None:
    old = find_prefix(root, "8.1.2 Preparação para impressão", "ndice3")
    nodes = old.xpath(".//w:t", namespaces=NS)
    if len(nodes) < 2:
        raise RuntimeError("Unexpected static index structure for Section 8.1.2")
    new = deepcopy(old)
    new_nodes = new.xpath(".//w:t", namespaces=NS)
    new_nodes[0].text = NEW_HEADING
    old.addprevious(new)
    nodes[0].text = "8.1.3 Preparação para impressão e protótipos físicos"


def update_phoenix_table(root: etree._Element) -> None:
    anchor = find_prefix(root, "UnLimbited Phoenix, 15 anos")
    rows = anchor.xpath("ancestor::w:tr[1]", namespaces=NS)
    if len(rows) != 1:
        raise RuntimeError("Could not locate the UnLimbited Phoenix preparation row")
    cells = rows[0].findall(qn("tc"))
    if len(cells) != 4:
        raise RuntimeError(f"Expected four cells in the Phoenix row; found {len(cells)}")
    values = [
        "UnLimbited Phoenix, 15 anos",
        "Bambu Lab A1, Bambu Studio 1.10.02.76",
        (
            "Dois projectos com camada de 0,24 mm, duas paredes e 15% de enchimento: peças atribuídas, "
            "respectivamente, a PLA e a Bambu PETG Basic; no PETG, bico a 255 °C e mesa a 70 °C"
        ),
        "Oito conjuntos de peças em cada projecto; programa regista 0 arestas corrigidas e 0 faces degeneradas",
    ]
    for cell, value in zip(cells, values):
        ps = cell.xpath(".//w:p", namespaces=NS)
        if not ps:
            raise RuntimeError("Expected a paragraph in each Phoenix table cell")
        set_paragraph_text(ps[0], value)
        for extra in ps[1:]:
            extra.getparent().remove(extra)


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))

    version_matches = [p for p in paragraphs(root) if paragraph_text(p).startswith("Versão do documento:")]
    if len(version_matches) > 1:
        raise RuntimeError("Found more than one manuscript version paragraph")
    if version_matches:
        set_paragraph_text(version_matches[0], "Versão do documento: 0.4.32")

    replace_prefix(root, "Os modelos foram preparados no PrusaSlicer", METHOD)

    criteria = find_prefix(root, "A avaliação usa seis critérios:")
    if not any(paragraph_text(p) == METHOD_COMPLEMENT for p in paragraphs(root)):
        complement = deepcopy(criteria)
        set_paragraph_text(complement, METHOD_COMPLEMENT)
        criteria.addnext(complement)

    old_body_heading = find_prefix(root, "8.1.2 Preparação para impressão", "Cabealho3")
    if not any(paragraph_text(p) == NEW_HEADING for p in paragraphs(root)):
        update_toc(root)
        new_heading = deepcopy(old_body_heading)
        set_paragraph_text(new_heading, NEW_HEADING)
        old_body_heading.addprevious(new_heading)
        normal_template = find_prefix(root, "Estes resultados confirmam a existência")
        insert_normal_paragraphs(old_body_heading, normal_template, RESULT_PARAGRAPHS)
    set_paragraph_text(old_body_heading, "8.1.3 Preparação para impressão e protótipos físicos")

    replace_prefix(root, "A evidência de fabrico inclui 116 ficheiros", FABRICATION_EVIDENCE)
    update_phoenix_table(root)

    material = replace_prefix(root, "Os dois projectos Bambu contêm três materiais", MATERIAL)
    if not any(paragraph_text(p) == FLEXY_LIMIT for p in paragraphs(root)):
        flexy = deepcopy(material)
        set_paragraph_text(flexy, FLEXY_LIMIT)
        material.addnext(flexy)

    existing_annex_link = [
        p for p in paragraphs(root)
        if paragraph_text(p).startswith("Este encadeamento separa quatro unidades")
        or paragraph_text(p).startswith("Este encadeamento separa a linha estatística")
    ]
    if len(existing_annex_link) != 1:
        raise RuntimeError(f"Expected one Annex A linkage paragraph; found {len(existing_annex_link)}")
    set_paragraph_text(existing_annex_link[0], ANNEX_A_LINK)

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()

    source = args.docx.resolve()
    if not source.exists():
        raise SystemExit(f"DOCX not found: {source}")

    with ZipFile(source, "r") as archive:
        updated_xml = apply(archive.read("word/document.xml"))
        fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=source.parent)
        os.close(fd)
        temp_path = Path(temp_name)
        try:
            with ZipFile(temp_path, "w", ZIP_DEFLATED) as output:
                for item in archive.infolist():
                    data = updated_xml if item.filename == "word/document.xml" else archive.read(item.filename)
                    output.writestr(item, data)
            temp_path.replace(source)
        finally:
            temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
