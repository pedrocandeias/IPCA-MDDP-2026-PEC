#!/usr/bin/env python3
"""Create a timestamped manuscript snapshot in versions/."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSIONS_DIR = REPO_ROOT / "versions"
DEFAULT_PATTERNS = ("projecto-completo*.md", "Projecto completo.md")
EXCLUDED_NAMES = {"Projecto completo_baseline.md"}


def resolve_repo_path(value: str | None) -> Path | None:
    if value is None:
        return None

    path = Path(value)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def find_latest_manuscript() -> Path:
    candidates: list[Path] = []

    for pattern in DEFAULT_PATTERNS:
        for path in REPO_ROOT.glob(pattern):
            if path.name in EXCLUDED_NAMES:
                continue
            if path.is_file():
                candidates.append(path)

    if not candidates:
        patterns = ", ".join(DEFAULT_PATTERNS)
        raise FileNotFoundError(f"No manuscript found in repository root matching: {patterns}")

    return max(candidates, key=lambda path: path.stat().st_mtime)


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
    return VERSIONS_DIR / f"projecto-completo-{timestamp}.md"


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
        description="Copy the latest thesis manuscript to versions/ with a timestamped filename."
    )
    parser.add_argument(
        "--source",
        help=(
            "Manuscript to version. If omitted, the newest root Markdown file matching "
            "'projecto-completo*.md' or 'Projecto completo.md' is used."
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
