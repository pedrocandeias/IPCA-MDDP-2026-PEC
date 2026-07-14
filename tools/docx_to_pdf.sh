#!/usr/bin/env bash
#
# Regenerate the canonical revised PDF from the canonical revised DOCX.
#
# Usage:
#   ./tools/docx_to_pdf.sh
#
# Converts the root canonical DOCX to the matching PDF (root-level,
# overwritten in place) using headless LibreOffice. This is the single source of
# truth for the DOCX->PDF conversion; both tools/backup_docx.sh and the
# pre-commit hook call it so the PDF always tracks the latest DOCX.
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

BASE="pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto"
DOCX="$BASE.docx"
PDF="$BASE.pdf"

if [ ! -f "$DOCX" ]; then
  echo "error: $DOCX not found in $REPO_ROOT" >&2
  exit 1
fi

soffice_bin="$(command -v libreoffice || command -v soffice || true)"
if [ -z "$soffice_bin" ]; then
  echo "error: LibreOffice (libreoffice/soffice) not found on PATH" >&2
  exit 1
fi

# --convert-to writes the matching PDF into --outdir (repo root),
# overwriting the previous PDF.
"$soffice_bin" --headless --convert-to pdf --outdir "$REPO_ROOT" "$DOCX" >/dev/null
echo "PDF:      $PDF"
