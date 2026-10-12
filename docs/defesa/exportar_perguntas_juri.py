#!/usr/bin/env python3
"""Exporta as perguntas do júri para ODT, com estilos do caderno de defesa."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import re
import subprocess

from lxml import etree as ET
from exportar_odt import NS, S, T, encoded, rewrite_zip

HERE = Path(__file__).resolve().parent
F = '{' + NS['fo'] + '}'


def main():
    source = HERE / 'perguntas_juri.md'
    expected = re.findall(r'^### (\d+\. .+)$', source.read_text(), re.M)
    assert len(expected) == 47
    with TemporaryDirectory(prefix='perguntas_juri_') as folder:
        generated = Path(folder) / 'perguntas.odt'
        subprocess.run([
            'pandoc', str(source), '--from=markdown', '--to=odt', '--standalone',
            '--reference-doc=' + str(HERE / 'preparacao_defesa_bernardo_providencia.odt'),
            '--metadata=lang:pt-PT', '--output=' + str(generated),
        ], check=True, cwd=HERE)
        with ZipFile(generated) as archive:
            content = ET.fromstring(archive.read('content.xml'))
        automatic = content.find('office:automatic-styles', NS)
        for name, parent, size, keep in [
            ('JuriTexto', 'Text_20_body', '11pt', False),
            ('JuriResposta', 'Quotations', '11pt', False),
            ('JuriEtiqueta', 'Text_20_body', '11pt', True),
            ('JuriTitulo', 'Heading_20_1', '20pt', True),
            ('JuriTema', 'Heading_20_2', '15pt', True),
            ('JuriPergunta', 'Heading_20_3', '12pt', True),
            ('JuriTabela', 'Text_20_body', '10pt', False),
        ]:
            style = ET.SubElement(automatic, S + 'style', {
                S + 'name': name, S + 'family': 'paragraph',
                S + 'parent-style-name': parent,
            })
            props = {F + 'text-align': 'start', F + 'line-height': '120%',
                     F + 'margin-bottom': '0.2cm', F + 'text-indent': '0cm',
                     F + 'orphans': '2', F + 'widows': '2'}
            if keep:
                props[F + 'keep-with-next'] = 'always'
                props[F + 'margin-top'] = '0.25cm'
            ET.SubElement(style, S + 'paragraph-properties', props)
            ET.SubElement(style, S + 'text-properties', {
                F + 'font-size': size, F + 'hyphenate': 'false',
                F + 'text-transform': 'none',
            })
        for p in content.findall('.//office:body//text:p', NS):
            style = 'JuriResposta' if p.get(T + 'style-name') == 'Quotations' else 'JuriTexto'
            if ''.join(p.itertext()) == 'A minha resposta:':
                style = 'JuriEtiqueta'
            p.set(T + 'style-name', style)
        # Separar visualmente as colunas e manter cada exemplo na mesma página.
        table_ns = '{' + NS['table'] + '}'
        for name, family, properties in [
            ('JuriCelula', 'table-cell', {F + 'padding': '0.12cm',
                                        F + 'border': '0.5pt solid #b0b0b0'}),
            ('JuriLinha', 'table-row', {F + 'keep-together': 'always'}),
        ]:
            style = ET.SubElement(automatic, S + 'style', {
                S + 'name': name, S + 'family': family,
            })
            ET.SubElement(style, S + family + '-properties', properties)
        for cell in content.findall('.//table:table-cell', NS):
            cell.set(table_ns + 'style-name', 'JuriCelula')
            for p in cell.findall('.//text:p', NS):
                p.set(T + 'style-name', 'JuriTabela')
        for row in content.findall('.//table:table-row', NS):
            row.set(table_ns + 'style-name', 'JuriLinha')
        headings = content.findall('.//office:body//text:h', NS)
        for h in headings:
            h.set(T + 'style-name', {'1': 'JuriTitulo', '2': 'JuriTema',
                                    '3': 'JuriPergunta'}[h.get(T + 'outline-level')])
        assert all(title in [''.join(h.itertext()) for h in headings] for title in expected)
        assert sum(''.join(p.itertext()) == 'A minha resposta:'
                   for p in content.findall('.//text:p', NS)) == 47
        output = HERE / 'perguntas_juri.odt'
        rewrite_zip(generated, output, {'content.xml': encoded(content)})
        with ZipFile(output) as archive:
            assert archive.testzip() is None
        print(f'{output}: 47 perguntas e respostas verificadas')


if __name__ == '__main__':
    main()
