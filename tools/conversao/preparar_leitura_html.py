"""Prepare the reading edition: administrative omission and paged indexes."""
import math
import re
from urllib.parse import unquote

from lxml import html, etree


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
            if original == 'xx':
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
                cost = 1 + math.ceil(len(original) / 66)
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
                        label, page = target_title, suffix
                    else:
                        match = re.match(r'^(.*?)(\d+)\s*$', original)
                        assert match, original
                        label, page = match[1].rstrip(), match[2]
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
                    etree.SubElement(link, 'span', attrib={'class': 'index-leader', 'aria-hidden': 'true'})
                    etree.SubElement(link, 'span', attrib={'class': 'index-page'}).text = page
                    link.set('aria-label', f'{label}, página {page} no documento original')
                    cost = 1 + math.ceil(len(label) / 66) + int(major)
                else:
                    row.set('class', 'index-group-label')
                    cost = 3
            row.set('data-original-text', original)
            rows.append((row, cost))
            if kind == 'abbreviations':
                document.remove(node)

        chunks = [[]]
        units = 0
        for row, cost in rows:
            if units + cost > 38 and chunks[-1]:
                chunks.append([])
                units = 0
            chunks[-1].append(row)
            units += cost
        # Keep an appendix group label with its first entry.
        for index in range(len(chunks) - 1):
            if chunks[index][-1].get('class') == 'index-group-label':
                chunks[index + 1].insert(0, chunks[index].pop())
        title = text(heading)
        position = document.index(heading)
        section = html.Element('section', attrib={'class': 'reading-section', 'aria-label': title})
        document.insert(position, section)
        for number, chunk in enumerate(chunks, 1):
            page = etree.SubElement(section, 'section', attrib={'class': f'reading-page {kind}-sheet'})
            if number == 1:
                page.append(heading)
                heading.set('class', 'reading-page-title')
            else:
                etree.SubElement(page, 'h2', attrib={'class': 'reading-page-title', 'data-reading-decoration': 'true'}).text = title + ' · continuação'
            if kind == 'index':
                etree.SubElement(page, 'p', attrib={'class': 'index-page-note', 'data-reading-decoration': 'true'}).text = 'Páginas do documento original'
            container = etree.SubElement(page, 'dl' if kind == 'abbreviations' else 'div', attrib={'class': 'abbreviation-list' if kind == 'abbreviations' else 'index-entries'})
            for row in chunk:
                container.append(row)
            etree.SubElement(page, 'p', attrib={'class': 'reading-page-number', 'data-reading-decoration': 'true'}).text = f'{number} / {len(chunks)}'
        report['sections'].append({'title': title, 'entries': len(rows), 'pages': len(chunks)})
    return report
