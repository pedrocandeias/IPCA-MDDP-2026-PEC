#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

usage() {
  cat <<'EOF'
Usage:
  ./deploy.sh ["Changelog entry"] ["Another changelog entry"] [-- path ...]

Examples:
  ./deploy.sh
  ./deploy.sh "Revised section 4.1 and updated bibliography."
  ./deploy.sh "Added workflow scripts." -- CHANGELOG.md tools deploy.sh

Sequence:
  1. Update CHANGELOG.md only when needed:
     - with supplied text, add that text;
     - without supplied text, compare the latest local changelog section with
       the latest committed changelog section;
     - if they are equal, generate an automatic entry;
     - if they differ, keep the existing local entry and use it for the commit.
  2. Create a timestamped manuscript snapshot in versions/.
  3. Stage and commit changes using the latest changelog section as the commit message.
EOF
}

latest_changelog_differs_from_head() {
  python3 - <<'PY_COMPARE_CHANGELOG'
from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path.cwd()
CHANGELOG = REPO_ROOT / "CHANGELOG.md"


def latest_section(text: str) -> str:
    match = re.search(r"^##\s+.+?\s*$", text, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.start()
    next_match = re.search(r"^##\s+", text[match.end():], flags=re.MULTILINE)
    end = match.end() + next_match.start() if next_match else len(text)
    return text[start:end].strip()

local = latest_section(CHANGELOG.read_text(encoding="utf-8"))
try:
    committed_text = subprocess.run(
        ["git", "show", "HEAD:CHANGELOG.md"],
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    ).stdout
except subprocess.CalledProcessError:
    raise SystemExit(1)

committed = latest_section(committed_text)
raise SystemExit(0 if local != committed else 1)
PY_COMPARE_CHANGELOG
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

changelog_entries=()
commit_paths=()
parsing_paths=0

for arg in "$@"; do
  if [[ "$arg" == "--" ]]; then
    parsing_paths=1
    continue
  fi

  if [[ "$parsing_paths" -eq 1 ]]; then
    commit_paths+=("$arg")
  else
    changelog_entries+=("$arg")
  fi
done

if [[ "${#commit_paths[@]}" -eq 0 ]]; then
  commit_paths=(".")
fi

echo "[1/3] Preparing CHANGELOG.md..."
if [[ "${#changelog_entries[@]}" -gt 0 ]]; then
  python3 tools/update_changelog.py "${changelog_entries[@]}"
elif latest_changelog_differs_from_head; then
  echo "Latest local changelog entry differs from HEAD; using it as the commit message."
else
  echo "Latest changelog entry already exists in HEAD; generating an automatic entry."
  python3 tools/update_changelog.py --auto
fi

echo "[2/3] Creating manuscript snapshot..."
python3 tools/version_manuscript.py

echo "[3/3] Staging and committing changes..."
python3 tools/commit_from_changelog.py "${commit_paths[@]}"
