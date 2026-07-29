#!/usr/bin/env python3
"""Aplica itálico a estrangeirismos ingleses no manuscrito 0.4.55.

A revisão abrange o texto académico em português, as listas e os anexos. O
Abstract, a bibliografia, as notas de fonte, os identificadores de código, os
URL e os nomes próprios de aplicações/modelos permanecem inalterados.
"""

from __future__ import annotations

import os
import re
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


ACRONYM_EXPANSIONS = {
    "3DP": "3D Printing",
    "3MF": "3D Manufacturing Format",
    "AMS": "Automatic Material System",
    "ANSUR": "Anthropometric Survey of U.S. Army Personnel",
    "API": "Application Programming Interface",
    "ASTM": "American Society for Testing and Materials",
    "CAD": "Computer-Aided Design",
    "CAM": "Computer-Aided Manufacturing",
    "CSG": "Constructive Solid Geometry",
    "CSV": "Comma-Separated Values",
    "CT": "Computed Tomography",
    "DfAM": "Design for Additive Manufacturing",
    "DINED": "Delft Institute of Ergonomics and Design",
    "DOI": "Digital Object Identifier",
    "EU": "European Union",
    "FDA": "Food and Drug Administration",
    "FDM": "Fused Deposition Modelling",
    "FEA": "Finite Element Analysis",
    "FEM": "Finite Element Method",
    "FFF": "Fused Filament Fabrication",
    "FFD": "Free-Form Deformation",
    "HB": "Hand Breadth",
    "HCD": "Human-Centred Design",
    "HGD": "Hand Grip Diameter",
    "HL": "Hand Length",
    "HTML": "HyperText Markup Language",
    "ICF": "International Classification of Functioning, Disability and Health",
    "IEEE": "Institute of Electrical and Electronics Engineers",
    "ISO": "International Organization for Standardization",
    "JSON": "JavaScript Object Notation",
    "JWT": "JSON Web Token",
    "LL": "Lower Limb",
    "MCP": "Metacarpophalangeal",
    "MDR": "Medical Device Regulation",
    "MPT": "Matching Person and Technology",
    "MRI": "Magnetic Resonance Imaging",
    "PCA": "Principal Component Analysis",
    "PDF": "Portable Document Format",
    "PIP": "Proximal Interphalangeal",
    "PL": "Palm Length",
    "PRISMA": "Preferred Reporting Items for Systematic Reviews and Meta-Analyses",
    "RTD": "Research Through Design",
    "SD": "Standard Deviation",
    "SLA": "Stereolithography",
    "SLS": "Selective Laser Sintering",
    "SSM": "Statistical Shape Modelling",
    "STL": "Stereolithography",
    "TC": "Technical Committee",
    "TRL": "Technology Readiness Level",
    "UCD": "User-Centred Design",
    "UI": "User Interface",
    "UL": "Upper Limb",
    "UX": "User Experience",
    "WASM": "WebAssembly",
    "XAI": "Explainable Artificial Intelligence",
}


PHRASES = [
    "Preferred Reporting Items for Systematic Reviews and Meta-Analyses",
    "International Classification of Functioning, Disability and Health",
    "Seeding, Evolutionary Growth, and Reseeding",
    "Website Accessibility Conformance Evaluation Methodology",
    "Web Content Accessibility Guidelines",
    "Institute of Electrical and Electronics Engineers",
    "International Organization for Standardization",
    "American Society for Testing and Materials",
    "Anthropometric Survey of U.S. Army Personnel",
    "Delft Institute of Ergonomics and Design",
    "Design for Additive Manufacturing",
    "Application Programming Interface",
    "toolkits for user innovation",
    "designerly ways of knowing",
    "Software Shaping Workshop",
    "Magnetic Resonance Imaging",
    "Research Through Design",
    "Human-Centred Design",
    "User-Centred Design",
    "Design for All",
    "mass customization",
    "mass personalization",
    "Thermal hot spots",
    "virtual coaching",
    "serious games",
    "end-user development",
    "file-to-factory",
    "uniform scaling",
    "JSON Web Token",
    "Web Worker",
    "Double Diamond",
    "journey maps",
    "digital twins",
    "living labs",
    "long format",
    "Finger length",
    "LL other",
    "think-aloud",
    "body-powered",
    "open-source",
    "open source",
    "end-to-end",
]


