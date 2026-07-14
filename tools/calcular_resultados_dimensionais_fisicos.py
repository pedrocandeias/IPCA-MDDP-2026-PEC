#!/usr/bin/env python3
"""Calcular os desvios dimensionais sem substituir as leituras originais."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_DIR = Path("sources/manuscript/annexes/testes_preparacao_impressao")


def number(value: str) -> float:
    return float(value.strip().replace(",", "."))


def formatted(value: float) -> str:
    return f"{value:.3f}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_DIR / "tabela_comparacao_dimensional.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_DIR / "resultados_dimensionais_fisicos_calculados.csv",
    )
    args = parser.parse_args()

    with args.input.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)

    completed = 0
    incomplete = 0
    for row in rows:
        readings = [row.get(f"leitura_{index}_mm", "").strip() for index in (1, 2, 3)]
        if not any(readings):
            continue
        if not all(readings):
            incomplete += 1
            continue
        values = [number(value) for value in readings]
        mesh = number(row["malha_mm"])
        mean = sum(values) / 3
        span = max(values) - min(values)
        deviation = mean - mesh
        percentage = 100 * deviation / mesh
        row["media_peca_fisica_mm"] = formatted(mean)
        row["amplitude_leituras_mm"] = formatted(span)
        row["desvio_malha_peca_mm"] = formatted(deviation)
        row["desvio_percentual"] = formatted(percentage)
        completed += 1

    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Linhas calculadas: {completed}")
    print(f"Linhas com leituras incompletas: {incomplete}")
    print(f"Resultado: {args.output}")


if __name__ == "__main__":
    main()
