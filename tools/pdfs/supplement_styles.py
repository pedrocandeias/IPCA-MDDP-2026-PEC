"""Transfere a apresentação do manuscrito para as exportações dos suplementos."""
from copy import deepcopy
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
import re
from lxml import etree as ET

NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
}
S, T, F = ('{' + NS[k] + '}' for k in ('style', 'text', 'fo'))
BODY = 'Texto_20_Normal_20_-_20_IPCA'

def xml(data):
    return ET.fromstring(data)

def encoded(node):
    return ET.tostring(node, encoding='utf-8', xml_declaration=True)

def put_style(container, element):
    name = element.get(S+'name')
    for old in container.findall('style:style', NS):
        if old.get(S+'name') == name:
            container.remove(old)
    container.append(element)

def property_node(style, kind):
    element = style.find('style:'+kind, NS)
    if element is None:
        element = ET.SubElement(style, S+kind)
    return element

def make_reference(template, manuscript, output):
    with ZipFile(manuscript) as archive:
        source = xml(archive.read('styles.xml'))
        content = xml(archive.read('content.xml'))
    named = {e.get(S+'name'): e for e in source.findall('.//style:style', NS)}
    automatic = {e.get(S+'name'): e for e in content.findall('.//style:style', NS)}
    # The main body starts at Introdução; front matter and annex D use other pages.
    master_name = None
    for paragraph in content.xpath('//text:h|//text:p', namespaces=NS):
        if ''.join(paragraph.itertext()).strip() == 'Introdução':
            style = automatic.get(paragraph.get(T+'style-name'))
            if style is not None and style.get(S+'master-page-name'):
                master_name = style.get(S+'master-page-name')
                break
    masters = {e.get(S+'name'): e for e in source.findall('.//style:master-page', NS)}
    if master_name not in masters:
        raise ValueError('Não foi identificado o estilo de página do corpo principal.')
    master = deepcopy(masters[master_name])
    layout_name = master.get(S+'page-layout-name')
    layouts = {e.get(S+'name'): e for e in source.findall('.//style:page-layout', NS)}
    layout = deepcopy(layouts[layout_name])
    with ZipFile(template) as archive:
        styles = xml(archive.read('styles.xml'))
        container = styles.find('office:styles', NS)
        names = ['Standard', BODY, 'Heading_20_1', 'Heading_20_2', 'Heading_20_3',
                 'Heading_20_4', 'Caption', 'Header', 'Footer', 'Rodapé_20_Romano_20_-_20_IPCA',
                 'Rodapé_20_Caráter', 'Source_20_Text']
        for name in names:
            element = deepcopy(named[name])
            # Number labels in these documents already belong to their text.
            for key in list(element.attrib):
                if ET.QName(key).localname in ['linked-style-name','list-style-name','list-level']:
                    del element.attrib[key]
            if name.startswith('Heading_20_'):
                level = name.rsplit('_', 1)[1]
                element.set(S+'default-outline-level', level)
                element.set(S+'next-style-name', BODY)
                property_node(element,'paragraph-properties').set(F+'keep-with-next','always')
            put_style(container, element)
        for alias in ['Text_20_body', 'First_20_paragraph']:
            put_style(container, ET.Element(S+'style', {S+'name':alias, S+'family':'paragraph', S+'parent-style-name':BODY}))
        # Main-manuscript tables predominantly use 10 pt TNR, 150%, without indentation.
        for name, align, bold in [('Table_20_Contents','left',False),('Table_20_Heading','center',True)]:
            element = ET.Element(S+'style', {S+'name':name,S+'family':'paragraph',S+'parent-style-name':BODY})
            prop = property_node(element,'paragraph-properties')
            for k,v in {'text-indent':'0in','text-align':align,'keep-with-next':'auto','orphans':'0','widows':'0'}.items():
                prop.set(F+k,v)
            if bold: property_node(element,'text-properties').set(F+'font-weight','bold')
            put_style(container,element)
        cells = Counter(e.get('{'+NS['table']+'}style-name') for e in content.findall('.//table:table-cell', NS))
        cell_name = cells.most_common(1)[0][0]
        cell = deepcopy(automatic[cell_name]);cell.set(S+'name','SupplementCellPrototype')
        put_style(container,cell)
        # The source uses Liberation Mono for literal code. Keep code distinct from prose.
        for name in ['Source_Text','Teletype']:
            element=deepcopy(named['Source_20_Text']);element.set(S+'name',name)
            property_node(element,'text-properties').set(F+'text-transform','none')
            put_style(container,element)
        filename=ET.Element(S+'style',{S+'name':'SupplementFileName',S+'family':'text'})
        property_node(filename,'text-properties').set(F+'text-transform','none')
        put_style(container,filename)
        spacer=ET.Element(S+'style',{S+'name':'SupplementHeadingSpacer',S+'family':'paragraph',S+'parent-style-name':BODY})
        property_node(spacer,'paragraph-properties').set(F+'keep-with-next','always')
        put_style(container,spacer)
        fonts=styles.find('office:font-face-decls',NS)
        existing={e.get(S+'name') for e in fonts}
        for font in source.find('office:font-face-decls',NS):
            if font.get(S+'name') not in existing:fonts.append(deepcopy(font))
        auto=styles.find('office:automatic-styles',NS)
        for old in list(auto):
            if old.tag==S+'page-layout':auto.remove(old)
        layout.set(S+'name','SupplementPageLayout');auto.append(layout)
        master.set(S+'name','Standard');master.set(S+'page-layout-name','SupplementPageLayout')
        master.attrib.pop(S+'next-style-name',None)
        for page in master.findall('.//text:page-number',NS):page.text='1'
        master_container=styles.find('office:master-styles',NS)
        for old in list(master_container):master_container.remove(old)
        master_container.append(master)
        with ZipFile(output,'w') as target:
            for item in archive.infolist():
                target.writestr(item,encoded(styles) if item.filename=='styles.xml' else archive.read(item.filename))
    return {'master_page':master_name,'page_layout':layout_name,'body_style':BODY}

