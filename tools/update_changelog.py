#!/usr/bin/env python3
"""Add dated entries to the repository changelog."""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = REPO_ROOT / "CHANGELOG.md"
VERSIONS_DIR = REPO_ROOT / "versions"
HEADER = "# Changelog"
MANUSCRIPT_PATTERNS = ("projecto-completo*.md", "Projecto completo.md")
EXCLUDED_MANUSCRIPTS = {"Projecto completo_baseline.md"}


def normalize_entries(values: list[str]) -> list[str]:
    entries: list[str] = []

    for value in values:
        for line in value.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("- "):
                line = line[2:].strip()
            entries.append(line)

    if not entries:
        raise ValueError("At least one non-empty changelog entry is required")

    return entries


def read_stdin_entries() -> list[str]:
    if sys.stdin.isatty():
        return []
    return sys.stdin.read().splitlines()


def format_bullets(entries: list[str]) -> str:
    return "".join(f"- {entry}\n" for entry in entries)


def update_changelog(text: str, entries: list[str], date: str) -> str:
    if not text.startswith(HEADER):
        raise ValueError(f"Unexpected changelog header. Expected: {HEADER}")

    heading = f"## {date}"
    lines = text.splitlines(keepends=True)

    if len(lines) >= 3 and lines[0].strip() == HEADER and lines[2].strip() == heading:
        insert_at = 3
        while insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1
        return "".join(lines[:insert_at]) + format_bullets(entries) + "".join(lines[insert_at:])

    prefix = f"{HEADER}\n\n"
    if not text.startswith(prefix):
        raise ValueError("Unexpected changelog spacing after header")

    new_section = f"{heading}\n\n{format_bullets(entries)}\n"
    return prefix + new_section + text[len(prefix):]


def resolve_repo_path(value: str | None) -> Path | None:
    if value is None:
        return None

    path = Path(value)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def find_latest_manuscript() -> Path:
    candidates: list[Path] = []

    for pattern in MANUSCRIPT_PATTERNS:
        for path in REPO_ROOT.glob(pattern):
            if path.name in EXCLUDED_MANUSCRIPTS:
                continue
            if path.is_file():
                candidates.append(path)

    if not candidates:
        patterns = ", ".join(MANUSCRIPT_PATTERNS)
        raise FileNotFoundError(f"No manuscript found in repository root matching: {patterns}")

    return max(candidates, key=lambda path: path.stat().st_mtime)


def find_latest_snapshot() -> Path | None:
    if not VERSIONS_DIR.exists():
        return None

    candidates = [path for path in VERSIONS_DIR.glob("*.md") if path.is_file()]
    if not candidates:
        return None

    return max(candidates, key=lambda path: path.stat().st_mtime)


def nearest_heading(lines: list[str], index: int) -> str | None:
    if not lines:
        return None

    index = min(max(index, 0), len(lines) - 1)
    for line_index in range(index, -1, -1):
        stripped = lines[line_index].strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return None


def changed_headings(old_lines: list[str], new_lines: list[str]) -> tuple[list[str], int, int]:
    matcher = SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    headings: list[str] = []
    added = 0
    removed = 0

    for tag, old_start, old_end, new_start, new_end in matcher.get_opcodes():
        if tag == "equal":
            continue

        added += max(new_end - new_start, 0)
        removed += max(old_end - old_start, 0)
        heading = nearest_heading(new_lines, new_start)
        if heading and heading not in headings:
            headings.append(heading)

    return headings, added, removed


def git_changed_paths() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    paths: list[str] = []
    for line in result.stdout.splitlines():
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()
        if path and path not in paths:
            paths.append(path)
    return paths


def auto_entries(source: Path | None = None) -> list[str]:
    manuscript = source or find_latest_manuscript()
    snapshot = find_latest_snapshot()

    if snapshot is not None and manuscript.exists():
        old_lines = snapshot.read_text(encoding="utf-8").splitlines()
        new_lines = manuscript.read_text(encoding="utf-8").splitlines()
        headings, added, removed = changed_headings(old_lines, new_lines)

        if added or removed:
            if headings:
                shown = "; ".join(headings[:5])
                if len(headings) > 5:
                    shown += f"; and {len(headings) - 5} more section(s)"
                return [
                    f"Updated `{manuscript.name}` against `{snapshot.relative_to(REPO_ROOT)}`, affecting: {shown} ({added} line(s) added, {removed} removed)."
                ]
            return [
                f"Updated `{manuscript.name}` against `{snapshot.relative_to(REPO_ROOT)}` ({added} line(s) added, {removed} removed)."
            ]

    paths = [path for path in git_changed_paths() if path != "CHANGELOG.md"]
    if paths:
        shown_paths = ", ".join(f"`{path}`" for path in paths[:8])
        if len(paths) > 8:
            shown_paths += f", and {len(paths) - 8} more path(s)"
        return [f"Updated repository files: {shown_paths}."]

    return ["Recorded repository maintenance update."]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prepend entries to CHANGELOG.md under today's date.")
    parser.add_argument("entries", nargs="*", help="Changelog entry text. Each argument becomes one bullet.")
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read additional changelog entries from standard input, one entry per line.",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Generate a changelog entry by comparing the current manuscript with the latest versions/ snapshot.",
    )
    parser.add_argument(
        "--source",
        help="Manuscript to compare in --auto mode. Defaults to the latest root manuscript.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date heading to update, in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the updated changelog without writing it.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    raw_entries = list(args.entries)
    if args.stdin:
        raw_entries.extend(read_stdin_entries())
    if args.auto:
        raw_entries.extend(auto_entries(resolve_repo_path(args.source)))

    entries = normalize_entries(raw_entries)
    current = CHANGELOG.read_text(encoding="utf-8")
    updated = update_changelog(current, entries, args.date)

    if args.dry_run:
        print(updated, end="")
    else:
        CHANGELOG.write_text(updated, encoding="utf-8")
        print(f"Updated: {CHANGELOG.relative_to(REPO_ROOT)}")
        for entry in entries:
            print(f"- {entry}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
