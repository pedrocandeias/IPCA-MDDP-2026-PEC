#!/usr/bin/env python3
"""Ler células não vazias de uma folha XLSX sem dependências externas."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN, "r": REL, "pr": PACKAGE_REL}


def column_number(reference: str) -> int:
    letters = re.match(r"[A-Z]+", reference).group(0)
    value = 0
    for letter in letters:
        value = value * 26 + ord(letter) - 64
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xlsx", type=Path)
    parser.add_argument("--sheet", default="Sheet1")
    args = parser.parse_args()

    with ZipFile(args.xlsx) as archive:
        workbook = etree.fromstring(archive.read("xl/workbook.xml"))
        relationships = etree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        target_by_id = {
            item.get("Id"): item.get("Target")
            for item in relationships.findall(f"{{{PACKAGE_REL}}}Relationship")
        }
        sheet_nodes = workbook.xpath("//m:sheet", namespaces=NS)
        sheet = next((node for node in sheet_nodes if node.get("name") == args.sheet), None)
        if sheet is None:
            names = ", ".join(node.get("name") for node in sheet_nodes)
            raise SystemExit(f"Folha {args.sheet!r} inexistente. Disponíveis: {names}")
        target = target_by_id[sheet.get(f"{{{REL}}}id")]
        sheet_path = "xl/" + target.lstrip("/")

        shared: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = etree.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = ["".join(item.itertext()) for item in strings.xpath("//m:si", namespaces=NS)]

        worksheet = etree.fromstring(archive.read(sheet_path))
        for row in worksheet.xpath("//m:sheetData/m:row", namespaces=NS):
            values: list[tuple[int, str, str]] = []
            for cell in row.findall(f"{{{MAIN}}}c"):
                value_node = cell.find(f"{{{MAIN}}}v")
                formula_node = cell.find(f"{{{MAIN}}}f")
                value = "" if value_node is None else (value_node.text or "")
                if cell.get("t") == "s" and value:
                    value = shared[int(value)]
                formula = "" if formula_node is None else (formula_node.text or "")
                if value or formula:
                    values.append((column_number(cell.get("r")), value, formula))
            if values:
                rendered = " | ".join(
                    f"{column}: {value}" + (f" [={formula}]" if formula else "")
                    for column, value, formula in values
                )
                print(f"linha {row.get('r')}: {rendered}")


if __name__ == "__main__":
    main()