def prepare_document(path):
    """Aplica separadores IPCA por grupo de títulos sem alterar o texto."""
    with ZipFile(path) as archive:
        content=xml(archive.read('content.xml'))
        styles=xml(archive.read('styles.xml'))
        cell=next(e for e in styles.findall('.//style:style',NS) if e.get(S+'name')=='SupplementCellPrototype')
        cell_properties=cell.find('style:table-cell-properties',NS)
        for style in content.findall('.//style:style',NS):
            if style.get(S+'family')=='table-cell':
                old=style.find('style:table-cell-properties',NS)
                if old is not None:style.remove(old)
                style.append(deepcopy(cell_properties))
        body=content.find('.//office:text',NS)
        original_text=''.join(body.itertext())
        children=list(body)
        for index,node in enumerate(children):
            if node.tag != T+'h':continue
            # File paths retain their case even when the heading uses uppercase.
            text=''.join(node.itertext()).strip()
            if re.search(r'\.(md|json|csv|docx|3mf|jpe?g|png|odt|pdf)$',text,re.I):
                span=ET.Element(T+'span',{T+'style-name':'SupplementFileName'})
                span.text=node.text;node.text=None
                for child in list(node):node.remove(child);span.append(child)
                node.append(span)
            if index and children[index-1].tag != T+'h':
                body.insert(body.index(node),ET.Element(T+'p',{T+'style-name':'SupplementHeadingSpacer'}))
            if index+1 < len(children) and children[index+1].tag != T+'h':
                body.insert(body.index(node)+1,ET.Element(T+'p',{T+'style-name':'SupplementHeadingSpacer'}))
        assert ''.join(body.itertext())==original_text
        output=path.with_name('.'+path.name+'.styles-tmp')
        with ZipFile(output,'w') as target:
            for item in archive.infolist():
                target.writestr(item,encoded(content) if item.filename=='content.xml' else archive.read(item.filename))
    output.replace(path)
