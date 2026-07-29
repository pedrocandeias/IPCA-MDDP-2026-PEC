#!/usr/bin/env python3
"""Restore thesis footnotes lost during the IPCA-template migration.

The note text is recovered from the last pre-migration DOCX.  The script
inserts native Word footnote references at unambiguous anchors in the current
canonical DOCX, creates ``word/footnotes.xml``, and registers the OOXML part in
the package relationships and content types.

The operation is deliberately guarded: it refuses to run if the target already
contains footnote references, if an anchor is ambiguous, or if the optional
expected SHA-256 does not match.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W, "rel": REL, "ct": CT}

FOOTNOTE_REL_TYPE = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footnotes"
)
FOOTNOTE_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml"
)

DEFAULT_TARGET = Path(
    "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
)
DEFAULT_SOURCE = Path(
    "docs/versoes/backups/"
    "projecto-completo-docx-2026-07-13_16-32-11-"
    "before-integral-academic-revision.docx"
)

# source_id identifies the recovered note in the pre-migration DOCX.  Prefixes
# prevent a term in the acronym list or bibliography from being selected.
NOTE_SPECS = (
    {
        "source_id": 2,
        "paragraph_prefix": "Um atributo particularmente relevante",
        "anchor": "feedback proprioceptivo indireto",
        "italics": ("feedback",),
    },
    {
        "source_id": 4,
        "paragraph_prefix": "A avaliação da evidência",
        "anchor": "PRISMA",
        "italics": (
            "Preferred Reporting Items for Systematic Reviews and Meta Analyses",
        ),
    },
    {
        "source_id": 6,
        "paragraph_prefix": "Este modelo",
        "anchor": "“file-to-factory”",
        "italics": ("File-to-factory",),
    },
    {
        "source_id": 7,
        "paragraph_prefix": "A parametrização é",
        "anchor": "fronteiras de Pareto",
        "italics": (),
    },
    {
        "source_id": 8,
        "paragraph_prefix": "4. As imagens médicas",
        "anchor": "modelação estatística de forma",
        "italics": (),
    },
    {
        "source_id": 9,
        "paragraph_prefix": "– Modelos preditivos",
        "anchor": "análise de componentes principais (PCA)",
        "italics": (),
    },
    {
        "source_id": 10,
        "paragraph_prefix": "Dentro deste campo",
        "anchor": "redes neuronais artificiais",
        "italics": (),
    },
    {
        "source_id": 11,
        "paragraph_prefix": "Nos modelos generativos",
        "anchor": "prompts",
        "italics": ("prompt",),
    },
    {
        "source_id": 12,
        "paragraph_prefix": "Em saúde, plataformas",
        "anchor": "digital twins",
        "italics": ("digital twin",),
    },
    {
        "source_id": 13,
        "paragraph_prefix": "Na reabilitação",
        "anchor": "virtual coaching",
        "italics": ("Virtual coaching", "feedback"),
    },
    {
        "source_id": 14,
        "paragraph_prefix": "Na reabilitação",
        "anchor": "serious games",
        "italics": ("Serious games",),
    },
    {
        "source_id": 15,
        "paragraph_prefix": "A distância entre o potencial técnico",
        "anchor": "Technology Readiness Level (TRL)",
        "italics": ("Technology Readiness Level",),
    },
)


def qn(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def serialise(root: etree._Element) -> bytes:
    return etree.tostring(
        root,
        encoding="UTF-8",
        xml_declaration=True,
        standalone=True,
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def element_text(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def make_reference_run(note_id: int) -> etree._Element:
    run = etree.Element(qn(W, "r"))
    properties = etree.SubElement(run, qn(W, "rPr"))
    style = etree.SubElement(properties, qn(W, "rStyle"))
    style.set(qn(W, "val"), "FootnoteReference")
    reference = etree.SubElement(run, qn(W, "footnoteReference"))
    reference.set(qn(W, "id"), str(note_id))
    return run


def set_text(node: etree._Element, value: str) -> None:
    node.text = value
    if value.startswith(" ") or value.endswith(" "):
        node.set(qn(XML, "space"), "preserve")
    else:
        node.attrib.pop(qn(XML, "space"), None)


def insert_reference(paragraph: etree._Element, anchor: str, note_id: int) -> None:
    paragraph_text = element_text(paragraph)
    if paragraph_text.count(anchor) != 1:
        raise RuntimeError(
            f"Expected one occurrence of {anchor!r} in paragraph, found "
            f"{paragraph_text.count(anchor)}"
        )
    insertion_offset = paragraph_text.index(anchor) + len(anchor)
    offset = 0

    for text_node in paragraph.xpath(".//w:t", namespaces=NS):
        value = text_node.text or ""
        node_end = offset + len(value)
        if offset < insertion_offset <= node_end:
            run = text_node.getparent()
            if run.tag != qn(W, "r") or len(run.xpath("./w:t", namespaces=NS)) != 1:
                raise RuntimeError(f"Unsupported run structure at anchor {anchor!r}")
            parent = run.getparent()
            if parent.tag != qn(W, "p"):
                raise RuntimeError(f"Anchor {anchor!r} is not in a direct paragraph run")

            relative_offset = insertion_offset - offset
            run_index = parent.index(run)
            reference_run = make_reference_run(note_id)

            if relative_offset < len(value):
                suffix_run = deepcopy(run)
                suffix_text = suffix_run.xpath("./w:t", namespaces=NS)[0]
                set_text(text_node, value[:relative_offset])
                set_text(suffix_text, value[relative_offset:])
                parent.insert(run_index + 1, reference_run)
                parent.insert(run_index + 2, suffix_run)
            else:
                insert_at = run_index + 1
                # Keep an existing comment range limited to the selected word.
                while (
                    insert_at < len(parent)
                    and parent[insert_at].tag == qn(W, "commentRangeEnd")
                ):
                    insert_at += 1
                parent.insert(insert_at, reference_run)
            return
        offset = node_end

    raise RuntimeError(f"Could not locate insertion point for {anchor!r}")


def split_italic_segments(text: str, phrases: tuple[str, ...]) -> list[tuple[str, bool]]:
    segments: list[tuple[str, bool]] = [(text, False)]
    for phrase in phrases:
        updated: list[tuple[str, bool]] = []
        found = 0
        for segment, italic in segments:
            if italic or phrase not in segment:
                updated.append((segment, italic))
                continue
            before, matched, after = segment.partition(phrase)
            if before:
                updated.append((before, False))
            updated.append((matched, True))
            if after:
                updated.append((after, False))
            found += 1
        if found != 1:
            raise RuntimeError(
                f"Expected one occurrence of italic phrase {phrase!r}, found {found}"
            )
        segments = updated
    return segments


def make_footnote(note_id: int, text: str, italics: tuple[str, ...]) -> etree._Element:
    note = etree.Element(qn(W, "footnote"))
    note.set(qn(W, "id"), str(note_id))
    paragraph = etree.SubElement(note, qn(W, "p"))
    properties = etree.SubElement(paragraph, qn(W, "pPr"))
    style = etree.SubElement(properties, qn(W, "pStyle"))
    style.set(qn(W, "val"), "FootnoteText")

    marker_run = etree.SubElement(paragraph, qn(W, "r"))
    marker_properties = etree.SubElement(marker_run, qn(W, "rPr"))
    marker_style = etree.SubElement(marker_properties, qn(W, "rStyle"))
    marker_style.set(qn(W, "val"), "FootnoteReference")
    etree.SubElement(marker_run, qn(W, "footnoteRef"))

    tab_run = etree.SubElement(paragraph, qn(W, "r"))
    etree.SubElement(tab_run, qn(W, "tab"))

    for segment, italic in split_italic_segments(text, italics):
        run = etree.SubElement(paragraph, qn(W, "r"))
        if italic:
            run_properties = etree.SubElement(run, qn(W, "rPr"))
            etree.SubElement(run_properties, qn(W, "i"))
            etree.SubElement(run_properties, qn(W, "iCs"))
        text_node = etree.SubElement(run, qn(W, "t"))
        set_text(text_node, segment)
    return note


def load_source_notes(path: Path) -> tuple[etree._Element, dict[int, str]]:
    with ZipFile(path) as source_zip:
        root = etree.fromstring(source_zip.read("word/footnotes.xml"))
    notes: dict[int, str] = {}
    for note in root.xpath("./w:footnote", namespaces=NS):
        raw_id = note.get(qn(W, "id"))
        try:
            note_id = int(raw_id)
        except (TypeError, ValueError):
            continue
        if note_id > 0:
            notes[note_id] = " ".join(element_text(note).split())
    return root, notes


def ensure_relationship(root: etree._Element) -> None:
    existing = root.xpath(
        "./rel:Relationship[@Type=$type]", namespaces=NS, type=FOOTNOTE_REL_TYPE
    )
    if existing:
        raise RuntimeError("Target already has a footnotes relationship")
    used_ids = {rel.get("Id") for rel in root}
    number = 1
    while f"rId{number}" in used_ids:
        number += 1
    relationship = etree.SubElement(root, qn(REL, "Relationship"))
    relationship.set("Id", f"rId{number}")
    relationship.set("Type", FOOTNOTE_REL_TYPE)
    relationship.set("Target", "footnotes.xml")


def ensure_content_type(root: etree._Element) -> None:
    existing = root.xpath(
        "./ct:Override[@PartName='/word/footnotes.xml']", namespaces=NS
    )
    if existing:
        raise RuntimeError("Target already registers word/footnotes.xml")
    override = etree.SubElement(root, qn(CT, "Override"))
    override.set("PartName", "/word/footnotes.xml")
    override.set("ContentType", FOOTNOTE_CONTENT_TYPE)


def restore(target: Path, source: Path, expected_sha: str | None) -> None:
    if expected_sha and sha256(target) != expected_sha:
        raise RuntimeError(
            "Target SHA-256 changed after backup; refusing to overwrite a newer save"
        )

    source_root, source_notes = load_source_notes(source)
    with ZipFile(target) as target_zip:
        infos = target_zip.infolist()
        files = {info.filename: target_zip.read(info.filename) for info in infos}

    if "word/footnotes.xml" in files:
        raise RuntimeError("Target already contains word/footnotes.xml")

    document = etree.fromstring(files["word/document.xml"])
    if document.xpath("//w:footnoteReference", namespaces=NS):
        raise RuntimeError("Target already contains footnote references")

    paragraphs = document.xpath("//w:p", namespaces=NS)
    recovered: list[tuple[int, str, tuple[str, ...]]] = []
    for new_id, spec in enumerate(NOTE_SPECS, start=1):
        matches = [
            paragraph
            for paragraph in paragraphs
            if element_text(paragraph).startswith(spec["paragraph_prefix"])
            and spec["anchor"] in element_text(paragraph)
        ]
        if len(matches) != 1:
            raise RuntimeError(
                f"Expected one paragraph for {spec['anchor']!r}, found {len(matches)}"
            )
        source_id = spec["source_id"]
        note_text = source_notes.get(source_id, "")
        if not note_text:
            raise RuntimeError(f"Source footnote {source_id} is empty or missing")
        if note_text[-1] not in ".?!":
            note_text += "."
        insert_reference(matches[0], spec["anchor"], new_id)
        recovered.append((new_id, note_text, spec["italics"]))

    footnotes = etree.Element(source_root.tag, nsmap=source_root.nsmap)
    for name, value in source_root.attrib.items():
        footnotes.set(name, value)
    for system_note in source_root.xpath(
        "./w:footnote[number(@w:id) <= 0]", namespaces=NS
    ):
        footnotes.append(deepcopy(system_note))
    for note_id, note_text, italics in recovered:
        footnotes.append(make_footnote(note_id, note_text, italics))

    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    ensure_relationship(relationships)
    content_types = etree.fromstring(files["[Content_Types].xml"])
    ensure_content_type(content_types)

    files["word/document.xml"] = serialise(document)
    files["word/_rels/document.xml.rels"] = serialise(relationships)
    files["[Content_Types].xml"] = serialise(content_types)
    files["word/footnotes.xml"] = serialise(footnotes)

    temporary = target.with_name(f".{target.name}.footnotes.tmp")
    try:
        with ZipFile(temporary, "w") as output_zip:
            for info in infos:
                output_zip.writestr(info, files[info.filename])
            output_zip.writestr(
                "word/footnotes.xml",
                files["word/footnotes.xml"],
                compress_type=ZIP_DEFLATED,
            )
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()

    print(f"Restored {len(recovered)} native footnotes in {target}")
    print(f"SHA-256: {sha256(target)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--expected-sha")
    args = parser.parse_args()
    restore(args.target, args.source, args.expected_sha)


if __name__ == "__main__":
    main()
