#!/usr/bin/env python3
"""Restore the validated IPCA paragraph formats in the canonical DOCX.

The DOCX saved by Microsoft Word on 22 July 2026 localised built-in style
identifiers and also replaced several of their definitions with Word defaults.
In particular, ``Normal`` lost the 10 pt size used by the IPCA template, so
``Texto Normal - IPCA`` began to inherit 12 pt. Four paragraphs kept the
separate ``Body Text``/``Corpo de texto`` style at 10 pt and consequently
appeared as visibly different blocks on printed pages 66–67.

This transformation:

* restores the paragraph and run properties of every paragraph style used in
  the current DOCX from the last validated IPCA-formatted export;
* matches styles by their stable ``w:name`` rather than by localised style ID;
* reassigns the four accidental ``Body Text`` paragraphs to
  ``Texto Normal - IPCA``;
* preserves document content, live Mendeley controls, comments, footnotes,
  relationships, media and all other package parts.

The reference export is itself a LibreOffice-normalised derivative of
``projeto-mestrado-template-ipca.docx`` and corresponds to the validated PDF
layout used before the Word style drift.
"""

from __future__ import annotations

import argparse
import re
from copy import deepcopy
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from lxml import etree


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL = REPO_ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
REFERENCE = (
    REPO_ROOT
    / "docs/versoes/exportacoes/2026-07-20_22-29-13-correcao-mpt-icf-106"
    / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
)

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

BODY_TEXT_PREFIXES = (
    "A ponta do dedo médio apresenta uma geometria aberta",
    "O percurso evidencia ainda que o valor de 64 mm",
    "Os registos de parâmetros, as malhas, o percurso de transformação",
    "Os exemplos complementares do Anexo C mostram duas dependências",
)

RTD_TABLE_TITLE = (
    "Tabela 4 — Ciclos de Research Through Design documentados no desenvolvimento"
)
RTD_BOOKMARK = "_TocRTDTable4"


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def serialise(root: etree._Element) -> bytes:
    return etree.tostring(
        root,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS)).strip()


def style_name(style: etree._Element) -> str:
    values = style.xpath("./w:name/@w:val", namespaces=NS)
    if len(values) != 1:
        raise RuntimeError("Paragraph style without one stable w:name")
    return values[0]


def style_id(style: etree._Element) -> str:
    value = style.get(qn("styleId"))
    if not value:
        raise RuntimeError(f"Style {style_name(style)!r} without w:styleId")
    return value


def paragraph_styles(root: etree._Element) -> list[etree._Element]:
    return root.xpath("//w:style[@w:type='paragraph']", namespaces=NS)


def used_paragraph_style_ids(document: etree._Element) -> set[str]:
    return set(document.xpath("//w:pPr/w:pStyle/@w:val", namespaces=NS))


def replace_format_properties(
    destination: etree._Element,
    source: etree._Element,
) -> None:
    """Copy only pPr/rPr, retaining local IDs and valid style links."""

    for local_name in ("pPr", "rPr"):
        current = destination.find(f"w:{local_name}", NS)
        if current is not None:
            destination.remove(current)
    for local_name in ("pPr", "rPr"):
        reference = source.find(f"w:{local_name}", NS)
        if reference is not None:
            destination.append(deepcopy(reference))


def restore_used_styles(
    current_styles: etree._Element,
    reference_styles: etree._Element,
    document: etree._Element,
) -> list[tuple[str, str]]:
    current_by_id = {style_id(s): s for s in paragraph_styles(current_styles)}
    current_ids_by_name = {
        style_name(s): style_id(s) for s in paragraph_styles(current_styles)
    }
    reference_by_name = {
        style_name(s): s for s in paragraph_styles(reference_styles)
    }
    restored: list[tuple[str, str]] = []

    used_ids = used_paragraph_style_ids(document)
    normal_id = current_ids_by_name.get("Normal")
    if normal_id:
        used_ids.add(normal_id)
    for current_id in sorted(used_ids):
        current = current_by_id.get(current_id)
        if current is None:
            raise RuntimeError(f"Used paragraph style is undefined: {current_id}")
        name = style_name(current)
        reference = reference_by_name.get(name)
        if reference is None:
            # Annex-local index styles were created after the reference export.
            # They intentionally inherit from the restored TOC styles and do
            # not need an independent reference definition.
            continue
        replace_format_properties(current, reference)
        restored.append((current_id, name))

    required = {
        "Normal",
        "Texto Normal - IPCA",
        "heading 1",
        "heading 2",
        "heading 3",
        "heading 4",
        "Bibliography",
        "caption",
        "Nota - IPCA",
        "toc 1",
        "toc 2",
        "toc 3",
        "table of figures",
    }
    restored_names = {name for _, name in restored}
    missing = sorted(required - restored_names)
    if missing:
        raise RuntimeError(f"Required IPCA styles were not restored: {missing}")
    return restored


