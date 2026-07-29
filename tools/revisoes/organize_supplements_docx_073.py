#!/usr/bin/env python3
"""Integra no DOCX 0.4.73 a organização explícita dos suplementos.

O programa altera apenas ``word/document.xml``. As notas, os comentários, as
imagens e todos os restantes componentes do pacote são preservados byte a byte.
"""

import argparse
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx")
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def qn(local: str) -> str:
    return f"{{{W}}}{local}"


def text_of(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_space(text_node: etree._Element) -> None:
    value = text_node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        text_node.set(XML_SPACE, "preserve")
    else:
        text_node.attrib.pop(XML_SPACE, None)


def replace_fragment(paragraph: etree._Element, old: str, new: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    full = "".join(node.text or "" for node in nodes)
    if full.count(old) != 1:
        raise RuntimeError(
            f"Fragmento não unívoco no parágrafo: {old!r}; texto={full!r}"
        )
    start = full.index(old)
    end = start + len(old)
    positions: list[tuple[etree._Element, int, int]] = []
    cursor = 0
    for node in nodes:
        value = node.text or ""
        positions.append((node, cursor, cursor + len(value)))
        cursor += len(value)
    first = next(item for item in positions if item[2] > start)
    last = next(item for item in positions if item[2] >= end and item[1] < end)
    first_node, first_start, _ = first
    last_node, last_start, _ = last
    first_value = first_node.text or ""
    last_value = last_node.text or ""
    prefix = first_value[: start - first_start]
    suffix = last_value[end - last_start :]
    if first_node is last_node:
        first_node.text = prefix + new + suffix
        set_space(first_node)
        return
    first_node.text = prefix + new
    set_space(first_node)
    clearing = False
    for node, _, _ in positions:
        if node is first_node:
            clearing = True
            continue
        if not clearing:
            continue
        if node is last_node:
            node.text = suffix
            set_space(node)
            break
        node.text = ""
        set_space(node)


def replace_once(root: etree._Element, old: str, new: str) -> None:
    paragraphs = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if old in text_of(paragraph)
    ]
    if len(paragraphs) != 1:
        raise RuntimeError(
            f"Esperava uma ocorrência de {old!r}; encontrei {len(paragraphs)}"
        )
    replace_fragment(paragraphs[0], old, new)


def clone_paragraph(template: etree._Element, text: str) -> etree._Element:
    paragraph = deepcopy(template)
    for child in list(paragraph):
        if child.tag != qn("pPr"):
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    text_node = etree.SubElement(run, qn("t"))
    text_node.text = text
    set_space(text_node)
    return paragraph


def unique_paragraph(root: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:body/w:p", namespaces=NS)
        if text_of(paragraph) == text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo {text!r}; encontrei {len(matches)}")
    return matches[0]


def document_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnote_references": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "comment_references": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def add_general_index(root: etree._Element) -> None:
    text = (
        "O material suplementar entregue com a dissertação encontra-se organizado "
        "na pasta suplementos/ em quatro conjuntos: Suplemento 1 — Dados "
        "antropométricos; Suplemento 2 — Avaliação técnica da plataforma; "
        "Suplemento 3 — Parametrização e percurso numérico; e Suplemento 4 — "
        "Preparação para impressão e protótipos. O ficheiro "
        "manifesto_ficheiros.csv relaciona cada elemento com a sua origem e função, "
        "enquanto SHA256SUMS permite verificar a integridade do pacote."
    )
    if any(text_of(p) == text for p in root.xpath("//w:body/w:p", namespaces=NS)):
        return
    heading = unique_paragraph(root, "3.4 Métodos de recolha e análise de dados")
    template = unique_paragraph(
        root,
        "A recolha combinou análise documental, comparação de precedentes, "
        "inspecção do código, construção paramétrica, cenários automatizados, "
        "medição de malhas, preparação para impressão, observação de peças físicas "
        "e reflexão sobre cada ciclo. Os dados usados na análise foram: parâmetros "
        "e limites declarados em catálogo de modelos; respostas JSON e metadados de "
        "execução; dimensões das malhas exportadas; relatórios técnicos por modelo; "
        "ficheiros 3MF; quatro projectos com parâmetros de preparação; resultados "
        "de doze casos sob uma condição digital comum; fotografias dos protótipos; "
        "e registos de alterações do código.",
    )
    heading.addprevious(clone_paragraph(template, text))


def add_missing_annex_c_sections(root: etree._Element) -> None:
    c10 = unique_paragraph(root, "C.10 Limite de interpretação")
    heading_template = c10
    body_template = unique_paragraph(
        root,
        "As adaptações mostram como modelos abertos e heterogéneos podem ser "
        "reorganizados em torno de um conjunto comum de medidas e controlos. O "
        "contributo é técnico e de projecto: explicita decisões, dependências, "
        "excepções e fragilidades que ficam ocultas quando uma prótese é tratada "
        "apenas como um ficheiro STL escalável.",
    )
    if not any(
        text_of(p) == "C.9 Relação com o Suplemento 3"
        for p in root.xpath("//w:body/w:p", namespaces=NS)
    ):
        additions = (
            clone_paragraph(heading_template, "C.9 Relação com o Suplemento 3"),
            clone_paragraph(
                body_template,
                "O Suplemento 3 — Parametrização e percurso numérico preserva um "
                "estado histórico útil: contém 42 parâmetros numéricos dos três "
                "modelos comparados e um percurso do perfil de ensaio até a três "
                "malhas do Flexy Beast. Deve, contudo, ser identificado como "
                "fotografia do estado usado nesses ensaios.",
            ),
            clone_paragraph(
                body_template,
                "Depois desse estado, a estrutura paramétrica da braçadeira do "
                "Flexy Beast foi alterada. Por esse motivo, gauntlet_width_mm, "
                "gauntlet_length_mm, gauntlet_wall_mm, gauntlet_pos_adjust e "
                "strap_splay_adjust não descrevem o estado final examinado. Foram "
                "substituídos, no essencial, por wrist_circumference_mm, "
                "gauntlet_tilt, gauntlet_length_scale, gauntlet_rim_hole_d e uma "
                "colocação automática sobre o eixo do pino. O presente anexo "
                "acompanha esse estado histórico com esta nota de evolução.",
            ),
        )
        for addition in additions:
            c10.addprevious(addition)

    c12 = unique_paragraph(root, "C.12 Verificações executadas")
    bullet_template = unique_paragraph(
        root,
        "- comparação dos quatro modelos registados com os parâmetros de catálogo de modelos;",
    )
    if not any(
        text_of(p) == "C.11 Fontes técnicas consultadas"
        for p in root.xpath("//w:body/w:p", namespaces=NS)
    ):
        texts = (
            "C.11 Fontes técnicas consultadas",
            "- relatório técnico de adaptação antropométrica da plataforma;",
            "- catálogo de configuração dos modelos;",
            "- serviços de correspondência e importação de perfis antropométricos;",
            "- implementações OpenSCAD activas das famílias Flexy Beast, Cyborg "
            "Beast, Paraglider Hand e UnLimbited Phoenix, incluindo as dependências "
            "de montagem;",
            "- dicionário integral de parâmetros e percurso numérico do perfil de "
            "ensaio, conservados no Suplemento 3 — Parametrização e percurso numérico;",
            "- Capítulo 4 do manuscrito consolidado;",
            "- relatório integral de revisão académica.",
        )
        additions = [clone_paragraph(heading_template, texts[0])]
        additions.extend(clone_paragraph(bullet_template, text) for text in texts[1:])
        for addition in additions:
            c12.addprevious(addition)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", nargs="?", type=Path, default=DOCX)
    args = parser.parse_args()
    docx = args.docx
    if not docx.is_file():
        raise SystemExit(f"Ficheiro não encontrado: {docx}")
    with ZipFile(docx) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    outside_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    root = etree.fromstring(entries["word/document.xml"])
    before_state = document_state(root)

    replacements = (
        (
            "dicionário suplementar arquivado",
            "dicionário do Suplemento 3 — Parametrização e percurso numérico",
        ),
        (
            "O material suplementar do Anexo C apresenta a versão integral do "
            "dicionário de parâmetros",
            "O Suplemento 3 — Parametrização e percurso numérico apresenta a versão "
            "integral do dicionário de parâmetros",
        ),
        (
            "integram o material suplementar do Anexo C",
            "integram o Suplemento 3 — Parametrização e percurso numérico",
        ),
        (
            "conservados apenas no material técnico suplementar",
            "conservados no Suplemento 2 — Avaliação técnica da plataforma",
        ),
        (
            "integram o material suplementar da Série A",
            "são entregues na subpasta projectos_preparacao/ do Suplemento 4 — "
            "Preparação para impressão e protótipos",
        ),
        (
            "conservados no material suplementar da avaliação",
            "conservados na subpasta avaliacao_ia_antropometrica/ do Suplemento 2 — "
            "Avaliação técnica da plataforma",
        ),
        (
            "Material de apoio da investigação, base de dados da mão com dados de "
            "várias populações, repositório da plataforma",
            "Suplemento 1 — Dados antropométricos",
        ),
        (
            "C.9 Relação com o suplemento dos ensaios principais",
            "C.9 Relação com o Suplemento 3",
        ),
        (
            "encontra-se registado no material suplementar associado ao Anexo C",
            "encontra-se preservado no Suplemento 3 — Parametrização e percurso numérico",
        ),
        (
            "no suplemento dos ensaios principais",
            "nesse suplemento",
        ),
        (
            "Os resultados quantitativos completos e os registos geométricos "
            "encontram-se no material suplementar associado a este anexo.",
            "Os resultados quantitativos completos e os registos geométricos "
            "encontram-se no Suplemento 4 — Preparação para impressão e protótipos.",
        ),
        (
            "constam do registo suplementar da Série B",
            "constam do ficheiro resultados_serie_b.csv do Suplemento 4",
        ),
        (
            "constam do registo geométrico suplementar",
            "constam do ficheiro resultados_geometria.csv do Suplemento 4",
        ),
        (
            "a folha suplementar de comparação dimensional",
            "o ficheiro comparacao_dimensional_72_medicoes.csv do Suplemento 4",
        ),
        (
            "no campo estado_parametro da folha suplementar",
            "no campo estado_parametro do mesmo ficheiro",
        ),
        (
            "Os originais integram o material suplementar",
            "Os 19 originais encontram-se na subpasta fotografias_originais/ do "
            "Suplemento 4",
        ),
        (
            "nota técnica suplementar de compatibilidade dimensional",
            "ficheiro compatibilidade_dimensionamento.md do Suplemento 4",
        ),
        (
            "- confronto entre os ensaios principais e o estado final examinado;",
            "- confronto entre o Suplemento 3 e o estado final examinado;",
        ),
    )
    for old, new in replacements:
        replace_once(root, old, new)

    add_general_index(root)
    add_missing_annex_c_sections(root)

    vague = [
        text_of(p)
        for p in root.xpath(".//w:p", namespaces=NS)
        if (
            "material suplementar" in text_of(p).casefold()
            and not text_of(p).startswith(
                "O material suplementar entregue com a dissertação encontra-se organizado"
            )
        )
        or "registo suplementar" in text_of(p).casefold()
        or "folha suplementar" in text_of(p).casefold()
    ]
    if vague:
        raise RuntimeError(f"Permanecem referências suplementares vagas: {vague}")
    after_state = document_state(root)
    if after_state != before_state:
        raise RuntimeError(
            f"Referências internas alteradas: antes={before_state}; depois={after_state}"
        )

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(
        prefix=f".{docx.name}.", suffix=".tmp", dir=docx.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_entries = {
                info.filename: result.read(info.filename) for info in result.infolist()
            }
        new_outside_hashes = {
            name: sha256(data).hexdigest()
            for name, data in result_entries.items()
            if name != "word/document.xml"
        }
        if new_outside_hashes != outside_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        temporary.replace(docx)
    finally:
        if temporary.exists():
            temporary.unlink()

    print(
        "Suplementos organizados no DOCX; "
        f"notas={before_state['footnote_references']}, "
        f"comentários={before_state['comment_references']}, "
        f"imagens={before_state['drawings']}"
    )


if __name__ == "__main__":
    main()
