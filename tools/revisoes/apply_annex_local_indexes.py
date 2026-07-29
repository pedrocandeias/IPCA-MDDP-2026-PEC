#!/usr/bin/env python3
"""Move detailed annex entries from the main contents to local annex indexes.

The IPCA DOCX uses static contents paragraphs.  This transformation keeps only
the three annex title entries in the main contents, copies each annex's
detailed entries immediately after its body title, and starts the annex body on
a new page after the local index.  Page numbers are synchronised after PDF
generation with ``tools/manutencao/synchronise_docx_pagination.py``.
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


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def style_of(paragraph: etree._Element) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return values[0] if values else ""


def ensure_ppr(paragraph: etree._Element) -> etree._Element:
    ppr = paragraph.find(qn("pPr"))
    if ppr is None:
        ppr = etree.Element(qn("pPr"))
        paragraph.insert(0, ppr)
    return ppr


def set_style(paragraph: etree._Element, style_id: str) -> None:
    ppr = ensure_ppr(paragraph)
    node = ppr.find(qn("pStyle"))
    if node is None:
        node = etree.Element(qn("pStyle"))
        ppr.insert(0, node)
    node.set(qn("val"), style_id)


def set_page_break_before(paragraph: etree._Element) -> None:
    ppr = ensure_ppr(paragraph)
    if ppr.find(qn("pageBreakBefore")) is None:
        ppr.append(etree.Element(qn("pageBreakBefore")))


def make_local_title(letter: str) -> etree._Element:
    paragraph = etree.Element(qn("p"))
    ppr = etree.SubElement(paragraph, qn("pPr"))
    style = etree.SubElement(ppr, qn("pStyle"))
    style.set(qn("val"), "TextoNormal-IPCA")
    keep_next = etree.SubElement(ppr, qn("keepNext"))
    keep_next.set(qn("val"), "1")
    spacing = etree.SubElement(ppr, qn("spacing"))
    spacing.set(qn("before"), "240")
    spacing.set(qn("after"), "160")
    run = etree.SubElement(paragraph, qn("r"))
    rpr = etree.SubElement(run, qn("rPr"))
    etree.SubElement(rpr, qn("b"))
    size = etree.SubElement(rpr, qn("sz"))
    size.set(qn("val"), "28")
    size_cs = etree.SubElement(rpr, qn("szCs"))
    size_cs.set(qn("val"), "28")
    text = etree.SubElement(run, qn("t"))
    text.text = f"Índice do Anexo {letter}"
    return paragraph


def add_local_index_styles(styles_root: etree._Element) -> None:
    existing = {
        style.get(qn("styleId")): style
        for style in styles_root.xpath("//w:style", namespaces=NS)
    }
    for level in (2, 3, 4, 5):
        target_id = f"ndiceAnexo{level}"
        if target_id in existing:
            continue
        source_id = f"ndice{level}"
        source = existing.get(source_id)
        if source is None:
            raise RuntimeError(f"Missing paragraph style {source_id}")
        clone = deepcopy(source)
        clone.set(qn("styleId"), target_id)
        names = clone.xpath("./w:name", namespaces=NS)
        if names:
            names[0].set(qn("val"), f"Índice do Anexo {level}")
        styles_root.append(clone)


def find_main_annex_entry(body: etree._Element, letter: str) -> etree._Element:
    prefix = f"Anexo {letter} —"
    matches = [
        paragraph
        for paragraph in body.findall(qn("p"))
        if style_of(paragraph) == "ndice1" and text_of(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one main contents entry for {prefix}; found {len(matches)}")
    return matches[0]


def extract_detail_entries(body: etree._Element, letter: str) -> list[etree._Element]:
    anchor = find_main_annex_entry(body, letter)
    entries: list[etree._Element] = []
    sibling = anchor.getnext()
    while sibling is not None and sibling.tag == qn("p"):
        title = text_of(sibling)
        style = style_of(sibling)
        if not style.startswith("ndice") or not title.startswith(f"{letter}."):
            break
        following = sibling.getnext()
        entries.append(deepcopy(sibling))
        body.remove(sibling)
        sibling = following
    if not entries:
        raise RuntimeError(f"No detailed main contents entries found for Annex {letter}")
    return entries


def find_body_annex_title(body: etree._Element, letter: str) -> etree._Element:
    prefix = f"Anexo {letter} —"
    matches = [
        paragraph
        for paragraph in body.findall(qn("p"))
        if style_of(paragraph) == "TtulosPrembulo-IPCA"
        and text_of(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one body title for {prefix}; found {len(matches)}")
    return matches[0]


def insert_local_index(
    body: etree._Element,
    letter: str,
    entries: list[etree._Element],
) -> None:
    title = find_body_annex_title(body, letter)
    first_content = title.getnext()
    if first_content is None or first_content.tag != qn("p"):
        raise RuntimeError(f"Annex {letter} has no paragraph after its title")
    if text_of(first_content).startswith("Índice do Anexo"):
        raise RuntimeError(f"Annex {letter} already contains a local index")

    position = body.index(title) + 1
    local_title = make_local_title(letter)
    body.insert(position, local_title)
    position += 1

    for entry in entries:
        source_style = style_of(entry)
        level_text = source_style.removeprefix("ndice")
        if not level_text.isdigit():
            raise RuntimeError(f"Unexpected contents style {source_style}")
        level = min(max(int(level_text), 2), 5)
        set_style(entry, f"ndiceAnexo{level}")
        body.insert(position, entry)
        position += 1

    set_page_break_before(first_content)


def update_version(document: etree._Element, version: str) -> None:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if text_of(paragraph).startswith("Versão do documento:")
    ]
    if not matches:
        return
    if len(matches) != 1:
        raise RuntimeError("Unexpected number of manuscript version paragraphs")
    nodes = matches[0].xpath(".//w:t", namespaces=NS)
    if not nodes:
        raise RuntimeError("Version paragraph contains no text node")
    nodes[0].text = f"Versão do documento: {version}"
    for node in nodes[1:]:
        node.text = ""


def apply(path: Path, version: str) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path, "r") as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    styles = etree.fromstring(files["word/styles.xml"])
    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("DOCX has no body")

    if any(
        text_of(paragraph).startswith("Índice do Anexo")
        for paragraph in body.findall(qn("p"))
    ):
        raise RuntimeError("The DOCX already contains local annex indexes")

    add_local_index_styles(styles)
    counts: dict[str, int] = {}
    for letter in ("A", "B", "C"):
        entries = extract_detail_entries(body, letter)
        insert_local_index(body, letter, entries)
        counts[letter] = len(entries)
    update_version(document, version)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/styles.xml"] = etree.tostring(
        styles, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

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
    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--version", default="0.4.39")
    args = parser.parse_args()
    path = args.docx.resolve()
    counts = apply(path, args.version)
    print(f"Updated DOCX: {path}")
    for letter, count in counts.items():
        print(f"Annex {letter}: {count} local contents entries")


if __name__ == "__main__":
    main()
