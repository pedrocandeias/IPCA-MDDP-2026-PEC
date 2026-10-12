#!/usr/bin/env python3
"""Deriva um PNG do SVG oficial, mantendo cores, geometria e transparência."""
from pathlib import Path
import hashlib
import json
import fitz
from lxml import etree

ASSETS = Path(__file__).resolve().parent / 'assets'
source = ASSETS / 'upca_logo_oficial.svg'
output = source.with_suffix('.png')
root = etree.fromstring(source.read_bytes())
# O renderizador SVG do MuPDF não aplica estas classes CSS. Explicitar as
# mesmas cores numa cópia em memória, mantendo intacto o ficheiro recebido.
assert '.cls-1{fill:#00c83c;}.cls-2{fill:#fff;}' in source.read_text()
for element in root.iter():
    colour = {'cls-1': '#00c83c', 'cls-2': '#fff'}.get(element.get('class'))
    if colour:
        element.set('fill', colour)
with fitz.open('svg', etree.tostring(root)) as svg:
    with fitz.open('pdf', svg.convert_to_pdf()) as document:
        document[0].get_pixmap(matrix=fitz.Matrix(8, 8), alpha=True).save(output)
record = {
    'consultado_em': '2026-10-11',
    'instituicao': 'Universidade Politécnica do Cávado e do Ave (UPCA)',
    'pagina': 'https://ipca.pt/apresentacao/normas-graficas/',
    'url_svg': 'https://ipca.pt/wp-content/themes/ipca/img/logos/UPCA-pt.svg',
    'metodo': 'python3 docs/defesa/apresentacao/preparar_logo_upca.py',
    'tratamento': 'SVG original preservado; classes CSS explicitadas em memória para rasterização MuPDF a 8×, com transparência. Sem alteração de cores ou proporções.',
    'ficheiros': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (source, output)},
}
(ASSETS / 'upca_logo_proveniencia.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
