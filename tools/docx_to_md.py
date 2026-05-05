#!/usr/bin/env python3
"""Export a local DOCX file to a simple Markdown copy."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs"


class DocxConversionError(RuntimeError):
    pass


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


def extract_paragraph_text(element: ET.Element) -> str:
    parts: list[str] = []
    for child in element.iter():
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "t":
            parts.append(child.text or "")
        elif tag in {"br", "cr"}:
            parts.append("\n")
        elif tag == "tab":
            parts.append("\t")
    text = "".join(parts)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def paragraph_prefix(element: ET.Element, style: str) -> str:
    if style == "ListBullet":
        return "- "
    if style == "ListNumber":
        return ""
    num_pr = element.find("w:pPr/w:numPr", WORD_NS)
    if num_pr is not None:
        return "- "
    return ""


def docx_to_markdown(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        try:
            xml_bytes = archive.read("word/document.xml")
        except KeyError as exc:
            raise DocxConversionError(f"Missing word/document.xml in {path}") from exc

    root = ET.fromstring(xml_bytes)
    body = root.find("w:body", WORD_NS)
    if body is None:
        raise DocxConversionError(f"Missing document body in {path}")

    lines: list[str] = []
    for element in body:
        tag = element.tag.rsplit("}", 1)[-1]
        if tag == "p":
            style_elem = element.find("w:pPr/w:pStyle", WORD_NS)
            style = style_elem.get(f"{{{WORD_NS['w']}}}val", "") if style_elem is not None else ""
            text = extract_paragraph_text(element)

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
                        cell_text = extract_paragraph_text(para)
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
    markdown = docx_to_markdown(input_path)
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
