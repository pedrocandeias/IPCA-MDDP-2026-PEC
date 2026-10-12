#!/usr/bin/env python3
"""Prepare the annotated manuscript for static hosting without local PDF links."""
from pathlib import Path
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
}


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
    shutil.copy2(HOMEPAGE / 'style.css', assets / 'homepage.css')
    for name in ('lightbox.css', 'lightbox.js'):
        shutil.copy2(HOMEPAGE / name, assets / name)
    shutil.copy2(ROOT / 'docs/defesa/apresentacao/assets/phoenix_montagem.jpg', assets / 'phoenix_montagem.jpg')
    template = Template((HOMEPAGE / 'template.html').read_text())
    for language, content in json.loads((HOMEPAGE / 'conteudo.json').read_text()).items():
        values = {key: escape(value, quote=True) for key, value in content.items() if isinstance(value, str)}
        values['language_links'] = ''.join(
            f'<a href="{filename}" lang="{lang}" hreflang="{lang}"' +
            (' aria-current="page"' if key == language else '') + f'>{label}</a>'
            for key, filename, lang, label in [('pt', 'index.html', 'pt-PT', 'Português'), ('en', 'en.html', 'en', 'English')])
        values['tool_rows'] = ''.join(
            f'<article class="tool-row"><span class="tool-number" aria-hidden="true">{i:02}</span>'
            f'<h4>{escape(tool["name"])}</h4><p>{escape(tool["text"])}</p>'
            f'<a href="{escape(tool["url"], quote=True)}">{escape(tool["link"])} <span aria-hidden="true">↗</span></a></article>'
            for i, tool in enumerate(content['tools'], 1))
        (dist / content['file']).write_text(template.substitute(values))


def main():
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
    deployed = deployed.replace(marker, '<a class="print-button" href="index.html">Início / Home</a>\n    ' + marker, 1)
    deployed = deployed.replace('</head>', '<link rel="stylesheet" href="assets/lightbox.css">\n<script src="assets/lightbox.js" defer></script>\n</head>', 1)
    dist = OUTPUT / 'dist'
    dist.mkdir(parents=True, exist_ok=True)
    target = dist/'manuscrito.html'
    target.write_text(deployed)
    homepage(dist)
    defense_files = defense_documents(dist)
    report = {'source': str(SOURCE.relative_to(ROOT)), 'sha256_source': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'entrypoint': 'dist/index.html', 'manuscript': 'dist/manuscrito.html',
              'sha256_index': hashlib.sha256((dist/'index.html').read_bytes()).hexdigest(),
              'sha256_manuscript': hashlib.sha256(target.read_bytes()).hexdigest(),
              'homepage_sources': str(HOMEPAGE.relative_to(ROOT)),
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
    main()
