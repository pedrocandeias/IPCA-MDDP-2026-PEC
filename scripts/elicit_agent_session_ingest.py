#!/usr/bin/env python3
"""Ingest local Elicit agent-session exports into a structured workspace folder.

The script copies raw files, extracts readable text when possible, detects
bibliography artifacts, and writes a local manifest so the material can later be
used to enrich the manuscript.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import subprocess
import sys
import textwrap
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


class IngestError(RuntimeError):
    pass


def slugify(text: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    normalized = normalized.strip("-")
    return normalized or "agent-session"


def classify_file(path: Path) -> str:
    lower_name = path.name.lower()
    if "apa source" in lower_name or "bibliograph" in lower_name:
        return "bibliography"
    if "chat" in lower_name or "transcript" in lower_name:
        return "chat"
    if path.suffix.lower() in {".csv", ".xlsx"}:
        return "data_export"
    if path.suffix.lower() in {".docx", ".pdf", ".txt", ".md", ".html"}:
        return "artifact"
    return "other"


class ElicitHTMLCitationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lines: list[str] = []
        self.inline_citations: list[str] = []
        self._current_parts: list[str] = []
        self._current_tag: str | None = None
        self._in_citation_button = False
        self._in_list_item = False
        self._heading_level: int | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"p", "li", "h1", "h2", "h3"}:
            self._current_parts = []
            self._current_tag = tag
            self._in_list_item = tag == "li"
            self._heading_level = int(tag[1]) if tag.startswith("h") else None
        elif tag == "button" and attrs_dict.get("data-citation-anchor") == "true":
            self._in_citation_button = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "button":
            self._in_citation_button = False
            return

        if tag == self._current_tag:
            text = html.unescape("".join(self._current_parts))
            text = re.sub(r"\s+", " ", text).strip()
            if text:
                if self._heading_level:
                    prefix = "#" * self._heading_level
                    self.lines.append(f"{prefix} {text}")
                elif self._in_list_item:
                    self.lines.append(f"- {text}")
                else:
                    self.lines.append(text)
            self._current_parts = []
            self._current_tag = None
            self._in_list_item = False
            self._heading_level = None

    def handle_data(self, data: str) -> None:
        if not self._current_tag:
            return
        cleaned = data.strip()
        if not cleaned:
            return
        if self._in_citation_button:
            self.inline_citations.append(cleaned)
            self._current_parts.append(f" [{cleaned}]")
        else:
            if self._current_parts and not self._current_parts[-1].endswith((" ", "[")):
                self._current_parts.append(" ")
            self._current_parts.append(cleaned)


def html_to_markdown(path: Path) -> tuple[str, dict[str, Any]]:
    parser = ElicitHTMLCitationParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    lines = [line for line in parser.lines if line.strip()]
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    metadata = {
        "title": title,
        "headings": [line[2:].strip() for line in lines if line.startswith("# ")],
        "inlineCitations": list(dict.fromkeys(parser.inline_citations)),
    }
    return "\n\n".join(lines).strip() + "\n", metadata


def docx_to_markdown(path: Path) -> tuple[str, dict[str, Any]]:
    with zipfile.ZipFile(path) as archive:
        xml_bytes = archive.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    body = root.find("w:body", WORD_NS)
    if body is None:
        raise IngestError(f"Missing document body in {path}")

    lines: list[str] = []
    title = ""
    headings: list[str] = []
    section_counts: dict[str, int] = {}

    for element in body:
        tag = element.tag.rsplit("}", 1)[-1]
        if tag == "p":
            style_elem = element.find("w:pPr/w:pStyle", WORD_NS)
            style = style_elem.get(f"{{{WORD_NS['w']}}}val", "") if style_elem is not None else ""
            text = "".join(t.text or "" for t in element.findall(".//w:t", WORD_NS)).strip()
            if not text:
                continue

            if style == "Heading1":
                if not title:
                    title = text
                headings.append(text)
                lines.append(f"# {text}")
            elif style == "Heading2":
                headings.append(text)
                section_counts[text] = section_counts.get(text, 0) + 1
                lines.append(f"## {text}")
            elif style == "Heading3":
                headings.append(text)
                section_counts[text] = section_counts.get(text, 0) + 1
                lines.append(f"### {text}")
            else:
                num_pr = element.find("w:pPr/w:numPr", WORD_NS)
                prefix = "- " if num_pr is not None else ""
                lines.append(f"{prefix}{text}")
        elif tag == "tbl":
            rows = []
            for row in element.findall("w:tr", WORD_NS):
                cells = []
                for cell in row.findall("w:tc", WORD_NS):
                    cell_text = " ".join(
                        "".join(t.text or "" for t in para.findall(".//w:t", WORD_NS)).strip()
                        for para in cell.findall("w:p", WORD_NS)
                    ).strip()
                    cells.append(cell_text)
                if any(cells):
                    rows.append(cells)

            if rows:
                header = rows[0]
                lines.append("| " + " | ".join(header) + " |")
                lines.append("| " + " | ".join("---" for _ in header) + " |")
                for row in rows[1:]:
                    padded = row + [""] * (len(header) - len(row))
                    lines.append("| " + " | ".join(padded[: len(header)]) + " |")

    metadata = {
        "title": title,
        "headings": headings,
        "sectionCounts": section_counts,
    }
    return "\n\n".join(lines).strip() + "\n", metadata


def pdf_to_text(path: Path) -> str | None:
    try:
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return result.stdout


def plain_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def infer_title(texts: list[tuple[Path, str]]) -> str | None:
    for path, text in texts:
        if path.suffix.lower() == ".docx":
            first_heading = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), None)
            if first_heading:
                return first_heading
        first_line = next((line.strip() for line in text.splitlines() if line.strip()), None)
        if first_line:
            return first_line[:180]
    return None


def extract_bibliography_blocks(text: str) -> list[str]:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
    entries = []
    for block in blocks:
        if "doi.org/" in block.lower() or re.search(r"\(\d{4}\)|\(n\.d\.\)", block):
            entries.append(block)
    return entries


def extract_markdown_footnotes(text: str) -> tuple[list[str], list[str]]:
    inline_markers = re.findall(r"\[\^([^\]]+)\]", text)
    footnote_lines = re.findall(r"^\[\^([^\]]+)\]:\s*(.+)$", text, flags=re.MULTILINE)

    citations = []
    bibliography_entries = []
    for marker, content in footnote_lines:
        entry = f"[^{marker}]: {content.strip()}"
        citations.append(entry)
        bibliography_entries.append(content.strip())

    deduped_markers = list(dict.fromkeys(inline_markers))
    deduped_citations = list(dict.fromkeys(citations))
    deduped_bibliography = list(dict.fromkeys(bibliography_entries))
    return deduped_markers + deduped_citations, deduped_bibliography


def detect_chat(text: str) -> dict[str, Any]:
    speaker_pattern = re.compile(r"^(User|Assistant|Researcher|System|You|Elicit)\s*:", re.IGNORECASE)
    speaker_lines = [line for line in text.splitlines() if speaker_pattern.match(line.strip())]
    speakers = sorted({line.split(":", 1)[0].strip() for line in speaker_lines})
    return {
        "detected": len(speaker_lines) >= 2 and len(speakers) >= 2,
        "speakerCount": len(speakers),
        "speakers": speakers,
        "lineCount": len(speaker_lines),
    }


def csv_to_markdown(path: Path, max_rows: int = 25) -> tuple[str, dict[str, Any]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.reader(handle)
        rows = list(reader)

    if not rows:
        return "", {"rowCount": 0, "columnCount": 0}

    header = rows[0]
    body = rows[1 : 1 + max_rows]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in body:
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(padded[: len(header)]) + " |")

    metadata = {
        "rowCount": max(0, len(rows) - 1),
        "columnCount": len(header),
        "truncated": len(rows) - 1 > max_rows,
    }
    return "\n".join(lines) + "\n", metadata


def extract_text_from_path(path: Path) -> tuple[str | None, str, dict[str, Any]]:
    suffix = path.suffix.lower()
    metadata: dict[str, Any] = {}
    if suffix == ".docx":
        text, metadata = docx_to_markdown(path)
        return text, ".md", metadata
    if suffix == ".html":
        text, metadata = html_to_markdown(path)
        return text, ".md", metadata
    if suffix == ".pdf":
        text = pdf_to_text(path)
        return text, ".txt", metadata
    if suffix in {".txt", ".md"}:
        return plain_text(path), ".md" if suffix == ".md" else ".txt", metadata
    if suffix == ".csv":
        text, metadata = csv_to_markdown(path)
        return text, ".md", metadata
    return None, ".txt", metadata


def read_session_title_file(path: Path) -> str:
    lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    if not lines:
        return path.stem
    first = lines[0].lstrip("# ").strip()
    if first.lower() == "session title" and len(lines) > 1:
        return lines[1].lstrip("# ").strip()
    return first


def write_manifest(destination: Path, manifest: dict[str, Any]) -> None:
    (destination / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_session_index(destination: Path, manifest: dict[str, Any]) -> None:
    lines = [
        f"# {manifest['title']}",
        "",
        f"- Chapter: `{manifest['chapter']}`",
        f"- Section: `{manifest['section']}`",
        f"- Session slug: `{manifest['slug']}`",
        f"- Chat detected: `{manifest['chat']['detected']}`",
        f"- Bibliography entries: `{manifest['bibliographyEntryCount']}`",
        "",
        "## Raw Files",
        "",
    ]
    for item in manifest["files"]:
        item_path = item.get("rawPath") or item.get("relativePath") or item.get("sourcePath", "")
        lines.append(f"- `{item_path}` ({item['kind']})")

    lines.extend(["", "## Extracted Text Files", ""])
    for item in manifest["files"]:
        if item.get("extractedPath"):
            lines.append(f"- `{item['extractedPath']}`")

    if manifest["bibliographyEntryCount"]:
        lines.extend(["", "## Bibliography", "", f"- `bibliography_apa.txt` with {manifest['bibliographyEntryCount']} entries"])

    if manifest["docxHeadings"]:
        lines.extend(["", "## Detected Headings", ""])
        for heading in manifest["docxHeadings"]:
            lines.append(f"- {heading}")

    (destination / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def command_ingest(args: argparse.Namespace) -> int:
    input_paths = [Path(p).resolve() for p in args.inputs]
    for path in input_paths:
        if not path.exists():
            raise IngestError(f"Input file does not exist: {path}")

    output_root = Path(args.output_root)
    raw_texts: list[tuple[Path, str]] = []
    file_records: list[dict[str, Any]] = []
    docx_headings: list[str] = []
    bibliography_entries: list[str] = []
    chat_results: list[dict[str, Any]] = []
    inline_citations: list[str] = []

    temp_title = args.title
    for path in input_paths:
        suffix = path.suffix.lower()
        if suffix == ".docx":
            text, metadata = docx_to_markdown(path)
            raw_texts.append((path, text))
            docx_headings.extend(metadata.get("headings", []))
            if not temp_title and metadata.get("title"):
                temp_title = metadata["title"]
        elif suffix == ".html":
            text, metadata = html_to_markdown(path)
            raw_texts.append((path, text))
            docx_headings.extend(metadata.get("headings", []))
            inline_citations.extend(metadata.get("inlineCitations", []))
            if not temp_title and metadata.get("title"):
                temp_title = metadata["title"]
        elif suffix == ".pdf":
            text = pdf_to_text(path)
            if text:
                raw_texts.append((path, text))
        elif suffix in {".txt", ".md"}:
            text = plain_text(path)
            raw_texts.append((path, text))
            md_citations, md_bibliography = extract_markdown_footnotes(text)
            inline_citations.extend(md_citations)
            bibliography_entries.extend(md_bibliography)

    if not temp_title:
        temp_title = infer_title(raw_texts) or args.slug or input_paths[0].stem

    slug = args.slug or slugify(temp_title)
    destination = output_root / args.chapter / args.section / slug
    raw_dir = destination / "raw"
    extracted_dir = destination / "extracted"
    raw_dir.mkdir(parents=True, exist_ok=True)
    extracted_dir.mkdir(parents=True, exist_ok=True)

    text_lookup = {path: text for path, text in raw_texts}
    for path in input_paths:
        kind = classify_file(path)
        raw_target = raw_dir / path.name
        shutil.copy2(path, raw_target)
        record = {
            "sourcePath": str(path),
            "rawPath": str(raw_target.relative_to(destination)),
            "kind": kind,
        }

        text = text_lookup.get(path)
        if text:
            extension = ".md" if path.suffix.lower() == ".docx" else ".txt"
            extracted_target = extracted_dir / f"{path.stem}{extension}"
            extracted_target.write_text(text, encoding="utf-8")
            record["extractedPath"] = str(extracted_target.relative_to(destination))
            chat_results.append(detect_chat(text))
            if kind == "bibliography":
                bibliography_entries.extend(extract_bibliography_blocks(text))
        elif kind == "bibliography":
            bibliography_entries.extend(extract_bibliography_blocks(plain_text(path)))

        file_records.append(record)

    if bibliography_entries:
        deduped = list(dict.fromkeys(bibliography_entries))
        (destination / "bibliography_apa.txt").write_text(
            "\n\n".join(deduped) + "\n",
            encoding="utf-8",
        )
    else:
        deduped = []

    deduped_inline_citations = list(dict.fromkeys(inline_citations))
    if deduped_inline_citations:
        (destination / "inline_citations.txt").write_text(
            "\n".join(deduped_inline_citations) + "\n",
            encoding="utf-8",
        )

    overall_chat = {
        "detected": any(item["detected"] for item in chat_results),
        "speakers": sorted({speaker for item in chat_results for speaker in item["speakers"]}),
    }

    manifest = {
        "title": temp_title,
        "chapter": args.chapter,
        "section": args.section,
        "slug": slug,
        "files": file_records,
        "docxHeadings": list(dict.fromkeys(docx_headings)),
        "chat": overall_chat,
        "bibliographyEntryCount": len(deduped),
        "inlineCitationCount": len(deduped_inline_citations),
        "inlineCitations": deduped_inline_citations,
    }
    write_manifest(destination, manifest)
    write_session_index(destination, manifest)
    print(json.dumps({"outputDir": str(destination), "title": temp_title, "slug": slug}, ensure_ascii=False, indent=2))
    return 0


def should_skip_existing(path: Path) -> bool:
    if path.is_dir():
        return path.name == "extracted"
    if path.name in {"manifest.json", "README.md", "bibliography_apa.txt", "inline_citations.txt"}:
        return True
    return False


def command_extract_session(args: argparse.Namespace) -> int:
    session_dir = Path(args.session_dir).resolve()
    if not session_dir.is_dir():
        raise IngestError(f"Session directory does not exist: {session_dir}")

    section = session_dir.parent.name
    chapter = session_dir.parent.parent.name
    slug = session_dir.name

    extracted_dir = session_dir / "extracted"
    extracted_dir.mkdir(exist_ok=True)

    title_file = next(session_dir.glob(f"{section}_{slug}_session_title.md"), None)
    title = read_session_title_file(title_file) if title_file else slug

    file_records: list[dict[str, Any]] = []
    docx_headings: list[str] = []
    bibliography_entries: list[str] = []
    inline_citations: list[str] = []
    chat_results: list[dict[str, Any]] = []
    data_files: list[dict[str, Any]] = []

    for path in sorted(session_dir.iterdir()):
        if should_skip_existing(path):
            continue
        kind = classify_file(path)
        record = {
            "sourcePath": str(path),
            "relativePath": path.name,
            "kind": kind,
        }

        text, out_ext, metadata = extract_text_from_path(path)
        if text:
            extracted_name = f"{path.stem}_extracted{out_ext}"
            extracted_path = extracted_dir / extracted_name
            extracted_path.write_text(text, encoding="utf-8")
            record["extractedPath"] = str(extracted_path.relative_to(session_dir))
            chat_results.append(detect_chat(text))
            docx_headings.extend(metadata.get("headings", []))
            inline_citations.extend(metadata.get("inlineCitations", []))
            if path.suffix.lower() in {".md", ".txt"}:
                md_citations, md_bibliography = extract_markdown_footnotes(text)
                inline_citations.extend(md_citations)
                bibliography_entries.extend(md_bibliography)
            if kind == "bibliography":
                bibliography_entries.extend(extract_bibliography_blocks(text))
            if path.suffix.lower() == ".csv":
                data_files.append(
                    {
                        "file": path.name,
                        "rows": metadata.get("rowCount", 0),
                        "columns": metadata.get("columnCount", 0),
                        "preview": str(extracted_path.relative_to(session_dir)),
                    }
                )
        elif kind == "bibliography":
            bibliography_entries.extend(extract_bibliography_blocks(plain_text(path)))
        elif path.suffix.lower() == ".xlsx":
            data_files.append({"file": path.name, "rows": None, "columns": None, "preview": None})

        file_records.append(record)

    deduped_bibliography = list(dict.fromkeys(entry for entry in bibliography_entries if entry.strip()))
    if deduped_bibliography:
        (session_dir / "bibliography_apa.txt").write_text(
            "\n\n".join(deduped_bibliography) + "\n",
            encoding="utf-8",
        )

    deduped_inline_citations = list(dict.fromkeys(entry for entry in inline_citations if entry.strip()))
    if deduped_inline_citations:
        (session_dir / "inline_citations.txt").write_text(
            "\n".join(deduped_inline_citations) + "\n",
            encoding="utf-8",
        )

    overall_chat = {
        "detected": any(item["detected"] for item in chat_results),
        "speakers": sorted({speaker for item in chat_results for speaker in item["speakers"]}),
    }

    manifest = {
        "title": title,
        "chapter": chapter,
        "section": section,
        "slug": slug,
        "files": file_records,
        "docxHeadings": list(dict.fromkeys(docx_headings)),
        "chat": overall_chat,
        "bibliographyEntryCount": len(deduped_bibliography),
        "inlineCitationCount": len(deduped_inline_citations),
        "inlineCitations": deduped_inline_citations,
        "dataFiles": data_files,
    }
    write_manifest(session_dir, manifest)
    write_session_index(session_dir, manifest)
    print(json.dumps({"sessionDir": str(session_dir), "extractedDir": str(extracted_dir), "title": title}, ensure_ascii=False, indent=2))
    return 0


def command_extract_tree(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not root.is_dir():
        raise IngestError(f"Agent-session root does not exist: {root}")

    session_dirs: list[Path] = []
    for chapter_dir in sorted(root.iterdir()):
        if not chapter_dir.is_dir():
            continue
        for section_dir in sorted(chapter_dir.iterdir()):
            if not section_dir.is_dir():
                continue
            for session_dir in sorted(section_dir.iterdir()):
                if session_dir.is_dir():
                    session_dirs.append(session_dir)

    results = []
    for session_dir in session_dirs:
        ns = argparse.Namespace(session_dir=str(session_dir))
        command_extract_session(ns)
        results.append(str(session_dir))

    print(json.dumps({"processedSessions": results, "count": len(results)}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ingest local Elicit agent-session exports")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest", help="Copy and extract one local agent-session export set")
    ingest.add_argument("inputs", nargs="+", help="Input files to ingest")
    ingest.add_argument("--chapter", required=True, help="Target chapter folder, e.g. capitulo-2")
    ingest.add_argument("--section", required=True, help="Target section folder, e.g. 2.3")
    ingest.add_argument("--title", help="Override session title")
    ingest.add_argument("--slug", help="Override session slug")
    ingest.add_argument(
        "--output-root",
        default="sources/elicit/agent-sessions",
        help="Destination root folder",
    )
    ingest.set_defaults(func=command_ingest)

    extract_session = subparsers.add_parser(
        "extract-session",
        help="Extract readable outputs in place for one existing agent-session folder",
    )
    extract_session.add_argument("session_dir", help="Existing session directory")
    extract_session.set_defaults(func=command_extract_session)

    extract_tree = subparsers.add_parser(
        "extract-tree",
        help="Extract readable outputs in place for every existing agent-session folder under a root",
    )
    extract_tree.add_argument(
        "--root",
        default="sources/elicit/agent-sessions",
        help="Agent-session root directory",
    )
    extract_tree.set_defaults(func=command_extract_tree)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except IngestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
