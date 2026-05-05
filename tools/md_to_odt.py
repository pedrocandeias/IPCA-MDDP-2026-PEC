#!/usr/bin/env python3
"""Export a local Markdown file to a simple ODT package without LibreOffice."""

from __future__ import annotations

import argparse
import datetime as dt
import zipfile
from html import escape
from pathlib import Path

from md_to_docx import DEFAULT_OUTPUT_DIR, ImageBlock, ParagraphBlock, TableBlock, infer_title, parse_markdown, slugify_filename

XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>'


def xml_text(value: str) -> str:
    return escape(value, quote=False)


def build_output_path(input_path: Path, output_dir: Path | None) -> Path:
    timestamp = dt.datetime.now().strftime("%H%M-%d%m%Y")
    filename = f"{slugify_filename(input_path.stem)}-{timestamp}.odt"
    target_dir = output_dir if output_dir is not None else DEFAULT_OUTPUT_DIR
    return target_dir / filename


def resolve_output_path(input_path: Path, output: Path | None, output_dir: Path | None) -> Path:
    if output and output_dir:
        raise SystemExit("Use either --output or --output-dir, not both.")
    if output:
        return output.expanduser().resolve()
    return build_output_path(input_path, output_dir.expanduser().resolve() if output_dir else None)


def odt_paragraph_text(text: str) -> str:
    parts: list[str] = []
    for line_index, line in enumerate(text.split("\n")):
        if line_index:
            parts.append("<text:line-break/>")
        segments = line.split("\t")
        for segment_index, segment in enumerate(segments):
            if segment_index:
                parts.append("<text:tab/>")
            escaped = xml_text(segment)
            if escaped:
                escaped = escaped.replace("  ", " <text:s/>")
            parts.append(escaped)
    return "".join(parts)


def convert_px_to_cm(px: int) -> str:
    cm = max(px * 2.54 / 96.0, 0.5)
    return f"{cm:.2f}cm"


def image_media_path(index: int, extension: str) -> str:
    return f"Pictures/image{index}.{extension}"


def paragraph_xml(block: ParagraphBlock) -> str:
    if block.style == "HorizontalRule":
        return "<text:p text:style-name=\"HorizontalRule\">--------------------</text:p>"

    if block.style in {"Heading1", "Heading2", "Heading3"}:
        level_map = {"Heading1": 1, "Heading2": 2, "Heading3": 3}
        style_map = {
            "Heading1": "Heading_20_1",
            "Heading2": "Heading_20_2",
            "Heading3": "Heading_20_3",
        }
        return (
            f"<text:h text:style-name=\"{style_map[block.style]}\" "
            f"text:outline-level=\"{level_map[block.style]}\">{odt_paragraph_text(block.text)}</text:h>"
        )

    style_map = {
        "Normal": "Standard",
        "Quote": "Quotations",
        "CodeBlock": "Preformatted_20_Text",
    }
    style_name = style_map.get(block.style, "Standard")
    if block.style == "ListBullet":
        text = f"- {block.text}"
    elif block.style == "ListNumber":
        prefix = block.number if block.number is not None else 1
        text = f"{prefix}. {block.text}"
    else:
        text = block.text
    return f"<text:p text:style-name=\"{style_name}\">{odt_paragraph_text(text)}</text:p>"


def table_xml(block: TableBlock) -> str:
    columns = max((len(row) for row in block.rows), default=0)
    column_defs = "".join(
        "<table:table-column table:style-name=\"TableColumn\" table:number-columns-repeated=\"1\"/>"
        for _ in range(columns)
    )
    rows_xml: list[str] = []
    for row in block.rows:
        padded = row + [""] * (columns - len(row))
        cells = "".join(
            f"<table:table-cell office:value-type=\"string\"><text:p>{odt_paragraph_text(cell)}</text:p></table:table-cell>"
            for cell in padded
        )
        rows_xml.append(f"<table:table-row>{cells}</table:table-row>")
    return f"<table:table table:name=\"Tabela\">{column_defs}{''.join(rows_xml)}</table:table>"


def image_xml(block: ImageBlock, index: int) -> str:
    max_width_px = 600
    width_px = block.width_px
    height_px = block.height_px
    if width_px > max_width_px:
        height_px = max(1, int(height_px * max_width_px / width_px))
        width_px = max_width_px
    width = convert_px_to_cm(width_px)
    height = convert_px_to_cm(height_px)
    href = image_media_path(index, block.extension)
    name = xml_text(block.alt_text or f"Image {index}")
    return (
        "<text:p text:style-name=\"Standard\">"
        f"<draw:frame draw:name=\"{name}\" text:anchor-type=\"paragraph\" svg:width=\"{width}\" svg:height=\"{height}\">"
        f"<draw:image xlink:href=\"{href}\" xlink:type=\"simple\" xlink:show=\"embed\" xlink:actuate=\"onLoad\"/>"
        "</draw:frame>"
        "</text:p>"
    )


