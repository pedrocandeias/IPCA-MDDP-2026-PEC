#!/usr/bin/env python3
"""Export a local ODT file to a simple Markdown copy without LibreOffice."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from docx_to_md import DEFAULT_OUTPUT_DIR, slugify_filename

ODT_NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "xlink": "http://www.w3.org/1999/xlink",
}


class OdtConversionError(RuntimeError):
    pass


def build_output_path(input_path: Path, output_dir: Path | None) -> Path:
    timestamp = dt.datetime.now().strftime("%H%M-%d%m%Y")
    filename = f"{slugify_filename(input_path.stem)}-{timestamp}.md"
    target_dir = output_dir if output_dir is not None else DEFAULT_OUTPUT_DIR
    return target_dir / filename


def resolve_output_path(input_path: Path, output: Path | None, output_dir: Path | None) -> Path:
    if output and output_dir:
        raise SystemExit("Use either --output or --output-dir, not both.")
    if output:
        return output.expanduser().resolve()
    return build_output_path(input_path, output_dir.expanduser().resolve() if output_dir else None)


def collect_text(element: ET.Element) -> str:
    parts: list[str] = []
    if element.text:
        parts.append(element.text)
    for child in element:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "line-break":
            parts.append("\n")
        elif tag == "tab":
            parts.append("\t")
        elif tag == "s":
            count = int(child.attrib.get(f"{{{ODT_NS['text']}}}c", "1"))
            parts.append(" " * count)
        else:
            parts.append(collect_text(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def normalize_block_text(text: str) -> str:
    lines = [line.strip() for line in text.split("\n")]
    normalized = "\n".join(lines).strip()
    normalized = normalized.replace("\xa0", " ")
    normalized = normalized.replace(" \t", "\t").replace("\t ", "\t")
    return normalized


def normalize_image_markdown(text: str) -> str:
    if not text.startswith("!["):
        return text
    return re.sub(r"\s+", "", text)


def split_caption_text(text: str) -> list[str]:
    normalized = re.sub(r"\.\s*Fonte original", ".\nFonte original", text)
    return [part.strip() for part in normalized.split("\n") if part.strip()]


def split_glued_heading(text: str) -> tuple[str, str] | None:
    direct_splits = (
        ("Tipologias de próteses de membro superior As ", "Tipologias de próteses de membro superior", "As "),
        ("Próteses mecânicas acionadas pelo corpo (body-powered) As ", "Próteses mecânicas acionadas pelo corpo (body-powered)", "As "),
        ("Próteses mioelétricas: As ", "Próteses mioelétricas", "As "),
        ("Próteses mioelétricas As ", "Próteses mioelétricas", "As "),
        ("Sistemas híbridos: ", "Sistemas híbridos", "Combinam "),
    )
    for marker, heading, prefix in direct_splits:
        if text.startswith(marker):
            remainder = text[len(marker):].strip()
            if prefix:
                remainder = f"{prefix}{remainder}"
            return heading, remainder

    patterns = (
        r"^(Tipologias de próteses de membro superior)\s+(As\s+.+)$",
        r"^(Próteses mecânicas acionadas pelo corpo\s+\(\*?body-powered\*?\))\s+(As\s+.+)$",
        r"^(Próteses mioelétricas):?\s+(As\s+.+)$",
        r"^(Sistemas híbridos):\s+(.+)$",
    )
    for pattern in patterns:
        match = re.match(pattern, text)
        if match:
            return match.group(1).strip(), match.group(2).strip()
    return None


def render_paragraph(text: str) -> list[str]:
    if not text:
        return []
    glued_heading = split_glued_heading(text)
    if glued_heading:
        heading, paragraph = glued_heading
        if paragraph and paragraph[0].islower():
            paragraph = paragraph[0].upper() + paragraph[1:]
        return [f"### {heading}", paragraph]
    if text == "--------------------" or re.fullmatch(r"\\{8,}", text):
        return ["---"]
    if re.match(r"^Capítulo\s+\d+\s+—\s+", text):
        return [f"## {text}"]
    if text.startswith("![") and "./figuras/" in text:
        return [normalize_image_markdown(text)]
    if re.match(r"^Figura\s+\d+(?:\.\d+)?\s+—\s+", text):
        return split_caption_text(text)
    return [text]


def heading_level(element: ET.Element) -> int:
    level = element.attrib.get(f"{{{ODT_NS['text']}}}outline-level", "1")
    try:
        return min(max(int(level), 1), 6)
    except ValueError:
        return 1


def image_extension(media_path: str) -> str:
    suffix = Path(media_path).suffix.lower()
    return suffix if suffix else ".bin"


def extract_images(archive: zipfile.ZipFile, image_paths: list[str], output_path: Path) -> dict[str, str]:
    if not image_paths:
        return {}
    asset_dir = output_path.parent / f"{output_path.stem}_assets"
    if asset_dir.exists():
        shutil.rmtree(asset_dir)
    asset_dir.mkdir(parents=True, exist_ok=True)

    mapping: dict[str, str] = {}
    for index, image_path in enumerate(image_paths, start=1):
        data = archive.read(image_path)
        asset_name = f"image{index}{image_extension(image_path)}"
        target = asset_dir / asset_name
        target.write_bytes(data)
        mapping[image_path] = f"./{asset_dir.name}/{asset_name}"
    return mapping


def odt_to_markdown(input_path: Path, output_path: Path) -> str:
    with zipfile.ZipFile(input_path) as archive:
        try:
            xml_bytes = archive.read("content.xml")
        except KeyError as exc:
            raise OdtConversionError(f"Missing content.xml in {input_path}") from exc

        root = ET.fromstring(xml_bytes)
        text_root = root.find("office:body/office:text", ODT_NS)
        if text_root is None:
            raise OdtConversionError(f"Missing office:text body in {input_path}")

        raw_image_paths: list[str] = []
        for frame in text_root.findall(".//draw:frame", ODT_NS):
            image = frame.find("draw:image", ODT_NS)
            if image is None:
                continue
            href = image.attrib.get(f"{{{ODT_NS['xlink']}}}href")
            if href:
                raw_image_paths.append(href)
        image_map = extract_images(archive, raw_image_paths, output_path)

        lines: list[str] = []
        for element in list(text_root):
            tag = element.tag.rsplit("}", 1)[-1]
            if tag == "h":
                text = normalize_block_text(collect_text(element))
                if text:
                    glued_heading = split_glued_heading(text)
                    if glued_heading:
                        heading, paragraph = glued_heading
                        lines.append(f"{'#' * heading_level(element)} {heading}")
                        lines.extend(render_paragraph(paragraph))
                    else:
                        lines.append(f"{'#' * heading_level(element)} {text}")
            elif tag == "p":
                frames = element.findall("draw:frame", ODT_NS)
                if frames:
                    for frame in frames:
                        image = frame.find("draw:image", ODT_NS)
                        if image is None:
                            continue
                        href = image.attrib.get(f"{{{ODT_NS['xlink']}}}href")
                        if href and href in image_map:
                            lines.append(f"![]({image_map[href]})")
                    text = normalize_block_text(collect_text(element))
                    if text:
                        lines.extend(render_paragraph(text))
                else:
                    text = normalize_block_text(collect_text(element))
                    if text:
                        lines.extend(render_paragraph(text))
            elif tag == "list":
                list_style = element.attrib.get(f"{{{ODT_NS['text']}}}style-name", "")
                is_numbered = list_style == "L1N"
                for item_index, item in enumerate(element.findall("text:list-item", ODT_NS), start=1):
                    item_lines: list[str] = []
                    for child in item:
                        child_tag = child.tag.rsplit("}", 1)[-1]
                        if child_tag == "p":
                            child_text = normalize_block_text(collect_text(child))
                            if child_text:
                                item_lines.append(child_text)
                    if item_lines:
                        marker = f"{item_index}. " if is_numbered else "- "
                        lines.append(f"{marker}{' '.join(item_lines)}")
            elif tag == "table":
                rows: list[list[str]] = []
                for row in element.findall("table:table-row", ODT_NS):
                    cells: list[str] = []
                    for cell in row.findall("table:table-cell", ODT_NS):
                        cell_parts: list[str] = []
                        for para in cell.findall("text:p", ODT_NS):
                            cell_text = normalize_block_text(collect_text(para))
                            if cell_text:
                                cell_parts.append(cell_text.replace("\n", "<br>"))
                        cells.append(" ".join(cell_parts).strip())
                    if any(cells):
                        rows.append(cells)
                if rows:
                    width = max(len(row) for row in rows)
                    padded = [row + [""] * (width - len(row)) for row in rows]
                    header = padded[0]
                    table_lines = [
                        "| " + " | ".join(header) + " |",
                        "| " + " | ".join("---" for _ in header) + " |",
                    ]
                    for row in padded[1:]:
                        table_lines.append("| " + " | ".join(row) + " |")
                    lines.append("\n".join(table_lines))

    return "\n\n".join(line for line in lines if line.strip()).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export an ODT file to Markdown without LibreOffice.")
    parser.add_argument("input", type=Path, help="Path to the input ODT file.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Explicit output file path, including filename.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for the generated Markdown copy. Defaults to the repository docs/ directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.expanduser().resolve()
    output_path = resolve_output_path(input_path, args.output, args.output_dir)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")
    if input_path.suffix.lower() != ".odt":
        raise SystemExit(f"Input file must be an .odt document: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown = odt_to_markdown(input_path, output_path)
    output_path.write_text(markdown, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
