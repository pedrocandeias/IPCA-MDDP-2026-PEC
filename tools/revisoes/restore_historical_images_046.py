#!/usr/bin/env python3
"""Restaura imagens históricas validadas e preserva as figuras posteriores."""

from __future__ import annotations

import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from integrate_annexes_bc import NS, element_text, paragraph_style, replace_paragraph_text


ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
HISTORICAL = ROOT / "docs/versoes/documentos-historicos/pedro-candeias-projeto-mestrado-mdddp-ipca-2026.docx"

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
IMAGE_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"

XPATH_NS = dict(NS)
XPATH_NS.update({"a": A_NS, "r": R_NS, "wp": WP_NS})

MEDIA_NAMES = {
    "source_image01.jpeg": "restored_figura_1_1.jpeg",
    "source_image03.jpeg": "restored_figura_2_2.jpeg",
    "source_image04.png": "restored_figura_2_3.png",
    "source_image09.png": "restored_figura_2_8.png",
    "source_image10.png": "restored_figura_3_1.png",
    "source_image12.png": "restored_figura_4_1.png",
    "source_image16.png": "restored_figura_5_2.png",
    "source_image17.png": "restored_figura_5_5.png",
    "source_image18.png": "restored_figura_5_7.png",
    "source_image20.png": "restored_figura_5_8a.png",
    "source_image21.png": "restored_figura_5_8b.png",
    "source_image22.png": "restored_figura_5_8c.png",
    "source_image23.png": "restored_figura_5_8d.png",
}


def relationships_by_id(root: etree._Element) -> dict[str, str]:
    return {item.get("Id"): item.get("Target") for item in root}


def next_relationship_id(root: etree._Element) -> str:
    numbers = []
    for item in root:
        value = item.get("Id", "")
        if value.startswith("rId") and value[3:].isdigit():
            numbers.append(int(value[3:]))
    return f"rId{max(numbers, default=0) + 1}"


def add_relationship(root: etree._Element, target: str) -> str:
    rel_id = next_relationship_id(root)
    item = etree.SubElement(root, f"{{{REL_NS}}}Relationship")
    item.set("Id", rel_id)
    item.set("Type", IMAGE_REL)
    item.set("Target", target)
    return rel_id