def reassign_body_text_blocks(
    document: etree._Element,
    styles: etree._Element,
) -> list[str]:
    current_styles = paragraph_styles(styles)
    ids_by_name = {style_name(s): style_id(s) for s in current_styles}
    body_text_id = ids_by_name.get("Body Text")
    ipca_id = ids_by_name.get("Texto Normal - IPCA")
    if not body_text_id or not ipca_id:
        raise RuntimeError("Body Text or Texto Normal - IPCA style is missing")

    matches: dict[str, etree._Element] = {}
    unexpected: list[str] = []
    for paragraph in document.xpath("//w:body/w:p", namespaces=NS):
        values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        if values != [body_text_id]:
            continue
        text = paragraph_text(paragraph)
        if not text:
            continue
        prefix = next((p for p in BODY_TEXT_PREFIXES if text.startswith(p)), None)
        if prefix is None:
            unexpected.append(text[:120])
            continue
        if prefix in matches:
            raise RuntimeError(f"Duplicate Body Text block: {prefix!r}")
        matches[prefix] = paragraph

    missing = [prefix for prefix in BODY_TEXT_PREFIXES if prefix not in matches]
    if missing or unexpected:
        raise RuntimeError(
            "Unexpected Body Text block set; "
            f"missing={missing!r}, unexpected={unexpected!r}"
        )

    for paragraph in matches.values():
        style = paragraph.find("./w:pPr/w:pStyle", NS)
        if style is None:
            raise RuntimeError("Matched Body Text paragraph has no pStyle")
        style.set(qn("val"), ipca_id)
    return [paragraph_text(matches[prefix]) for prefix in BODY_TEXT_PREFIXES]


def paragraph_style_name(
    paragraph: etree._Element,
    names_by_id: dict[str, str],
) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return names_by_id.get(values[0], "") if values else ""


def add_rtd_table_index_entry(
    document: etree._Element,
    names_by_id: dict[str, str],
) -> bool:
    """Add the table-list entry omitted when the RTD caption gained a SEQ."""

    body_caption = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_text(paragraph) == RTD_TABLE_TITLE
        and paragraph_style_name(paragraph, names_by_id) == "caption"
    ]
    if len(body_caption) != 1:
        raise RuntimeError(
            f"Expected one RTD table caption; found {len(body_caption)}"
        )
    existing = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_text(paragraph).startswith(RTD_TABLE_TITLE)
        and paragraph_style_name(paragraph, names_by_id) == "table of figures"
    ]
    if existing:
        if len(existing) != 1:
            raise RuntimeError(f"Duplicate RTD table-list entries: {len(existing)}")
        return False

    caption = body_caption[0]
    bookmark_names = set(
        document.xpath("//w:bookmarkStart/@w:name", namespaces=NS)
    )
    if RTD_BOOKMARK in bookmark_names:
        raise RuntimeError(f"Orphan bookmark already exists: {RTD_BOOKMARK}")
    bookmark_ids = [
        int(value)
        for value in document.xpath("//w:bookmarkStart/@w:id", namespaces=NS)
        if value.isdigit()
    ]
    bookmark_id = str(max(bookmark_ids, default=0) + 1)
    start = etree.Element(qn("bookmarkStart"))
    start.set(qn("id"), bookmark_id)
    start.set(qn("name"), RTD_BOOKMARK)
    end = etree.Element(qn("bookmarkEnd"))
    end.set(qn("id"), bookmark_id)
    insertion_index = 1 if caption.find("w:pPr", NS) is not None else 0
    caption.insert(insertion_index, start)
    caption.append(end)

    table_entries = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_style_name(paragraph, names_by_id) == "table of figures"
        and paragraph_text(paragraph).startswith("Tabela ")
    ]
    preceding = [
        paragraph
        for paragraph in table_entries
        if paragraph_text(paragraph).startswith("Tabela 3 ")
    ]
    if len(preceding) != 1:
        raise RuntimeError(
            f"Expected one Table 3 list entry; found {len(preceding)}"
        )
    entry = deepcopy(preceding[0])
    for attribute in list(entry.attrib):
        if etree.QName(attribute).localname in {"paraId", "textId"}:
            del entry.attrib[attribute]
    hyperlinks = entry.xpath("./w:hyperlink", namespaces=NS)
    if len(hyperlinks) != 1:
        raise RuntimeError("Reference table-list entry has no single hyperlink")
    hyperlinks[0].set(qn("history"), "1")
    hyperlinks[0].set(qn("anchor"), RTD_BOOKMARK)
    text_nodes = entry.xpath(".//w:t", namespaces=NS)
    if len(text_nodes) != 2:
        raise RuntimeError("Reference table-list entry is not a two-text entry")
    text_nodes[0].text = RTD_TABLE_TITLE
    text_nodes[1].text = "—"
    instructions = entry.xpath(".//w:instrText", namespaces=NS)
    if len(instructions) != 1:
        raise RuntimeError("Reference table-list entry has no single PAGEREF")
    instructions[0].text = f" PAGEREF {RTD_BOOKMARK} \\h "
    preceding[0].addnext(entry)
    return True