def content_xml(blocks: list[ParagraphBlock | TableBlock | ImageBlock]) -> str:
    body_parts: list[str] = []
    image_index = 0
    current_list_style: str | None = None
    for block in blocks:
        if isinstance(block, ParagraphBlock) and block.style in {"ListBullet", "ListNumber"}:
            target_list_style = "L1" if block.style == "ListBullet" else "L1N"
            if current_list_style != target_list_style:
                if current_list_style is not None:
                    body_parts.append("</text:list>")
                body_parts.append(f"<text:list text:style-name=\"{target_list_style}\">")
                current_list_style = target_list_style
            body_parts.append(f"<text:list-item>{paragraph_xml(ParagraphBlock(block.text))}</text:list-item>")
            continue
        if current_list_style is not None:
            body_parts.append("</text:list>")
            current_list_style = None
        if isinstance(block, ParagraphBlock):
            body_parts.append(paragraph_xml(block))
        elif isinstance(block, TableBlock):
            body_parts.append(table_xml(block))
        else:
            image_index += 1
            body_parts.append(image_xml(block, image_index))
    if current_list_style is not None:
        body_parts.append("</text:list>")

    return (
        XML_HEADER
        + "<office:document-content "
        + "xmlns:office=\"urn:oasis:names:tc:opendocument:xmlns:office:1.0\" "
        + "xmlns:style=\"urn:oasis:names:tc:opendocument:xmlns:style:1.0\" "
        + "xmlns:text=\"urn:oasis:names:tc:opendocument:xmlns:text:1.0\" "
        + "xmlns:table=\"urn:oasis:names:tc:opendocument:xmlns:table:1.0\" "
        + "xmlns:draw=\"urn:oasis:names:tc:opendocument:xmlns:drawing:1.0\" "
        + "xmlns:fo=\"urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0\" "
        + "xmlns:xlink=\"http://www.w3.org/1999/xlink\" "
        + "xmlns:svg=\"urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0\" "
        + "office:version=\"1.3\">"
        + "<office:scripts/>"
        + "<office:automatic-styles>"
        + "<style:style style:name=\"TableColumn\" style:family=\"table-column\">"
        + "<style:table-column-properties style:column-width=\"3cm\"/>"
        + "</style:style>"
        + "</office:automatic-styles>"
        + "<office:body><office:text>"
        + "".join(body_parts)
        + "</office:text></office:body></office:document-content>"
    )


def styles_xml() -> str:
    return (
        XML_HEADER
        + "<office:document-styles "
        + "xmlns:office=\"urn:oasis:names:tc:opendocument:xmlns:office:1.0\" "
        + "xmlns:style=\"urn:oasis:names:tc:opendocument:xmlns:style:1.0\" "
        + "xmlns:text=\"urn:oasis:names:tc:opendocument:xmlns:text:1.0\" "
        + "xmlns:fo=\"urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0\" "
        + "office:version=\"1.3\">"
        + "<office:styles>"
        + "<style:default-style style:family=\"paragraph\">"
        + "<style:text-properties style:font-name=\"Liberation Serif\" fo:font-size=\"12pt\"/>"
        + "</style:default-style>"
        + "<style:style style:name=\"Standard\" style:family=\"paragraph\" style:class=\"text\"/>"
        + "<style:style style:name=\"Heading_20_1\" style:family=\"paragraph\" style:parent-style-name=\"Standard\">"
        + "<style:text-properties fo:font-size=\"18pt\" fo:font-weight=\"bold\"/>"
        + "</style:style>"
        + "<style:style style:name=\"Heading_20_2\" style:family=\"paragraph\" style:parent-style-name=\"Standard\">"
        + "<style:text-properties fo:font-size=\"16pt\" fo:font-weight=\"bold\"/>"
        + "</style:style>"
        + "<style:style style:name=\"Heading_20_3\" style:family=\"paragraph\" style:parent-style-name=\"Standard\">"
        + "<style:text-properties fo:font-size=\"14pt\" fo:font-weight=\"bold\"/>"
        + "</style:style>"
        + "<style:style style:name=\"Quotations\" style:family=\"paragraph\" style:parent-style-name=\"Standard\">"
        + "<style:paragraph-properties fo:margin-left=\"1cm\" fo:margin-right=\"1cm\"/>"
        + "<style:text-properties fo:font-style=\"italic\" fo:color=\"#555555\"/>"
        + "</style:style>"
        + "<style:style style:name=\"Preformatted_20_Text\" style:family=\"paragraph\" style:parent-style-name=\"Standard\">"
        + "<style:paragraph-properties fo:margin-left=\"0.5cm\" fo:margin-right=\"0.5cm\"/>"
        + "<style:text-properties style:font-name=\"Liberation Mono\" fo:font-size=\"10pt\"/>"
        + "</style:style>"
        + "<style:style style:name=\"HorizontalRule\" style:family=\"paragraph\" style:parent-style-name=\"Standard\"/>"
        + "</office:styles>"
        + "<office:automatic-styles>"
        + "<text:list-style style:name=\"L1\">"
        + "<text:list-level-style-bullet text:level=\"1\" text:bullet-char=\"•\">"
        + "<style:list-level-properties text:list-level-position-and-space-mode=\"label-alignment\">"
        + "<style:list-level-label-alignment text:label-followed-by=\"listtab\" text:list-tab-stop-position=\"1cm\" fo:text-indent=\"-0.5cm\" fo:margin-left=\"1cm\"/>"
        + "</style:list-level-properties>"
        + "</text:list-level-style-bullet>"
        + "</text:list-style>"
        + "<text:list-style style:name=\"L1N\">"
        + "<text:list-level-style-number text:level=\"1\" style:num-format=\"1\">"
        + "<style:list-level-properties text:list-level-position-and-space-mode=\"label-alignment\">"
        + "<style:list-level-label-alignment text:label-followed-by=\"listtab\" text:list-tab-stop-position=\"1cm\" fo:text-indent=\"-0.5cm\" fo:margin-left=\"1cm\"/>"
        + "</style:list-level-properties>"
        + "</text:list-level-style-number>"
        + "</text:list-style>"
        + "</office:automatic-styles>"
        + "</office:document-styles>"
    )


