"""Prepare the reading edition: administrative omission and continuous indexes."""
import re
from urllib.parse import unquote

from lxml import html, etree


def repair_mixed_caption(document):
    """Recover the table caption accidentally pasted inside a word in the ODT.

    This narrowly scoped reading adaptation preserves both texts and is logged;
    it does not infer corrections for other captions or change the source ODT.
    """
    caption = 'Distribuição de tarefas entre regras, IA e supervisão humana'
    pattern = re.compile(r'medidTabela\s+22\s*-\s*' + re.escape(caption) + r'as completas')
    paragraphs = [p for p in document.xpath('./p') if pattern.search(p.text_content())]
    if not paragraphs:
        return []
    assert len(paragraphs) == 2, 'Rever legenda fundida da Tabela 22'
    entries = [p for p in paragraphs if re.search(r'hipotéticas\.\s*\d+\s*$', p.text_content())]
    assert len(entries) == 1, 'Rever entrada da Tabela 22 no índice'
    index_entry = entries[0]
    body = next(p for p in paragraphs if p is not index_entry)
    tables = [t for t in document.xpath('./table')
              if re.sub(r'\s+', '', t.text_content()).startswith('TarefaMecanismoResultadoIdentificarsexoeidade')]
    assert len(tables) == 1, 'Rever tabela de distribuição de tarefas'
    title = 'Tabela 22 - ' + caption
    original_body = body.text_content()
    original_index = index_entry.text_content()
    page = re.search(r'(\d+)\s*$', original_index)[1]
    previous = tables[0].getprevious()
    original_caption = None
    if previous is not None and re.match(r'^Tabela\s+22\s*[-–—]', previous.text_content()):
        caption_node = previous
        original_caption = caption_node.text_content()
        for child in list(caption_node):
            caption_node.remove(child)
    else:
        caption_node = html.Element('p')
        tables[0].addprevious(caption_node)
    caption_node.text = title
    # Preserve any old destinations at the caption's corrected location.
    for value in body.xpath('.//@id'):
        etree.SubElement(caption_node, 'span', id=value)
    for child in list(body):
        body.remove(child)
    body.text = pattern.sub('medidas completas', original_body)
    for child in list(index_entry):
        index_entry.remove(child)
    index_entry.text = title + page
    return [{'type': 'mixed_table_caption', 'table': 22,
             'source_body': original_body, 'reading_body': body.text_content(),
             'source_index': original_index, 'reading_index': index_entry.text,
             'source_caption_near_table': original_caption,
             'caption': title,
             'reason': 'Legenda fundida com a palavra medidas no ODT; separada e colocada antes da tabela identificada pelo cabeçalho Tarefa / Mecanismo / Resultado.'}]


