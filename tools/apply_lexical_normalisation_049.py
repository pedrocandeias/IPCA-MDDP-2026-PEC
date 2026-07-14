#!/usr/bin/env python3
"""Apply the 0.4.49 lexical normalisation to the canonical DOCX."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REPLACEMENTS = {
    "explicabilidade": ("compreensão das decisões", 3),
    "reprodutibilidade": ("possibilidade de reproduzir os resultados", 3),
    "variabilidade": ("variação", 1),
    "repetibilidade": ("consistência entre repetições", 3),
    "Rastreabilidade entre problema observado, decisão, versão e resultado": (
        "Correspondência documentada entre problema observado, decisão, versão e resultado",
        1,
    ),
    "O estudo acrescenta rastreabilidade entre entrada, decisão e artefacto": (
        "O estudo acrescenta uma relação documentada entre entrada, decisão e artefacto",
        1,
    ),
    "A rastreabilidade reforça o registo metodológico": (
        "A documentação do percurso reforça o registo metodológico",
        1,
    ),
    "previsibilidade mecânica": ("comportamento mecânico previsível", 1),
    "previsibilidade da geração paramétrica": ("consistência da geração paramétrica", 1),
    "Avaliação complementar da previsibilidade, recuperação e acessibilidade": (
        "Avaliação complementar da consistência da geração, recuperação e acessibilidade",
        2,
    ),
    "A previsibilidade depende": ("A consistência dos resultados depende", 1),
    "<w:t>previsibilidade</w:t>": ("<w:t>consistência da geração</w:t>", 1),
    "Resultados de previsibilidade": ("Resultados de consistência da geração", 2),
    "A previsibilidade deve": ("A consistência deve", 1),
}


def apply(path: Path) -> None:
    original_mode = path.stat().st_mode
    with ZipFile(path, "r") as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = files["word/document.xml"].decode("utf-8")
    for old, (new, expected) in REPLACEMENTS.items():
        found = document.count(old)
        if found != expected:
            raise RuntimeError(
                f"Ocorrências inesperadas para {old!r}: {found}; esperado: {expected}"
            )
        document = document.replace(old, new)
    files["word/document.xml"] = document.encode("utf-8")

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in items:
                target.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    apply(root / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx")
    print("DOCX normalizado para a versão 0.4.49")
