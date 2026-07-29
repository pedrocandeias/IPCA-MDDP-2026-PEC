#!/usr/bin/env python3
"""Insere as Figuras 5.9 e 5.10 sobre perfis antropométricos no manuscrito."""

from __future__ import annotations

import os
import re
import struct
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import NS, qn, sensitive_state, set_space, text_of


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
IMAGE_59 = ROOT / "figuras/perfis-antropometricos-handfab.png"
IMAGE_510 = ROOT / "figuras/editor-adicao-perfis-antropometricos-handfab.png"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NSX = {**NS, "r": R, "wp": WP, "a": A, "pic": PIC, "rel": REL}
EMU_PER_INCH = 914400

ANCHOR = (
    "A evolução posterior do módulo acrescentou uma referência opcional baseada em "
    "dados populacionais. Quando a interface envia a descrição do utilizador e o "
    "identificador do modelo, o servidor procura o perfil antropométrico populacional "
    "com melhor pontuação segundo sexo, idade aproximada e país, e projecta as médias "
    "desse perfil sobre os parâmetros disponíveis no modelo activo. O bloco de referência "
    "é anexado ao pedido enviado à IA, permitindo orientar a sugestão sem se sobrepor a "
    "medições fornecidas pelo utilizador. Esta solução estabelece continuidade entre "
    "três formas de introdução de dados: selecção manual de um perfil populacional, "
    "importação de perfis antropométricos e sugestão apoiada por IA."
)
EXPLANATION = (
    "As Figuras 5.9 e 5.10 documentam esta componente. A primeira apresenta a lista de "
    "perfis antropométricos populacionais e os campos usados para os filtrar, importar, "
    "editar ou eliminar. A segunda mostra a estrutura usada para adicionar ou editar um "
    "perfil, separando a identificação do conjunto de dados, as medidas da mão e as "
    "medidas do membro residual. Estas vistas documentam as funções disponíveis no "
    "protótipo; não demonstram a qualidade ou a representatividade dos dados importados."
)
CAPTION_59 = (
    "Figura 5.9 — Perfis antropométricos populacionais disponíveis na plataforma HandFab."
)
CAPTION_510 = (
    "Figura 5.10 — Campos de identificação, contexto e medição para adição ou edição de "
    "perfis antropométricos na plataforma HandFab."
)
SOURCE = "Fonte: produção própria."

LIST_58_MD = (
    "| Figura 5.8 | Interface de selecção, configuração paramétrica e materiais da "
    "plataforma HandFab. | 80 |"
)
LIST_59_MD = (
    "| Figura 5.9 | Perfis antropométricos populacionais disponíveis na plataforma "
    "HandFab. | A DEFINIR |"
)
LIST_510_MD = (
    "| Figura 5.10 | Campos de identificação, contexto e medição para adição ou edição "
    "de perfis antropométricos na plataforma HandFab. | A DEFINIR |"
)
INSERT_MD = (
    f"{EXPLANATION}\n\n"
    "![](figuras/perfis-antropometricos-handfab.png)\n\n"
    f"{CAPTION_59}\n\n{SOURCE}\n\n"
    "![](figuras/editor-adicao-perfis-antropometricos-handfab.png)\n\n"
    f"{CAPTION_510}\n\n{SOURCE}"
)


def q(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"Ficheiro não é PNG: {path}")
    return struct.unpack(">II", header[16:24])


def fit_size(path: Path, max_width: float = 5.9, max_height: float = 4.42) -> tuple[int, int]:
    width, height = png_size(path)
    ratio = min(max_width / width, max_height / height)
    return round(width * ratio * EMU_PER_INCH), round(height * ratio * EMU_PER_INCH)


def next_relationship_id(rels: etree._Element) -> str:
    maximum = 0
    for node in rels.xpath("./rel:Relationship", namespaces=NSX):
        match = re.fullmatch(r"rId(\d+)", node.get("Id", ""))
        if match:
            maximum = max(maximum, int(match.group(1)))
    return f"rId{maximum + 1}"


def add_text_run(paragraph: etree._Element, value: str) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    text = etree.SubElement(run, qn("t"))
    text.text = value
    set_space(text)


def replace_paragraph_text(paragraph: etree._Element, value: str) -> None:
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    add_text_run(paragraph, value)


def paragraph_from(template: etree._Element, value: str) -> etree._Element:
    paragraph = deepcopy(template)
    replace_paragraph_text(paragraph, value)
    return paragraph


