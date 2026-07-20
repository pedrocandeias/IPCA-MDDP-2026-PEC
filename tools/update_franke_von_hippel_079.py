#!/usr/bin/env python3
"""Corrige Franke/von Hippel e a formulação sobre *toolkits* no manuscrito."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

OLD_FRANKE_CITATION = "Franke & Hippel, 2002"
NEW_FRANKE_CITATION = "Franke & von Hippel, 2003"
OLD_KATZ_CITATION = "Hippel & Katz, 2002"
NEW_KATZ_CITATION = "von Hippel & Katz, 2002"
OLD_CLAIM = "criar configurações num ambiente com regras e resposta visual"
NEW_CLAIM = (
    "criar configurações num espaço de projecto delimitado, com regras, simulação e "
    "avaliação iterativa dos resultados"
)

OLD_FRANKE_ENTRY = (
    "Franke, N., & von Hippel, E. (2002). Satisfying heterogeneous user needs via "
    "innovation toolkits: The case of Apache security software."
)
FRANKE_PREFIX = (
    "Franke, N., & von Hippel, E. (2003). Satisfying heterogeneous user needs via "
    "innovation toolkits: The case of Apache security software. "
)
FRANKE_JOURNAL = "Research Policy, 32"
FRANKE_SUFFIX = (
    "(7), 1199–1215. https://doi.org/10.1016/S0048-7333(03)00049-0"
)
NEW_FRANKE_DOCX = FRANKE_PREFIX + FRANKE_JOURNAL + FRANKE_SUFFIX
NEW_FRANKE_MD = FRANKE_PREFIX + f"*{FRANKE_JOURNAL}*" + FRANKE_SUFFIX

OLD_KATZ_ENTRY = (
    "Hippel, E. von, & Katz, R. (2002). Shifting innovation to users via toolkits. "
    "Management Science, 48(7)."
)
KATZ_PREFIX = (
    "von Hippel, E., & Katz, R. (2002). Shifting innovation to users via toolkits. "
)
KATZ_JOURNAL = "Management Science, 48"
KATZ_SUFFIX = "(7), 821–833. https://doi.org/10.1287/mnsc.48.7.821.2817"
NEW_KATZ_DOCX = KATZ_PREFIX + KATZ_JOURNAL + KATZ_SUFFIX
NEW_KATZ_MD = KATZ_PREFIX + f"*{KATZ_JOURNAL}*" + KATZ_SUFFIX


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def find_exact(root: etree._Element, value: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == value]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo para {value[:70]!r}; encontrei {len(matches)}")
    return matches[0]


def replace_fragment(paragraph: etree._Element, old: str, new: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    full = "".join(node.text or "" for node in nodes)
    if full.count(old) != 1:
        raise RuntimeError(f"Fragmento não unívoco: {old!r}; texto={full!r}")
    start = full.index(old)
    end = start + len(old)
    positions: list[tuple[etree._Element, int, int]] = []
    cursor = 0
    for node in nodes:
        value = node.text or ""
        positions.append((node, cursor, cursor + len(value)))
        cursor += len(value)
    first_node, first_start, _ = next(item for item in positions if item[2] > start)
    last_node, last_start, _ = next(item for item in positions if item[2] >= end and item[1] < end)
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


def replace_all(root: etree._Element, old: str, new: str, expected: int) -> None:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if old in text_of(p)]
    if len(matches) != expected:
        raise RuntimeError(f"Esperava {expected} parágrafos com {old!r}; encontrei {len(matches)}")
    for paragraph in matches:
        replace_fragment(paragraph, old, new)


def add_run(paragraph: etree._Element, value: str, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        rpr = etree.SubElement(run, qn("rPr"))
        etree.SubElement(rpr, qn("i"))
        etree.SubElement(rpr, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_bibliography(
    paragraph: etree._Element, prefix: str, journal: str, suffix: str
) -> None:
    ppr = paragraph.find(qn("pPr"))
    ppr_copy = deepcopy(ppr) if ppr is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if ppr_copy is not None:
        paragraph.append(ppr_copy)
    add_run(paragraph, prefix)
    add_run(paragraph, journal, italic=True)
    add_run(paragraph, suffix)


def state(root: etree._Element) -> dict[str, int]:
    text = text_of(root)
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "franke_citations": text.count(OLD_FRANKE_CITATION)
        + text.count(NEW_FRANKE_CITATION),
        # The corrected form contains the old text as a substring; counting
        # the shared tail yields the number of citations before and after.
        "katz_citations": text.count(OLD_KATZ_CITATION),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    exact_replacements = [
        ("Versão do documento: 0.4.78", "Versão do documento: 0.4.79"),
        (OLD_CLAIM, NEW_CLAIM),
        (OLD_FRANKE_ENTRY, NEW_FRANKE_MD),
        (OLD_KATZ_ENTRY, NEW_KATZ_MD),
        ('id="ref-franke-2002"', 'id="ref-franke-2003"'),
    ]
    for old, new in exact_replacements:
        if markdown.count(old) != 1:
            raise RuntimeError(f"Ocorrência Markdown inesperada para {old[:70]!r}")
        markdown = markdown.replace(old, new, 1)
    if markdown.count(OLD_FRANKE_CITATION) != 1:
        raise RuntimeError("A citação antiga de Franke não é única no Markdown")
    if markdown.count(OLD_KATZ_CITATION) != 3:
        raise RuntimeError("A citação antiga de von Hippel e Katz não ocorre três vezes")
    markdown = markdown.replace(OLD_FRANKE_CITATION, NEW_FRANKE_CITATION)
    markdown = markdown.replace(OLD_KATZ_CITATION, NEW_KATZ_CITATION)
    return markdown


def main() -> None:
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    before = state(root)
    if before["franke_citations"] != 1 or before["katz_citations"] != 3:
        raise RuntimeError(f"Contagens iniciais inesperadas: {before}")

    replace_all(root, OLD_CLAIM, NEW_CLAIM, 1)
    replace_all(root, OLD_FRANKE_CITATION, NEW_FRANKE_CITATION, 1)
    replace_all(root, OLD_KATZ_CITATION, NEW_KATZ_CITATION, 3)
    replace_bibliography(
        find_exact(root, OLD_FRANKE_ENTRY),
        FRANKE_PREFIX,
        FRANKE_JOURNAL,
        FRANKE_SUFFIX,
    )
    replace_bibliography(
        find_exact(root, OLD_KATZ_ENTRY),
        KATZ_PREFIX,
        KATZ_JOURNAL,
        KATZ_SUFFIX,
    )
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível ou citações alteradas: {before} -> {after}")
    body = text_of(root)
    if body.count(NEW_FRANKE_DOCX) != 1 or body.count(NEW_KATZ_DOCX) != 1:
        raise RuntimeError("Uma das entradas bibliográficas não ficou íntegra no DOCX")
    if OLD_FRANKE_CITATION in body or body.count(NEW_KATZ_CITATION) != 3:
        raise RuntimeError("Permaneceram citações antigas ou incompletas no DOCX")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Franke e von Hippel corrigidos; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, citações Franke={after['franke_citations']}, "
        f"citações von Hippel e Katz={after['katz_citations']}"
    )


if __name__ == "__main__":
    main()
