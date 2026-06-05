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
  1. Update CHANGELOG.md. Without supplied text, generate an entry by comparing
     the current manuscript with the latest snapshot in versions/.
  2. Create a timestamped manuscript snapshot in versions/.
  3. Stage and commit changes using the latest changelog section as the commit message.
EOF
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

echo "[1/3] Updating CHANGELOG.md..."
if [[ "${#changelog_entries[@]}" -eq 0 ]]; then
  python3 tools/update_changelog.py --auto
else
  python3 tools/update_changelog.py "${changelog_entries[@]}"
fi

echo "[2/3] Creating manuscript snapshot..."
python3 tools/version_manuscript.py

echo "[3/3] Staging and committing changes..."
python3 tools/commit_from_changelog.py "${commit_paths[@]}"