def meta_xml(title: str) -> str:
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return (
        XML_HEADER
        + "<office:document-meta "
        + "xmlns:office=\"urn:oasis:names:tc:opendocument:xmlns:office:1.0\" "
        + "xmlns:meta=\"urn:oasis:names:tc:opendocument:xmlns:meta:1.0\" "
        + "xmlns:dc=\"http://purl.org/dc/elements/1.1/\" "
        + "office:version=\"1.3\">"
        + "<office:meta>"
        + f"<dc:title>{xml_text(title)}</dc:title>"
        + "<meta:initial-creator>Codex Markdown Exporter</meta:initial-creator>"
        + "<meta:generator>Codex Markdown Exporter</meta:generator>"
        + f"<meta:creation-date>{timestamp}</meta:creation-date>"
        + f"<dc:date>{timestamp}</dc:date>"
        + "</office:meta></office:document-meta>"
    )


def manifest_xml(blocks: list[ParagraphBlock | TableBlock | ImageBlock]) -> str:
    entries = [
        '<manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.text"/>',
        '<manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>',
        '<manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>',
        '<manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>',
    ]
    media_types = {"png": "image/png", "jpg": "image/jpeg", "gif": "image/gif"}
    image_index = 0
    for block in blocks:
        if not isinstance(block, ImageBlock):
            continue
        image_index += 1
        href = image_media_path(image_index, block.extension)
        entries.append(
            f'<manifest:file-entry manifest:full-path="{href}" manifest:media-type="{media_types[block.extension]}"/>'
        )
    return (
        XML_HEADER
        + "<manifest:manifest "
        + "xmlns:manifest=\"urn:oasis:names:tc:opendocument:xmlns:manifest:1.0\" "
        + 'manifest:version="1.3">'
        + "".join(entries)
        + "</manifest:manifest>"
    )


def write_odt(input_path: Path, output_path: Path) -> None:
    markdown = input_path.read_text(encoding="utf-8", errors="replace")
    blocks = parse_markdown(markdown, input_path.parent)
    title = infer_title(input_path, blocks)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w") as archive:
        archive.writestr(
            zipfile.ZipInfo("mimetype"),
            "application/vnd.oasis.opendocument.text",
            compress_type=zipfile.ZIP_STORED,
        )
        archive.writestr("content.xml", content_xml(blocks), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("styles.xml", styles_xml(), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("meta.xml", meta_xml(title), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("META-INF/manifest.xml", manifest_xml(blocks), compress_type=zipfile.ZIP_DEFLATED)
        image_index = 0
        for block in blocks:
            if not isinstance(block, ImageBlock):
                continue
            image_index += 1
            archive.writestr(image_media_path(image_index, block.extension), block.data, compress_type=zipfile.ZIP_DEFLATED)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a Markdown file to ODT without LibreOffice.")
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
        help="Output directory for the generated ODT copy. Defaults to the repository docs/ directory.",
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

    write_odt(input_path, output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