def refresh_sequence_fields_and_lists(
    document: etree._Element,
    styles: etree._Element,
) -> tuple[dict[str, int], bool, int]:
    """Refresh cached SEQ numbers and their static figure/table-list labels."""

    names_by_id = {
        style_id(style): style_name(style) for style in paragraph_styles(styles)
    }
    counters = {"Tabela": 0, "Figura": 0}
    for field in document.xpath("//w:fldSimple", namespaces=NS):
        instruction = field.get(qn("instr"), "")
        match = re.search(r"\bSEQ\s+(Tabela|Figura)\b", instruction)
        if match is None:
            continue
        kind = match.group(1)
        counters[kind] += 1
        numeric_nodes = [
            node
            for node in field.xpath(".//w:t", namespaces=NS)
            if (node.text or "").strip().isdigit()
        ]
        if len(numeric_nodes) != 1:
            raise RuntimeError(
                f"{kind} SEQ field does not contain one cached integer result"
            )
        numeric_nodes[0].text = str(counters[kind])

    expected = {"Tabela": 31, "Figura": 29}
    if counters != expected:
        raise RuntimeError(f"Unexpected SEQ field counts: {counters}")

    inserted = add_rtd_table_index_entry(document, names_by_id)
    list_counts = {"Tabela": 0, "Figura": 0}
    updated_labels = 0
    for paragraph in document.xpath("//w:body/w:p", namespaces=NS):
        if paragraph_style_name(paragraph, names_by_id) != "table of figures":
            continue
        text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
        if len(text_nodes) != 2:
            continue
        title = text_nodes[0].text or ""
        match = re.match(r"^(Tabela|Figura)\s+\d+", title)
        if match is None:
            continue
        kind = match.group(1)
        list_counts[kind] += 1
        replacement = f"{kind} {list_counts[kind]}"
        updated = replacement + title[match.end() :]
        if updated != title:
            text_nodes[0].text = updated
            updated_labels += 1

    if list_counts != expected:
        raise RuntimeError(f"Unexpected static list counts: {list_counts}")
    return counters, inserted, updated_labels


def clear_mendeley_bibliography_placeholder(
    document: etree._Element,
) -> bool:
    """Hide no content: clear only the visible Mendeley dummy placeholder."""

    controls = document.xpath(
        "//w:body/w:sdt[w:sdtPr/w:tag[@w:val='MENDELEY_BIBLIOGRAPHY']]",
        namespaces=NS,
    )
    if len(controls) != 1:
        raise RuntimeError(
            "Expected one top-level MENDELEY_BIBLIOGRAPHY control; "
            f"found {len(controls)}"
        )
    control = controls[0]
    current = "".join(
        control.xpath("./w:sdtContent//w:t/text()", namespaces=NS)
    ).strip()
    if current != "initial value":
        raise RuntimeError(
            f"Unexpected Mendeley bibliography placeholder: {current!r}"
        )
    nodes = control.xpath("./w:sdtContent//w:t", namespaces=NS)
    if len(nodes) != 3:
        raise RuntimeError(
            f"Unexpected placeholder text-node count: {len(nodes)}"
        )
    for node in nodes:
        node.text = ""
        node.attrib.pop(
            "{http://www.w3.org/XML/1998/namespace}space",
            None,
        )
    return True


