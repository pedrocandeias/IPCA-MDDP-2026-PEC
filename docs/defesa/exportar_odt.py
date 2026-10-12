#!/usr/bin/env python3
"""Gera o caderno de defesa a partir dos seis Markdown da pasta."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import re
import subprocess
import sys

from lxml import etree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PARTS = [
    ('README.md', 'Parte I - Guia do caderno de preparação', 'guia'),
    ('guiao_apresentacao.md', 'Parte II - Guião da apresentação', 'apresentacao'),
    ('contexto_arguente.md', 'Parte III - Contextualização do arguente', 'contexto'),
    ('perfil_bernardo_providencia.md', 'Parte IV - Perfil académico e publicações', 'perfil'),
    ('perguntas_juri.md', 'Parte V - Perguntas e respostas para treino', 'perguntas'),
    ('evidencias_e_pontos_a_alinhar.md', 'Parte VI - Evidências e pontos a alinhar', 'evidencias'),
]
sys.path.insert(0, str(ROOT / 'tools/pdfs'))
from supplement_styles import NS, S, T, make_reference, prepare_document, encoded


def rewrite_zip(source, output, replacements):
    with ZipFile(source) as original, ZipFile(output, 'w') as target:
        for item in original.infolist():
            target.writestr(item, replacements.get(item.filename, original.read(item.filename)))


def main():
    assert {p.name for p in HERE.glob('*.md')} == {p[0] for p in PARTS}, \
        'Atualizar PARTS para abranger todos os Markdown da pasta.'
    template = ROOT / 'docs/revisoes/manuscrito/estilos_template_ipca_2026_10_05/projeto-mestrado-template-ipca.odt'
    output = HERE / 'preparacao_defesa_bernardo_providencia.odt'
    with TemporaryDirectory(prefix='defesa_odt_') as td:
        temp = Path(td)
        # O exportador dos suplementos localiza a página através de «Introdução».
        # Adaptar somente uma cópia temporária do template, sem alterar a fonte.
        with ZipFile(template) as z:
            styles = ET.fromstring(z.read('styles.xml'))
            content = ET.fromstring(z.read('content.xml'))
        named = {e.get(S + 'name') for e in styles.findall('.//style:style', NS)}
        if 'Source_20_Text' not in named:
            code = ET.SubElement(styles.find('office:styles', NS), S + 'style', {
                S + 'name': 'Source_20_Text', S + 'family': 'text',
            })
            ET.SubElement(code, S + 'text-properties', {
                S + 'font-name': 'Liberation Mono', '{' + NS['fo'] + '}font-size': '10pt',
            })
        master = next(e for e in styles.findall('.//style:master-page', NS)
                      if e.get(S + 'page-layout-name') == 'Mpm7')
        anchor = ET.SubElement(content.find('office:automatic-styles', NS), S + 'style',
                               {S + 'name': 'DefesaPageAnchor', S + 'family': 'paragraph',
                                S + 'master-page-name': master.get(S + 'name')})
        paragraph = ET.Element(T + 'p', {T + 'style-name': anchor.get(S + 'name')})
        paragraph.text = 'Introdução'
        content.find('.//office:text', NS).insert(0, paragraph)
        # O template não contém tabelas; definir uma grelha simples na cópia.
        table_ns = '{' + NS['table'] + '}'
        cell_style = ET.SubElement(content.find('office:automatic-styles', NS), S + 'style', {
            S + 'name': 'DefesaCell', S + 'family': 'table-cell',
        })
        ET.SubElement(cell_style, S + 'table-cell-properties', {
            '{' + NS['fo'] + '}border': '0.5pt solid #808080',
            '{' + NS['fo'] + '}padding': '0.08in',
        })
        table = ET.SubElement(content.find('.//office:text', NS), table_ns + 'table')
        row = ET.SubElement(table, table_ns + 'table-row')
        ET.SubElement(row, table_ns + 'table-cell', {table_ns + 'style-name': 'DefesaCell'})
        source = temp / 'template.odt'
        rewrite_zip(template, source, {'content.xml': encoded(content), 'styles.xml': encoded(styles)})
        reference = temp / 'reference.odt'
        make_reference(ROOT / 'tools/pdfs/suplementos_reference.odt', source, reference)

        # Evitar cabeçalhos e numeração de capítulos próprios do manuscrito.
        with ZipFile(reference) as z:
            rs = ET.fromstring(z.read('styles.xml'))
        for m in rs.findall('.//style:master-page', NS):
            for child in list(m):
                m.remove(child)
            footer = ET.SubElement(m, S + 'footer')
            p = ET.SubElement(footer, T + 'p', {T + 'style-name': 'Footer'})
            ET.SubElement(p, T + 'page-number', {T + 'select-page': 'current'}).text = '1'
        updated = temp / 'reference_updated.odt'
        rewrite_zip(reference, updated, {'styles.xml': encoded(rs)})

        blocks = []
        for filename, title, bookmark in PARTS:
            text = (HERE / filename).read_text(encoding='utf-8')
            text = re.sub(r'^# .+$', '# ' + title + ' {#' + bookmark + '}', text, count=1, flags=re.M)
            # Referências aos documentos reunidos passam a ser ligações internas.
            for target, _, destination in PARTS:
                text = text.replace('](' + target + ')', '](#' + destination + ')')
            text = text.replace('](preparacao_defesa_bernardo_providencia.odt)', '](#guia)')
            blocks.append(text)
        combined = temp / 'caderno.md'
        combined.write_text('\n\n'.join(blocks), encoding='utf-8')
        generated = temp / 'caderno.odt'
        subprocess.run([
            'pandoc', str(combined), '--from=markdown', '--to=odt', '--standalone',
            '--reference-doc=' + str(updated), '--metadata=lang:pt-PT',
            '--metadata=title:Preparação da defesa - Bernardo Providência',
            '--output=' + str(generated),
        ], cwd=HERE, check=True)
        prepare_document(generated)
        # Começar cada parte seguinte em nova página, conservando os estilos.
        with ZipFile(generated) as z:
            xml = ET.fromstring(z.read('content.xml'))
        automatic = xml.find('office:automatic-styles', NS)
        heading = ET.SubElement(automatic, S + 'style', {
            S + 'name': 'DefesaPartStart', S + 'family': 'paragraph',
            S + 'parent-style-name': 'Heading_20_1',
        })
        ET.SubElement(heading, S + 'paragraph-properties', {
            '{' + NS['fo'] + '}break-before': 'page',
        })
        for h in xml.findall('.//text:h', NS):
            if ''.join(h.itertext()) in {part[1] for part in PARTS[1:]}:
                h.set(T + 'style-name', 'DefesaPartStart')
        row_style = ET.SubElement(automatic, S + 'style', {
            S + 'name': 'DefesaTableRow', S + 'family': 'table-row',
        })
        ET.SubElement(row_style, S + 'table-row-properties', {
            '{' + NS['fo'] + '}keep-together': 'always',
        })
        for row in xml.findall('.//table:table-row', NS):
            row.set('{' + NS['table'] + '}style-name', 'DefesaTableRow')
        label = ET.SubElement(automatic, S + 'style', {
            S + 'name': 'DefesaAnswerLabel', S + 'family': 'paragraph',
            S + 'parent-style-name': 'Text_20_body',
        })
        ET.SubElement(label, S + 'paragraph-properties', {
            '{' + NS['fo'] + '}keep-with-next': 'always',
        })
        for paragraph in xml.findall('.//text:p', NS):
            if ''.join(paragraph.itertext()) == 'A minha resposta:':
                paragraph.set(T + 'style-name', 'DefesaAnswerLabel')
        result = temp / 'result.odt'
        rewrite_zip(generated, result, {'content.xml': encoded(xml)})
        # Todos os títulos de perguntas têm de sobreviver à conversão.
        texts = [''.join(h.itertext()) for h in xml.findall('.//text:h', NS)]
        expected = re.findall(r'^### (\d+\. .+)$', (HERE / 'perguntas_juri.md').read_text(), re.M)
        assert len(expected) == 47 and all(t in texts for t in expected)
        paragraphs = [''.join(p.itertext()) for p in xml.findall('.//text:p', NS)]
        assert sum(t == 'A minha resposta:' for t in paragraphs) == 47
        assert all(title in texts for _, title, _ in PARTS)
        bookmarks = {b.get(T + 'name') for b in xml.findall('.//text:bookmark-start', NS)}
        assert {part[2] for part in PARTS} <= bookmarks
        output.write_bytes(result.read_bytes())
        print(f'{output}: {len(PARTS)} documentos e {len(expected)} perguntas e respostas verificados')


if __name__ == '__main__':
    main()
