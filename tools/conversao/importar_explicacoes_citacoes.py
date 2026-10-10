#!/usr/bin/env python3
"""Associate the author's rewritten TXT notes with citation/source identifiers."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOTES = ROOT / 'docs/revisoes/bibliografia'
OUT = ROOT / 'docs/capitulos/html/manuscrito_citacoes'


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def import_notes():
    full_path = NOTES / 'explicacoes_citacoes_reescritas.txt'
    simple_path = NOTES / 'explicacoes_citacoes_versao_simples.txt'
    full = full_path.read_text(encoding='utf-8')
    simple = simple_path.read_text(encoding='utf-8')
    data = json.loads((OUT / 'citacoes.json').read_text())
    groups = list(re.finditer(r'^CITAÇÃO (\d+)/(\d+) \| ID: (\S+)\s*$', full, re.M))
    simplified = re.split(r'^CITAÇÃO (?=\d+/\d+ \| ENTRADA )', simple, flags=re.M)[1:]
    explanations = {}
    count = 0
    assert len(groups) == len(data), 'Número de citações alterado'
    for group_index, match in enumerate(groups):
        number, total, key = match.groups()
        assert int(number) == group_index + 1 and int(total) == len(data)
        assert key in data and key not in explanations, key
        block = full[match.end():groups[group_index + 1].start() if group_index + 1 < len(groups) else len(full)]
        context = re.search(r'PASSAGEM ATUAL DO MANUSCRITO:\n(.*?)\n-{20,}', block, re.S).group(1).strip()
        assert context == data[key]['context'], f'Contexto alterado: {key}'
        entries = list(re.finditer(r'^ENTRADA (\d+)/(\d+) \| FONTE (\d+)/(\d+)\s*$', block, re.M))
        assert len(entries) == len(data[key]['sources']), key
        sources = {}
        for index, entry in enumerate(entries):
            count += 1
            serial, source_total, position, group_total = map(int, entry.groups())
            assert serial == count and source_total == len(simplified)
            assert position == index + 1 and group_total == len(entries)
            section = block[entry.end():entries[index + 1].start() if index + 1 < len(entries) else len(block)]
            rid = re.search(r'^ID DA FONTE: (.+)$', section, re.M).group(1)
            reference = re.search(r'^REFERÊNCIA: (.+)$', section, re.M).group(1)
            source = data[key]['sources'][index]
            assert rid == source['record_id'] and reference == source['reference'], (key, rid)
            note = re.search(r'EXPLICAÇÃO REESCRITA:\n(.*?)\nFIM DA EXPLICAÇÃO', section, re.S).group(1).strip()
            assert note and rid not in sources, (key, rid)
            short = simplified[count - 1]
            header = re.match(r'(\d+)/(\d+) \| ENTRADA (\d+)/(\d+) \| FONTE (\d+)/(\d+)', short)
            assert tuple(map(int, header.groups())) == (int(number), len(data), count, len(simplified), position, group_total)
            assert re.search(r'^ID DA FONTE: (.+)$', short, re.M).group(1) == rid
            short_note = re.search(r'EXPLICAÇÃO REESCRITA:\n(.*?)(?=\n-{20,}|\Z)', short, re.S).group(1).strip()
            assert short_note == note, f'Versões divergentes: entrada {count}'
            sources[rid] = {'reference': reference, 'explanation': note}
        explanations[key] = {'context_sha256': digest(context), 'sources': sources}
    assert count == len(simplified) == sum(len(c['sources']) for c in data.values())
    payload = {
        'method': 'tools/conversao/importar_explicacoes_citacoes.py',
        'note': 'Textos fornecidos pelo autor, preservados literalmente; não constituem uma nova verificação integral das fontes.',
        'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in (full_path, simple_path)],
        'citations_count': len(explanations), 'explanations_count': count,
        'citations': explanations,
    }
    (OUT / 'explicacoes_citacoes.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{count} explicações concordantes, associadas a {len(explanations)} citações.')


def attach_explanations(data):
    payload = json.loads((OUT / 'explicacoes_citacoes.json').read_text())
    notes = payload['citations']
    assert set(notes) == set(data), 'Reimportar explicações: citações alteradas'
    for key, cite in data.items():
        entry = notes[key]
        assert entry['context_sha256'] == digest(cite['context']), f'Rever explicação: contexto alterado em {key}'
        assert set(entry['sources']) == {s['record_id'] for s in cite['sources']}, key
        for source in cite['sources']:
            note = entry['sources'][source['record_id']]
            assert note['reference'] == source['reference'] and note['explanation'].strip(), (key, source['record_id'])
            source['explanation'] = note['explanation']


if __name__ == '__main__':
    import_notes()
