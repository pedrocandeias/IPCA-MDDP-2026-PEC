#!/usr/bin/env python3
"""Convert the current ODT to reviewable Markdown; never modify the source ODT.

Requires pandoc and lxml. Back up the canonical Markdown before replacing it.
The version argument identifies the Markdown revision, not an ODT revision.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

from lxml import etree as ET


def walk(value):
    if isinstance(value, dict):
        yield value
        yield from walk(value.get('c'))
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


def text(value):
    if isinstance(value, dict):
        if value.get('t') == 'Str':
            return value['c']
        if value.get('t') in ('Space', 'SoftBreak', 'LineBreak'):
            return ' '
        return text(value.get('c'))
    if isinstance(value, list):
        return ''.join(map(text, value))
    return ''


def clean(value, targets):
    if isinstance(value, list):
        result = []
        for item in value:
            if isinstance(item, dict):
                kind = item.get('t')
                if kind == 'BlockQuote':
                    # The ODT reader represents every IPCA body paragraph as a quote.
                    result.extend(clean(item['c'], targets))
                    continue
                if kind == 'OrderedList' and re.fullmatch(r'Capítulo \d+ - .+', text(item)):
                    result.extend(clean(item['c'][1][0], targets))
                    continue
                if kind == 'Span' and item['c'][0][0] not in targets:
                    result.extend(clean(item['c'][1], targets))
                    continue
                if kind in ('Strong', 'Emph') and not text(item).strip():
                    continue
                if kind in ('Strong', 'Emph'):
                    contents = clean(item['c'], targets)
                    before, after = [], []
                    while contents and contents[0].get('t') == 'Space':
                        before.append(contents.pop(0))
                    while contents and contents[-1].get('t') == 'Space':
                        after.insert(0, contents.pop())
                    result.extend(before)
                    result.append({'t': kind, 'c': contents})
                    result.extend(after)
                    continue
            converted = clean(item, targets)
            if isinstance(converted, dict) and converted.get('t') in ('Para', 'Header'):
                if not text(converted).strip() and not any(
                    n.get('t') in ('Image', 'Span') for n in walk(converted)
                ):
                    continue
            result.append(converted)
        return result
    if isinstance(value, dict):
        return {key: clean(val, targets) if key == 'c' else val for key, val in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--assets', type=Path, required=True, help='Path relative to the repository root')
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--version', required=True)
    args = parser.parse_args()
    original = args.source.read_bytes()
    manifest = []
    with zipfile.ZipFile(args.source) as archive, tempfile.TemporaryDirectory() as tmp:
        root = ET.fromstring(archive.read('content.xml'))
        ns = root.nsmap
        body = root.find('office:body/office:text', ns)
        # LibreOffice form fields contain visible text that pandoc otherwise drops.
        for node in root.findall('.//loext:content-control', ns):
            node.tag = '{' + ns['text'] + '}span'
            node.attrib.clear()
        for node in root.findall('.//draw:frame', ns):
            if node.find('draw:image', ns) is not None:
                node.set('{' + ns['text'] + '}anchor-type', 'as-char')
        # Pandoc 3.1.3 drops ODT table-header-rows, including their text/images.
        for node in root.findall('.//table:table-header-rows', ns):
            parent = node.getparent()
            pos = parent.index(node)
            for row in list(node):
                parent.insert(pos, row)
                pos += 1
            parent.remove(node)
        # Preserve generated indices as ordinary paragraphs, including PDF page labels.
        for node in list(body):
            if ET.QName(node).localname not in ('table-of-content', 'illustration-index'):
                continue
            index_body = node.find('text:index-body', ns)
            pos = body.index(node)
            if index_body is not None:
                for child in index_body:
                    children = list(child) if ET.QName(child).localname == 'index-title' else [child]
                    for entry in children:
                        body.insert(pos, copy.deepcopy(entry))
                        pos += 1
            body.remove(node)
        prepared = Path(tmp) / 'source.odt'
        with zipfile.ZipFile(prepared, 'w') as out:
            for info in archive.infolist():
                out.writestr(copy.copy(info), ET.tostring(root) if info.filename == 'content.xml' else archive.read(info.filename))
        result = subprocess.run(['pandoc', str(prepared), '-f', 'odt', '-t', 'json'], check=True, capture_output=True)
        ast = json.loads(result.stdout)
        targets = {n['c'][-1][0][1:] for n in walk(ast['blocks']) if n.get('t') == 'Link' and n['c'][-1][0].startswith('#')}
        ast['blocks'] = clean(ast['blocks'], targets)
        for block in ast['blocks']:
            if block['t'] == 'Para' and text(block).strip() == 'Referências Bibliográficas':
                block['t'] = 'Header'
                block['c'] = [1, ['', [], []], block['c']]
        args.assets.mkdir(parents=True, exist_ok=True)
        seen = {}
        for node in walk(ast['blocks']):
            if node.get('t') != 'Image':
                continue
            member = node['c'][-1][0]
            if member not in seen:
                data = archive.read(member)
                path = args.assets / f'imagem_{len(seen)+1:02d}{Path(member).suffix.lower()}'
                if path.exists() and path.read_bytes() != data:
                    raise RuntimeError(f'Asset collision: {path}')
                path.write_bytes(data)
                seen[member] = path.as_posix()
                manifest.append({'origem_odt': member, 'destino': str(path), 'sha256': hashlib.sha256(data).hexdigest()})
            node['c'][-1][0] = seen[member]
        nodes = list(walk(ast['blocks']))
        # Keep usable targets; turn unresolved ODT-only page references into plain text.
        ids = {n['c'][0][0] for n in nodes if n.get('t') == 'Span'}
        unresolved = []
        for node in nodes:
            if node.get('t') == 'Link' and node['c'][-1][0].startswith('#') and node['c'][-1][0][1:] not in ids:
                unresolved.append(node['c'][-1][0])
                node['t'], node['c'] = 'Span', [['', [], []], node['c'][1]]
        output = subprocess.run(['pandoc', '-f', 'json', '-t', 'gfm', '--wrap=none'], input=json.dumps(ast), text=True, capture_output=True, check=True).stdout
        preamble = f'Versão do documento: {args.version}\n\n<!-- Fonte: {args.source.name}; sincronização textual por tools/conversao/sincronizar_manuscrito_odt.py. -->\n\n'
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(preamble + output, encoding='utf-8')
        stats = {kind: sum(n.get('t') == kind for n in nodes) for kind in ('Header', 'Table', 'Image', 'Note')}
        stats.update({'fonte': str(args.source), 'sha256_fonte': hashlib.sha256(original).hexdigest(), 'versao_markdown': args.version,
                      'pandoc': subprocess.check_output(['pandoc', '--version'], text=True).splitlines()[0],
                      'referencias_internas_sem_destino_convertidas_em_texto': sorted(set(unresolved)), 'imagens': manifest})
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(stats, ensure_ascii=False, indent=2)+'\n')
        (args.assets/'proveniencia.json').write_text(json.dumps({'fonte': str(args.source), 'metodo': 'Extração direta do ZIP ODT por tools/conversao/sincronizar_manuscrito_odt.py; sem alteração das imagens.', 'imagens': manifest}, ensure_ascii=False, indent=2)+'\n')
    assert args.source.read_bytes() == original
    print(json.dumps({k:v for k,v in stats.items() if k not in ('imagens', 'referencias_internas_sem_destino_convertidas_em_texto')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
