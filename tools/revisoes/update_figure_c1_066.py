#!/usr/bin/env python3
"""Substitui a Figura C.1 nos DOCX que incorporam o Anexo C."""

from __future__ import annotations

import os
import struct
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
PNG = ROOT / "componentes/figuras/figura_c1_fluxo_adaptacao_parametrica.png"

TARGETS = {
    ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx":
        "word/media/image34.png",
    ROOT / "componentes/anexos/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.docx":
        "word/media/image1.png",
}

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def png_dimensions(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise RuntimeError(f"Imagem inválida: {PNG}")
    return struct.unpack(">II", data[16:24])


def replace_media(path: Path, media_name: str, image: bytes) -> None:
    with ZipFile(path) as source:
        entries = {item.filename: source.read(item.filename) for item in source.infolist()}

    if media_name not in entries:
        raise RuntimeError(f"{media_name} não existe em {path.relative_to(ROOT)}")

    entries[media_name] = image

    if path.parent == ROOT:
        document = etree.fromstring(entries["word/document.xml"])
        page_entries = 0
        for paragraph in document.xpath("//w:p", namespaces=NS):
            nodes = paragraph.xpath(".//w:t", namespaces=NS)
            text = "".join(node.text or "" for node in nodes)
            if "Figura C.1" not in text:
                continue
            for node in nodes:
                if node.text in {"143", "144"}:
                    node.text = "144"
                    page_entries += 1
        if page_entries != 1:
            raise RuntimeError(
                f"Esperada uma entrada paginada da Figura C.1; encontradas: {page_entries}"
            )
        entries["word/document.xml"] = etree.tostring(
            document, xml_declaration=True, encoding="UTF-8", standalone="yes"
        )
    temporary = path.with_suffix(path.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for filename, data in entries.items():
            output.writestr(filename, data)
    os.replace(temporary, path)
    print(f"Figura substituída: {path.relative_to(ROOT)} -> {media_name}")


def main() -> None:
    image = PNG.read_bytes()
    dimensions = png_dimensions(image)
    if dimensions != (1800, 1035):
        raise RuntimeError(f"Dimensões inesperadas: {dimensions}; esperado: (1800, 1035)")

    for path, media_name in TARGETS.items():
        replace_media(path, media_name, image)


if __name__ == "__main__":
    main()
