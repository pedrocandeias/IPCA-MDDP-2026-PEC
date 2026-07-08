#!/usr/bin/env bash
#
# Back up projecto-completo.docx and always (re)generate projecto-completo.pdf.
#
# Usage:
#   ./tools/backup_docx.sh [label]
#
# Examples:
#   ./tools/backup_docx.sh                       # label defaults to "backup"
#   ./tools/backup_docx.sh before-chapter-5-edit
#
# What it does:
#   1. Copies the root projecto-completo.docx to
#      versions/projecto-completo-docx-<YYYY-MM-DD_HH-MM-SS>-<label>.docx
#   2. Converts the current root projecto-completo.docx to projecto-completo.pdf
#      (root-level, overwritten in place) using headless LibreOffice.
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

DOCX="projecto-completo.docx"
VERSIONS_DIR="versions"

label="${1:-backup}"
# Sanitise the label: keep it filesystem-friendly.
label="$(printf '%s' "$label" | tr ' /' '--' | tr -cd 'A-Za-z0-9._-')"
[ -n "$label" ] || label="backup"

if [ ! -f "$DOCX" ]; then
  echo "error: $DOCX not found in $REPO_ROOT" >&2
  exit 1
fi

timestamp="$(date +%Y-%m-%d_%H-%M-%S)"
backup="$VERSIONS_DIR/projecto-completo-docx-${timestamp}-${label}.docx"

mkdir -p "$VERSIONS_DIR"
cp -p "$DOCX" "$backup"
echo "Backup:   $backup"

# Regenerate projecto-completo.pdf from the current DOCX (single source of
# truth for the conversion lives in tools/docx_to_pdf.sh).
"$(dirname "${BASH_SOURCE[0]}")/docx_to_pdf.sh"
