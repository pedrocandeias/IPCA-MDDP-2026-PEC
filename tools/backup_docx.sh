#!/usr/bin/env bash
#
# Back up the canonical revised DOCX and always regenerate its PDF.
#
# Usage:
#   ./tools/backup_docx.sh [label]
#
# Examples:
#   ./tools/backup_docx.sh                       # label defaults to "backup"
#   ./tools/backup_docx.sh before-chapter-5-edit
#
# What it does:
#   1. Copies the canonical root DOCX to
#      docs/versoes/backups/<name>-<YYYY-MM-DD_HH-MM-SS>-<label>.docx
#   2. Converts the current canonical root DOCX to the matching PDF
#      (root-level, overwritten in place) using headless LibreOffice.
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

BASE="pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto"
DOCX="$BASE.docx"
VERSIONS_DIR="docs/versoes/backups"

label="${1:-backup}"
# Sanitise the label: keep it filesystem-friendly.
label="$(printf '%s' "$label" | tr ' /' '--' | tr -cd 'A-Za-z0-9._-')"
[ -n "$label" ] || label="backup"

if [ ! -f "$DOCX" ]; then
  echo "error: $DOCX not found in $REPO_ROOT" >&2
  exit 1
fi

timestamp="$(date +%Y-%m-%d_%H-%M-%S)"
backup="$VERSIONS_DIR/${BASE}-${timestamp}-${label}.docx"

mkdir -p "$VERSIONS_DIR"
cp -p "$DOCX" "$backup"
echo "Backup:   $backup"

# Regenerate the matching PDF from the current DOCX (single source of
# truth for the conversion lives in tools/docx_to_pdf.sh).
"$(dirname "${BASH_SOURCE[0]}")/docx_to_pdf.sh"
