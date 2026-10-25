#!/usr/bin/env python3
"""Lê a fala por diapositivo e exporta o guião para ODT através do Pandoc."""
from pathlib import Path
from zipfile import ZipFile
import json
import re
import subprocess
from lxml import etree as ET

HERE = Path(__file__).resolve().parent


def ler_falas():
    source = (HERE / 'guiao_falado.md').read_text(encoding='utf-8')
    result = {}
    for section in re.split(r'^## ', source, flags=re.M)[1:]:
        heading = section.splitlines()[0]
        number, title = heading.split('. ', 1)
        parts = {}
        for part in re.split(r'^### ', section, flags=re.M)[1:]:
            label, body = part.split('\n', 1)
            parts[label] = body.strip()
        result[int(number)] = {
            'titulo': title,
            'fala': parts['O que quero dizer'],
            'aprofundamento': parts.get('Se precisar de desenvolver', ''),
            'indicacao': parts['Lembrar-me'],
        }
    assert list(result) == list(range(1, 31))
    return result


def main():
    records = ler_falas()
    reference = HERE.parent / 'preparacao_defesa_bernardo_providencia.odt'
    output = HERE / 'guiao_falado.odt'
    subprocess.run([
        'pandoc', str(HERE / 'guiao_falado.md'), '--from=markdown', '--to=odt',
        '--standalone', '--reference-doc=' + str(reference), '--metadata=lang:pt-PT',
        '--output=' + str(output),
    ], check=True, cwd=HERE)
    # Uma folha por diapositivo facilita o ensaio e a consulta durante a prova.
    # Conservar as famílias tipográficas e a página do caderno, ampliando a fala.
    ns = {'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
          'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
          'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
          'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0'}
    q = lambda prefix, local: '{' + ns[prefix] + '}' + local
    with ZipFile(output) as archive:
        entries = [(i, archive.read(i.filename)) for i in archive.infolist()]
        content_xml = ET.fromstring(archive.read('content.xml'))
    automatic = content_xml.find('office:automatic-styles', ns)
    for name, parent, size, pagebreak in [
        ('FalaTexto', 'Text_20_body', '12pt', False),
        ('FalaTitulo', 'Heading_20_1', '18pt', False),
        ('FalaSlide', 'Heading_20_2', '14pt', True),
        ('FalaEtiqueta', 'Heading_20_3', '11pt', False),
    ]:
        style = ET.SubElement(automatic, q('style', 'style'), {
            q('style', 'name'): name, q('style', 'family'): 'paragraph',
            q('style', 'parent-style-name'): parent})
        props = {q('fo', 'margin-left'): '0cm', q('fo', 'text-indent'): '0cm',
                 q('fo', 'text-align'): 'start', q('fo', 'line-height'): '120%',
                 q('fo', 'margin-bottom'): '0.16cm'}
        if pagebreak:
            props[q('fo', 'break-before')] = 'page'
        if name != 'FalaTexto':
            props[q('fo', 'keep-with-next')] = 'always'
            props[q('fo', 'margin-top')] = '0.25cm'
        ET.SubElement(style, q('style', 'paragraph-properties'), props)
        ET.SubElement(style, q('style', 'text-properties'), {
            q('fo', 'font-size'): size, q('fo', 'text-transform'): 'none',
            q('fo', 'hyphenate'): 'false'})
    for paragraph in content_xml.findall('.//office:body//text:p', ns):
        paragraph.set(q('text', 'style-name'), 'FalaTexto')
    for heading in content_xml.findall('.//office:body//text:h', ns):
        level = heading.get(q('text', 'outline-level'))
        heading.set(q('text', 'style-name'), {
            '1': 'FalaTitulo', '2': 'FalaSlide', '3': 'FalaEtiqueta'}[level])
    replacement = ET.tostring(content_xml, encoding='UTF-8', xml_declaration=True)
    with ZipFile(output, 'w') as archive:
        for info, data in entries:
            archive.writestr(info, replacement if info.filename == 'content.xml' else data)
    with ZipFile(output) as archive:
        assert archive.testzip() is None
        xml = ET.fromstring(archive.read('content.xml'))
        content = ''.join(xml.itertext())
        for n, record in records.items():
            assert f'{n:02d}. {record["titulo"]}' in content
            for paragraph in record['fala'].split('\n\n'):
                assert paragraph in content
    counts = [{'diapositivo': n, 'palavras_fala': len(r['fala'].split()),
               'palavras_aprofundamento': len(r['aprofundamento'].split())}
              for n, r in records.items()]
    total = sum(r['palavras_fala'] for r in counts[:23])
    stats = {'criterio_contagem': 'Tokens separados por espaço; inclui apenas texto para dizer.',
             'palavras_percurso_principal': total,
             'palavras_aprofundamento': sum(r['palavras_aprofundamento'] for r in counts[:23]),
             'estimativa_leitura_sem_pausas_minutos': {
                 'a_115_palavras_por_minuto': round(total / 115, 1),
                 'a_135_palavras_por_minuto': round(total / 135, 1)},
             'pressuposto': 'Ritmos usados apenas para estimativa; não medidos no autor. As metas de 20/30 minutos incluem pausas e observação das imagens.',
             'diapositivos': counts}
    (HERE / 'tempos_fala.json').write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n')
    print(f'{output}: 30 falas verificadas; {total} palavras no percurso principal.')


if __name__ == '__main__':
    main()
