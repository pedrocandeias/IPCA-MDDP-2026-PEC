#!/usr/bin/env python3
"""Repõe o enquadramento aprovado, sincroniza secções revistas e integra o Anexo D."""

from __future__ import annotations

import os
import tempfile
from copy import deepcopy
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_annex_local_indexes import (
    add_local_index_styles,
    make_local_title,
    set_page_break_before,
    set_style,
)
from integrate_annexes_bc import (
    NS,
    W,
    element_text,
    import_annex,
    make_static_entry,
    paragraph_style,
    qn,
    replace_paragraph_text,
    set_paragraph_style,
)
# `md_to_docx`/`docx_to_md` estão na raiz de tools/ (pontos de entrada
# documentados); acrescentá-la ao sys.path mantém este import a funcionar.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from md_to_docx import write_docx


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
ANNEX_D = (
    ROOT
    / "anexos/testes_preparacao_impressao"
    / "anexo_d_preparacao_impressao.docx"
)

FRAGMENTS = (
    (
        "### 1.3.2 Objectivos específicos",
        "### 1.4 Abordagem metodológica geral",
        "1.3.2 Objectivos específicos",
        "1.4 Abordagem metodológica geral",
        "questions",
    ),
    (
        "### 3.2 O design industrial como prática investigativa",
        "## Capítulo 4 — Desenvolvimento do Modelo Paramétrico",
        "3.2 O design industrial como prática investigativa",
        "Capítulo 4 — Desenvolvimento do Modelo Paramétrico",
        "chapter3",
    ),
    (
        "### 8.1.3 Preparação para impressão e protótipos físicos",
        "### 8.2 Avaliação da coerência das sugestões de IA",
        "8.1.3 Preparação para impressão e protótipos físicos",
        "8.2 Avaliação da coerência das sugestões de IA",
        "chapter8_print",
    ),
    (
        "### 8.4 Discussão dos resultados face aos objectivos",
        "## Capítulo 9 — Conclusões e Trabalhos Futuros",
        "8.4 Discussão dos resultados face aos objectivos",
        "Capítulo 9 — Conclusões e Trabalhos Futuros",
        "chapter8_discussion",
    ),
    (
        "### 9.1 Resposta ao problema e às perguntas de investigação",
        "### 9.2 Contributos da investigação",
        "9.1 Resposta ao problema e às perguntas de investigação",
        "9.2 Contributos da investigação",
        "chapter9_answers",
    ),
    (
        "### 9.3 Limitações",
        "## Bibliografia",
        "9.3 Limitações",
        "Referências Bibliográficas",
        "chapter9_limits",
    ),
)


def find_body_paragraph(root: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}")
    return matches[0]


def find_index_entry(root: etree._Element, prefix: str, style: str | None = None) -> etree._Element:
    matches = []
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        p_style = paragraph_style(paragraph)
        if not p_style.startswith("ndice"):
            continue
        if style is not None and p_style != style:
            continue
        if element_text(paragraph).startswith(prefix):
            matches.append(paragraph)
    if len(matches) != 1:
        raise RuntimeError(f"Esperada uma entrada de índice {prefix!r}; encontradas {len(matches)}")
    return matches[0]


def replace_range(
    start: etree._Element,
    end: etree._Element,
    replacements: list[etree._Element],
) -> None:
    parent = start.getparent()
    current = start
    while current is not None and current is not end:
        following = current.getnext()
        parent.remove(current)
        current = following
    if current is None:
        raise RuntimeError("O fim da secção não sucede ao início")
    for element in replacements:
        end.addprevious(element)


def extract_fragment(markdown: str, start: str, end: str) -> str:
    start_pos = markdown.find(start)
    end_pos = markdown.find(end, start_pos + len(start))
    if start_pos < 0 or end_pos < 0:
        raise RuntimeError(f"Não foi possível extrair {start!r} até {end!r}")
    return markdown[start_pos:end_pos].strip() + "\n"


def import_fragment(
    markdown: str,
    start: str,
    end: str,
    label: str,
    document: etree._Element,
    relationships: etree._Element,
    files: dict[str, bytes],
) -> list[etree._Element]:
    fragment_text = extract_fragment(markdown, start, end)
    md_path = ROOT / f"._fragment_{label}.md"
    docx_path = ROOT / f"._fragment_{label}.docx"
    try:
        md_path.write_text(fragment_text, encoding="utf-8")
        write_docx(md_path, docx_path)
        elements, _, _, _ = import_annex(
            docx_path,
            document,
            relationships,
            files,
            f"fragment_{label}",
        )
    finally:
        md_path.unlink(missing_ok=True)
        docx_path.unlink(missing_ok=True)

    for element in elements:
        if element.tag != qn(W, "p"):
            continue
        text = element_text(element)
        if text.startswith(("Tabela ", "Figura ")) and " — " in text:
            set_paragraph_style(element, "Legenda")
    return elements


