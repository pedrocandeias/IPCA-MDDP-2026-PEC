#!/usr/bin/env python3
"""Integra sete figuras revistas sem alterar o XML dos documentos."""

from __future__ import annotations

import hashlib
import os
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from lxml import etree
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
ANNEX = ROOT / "anexos/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.docx"

CANONICAL_MEDIA = {
    "word/media/image5.jpeg": (
        ROOT / "figuras/figura_2_2_utilizacao_rejeicao_proteses_estilizada.jpeg",
        (2160, 1458),
    ),
    "word/media/image6.png": (
        ROOT / "figuras/figura_2_3_fluxo_digital_proteses_estilizada.png",
        (2394, 1623),
    ),
    "word/media/image9.png": (
        ROOT / "figuras/figura_2_6_fluxo_cad_ia_estilizado.png",
        (2608, 1124),
    ),
    "word/media/image10.png": (
        ROOT / "figuras/figura_2_7_participacao_cocriacao_estilizada.png",
        (2032, 1048),
    ),
    "word/media/image12.png": (
        ROOT / "figuras/figura_3_1_processo_interdisciplinar_estilizada.png",
        (2070, 744),
    ),
    "word/media/image28.png": (
        ROOT / "figuras/figura_6_1_ia_responsavel_estilizada.png",
        (2782, 978),
    ),
    "word/media/image34.png": (
        ROOT / "figuras/figura_c1_fluxo_adaptacao_parametrica.png",
        (1800, 1035),
    ),
}

ANNEX_MEDIA = {
    "word/media/image1.png": (
        ROOT / "figuras/figura_c1_fluxo_adaptacao_parametrica.png",
        (1800, 1035),
    ),
}

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = f"{{{NS['w']}}}"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dimensions(data: bytes) -> tuple[int, int]:
    with Image.open(BytesIO(data)) as image:
        return image.size


def annotation_state(entries: dict[str, bytes]) -> dict[str, object]:
    state: dict[str, object] = {}
    document = etree.fromstring(entries["word/document.xml"])
    for name, xpath in (
        ("footnote_references", "//w:footnoteReference"),
        ("comment_starts", "//w:commentRangeStart"),
        ("comment_ends", "//w:commentRangeEnd"),
        ("comment_references", "//w:commentReference"),
    ):
        state[name] = tuple(
            node.get(f"{W}id", "") for node in document.xpath(xpath, namespaces=NS)
        )

    if "word/footnotes.xml" in entries:
        footnotes = etree.fromstring(entries["word/footnotes.xml"])
        state["footnotes"] = tuple(
            node.get(f"{W}id", "")
            for node in footnotes.xpath("//w:footnote", namespaces=NS)
            if int(node.get(f"{W}id", "-1")) > 0
        )
    if "word/comments.xml" in entries:
        comments = etree.fromstring(entries["word/comments.xml"])
        state["comments"] = tuple(
            node.get(f"{W}id", "")
            for node in comments.xpath("//w:comment", namespaces=NS)
        )
    return state


def replace_media(docx: Path, replacements: dict[str, tuple[Path, tuple[int, int]]]) -> None:
    with ZipFile(docx) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    missing = [name for name in ("word/document.xml", *replacements) if name not in entries]
    if missing:
        raise RuntimeError(f"Partes em falta em {docx.name}: {', '.join(missing)}")

    before = dict(entries)
    annotations_before = annotation_state(before)

    for media_name, (source_path, expected_dimensions) in replacements.items():
        image = source_path.read_bytes()
        actual_dimensions = dimensions(image)
        if actual_dimensions != expected_dimensions:
            raise RuntimeError(
                f"Dimensões inesperadas em {source_path.name}: "
                f"{actual_dimensions}; esperado: {expected_dimensions}"
            )
        entries[media_name] = image
        print(f"Substituída em {docx.name}: {media_name} <- {source_path.relative_to(ROOT)}")

    temporary = docx.with_suffix(docx.suffix + ".tmp")
    with ZipFile(temporary, "w") as output:
        for info in infos:
            output.writestr(info, entries[info.filename])
    os.replace(temporary, docx)

    with ZipFile(docx) as result:
        after = {name: result.read(name) for name in result.namelist()}

    if set(after) != set(before):
        raise RuntimeError(f"A estrutura ZIP foi alterada em {docx.name}")

    unexpected = [
        name for name in before
        if name not in replacements and after[name] != before[name]
    ]
    if unexpected:
        raise RuntimeError(
            f"Partes não autorizadas alteradas em {docx.name}: {', '.join(unexpected)}"
        )

    if annotation_state(after) != annotations_before:
        raise RuntimeError(f"Notas ou comentários alterados em {docx.name}")

    for media_name, (source_path, _) in replacements.items():
        if after[media_name] != source_path.read_bytes():
            raise RuntimeError(f"Imagem não sincronizada: {media_name}")

    state = annotation_state(after)
    print(
        f"Validado: {docx.name}; "
        f"notas={len(state.get('footnotes', ()))}, "
        f"comentários={len(state.get('comments', ()))}, "
        f"document.xml={digest(after['word/document.xml'])}"
    )


def main() -> None:
    replace_media(CANONICAL, CANONICAL_MEDIA)
    replace_media(ANNEX, ANNEX_MEDIA)


if __name__ == "__main__":
    main()
