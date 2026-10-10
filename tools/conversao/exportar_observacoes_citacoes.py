#!/usr/bin/env python3
"""Export citation notes to an editable UTF-8 TXT without overwriting revisions."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from lxml import html

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'docs/capitulos/html/manuscrito_citacoes/citacoes.json'
HTML = SOURCE.with_name('pedro_candeias_manuscrito_citacoes.html')
OUTPUT = ROOT / 'docs/revisoes/bibliografia/explicacoes_citacoes.txt'


def export(destination: Path):
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    document = html.fromstring(HTML.read_text(encoding='utf-8'))
    buttons = document.xpath('//article//button[contains(concat(" ", normalize-space(@class), " "), " citation-star ")]')
    keys = [button.get('data-citation') for button in buttons]
    assert len(keys) == len(set(keys)) and set(keys) == set(data)
    total = sum(len(cite['sources']) for cite in data.values())
    lines = [
        'EXPLICAÇÕES DAS CITAÇÕES — CADERNO DE REESCRITA',
        '',
        'Objetivo: substituir o bloco «Texto auditado e avaliação histórica» por uma',
        'explicação da relação entre cada fonte e a passagem atual do manuscrito.',
        '',
        f'Conteúdo: {total} entradas, agrupadas em {len(keys)} citações, pela ordem do manuscrito.',
        'A mesma obra pode aparecer várias vezes porque a explicação depende da passagem.',
        '',
        'COMO EDITAR',
        'Escrever no campo «EXPLICAÇÃO REESCRITA» de cada fonte. Indicar a ideia que a',
        'fonte sustenta e a sua relação com o texto; delimitar o apoio quando for parcial.',
        'As observações atuais são transcrições dos registos existentes, não novas',
        'validações. Os campos de reescrita ficam em branco para revisão pelo autor.',
        'Manter os identificadores CITAÇÃO e FONTE para associar a revisão ao tooltip.',
        'Os campos sem excerto devem explicar a pendência, sem presumir suporte.',
        '',
        'PROVENIÊNCIA E GERAÇÃO',
        f'Dados: {SOURCE.relative_to(ROOT)}',
        f'SHA-256 dos dados: {hashlib.sha256(SOURCE.read_bytes()).hexdigest()}',
        f'Ordem: {HTML.relative_to(ROOT)}',
        'Método: python3 tools/conversao/exportar_observacoes_citacoes.py',
        'O exportador recusa substituir um TXT existente, para preservar a reescrita.',
        'Para uma nova exportação, usar --output /tmp/explicacoes_citacoes.txt.',
        '',
    ]
    entry = 0
    for group, (key, button) in enumerate(zip(keys, buttons), 1):
        cite = data[key]
        headings = button.xpath('preceding::*[self::h1 or self::h2 or self::h3]')
        heading = ' '.join(headings[-1].text_content().split()) if headings else 'Sem título de secção'
        lines.extend([
            '=' * 78,
            f'CITAÇÃO {group:03d}/{len(keys)} | ID: {key}',
            f'SECÇÃO: {heading}',
            f'CITAÇÃO NO TEXTO: {cite["visible"]}',
            '', 'PASSAGEM ATUAL DO MANUSCRITO:', cite['context'], '',
        ])
        for position, source in enumerate(cite['sources'], 1):
            entry += 1
            evidence = source['evidence'] or {}
            lines.extend([
                '-' * 78,
                f'ENTRADA {entry:03d}/{total} | FONTE {position}/{len(cite["sources"])}',
                f'ID DA FONTE: {source["record_id"]}',
                f'REFERÊNCIA: {source["reference"]}',
            ])
            if source['doi']:
                lines.append('LIGAÇÃO: https://doi.org/' + source['doi'])
            elif source['url']:
                lines.append('LIGAÇÃO: ' + source['url'])
            lines.extend(['', 'EXCERTO(S) DISPONÍVEL(EIS):'])
            for number, excerpt in enumerate(evidence.get('excerpts', []), 1):
                lines.append(f'{number}. {excerpt}')
            if not evidence.get('excerpts'):
                lines.append('Sem excerto associado.')
            if evidence.get('pages'):
                lines.append('PÁGINA / LOCALIZAÇÃO: ' + evidence['pages'])
            if evidence.get('claims'):
                lines.extend(['', 'PASSAGEM ANTERIORMENTE ASSOCIADA À FONTE:'])
                lines.extend(evidence['claims'])
            lines.extend(['', 'OBSERVAÇÃO ATUAL:'])
            lines.append(evidence.get('assessment') or source.get('pending_note') or 'Sem avaliação registada.')
            if evidence.get('review_note'):
                lines.append('NOTA DE ATRIBUIÇÃO: ' + evidence['review_note'])
            if evidence.get('origin_kind') == 'xlsx' and not evidence.get('pdf_text_verified'):
                lines.append('NOTA DE TRANSCRIÇÃO: o texto preservado na matriz não foi integralmente confirmado pela extração automática do PDF.')
            lines.extend(['', 'EXPLICAÇÃO REESCRITA:', '', '', 'FIM DA EXPLICAÇÃO', ''])
    assert entry == total
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('x', encoding='utf-8') as output:
        output.write('\n'.join(lines) + '\n')
    print(f'{destination}: {len(keys)} citações, {entry} entradas.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    export(parser.parse_args().output)
