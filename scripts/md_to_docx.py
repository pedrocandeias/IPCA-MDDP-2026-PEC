#!/usr/bin/env python3
"""Export a local Markdown file to a simple DOCX package.

The exporter is dependency-free and targets the Markdown patterns used in this
workspace: headings, paragraphs, bullet lists, block quotes, fenced code
blocks, horizontal rules, and pipe tables.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import zipfile
from dataclasses import dataclass
from html import escape
from pathlib import Path

XML_HEADER = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs"


@dataclass
class ParagraphBlock:
    text: str
    style: str = "Normal"


@dataclass
class TableBlock:
    rows: list[list[str]]


Block = ParagraphBlock | TableBlock


def xml_text(value: str) -> str:
    return escape(value, quote=False)


def slugify_filename(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    slug = slug.strip("-")
    return slug or "documento"


def normalize_lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def is_table_delimiter(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False
    parts = [part.strip() for part in stripped.strip("|").split("|")]
    if not parts:
        return False
    return all(re.fullmatch(r":?-{3,}:?", part) for part in parts)


def parse_pipe_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_markdown(text: str) -> list[Block]:
    lines = normalize_lines(text)
    blocks: list[Block] = []
    paragraph_lines: list[str] = []
    code_lines: list[str] = []
    quote_lines: list[str] = []
    in_code = False

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            joined = " ".join(line.strip() for line in paragraph_lines).strip()
            if joined:
                blocks.append(ParagraphBlock(joined))
        paragraph_lines = []

    def flush_code() -> None:
        nonlocal code_lines
        if code_lines:
            blocks.append(ParagraphBlock("\n".join(code_lines).rstrip("\n"), style="CodeBlock"))
        code_lines = []

    def flush_quote() -> None:
        nonlocal quote_lines
        if quote_lines:
            joined = " ".join(line.strip() for line in quote_lines).strip()
            if joined:
                blocks.append(ParagraphBlock(joined, style="Quote"))
        quote_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_quote()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line.rstrip("\n"))
            i += 1
            continue

        if not stripped:
            flush_paragraph()
            flush_quote()
            i += 1
            continue

        if (
            "|" in line
            and i + 1 < len(lines)
            and is_table_delimiter(lines[i + 1])
        ):
            flush_paragraph()
            flush_quote()
            rows = [parse_pipe_row(line)]
            i += 2
            while i < len(lines):
                candidate = lines[i]
                if not candidate.strip() or "|" not in candidate:
                    break
                rows.append(parse_pipe_row(candidate))
                i += 1
            if rows:
                width = max(len(row) for row in rows)
                padded = [row + [""] * (width - len(row)) for row in rows]
                blocks.append(TableBlock(padded))
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            flush_paragraph()
            flush_quote()
            level = min(len(heading.group(1)), 3)
            blocks.append(ParagraphBlock(heading.group(2).strip(), style=f"Heading{level}"))
            i += 1
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            flush_paragraph()
            flush_quote()
            blocks.append(ParagraphBlock("", style="HorizontalRule"))
            i += 1
            continue

        quote = re.match(r"^>\s?(.*)$", stripped)
        if quote:
            flush_paragraph()
            quote_lines.append(quote.group(1))
            i += 1
            continue
        flush_quote()

        bullet = re.match(r"^[-*+]\s+(.*)$", stripped)
        if bullet:
            flush_paragraph()
            blocks.append(ParagraphBlock(bullet.group(1).strip(), style="ListBullet"))
            i += 1
            continue

        paragraph_lines.append(line)
        i += 1

    flush_paragraph()
    flush_quote()
    if in_code:
        flush_code()
    return blocks


def parse_inlines(text: str) -> list[tuple[str, str]]:
    runs: list[tuple[str, str]] = []
    i = 0
    state = "normal"
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        if buffer:
            runs.append((state, "".join(buffer)))
            buffer = []

    while i < len(text):
        if text.startswith("**", i):
            flush()
            state = "bold" if state != "bold" else "normal"
            i += 2
            continue
        if text.startswith("__", i):
            flush()
            state = "bold" if state != "bold" else "normal"
            i += 2
            continue
        if text[i] == "`":
            flush()
            state = "code" if state != "code" else "normal"
            i += 1
            continue
        if text.startswith("[", i):
            match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", text[i:])
            if match:
                buffer.append(f"{match.group(1)} ({match.group(2)})")
                i += len(match.group(0))
                continue
        if text[i] in {"*", "_"}:
            single = text[i]
            if i + 1 < len(text) and text[i + 1] == single:
                buffer.append(single)
                i += 1
            else:
                flush()
                state = "italic" if state != "italic" else "normal"
            i += 1
            continue
        buffer.append(text[i])
        i += 1

    flush()
    return runs or [("normal", text)]


def run_xml(kind: str, text: str) -> str:
    if not text and kind != "normal":
        return ""
    properties = []
    if kind == "bold":
        properties.append("<w:b/>")
    elif kind == "italic":
        properties.append("<w:i/>")
    elif kind == "code":
        properties.extend(["<w:rFonts w:ascii=\"Consolas\" w:hAnsi=\"Consolas\"/>", "<w:sz w:val=\"20\"/>"])

    prop_xml = f"<w:rPr>{''.join(properties)}</w:rPr>" if properties else ""
    segments = text.split("\n")
    if not segments:
        segments = [""]
    pieces: list[str] = []
    for idx, segment in enumerate(segments):
        if idx:
            pieces.append("<w:br/>")
        if segment or idx == 0:
            space = ' xml:space="preserve"' if segment[:1].isspace() or segment[-1:].isspace() else ""
            pieces.append(f"<w:t{space}>{xml_text(segment)}</w:t>")
    return f"<w:r>{prop_xml}{''.join(pieces)}</w:r>"


def paragraph_xml(block: ParagraphBlock) -> str:
    if block.style == "HorizontalRule":
        return (
            "<w:p><w:pPr><w:pBdr><w:bottom w:val=\"single\" w:sz=\"6\" "
            "w:space=\"1\" w:color=\"808080\"/></w:pBdr></w:pPr></w:p>"
        )

    style_xml = ""
    if block.style != "Normal":
        style_xml = f"<w:pStyle w:val=\"{block.style}\"/>"
    text = f"- {block.text}" if block.style == "ListBullet" else block.text
    runs = "".join(run_xml(kind, content) for kind, content in parse_inlines(text))
    if not runs:
        runs = "<w:r><w:t></w:t></w:r>"
    return f"<w:p><w:pPr>{style_xml}</w:pPr>{runs}</w:p>"


def cell_xml(text: str) -> str:
    paragraph = paragraph_xml(ParagraphBlock(text))
    return f"<w:tc><w:tcPr><w:tcW w:w=\"0\" w:type=\"auto\"/></w:tcPr>{paragraph}</w:tc>"


def table_xml(block: TableBlock) -> str:
    rows: list[str] = []
    for row_index, row in enumerate(block.rows):
        cells = "".join(cell_xml(cell) for cell in row)
        tr_pr = "<w:trPr><w:tblHeader/></w:trPr>" if row_index == 0 else ""
        rows.append(f"<w:tr>{tr_pr}{cells}</w:tr>")
    return (
        "<w:tbl>"
        "<w:tblPr><w:tblW w:w=\"0\" w:type=\"auto\"/>"
        "<w:tblBorders>"
        "<w:top w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "<w:left w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "<w:bottom w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "<w:right w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "<w:insideH w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "<w:insideV w:val=\"single\" w:sz=\"4\" w:color=\"808080\"/>"
        "</w:tblBorders></w:tblPr>"
        + "".join(rows)
        + "</w:tbl>"
    )


def document_xml(blocks: list[Block]) -> str:
    body_parts: list[str] = []
    for block in blocks:
        if isinstance(block, ParagraphBlock):
            body_parts.append(paragraph_xml(block))
        else:
            body_parts.append(table_xml(block))
    body_parts.append(
        "<w:sectPr>"
        "<w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" "
        "w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>"
        "</w:sectPr>"
    )
    return (
        XML_HEADER
        + "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        + f"<w:body>{''.join(body_parts)}</w:body></w:document>"
    )


def content_types_xml() -> str:
    return (
        XML_HEADER
        + "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
        + "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
        + "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
        + "<Override PartName=\"/word/document.xml\" "
        + "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>"
        + "<Override PartName=\"/word/styles.xml\" "
        + "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml\"/>"
        + "<Override PartName=\"/docProps/core.xml\" ContentType=\"application/vnd.openxmlformats-package.core-properties+xml\"/>"
        + "<Override PartName=\"/docProps/app.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.extended-properties+xml\"/>"
        + "</Types>"
    )


def root_rels_xml() -> str:
    return (
        XML_HEADER
        + "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        + "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" "
        + "Target=\"word/document.xml\"/>"
        + "<Relationship Id=\"rId2\" Type=\"http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties\" "
        + "Target=\"docProps/core.xml\"/>"
        + "<Relationship Id=\"rId3\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties\" "
        + "Target=\"docProps/app.xml\"/>"
        + "</Relationships>"
    )


def document_rels_xml() -> str:
    return (
        XML_HEADER
        + "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        + "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" "
        + "Target=\"styles.xml\"/>"
        + "</Relationships>"
    )


def styles_xml() -> str:
    return (
        XML_HEADER
        + "<w:styles xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        + "<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii=\"Calibri\" w:hAnsi=\"Calibri\"/>"
        + "<w:sz w:val=\"22\"/></w:rPr></w:rPrDefault></w:docDefaults>"
        + "<w:style w:type=\"paragraph\" w:default=\"1\" w:styleId=\"Normal\"><w:name w:val=\"Normal\"/></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"Heading1\"><w:name w:val=\"heading 1\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:uiPriority w:val=\"9\"/><w:qFormat/>"
        + "<w:rPr><w:b/><w:sz w:val=\"32\"/></w:rPr></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"Heading2\"><w:name w:val=\"heading 2\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:uiPriority w:val=\"9\"/><w:qFormat/>"
        + "<w:rPr><w:b/><w:sz w:val=\"28\"/></w:rPr></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"Heading3\"><w:name w:val=\"heading 3\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:uiPriority w:val=\"9\"/><w:qFormat/>"
        + "<w:rPr><w:b/><w:sz w:val=\"24\"/></w:rPr></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"ListBullet\"><w:name w:val=\"List Bullet\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:pPr><w:ind w:left=\"720\" w:hanging=\"360\"/></w:pPr></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"Quote\"><w:name w:val=\"Quote\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:pPr><w:ind w:left=\"720\" w:right=\"720\"/></w:pPr>"
        + "<w:rPr><w:i/><w:color w:val=\"555555\"/></w:rPr></w:style>"
        + "<w:style w:type=\"paragraph\" w:styleId=\"CodeBlock\"><w:name w:val=\"Code Block\"/>"
        + "<w:basedOn w:val=\"Normal\"/><w:pPr><w:spacing w:before=\"120\" w:after=\"120\"/>"
        + "<w:ind w:left=\"360\" w:right=\"360\"/></w:pPr>"
        + "<w:rPr><w:rFonts w:ascii=\"Consolas\" w:hAnsi=\"Consolas\"/><w:sz w:val=\"20\"/></w:rPr></w:style>"
        + "</w:styles>"
    )


def core_xml(title: str) -> str:
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    safe_title = xml_text(title)
    return (
        XML_HEADER
        + "<cp:coreProperties "
        + "xmlns:cp=\"http://schemas.openxmlformats.org/package/2006/metadata/core-properties\" "
        + "xmlns:dc=\"http://purl.org/dc/elements/1.1/\" "
        + "xmlns:dcterms=\"http://purl.org/dc/terms/\" "
        + "xmlns:dcmitype=\"http://purl.org/dc/dcmitype/\" "
        + "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">"
        + f"<dc:title>{safe_title}</dc:title>"
        + "<dc:creator>Codex Markdown Exporter</dc:creator>"
        + f"<cp:lastModifiedBy>Codex Markdown Exporter</cp:lastModifiedBy>"
        + f"<dcterms:created xsi:type=\"dcterms:W3CDTF\">{timestamp}</dcterms:created>"
        + f"<dcterms:modified xsi:type=\"dcterms:W3CDTF\">{timestamp}</dcterms:modified>"
        + "</cp:coreProperties>"
    )


def app_xml() -> str:
    return (
        XML_HEADER
        + "<Properties xmlns=\"http://schemas.openxmlformats.org/officeDocument/2006/extended-properties\" "
        + "xmlns:vt=\"http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes\">"
        + "<Application>Codex Markdown Exporter</Application>"
        + "</Properties>"
    )


def infer_title(path: Path, blocks: list[Block]) -> str:
    for block in blocks:
        if isinstance(block, ParagraphBlock) and block.style == "Heading1" and block.text.strip():
            return block.text.strip()
    return path.stem


def build_output_path(input_path: Path, output_dir: Path | None) -> Path:
    timestamp = dt.datetime.now().strftime("%H%M-%d%m%Y")
    filename = f"{slugify_filename(input_path.stem)}-{timestamp}.docx"
    target_dir = output_dir if output_dir is not None else DEFAULT_OUTPUT_DIR
    return target_dir / filename


def write_docx(input_path: Path, output_path: Path) -> None:
    markdown = input_path.read_text(encoding="utf-8", errors="replace")
    blocks = parse_markdown(markdown)
    title = infer_title(input_path, blocks)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml())
        archive.writestr("_rels/.rels", root_rels_xml())
        archive.writestr("word/document.xml", document_xml(blocks))
        archive.writestr("word/_rels/document.xml.rels", document_rels_xml())
        archive.writestr("word/styles.xml", styles_xml())
        archive.writestr("docProps/core.xml", core_xml(title))
        archive.writestr("docProps/app.xml", app_xml())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a Markdown file to DOCX without external dependencies.")
    parser.add_argument("input", type=Path, help="Path to the input Markdown file.")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="Output directory for the generated DOCX copy. Defaults to the repository docs/ directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve() if args.output_dir else None
    output_path = build_output_path(input_path, output_dir)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if input_path.suffix.lower() not in {".md", ".markdown", ".txt"}:
        raise SystemExit(f"Input file must be Markdown-like (.md, .markdown, .txt): {input_path}")

    write_docx(input_path, output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
