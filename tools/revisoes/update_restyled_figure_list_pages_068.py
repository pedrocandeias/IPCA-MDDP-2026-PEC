#!/usr/bin/env python3
"""Sincroniza quatro páginas alteradas na lista de figuras da versão 0.4.68."""

from __future__ import annotations

import os
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

UPDATES = {
    "Figura 2.6 — Enquadramento de um fluxo de CAD apoiado por IA para desenvolvimento de produto.": ("22", "23"),
    "Figura 3.1 — Processo interdisciplinar de desenvolvimento de uma prótese de membro superior impressa em 3D.": ("37", "38"),
    "Figura 6.1 — Relação entre desafios de compreensão das decisões e princípios de IA responsável.": ("84", "86"),
    "Figura C.1 — Fluxo entre dados de entrada, mapa comum, regras específicas dos modelos e geometria exportável. Produção própria.": ("144", "145"),
}

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = f"{{{NS['w']}}}"


def reference_ids(document: bytes) -> tuple[tuple[str, ...], ...]:
    root = etree.fromstring(document)
    return tuple(
        tuple(node.get(f"{W}id", "") for node in root.xpath(xpath, namespaces=NS))
        for xpath in (
            "//w:footnoteReference",
            "//w:commentRangeStart",
            "//w:commentRangeEnd",
            "//w:commentReference",
        )
    )


def update_document(document: bytes) -> bytes:
    text = document.decode("utf-8")
    for caption, (old_page, new_page) in UPDATES.items():
        old_tag = f"<w:t>{old_page}</w:t>"
        new_tag = f"<w:t>{new_page}</w:t>"
        positions: list[int] = []
        start = 0
        while True:
            position = text.find(caption, start)
            if position < 0:
                break
            positions.append(position)
            start = position + len(caption)

        candidates: list[tuple[int, int, str]] = []
        for position in positions:
            paragraph_start = text.rfind("<w:p", 0, position)
            paragraph_end = text.index("</w:p>", position) + len("</w:p>")
            paragraph = text[paragraph_start:paragraph_end]
            if paragraph.count(old_tag) == 1:
                candidates.append((paragraph_start, paragraph_end, paragraph))

        if len(candidates) != 1:
            raise RuntimeError(f"Página não localizada de forma inequívoca para {caption}")
        paragraph_start, paragraph_end, paragraph = candidates[0]
        revised = paragraph.replace(old_tag, new_tag, 1)
        text = text[:paragraph_start] + revised + text[paragraph_end:]
        print(f"Actualizada: {caption.split(' — ', 1)[0]} — {old_page} -> {new_page}")
    return text.encode("utf-8")


def main() -> None:
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    original = entries["word/document.xml"]
    references = reference_ids(original)
    entries["word/document.xml"] = update_document(original)
    if len(entries["word/document.xml"]) != len(original):
        raise RuntimeError("O tamanho de document.xml mudou inesperadamente")
    if reference_ids(entries["word/document.xml"]) != references:
        raise RuntimeError("As referências a notas ou comentários foram alteradas")

    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w") as output:
        for info in infos:
            output.writestr(info, entries[info.filename])
    os.replace(temporary, DOCX)

    with ZipFile(DOCX) as result:
        after = {name: result.read(name) for name in result.namelist()}
    unexpected = [
        name for name in entries
        if name != "word/document.xml" and after[name] != entries[name]
    ]
    if unexpected:
        raise RuntimeError(f"Partes não autorizadas alteradas: {', '.join(unexpected)}")
    if reference_ids(after["word/document.xml"]) != references:
        raise RuntimeError("A validação final das anotações falhou")
    print(
        "Referências preservadas; "
        f"notas de rodapé={len(references[0])}; comentários={len(references[3])}"
    )


if __name__ == "__main__":
    main()
