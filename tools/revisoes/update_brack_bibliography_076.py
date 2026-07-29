#!/usr/bin/env python3
"""Corrige a referência de Brack e Amalu no Markdown e no DOCX canónicos."""

from __future__ import annotations

import html
import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

OLD = (
    "Brack, T., & Amalu, E. H. (2021). A review of technology, materials and R&D "
    "challenges of upper limb prosthesis for improved user suitability. Journal of "
    "Orthopaedics, 24, 88-96. https://doi.org/10.1016/j.jor.2021.03.011"
)
NEW = (
    "Brack, R., & Amalu, E. H. (2021). A review of technology, materials and R&D "
    "challenges of upper limb prosthesis for improved user suitability. Journal of "
    "Orthopaedics, 23, 88-96. https://doi.org/10.1016/j.jor.2020.12.009"
)


def xml_text(value: str) -> bytes:
    return html.escape(value, quote=False).encode("utf-8")


def state(xml: bytes) -> dict[str, int]:
    root = etree.fromstring(xml)
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def main() -> None:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count("Versão do documento: 0.4.75") != 1:
        raise RuntimeError("A versão de origem do Markdown não é 0.4.75")
    if markdown.count(OLD) != 1:
        raise RuntimeError("A entrada antiga de Brack e Amalu não é única no Markdown")

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    document = entries["word/document.xml"]
    if document.count(xml_text(OLD)) != 1:
        raise RuntimeError("A entrada antiga de Brack e Amalu não é única no DOCX")
    before_state = state(document)
    other_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }

    markdown = markdown.replace(OLD, NEW, 1).replace(
        "Versão do documento: 0.4.75", "Versão do documento: 0.4.76", 1
    )
    document = document.replace(xml_text(OLD), xml_text(NEW), 1)
    if state(document) != before_state:
        raise RuntimeError("A contagem de notas, comentários ou imagens foi alterada")
    entries["word/document.xml"] = document

    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if result_hashes != other_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Referência de Brack e Amalu corrigida; "
        f"notas={before_state['footnotes']}, comentários={before_state['comments']}, "
        f"imagens={before_state['drawings']}"
    )


if __name__ == "__main__":
    main()
