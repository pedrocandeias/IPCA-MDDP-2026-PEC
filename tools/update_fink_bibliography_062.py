#!/usr/bin/env python3
"""Synchronise the Fink and Diamond bibliography metadata in the DOCX."""

from __future__ import annotations

import os
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD = (
    "Fink, C., &amp; Diamond, Y. (2023). Prosthesis options and management in upper "
    "extremity amputation. https://www.semanticscholar.org/paper/"
    "3532a770446eb6144ef25a6b0162d1f98b61e0ff"
).encode()

NEW = (
    "Fink, C., &amp; Diamond, Y. (2023). Prosthesis options and management in upper "
    "extremity amputation. Operative Techniques in Orthopaedics, 33(3), 101061. "
    "https://doi.org/10.1016/j.oto.2023.101061"
).encode()


def main() -> int:
    with zipfile.ZipFile(DOCX) as source:
        document_xml = source.read("word/document.xml")
        old_count = document_xml.count(OLD)
        new_count = document_xml.count(NEW)

        if old_count == 0 and new_count == 1:
            print("Fink and Diamond bibliography entry already synchronised.")
            return 0
        if old_count != 1 or new_count != 0:
            raise RuntimeError(
                f"Expected one old entry and no new entry; found old={old_count}, new={new_count}"
            )

        updated_xml = document_xml.replace(OLD, NEW, 1)
        with tempfile.NamedTemporaryFile(
            prefix=f".{DOCX.stem}-", suffix=".docx", dir=DOCX.parent, delete=False
        ) as handle:
            temporary = Path(handle.name)

        try:
            with zipfile.ZipFile(temporary, "w") as target:
                for item in source.infolist():
                    data = updated_xml if item.filename == "word/document.xml" else source.read(item)
                    target.writestr(item, data)
            os.replace(temporary, DOCX)
        finally:
            temporary.unlink(missing_ok=True)

    print(f"Updated {DOCX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
