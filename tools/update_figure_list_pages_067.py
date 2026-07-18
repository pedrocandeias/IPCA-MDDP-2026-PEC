#!/usr/bin/env python3
"""Actualiza apenas as páginas das Figuras 5.3–5.5 na lista do DOCX."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

PAGE_UPDATES = {
    "Figura 5.3 — Arquitetura da plataforma e fronteiras entre navegador, "
    "servidor, serviço externo de IA e preparação do fabrico.": ("65", "67"),
    "Figura 5.4 — Sequência de dados e decisões desde o perfil ou descrição "
    "até à sugestão, confirmação, geração determinística e exportação.": ("66", "68"),
    "Figura 5.5 — Fluxo geral de produção personalizada de próteses a partir "
    "de digitalização, CAD adaptativo e fabrico aditivo.": ("68", "70"),
}

PROTECTED_PARTS = (
    "word/_rels/document.xml.rels",
    "word/footnotes.xml",
    "word/comments.xml",
)

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = f"{{{NS['w']}}}"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reference_ids(document: bytes) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
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

    for caption, (old_page, new_page) in PAGE_UPDATES.items():
        old_tag = f"<w:t>{old_page}</w:t>"
        new_tag = f"<w:t>{new_page}</w:t>"

        positions: list[int] = []
        search_from = 0
        while True:
            position = text.find(caption, search_from)
            if position < 0:
                break
            positions.append(position)
            search_from = position + len(caption)

        candidates: list[tuple[int, int, str]] = []
        for caption_position in positions:
            paragraph_start = text.rfind("<w:p", 0, caption_position)
            paragraph_end = text.index("</w:p>", caption_position) + len("</w:p>")
            paragraph = text[paragraph_start:paragraph_end]
            if paragraph.count(old_tag) == 1:
                candidates.append((paragraph_start, paragraph_end, paragraph))

        if len(candidates) != 1:
            raise RuntimeError(
                f"Página {old_page} não localizada de forma inequívoca para {caption}"
            )

        paragraph_start, paragraph_end, paragraph = candidates[0]
        revised_paragraph = paragraph.replace(old_tag, new_tag, 1)
        text = text[:paragraph_start] + revised_paragraph + text[paragraph_end:]
        print(f"Actualizada: {caption.split(' — ', 1)[0]} — página {old_page} -> {new_page}")

    return text.encode("utf-8")


def main() -> None:
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    required = ("word/document.xml", *PROTECTED_PARTS)
    missing = [name for name in required if name not in entries]
    if missing:
        raise RuntimeError(f"Partes em falta no DOCX: {', '.join(missing)}")

    protected_before = {name: digest(entries[name]) for name in PROTECTED_PARTS}
    references_before = reference_ids(entries["word/document.xml"])
    original_document = entries["word/document.xml"]
    entries["word/document.xml"] = update_document(original_document)

    if len(entries["word/document.xml"]) != len(original_document):
        raise RuntimeError("O tamanho de document.xml mudou para além das substituições previstas")

    references_after = reference_ids(entries["word/document.xml"])
    if references_after != references_before:
        raise RuntimeError("As referências a notas de rodapé ou comentários foram alteradas")

    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w") as output:
        for info in infos:
            output.writestr(info, entries[info.filename])
    os.replace(temporary, DOCX)

    with ZipFile(DOCX) as result:
        after = {name: result.read(name) for name in required}

    protected_after = {name: digest(after[name]) for name in PROTECTED_PARTS}
    if protected_after != protected_before:
        changed = [
            name for name in PROTECTED_PARTS
            if protected_after[name] != protected_before[name]
        ]
        raise RuntimeError(f"Partes protegidas alteradas: {', '.join(changed)}")

    if reference_ids(after["word/document.xml"]) != references_before:
        raise RuntimeError("A validação final das referências a anotações falhou")

    print(
        "Notas e comentários preservados; "
        f"referências de rodapé: {len(references_before[0])}; "
        f"comentários: {len(references_before[3])}"
    )


if __name__ == "__main__":
    main()