def prepare_reading(document):
    def text(node):
        return node.text_content().strip()

    nodes = list(document)
    start = next(i for i, n in enumerate(nodes) if text(n) == 'Declaração')
    end = next(i for i, n in enumerate(nodes) if n.get('id') == 'resumo')
    removed = nodes[start:end]
    assert len(removed) == 14 and any(text(n).startswith('Assinatura:') for n in removed)
    report = {'administrative_paragraphs_removed': [text(n) for n in removed],
              'print_artifacts_removed': [], 'sections': []}
    for node in removed:
        document.remove(node)

    # The ODT has a cover and title page with identical content. Show it once.
    assert start == 16 and [text(n) for n in nodes[:8]] == [text(n) for n in nodes[8:16]], 'Rever capa e folha de rosto'
    report['duplicate_cover_paragraphs_removed'] = [text(n) for n in nodes[8:16]]
    for node in nodes[8:16]:
        document.remove(node)

    # Collect ranges before restructuring the direct children of the article.
    nodes = list(document)
    abbreviations = next(n for n in nodes if n.get('id') == 'lista-de-abreviaturas-e-siglas')
    main = next(n for n in nodes if text(n) == 'ÍNDICE')
    figures = next(n for n in nodes if text(n) == 'ÍNDICE DE FIGURAS')
    tables = next(n for n in nodes if text(n) == 'ÍNDICE DE TABELAS')
    body = next(n for n in nodes if text(n) == 'Capítulo 1 - Introdução')
    ranges = [(abbreviations, main, 'abbreviations'), (main, figures, 'index'),
              (figures, tables, 'index'), (tables, body, 'index')]
    for heading in nodes:
        if re.fullmatch(r'Índice do Anexo [A-D]', text(heading)):
            following = next(n for n in heading.itersiblings() if re.fullmatch(r'h[1-6]', n.tag))
            ranges.append((heading, following, 'index'))
    main.tag = 'h1'
    main.set('id', 'indice-geral')

    for heading, following, kind in ranges:
        source_rows = nodes[nodes.index(heading) + 1:nodes.index(following)]
        rows = []
        for node in source_rows:
            original = text(node)
            if kind == 'index' and re.fullmatch(r'[ivxlcdm]+|\d+', original, re.I):
                report['print_artifacts_removed'].append(original)
                document.remove(node)
                continue
            if kind == 'abbreviations':
                match = re.match(r'^(.+?) - (.*)', node.text or '', re.S)
                assert match, original
                row = html.Element('div', attrib={'class': 'abbreviation-row'})
                term = etree.SubElement(row, 'dt')
                term.text = match[1]
                definition = etree.SubElement(row, 'dd')
                definition.text = match[2]
                for child in list(node):
                    definition.append(child)
            else:
                row = node
                links = node.xpath('./a[@class="index-link"]')
                if links:
                    link = links[0]
                    target_id = unquote(link.get('href')[1:])
                    target = document.xpath('.//*[@id=$id]', id=target_id)[0]
                    target_title = text(target)
                    # Use the title boundary before reading the page number:
                    # titles themselves can end in Roman letters or digits.
                    suffix = original[len(target_title):].strip()
                    if original.startswith(target_title) and re.fullmatch(r'[ivxlcdm]+|\d+', suffix):
                        label = target_title
                    else:
                        match = re.match(r'^(.*?)(\d+)\s*$', original)
                        assert match, original
                        label = match[1].rstrip()
                    level = min(int(target.tag[1:]) - 1, 3) if re.fullmatch(r'h[1-6]', target.tag) else 0
                    if re.match(r'^[A-D]\.\d+\.\d+', label):
                        level = 2
                    elif re.match(r'^[A-D]\.\d+', label):
                        level = 1
                    major = bool(re.match(r'Capítulo \d|Anexo [A-D] - |Referências Bibliográficas', label))
                    row.set('class', f'index-entry index-level-{level}' + (' index-chapter' if major else ''))
                    link.text = None
                    for child in list(link):
                        link.remove(child)
                    etree.SubElement(link, 'span', attrib={'class': 'index-label'}).text = label
                    link.set('aria-label', label)
                else:
                    row.set('class', 'index-group-label')
            row.set('data-original-text', original)
            rows.append(row)
            if kind == 'abbreviations':
                document.remove(node)

        title = text(heading)
        position = document.index(heading)
        section = html.Element('section', attrib={'class': 'reading-section', 'aria-label': title})
        document.insert(position, section)
        section.append(heading)
        heading.set('class', 'reading-section-title')
        container = etree.SubElement(section, 'dl' if kind == 'abbreviations' else 'div', attrib={'class': 'abbreviation-list' if kind == 'abbreviations' else 'index-entries'})
        for row in rows:
            container.append(row)
        report['sections'].append({'title': title, 'entries': len(rows), 'layout': 'continuous'})

    dedication_texts = [
        'À Patrícia, pela coragem de abraçar os meus desafios.',
        'À família e aos amigos, pelo apoio constante.',
        'A ti, por estares a ler estas palavras.',
    ]
    declaration = document.get_element_by_id('declaração-de-utilização-de-ferramentas-de-inteligência-artificial')
    dedication_rows = [n for n in document if n.tag == 'p' and text(n) in dedication_texts]
    assert [text(n) for n in dedication_rows] == dedication_texts, 'Rever dedicatória'
    declaration_rows = []
    for node in declaration.itersiblings():
        if node is dedication_rows[0]:
            break
        declaration_rows.append(node)
    declaration_section = html.Element('section', attrib={'class': 'ai-declaration', 'aria-labelledby': declaration.get('id')})
    document.insert(document.index(declaration), declaration_section)
    for node in [declaration, *declaration_rows]:
        declaration_section.append(node)
    dedication = html.Element('section', attrib={'class': 'dedication', 'aria-labelledby': 'dedicatoria'})
    document.insert(document.index(dedication_rows[0]), dedication)
    etree.SubElement(dedication, 'h1', id='dedicatoria').text = 'Dedicatória'
    for node in dedication_rows:
        dedication.append(node)
    report['dedication_separated'] = True
    backlinks = document.xpath('.//a[@role="doc-backlink"]')
    for link in backlinks:
        reference = document.get_element_by_id(unquote(link.get('href')[1:]))
        link.text = '↩ Voltar ao texto'
        link.set('aria-label', f'Voltar ao texto da nota {text(reference)}')
    report['footnote_return_links'] = len(backlinks)
    return report
