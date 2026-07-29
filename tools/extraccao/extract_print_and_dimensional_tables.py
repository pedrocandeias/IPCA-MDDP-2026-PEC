#!/usr/bin/env python3
"""Gerar as tabelas de preparação e comparação dimensional da dissertação.

A tabela de preparação é reduzida a partir da campanha controlada de fatiamento.
A tabela dimensional lê os parâmetros aplicados e mede directamente a caixa
envolvente da malha 3MF da palma de cada perfil. A coluna da peça física fica
vazia até existir uma medição manual realizada no mesmo referencial.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import trimesh


MODELS = {
    "Flexy Beast": "flexy_beast",
    "Paraglider Hand": "paraglider_hand",
    "UnLimbited Phoenix": "unlimbed_phoenix_hand",
}
PROFILES = ("child_8", "teen_15", "adult_28", "elderly_70")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform-root",
        type=Path,
        default=Path("/home/pec/dev/ai-parametric-prosthetic-hand-generator"),
    )
    parser.add_argument(
        "--annex-dir",
        type=Path,
        default=Path(
            "sources/manuscript/annexes/testes_preparacao_impressao"
        ),
    )
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def palm_path(base: Path, slug: str, profile: str) -> Path:
    folder = base / slug / profile
    if slug in {"flexy_beast", "paraglider_hand"}:
        return folder / "parts" / "palm.3mf"
    return folder / f"unlimbed_phoenix_hand_{profile}_palm.3mf"


def main() -> None:
    args = parse_args()
    annex_dir = args.annex_dir.resolve()
    validation = args.platform_root.resolve() / "docs" / "print-validation"

    campaign = read_csv(annex_dir / "resultados_campanha_controlada.csv")
    archived = read_csv(annex_dir / "resultados_projectos_arquivados.csv")
    archived_rows: list[dict[str, object]] = []
    for row in archived:
        project = row["projecto"]
        model = project.split(" (", 1)[0]
        profile = "teen_15"
        archived_rows.append(
            {
                "modelo": model,
                "perfil": profile,
                "material": row["material"],
                "impressora": f'{row["impressora"]}; bico {row["bico_mm"]} mm',
                "camada_mm": row["altura_camada_mm"],
                "enchimento": row["enchimento"],
                "suportes": row["suportes"],
                "tempo_estimado": row["tempo_estimado"],
                "filamento_estimado_mm": row["comprimento_filamento_mm"],
                "massa_estimada_g": row["massa_g"],
            }
        )

    output_fields = [
        "modelo",
        "perfil",
        "material",
        "impressora",
        "camada_mm",
        "enchimento",
        "suportes",
        "tempo_estimado",
        "filamento_estimado_mm",
        "massa_estimada_g",
    ]
    write_csv(
        annex_dir / "tabela_projectos_arquivados_impressao.csv",
        output_fields,
        archived_rows,
    )

    print_rows: list[dict[str, object]] = []
    for row in campaign:
        print_rows.append(
            {
                "modelo": row["modelo"],
                "perfil": row["perfil"],
                "material": "Bambu PLA Basic",
                "impressora": "Bambu Lab A1; bico 0,4 mm",
                "camada_mm": "0,20",
                "enchimento": "15%; grelha",
                "suportes": "Não",
                "tempo_estimado": row["tempo_estimado_total"],
                "filamento_estimado_mm": row["comprimento_filamento_mm"],
                "massa_estimada_g": row["massa_g"],
            }
        )

    write_csv(
        annex_dir / "tabela_preparacao_impressao.csv",
        output_fields,
        print_rows,
    )

    dimensional_rows: list[dict[str, object]] = []
    for model, slug in MODELS.items():
        for profile in PROFILES:
            folder = validation / slug / profile
            params_file = folder / "params.json"
            with params_file.open(encoding="utf-8") as handle:
                params = json.load(handle)
            mesh_file = palm_path(validation, slug, profile)
            scene = trimesh.load(mesh_file, force="scene")
            suggestions = params["suggestions"]
            parameter_by_axis = {
                "X": "palm_breadth_mm",
                "Y": "palm_length_mm",
                "Z": "palm_thickness_mm",
            }
            for axis_index, axis in enumerate(("X", "Y", "Z")):
                parameter = parameter_by_axis[axis]
                entry = suggestions.get(parameter)
                if entry is None:
                    parameter_status = "sem parâmetro correspondente no perfil aplicado"
                elif axis == "X":
                    parameter_status = "activo na transformação geométrica"
                else:
                    parameter_status = "contextual; não controla este eixo de forma independente"
                dimensional_rows.append(
                    {
                        "modelo": model,
                        "perfil": profile,
                        "ponto_medido": f"Palma: extensão total no eixo {axis}",
                        "parametro_entrada": parameter if entry is not None else "",
                        "estado_parametro": parameter_status,
                        "entrada_mm": "" if entry is None else f"{float(entry):.1f}",
                        "malha_mm": f"{float(scene.extents[axis_index]):.3f}",
                        "leitura_1_mm": "",
                        "leitura_2_mm": "",
                        "leitura_3_mm": "",
                        "media_peca_fisica_mm": "",
                        "amplitude_leituras_mm": "",
                        "desvio_malha_peca_mm": "",
                        "desvio_percentual": "",
                        "ficheiro_malha": str(mesh_file.relative_to(args.platform_root)),
                    }
                )

    write_csv(
        annex_dir / "tabela_comparacao_dimensional.csv",
        [
            "modelo",
            "perfil",
            "ponto_medido",
            "parametro_entrada",
            "estado_parametro",
            "entrada_mm",
            "malha_mm",
            "leitura_1_mm",
            "leitura_2_mm",
            "leitura_3_mm",
            "media_peca_fisica_mm",
            "amplitude_leituras_mm",
            "desvio_malha_peca_mm",
            "desvio_percentual",
            "ficheiro_malha",
        ],
        dimensional_rows,
    )

    print(f"Gerada: {annex_dir / 'tabela_projectos_arquivados_impressao.csv'}")
    print(f"Gerada: {annex_dir / 'tabela_preparacao_impressao.csv'}")
    print(f"Gerada: {annex_dir / 'tabela_comparacao_dimensional.csv'}")


if __name__ == "__main__":
    main()
