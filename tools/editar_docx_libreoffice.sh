#!/usr/bin/env bash
# Abre o DOCX canónico no LibreOffice Writer preservando o Mendeley Cite.
#
# Fluxo: guarda uma referência, abre o Writer, e quando o fechares repõe
# automaticamente o estado do add-in do Word (webextensions) que o
# LibreOffice descarta ao gravar.
#
# Uso: tools/editar_docx_libreoffice.sh [ficheiro.docx]
#
# Atenção: fecha as outras janelas do LibreOffice antes de correr isto —
# se já houver uma instância aberta, o comando regressa imediatamente e a
# reparação corre antes de acabares de editar.

set -euo pipefail
cd "$(dirname "$0")/.."

DOCX="${1:-pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx}"

python3 tools/word_lo_bridge.py backup "$DOCX"
echo "A abrir no LibreOffice Writer… (a reparação corre quando fechares)"
libreoffice --norestore "$DOCX"
python3 tools/word_lo_bridge.py restore "$DOCX"
echo "Concluído. Se editaste citações no texto, faz Refresh no Word na próxima oportunidade."
