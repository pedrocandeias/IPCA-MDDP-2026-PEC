#!/usr/bin/env python3
"""Synchronise static DOCX indexes with the printed pages of a PDF export.

The IPCA document contains static contents, table and figure lists. This tool
matches each index title against the body text extracted with ``pdftotext
-layout`` and writes the printed page number back to the two-run index entry.
It also applies the final widths to Table 4.9.
"""

from __future__ import annotations

import argparse
import os
import tempfile
import unicodedata
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).casefold()
    return "".join(character for character in text if character.isalnum())


def update_table_49_widths(root: etree._Element) -> None:
    captions = [
        p for p in root.xpath(".//w:p", namespaces=NS)
        if text_of(p) == "Tabela 4.9 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados"
    ]
    if len(captions) != 1:
        raise RuntimeError(f"Expected one Table 4.9 caption; found {len(captions)}")
    table = captions[0].getnext()
    if table is None or table.tag != qn("tbl"):
        raise RuntimeError("Table 4.9 does not follow its caption")
    widths = [1650, 1950, 900, 1500, 3100]
    grid_columns = table.xpath("./w:tblGrid/w:gridCol", namespaces=NS)
    if len(grid_columns) != len(widths):
        raise RuntimeError("Unexpected Table 4.9 column count")
    for column, width in zip(grid_columns, widths, strict=True):
        column.set(qn("w"), str(width))
    for row in table.xpath("./w:tr", namespaces=NS):
        cells = row.xpath("./w:tc", namespaces=NS)
        if len(cells) != len(widths):
            raise RuntimeError("Unexpected Table 4.9 row shape")
        for cell, width in zip(cells, widths, strict=True):
            cell_width = cell.find("./w:tcPr/w:tcW", namespaces=NS)
            if cell_width is None:
                raise RuntimeError("Missing Table 4.9 cell width")
            cell_width.set(qn("w"), str(width))


def apply(document_xml: bytes, extracted_pdf: str, page_offset: int) -> tuple[bytes, int, list[str]]:
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(document_xml, parser)
    pages = extracted_pdf.split("\f")
    normalised_pages = [normalise(page) for page in pages]

    updated = 0
    unmatched: list[str] = []
    for paragraph in root.xpath("//w:body/w:p", namespaces=NS):
        style = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if not style or not style[0].startswith("ndice") or len(text_nodes) != 2:
            continue
        title = text_nodes[0].text or ""
        old_page = text_nodes[1].text or ""
        if not old_page.isdigit():
            continue
        needle = normalise(title)
        hits = [
            physical_page for physical_page, page in enumerate(normalised_pages, start=1)
            if physical_page > page_offset and needle and needle in page
        ]
        if not hits:
            # The title page and Chapter 1 heading are visually present but are
            # not emitted as searchable PDF text; their existing page 1 is valid.
            unmatched.append(title)
            continue
        if style[0].startswith("ndiceAnexo"):
            # A local annex index repeats the title before the body heading.
            # The first hit is therefore the local index itself and the second
            # hit is the section heading whose page must be reported.
            if len(hits) < 2:
                unmatched.append(title)
                continue
            physical_page = hits[1]
        else:
            physical_page = min(hits)
        printed_page = physical_page - page_offset
        if printed_page < 1:
            raise RuntimeError(f"Invalid printed page for {title!r}: {printed_page}")
        value = str(printed_page)
        if text_nodes[1].text != value:
            text_nodes[1].text = value
            updated += 1

    update_table_49_widths(root)
    return (
        etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes"),
        updated,
        unmatched,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("pdf_text", type=Path, help="Output of pdftotext -layout")
    parser.add_argument("--page-offset", type=int, default=19)
    args = parser.parse_args()
    path = args.docx.resolve()
    with ZipFile(path, "r") as archive:
        document_xml = archive.read("word/document.xml")
    updated_xml, count, unmatched = apply(
        document_xml,
        args.pdf_text.read_text(encoding="utf-8", errors="replace"),
        args.page_offset,
    )

    fd, temporary = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    try:
        with ZipFile(path, "r") as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                data = updated_xml if item.filename == "word/document.xml" else source.read(item.filename)
                target.writestr(item, data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

    print(f"Updated index entries: {count}")
    print("Unmatched entries retained:")
    for title in unmatched:
        print(f"- {title}")


if __name__ == "__main__":
    main()