def replace_campaign_terms(document: etree._Element) -> int:
    replacements = (
        ("Data das campanhas", "Data das séries de ensaios"),
        ("campanhas complementares", "séries complementares de ensaios"),
        ("Campanhas complementares", "Séries complementares de ensaios"),
        ("campanha complementar", "série complementar de ensaios"),
        ("Campanha complementar", "Série complementar de ensaios"),
        ("campanhas", "séries de ensaios"),
        ("Campanhas", "Séries de ensaios"),
        ("campanha", "série de ensaios"),
        ("Campanha", "Série de ensaios"),
    )
    changed = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        original = element_text(paragraph)
        if "campanha" not in original.lower():
            continue
        updated = original
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != original:
            replace_paragraph_text(paragraph, updated)
            changed += 1
    return changed


def update_version(document: etree._Element) -> None:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph).startswith("Versão do documento:")
    ]
    if len(matches) == 1:
        replace_paragraph_text(matches[0], "Versão do documento: 0.4.40")


def add_static_entry_after(
    document: etree._Element,
    anchor_prefix: str,
    title: str,
    page: str,
    style: str | None = None,
) -> etree._Element:
    if any(
        paragraph_style(p).startswith("ndice") and element_text(p).startswith(title.split(" — ", 1)[0])
        for p in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        return find_index_entry(document, title.split(" — ", 1)[0])
    anchor = find_index_entry(document, anchor_prefix, style)
    entry = make_static_entry(anchor, title, page)
    anchor.addnext(entry)
    return entry


def section_break(final_sectpr: etree._Element) -> etree._Element:
    paragraph = etree.Element(qn(W, "p"))
    ppr = etree.SubElement(paragraph, qn(W, "pPr"))
    previous = deepcopy(final_sectpr)
    section_type = previous.find(qn(W, "type"))
    if section_type is None:
        section_type = etree.Element(qn(W, "type"))
        previous.insert(0, section_type)
    section_type.set(qn(W, "val"), "nextPage")
    ppr.append(previous)
    return paragraph


def set_landscape(sectpr: etree._Element) -> None:
    page_size = sectpr.find(qn(W, "pgSz"))
    if page_size is None:
        page_size = etree.SubElement(sectpr, qn(W, "pgSz"))
    page_size.set(qn(W, "w"), "16838")
    page_size.set(qn(W, "h"), "11906")
    page_size.set(qn(W, "orient"), "landscape")
    margins = sectpr.find(qn(W, "pgMar"))
    if margins is not None:
        margins.set(qn(W, "left"), "1134")
        margins.set(qn(W, "right"), "1134")
    page_numbering = sectpr.find(qn(W, "pgNumType"))
    if page_numbering is not None:
        page_numbering.attrib.pop(qn(W, "start"), None)


def build_local_index(
    document: etree._Element,
    styles: etree._Element,
    imported: list[etree._Element],
    headings: list[tuple[str, int]],
) -> list[etree._Element]:
    add_local_index_styles(styles)
    if not imported or not element_text(imported[0]).startswith("Anexo D —"):
        raise RuntimeError("O corpo importado do Anexo D não começa pelo título esperado")
    title = imported[0]
    remainder = imported[1:]
    local_title = make_local_title("D")

    templates = {}
    for level in (2, 3, 4):
        templates[level] = next(
            paragraph
            for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
            if paragraph_style(paragraph) == f"ndiceAnexo{level}"
            and len(paragraph.xpath(".//w:t", namespaces=NS)) >= 2
        )

    entries = []
    for heading, level in headings:
        if level == 1:
            continue
        target_level = min(max(level, 2), 4)
        entry = make_static_entry(templates[target_level], heading, "145")
        set_style(entry, f"ndiceAnexo{target_level}")
        entries.append(entry)
    if remainder and remainder[0].tag == qn(W, "p"):
        set_page_break_before(remainder[0])
    return [title, local_title, *entries, *remainder]


def apply(path: Path) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    styles = etree.fromstring(files["word/styles.xml"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    if any(
        element_text(p).startswith("Anexo D —")
        and paragraph_style(p) == "TtulosPrembulo-IPCA"
        for p in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        raise RuntimeError("O Anexo D já está integrado no DOCX")

    term_changes = replace_campaign_terms(document)
    update_version(document)

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
        start = find_body_paragraph(document, docx_start)
        end = find_body_paragraph(document, docx_end)
        replace_range(start, end, elements)

    add_static_entry_after(
        document,
        "Tabela 3.2",
        "Tabela 3.3 — Métodos, unidades de análise, critérios e localização dos resultados",
        "38",
    )
    add_static_entry_after(
        document,
        "Tabela 8.7",
        "Tabela 9.1 — Estado da resposta às perguntas de investigação aprovadas",
        "96",
    )

    imported_d, headings_d, _, _ = import_annex(
        ANNEX_D,
        document,
        relationships,
        files,
        "annex_d",
    )
    for element in imported_d:
        if element.tag == qn(W, "p") and element_text(element).startswith("Tabela D."):
            set_paragraph_style(element, "Legenda")
    annex_elements = build_local_index(document, styles, imported_d, headings_d)

    main_c = find_index_entry(document, "Anexo C —", "ndice1")
    main_d = make_static_entry(
        main_c,
        "Anexo D — Preparação para fabrico e verificação dos protótipos",
        "145",
    )
    main_c.addnext(main_d)

    table_anchor = find_index_entry(document, "Tabela C.4")
    for title in (
        "Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada",
        "Tabela D.2 — Estimativas de preparação para impressão na condição digital comum",
        "Tabela D.3 — Preparação da comparação dimensional da palma",
    ):
        entry = make_static_entry(table_anchor, title, "145")
        table_anchor.addnext(entry)
        table_anchor = entry

    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("DOCX sem corpo")
    final_sectpr = body.find(qn(W, "sectPr"))
    if final_sectpr is None:
        raise RuntimeError("DOCX sem propriedades finais de secção")
    position = body.index(final_sectpr)
    body.insert(position, section_break(final_sectpr))
    position += 1
    for element in annex_elements:
        body.insert(position, element)
        position += 1
    set_landscape(final_sectpr)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/styles.xml"] = etree.tostring(
        styles, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temp_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)
    return {"terminology_changes": term_changes, "annex_headings": len(headings_d)}


def fix_existing_section_numbering(path: Path) -> None:
    """Remove o reinício herdado da numeração na secção final do Anexo D."""
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}
    document = etree.fromstring(files["word/document.xml"])
    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("DOCX sem corpo")
    final_sectpr = body.find(qn(W, "sectPr"))
    if final_sectpr is None:
        raise RuntimeError("DOCX sem propriedades finais de secção")
    page_numbering = final_sectpr.find(qn(W, "pgNumType"))
    if page_numbering is not None:
        page_numbering.attrib.pop(qn(W, "start"), None)
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temp_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


def restore_exact_approved_formulations(path: Path) -> int:
    """Repõe a sintaxe aprovada, alterando apenas a ortografia europeia."""
    replacements = {
        "1. Como podem o design de produto, os métodos paramétricos e a inteligência artificial melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo projectual?":
            "1. Como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo projectual?",
        "2. Quais são as metodologias e as ferramentas que permitem avaliar a eficácia, a usabilidade, a durabilidade e a reprodutibilidade de próteses impressas em 3D?":
            "2. Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a reprodutibilidade de próteses impressas em 3D?",
        "3. Como pode o design industrial conciliar requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?":
            "3. Como o design industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?",
        "A hipótese principal sustenta que a integração do design paramétrico e de ferramentas de inteligência artificial permite desenvolver próteses mais adequadas às necessidades anatómicas e funcionais dos utilizadores, tornando o processo de personalização mais acessível e escalável, especialmente em contextos economicamente desfavorecidos. As hipóteses secundárias aprofundam esta perspectiva, sugerindo que a combinação de princípios de design inclusivo, Design for Additive Manufacturing (DfAM) e processos participativos pode melhorar a usabilidade, o conforto e a aceitação, ao mesmo tempo que reduz a dependência de especialistas.":
            "A hipótese principal sustenta que a integração de design paramétrico e de ferramentas de inteligência artificial permite desenvolver próteses mais adequadas às necessidades anatómicas e funcionais dos utilizadores, tornando o processo de personalização mais acessível e escalável, especialmente em contextos economicamente desfavorecidos. As hipóteses secundárias aprofundam esta perspetiva, sugerindo que a combinação de princípios de design inclusivo, Design for Additive Manufacturing (DfAM) e processos participativos pode melhorar a usabilidade, o conforto e a aceitação, ao mesmo tempo que reduz a dependência de especialistas.",
    }
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}
    document = etree.fromstring(files["word/document.xml"])
    changed = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        current = element_text(paragraph)
        if current in replacements:
            replace_paragraph_text(paragraph, replacements[current])
            changed += 1
    if changed != len(replacements):
        raise RuntimeError(
            f"Esperadas {len(replacements)} formulações; foram localizadas {changed}"
        )
    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temp_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)
    return changed


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--fix-existing-numbering", action="store_true")
    parser.add_argument("--restore-exact-formulations", action="store_true")
    args = parser.parse_args()
    if args.restore_exact_formulations:
        changed = restore_exact_approved_formulations(args.docx.resolve())
        print(f"Formulações aprovadas repostas: {changed}")
        return
    if args.fix_existing_numbering:
        fix_existing_section_numbering(args.docx.resolve())
        print(f"Numeração da secção final corrigida: {args.docx.resolve()}")
        return
    result = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Substituições terminológicas: {result['terminology_changes']}")
    print(f"Cabeçalhos importados do Anexo D: {result['annex_headings']}")


if __name__ == "__main__":
    main()
