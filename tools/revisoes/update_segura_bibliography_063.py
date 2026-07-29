#!/usr/bin/env python3
"""Synchronise the Segura et al. bibliography URL in the canonical DOCX."""

from __future__ import annotations

import os
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD = (
    "https://www.mdpi.com/2673-1592/6/2/22/pdf?version=1710818539"
).encode()
NEW = "https://doi.org/10.3390/prosthesis6020022".encode()


def main() -> int:
    with zipfile.ZipFile(DOCX) as source:
        document_xml = source.read("word/document.xml")
        old_count = document_xml.count(OLD)
        new_count = document_xml.count(NEW)

        if old_count == 0 and new_count == 1:
            print("Segura et al. bibliography entry already synchronised.")
            return 0
        if old_count != 1 or new_count != 0:
            raise RuntimeError(
                f"Expected one old URL and no canonical DOI; found old={old_count}, new={new_count}"
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
