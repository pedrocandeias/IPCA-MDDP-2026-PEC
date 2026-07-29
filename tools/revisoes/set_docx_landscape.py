#!/usr/bin/env python3
"""Aplicar A4 horizontal e margens adequadas a um DOCX autónomo."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def set_table_widths(table: etree._Element, widths: list[int]) -> None:
    grid = table.find(qn("tblGrid"))
    if grid is not None:
        columns = grid.findall(qn("gridCol"))
        for column, width in zip(columns, widths):
            column.set(qn("w"), str(width))

    properties = table.find(qn("tblPr"))
    if properties is None:
        properties = etree.Element(qn("tblPr"))
        table.insert(0, properties)
    table_width = properties.find(qn("tblW"))
    if table_width is None:
        table_width = etree.SubElement(properties, qn("tblW"))
    table_width.set(qn("w"), str(sum(widths)))
    table_width.set(qn("type"), "dxa")
    layout = properties.find(qn("tblLayout"))
    if layout is None:
        layout = etree.SubElement(properties, qn("tblLayout"))
    layout.set(qn("type"), "fixed")

    for row in table.findall(qn("tr")):
        for cell, width in zip(row.findall(qn("tc")), widths):
            cell_properties = cell.find(qn("tcPr"))
            if cell_properties is None:
                cell_properties = etree.Element(qn("tcPr"))
                cell.insert(0, cell_properties)
            cell_width = cell_properties.find(qn("tcW"))
            if cell_width is None:
                cell_width = etree.SubElement(cell_properties, qn("tcW"))
            cell_width.set(qn("w"), str(width))
            cell_width.set(qn("type"), "dxa")
            for run in cell.xpath(".//w:r", namespaces=NS):
                run_properties = run.find(qn("rPr"))
                if run_properties is None:
                    run_properties = etree.Element(qn("rPr"))
                    run.insert(0, run_properties)
                for size_name in ("sz", "szCs"):
                    size = run_properties.find(qn(size_name))
                    if size is None:
                        size = etree.SubElement(run_properties, qn(size_name))
                    size.set(qn("val"), "16")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--margin-mm", type=float, default=15.0)
    args = parser.parse_args()

    with ZipFile(args.docx) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    margin_twips = str(round(args.margin_mm / 25.4 * 1440))
    for section in document.xpath("//w:sectPr", namespaces=NS):
        size = section.find(qn("pgSz"))
        if size is None:
            size = etree.SubElement(section, qn("pgSz"))
        size.set(qn("w"), "16838")
        size.set(qn("h"), "11906")
        size.set(qn("orient"), "landscape")

        margins = section.find(qn("pgMar"))
        if margins is None:
            margins = etree.SubElement(section, qn("pgMar"))
        for name in ("top", "right", "bottom", "left"):
            margins.set(qn(name), margin_twips)

    width_sets = {
        10: [1800, 1200, 1400, 1900, 900, 1000, 1800, 1500, 1400, 1100],
        7: [1700, 1100, 4500, 1400, 1400, 1500, 2100],
    }
    for table in document.xpath("//w:tbl", namespaces=NS):
        rows = table.findall(qn("tr"))
        if not rows:
            continue
        column_count = len(rows[0].findall(qn("tc")))
        widths = width_sets.get(column_count)
        if widths:
            set_table_widths(table, widths)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=args.docx.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(args.docx)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
