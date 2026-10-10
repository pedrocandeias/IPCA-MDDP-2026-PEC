#!/usr/bin/env python3
"""Export the ODT as standalone HTML with citation popovers and historical excerpts.

Reads Mendeley bookmarks and compressed metadata directly from the ODT. Original
ODT, Markdown and audit files are never changed. Requires pandoc and lxml.
"""
from __future__ import annotations

import base64
import collections
import copy
import csv
import hashlib
import html as html_std
import json
import mimetypes
import os
import re
import subprocess
import tempfile
import unicodedata
import zipfile
import zlib
from difflib import SequenceMatcher
from pathlib import Path

from lxml import etree as ET, html
import fitz
from evidencia_matriz import read_matrix
from importar_explicacoes_citacoes import attach_explanations

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt'
AUDIT = ROOT / 'docs/revisoes/bibliografia/auditoria_referencias_texto_papers_061.md'
MATRIX = ROOT / 'material/bibliografia/auditoria_citacoes/referencias_evidencia_docx_2026-07-22.xlsx'
OUT = ROOT / 'docs/capitulos/html/manuscrito_citacoes'
ASSETS = Path(__file__).with_name('html_citacoes')


def norm(value):
    value = html_std.unescape(value).translate(str.maketrans({'Ø': 'O', 'ø': 'o', 'ı': 'i', 'ł': 'l', 'Ł': 'L'}))
    value = re.sub(r'[\u2010-\u2015\u2212]', ' ', value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', value).strip()


def plain(value):
    return re.sub(r'[*`]', '', value).strip()


def similarity(left, right):
    a, b = norm(left), norm(right)
    if not a or not b:
        return 0.0
    if a in b or b in a:
        return 1.0
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def relative_link(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file() or not path.resolve().is_relative_to(ROOT):
        return None
    from urllib.parse import quote
    return quote(os.path.relpath(path, OUT), safe='/')


def author_label(rec):
    authors = [a.get('family', a.get('literal', '')) for a in rec['authors']]
    name = authors[0] if len(authors) == 1 else (' & '.join(authors) if len(authors) == 2 else (authors[0] + ' et al.' if authors else rec['title']))
    return f"{name} ({rec.get('year') or 's.d.'})"


def reference_text(rec):
    authors = []
    for author in rec['authors']:
        given = author.get('given', '')
        initials = ' '.join(p[0] + '.' for p in re.findall(r'[^\W\d_]+', given, re.U))
        authors.append(author.get('family', author.get('literal', '')) + (', ' + initials if initials else ''))
    byline = ', '.join(authors[:-1]) + ', & ' + authors[-1] if len(authors) > 1 else ', '.join(authors)
    parts = [f"{byline} ({rec.get('year') or 's.d.'}).", rec.get('title', '').rstrip('.') + '.']
    venue = rec.get('container', '')
    if rec.get('volume'):
        venue += ', ' + str(rec['volume'])
    if rec.get('issue'):
        venue += '(' + str(rec['issue']) + ')'
    if rec.get('pages'):
        venue += ', ' + str(rec['pages'])
    if venue:
        parts.append(venue.rstrip('.') + '.')
    elif rec.get('publisher'):
        parts.append(rec['publisher'].rstrip('.') + '.')
    return ' '.join(parts)


def get_citations():
    with zipfile.ZipFile(SOURCE) as archive:
        meta = ET.fromstring(archive.read('meta.xml'))
        groups = collections.defaultdict(dict)
        for entry in meta.findall('.//meta:user-defined', meta.nsmap):
            match = re.fullmatch(r'MLO_DATA_([a-z0-9]+)_(\d+)', entry.get('{' + meta.nsmap['meta'] + '}name', ''))
            if match:
                groups[match[1]][int(match[2])] = entry.text or ''
        data = {key: json.loads(zlib.decompress(base64.urlsafe_b64decode(''.join(v for _, v in sorted(parts.items()))))) for key, parts in groups.items()}
        root = ET.fromstring(archive.read('content.xml'))
    ns = root.nsmap
    active, visible, contexts, order = {}, {}, {}, []

    def append(value):
        for parts in active.values():
            parts.append(value or '')

    def visit(node):
        kind = ET.QName(node).localname
        name = node.get('{' + ns['text'] + '}name', '')
        if kind == 'bookmark-start' and name.startswith('MLO_C_'):
            key = name[6:]
            assert key not in active and key in data
            active[key] = []
            order.append(key)
            paragraph = next(p for p in node.iterancestors() if ET.QName(p).localname in ('p', 'h'))
            contexts[key] = ''.join(paragraph.itertext()).strip()
        if kind == 'bookmark-end' and name.startswith('MLO_C_'):
            key = name[6:]
            visible[key] = ''.join(active.pop(key)).strip()
        append(node.text)
        for child in node:
            visit(child)
            append(child.tail)

    visit(root)
    assert not active and len(order) == len(set(order)) == len(data)
    for key in order:
        assert visible[key], key
        data[key].update({'visible': visible[key], 'context': contexts[key]})
    return root, data, order


def read_audit(records):
    """Extract quoted evidence only from sections with an unambiguous source.

    Multi-source sections are deliberately not attributed as a single paper.
    The source text and historical assessment remain visible to the reader.
    """
    sections = re.split(r'(?m)^(?=#{2,4} )', AUDIT.read_text())
    results = collections.defaultdict(list)
    for section in sections:
        heading = section.split('\n', 1)[0].lstrip('# ').strip()
        fields = re.split(r'(?m)^\*\*([^\n]+?):\*\*', section)
        pairs = list(zip(fields[1::2], fields[2::2]))
        source_titles = [plain(value.strip().split('\n', 1)[0]).split(';', 1)[0].rstrip('.') for label, value in pairs if norm(label).startswith('titulo')]
        ids = {rid for rid in records if rid in section}
        if not ids and len(source_titles) == 1:
            ids = {rid for rid, rec in records.items() if similarity(source_titles[0], rec['title']) >= .96}
        if not ids:
            # Author/year is only a fallback when exactly one record fits.
            for rid, rec in records.items():
                author = norm(rec['authors'][0].get('family', '')) if rec['authors'] else ''
                if str(rec.get('year')) in heading and author and re.search(r'(?<!\w)' + re.escape(author) + r'(?!\w)', norm(heading)):
                    ids.add(rid)
        if len(ids) != 1:
            continue
        rid = next(iter(ids))
        # A section explicitly naming several works cannot supply one source's quotes.
        years_in_heading = re.findall(r'\((?:19|20)\d{2}[a-z]?\)', heading)
        if len(years_in_heading) > 1:
            continue
        claims, quotes, pages, assessment, pdf = [], [], [], '', ''
        for label, value in pairs:
            label = norm(label)
            blocks = re.findall(r'(?m)^> ?(.*(?:\n> ?.*)*)', value)
            quoted = [plain(re.sub(r'(?m)^> ?', '', b)).strip('“”" ') for b in blocks]
            if label.startswith(('texto da dissertacao', 'texto e celulas', 'afirmacoes')):
                claims.extend(quoted)
            if label.startswith(('excerto', 'excertos')):
                quotes.extend(q for q in quoted if q)
            if label.startswith(('pagina', 'zona')):
                pages.append(plain(value.strip().split('\n', 1)[0]))
            if label == 'avaliacao':
                assessment = plain(value.strip().split('\n', 1)[0])
            if label in ('caminho local', 'ficheiro'):
                candidates = re.findall(r'`([^`]+\.pdf)`', value)
                if candidates:
                    pdf = html_std.unescape(candidates[0])
        if quotes:
            results[rid].append({'section': heading, 'claims': claims, 'excerpts': list(dict.fromkeys(quotes)),
                                 'pages': ' '.join(pages), 'assessment': assessment, 'pdf': pdf,
                                 'origin': str(AUDIT.relative_to(ROOT)), 'origin_kind': 'markdown'})
    # Later audit tables store source-specific quotations in their second cell.
    for number, line in enumerate(AUDIT.read_text().splitlines(), 1):
        if not line.startswith('|'):
            continue
        cells = re.split(r'(?<!\\)\|', line)[1:-1]
        if len(cells) < 3:
            continue
        quotes = re.findall(r'“([^”]+)”', cells[1])
        titles = re.findall(r'(?<!\*)\*([^*]+)\*(?!\*)', cells[0])
        ids = {rid for rid, rec in records.items() for title in titles
               if norm(title) == norm(re.sub(r'\s+Authors$', '', rec['title']))}
        if len(ids) != 1 or not quotes:
            continue
        paths = re.findall(r'`([^`]+\.pdf)`', cells[0])
        pdf = paths[0] if paths else ''
        if pdf and '/' not in pdf:
            pdf = 'material/bibliografia/' + pdf
        results[next(iter(ids))].append({'section': f'Tabela de confronto, linha {number}',
            'claims': [], 'excerpts': quotes, 'pages': plain(re.sub(r'“[^”]+”', '', cells[1])),
            'assessment': plain(cells[2]), 'pdf': pdf,
            'origin': str(AUDIT.relative_to(ROOT)), 'origin_kind': 'markdown'})
    return results


def annotate_manual(document, records, data, evidence):
    """Add controls to literal author/year citations lacking a Mendeley bookmark.

    Only unique exact normalized aliases are accepted. Never pick the first
    author/year match when several works share it.
    """
    aliases = collections.defaultdict(set)
    narrative = []
    for rid, rec in records.items():
        names = [a.get('family', a.get('literal', '')) for a in rec['authors']]
        if not names or not rec.get('year'):
            continue
        names = [names[0]] if len(names) == 1 else ([' & '.join(names), ' e '.join(names)] if len(names) == 2 else [names[0]+' et al.'])
        for name in names:
            year = str(rec['year'])
            aliases[norm(name + ', ' + year)].add(rid)
            literal = name + ' (' + year + ')'
            aliases[norm(literal)].add(rid)
            narrative.append(literal)
    narrative_re = re.compile('|'.join(re.escape(s) for s in sorted(set(narrative), key=len, reverse=True)), re.I)
    added = []
    in_bibliography = False
    in_front_matter = True
    in_index = False
    for top in document:
        title = re.sub(r'\s+', ' ', ''.join(top.itertext())).strip()
        if top.tag == 'h1' and title.startswith('Capítulo 1 - '):
            in_front_matter = False
        if top.tag == 'h1' and title.startswith('Índice'):
            in_index = True
        elif top.tag in ('h1', 'h2', 'h3'):
            in_index = False
        if top.tag == 'h1' and title == 'Referências Bibliográficas':
            in_bibliography = True
        elif top.tag == 'h1' and title.startswith('Anexo A'):
            in_bibliography = False
        if in_bibliography or in_front_matter or in_index:
            continue
        blocks = [top] if top.tag in ('p', 'li') and not top.xpath('.//p') else top.xpath('.//p | .//td[not(.//p)] | .//th[not(.//p)]')
        for block in blocks:
            text = ''.join(block.itertext())
            matches = []
            groups = list(re.finditer(r'\([^()\n]*(?:19|20)\d{2}[a-z]?[^()\n]*\)', text)) + list(narrative_re.finditer(text))
            used = set()
            for match in groups:
                if text[match.end():].startswith('*') or match.end() in used:
                    continue
                visible = match.group()
                parts = visible[1:-1].split(';') if visible.startswith('(') else [visible]
                ids = [aliases[norm(part)] for part in parts]
                if not all(len(candidates) == 1 for candidates in ids):
                    continue
                used.add(match.end())
                matches.append((match.end(), visible, [next(iter(candidates)) for candidates in ids]))
            for end, visible, ids in sorted(matches, reverse=True):
                key = 'manual-' + str(len(added)+1)
                cite = {'visible': visible, 'context': text.replace('*', ''), 'association': 'autor_ano_inequivoco',
                        'items': [{'rec': records[rid]} for rid in ids]}
                subset = {key: cite}
                attach_evidence(subset, records, evidence)
                data.update(subset)
                button = html.Element('button', {'class': 'citation-star', 'data-citation': key, 'type': 'button',
                                      'aria-label': f'Consultar {len(ids)} fontes: {visible}', 'aria-haspopup': 'dialog',
                                      'aria-expanded': 'false', 'aria-controls': 'citation-panel'})
                button.text = '*'
                offset = 0
                inserted = False
                for segment in block.xpath('.//text()'):
                    size = len(str(segment))
                    if offset < end <= offset + size:
                        point = end - offset
                        owner = segment.getparent()
                        if segment.is_text:
                            owner.text = str(segment)[:point]
                            button.tail = str(segment)[point:]
                            owner.insert(0, button)
                        else:
                            owner.tail = str(segment)[:point]
                            button.tail = str(segment)[point:]
                            owner.addnext(button)
                        inserted = True
                        break
                    offset += size
                assert inserted, visible
                added.append(key)
    return added


def attach_evidence(data, records, evidence):
    matches_path = ROOT / 'docs/revisoes/manuscrito/sincronizacao_markdown_2026_10_10/bibliografia_local.json'
    matches = json.loads(matches_path.read_text())['correspondencias']
    pending_notes = json.loads((OUT/'excertos_complementares.json').read_text()).get('pending_notes', {})
    for cite in data.values():
        sources = []
        for item in cite['items']:
            rec = item['rec']
            candidates = evidence.get(rec['id'], [])
            ranked = sorted(((max((similarity(cite['context'], c) for c in e['claims']), default=0), e) for e in candidates), key=lambda pair: pair[0], reverse=True)
            selected = copy.deepcopy(ranked[0][1]) if ranked else None
            score = ranked[0][0] if ranked else 0
            if selected:
                selected['context_similarity'] = round(score, 3)
                selected['same_passage'] = score >= .65
            pdf = relative_link(selected['pdf']) if selected and selected['pdf'] else None
            if not pdf:
                for match in matches:
                    doi_matches = rec.get('doi') and rec['doi'].casefold().rstrip('.') in match['referencia']['dois']
                    title_matches = norm(rec['title']) == norm(match['referencia']['title'])
                    if match['pdf'] and (doi_matches or title_matches):
                        pdf = relative_link(match['pdf']['path'])
                        break
            sources.append({'record_id': rec['id'], 'label': author_label(rec), 'title': rec['title'],
                            'reference': reference_text(rec), 'doi': rec.get('doi', ''), 'url': rec.get('url', ''),
                            'locator': item.get('locator', ''), 'pdf': pdf, 'evidence': selected,
                            'pending_note': pending_notes.get(rec['id'], '') if not selected else ''})
        cite['sources'] = sources
        del cite['items']


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    original_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    root, data, order = get_citations()
    records = {item['rec']['id']: item['rec'] for cite in data.values() for item in cite['items']}
    evidence = read_audit(records)
    matrix_evidence, matrix_report = read_matrix(MATRIX, ROOT, records, norm)
    for rid, entries in matrix_evidence.items():
        if not evidence.get(rid):
            evidence[rid].extend(entries)
    supplement = OUT/'excertos_complementares.json'
    for entry in json.loads(supplement.read_text())['entries']:
        path = ROOT/entry['pdf']
        assert entry['record_id'] in records
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256_pdf'], path
        with fitz.open(path) as pdf:
            text = norm(pdf[entry['pdf_page']-1].get_text()).replace(' ', '')
        assert all(norm(q).replace(' ', '') in text for q in entry['excerpts']), path
        evidence[entry['record_id']] = [entry]
    (OUT/'recuperacao_matriz.json').write_text(json.dumps(matrix_report, ensure_ascii=False, indent=2)+'\n')
    attach_evidence(data, records, evidence)
    ns = root.nsmap
    for node in root.findall('.//text:bookmark-end', ns):
        name = node.get('{' + ns['text'] + '}name', '')
        if name.startswith('MLO_C_'):
            node.tail = 'CITPOP' + name[6:] + 'END' + (node.tail or '')
    with tempfile.TemporaryDirectory(prefix='mestrado_html_') as tmpname:
        tmp = Path(tmpname)
        prepared = tmp/'source.odt'
        with zipfile.ZipFile(SOURCE) as archive, zipfile.ZipFile(prepared, 'w') as out:
            for info in archive.infolist():
                out.writestr(copy.copy(info), ET.tostring(root) if info.filename == 'content.xml' else archive.read(info.filename))
        subprocess.run(['python3', str(ROOT/'tools/conversao/sincronizar_manuscrito_odt.py'), str(prepared),
                        '--output', str(tmp/'source.md'), '--assets', str(tmp/'images'),
                        '--report', str(tmp/'conversion.json'), '--version', '0.4.114'], check=True, capture_output=True)
        markdown = (tmp/'source.md').read_text()
        markdown = re.sub(r'^Versão do documento:.*?-->\s*', '', markdown, count=1, flags=re.S)
        rendered = subprocess.check_output(['pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none'], input=markdown, text=True)
        document = html.fragment_fromstring(rendered, create_parent='article')
        document.set('id', 'manuscrito')
        for image in document.xpath('.//img'):
            path = Path(image.get('src'))
            mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
            image.set('src', 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode())
            image.set('loading', 'lazy')
        # Work on serialized HTML: the markers are alphanumeric and cannot split tags.
        marked = html.tostring(document, encoding='unicode')
        added = []
        def button(match):
            key = match[1]
            cite = data[key]
            count = len(cite['sources'])
            label = html_std.escape(f"Consultar {count} {'fonte' if count == 1 else 'fontes'}: {cite['visible']}", quote=True)
            added.append(key)
            return f'<button class="citation-star" data-citation="{key}" aria-label="{label}" aria-haspopup="dialog" aria-expanded="false" aria-controls="citation-panel" type="button">*</button>'
        marked = re.sub(r'CITPOP([a-f0-9]+)END', button, marked)
        assert added == order, (len(added), len(order))
        document = html.fromstring(marked)
        manual = annotate_manual(document, records, data, evidence)
        order.extend(manual)
        attach_explanations(data)
        # Citation controls must not inherit italics/bold styles from the source.
        navigation = []
        for i, heading in enumerate(document.xpath('.//h1'), 1):
            title = re.sub(r'\s+', ' ', ''.join(heading.itertext())).strip()
            if re.match(r'Capítulo \d+ - |Anexo [A-D] - |Referências Bibliográficas', title):
                heading.set('id', f'seccao-{i}')
                short = re.sub(r'^Capítulo (\d+) - ', r'\1. ', title)
                navigation.append(f'<a href="#seccao-{i}">{html_std.escape(short)}</a>')
        citation_json = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
        payload = (ASSETS/'template.html').read_text()
        replacements = {'{{CSS}}': (ASSETS/'style.css').read_text(), '{{JS}}': (ASSETS/'script.js').read_text(),
                        '{{CONTENT}}': html.tostring(document, encoding='unicode'), '{{NAVIGATION}}': '\n'.join(navigation),
                        '{{CITATIONS}}': citation_json, '{{COUNT}}': str(len(data))}
        for key, value in replacements.items():
            payload = payload.replace(key, value)
        (OUT/'pedro_candeias_manuscrito_citacoes.html').write_text(payload)
    (OUT/'citacoes.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    with (OUT/'cobertura_excertos.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['marcador_odt', 'citacao', 'obra', 'doi', 'excerto_disponivel', 'similaridade_contexto', 'secao_auditoria', 'origem', 'tipo_origem'])
        for key in order:
            for s in data[key]['sources']:
                e = s['evidence'] or {}
                writer.writerow([key, data[key]['visible'], s['label'], s['doi'], bool(e), e.get('context_similarity', ''), e.get('section', ''), e.get('origin', ''), e.get('origin_kind', '')])
    with (OUT/'excertos_pendentes.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['marcador', 'obra', 'titulo', 'contexto', 'nota'])
        for key, cite in data.items():
            for source in cite['sources']:
                if not source['evidence']:
                    writer.writerow([key, source['label'], source['title'], cite['context'], source['pending_note']])
    items = [s for c in data.values() for s in c['sources']]
    report = {'source': SOURCE.name, 'sha256_odt': original_hash, 'audit': str(AUDIT.relative_to(ROOT)),
              'sha256_audit': hashlib.sha256(AUDIT.read_bytes()).hexdigest(), 'citations': len(data),
              'matrix': str(MATRIX.relative_to(ROOT)), 'sha256_matrix': hashlib.sha256(MATRIX.read_bytes()).hexdigest(),
              'supplement': str(supplement.relative_to(ROOT)), 'sha256_supplement': hashlib.sha256(supplement.read_bytes()).hexdigest(),
              'source_occurrences': len(items), 'unique_sources': len(records),
              'source_occurrences_with_explanation': sum(bool(s.get('explanation')) for s in items),
              'sha256_explanations': hashlib.sha256((OUT/'explicacoes_citacoes.json').read_bytes()).hexdigest(),
              'multiple_source_citations': sum(len(c['sources']) > 1 for c in data.values()),
              'maximum_sources_per_citation': max(len(c['sources']) for c in data.values()),
              'mendeley_citations': len(data) - len(manual), 'manual_citations_matched_by_author_year': len(manual),
              'source_occurrences_with_excerpt': sum(bool(s['evidence']) for s in items),
              'source_occurrences_with_historical_excerpt': sum(bool(s['evidence'] and s['evidence']['origin_kind'] != 'pdf') for s in items),
              'source_occurrences_with_similar_historical_passage': sum(bool(s['evidence'] and s['evidence']['origin_kind'] != 'pdf' and s['evidence']['same_passage']) for s in items),
              'selected_excerpt_origins': dict(collections.Counter(s['evidence']['origin_kind'] for s in items if s['evidence'])),
              'note': 'Distinguem-se auditorias históricas e consultas diretas de PDF. A semelhança textual não é uma validação da afirmação atual.'}
    (OUT/'manifesto.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == original_hash
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    build()
