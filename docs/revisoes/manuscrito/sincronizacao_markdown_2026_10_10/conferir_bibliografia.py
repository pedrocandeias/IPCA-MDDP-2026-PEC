#!/usr/bin/env python3
"""Inventory local PDFs against the bibliography actually present in the ODT.

Reuses the repository's matching rules; does not alter the manuscript.
Exact duplicate entries are counted once for PDF availability only.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
import json
import re
import sys
import zipfile
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from tools.bibliografia.consolidate_docx_referenced_pdfs import (
    Reference, pdf_info, best_match, norm, KNOWN_PDFS, NON_PDF_RESOURCES,
    DOI_RE, clean_doi, extract_title,
)

SOURCE = ROOT / 'pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt'
with zipfile.ZipFile(SOURCE) as z:
    root = ET.fromstring(z.read('content.xml'))
entries = [''.join(p.itertext()).strip() for p in root.xpath(
    '//text:p[@text:style-name="Bibliography"]', namespaces=root.nsmap
)]
entries = [e for e in entries if e]
unique = list(dict.fromkeys(entries))
paths = sorted((ROOT/'material').rglob('*.pdf'))
with ThreadPoolExecutor(max_workers=8) as pool:
    infos = [p for p in pool.map(pdf_info, paths) if p]
by_path = {p.path: p for p in infos}
local = [p for p in infos if p.path.startswith('material/bibliografia/')]
library = [p for p in infos if not p.path.startswith('material/bibliografia/')]
year_re = re.compile(r'\(((?:(?:19|20)\d{2}|n\.d\.)(?:-?[a-z])?)(?:,\s*[^)]*)?\)\.\s+', re.I)
rows = []
for number, entry in enumerate(unique, 1):
    match = year_re.search(entry)
    author = entry[:match.start()].split(',', 1)[0].strip() if match else entry.split(',', 1)[0]
    year = match.group(1) if match else ''
    title = extract_title(entry[match.end():]) if match else entry
    dois = tuple(sorted({clean_doi(m.group(0)) for m in DOI_RE.finditer(entry)}))
    ref = Reference(number, entry, title, author, year, dois)
    key = (norm(author), year)
    known = KNOWN_PDFS.get(key)
    if known in by_path:
        pdf, score, reason = by_path[known], 103.0, 'Associação documental previamente auditada'
    else:
        pdf, score, reason = best_match(ref, local)
        if pdf is None:
            pdf, score, reason = best_match(ref, library)
    web_resource = key in NON_PDF_RESOURCES or norm(author) == 'delft university of technology'
    status = 'pdf_local' if pdf else ('recurso_web' if web_resource else 'pdf_nao_localizado')
    rows.append({'referencia': asdict(ref), 'estado': status, 'pdf': asdict(pdf) if pdf else None,
                 'pontuacao': score, 'criterio': reason, 'entrada_incompleta': match is None})
result = {'fonte': SOURCE.name, 'paragrafos_bibliograficos': len(entries),
          'entradas_textuais_distintas': len(unique), 'ocorrencias_repetidas': len(entries)-len(unique),
          'correspondencias': rows}
out = Path(__file__).with_name('bibliografia_local.json')
out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
for row in rows:
    if row['estado'] != 'pdf_local' or row['entrada_incompleta']:
        print(row['estado'], row['referencia']['number'], row['referencia']['entry'][:180])
print('Total:', len(rows), 'PDF local:', sum(r['estado'] == 'pdf_local' for r in rows))
