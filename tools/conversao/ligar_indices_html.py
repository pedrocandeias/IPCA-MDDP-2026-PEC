"""Link the exported manuscript indexes without changing their visible text."""
import re
from collections import Counter

from lxml import html


def link_indexes(document, normalize):
    def text(node):
        return ''.join(node.xpath('.//text()[not(ancestor::button)]')).strip()

    nodes = list(document)
    headings = document.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6')
    main = next(n for n in nodes if text(n) == 'ÍNDICE')
    figures = next(n for n in headings if text(n) == 'ÍNDICE DE FIGURAS')
    tables = next(n for n in headings if text(n) == 'ÍNDICE DE TABELAS')
    body = next(n for n in headings if text(n) == 'Capítulo 1 - Introdução')
    ids = Counter(document.xpath('.//@id'))
    report = {'principal': 0, 'figuras': 0, 'tabelas': 0, 'anexos': 0,
              'sem_titulo': [], 'ligacoes': []}

    def anchor(target, suggested):
        if not target.get('id'):
            assert suggested not in ids, suggested
            target.set('id', suggested)
            ids[suggested] = 1
        assert ids[target.get('id')] == 1, target.get('id')
        return target.get('id')

    def wrap(entry, target_id, kind):
        before = text(entry)
        # Annex indexes already link their page numbers. Reuse the destination
        # and extend the clickable area to the title, retaining inline styles.
        for previous in entry.xpath('.//a'):
            previous.drop_tag()
        link = html.Element('a', href='#' + target_id, attrib={'class': 'index-link'})
        link.text = entry.text
        entry.text = None
        for child in list(entry):
            link.append(child)
        entry.append(link)
        assert text(entry) == before
        report[kind] += 1
        report['ligacoes'].append({'indice': kind, 'entrada': before, 'destino': target_id})

    for entry in nodes[nodes.index(main) + 1:nodes.index(figures)]:
        value = normalize(text(entry))
        if re.fullmatch(r'[ivxlcdm]+|\d+', value):
            # A standalone printed page number in the ODT has no section title.
            report['sem_titulo'].append(text(entry))
            continue
        matches = [h for h in headings if value.startswith(normalize(text(h)))
                   and re.fullmatch(r'[ivxlcdm]+|\d+', value[len(normalize(text(h))):].strip())]
        assert len(matches) == 1, ('Entrada sem destino inequívoco', text(entry))
        target = matches[0]
        wrap(entry, anchor(target, 'indice-' + normalize(text(target)).replace(' ', '-')), 'principal')

    for kind, start, end, label in [('figuras', figures, tables, 'Figura'), ('tabelas', tables, body, 'Tabela')]:
        captions = {}
        for node in nodes[nodes.index(body) + 1:]:
            match = re.match(rf'^{label} (\d+)\s*[-–—]', text(node)) if node.tag == 'p' else None
            if match:
                assert match[1] not in captions, (label, match[1])
                captions[match[1]] = node
        for entry in nodes[nodes.index(start) + 1:nodes.index(end)]:
            match = re.match(rf'^{label} (\d+)\s*[-–—]', text(entry))
            assert match and match[1] in captions, text(entry)
            wrap(entry, anchor(captions[match[1]], label.lower() + '-' + match[1]), kind)

    for heading in headings:
        if not re.fullmatch(r'Índice do Anexo [A-D]', text(heading)):
            continue
        for entry in heading.itersiblings():
            if re.fullmatch(r'h[1-6]', entry.tag):
                break
            links = entry.xpath('.//a[starts-with(@href,"#")]')
            if not links:
                continue
            destinations = {link.get('href')[1:] for link in links}
            assert len(destinations) == 1, text(entry)
            target = destinations.pop()
            assert ids[target] == 1, target
            wrap(entry, target, 'anexos')

    assert not document.xpath('.//a//a'), 'Ligações aninhadas'
    report['total'] = sum(report[k] for k in ('principal', 'figuras', 'tabelas', 'anexos'))
    return report
