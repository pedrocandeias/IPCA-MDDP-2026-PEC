#!/usr/bin/env python3
"""Uniformiza a terminologia dos limites dimensionais nos DOCX canónicos."""

from __future__ import annotations

import os
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
PNG = ROOT / "figuras/figura_c1_fluxo_adaptacao_parametrica.png"

TARGETS = {
    ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx": "word/media/image34.png",
    ROOT / "sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.docx": "word/media/image1.png",
}

REPLACEMENTS = {
    "escala global limitada por um piso": "escala global limitada por um valor mínimo",
    "Perfis inferiores a 82 mm ficam no piso": "Perfis inferiores a 82 mm atingem o limite mínimo",
    "valores positivos continuam sujeitos ao piso de 100%": "valores positivos continuam sujeitos ao limite mínimo de 100%",
    "HandPerc_override permitia ao Phoenix contornar o piso de 100%": "HandPerc_override permitia ao Phoenix contornar o limite mínimo de 100%",
    "Aplicação do mesmo limite de 100%–160% aos dois percursos": "Aplicação do mesmo intervalo de 100%–160% aos dois percursos",
    "C.6.2 Escala global e piso dimensional": "C.6.2 Escala global e limite dimensional mínimo",
    "valores positivos ficam sujeitos ao mesmo piso de 100% e tecto de 160%": "valores positivos ficam sujeitos ao mesmo limite mínimo de 100% e ao limite máximo de 160%",
    "uma entrada é reduzida ao piso do modelo": "uma entrada é fixada no limite mínimo do modelo",
}

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def update_docx(path: Path, media_name: str) -> None:
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    counts = {old: 0 for old in REPLACEMENTS}

    for node in document.xpath("//w:t", namespaces=NS):
        if not node.text:
            continue
        for old, new in REPLACEMENTS.items():
            occurrences = node.text.count(old)
            if occurrences:
                node.text = node.text.replace(old, new)
                counts[old] += occurrences

    full_text = " ".join(document.xpath("//w:t/text()", namespaces=NS))
    if re.search(r"\b(?:piso|pisos|tecto|tectos)\b", full_text, flags=re.IGNORECASE):
        raise RuntimeError(f"Terminologia antiga ainda presente em {path}")
    if not any(counts.values()):
        raise RuntimeError(f"Nenhuma substituição efectuada em {path}")
    if media_name not in files:
        raise RuntimeError(f"Imagem {media_name} inexistente em {path}")

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files[media_name] = PNG.read_bytes()

    temporary = path.with_suffix(path.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for filename, data in files.items():
            output.writestr(filename, data)
    os.replace(temporary, path)

    summary = ", ".join(str(value) for value in counts.values() if value)
    print(f"Actualizado: {path.relative_to(ROOT)} ({summary} ocorrências por expressão)")


def main() -> None:
    for path, media_name in TARGETS.items():
        update_docx(path, media_name)


if __name__ == "__main__":
    main()
