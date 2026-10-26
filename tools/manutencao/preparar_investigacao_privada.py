#!/usr/bin/env python3
"""Restabelecer os caminhos locais de trabalho após inicializar o submódulo privado."""
import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / 'investigacao_privada/docs/migracao/configuracao.json'


def main(check=False):
    private = ROOT / 'investigacao_privada'
    if not (private / 'README.md').is_file() or not CONFIG.is_file():
        raise SystemExit('Inicialize primeiro o submódulo autorizado: git submodule update --init --checkout investigacao_privada')
    config = json.loads(CONFIG.read_text())
    problems = []
    for entry in config['mappings']:
        if not entry['compatibility_link']:
            continue
        original = ROOT / entry['source']
        target = private / entry['target']
        if not target.exists():
            problems.append(f'Ficheiro privado em falta: {entry["target"]}')
        elif original.is_symlink() and original.resolve() == target.resolve():
            continue
        elif original.exists() or original.is_symlink():
            problems.append(f'Caminho local ocupado, preservado: {entry["source"]}')
        elif check:
            problems.append(f'Ligação local em falta: {entry["source"]}')
        else:
            original.parent.mkdir(parents=True, exist_ok=True)
            original.symlink_to(os.path.relpath(target, original.parent), target_is_directory=target.is_dir())
            print(f'Ligação local criada: {entry["source"]}')
    if problems:
        raise SystemExit('\n'.join(problems))
    print('Caminhos locais da investigação privada verificados.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verificar sem criar ligações.')
    main(check=parser.parse_args().check)
