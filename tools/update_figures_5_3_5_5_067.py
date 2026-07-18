#!/usr/bin/env python3
"""Substitui as Figuras 5.3–5.5 sem alterar o conteúdo XML do DOCX."""

from __future__ import annotations

import hashlib
import os
import struct
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

MEDIA = {
    "word/media/image19.png": (
        ROOT / "figuras/arquitectura_plataforma_parametrica.png",
        (3375, 2025),
    ),
    "word/media/image20.png": (
        ROOT / "figuras/sequencia_perfil_ia_openscad_exportacao.png",
        (1809, 1572),
    ),
    "word/media/image21.png": (
        ROOT / "figuras/figura_5_5_fluxo_producao_personalizada.png",
        (2337, 1194),
    ),
}

PROTECTED_PARTS = (
    "word/document.xml",
    "word/_rels/document.xml.rels",
    "word/footnotes.xml",
    "word/comments.xml",
)

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def png_dimensions(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise RuntimeError("Ficheiro PNG inválido")
    return struct.unpack(">II", data[16:24])


def annotation_counts(entries: dict[str, bytes]) -> tuple[int, int]:
    footnotes = etree.fromstring(entries["word/footnotes.xml"])
    comments = etree.fromstring(entries["word/comments.xml"])
    footnote_count = sum(
        1
        for node in footnotes.xpath("//w:footnote", namespaces=NS)
        if int(node.get(f"{{{NS['w']}}}id")) > 0
    )
    comment_count = len(comments.xpath("//w:comment", namespaces=NS))
    return footnote_count, comment_count


def main() -> None:
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    missing = [name for name in (*MEDIA, *PROTECTED_PARTS) if name not in entries]
    if missing:
        raise RuntimeError(f"Partes em falta no DOCX: {', '.join(missing)}")

    protected_before = {name: digest(entries[name]) for name in PROTECTED_PARTS}
    counts_before = annotation_counts(entries)

    for media_name, (source_path, expected_dimensions) in MEDIA.items():
        image = source_path.read_bytes()
        dimensions = png_dimensions(image)
        if dimensions != expected_dimensions:
            raise RuntimeError(
                f"Dimensões inesperadas em {source_path.name}: "
                f"{dimensions}; esperado: {expected_dimensions}"
            )
        entries[media_name] = image
        print(f"Substituída: {media_name} <- {source_path.relative_to(ROOT)}")

    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w") as output:
        for info in infos:
            output.writestr(info, entries[info.filename])
    os.replace(temporary, DOCX)

    with ZipFile(DOCX) as result:
        after = {name: result.read(name) for name in result.namelist()}

    protected_after = {name: digest(after[name]) for name in PROTECTED_PARTS}
    if protected_after != protected_before:
        changed = [
            name for name in PROTECTED_PARTS
            if protected_after[name] != protected_before[name]
        ]
        raise RuntimeError(f"Partes protegidas alteradas: {', '.join(changed)}")

    counts_after = annotation_counts(after)
    if counts_after != counts_before:
        raise RuntimeError(
            f"Notas/comentários alterados: {counts_before} -> {counts_after}"
        )

    for media_name, (source_path, _) in MEDIA.items():
        if after[media_name] != source_path.read_bytes():
            raise RuntimeError(f"Imagem não sincronizada: {media_name}")

    print(
        "Partes XML preservadas; "
        f"notas de rodapé: {counts_after[0]}; comentários: {counts_after[1]}"
    )


if __name__ == "__main__":
    main()
