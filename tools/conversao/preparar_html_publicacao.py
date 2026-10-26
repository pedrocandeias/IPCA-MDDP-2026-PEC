#!/usr/bin/env python3
"""Prepare the annotated manuscript and thesis PDF for static hosting."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
from html import escape
from string import Template

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / 'docs/capitulos/html/manuscrito_citacoes'
SOURCE = SOURCE_DIR / 'pedro_candeias_manuscrito_citacoes.html'
OUTPUT = SOURCE_DIR / 'publicacao'
HOMEPAGE = Path(__file__).resolve().parent / 'homepage'
DEFENSE = ROOT / 'docs/defesa'
# Lista explícita: o guia pessoal em guia_leitura_local nunca é publicado.
DEFENSE_FILES = {
    'apresentacao_defesa.pdf': 'apresentacao/apresentacao_defesa.pdf',
    'apresentacao_defesa.pptx': 'apresentacao/apresentacao_defesa.pptx',
    'guiao_falado.pdf': 'apresentacao/guiao_falado.pdf',
    'guiao_falado.odt': 'apresentacao/guiao_falado.odt',
    'preparacao_defesa.pdf': 'preparacao_defesa_bernardo_providencia.pdf',
    'preparacao_defesa.odt': 'preparacao_defesa_bernardo_providencia.odt',
    'perguntas_juri.pdf': 'perguntas_juri.pdf',
    'perguntas_juri.odt': 'perguntas_juri.odt',
}


def manuscript_pdf(dist):
    manifest = json.loads((SOURCE_DIR / 'manifesto.json').read_text())
    source_odt = ROOT / manifest['source']
    if hashlib.sha256(source_odt.read_bytes()).hexdigest() != manifest['sha256_odt']:
        raise RuntimeError('Regenerar o HTML a partir da versão atual do manuscrito.')
    source = source_odt.with_suffix('.pdf')
    if source.stat().st_mtime < source_odt.stat().st_mtime:
        raise RuntimeError('Exportar o PDF da versão atual do manuscrito antes de publicar.')
    target = dist / 'tese.pdf'
    shutil.copy2(source, target)
    return {'source': str(source.relative_to(ROOT)), 'published': target.name,
            'source_odt': str(source_odt.relative_to(ROOT)),
            'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}


def defense_documents(dist):
    destination = dist / 'defesa'
    destination.mkdir(exist_ok=True)
    files = []
    for name, relative_source in DEFENSE_FILES.items():
        source = DEFENSE / relative_source
        target = destination / name
        shutil.copy2(source, target)
        files.append({'source': str(source.relative_to(ROOT)),
                      'published': 'defesa/' + name,
                      'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    return files


def homepage(dist):
    assets = dist / 'assets'
    assets.mkdir(exist_ok=True)
    shutil.copy2(HOMEPAGE.parent / 'tema_handfab.css', assets / 'tema_handfab.css')
    shutil.copy2(HOMEPAGE / 'style.css', assets / 'homepage.css')
    for name in ('lightbox.css', 'lightbox.js'):
        shutil.copy2(HOMEPAGE / name, assets / name)
    shutil.copy2(ROOT / 'docs/defesa/apresentacao/assets/phoenix_montagem.jpg', assets / 'phoenix_montagem.jpg')
    template = Template((HOMEPAGE / 'template.html').read_text())
    for language, content in json.loads((HOMEPAGE / 'conteudo.json').read_text()).items():
        values = {key: escape(value, quote=True) for key, value in content.items() if isinstance(value, str)}
        values['language_links'] = ''.join(
            f'<a href="{filename}" lang="{lang}" hreflang="{lang}" aria-label="{label}"' +
            (' aria-current="page"' if key == language else '') + f'>{key.upper()}</a>'
            for key, filename, lang, label in [('pt', 'index.html', 'pt-PT', 'Português'), ('en', 'en.html', 'en', 'English')])
        values['tool_rows'] = ''.join(
            f'<article class="tool-row"><span class="tool-number" aria-hidden="true">{i:02}</span>'
            f'<h4>{escape(tool["name"])}</h4><p>{escape(tool["text"])}</p>'
            f'<a href="{escape(tool["url"], quote=True)}">{escape(tool["link"])} <span aria-hidden="true">↗</span></a></article>'
            for i, tool in enumerate(content['tools'], 1))
        (dist / content['file']).write_text(template.substitute(values))


def main(manuscript_only=False, preserve_defense=False):
    dist = OUTPUT / 'dist'
    dist.mkdir(parents=True, exist_ok=True)
    pdf = manuscript_pdf(dist)
    source = SOURCE.read_text()
    pattern = re.compile(r'(<script id="citation-data" type="application/json">)(.*?)(</script>)', re.S)
    match = pattern.search(source)
    if not match:
        raise RuntimeError('Não foi encontrado o conjunto de dados das citações.')
    citations = json.loads(match[2])
    removed = 0
    for citation in citations.values():
        for item in citation['sources']:
            removed += bool(item.get('pdf'))
            item['pdf'] = None
    encoded = json.dumps(citations, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    deployed = source[:match.start(2)] + encoded + source[match.end(2):]
    marker = '<button class="print-button"'
    if marker not in deployed:
        raise RuntimeError('Não foi encontrado o cabeçalho para a ligação de regresso.')
    actions = ('<a class="print-button" href="index.html">Início / Home</a>\n    '
               f'<a class="print-button" id="download-pdf" href="{pdf["published"]}?v={pdf["sha256"][:12]}" '
               'download="pedro-candeias-dissertacao.pdf" aria-label="Descarregar a última versão da dissertação em PDF">'
               '<svg class="download-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/></svg>Descarregar PDF</a>\n    ')
    deployed = deployed.replace(marker, actions + marker, 1)
    deployed = deployed.replace('</head>', '<link rel="stylesheet" href="assets/lightbox.css">\n<script src="assets/lightbox.js" defer></script>\n</head>', 1)
    target = dist/'manuscrito.html'
    target.write_text(deployed)
    if not manuscript_only:
        homepage(dist)
    if manuscript_only or preserve_defense:
        defense_files = json.loads((OUTPUT / 'manifesto_publicacao.json').read_text())['defense_files']
    else:
        defense_files = defense_documents(dist)
    report = {'source': str(SOURCE.relative_to(ROOT)), 'sha256_source': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'entrypoint': 'dist/index.html', 'manuscript': 'dist/manuscrito.html',
              'sha256_index': hashlib.sha256((dist/'index.html').read_bytes()).hexdigest(),
              'sha256_manuscript': hashlib.sha256(target.read_bytes()).hexdigest(),
              'manuscript_pdf': pdf,
              'homepage_sources': str(HOMEPAGE.relative_to(ROOT)),
              'shared_theme': 'tools/conversao/tema_handfab.css',
              'sha256_theme': hashlib.sha256((HOMEPAGE.parent/'tema_handfab.css').read_bytes()).hexdigest(),
              'image_source': 'docs/defesa/apresentacao/assets/phoenix_montagem.jpg',
              'languages': ['pt-PT', 'en'],
              'defense_files': defense_files,
              'private_guide_published': False,
              'citations': len(citations), 'local_pdf_links_removed': removed,
              'includes_library_pdfs': False, 'external_links': 'DOI/URL existentes nas referências',
              'method': 'tools/conversao/preparar_html_publicacao.py'}
    (OUTPUT/'manifesto_publicacao.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manuscript-only', action='store_true', help='Atualizar apenas o manuscrito HTML e PDF, preservando a homepage e a defesa publicadas.')
    parser.add_argument('--preserve-defense', action='store_true', help='Atualizar o site e a dissertação sem substituir os documentos da defesa já preparados.')
    args = parser.parse_args()
    main(manuscript_only=args.manuscript_only, preserve_defense=args.preserve_defense)
