#!/usr/bin/env python3
"""Actualiza no DOCX 0.4.74 os nomes dos ficheiros dos suplementos.

O programa altera apenas ``word/document.xml``. As notas, os comentários, as
imagens e todos os restantes componentes do pacote são preservados byte a byte.
"""

from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx")
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def text_of(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def replace_fragment(paragraph: etree._Element, old: str, new: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    full = "".join(node.text or "" for node in nodes)
    if full.count(old) != 1:
        raise RuntimeError(f"Fragmento não unívoco: {old!r}; texto={full!r}")
    start = full.index(old)
    end = start + len(old)
    positions = []
    cursor = 0
    for node in nodes:
        value = node.text or ""
        positions.append((node, cursor, cursor + len(value)))
        cursor += len(value)
    first_node, first_start, _ = next(item for item in positions if item[2] > start)
    last_node, last_start, _ = next(
        item for item in positions if item[2] >= end and item[1] < end
    )
    prefix = (first_node.text or "")[: start - first_start]
    suffix = (last_node.text or "")[end - last_start :]
    if first_node is last_node:
        first_node.text = prefix + new + suffix
        set_space(first_node)
        return
    first_node.text = prefix + new
    set_space(first_node)
    clearing = False
    for node, _, _ in positions:
        if node is first_node:
            clearing = True
            continue
        if not clearing:
            continue
        if node is last_node:
            node.text = suffix
            set_space(node)
            break
        node.text = ""
        set_space(node)


def replace_once(root: etree._Element, old: str, new: str) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if old in text_of(paragraph)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava uma ocorrência de {old!r}; encontrei {len(matches)}")
    replace_fragment(matches[0], old, new)


def document_state(root: etree._Element) -> dict[str, int]:
    return {
        "notas": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comentarios": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "imagens": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def main() -> None:
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    root = etree.fromstring(entries["word/document.xml"])
    before = document_state(root)
    replace_once(
        root,
        "O ficheiro manifesto_ficheiros.csv relaciona cada elemento com a sua "
        "origem e função, enquanto SHA256SUMS permite verificar a integridade do pacote.",
        "O ficheiro guia_dos_suplementos.md apresenta o conteúdo de cada conjunto. "
        "O ficheiro manifesto_ficheiros.csv relaciona cada elemento com a sua origem "
        "e função.",
    )
    after = document_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(dir=DOCX.parent, suffix=".docx", delete=False) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for info in infos:
                target.writestr(info, entries[info.filename])
        with ZipFile(temporary) as check:
            outside = {
                name: sha256(check.read(name)).hexdigest()
                for name in check.namelist()
                if name != "word/document.xml"
            }
        if outside != hashes:
            raise RuntimeError("Foram alterados componentes do DOCX além do documento principal")
        temporary.replace(DOCX)
    finally:
        temporary.unlink(missing_ok=True)
    print(
        "Nomes dos suplementos actualizados no DOCX; "
        f"notas={after['notas']}, comentários={after['comentarios']}, "
        f"imagens={after['imagens']}"
    )


if __name__ == "__main__":
    main()
