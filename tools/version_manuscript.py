#!/usr/bin/env python3
"""Create a timestamped manuscript snapshot under docs/versoes/backups/."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSIONS_DIR = REPO_ROOT / "docs" / "versoes" / "backups"
CANONICAL_MANUSCRIPT = REPO_ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"


def resolve_repo_path(value: str | None) -> Path | None:
    if value is None:
        return None

    path = Path(value)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def find_latest_manuscript() -> Path:
    if not CANONICAL_MANUSCRIPT.is_file():
        raise FileNotFoundError(f"Canonical manuscript not found: {CANONICAL_MANUSCRIPT}")
    return CANONICAL_MANUSCRIPT


def validate_source(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"Source manuscript not found: {path}")
    if not path.is_file():
        raise IsADirectoryError(f"Source manuscript is not a file: {path}")
    if path.suffix.lower() != ".md":
        raise ValueError(f"Source manuscript must be a Markdown file: {path}")
    return path


def make_destination(now: dt.datetime | None = None) -> Path:
    timestamp = (now or dt.datetime.now()).strftime("%H%M%S-%d%m%Y")
    return VERSIONS_DIR / f"pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto-{timestamp}.md"


def create_snapshot(source: Path, dry_run: bool = False) -> Path:
    destination = make_destination()

    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    if not dry_run:
        VERSIONS_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    return destination


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Copy the canonical thesis manuscript to docs/versoes/backups with a timestamp."
    )
    parser.add_argument(
        "--source",
        help=(
            "Manuscript to version. If omitted, the canonical revised Markdown file is used."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the source and destination without copying the file.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    source = resolve_repo_path(args.source) if args.source else find_latest_manuscript()
    source = validate_source(source)
    destination = create_snapshot(source, dry_run=args.dry_run)

    action = "Would create" if args.dry_run else "Created"
    print(f"{action}: {destination.relative_to(REPO_ROOT)}")
    print(f"Source: {source.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