def blank_paragraph(template: etree._Element) -> etree._Element:
    paragraph = deepcopy(template)
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    return paragraph


def image_paragraph(
    rid: str, filename: str, cx: int, cy: int, docpr_id: int
) -> etree._Element:
    paragraph = etree.Element(qn("p"))
    ppr = etree.SubElement(paragraph, qn("pPr"))
    jc = etree.SubElement(ppr, qn("jc"))
    jc.set(qn("val"), "center")
    run = etree.SubElement(paragraph, qn("r"))
    drawing = etree.SubElement(run, qn("drawing"))
    inline = etree.SubElement(drawing, q(WP, "inline"))
    for name in ("distT", "distB", "distL", "distR"):
        inline.set(name, "0")
    extent = etree.SubElement(inline, q(WP, "extent"))
    extent.set("cx", str(cx))
    extent.set("cy", str(cy))
    effect = etree.SubElement(inline, q(WP, "effectExtent"))
    for name in ("l", "t", "r", "b"):
        effect.set(name, "0")
    docpr = etree.SubElement(inline, q(WP, "docPr"))
    docpr.set("id", str(docpr_id))
    docpr.set("name", filename)
    frame = etree.SubElement(inline, q(WP, "cNvGraphicFramePr"))
    etree.SubElement(frame, q(A, "graphicFrameLocks")).set("noChangeAspect", "1")
    graphic = etree.SubElement(inline, q(A, "graphic"))
    data = etree.SubElement(graphic, q(A, "graphicData"))
    data.set("uri", PIC)
    picture = etree.SubElement(data, q(PIC, "pic"))
    nv = etree.SubElement(picture, q(PIC, "nvPicPr"))
    cnv = etree.SubElement(nv, q(PIC, "cNvPr"))
    cnv.set("id", "0")
    cnv.set("name", filename)
    etree.SubElement(nv, q(PIC, "cNvPicPr"))
    fill = etree.SubElement(picture, q(PIC, "blipFill"))
    blip = etree.SubElement(fill, q(A, "blip"))
    blip.set(q(R, "embed"), rid)
    stretch = etree.SubElement(fill, q(A, "stretch"))
    etree.SubElement(stretch, q(A, "fillRect"))
    shape = etree.SubElement(picture, q(PIC, "spPr"))
    transform = etree.SubElement(shape, q(A, "xfrm"))
    offset = etree.SubElement(transform, q(A, "off"))
    offset.set("x", "0")
    offset.set("y", "0")
    dimensions = etree.SubElement(transform, q(A, "ext"))
    dimensions.set("cx", str(cx))
    dimensions.set("cy", str(cy))
    geometry = etree.SubElement(shape, q(A, "prstGeom"))
    geometry.set("prst", "rect")
    etree.SubElement(geometry, q(A, "avLst"))
    return paragraph


def add_list_rows(root: etree._Element) -> None:
    rows = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph).startswith("Figura 5.8 —")
        and text_of(paragraph).endswith("80")
        and paragraph.xpath("./w:pPr/w:pStyle[@w:val='TOC1']", namespaces=NS)
    ]
    if len(rows) != 1:
        raise RuntimeError(f"Linha da lista de figuras inesperada: {len(rows)}")
    base = rows[0]
    parent = base.getparent()
    position = parent.index(base)
    for offset, values in enumerate(
        (
            (CAPTION_59, "A DEFINIR"),
            (CAPTION_510, "A DEFINIR"),
        ),
        start=1,
    ):
        paragraph = deepcopy(base)
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if len(text_nodes) != 2 or not paragraph.xpath(".//w:tab", namespaces=NS):
            raise RuntimeError("Estrutura inesperada na lista de figuras")
        text_nodes[0].text = values[0]
        text_nodes[1].text = values[1]
        parent.insert(position + offset, paragraph)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    for value, expected in (
        ("Versão do documento: 0.4.105", 1),
        (ANCHOR, 1),
        (INSERT_MD, 0),
        (LIST_58_MD, 1),
        (LIST_59_MD, 0),
    ):
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada: {actual} != {expected} para {value[:80]!r}"
            )
    markdown = markdown.replace(
        LIST_58_MD, f"{LIST_58_MD}\n{LIST_59_MD}\n{LIST_510_MD}", 1
    )
    return markdown.replace(ANCHOR, f"{ANCHOR}\n\n{INSERT_MD}", 1)