def remove_trailing_blank_page_section(
    document: etree._Element,
) -> tuple[bool, bool]:
    """Collapse the empty final section that alone generated printed page 200."""

    body = document.find(".//w:body", NS)
    if body is None:
        raise RuntimeError("DOCX has no w:body")
    children = list(body)
    if len(children) < 2 or children[-1].tag != qn("sectPr"):
        raise RuntimeError("DOCX body does not end with the final sectPr")
    paragraph = children[-2]
    if paragraph.tag != qn("p"):
        raise RuntimeError("Element before the final sectPr is not a paragraph")
    if paragraph_text(paragraph) or paragraph.xpath(
        ".//w:drawing|.//w:sectPr|.//w:br",
        namespaces=NS,
    ):
        return False, False
    style = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    first_line = paragraph.xpath("./w:pPr/w:ind/@w:firstLine", namespaces=NS)
    if style != ["TextoNormal-IPCA"] or first_line != ["0"]:
        raise RuntimeError(
            "Unexpected trailing empty paragraph; refusing broad deletion"
        )
    previous_text = paragraph_text(children[-3]) if len(children) >= 3 else ""
    if not previous_text.startswith("36,29 €/kg"):
        raise RuntimeError(
            "Trailing empty paragraph is not after the expected final text"
        )
    body.remove(paragraph)

    # The preceding content paragraph also carries a section break. The final
    # body-level sectPr therefore described a new, empty section. Promote the
    # content section properties to the body-level final sectPr and remove the
    # embedded break.
    children = list(body)
    content = children[-2]
    if content.tag != qn("p"):
        raise RuntimeError("Final content before sectPr is not a paragraph")
    embedded = content.find("./w:pPr/w:sectPr", NS)
    final_section = children[-1]
    if embedded is None or final_section.tag != qn("sectPr"):
        raise RuntimeError("Expected final content section break was not found")
    if not paragraph_text(content).startswith("36,29 €/kg"):
        raise RuntimeError("Final section break is not attached to expected text")
    parent = embedded.getparent()
    if parent is None:
        raise RuntimeError("Final embedded sectPr has no parent")
    replacement = deepcopy(embedded)
    parent.remove(embedded)
    body.replace(final_section, replacement)
    return True, True


def package_parts(path: Path) -> tuple[list[ZipInfo], dict[str, bytes]]:
    with ZipFile(path) as archive:
        infos = archive.infolist()
        parts = {info.filename: archive.read(info.filename) for info in infos}
    return infos, parts


def write_package(
    output: Path,
    infos: list[ZipInfo],
    parts: dict[str, bytes],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        prefix=f".{output.name}.",
        suffix=".tmp",
        dir=output.parent,
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED) as archive:
            for info in infos:
                archive.writestr(info, parts[info.filename])
        with ZipFile(temporary) as check:
            corrupt = check.testzip()
            if corrupt is not None:
                raise RuntimeError(f"Corrupt DOCX part after write: {corrupt}")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)


def transform(source: Path, reference: Path, output: Path) -> None:
    infos, parts = package_parts(source)
    _, reference_parts = package_parts(reference)

    untouched_before = {
        name: data
        for name, data in parts.items()
        if name not in {"word/document.xml", "word/styles.xml"}
    }
    document_before = parts["word/document.xml"]
    mendeley_before = document_before.count(b"MENDELEY_CITATION_v3")

    parser = etree.XMLParser(remove_blank_text=False)
    document = etree.fromstring(document_before, parser)
    styles = etree.fromstring(parts["word/styles.xml"], parser)
    reference_styles = etree.fromstring(reference_parts["word/styles.xml"], parser)

    restored = restore_used_styles(styles, reference_styles, document)
    reassigned = reassign_body_text_blocks(document, styles)
    cleared_bibliography_placeholder = clear_mendeley_bibliography_placeholder(
        document
    )
    sequences, inserted_index, updated_labels = refresh_sequence_fields_and_lists(
        document,
        styles,
    )
    removed_blank_paragraph, collapsed_blank_section = (
        remove_trailing_blank_page_section(document)
    )

    parts["word/document.xml"] = serialise(document)
    parts["word/styles.xml"] = serialise(styles)

    mendeley_after = parts["word/document.xml"].count(b"MENDELEY_CITATION_v3")
    if mendeley_after != mendeley_before:
        raise RuntimeError(
            f"Mendeley live-citation count changed: {mendeley_before} -> {mendeley_after}"
        )
    if any(parts[name] != data for name, data in untouched_before.items()):
        raise RuntimeError("A package part outside document.xml/styles.xml changed")

    write_package(output, infos, parts)
    print(f"Output: {output}")
    print(f"Restored paragraph styles: {len(restored)}")
    for current_id, name in restored:
        print(f"  {current_id}: {name}")
    print(f"Reassigned Body Text blocks: {len(reassigned)}")
    print(
        "Cleared visible Mendeley bibliography placeholder: "
        f"{cleared_bibliography_placeholder}"
    )
    print(
        "Refreshed SEQ fields: "
        f"{sequences['Tabela']} tables, {sequences['Figura']} figures"
    )
    print(f"Inserted missing RTD table-list entry: {inserted_index}")
    print(f"Renumbered static list labels: {updated_labels}")
    print(f"Removed trailing blank-page paragraph: {removed_blank_paragraph}")
    print(f"Collapsed trailing empty section: {collapsed_blank_section}")
    print(f"Live Mendeley citations preserved: {mendeley_after}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=CANONICAL)
    parser.add_argument("--reference", type=Path, default=REFERENCE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    source = args.source.resolve()
    reference = args.reference.resolve()
    output = (args.output or source).resolve()
    for path, label in ((source, "source"), (reference, "reference")):
        if not path.is_file():
            raise FileNotFoundError(f"Missing {label} DOCX: {path}")
    transform(source, reference, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
