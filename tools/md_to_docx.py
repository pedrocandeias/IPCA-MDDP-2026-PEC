#!/usr/bin/env python3
"""Export a local Markdown file to a simple DOCX package.

The exporter is dependency-free and targets the Markdown patterns used in this
workspace: headings, paragraphs, bullet lists, block quotes, fenced code
blocks, horizontal rules, and pipe tables.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import datetime as dt
import re
import struct
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
    number: int | None = None


@dataclass
class TableBlock:
    rows: list[list[str]]


@dataclass
class ImageBlock:
    alt_text: str
    data: bytes
    extension: str
    width_px: int
    height_px: int


Block = ParagraphBlock | TableBlock | ImageBlock


def xml_text(value: str) -> str:
    return escape(value, quote=False)


def slugify_filename(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    slug = slug.strip("-")
    return slug or "documento"


def normalize_lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def extract_reference_definitions(text: str) -> tuple[str, dict[str, str]]:
    references: dict[str, str] = {}
    kept_lines: list[str] = []
    pattern = re.compile(r"^\[([^\]]+)\]:\s*(.+?)\s*$")

    for line in normalize_lines(text):
        match = pattern.match(line.strip())
        if not match:
            kept_lines.append(line)
            continue
        references[match.group(1).strip().lower()] = match.group(2).strip().strip("<>")
    return "\n".join(kept_lines), references


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


def is_escaped_horizontal_rule(line: str) -> bool:
    normalized = re.sub(r"\s+", "", line)
    return bool(normalized) and re.fullmatch(r"(\\_){8,}", normalized) is not None


def load_data_uri(uri: str) -> tuple[bytes, str]:
    match = re.match(r"^data:image/([a-zA-Z0-9.+-]+);base64,(.+)$", uri, flags=re.DOTALL)
    if not match:
        raise ValueError("Unsupported data URI")
    subtype = match.group(1).lower()
    extension = "jpg" if subtype == "jpeg" else subtype
    try:
        data = base64.b64decode(match.group(2), validate=True)
    except binascii.Error as exc:
        raise ValueError("Invalid base64 image payload") from exc
    return data, extension


def load_image_resource(source: str, base_dir: Path) -> tuple[bytes, str]:
    if source.startswith("data:image/"):
        return load_data_uri(source)

    image_path = (base_dir / source).resolve()
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    extension = image_path.suffix.lower().lstrip(".")
    if extension == "jpeg":
        extension = "jpg"
    if extension not in {"png", "jpg", "gif"}:
        raise ValueError(f"Unsupported image type: {image_path.suffix}")
    return image_path.read_bytes(), extension


def png_dimensions(data: bytes) -> tuple[int, int] | None:
    if data[:8] != b"\x89PNG\r\n\x1a\n" or len(data) < 24:
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def gif_dimensions(data: bytes) -> tuple[int, int] | None:
    if data[:6] not in {b"GIF87a", b"GIF89a"} or len(data) < 10:
        return None
    width, height = struct.unpack("<HH", data[6:10])
    return width, height


def jpeg_dimensions(data: bytes) -> tuple[int, int] | None:
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        return None
    offset = 2
    while offset + 9 < len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        marker = data[offset + 1]
        offset += 2
        if marker in {0xD8, 0xD9}:
            continue
        if offset + 2 > len(data):
            return None
        segment_length = struct.unpack(">H", data[offset:offset + 2])[0]
        if segment_length < 2 or offset + segment_length > len(data):
            return None
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            if offset + 7 > len(data):
                return None
            height, width = struct.unpack(">HH", data[offset + 3:offset + 7])
            return width, height
        offset += segment_length
    return None


def image_dimensions(data: bytes, extension: str) -> tuple[int, int]:
    dimensions = None
    if extension == "png":
        dimensions = png_dimensions(data)
    elif extension == "jpg":
        dimensions = jpeg_dimensions(data)
    elif extension == "gif":
        dimensions = gif_dimensions(data)
    return dimensions or (800, 600)


def image_block_from_source(source: str, alt_text: str, base_dir: Path) -> ImageBlock:
    data, extension = load_image_resource(source, base_dir)
    width_px, height_px = image_dimensions(data, extension)
    return ImageBlock(alt_text=alt_text, data=data, extension=extension, width_px=width_px, height_px=height_px)


def extract_inline_images(text: str, references: dict[str, str], base_dir: Path) -> tuple[str, list[ImageBlock]]:
    images: list[ImageBlock] = []

    def replace_inline(match: re.Match[str]) -> str:
        alt_text = match.group(1).strip()
        source = match.group(2).strip().strip("<>")
        try:
            images.append(image_block_from_source(source, alt_text, base_dir))
        except (FileNotFoundError, ValueError):
            return match.group(0)
        return ""

    def replace_reference(match: re.Match[str]) -> str:
        alt_text = match.group(1).strip()
        ref_name = match.group(2).strip().lower()
        source = references.get(ref_name)
        if not source:
            return match.group(0)
        try:
            images.append(image_block_from_source(source, alt_text or ref_name, base_dir))
        except (FileNotFoundError, ValueError):
            return match.group(0)
        return ""

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_inline, text)
    text = re.sub(r"!\[([^\]]*)\]\[([^\]]+)\]", replace_reference, text)
    return text.strip(), images


def parse_markdown(text: str, base_dir: Path) -> list[Block]:
    text, references = extract_reference_definitions(text)
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
            joined, images = extract_inline_images(joined, references, base_dir)
            if joined:
                blocks.append(ParagraphBlock(joined))
            blocks.extend(images)
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
            heading_text, images = extract_inline_images(heading.group(2).strip(), references, base_dir)
            if heading_text:
                blocks.append(ParagraphBlock(heading_text, style=f"Heading{level}"))
            blocks.extend(images)
            i += 1
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped) or is_escaped_horizontal_rule(stripped):
            flush_paragraph()
            flush_quote()
            blocks.append(ParagraphBlock("", style="HorizontalRule"))
            i += 1
            continue

        quote = re.match(r"^>\s?(.*)$", stripped)
        if quote:
            flush_paragraph()
            quote_text, images = extract_inline_images(quote.group(1), references, base_dir)
            if quote_text:
                quote_lines.append(quote_text)
            blocks.extend(images)
            i += 1
            continue
        flush_quote()

        bullet = re.match(r"^[-*+]\s+(.*)$", stripped)
        if bullet:
            flush_paragraph()
            bullet_text, images = extract_inline_images(bullet.group(1).strip(), references, base_dir)
            if bullet_text:
                blocks.append(ParagraphBlock(bullet_text, style="ListBullet"))
            blocks.extend(images)
            i += 1
            continue

        ordered = re.match(r"^(\d+)[.)]\s+(.*)$", stripped)
        if ordered:
            flush_paragraph()
            ordered_text, images = extract_inline_images(ordered.group(2).strip(), references, base_dir)
            if ordered_text:
                blocks.append(ParagraphBlock(ordered_text, style="ListNumber", number=int(ordered.group(1))))
            blocks.extend(images)
            i += 1
            continue

        line_text, images = extract_inline_images(line, references, base_dir)
        if line_text:
            paragraph_lines.append(line_text)
        if images:
            flush_paragraph()
            blocks.extend(images)
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
    if block.style == "ListBullet":
        text = f"- {block.text}"
    elif block.style == "ListNumber":
        prefix = block.number if block.number is not None else 1
        text = f"{prefix}. {block.text}"
    else:
        text = block.text
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


def image_xml(block: ImageBlock, rel_id: str, image_id: int) -> str:
    emu_per_px = 9525
    max_width_px = 600
    width_px = block.width_px
    height_px = block.height_px
    if width_px > max_width_px:
        height_px = max(1, int(height_px * max_width_px / width_px))
        width_px = max_width_px
    width_emu = width_px * emu_per_px
    height_emu = height_px * emu_per_px
    name = xml_text(block.alt_text or f"Image {image_id}")
    return (
        "<w:p><w:r><w:drawing>"
        "<wp:inline xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "distT=\"0\" distB=\"0\" distL=\"0\" distR=\"0\">"
        f"<wp:extent cx=\"{width_emu}\" cy=\"{height_emu}\"/>"
        f"<wp:docPr id=\"{image_id}\" name=\"{name}\" descr=\"{name}\"/>"
        "<wp:cNvGraphicFramePr>"
        "<a:graphicFrameLocks xmlns:a=\"http://schemas.openxmlformats.org/drawingml/2006/main\" noChangeAspect=\"1\"/>"
        "</wp:cNvGraphicFramePr>"
        "<a:graphic xmlns:a=\"http://schemas.openxmlformats.org/drawingml/2006/main\">"
        "<a:graphicData uri=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        "<pic:pic xmlns:pic=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        "<pic:nvPicPr>"
        f"<pic:cNvPr id=\"{image_id}\" name=\"{name}\" descr=\"{name}\"/>"
        "<pic:cNvPicPr/>"
        "</pic:nvPicPr>"
        "<pic:blipFill>"
        f"<a:blip r:embed=\"{rel_id}\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\"/>"
        "<a:stretch><a:fillRect/></a:stretch>"
        "</pic:blipFill>"
        "<pic:spPr>"
        "<a:xfrm><a:off x=\"0\" y=\"0\"/>"
        f"<a:ext cx=\"{width_emu}\" cy=\"{height_emu}\"/></a:xfrm>"
        "<a:prstGeom prst=\"rect\"><a:avLst/></a:prstGeom>"
        "</pic:spPr>"
        "</pic:pic>"
        "</a:graphicData>"
        "</a:graphic>"
        "</wp:inline>"
        "</w:drawing></w:r></w:p>"
    )


def document_xml(blocks: list[Block]) -> str:
    body_parts: list[str] = []
    image_index = 0
    for block in blocks:
        if isinstance(block, ParagraphBlock):
            body_parts.append(paragraph_xml(block))
        elif isinstance(block, TableBlock):
            body_parts.append(table_xml(block))
        else:
            image_index += 1
            body_parts.append(image_xml(block, rel_id=f"rId{image_index + 1}", image_id=image_index))
    body_parts.append(
        "<w:sectPr>"
        "<w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" "
        "w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>"
        "</w:sectPr>"
    )
    return (
        XML_HEADER
        + "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        + "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        + "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        + "xmlns:a=\"http://schemas.openxmlformats.org/drawingml/2006/main\" "
        + "xmlns:pic=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        + f"<w:body>{''.join(body_parts)}</w:body></w:document>"
    )


def content_types_xml(blocks: list[Block]) -> str:
    image_defaults: list[str] = []
    seen_extensions = {block.extension for block in blocks if isinstance(block, ImageBlock)}
    content_map = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "gif": "image/gif",
    }
    for extension in sorted(seen_extensions):
        content_type = content_map.get(extension)
        if content_type:
            image_defaults.append(f"<Default Extension=\"{extension}\" ContentType=\"{content_type}\"/>")
    return (
        XML_HEADER
        + "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
        + "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
        + "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
        + "".join(image_defaults)
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


def document_rels_xml(blocks: list[Block]) -> str:
    relationships = [
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" "
        "Target=\"styles.xml\"/>"
    ]
    image_index = 0
    for block in blocks:
        if not isinstance(block, ImageBlock):
            continue
        image_index += 1
        relationships.append(
            f"<Relationship Id=\"rId{image_index + 1}\" "
            "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/image\" "
            f"Target=\"media/image{image_index}.{block.extension}\"/>"
        )
    return (
        XML_HEADER
        + "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        + "".join(relationships)
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
        + "<w:style w:type=\"paragraph\" w:styleId=\"ListNumber\"><w:name w:val=\"List Number\"/>"
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


def resolve_output_path(input_path: Path, output: Path | None, output_dir: Path | None) -> Path:
    if output and output_dir:
        raise SystemExit("Use either --output or --output-dir, not both.")
    if output:
        return output.expanduser().resolve()
    return build_output_path(input_path, output_dir.expanduser().resolve() if output_dir else None)


def write_docx(input_path: Path, output_path: Path) -> None:
    markdown = input_path.read_text(encoding="utf-8", errors="replace")
    blocks = parse_markdown(markdown, input_path.parent)
    title = infer_title(input_path, blocks)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml(blocks))
        archive.writestr("_rels/.rels", root_rels_xml())
        archive.writestr("word/document.xml", document_xml(blocks))
        archive.writestr("word/_rels/document.xml.rels", document_rels_xml(blocks))
        archive.writestr("word/styles.xml", styles_xml())
        archive.writestr("docProps/core.xml", core_xml(title))
        archive.writestr("docProps/app.xml", app_xml())
        image_index = 0
        for block in blocks:
            if not isinstance(block, ImageBlock):
                continue
            image_index += 1
            archive.writestr(f"word/media/image{image_index}.{block.extension}", block.data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a Markdown file to DOCX without external dependencies.")
    parser.add_argument("input", type=Path, help="Path to the input Markdown file.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Explicit output file path, including filename.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for the generated DOCX copy. Defaults to the repository docs/ directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.expanduser().resolve()
    output_path = resolve_output_path(input_path, args.output, args.output_dir)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if input_path.suffix.lower() not in {".md", ".markdown", ".txt"}:
        raise SystemExit(f"Input file must be Markdown-like (.md, .markdown, .txt): {input_path}")

    write_docx(input_path, output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
