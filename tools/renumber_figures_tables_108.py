#!/usr/bin/env python3
"""Renumera figuras e tabelas do Markdown para numeração sequencial (v0.4.108).

O DOCX canónico usa numeração sequencial contínua (Figura 1..29,
Tabela 1..31) com números literais nas legendas; os anexos mantêm a
numeração por letra (B.1, C.1, D.1...). Este script converte o Markdown
da numeração por capítulo (Figura 8.1, Tabela 4.2) para a numeração
sequencial, derivando o mapa da ordem real das legendas no documento.

A tabela «Ciclos de Research Through Design» (antiga 3.1) assume o
número 4, corrigindo o duplicado «Tabela 4» existente no DOCX; as
tabelas seguintes avançam uma unidade em relação ao DOCX actual.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"

OLD_VERSION = "Versão do documento: 0.4.107"
NEW_VERSION = "Versão do documento: 0.4.108"

EXPECTED_FIGURES = 29
EXPECTED_TABLES = 31

CAPTION_RE = re.compile(r"^(Figura|Tabela) (\d+\.\d+) — ", re.M)
ENUM_RE = re.compile(
    r"(Figuras|Tabelas)(\s+)(\d+\.\d+(?:\s*(?:,\s*|\s+e\s+|\s+a\s+)\d+\.\d+)+)")
SINGLE_RE = re.compile(r"(Figura|Tabela)(s?)(\s+)(\d+\.\d+)(?!\d)")


def main() -> None:
    text = MD.read_text(encoding="utf-8")
    if text.count(OLD_VERSION) != 1:
        raise RuntimeError("A versão de origem do Markdown não é 0.4.107")

    fig_map: dict[str, str] = {}
    tab_map: dict[str, str] = {}
    for kind, num in CAPTION_RE.findall(text):
        target = fig_map if kind == "Figura" else tab_map
        if num in target:
            raise RuntimeError(f"Legenda duplicada: {kind} {num}")
        target[num] = str(len(target) + 1)

    if len(fig_map) != EXPECTED_FIGURES:
        raise RuntimeError(f"Esperava {EXPECTED_FIGURES} figuras, "
                           f"encontrei {len(fig_map)}")
    if len(tab_map) != EXPECTED_TABLES:
        raise RuntimeError(f"Esperava {EXPECTED_TABLES} tabelas, "
                           f"encontrei {len(tab_map)}")

    def lookup(kind: str, num: str) -> str:
        table = fig_map if kind.startswith("Figura") else tab_map
        if num not in table:
            raise RuntimeError(f"Referência sem legenda correspondente: "
                               f"{kind} {num}")
        return table[num]

    def enum_repl(m: re.Match) -> str:
        kind, space, nums = m.group(1), m.group(2), m.group(3)
        converted = re.sub(r"\d+\.\d+",
                           lambda n: lookup(kind, n.group(0)), nums)
        return f"{kind}{space}{converted}"

    text = ENUM_RE.sub(enum_repl, text)
    text = SINGLE_RE.sub(
        lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}"
                  f"{lookup(m.group(1), m.group(4))}", text)

    leftover = re.findall(r"(?:Figura|Tabela)s?\s+\d+\.\d+", text)
    if leftover:
        raise RuntimeError(f"Referências por converter: {leftover[:5]}")

    text = text.replace(OLD_VERSION, NEW_VERSION, 1)
    MD.write_text(text, encoding="utf-8")
    print(f"Renumeradas {len(fig_map)} figuras e {len(tab_map)} tabelas.")
    print("Mapa das tabelas:",
          ", ".join(f"{k}->{v}" for k, v in tab_map.items()))


if __name__ == "__main__":
    main()
