#!/usr/bin/env python3
"""Integra o registo fotográfico dos protótipos no DOCX institucional."""

from __future__ import annotations

import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_approved_questions_annex_d import import_fragment, replace_range
from integrate_annexes_bc import (
    NS,
    element_text,
    make_static_entry,
    paragraph_style,
    qn,
    set_paragraph_style,
    W,
)


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo {text!r}; encontrados {len(matches)}")
    return matches[0]


def update_figure_index(document: etree._Element) -> int:
    titles = {
        "Figura 8.1": (
            "Figura 8.1 — Componentes impressos e estados preliminares de montagem: "
            "segmentos digitais articulados, palma e elementos separados."
        ),
        "Figura 8.2": (
            "Figura 8.2 — Séries físicas de segmentos identificados pelos perfis de ensaio "
            "de 8, 15, 28 e 70 anos."
        ),
        "Figura 8.3": (
            "Figura 8.3 — UnLimbited Phoenix configurada para o perfil de ensaio de 15 anos, "
            "apresentada em sete vistas da montagem física."
        ),
    }
    changed = 0
    for prefix, title in titles.items():
        matches = [
            paragraph
            for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
            if paragraph_style(paragraph).startswith("ndice")
            and element_text(paragraph).startswith(prefix)
        ]
        if len(matches) != 1:
            raise RuntimeError(f"Esperada uma entrada de figuras {prefix}; encontradas {len(matches)}")
        nodes = matches[0].xpath(".//w:t", namespaces=NS)
        if len(nodes) < 2:
            raise RuntimeError(f"Entrada de figuras incompleta: {prefix}")
        nodes[0].text = title
        changed += 1
    return changed


def add_annex_index_entry(document: etree._Element) -> bool:
    title = "D.4.5 Registo fotográfico dos protótipos"
    if any(
        paragraph_style(p).startswith("ndiceAnexo") and element_text(p).startswith(title)
        for p in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        return False
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph) == "ndiceAnexo3"
        and element_text(paragraph).startswith("D.4.4 Comparação entre entrada")
    ]
    if len(matches) != 1:
        raise RuntimeError("Não foi localizada a entrada D.4.4 no índice local")
    entry = make_static_entry(matches[0], title, "159")
    matches[0].addnext(entry)
    return True


def apply(path: Path) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    replacements = (
        (
            "### 8.1.3 Preparação para impressão e protótipos físicos",
            "### 8.2 Avaliação da coerência das sugestões de IA",
            "8.1.3 Preparação para impressão e protótipos físicos",
            "8.2 Avaliação da coerência das sugestões de IA",
            "photographs_chapter8",
        ),
        (
            "### D.4.4 Comparação entre entrada, malha e peça física",
            "## D.5 Compatibilidade com orientações de dimensionamento",
            "D.4.4 Comparação entre entrada, malha e peça física",
            "D.5 Compatibilidade com orientações de dimensionamento",
            "photographs_annexd",
        ),
    )

    imported_count = 0
    for md_start, md_end, docx_start, docx_end, label in replacements:
        elements = import_fragment(
            markdown,
            md_start,
            md_end,
            label,
            document,
            relationships,
            files,
        )
        for element in elements:
            if element.tag == qn(W, "p"):
                text = element_text(element)
                if text.startswith(("Tabela ", "Figura ")) and " — " in text:
                    set_paragraph_style(element, "Legenda")
        replace_range(
            find_body_paragraph(document, docx_start),
            find_body_paragraph(document, docx_end),
            elements,
        )
        imported_count += len(elements)

    figures_changed = update_figure_index(document)
    annex_entry_added = add_annex_index_entry(document)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
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

    return {
        "elements": imported_count,
        "figure_index": figures_changed,
        "annex_index": int(annex_entry_added),
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    result = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Elementos importados: {result['elements']}")
    print(f"Entradas de figuras actualizadas: {result['figure_index']}")
    print(f"Entrada local do Anexo D acrescentada: {result['annex_index']}")


if __name__ == "__main__":
    main()
