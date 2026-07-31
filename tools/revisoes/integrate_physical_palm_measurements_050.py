#!/usr/bin/env python3
"""Build the dimensional comparison sheet from recorded PLA/PETG measurements."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/desenvolvimento/dimensionamento/palm-body-dimensions.md"
TARGET = (
    ROOT
    / "componentes/anexos/testes_preparacao_impressao"
    / "tabela_comparacao_dimensional.csv"
)

MODELS = {"Flexy Beast", "Paraglider Hand", "UnLimbited Phoenix"}
PROFILE_CODES = {
    "8 anos": "child_8",
    "15 anos": "teen_15",
    "28 anos": "adult_28",
    "70 anos": "elderly_70",
}
SECTION_LABELS = {
    "## 1. Nominal — modelo digital": "Nominal",
    "## 2. Medições físicas — PLA": "PLA",
    "## 3. Medições físicas — PETG": "PETG",
}
AXES = ("X", "Y", "Z")


def quantise(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP), "f")


def parse_measurements(path: Path) -> list[dict[str, object]]:
    section: str | None = None
    rows: list[dict[str, object]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line in SECTION_LABELS:
            section = SECTION_LABELS[line]
            continue
        if line.startswith("## ") and line not in SECTION_LABELS:
            section = None
            continue
        if section is None or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 5 or cells[0] not in MODELS:
            continue
        if cells[1] not in PROFILE_CODES:
            raise RuntimeError(f"Perfil inesperado: {cells[1]!r}")
        rows.append(
            {
                "section": section,
                "model": cells[0],
                "profile_label": cells[1],
                "profile": PROFILE_CODES[cells[1]],
                "values": {
                    axis: Decimal(cells[index].replace(",", "."))
                    for index, axis in enumerate(AXES, start=2)
                },
            }
        )
    if len(rows) != 36:
        raise RuntimeError(f"Esperadas 36 linhas nas três tabelas; obtidas {len(rows)}")
    return rows


def load_base_rows(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        result: dict[tuple[str, str, str], dict[str, str]] = {}
        for row in reader:
            axis = row["ponto_medido"].rsplit(" ", 1)[-1]
            result[(row["modelo"], row["perfil"], axis)] = row
    if len(result) != 36:
        raise RuntimeError(f"Esperadas 36 linhas-base; obtidas {len(result)}")
    return result


def build_output(
    measurements: list[dict[str, object]],
    base: dict[tuple[str, str, str], dict[str, str]],
) -> tuple[list[dict[str, str]], list[str]]:
    nominal = {
        (row["model"], row["profile"]): row
        for row in measurements
        if row["section"] == "Nominal"
    }
    physical = [row for row in measurements if row["section"] in {"PLA", "PETG"}]
    by_key = {(row["section"], row["model"], row["profile"]): row for row in physical}
    output: list[dict[str, str]] = []
    x_table: list[str] = []

    for model, profile in nominal:
        nominal_row = nominal[(model, profile)]
        pla_row = by_key[("PLA", model, profile)]
        petg_row = by_key[("PETG", model, profile)]
        malha_x = nominal_row["values"]["X"]
        pla_x = pla_row["values"]["X"]
        petg_x = petg_row["values"]["X"]
        x_table.append(
            "| "
            + " | ".join(
                [
                    str(model),
                    str(nominal_row["profile_label"]),
                    f"{quantise(malha_x).replace('.', ',')} mm",
                    f"{quantise(pla_x).replace('.', ',')} mm",
                    f"{quantise(pla_x - malha_x).replace('.', ',')} mm",
                    f"{quantise(petg_x).replace('.', ',')} mm",
                    f"{quantise(petg_x - malha_x).replace('.', ',')} mm",
                ]
            )
            + " |"
        )

        for material, physical_row in (("PLA", pla_row), ("PETG", petg_row)):
            for axis in AXES:
                base_row = base[(str(model), str(profile), axis)]
                mesh = nominal_row["values"][axis]
                measured = physical_row["values"][axis]
                deviation = measured - mesh
                percentage = Decimal("100") * deviation / mesh
                output.append(
                    {
                        "modelo": str(model),
                        "perfil": str(profile),
                        "material": material,
                        "ponto_medido": base_row["ponto_medido"],
                        "parametro_entrada": base_row["parametro_entrada"],
                        "estado_parametro": base_row["estado_parametro"],
                        "entrada_mm": base_row["entrada_mm"],
                        "malha_mm": quantise(mesh),
                        "medicao_fisica_mm": quantise(measured),
                        "numero_leituras": "1",
                        "desvio_malha_peca_mm": quantise(deviation),
                        "desvio_percentual": quantise(percentage),
                        "ficheiro_malha": base_row["ficheiro_malha"],
                        "fonte_medicao": "Registo dimensional das palmas em PLA e PETG",
                    }
                )
    return output, x_table


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    measurements = parse_measurements(SOURCE)
    base = load_base_rows(TARGET)
    output, x_table = build_output(measurements, base)
    write_csv(TARGET, output)
    print(f"CSV actualizado: {TARGET}")
    print(f"Resultados físicos: {len(output)} (24 palmas × 3 eixos)")
    print("\n".join(x_table))


if __name__ == "__main__":
    main()
