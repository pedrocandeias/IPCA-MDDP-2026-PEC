#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import tempfile
from difflib import SequenceMatcher
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

ET.register_namespace("w", W_NS)
ET.register_namespace("", R_NS)

COMMENTS_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
COMMENTS_CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"

# Some source paragraphs were split or lightly rewritten after the comments were
# first created. These explicit mappings preserve the user's comment locations.
MANUAL_TARGETS = {
    "0": 31,
    "3": 100,
    "8": 126,
    "12": 146,
    "13": 147,
    "17": 152,
    "18": 152,
}


def qn(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def paragraph_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.findall(f".//{qn(W_NS, 't')}")).strip()


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\(#ref-[^)]+\)", "", text)
    text = re.sub(r"[^\wáéíóúàèìòùâêîôûãõçüñ]+", " ", text, flags=re.I)
    return re.sub(r"\s+", " ", text).strip()


def next_rel_id(rels_root: ET.Element) -> str:
    highest = 0
    for rel in rels_root.findall(qn(R_NS, "Relationship")):
        match = re.fullmatch(r"rId(\d+)", rel.attrib.get("Id", ""))
        if match:
            highest = max(highest, int(match.group(1)))
    return f"rId{highest + 1}"


def source_comment_paragraphs(source_doc_root: ET.Element) -> dict[str, str]:
    result: dict[str, str] = {}
    for p in source_doc_root.findall(f".//{qn(W_NS, 'p')}"):
        ids = set()
        for elem_name in ("commentRangeStart", "commentReference"):
            for elem in p.findall(f".//{qn(W_NS, elem_name)}"):
                cid = elem.attrib.get(qn(W_NS, "id"))
                if cid is not None:
                    ids.add(cid)
        for cid in ids:
            result[cid] = paragraph_text(p)
    return result


def map_comments_to_target(source_map: dict[str, str], target_paragraphs: list[ET.Element]) -> dict[str, int]:
    target_texts = [paragraph_text(p) for p in target_paragraphs]
    normalized_targets = [normalize(t) for t in target_texts]
    mapped: dict[str, int] = {}

    for cid, source_text in source_map.items():
        if cid in MANUAL_TARGETS:
            mapped[cid] = MANUAL_TARGETS[cid]
            continue

        normalized_source = normalize(source_text)
        best_score = -1.0
        best_index = 0
        for idx, normalized_target in enumerate(normalized_targets):
            if not normalized_target:
                continue
            score = SequenceMatcher(None, normalized_source[:900], normalized_target[:900]).ratio()
            if len(normalized_source) > 100 and normalized_source[:100] in normalized_target:
                score = max(score, 0.98)
            if score > best_score:
                best_score = score
                best_index = idx
        mapped[cid] = best_index

    return mapped


def add_comment_markers(paragraph: ET.Element, comment_ids: list[str]) -> None:
    if not comment_ids:
        return

    insert_at = 0
    if len(paragraph) and paragraph[0].tag == qn(W_NS, "pPr"):
        insert_at = 1

    for cid in reversed(comment_ids):
        start = ET.Element(qn(W_NS, "commentRangeStart"))
        start.set(qn(W_NS, "id"), cid)
        paragraph.insert(insert_at, start)

    for cid in reversed(comment_ids):
        end = ET.Element(qn(W_NS, "commentRangeEnd"))
        end.set(qn(W_NS, "id"), cid)
        paragraph.append(end)
        run = ET.Element(qn(W_NS, "r"))
        ref = ET.SubElement(run, qn(W_NS, "commentReference"))
        ref.set(qn(W_NS, "id"), cid)
        paragraph.append(run)


def raw_paragraph_spans(document_xml: str) -> list[re.Match[str]]:
    return list(re.finditer(r"<w:p(?:\s[^>]*)?>.*?</w:p>", document_xml, flags=re.S))


def add_comment_markers_raw(paragraph_xml: str, comment_ids: list[str]) -> str:
    comment_ids = sorted(comment_ids, key=lambda value: int(value))
    starts = "".join(f'<w:commentRangeStart w:id="{cid}"/>' for cid in comment_ids)
    ends = "".join(
        f'<w:commentRangeEnd w:id="{cid}"/><w:r><w:commentReference w:id="{cid}"/></w:r>'
        for cid in reversed(comment_ids)
    )

    ppr_match = re.search(r"<w:pPr\b[^>]*/>|<w:pPr\b[^>]*>.*?</w:pPr>", paragraph_xml, flags=re.S)
    if ppr_match:
        paragraph_xml = paragraph_xml[: ppr_match.end()] + starts + paragraph_xml[ppr_match.end() :]
    else:
        open_match = re.match(r"<w:p(?:\s[^>]*)?>", paragraph_xml)
        if not open_match:
            raise RuntimeError("Could not locate paragraph opening tag")
        paragraph_xml = paragraph_xml[: open_match.end()] + starts + paragraph_xml[open_match.end() :]

    close = paragraph_xml.rfind("</w:p>")
    if close < 0:
        raise RuntimeError("Could not locate paragraph closing tag")
    return paragraph_xml[:close] + ends + paragraph_xml[close:]


def insert_comment_markers_raw(document_xml: str, comments_by_paragraph: dict[int, list[str]]) -> str:
    paragraphs = raw_paragraph_spans(document_xml)
    for para_index in sorted(comments_by_paragraph, reverse=True):
        if para_index >= len(paragraphs):
            raise RuntimeError(f"Paragraph index {para_index} not found in target document")
        match = paragraphs[para_index]
        paragraph_xml = add_comment_markers_raw(match.group(0), comments_by_paragraph[para_index])
        document_xml = document_xml[: match.start()] + paragraph_xml + document_xml[match.end() :]
    return document_xml


def ensure_comments_relationship(rels_root: ET.Element) -> None:
    for rel in rels_root.findall(qn(R_NS, "Relationship")):
        if rel.attrib.get("Type") == COMMENTS_REL_TYPE:
            rel.set("Target", "comments.xml")
            return
    rel = ET.SubElement(rels_root, qn(R_NS, "Relationship"))
    rel.set("Id", next_rel_id(rels_root))
    rel.set("Type", COMMENTS_REL_TYPE)
    rel.set("Target", "comments.xml")


def ensure_comments_content_type(content_root: ET.Element) -> None:
    part_name = "/word/comments.xml"
    for override in content_root.findall(qn(CT_NS, "Override")):
        if override.attrib.get("PartName") == part_name:
            override.set("ContentType", COMMENTS_CONTENT_TYPE)
            return
    override = ET.SubElement(content_root, qn(CT_NS, "Override"))
    override.set("PartName", part_name)
    override.set("ContentType", COMMENTS_CONTENT_TYPE)


def ensure_comments_relationship_raw(rels_xml: str) -> str:
    if COMMENTS_REL_TYPE in rels_xml:
        return re.sub(
            rf'(<Relationship\b[^>]*Type="{re.escape(COMMENTS_REL_TYPE)}"[^>]*Target=")[^"]+(")',
            r"\1comments.xml\2",
            rels_xml,
        )

    ids = [int(match) for match in re.findall(r'Id="rId(\d+)"', rels_xml)]
    next_id_value = max(ids, default=0) + 1
    rel = (
        f'<Relationship Id="rId{next_id_value}" Type="{COMMENTS_REL_TYPE}" '
        'Target="comments.xml"/>'
    )
    return rels_xml.replace("</Relationships>", f"{rel}</Relationships>")


def ensure_comments_content_type_raw(content_xml: str) -> str:
    part_name = "/word/comments.xml"
    if part_name in content_xml:
        return re.sub(
            rf'(<Override\b[^>]*PartName="{re.escape(part_name)}"[^>]*ContentType=")[^"]+(")',
            rf"\1{COMMENTS_CONTENT_TYPE}\2",
            content_xml,
        )

    override = f'<Override PartName="{part_name}" ContentType="{COMMENTS_CONTENT_TYPE}"/>'
    return content_xml.replace("</Types>", f"{override}</Types>")


def recover_comments(source_docx: Path, target_docx: Path, output_docx: Path) -> None:
    with ZipFile(source_docx) as source_zip, ZipFile(target_docx) as target_zip:
        source_names = set(source_zip.namelist())
        if "word/comments.xml" not in source_names:
            raise RuntimeError(f"No word/comments.xml found in {source_docx}")

        source_doc_root = ET.fromstring(source_zip.read("word/document.xml"))
        comments_xml = source_zip.read("word/comments.xml")
        target_doc_root = ET.fromstring(target_zip.read("word/document.xml"))
        target_document_xml = target_zip.read("word/document.xml").decode("utf-8")
        target_rels_xml = target_zip.read("word/_rels/document.xml.rels").decode("utf-8")
        content_xml = target_zip.read("[Content_Types].xml").decode("utf-8")

        source_map = source_comment_paragraphs(source_doc_root)
        target_paragraphs = target_doc_root.findall(f".//{qn(W_NS, 'p')}")
        comment_to_paragraph = map_comments_to_target(source_map, target_paragraphs)

        comments_by_paragraph: dict[int, list[str]] = {}
        for cid, para_index in comment_to_paragraph.items():
            comments_by_paragraph.setdefault(para_index, []).append(cid)

        target_document_xml = insert_comment_markers_raw(target_document_xml, comments_by_paragraph)
        target_rels_xml = ensure_comments_relationship_raw(target_rels_xml)
        content_xml = ensure_comments_content_type_raw(content_xml)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp_path = Path(tmp.name)

        skip = {
            "word/document.xml",
            "word/_rels/document.xml.rels",
            "[Content_Types].xml",
            "word/comments.xml",
        }
        with ZipFile(tmp_path, "w", ZIP_DEFLATED) as out_zip:
            for item in target_zip.infolist():
                if item.filename in skip:
                    continue
                out_zip.writestr(item, target_zip.read(item.filename))
            out_zip.writestr("[Content_Types].xml", content_xml.encode("utf-8"))
            out_zip.writestr("word/document.xml", target_document_xml.encode("utf-8"))
            out_zip.writestr("word/_rels/document.xml.rels", target_rels_xml.encode("utf-8"))
            out_zip.writestr("word/comments.xml", comments_xml)

    shutil.move(tmp_path, output_docx)
    print(f"Recovered {len(source_map)} comments into {output_docx}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Recover Word comments from one DOCX into another.")
    parser.add_argument("source_docx", type=Path)
    parser.add_argument("target_docx", type=Path)
    parser.add_argument("output_docx", type=Path)
    args = parser.parse_args()
    recover_comments(args.source_docx, args.target_docx, args.output_docx)


if __name__ == "__main__":
    main()