SINGLE_TERMS = [
    "co-designers",
    "stakeholders",
    "sub-datasets",
    "smartphones",
    "datasets",
    "toolkits",
    "scripts",
    "tokens",
    "co-design",
    "meta-design",
    "body-powered",
    "sub-dataset",
    "stakeholder",
    "dataset",
    "toolkit",
    "tailoring",
    "scanning",
    "software",
    "hardware",
    "feedback",
    "workflow",
    "firmware",
    "manifold",
    "gauntlet",
    "inline",
    "proxy",
    "maker",
    "script",
    "online",
    "socket",
    "shape",
    "token",
    "teen",
    "adult",
    "elderly",
    "Methods",
    "Results",
    "string",
    "float",
    "int",
    "design",
    "web",
]


FULL_ENGLISH_CELLS = [
    "man, 28 years old, 82 kg, 180 cm height, Brazil, arm length 70 cm",
    "girl, 10 years old, 32 kg, 138 cm height, Japan, small frame",
    "woman, 65 years old, 68 kg, 160 cm height, Nigeria, arm length 62 cm",
    "man, 50 years old, 95 kg, 175 cm height, Germany, broad hands, arm length 66 cm",
    "teenage boy, 15 years old, 60 kg, 168 cm height, India, slim build, arm length 67 cm",
    "hand anthropometry normative data population study percentiles",
    "hand dimensions measurement ergonomics working population",
    "anthropometric survey finger length breadth caliper",
    "girl, 10 years old, ... Japan",
    "hand, forearm, upperarm, lowerlimb, torso, head",
    "Young adults (age 18-30)",
    "male, female ou combined",
    "mean, stddev, percentile, min, max",
]


PHRASE_PATTERNS = [
    re.compile(rf"(?<![\w-]){re.escape(value)}(?![\w-])", re.IGNORECASE)
    for value in sorted(set(PHRASES) | set(ACRONYM_EXPANSIONS.values()), key=len, reverse=True)
]
TERM_PATTERNS = [
    re.compile(rf"(?<![\w-]){re.escape(value)}(?![\w-])", re.IGNORECASE)
    for value in sorted(SINGLE_TERMS, key=len, reverse=True)
]
FULL_PATTERNS = [re.compile(re.escape(value), re.IGNORECASE) for value in FULL_ENGLISH_CELLS]

SOURCE_PREFIXES = (
    "Adaptado de ",
    "Reproduzido de ",
    "Fonte: ",
    "- World Wide Web Consortium.",
)


