#!/usr/bin/env python3
"""Apply the 0.4.47 table-title terminology changes to the canonical DOCX."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZipFile


REPLACEMENTS = {
    "Percurso numérico do vector antropométrico até às malhas do Flexy Beast": (
        "Exemplo da transformação das medidas antropométricas em geometria digital no Flexy Beast",
        2,
    ),
    "Inventário consolidado dos modelos no fecho do estudo": (
        "Modelos integrados na plataforma e respectiva avaliação",
        2,
    ),
    "Rácio adimensional da maior dimensão da palma exportada face ao valor de referência": (
        "Factor de escala da maior dimensão da palma exportada relativamente à configuração de referência",
        2,
    ),
    "Nota: os rácios apresentados são adimensionais. Um valor de 1,000 corresponde à dimensão da configuração de referência; valores inferiores indicam redução e valores superiores indicam aumento face a essa configuração.": (
        "Nota: o factor de escala resulta da divisão entre a maior dimensão da palma exportada e a dimensão correspondente da configuração de referência. Um valor de 1,000 indica igualdade; valores inferiores indicam redução e valores superiores indicam aumento relativamente à referência.",
        1,
    ),
    "O perfil infantil produziu rácios de 0,761 e 0,747 face ao valor de referência": (
        "O perfil infantil produziu factores de escala de 0,761 e 0,747 relativamente à configuração de referência",
        1,
    ),
    "um rácio de 0,760 no perfil infantil": (
        "um factor de escala de 0,760 no perfil infantil",
        1,
    ),
}


def apply(path: Path) -> None:
    with ZipFile(path, "r") as source:
        document = source.read("word/document.xml").decode("utf-8")
        for old, (new, expected) in REPLACEMENTS.items():
            found = document.count(old)
            if found != expected:
                raise RuntimeError(
                    f"Ocorrências inesperadas para {old!r}: {found}; esperado: {expected}"
                )
            document = document.replace(old, new)

        fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
        os.close(fd)
        temporary = Path(temporary_name)
        try:
            with ZipFile(temporary, "w") as target:
                for item in source.infolist():
                    data = (
                        document.encode("utf-8")
                        if item.filename == "word/document.xml"
                        else source.read(item.filename)
                    )
                    target.writestr(item, data)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    apply(root / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx")
    print("DOCX actualizado para a versão 0.4.47")
