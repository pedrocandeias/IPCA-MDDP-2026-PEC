#!/usr/bin/env python3
"""Export a local DOCX file to a simple Markdown copy."""

from __future__ import annotations

import argparse
import datetime as dt
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

WORD_NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
}
PACKAGE_REL_NS = {"rel": "http://schemas.openxmlformats.org/package/2006/relationships"}
R_ID = f"{{{WORD_NS['r']}}}id"
R_EMBED = f"{{{WORD_NS['r']}}}embed"
R_LINK = f"{{{WORD_NS['r']}}}link"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs"


class DocxConversionError(RuntimeError):
    pass


def load_relationships(archive: zipfile.ZipFile) -> dict[str, dict[str, str]]:
    try:
        rels_xml = archive.read("word/_rels/document.xml.rels")
    except KeyError:
        return {}

    root = ET.fromstring(rels_xml)
    relationships: dict[str, dict[str, str]] = {}
    for rel in root.findall("rel:Relationship", PACKAGE_REL_NS):
        rel_id = rel.get("Id")
        if not rel_id:
            continue
        relationships[rel_id] = {
            "target": rel.get("Target", ""),
            "type": rel.get("Type", ""),
            "mode": rel.get("TargetMode", ""),
        }
    return relationships


def slugify_filename(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    slug = slug.strip("-")
    return slug or "documento"


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


def relationship_markdown_target(rel: dict[str, str]) -> str:
    target = rel.get("target", "")
    if rel.get("mode") == "External":
        return target
    return target.lstrip("/")


def extract_paragraph_text(element: ET.Element, relationships: dict[str, dict[str, str]]) -> str:
    parts: list[str] = []

    def walk(node: ET.Element) -> None:
        tag = node.tag.rsplit("}", 1)[-1]
        if tag == "t":
            parts.append(node.text or "")
            return
        if tag in {"br", "cr"}:
            parts.append("\n")
            return
        if tag == "tab":
            parts.append("\t")
            return
        if tag == "hyperlink":
            link_parts: list[str] = []
            old_parts = parts[:]
            parts.clear()
            for child in node:
                walk(child)
            link_parts.extend(parts)
            parts.clear()
            parts.extend(old_parts)
            link_text = "".join(link_parts)
            rel_id = node.get(R_ID)
            rel = relationships.get(rel_id or "")
            if link_text and rel:
                parts.append(f"[{link_text}]({relationship_markdown_target(rel)})")
            else:
                parts.append(link_text)
            return
        for child in node:
            walk(child)

    for child in element:
        walk(child)

    text = "".join(parts)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def docx_archive_path(target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join("word", target))


def iter_drawing_rel_ids(element: ET.Element) -> list[str]:
    rel_ids: list[str] = []
    for blip in element.findall(".//a:blip", WORD_NS):
        rel_id = blip.get(R_EMBED) or blip.get(R_LINK)
        if rel_id:
            rel_ids.append(rel_id)
    return rel_ids


def write_embedded_image(
    archive: zipfile.ZipFile,
    relationships: dict[str, dict[str, str]],
    rel_id: str,
    media_dir: Path,
    output_dir: Path,
    image_index: int,
) -> str | None:
    rel = relationships.get(rel_id)
    if not rel or rel.get("mode") == "External":
        return None

    target = rel.get("target", "")
    archive_path = docx_archive_path(target)
    try:
        data = archive.read(archive_path)
    except KeyError:
        return None

    media_dir.mkdir(parents=True, exist_ok=True)
    suffix = Path(target).suffix or ".bin"
    filename = f"image{image_index:02d}{suffix.lower()}"
    output_path = media_dir / filename
    output_path.write_bytes(data)
    relative = output_path.relative_to(output_dir).as_posix()
    return relative


def paragraph_prefix(element: ET.Element, style: str) -> str:
    if style == "ListBullet":
        return "- "
    if style == "ListNumber":
        return ""
    num_pr = element.find("w:pPr/w:numPr", WORD_NS)
    if num_pr is not None:
        return "- "
    return ""


def docx_to_markdown(path: Path, output_path: Path | None = None) -> str:
    with zipfile.ZipFile(path) as archive:
        try:
            xml_bytes = archive.read("word/document.xml")
        except KeyError as exc:
            raise DocxConversionError(f"Missing word/document.xml in {path}") from exc
        relationships = load_relationships(archive)

        root = ET.fromstring(xml_bytes)
        body = root.find("w:body", WORD_NS)
        if body is None:
            raise DocxConversionError(f"Missing document body in {path}")

        output_dir = output_path.parent if output_path else DEFAULT_OUTPUT_DIR
        media_dir = output_path.with_suffix("").parent / f"{output_path.stem}_media" if output_path else None
        image_index = 0
        lines: list[str] = []
        for element in body:
            tag = element.tag.rsplit("}", 1)[-1]
            if tag == "p":
                if media_dir is not None:
                    for rel_id in iter_drawing_rel_ids(element):
                        image_index += 1
                        image_ref = write_embedded_image(
                            archive,
                            relationships,
                            rel_id,
                            media_dir,
                            output_dir,
                            image_index,
                        )
                        if image_ref:
                            lines.append(f"![]({image_ref})")

                style_elem = element.find("w:pPr/w:pStyle", WORD_NS)
                style = style_elem.get(f"{{{WORD_NS['w']}}}val", "") if style_elem is not None else ""
                text = extract_paragraph_text(element, relationships)

                if style == "HorizontalRule":
                    lines.append("---")
                    continue
                if not text:
                    continue
                if style == "Heading1":
                    lines.append(f"# {text}")
                elif style == "Heading2":
                    lines.append(f"## {text}")
                elif style == "Heading3":
                    lines.append(f"### {text}")
                elif style == "Quote":
                    quote_lines = [f"> {line}" if line else ">" for line in text.splitlines()]
                    lines.append("\n".join(quote_lines))
                elif style == "CodeBlock":
                    lines.append(f"```\n{text}\n```")
                else:
                    lines.append(f"{paragraph_prefix(element, style)}{text}")
            elif tag == "tbl":
                rows: list[list[str]] = []
                for row in element.findall("w:tr", WORD_NS):
                    cells: list[str] = []
                    for cell in row.findall("w:tc", WORD_NS):
                        cell_paragraphs: list[str] = []
                        for para in cell.findall("w:p", WORD_NS):
                            cell_text = extract_paragraph_text(para, relationships)
                            if cell_text:
                                cell_paragraphs.append(cell_text.replace("\n", "<br>"))
                        cells.append(" ".join(cell_paragraphs).strip())
                    if any(cells):
                        rows.append(cells)

                if rows:
                    width = max(len(row) for row in rows)
                    padded = [row + [""] * (width - len(row)) for row in rows]
                    header = padded[0]
                    lines.append("| " + " | ".join(header) + " |")
                    lines.append("| " + " | ".join("---" for _ in header) + " |")
                    for row in padded[1:]:
                        lines.append("| " + " | ".join(row) + " |")

    return "\n\n".join(lines).strip() + "\n"


def write_markdown(input_path: Path, output_path: Path) -> None:
    markdown = docx_to_markdown(input_path, output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a DOCX file to Markdown without external dependencies.")
    parser.add_argument("input", type=Path, help="Path to the input DOCX file.")
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
    if input_path.suffix.lower() != ".docx":
        raise SystemExit(f"Input file must be a .docx document: {input_path}")

    write_markdown(input_path, output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
