#!/usr/bin/env python3
"""Stage changes and commit them with the latest CHANGELOG.md entry."""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = REPO_ROOT / "CHANGELOG.md"


def run_git(args: list[str], dry_run: bool = False) -> subprocess.CompletedProcess[str] | None:
    command = ["git", *args]
    if dry_run:
        print("$ " + " ".join(command))
        return None
    return subprocess.run(command, cwd=REPO_ROOT, check=True, text=True)


def capture_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout


def latest_changelog_section(text: str) -> tuple[str, list[str]]:
    match = re.search(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if not match:
        raise ValueError("No dated changelog section found")

    title = match.group(1).strip()
    start = match.end()
    next_match = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    body = text[start:end].strip("\n")
    bullets = [line[2:].strip() for line in body.splitlines() if line.strip().startswith("- ")]

    if not bullets:
        raise ValueError(f"Latest changelog section has no bullet entries: {title}")

    return title, bullets


def build_commit_message(title: str, bullets: list[str]) -> str:
    subject = bullets[0].rstrip(".")
    body = "\n".join(f"- {bullet}" for bullet in bullets)
    return f"{subject}\n\nChangelog {title}\n\n{body}\n"


def staged_has_changes() -> bool:
    result = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT)
    return result.returncode == 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run git add and git commit using the latest CHANGELOG.md section as the commit message."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Paths to stage. Defaults to the whole repository.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the commit message and git commands without staging or committing.",
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Pass --no-verify to git commit.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    title, bullets = latest_changelog_section(CHANGELOG.read_text(encoding="utf-8"))
    message = build_commit_message(title, bullets)

    if args.dry_run:
        print("Commit message:")
        print(message)
        run_git(["add", *args.paths], dry_run=True)
        commit_args = ["commit"]
        if args.no_verify:
            commit_args.append("--no-verify")
        commit_args.extend(["-F", "<temporary-message-file>"])
        run_git(commit_args, dry_run=True)
        print("\nCurrent status:")
        print(capture_git(["status", "--short"]), end="")
        return 0

    run_git(["add", *args.paths])
    if not staged_has_changes():
        print("No staged changes to commit.")
        return 1

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as handle:
        handle.write(message)
        message_path = Path(handle.name)

    try:
        commit_args = ["commit"]
        if args.no_verify:
            commit_args.append("--no-verify")
        commit_args.extend(["-F", str(message_path)])
        run_git(commit_args)
    finally:
        message_path.unlink(missing_ok=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