def find_paragraph(document: etree._Element, prefix: str, *, body_only: bool = True) -> etree._Element:
    xpath = "//w:body//w:p" if body_only else "//w:p"
    matches = [
        paragraph
        for paragraph in document.xpath(xpath, namespaces=NS)
        if element_text(paragraph).startswith(prefix)
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo {prefix!r}; encontrados {len(matches)}")
    return matches[0]


def previous_image_paragraph(paragraph: etree._Element) -> etree._Element:
    current = paragraph.getprevious()
    while current is not None:
        if current.xpath(".//a:blip[@r:embed]", namespaces=XPATH_NS):
            return current
        if element_text(current):
            break
        current = current.getprevious()
    raise RuntimeError(f"Imagem anterior não encontrada para {element_text(paragraph)!r}")


def max_docpr_id(document: etree._Element) -> int:
    values = [
        int(node.get("id"))
        for node in document.xpath("//wp:docPr[@id]", namespaces=XPATH_NS)
        if node.get("id", "").isdigit()
    ]
    return max(values, default=0)


def remap_images(
    element: etree._Element,
    historical_relationships: dict[str, str],
    historical_files: dict[str, bytes],
    current_relationships: etree._Element,
    current_files: dict[str, bytes],
    next_docpr: list[int],
) -> None:
    for blip in element.xpath(".//a:blip[@r:embed]", namespaces=XPATH_NS):
        old_id = blip.get(f"{{{R_NS}}}embed")
        old_target = historical_relationships[old_id]
        basename = Path(old_target).name
        new_name = MEDIA_NAMES[basename]
        new_target = f"media/{new_name}"
        current_files[f"word/{new_target}"] = historical_files[f"word/{old_target}"]
        new_id = add_relationship(current_relationships, new_target)
        blip.set(f"{{{R_NS}}}embed", new_id)

    for docpr in element.xpath(".//wp:docPr", namespaces=XPATH_NS):
        next_docpr[0] += 1
        docpr.set("id", str(next_docpr[0]))
        docpr.set("name", f"Imagem restaurada {next_docpr[0]}")


def clone_historical(
    element: etree._Element,
    historical_relationships: dict[str, str],
    historical_files: dict[str, bytes],
    current_relationships: etree._Element,
    current_files: dict[str, bytes],
    next_docpr: list[int],
) -> etree._Element:
    clone = deepcopy(element)
    remap_images(
        clone,
        historical_relationships,
        historical_files,
        current_relationships,
        current_files,
        next_docpr,
    )
    return clone


def replace_text_nodes(paragraph: etree._Element, old: str, new: str) -> bool:
    changed = False
    for node in paragraph.xpath(".//w:t", namespaces=NS):
        if node.text and old in node.text:
            node.text = node.text.replace(old, new)
            changed = True
    return changed


def renumber_chapter5(document: etree._Element) -> int:
    placeholders = {
        "Figura 5.5": "Figura 5.__7__",
        "Figura 5.4": "Figura 5.__5__",
        "Figura 5.3": "Figura 5.__4__",
        "Figura 5.2": "Figura 5.__3__",
    }
    finals = {
        "Figura 5.__7__": "Figura 5.7",
        "Figura 5.__5__": "Figura 5.5",
        "Figura 5.__4__": "Figura 5.4",
        "Figura 5.__3__": "Figura 5.3",
    }
    changed = 0
    paragraphs = document.xpath("//w:p", namespaces=NS)
    for paragraph in paragraphs:
        for old, new in placeholders.items():
            changed += int(replace_text_nodes(paragraph, old, new))
    for paragraph in paragraphs:
        for old, new in finals.items():
            replace_text_nodes(paragraph, old, new)
    return changed


def set_index_entry(paragraph: etree._Element, title: str, page: str = "—") -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if len(nodes) != 2:
        raise RuntimeError(f"Estrutura inesperada no índice: {element_text(paragraph)!r}")
    nodes[0].text = title
    nodes[1].text = page


def find_index_entry(document: etree._Element, prefix: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style(paragraph).startswith("ndice")
        and element_text(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Entrada de figuras {prefix!r}: encontradas {len(matches)}")
    return matches[0]


def add_content_type(content_types: etree._Element, extension: str, content_type: str) -> None:
    if any(
        item.get("Extension") == extension
        for item in content_types.findall(f"{{{CT_NS}}}Default")
    ):
        return
    item = etree.Element(f"{{{CT_NS}}}Default")
    item.set("Extension", extension)
    item.set("ContentType", content_type)
    content_types.insert(0, item)


def apply(current_path: Path, historical_path: Path) -> dict[str, int]:
    original_mode = current_path.stat().st_mode
    with ZipFile(current_path) as archive:
        current_files = {item.filename: archive.read(item.filename) for item in archive.infolist()}
    with ZipFile(historical_path) as archive:
        historical_files = {item.filename: archive.read(item.filename) for item in archive.infolist()}

    current_document = etree.fromstring(current_files["word/document.xml"])
    current_relationships = etree.fromstring(current_files["word/_rels/document.xml.rels"])
    content_types = etree.fromstring(current_files["[Content_Types].xml"])
    historical_document = etree.fromstring(historical_files["word/document.xml"])
    historical_rels_root = etree.fromstring(historical_files["word/_rels/document.xml.rels"])
    historical_relationships = relationships_by_id(historical_rels_root)
    next_docpr = [max_docpr_id(current_document)]

    replacements = (
        ("Figura 1.1 —", "Figura 1.1 —"),
        ("Figura 2.2 —", "Figura 2.2 —"),
        ("Figura 2.3 —", "Figura 2.3 —"),
        ("Figura 2.8 —", "Figura 2.8 —"),
        ("Figura 3.1 —", "Figura 3.1 —"),
        ("Figura 4.1 —", "Figura 4.1 —"),
        ("Figura 5.4 — Fluxo geral", "Figura 5.3 — Fluxo geral"),
    )
    replaced = 0
    for current_caption_prefix, historical_caption_prefix in replacements:
        current_caption = find_paragraph(current_document, current_caption_prefix)
        historical_caption = find_paragraph(historical_document, historical_caption_prefix)
        current_image = previous_image_paragraph(current_caption)
        historical_image = previous_image_paragraph(historical_caption)
        replacement = clone_historical(
            historical_image,
            historical_relationships,
            historical_files,
            current_relationships,
            current_files,
            next_docpr,
        )
        current_image.addprevious(replacement)
        current_image.getparent().remove(current_image)
        replaced += 1

    renumbered = renumber_chapter5(current_document)

    # Reintegrar a Figura 5.2 no final da descrição dos três perfis.
    profile_anchor = find_paragraph(current_document, "O perfil de administrador assegura")
    historical_profile_caption = find_paragraph(
        historical_document,
        "Figura 5.2 — Painel de configuração do perfil de utilizador",
    )
    profile_figure = clone_historical(
        historical_profile_caption,
        historical_relationships,
        historical_files,
        current_relationships,
        current_files,
        next_docpr,
    )
    replace_text_nodes(
        profile_figure,
        "Figura 5.2 — Painel de configuração do perfil de utilizador na plataforma – Hand Fab",
        "Figura 5.2 — Painel de configuração dos perfis de utilizador na plataforma HandFab.",
    )
    profile_source = deepcopy(historical_profile_caption.getnext())
    replace_paragraph_text(profile_source, "Fonte: produção própria.")
    profile_anchor.addnext(profile_source)
    profile_anchor.addnext(profile_figure)

    # Reintegrar a visualização do código como Figura 5.7 antes da Secção 5.4.
    section_54 = find_paragraph(current_document, "5.4 Estrutura funcional da plataforma")
    historical_code_caption = find_paragraph(historical_document, "Figura 5.4 —  Modelo paramétrico")
    historical_code_image = previous_image_paragraph(historical_code_caption)
    code_narrative = deepcopy(profile_anchor)
    replace_paragraph_text(
        code_narrative,
        "A Figura 5.6 documenta a relação entre o código OpenSCAD apresentado na plataforma e a geometria tridimensional produzida a partir da configuração activa.",
    )
    code_image = clone_historical(
        historical_code_image,
        historical_relationships,
        historical_files,
        current_relationships,
        current_files,
        next_docpr,
    )
    code_caption = deepcopy(historical_code_caption)
    replace_paragraph_text(
        code_caption,
        "Figura 5.6 — Visualização do código OpenSCAD e da geometria correspondente na plataforma HandFab.",
    )
    code_source = deepcopy(historical_code_caption.getnext())
    replace_paragraph_text(code_source, "Fonte: produção própria.")
    for element in (code_narrative, code_image, code_caption, code_source):
        section_54.addprevious(element)

    # Reintegrar as quatro vistas de configuração como Figura 5.8.
    figure_56_caption = find_paragraph(current_document, "Figura 5.6 — Ferramenta paramétrica")
    figure_56_source = figure_56_caption.getnext()
    historical_gallery_caption = find_paragraph(historical_document, "Figura 5.4 — Ferramentas para edição")
    historical_gallery = historical_gallery_caption.getprevious()
    gallery_count = len(
        historical_gallery.xpath(".//a:blip[@r:embed]", namespaces=XPATH_NS)
    )
    if gallery_count != 4:
        raise RuntimeError(f"Esperadas quatro imagens na galeria histórica; encontradas {gallery_count}")
    gallery_narrative = deepcopy(profile_anchor)
    replace_paragraph_text(
        gallery_narrative,
        "As vistas reunidas na Figura 5.8 documentam a selecção do modelo e diferentes grupos de controlos disponibilizados pela interface de configuração.",
    )
    gallery_caption = deepcopy(historical_gallery_caption)
    replace_paragraph_text(
        gallery_caption,
        "Figura 5.8 — Interface de selecção, configuração paramétrica e materiais da plataforma HandFab.",
    )
    gallery_source = deepcopy(historical_gallery_caption.getnext())
    replace_paragraph_text(gallery_source, "Fonte: produção própria.")
    insertion = figure_56_source
    gallery = clone_historical(
        historical_gallery,
        historical_relationships,
        historical_files,
        current_relationships,
        current_files,
        next_docpr,
    )
    for element in [gallery_narrative, gallery, gallery_caption, gallery_source]:
        insertion.addnext(element)
        insertion = element

    # Acrescentar as três novas entradas à lista estática de figuras.
    index_51 = find_index_entry(current_document, "Figura 5.1 —")
    index_52 = deepcopy(index_51)
    set_index_entry(index_52, "Figura 5.2 — Painel de configuração dos perfis de utilizador na plataforma HandFab.")
    index_51.addnext(index_52)

    index_57 = find_index_entry(current_document, "Figura 5.7 —")
    index_56 = deepcopy(index_57)
    set_index_entry(index_56, "Figura 5.6 — Visualização do código OpenSCAD e da geometria correspondente na plataforma HandFab.")
    index_58 = deepcopy(index_57)
    set_index_entry(index_58, "Figura 5.8 — Interface de selecção, configuração paramétrica e materiais da plataforma HandFab.")
    index_57.addprevious(index_56)
    index_57.addnext(index_58)

    add_content_type(content_types, "jpeg", "image/jpeg")
    add_content_type(content_types, "jpg", "image/jpeg")

    current_files["word/document.xml"] = etree.tostring(
        current_document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    current_files["word/_rels/document.xml.rels"] = etree.tostring(
        current_relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    current_files["[Content_Types].xml"] = etree.tostring(
        content_types, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=current_path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in current_files.items():
                output.writestr(name, data)
        temporary.replace(current_path)
        os.chmod(current_path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return {
        "replaced": replaced,
        "renumbered": renumbered,
        "inserted_groups": 3,
    }


def fix_existing_order(current_path: Path) -> None:
    """Corrige a ordem 5.6/5.7 numa execução já restaurada."""
    original_mode = current_path.stat().st_mode
    with ZipFile(current_path) as archive:
        files = {item.filename: archive.read(item.filename) for item in archive.infolist()}
    document = etree.fromstring(files["word/document.xml"])

    paragraphs = document.xpath("//w:p", namespaces=NS)
    for paragraph in paragraphs:
        replace_text_nodes(paragraph, "Figura 5.6", "Figura 5.__swap__")
    for paragraph in paragraphs:
        replace_text_nodes(paragraph, "Figura 5.7", "Figura 5.6")
    for paragraph in paragraphs:
        replace_text_nodes(paragraph, "Figura 5.__swap__", "Figura 5.7")

    index_56 = find_index_entry(document, "Figura 5.6 —")
    index_57 = find_index_entry(document, "Figura 5.7 —")
    index_57.addprevious(index_56)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=current_path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(current_path)
        os.chmod(current_path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--fix-order-only", action="store_true")
    args = parser.parse_args()
    if args.fix_order_only:
        fix_existing_order(CURRENT)
        print(f"Ordem das Figuras 5.6 e 5.7 corrigida: {CURRENT}")
        return
    result = apply(CURRENT, HISTORICAL)
    print(f"DOCX actualizado: {CURRENT}")
    print(f"Imagens substituídas: {result['replaced']}")
    print(f"Referências do Capítulo 5 renumeradas: {result['renumbered']}")
    print(f"Grupos históricos reintegrados: {result['inserted_groups']}")


if __name__ == "__main__":
    main()