def merge_spans(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[list[int]] = []
    for start, end in sorted(spans):
        if start == end:
            continue
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return [(start, end) for start, end in merged]


def foreign_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pattern in PHRASE_PATTERNS + TERM_PATTERNS + FULL_PATTERNS:
        spans.extend(match.span() for match in pattern.finditer(text))
    if text.strip() in {"string", "int", "float"}:
        start = text.index(text.strip())
        spans.append((start, start + len(text.strip())))
    return merge_spans(spans)


def protected_markdown_spans(text: str) -> list[tuple[int, int]]:
    patterns = [
        r"`+[^`\n]+`+",
        r"!?\[[^\]\n]*\]\([^\)\n]*\)",
        r"<[^>\n]+>",
        r"(?<!\*)\*{1,3}[^*\n]+\*{1,3}(?!\*)",
        r"\([^()\n]*(?:19|20)\d{2}[^()\n]*\)",
    ]
    spans: list[tuple[int, int]] = []
    for pattern in patterns:
        spans.extend(match.span() for match in re.finditer(pattern, text))
    return merge_spans(spans)


def add_markdown_italics(text: str) -> tuple[str, int]:
    protected = protected_markdown_spans(text)
    targets: list[tuple[int, int]] = []
    cursor = 0
    for start, end in protected + [(len(text), len(text))]:
        segment = text[cursor:start]
        targets.extend((cursor + a, cursor + b) for a, b in foreign_spans(segment))
        cursor = end
    targets = merge_spans(targets)
    for start, end in reversed(targets):
        text = text[:start] + "*" + text[start:end] + "*" + text[end:]
    return text, len(targets)


def update_markdown(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    output: list[str] = []
    in_code = False
    in_abstract = False
    in_bibliography = False
    changes = 0

    for raw in lines:
        newline = "\n" if raw.endswith("\n") else ""
        line = raw[:-1] if newline else raw

        if line.startswith("```"):
            in_code = not in_code
            output.append(raw)
            continue
        if line == "## Abstract":
            in_abstract = True
        elif line == "## Lista de acrónimos":
            in_abstract = False
        if line == "## Bibliografia":
            in_bibliography = True
        elif line.startswith("## Anexo A "):
            in_bibliography = False

        versioned = line.replace("Versão do documento: 0.4.54", "Versão do documento: 0.4.55")
        if versioned != line:
            line = versioned
            changes += 1

        if in_code or in_abstract or in_bibliography or line.startswith(SOURCE_PREFIXES):
            output.append(line + newline)
            continue

        acronym_match = re.match(r"^(\| ([^|]+) \| )([^;]+)(;.*)$", line)
        if acronym_match:
            acronym = acronym_match.group(2).strip()
            expected = ACRONYM_EXPANSIONS.get(acronym)
            if expected and acronym_match.group(3) == expected:
                line = acronym_match.group(1) + f"*{expected}*" + acronym_match.group(4)
                changes += 1

        if line.startswith("| Ensaio 1 — indicadores populacionais indiretos"):
            cells = line.split("|")
            if len(cells) >= 6 and cells[3].strip() in FULL_ENGLISH_CELLS:
                cells[3] = " *" + cells[3].strip() + "* "
                line = "|".join(cells)
                changes += 1

        line, count = add_markdown_italics(line)
        changes += count
        output.append(line + newline)

    path.write_text("".join(output), encoding="utf-8")
    return changes


def qn(namespace: str, name: str) -> str:
    return f"{{{namespace}}}{name}"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def run_is_code(run: etree._Element) -> bool:
    styles = run.xpath("./w:rPr/w:rStyle/@w:val", namespaces=NS)
    fonts = run.xpath("./w:rPr/w:rFonts/@w:ascii", namespaces=NS)
    values = " ".join(styles + fonts).lower()
    return "code" in values or "courier" in values or "consolas" in values


def text_node_is_italic(node: etree._Element) -> bool:
    run = node.getparent()
    return bool(run.xpath("./w:rPr/w:i|./w:rPr/w:iCs", namespaces=NS))


def add_italic_property(run: etree._Element) -> None:
    rpr = run.find("w:rPr", NS)
    if rpr is None:
        rpr = etree.Element(qn(W, "rPr"))
        run.insert(0, rpr)
    if rpr.find("w:i", NS) is None:
        etree.SubElement(rpr, qn(W, "i"))
    if rpr.find("w:iCs", NS) is None:
        etree.SubElement(rpr, qn(W, "iCs"))


def split_text_node(node: etree._Element, intervals: list[tuple[int, int]]) -> int:
    text = node.text or ""
    run = node.getparent()
    if run.tag != qn(W, "r") or run_is_code(run):
        return 0
    text_nodes = run.xpath("./w:t", namespaces=NS)
    if len(text_nodes) != 1:
        return 0
    boundaries = {0, len(text)}
    for start, end in intervals:
        boundaries.update((start, end))
    points = sorted(boundaries)
    chunks = [(text[a:b], any(a < end and b > start for start, end in intervals)) for a, b in zip(points, points[1:]) if a < b]
    if not chunks:
        return 0

    parent = run.getparent()
    index = parent.index(run)
    for offset, (value, italic) in enumerate(chunks):
        clone = deepcopy(run)
        clone_node = clone.xpath("./w:t", namespaces=NS)[0]
        clone_node.text = value
        if value.startswith(" ") or value.endswith(" "):
            clone_node.set(qn(XML, "space"), "preserve")
        elif qn(XML, "space") in clone_node.attrib:
            del clone_node.attrib[qn(XML, "space")]
        if italic:
            add_italic_property(clone)
        parent.insert(index + offset, clone)
    parent.remove(run)
    return sum(1 for _, italic in chunks if italic)


def protected_docx_spans(text: str) -> list[tuple[int, int]]:
    spans = [
        match.span()
        for match in re.finditer(r"\([^()\n]*(?:19|20)\d{2}[^()\n]*\)", text)
    ]
    return merge_spans(spans)


def target_docx_spans(text: str) -> list[tuple[int, int]]:
    protected = protected_docx_spans(text)
    targets: list[tuple[int, int]] = []
    cursor = 0
    for start, end in protected + [(len(text), len(text))]:
        segment = text[cursor:start]
        targets.extend((cursor + a, cursor + b) for a, b in foreign_spans(segment))
        cursor = end

    stripped = text.strip()
    if stripped in FULL_ENGLISH_CELLS:
        start = text.index(stripped)
        targets.append((start, start + len(stripped)))
    for expansion in ACRONYM_EXPANSIONS.values():
        if text.startswith(expansion + ";"):
            targets.append((0, len(expansion)))
    return merge_spans(targets)


def update_docx(path: Path) -> int:
    with ZipFile(path) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])
    changes = 0
    in_abstract = False
    in_bibliography = False

    for paragraph in document.xpath("//w:p", namespaces=NS):
        text = paragraph_text(paragraph)
        stripped = text.strip()
        if stripped.upper() == "ABSTRACT":
            in_abstract = True
        elif stripped in {"Lista de acrónimos", "Lista de Abreviaturas e/ou Siglas"}:
            in_abstract = False
        if stripped in {"Bibliografia", "Referências Bibliográficas"}:
            in_bibliography = True
        elif stripped.startswith("Anexo A —") and not stripped[-1:].isdigit():
            in_bibliography = False

        if (
            not stripped
            or in_abstract
            or in_bibliography
            or stripped.startswith(SOURCE_PREFIXES)
            or stripped.startswith("INTEGRATION OF DESIGN AND ARTIFICIAL INTELLIGENCE")
        ):
            continue

        targets = target_docx_spans(text)
        if not targets:
            continue

        nodes = paragraph.xpath(".//w:t", namespaces=NS)
        offset = 0
        work: list[tuple[etree._Element, list[tuple[int, int]]]] = []
        for node in nodes:
            value = node.text or ""
            node_start, node_end = offset, offset + len(value)
            intervals = []
            for start, end in targets:
                overlap_start = max(start, node_start)
                overlap_end = min(end, node_end)
                if overlap_start < overlap_end and not text_node_is_italic(node):
                    intervals.append((overlap_start - node_start, overlap_end - node_start))
            if intervals:
                work.append((node, merge_spans(intervals)))
            offset = node_end

        for node, intervals in reversed(work):
            changes += split_text_node(node, intervals)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = path.with_suffix(path.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, path)
    return changes


def main() -> None:
    markdown_changes = update_markdown(MARKDOWN)
    docx_changes = update_docx(DOCX)
    print(f"Markdown: {markdown_changes} segmentos actualizados")
    print(f"DOCX: {docx_changes} segmentos de execução actualizados")


if __name__ == "__main__":
    main()
