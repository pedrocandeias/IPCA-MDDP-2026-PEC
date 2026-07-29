#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import TextIO
from zipfile import ZipFile
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"


@dataclass
class MarkdownBlock:
    line: int
    section: str
    text: str
    normalized: str


@dataclass
class CommentRecord:
    id: str
    author: str
    date: str
    comment: str
    marked_text: str
    paragraph_text: str
    docx_paragraph: int | None
    markdown_line: int | None
    markdown_section: str
    markdown_score: float
    action_hint: str


def tag(name: str) -> str:
    return f"{W}{name}"


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\(#ref-[^)]+\)", "", text)
    text = re.sub(r"\[\^[^\]]+\]", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#|]+", " ", text)
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def element_text(element: ET.Element) -> str:
    parts: list[str] = []
    for node in element.iter():
        if node.tag == tag("t"):
            parts.append(node.text or "")
        elif node.tag == tag("tab"):
            parts.append("\t")
        elif node.tag in {tag("br"), tag("cr")}:
            parts.append("\n")
    return "".join(parts).strip()


def extract_comments(comments_root: ET.Element) -> dict[str, dict[str, str]]:
    comments: dict[str, dict[str, str]] = {}
    for comment in comments_root.findall(tag("comment")):
        cid = comment.attrib.get(tag("id"))
        if cid is None:
            continue
        comments[cid] = {
            "author": comment.attrib.get(tag("author"), ""),
            "date": comment.attrib.get(tag("date"), ""),
            "comment": element_text(comment),
        }
    return comments


def paragraph_comment_refs(paragraph: ET.Element) -> dict[str, str]:
    active: list[str] = []
    refs: dict[str, list[str]] = {}

    for node in paragraph.iter():
        cid = node.attrib.get(tag("id"))
        if node.tag == tag("commentRangeStart") and cid is not None:
            if cid not in refs:
                refs[cid] = []
            active.append(cid)
            continue

        if node.tag == tag("commentReference") and cid is not None:
            refs.setdefault(cid, [])
            continue

        if node.tag == tag("t"):
            value = node.text or ""
        elif node.tag == tag("tab"):
            value = "\t"
        elif node.tag in {tag("br"), tag("cr")}:
            value = "\n"
        else:
            value = ""

        if value:
            for active_id in active:
                refs.setdefault(active_id, []).append(value)

        if node.tag == tag("commentRangeEnd") and cid is not None:
            if cid in active:
                active.remove(cid)

    return {cid: "".join(parts).strip() for cid, parts in refs.items()}


def extract_docx_comment_records(docx_path: Path) -> list[CommentRecord]:
    with ZipFile(docx_path) as docx:
        names = set(docx.namelist())
        if "word/comments.xml" not in names:
            raise RuntimeError(f"{docx_path} has no word/comments.xml")
        document_root = ET.fromstring(docx.read("word/document.xml"))
        comments_root = ET.fromstring(docx.read("word/comments.xml"))

    comments = extract_comments(comments_root)
    paragraph_lookup: dict[str, tuple[int, str, str]] = {}
    paragraphs = list(document_root.iter(tag("p")))
    for index, paragraph in enumerate(paragraphs):
        paragraph_text = element_text(paragraph)
        for cid, marked_text in paragraph_comment_refs(paragraph).items():
            paragraph_lookup[cid] = (index, marked_text or paragraph_text, paragraph_text)

    records: list[CommentRecord] = []
    for cid in sorted(comments, key=lambda value: int(value) if value.isdigit() else value):
        para_index, marked_text, paragraph_text = paragraph_lookup.get(cid, (None, "", ""))
        comment_text = comments[cid]["comment"]
        records.append(
            CommentRecord(
                id=cid,
                author=comments[cid]["author"],
                date=comments[cid]["date"],
                comment=comment_text,
                marked_text=marked_text,
                paragraph_text=paragraph_text,
                docx_paragraph=para_index,
                markdown_line=None,
                markdown_section="",
                markdown_score=0.0,
                action_hint=classify_action(comment_text),
            )
        )
    return records


def parse_markdown_blocks(markdown_path: Path) -> list[MarkdownBlock]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    blocks: list[MarkdownBlock] = []
    section = ""
    start_line: int | None = None
    current: list[str] = []

    def flush() -> None:
        nonlocal start_line, current
        if start_line is None or not current:
            start_line = None
            current = []
            return
        text = " ".join(line.strip() for line in current).strip()
        if text:
            blocks.append(MarkdownBlock(start_line, section, text, normalize(text)))
        start_line = None
        current = []

    for line_number, line in enumerate(lines, start=1):
        if line.startswith("#"):
            flush()
            section = line.strip("# ").strip()
            blocks.append(MarkdownBlock(line_number, section, line.strip(), normalize(line)))
            continue
        if not line.strip():
            flush()
            continue
        if start_line is None:
            start_line = line_number
        current.append(line)
    flush()
    return blocks


def match_markdown(records: list[CommentRecord], blocks: list[MarkdownBlock]) -> None:
    for record in records:
        source = normalize(record.paragraph_text or record.marked_text)
        if not source:
            continue

        best_block: MarkdownBlock | None = None
        best_score = 0.0
        for block in blocks:
            if not block.normalized:
                continue
            score = SequenceMatcher(None, source[:1200], block.normalized[:1200]).ratio()
            if len(source) > 80 and source[:80] in block.normalized:
                score = max(score, 0.98)
            if len(block.normalized) > 80 and block.normalized[:80] in source:
                score = max(score, 0.98)
            if score > best_score:
                best_score = score
                best_block = block

        if best_block is not None:
            record.markdown_line = best_block.line
            record.markdown_section = best_block.section
            record.markdown_score = round(best_score, 4)


def classify_action(comment: str) -> str:
    value = normalize(comment)
    if any(token in value for token in ["definir", "explicar", "o que e", "sigla"]):
        return "define_or_explain"
    if any(token in value for token in ["quem diz", "citar", "referencia", "apa"]):
        return "citation_or_source"
    if any(token in value for token in ["portugues", "ingr", "fala portugues"]):
        return "language_pt_pt"
    if any(token in value for token in ["cortamos", "cortar", "perdido", "tabela"]):
        return "structure_or_relevance"
    if any(token in value for token in ["expressao correta", "escalados", "julgamento"]):
        return "wording"
    return "review"


def compact(text: str, limit: int = 700) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def write_markdown(records: list[CommentRecord], output: TextIO, docx_path: Path, markdown_path: Path | None) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    output.write("# DOCX comment worklist\n\n")
    output.write(f"- Source DOCX: `{docx_path}`\n")
    if markdown_path is not None:
        output.write(f"- Matched manuscript: `{markdown_path}`\n")
    output.write(f"- Generated: {now}\n")
    output.write(f"- Comments: {len(records)}\n\n")

    for record in records:
        output.write(f"## Comment {record.id}\n\n")
        output.write(f"- Action hint: `{record.action_hint}`\n")
        output.write(f"- DOCX paragraph: `{record.docx_paragraph}`\n")
        if record.markdown_line is not None:
            output.write(
                f"- Markdown location: `{markdown_path}:{record.markdown_line}` "
                f"(score {record.markdown_score:.2f})\n"
            )
            if record.markdown_section:
                output.write(f"- Section: {record.markdown_section}\n")
        if record.author:
            output.write(f"- Author: {record.author}\n")
        if record.date:
            output.write(f"- Date: {record.date}\n")
        output.write("\nComment:\n\n")
        output.write(f"> {compact(record.comment, 1200)}\n\n")
        output.write("Marked text:\n\n")
        output.write(f"> {compact(record.marked_text or record.paragraph_text, 1200)}\n\n")


def write_json(records: list[CommentRecord], output: TextIO) -> None:
    json.dump([asdict(record) for record in records], output, ensure_ascii=False, indent=2)
    output.write("\n")


def write_csv(records: list[CommentRecord], output: TextIO) -> None:
    fieldnames = list(asdict(records[0]).keys()) if records else list(CommentRecord.__dataclass_fields__)
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(asdict(record))


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract DOCX comments and map them to a Markdown manuscript.")
    parser.add_argument("docx", type=Path, help="DOCX file containing comments")
    parser.add_argument("--manuscript", type=Path, help="Markdown manuscript to match against")
    parser.add_argument("--output", type=Path, help="Output path. Defaults to stdout.")
    parser.add_argument("--format", choices=["md", "json", "csv"], default="md")
    args = parser.parse_args()

    records = extract_docx_comment_records(args.docx)
    if args.manuscript:
        match_markdown(records, parse_markdown_blocks(args.manuscript))

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8", newline="") as output:
            write_records(records, output, args.docx, args.manuscript, args.format)
    else:
        write_records(records, sys.stdout, args.docx, args.manuscript, args.format)


def write_records(
    records: list[CommentRecord],
    output: TextIO,
    docx_path: Path,
    markdown_path: Path | None,
    output_format: str,
) -> None:
    if output_format == "json":
        write_json(records, output)
    elif output_format == "csv":
        write_csv(records, output)
    else:
        write_markdown(records, output, docx_path, markdown_path)


if __name__ == "__main__":
    main()
