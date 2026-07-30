#!/usr/bin/env python3
"""Generate the HandFab 14.67.0 numeric-parameter dictionary and example trace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path

import trimesh


MODEL_IDS = ("flexy_beast", "paraglider_hand", "unlimbed_phoenix_hand")
EXAMPLE_PARTS = ("palm.3mf", "middle_base.3mf", "middle_tip.3mf")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_versioned_config(repository: Path, commit: str) -> dict:
    completed = subprocess.run(
        ["git", "-C", str(repository), "show", f"{commit}:models/models-config.json"],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def unit_for(parameter: dict) -> str:
    name = parameter["name"]
    caption = parameter.get("caption", "")
    if name == "HandPerc_override":
        return "%"
    if name.endswith("_scale"):
        return "razão adimensional"
    if name in {"gauntlet_pos_adjust", "strap_splay_adjust"}:
        return "mm"
    if name.endswith("_mm") or "(mm)" in caption or "diameter" in caption or "thickness" in caption:
        return "mm"
    return "unidade declarada no esquema"


def write_dictionary(config: dict, destination: Path) -> None:
    rows = []
    models = {model["id"]: model for model in config["models"]}
    for model_id in MODEL_IDS:
        model = models[model_id]
        for parameter in model["parameters"]:
            if parameter.get("type") != "number":
                continue
            rows.append(
                {
                    "model_id": model_id,
                    "model_name": model.get("name", model_id),
                    "parameter": parameter["name"],
                    "group": parameter.get("group", ""),
                    "unit": unit_for(parameter),
                    "initial": parameter.get("initial", ""),
                    "minimum": parameter.get("min", ""),
                    "maximum": parameter.get("max", ""),
                    "step": parameter.get("step", ""),
                    "label_pt": parameter.get("label_pt", ""),
                    "caption_pt": parameter.get("caption_pt", ""),
                    "role": parameter.get("role", ""),
                    "excluded_from_ai": parameter.get("excludeFromAI", False),
                }
            )

    fields = list(rows[0])
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def mesh_metrics(path: Path) -> dict:
    scene = trimesh.load(path, force="scene")
    mesh = trimesh.util.concatenate(tuple(scene.geometry.values()))
    extents = [round(float(value), 3) for value in mesh.extents]
    return {
        "file": path.name,
        "sha256": sha256(path),
        "bbox_xyz_mm": extents,
        "bbox_sorted_mm": sorted(extents, reverse=True),
        "watertight": bool(mesh.is_watertight),
        "volume_cm3": round(float(mesh.volume) / 1000, 3) if mesh.is_watertight else None,
        "faces": int(len(mesh.faces)),
    }


def write_trace(config: dict, example_dir: Path) -> None:
    params_path = example_dir / "params.json"
    params = json.loads(params_path.read_text(encoding="utf-8"))
    suggestions = params["suggestions"]
    flexy = next(model for model in config["models"] if model["id"] == "flexy_beast")
    definitions = {parameter["name"]: parameter for parameter in flexy["parameters"]}

    palm = float(suggestions["palm_breadth_mm"])
    middle = float(suggestions["middle_finger_length_mm"])
    x_scale = (palm + 5) / 55
    finger_length = middle / (37 * x_scale)
    digit_names = ("index", "middle", "ring", "pinky", "thumb")
    proportions = {
        digit: round(float(suggestions[f"{digit}_finger_length_mm" if digit != "thumb" else "thumb_length_mm"]) / middle, 6)
        for digit in digit_names
    }
    relevant = (
        "palm_breadth_mm",
        "middle_finger_length_mm",
        "index_finger_length_mm",
        "ring_finger_length_mm",
        "pinky_finger_length_mm",
        "thumb_length_mm",
        "joint_dia",
        "joint_thick",
        "gauntlet_width_mm",
        "gauntlet_length_mm",
        "gauntlet_wall_mm",
        "wrist_pin_dia",
    )
    limits = {
        name: {
            "initial": definitions[name].get("initial"),
            "minimum": definitions[name].get("min"),
            "maximum": definitions[name].get("max"),
            "applied": suggestions[name],
            "clamped": not (definitions[name].get("min", suggestions[name]) <= suggestions[name] <= definitions[name].get("max", suggestions[name])),
        }
        for name in relevant
    }

    trace = {
        "platform_version": "14.67.0",
        "git_commit": "bcef0db",
        "archived_execution_date": "2026-07-08",
        "model": "flexy_beast",
        "profile": params["profile"],
        "grounded": params["grounded"],
        "parameter_limits_and_values": limits,
        "derived_openscad_values": {
            "formula_xScaleFactor": "(palm_breadth_mm + 5) / 55",
            "xScaleFactor": round(x_scale, 6),
            "formula_fingerLength": "middle_finger_length_mm / (37 * xScaleFactor)",
            "fingerLength": round(finger_length, 6),
            "digit_proportions_relative_to_middle": proportions,
        },
        "mesh_metrics": [mesh_metrics(example_dir / name) for name in EXAMPLE_PARTS],
        "params_sha256": sha256(params_path),
        "interpretation_limit": "Technical trace of a simulated profile; not evidence of anatomical fit, comfort, function or clinical validity.",
    }
    (example_dir / "trace.json").write_text(json.dumps(trace, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_checksums(base: Path) -> None:
    files = [
        base / "README.md",
        base / "generate_supplement.py",
        base / "parameter_dictionary.csv",
        base / "example_flexy_beast_child_8" / "params.json",
        base / "example_flexy_beast_child_8" / "palm.3mf",
        base / "example_flexy_beast_child_8" / "middle_base.3mf",
        base / "example_flexy_beast_child_8" / "middle_tip.3mf",
        base / "example_flexy_beast_child_8" / "trace.json",
    ]
    lines = [f"{sha256(path)}  {path.relative_to(base)}" for path in files]
    (base / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--commit", default="bcef0db")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    config = read_versioned_config(args.repository.resolve(), args.commit)
    write_dictionary(config, base / "parameter_dictionary.csv")
    write_trace(config, base / "example_flexy_beast_child_8")
    write_checksums(base)


if __name__ == "__main__":
    main()