def main() -> None:
    for image in (IMAGE_59, IMAGE_510):
        if not image.exists() or png_size(image) != (1978, 1480):
            raise RuntimeError(f"Imagem inexistente ou com dimensões inesperadas: {image}")
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    if "word/document.xml" not in entries or "word/_rels/document.xml.rels" not in entries:
        raise RuntimeError("Partes estruturais do DOCX em falta")
    original_hashes = {name: sha256(data).hexdigest() for name, data in entries.items()}
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    rels = etree.fromstring(entries["word/_rels/document.xml.rels"], parser)
    before = sensitive_state(root)

    anchors = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == ANCHOR]
    if len(anchors) != 1:
        raise RuntimeError(f"Parágrafo de inserção inesperado: {len(anchors)}")
    anchor = anchors[0]
    following = anchor.getnext()
    if following is None or not following.tag.endswith("}p"):
        raise RuntimeError("Parágrafo seguinte ao ponto de inserção não encontrado")
    captions = [
        p
        for p in root.xpath("//w:p", namespaces=NS)
        if text_of(p)
        == "Figura 5.8 — Interface de selecção, configuração paramétrica e materiais da plataforma HandFab."
    ]
    if len(captions) != 1:
        raise RuntimeError("Modelo de legenda da Figura 5.8 não encontrado")
    caption_template = captions[0]
    source_template = caption_template.getnext()
    if source_template is None or text_of(source_template) != SOURCE:
        raise RuntimeError("Modelo da fonte de produção própria não encontrado")

    max_docpr = max(
        (int(value) for value in root.xpath("//wp:docPr/@id", namespaces=NSX)),
        default=0,
    )
    rid_59 = next_relationship_id(rels)
    rel_59 = etree.SubElement(rels, q(REL, "Relationship"))
    rel_59.set("Id", rid_59)
    rel_59.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
    rel_59.set("Target", f"media/{IMAGE_59.name}")
    rid_510 = next_relationship_id(rels)
    rel_510 = etree.SubElement(rels, q(REL, "Relationship"))
    rel_510.set("Id", rid_510)
    rel_510.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
    rel_510.set("Target", f"media/{IMAGE_510.name}")

    sequence = (
        paragraph_from(following, EXPLANATION),
        blank_paragraph(following),
        image_paragraph(rid_59, IMAGE_59.name, *fit_size(IMAGE_59), max_docpr + 1),
        paragraph_from(caption_template, CAPTION_59),
        paragraph_from(source_template, SOURCE),
        blank_paragraph(following),
        image_paragraph(rid_510, IMAGE_510.name, *fit_size(IMAGE_510), max_docpr + 2),
        paragraph_from(caption_template, CAPTION_510),
        paragraph_from(source_template, SOURCE),
        blank_paragraph(following),
    )
    current = anchor
    for node in sequence:
        current.addnext(node)
        current = node
    add_list_rows(root)

    after = sensitive_state(root)
    expected = dict(before)
    expected["drawings"] += 2
    if after != expected:
        raise RuntimeError(f"Estrutura sensível inesperada: {before} -> {after}")
    body = text_of(root)
    for value, expected_count in (
        (EXPLANATION, 1),
        (CAPTION_59, 2),
        (CAPTION_510, 2),
    ):
        if body.count(value) != expected_count:
            raise RuntimeError(f"Conteúdo inserido de forma incorrecta: {value[:80]!r}")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    entries["word/_rels/document.xml.rels"] = etree.tostring(
        rels, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    new_media = {
        f"word/media/{IMAGE_59.name}": IMAGE_59.read_bytes(),
        f"word/media/{IMAGE_510.name}": IMAGE_510.read_bytes(),
    }
    for name in new_media:
        if name in entries:
            raise RuntimeError(f"Parte multimédia já existente: {name}")

    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
            for name, data in new_media.items():
                output.writestr(name, data)
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_entries = {name: result.read(name) for name in result.namelist()}
        allowed_changes = {"word/document.xml", "word/_rels/document.xml.rels"}
        for name, digest in original_hashes.items():
            if name not in allowed_changes and sha256(result_entries[name]).hexdigest() != digest:
                raise RuntimeError(f"Parte não autorizada alterada: {name}")
        for name, data in new_media.items():
            if result_entries.get(name) != data:
                raise RuntimeError(f"Imagem não integrada correctamente: {name}")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Figuras 5.9 e 5.10 inseridas; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
