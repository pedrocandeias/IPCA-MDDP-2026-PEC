#!/usr/bin/env python3
"""Consolidate locally available PDFs cited in the canonical DOCX.

The script reads the bibliography directly from the Word document, compares
each entry with PDFs already held in ``projecto_completo_bibliografia`` and
then searches ``material`` for missing files.  Matching favours DOI equality
and high title similarity.  ``--apply`` copies only validated matches and
writes a traceability report alongside the consolidated PDF collection.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import unicodedata
import zipfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

import fitz


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
DEFAULT_TARGET = ROOT / "projecto_completo_bibliografia"
DEFAULT_LIBRARY = ROOT / "material"
DEFAULT_REPORT = DEFAULT_TARGET / "consolidacao_referencias_docx.md"

# Sources whose local filenames are historical, abbreviated or identify the
# containing volume rather than the cited chapter.  Every association below
# was already checked against the source in the reference-audit report.
KNOWN_PDFS = {
    ("barredo arrieta", "2020"): "projecto_completo_bibliografia/A Framework to Study Human-AI Collaborative Design Space Exploration (2021).pdf",
    ("center for universal design", "1997"): "projecto_completo_bibliografia/Center_for_Universal_Design_1997_Principles_of_Universal_Design.pdf",
    ("dexter", "2013"): "projecto_completo_bibliografia/dexter_atkinson_dearden_2013_open_design_cystic_fibrosis.pdf",
    ("fischer", "2004"): "projecto_completo_bibliografia/Meta-Design_A_manifesto_for_End-User_Development.pdf",
    ("fischer", "2017"): "projecto_completo_bibliografia/new_perspectives_end_user_development_2017.pdf",
    ("frangos", "2016"): "projecto_completo_bibliografia/frangos_et_al_2016_democratising_open_source_hardware_design.pdf",
    ("frayling", "1994"): "projecto_completo_bibliografia/Frayling-1994-Research in art and design.pdf",
    ("gordon", "2015"): "projecto_completo_bibliografia/Gordon_et_al_2015_ANSUR_II_methods_summary_statistics.pdf",
    ("herbst", "2021"): "projecto_completo_bibliografia/herbst_et_al_2021_scan_driven_personalized_prosthetic_hand.pdf",
    ("international electrotechnical commission", "2015"): "projecto_completo_bibliografia/IEC-62366-1_2015.pdf",
    ("international organization for standardization", "2017"): "projecto_completo_bibliografia/ISO_7250-1_2017_Basic_human_body_measurements.pdf",
    ("international organization for standardization", "2020"): "projecto_completo_bibliografia/ISO_8549-1_2020_Prosthetics_and_orthotics_vocabulary.pdf",
    ("resnik", "2010"): "projecto_completo_bibliografia/us-food-and-drug-administration-regulation-of-prosthetic.pdf",
    ("sims", "2017"): "projecto_completo_bibliografia/sims_et_al_2017_participatory_design_pediatric_upper_limb_prostheses.pdf",
}

NON_PDF_RESOURCES = {
    ("base local consolidada de dados antropometricos da mao e do membro superior distal", "2026"),
    ("brooks", "2026"),
    ("design council", "2020"),
    ("molenbroek", "1998"),
    ("world wide web consortium", "2024"),
    ("world wide web consortium", "2014"),
}

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
YEAR_RE = re.compile(r"\(((?:19|20)\d{2})[a-z]?(?:,\s*[^)]*)?\)\.\s+")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)

STOPWORDS = {
    "a", "an", "and", "as", "at", "by", "da", "das", "de", "del", "do",
    "dos", "e", "em", "for", "from", "in", "into", "of", "on", "or",
    "para", "the", "to", "using", "with", "without", "um", "uma",
    "review", "study", "analysis", "design", "development", "method",
}


@dataclass(frozen=True)
class Reference:
    number: int
    entry: str
    title: str
    author: str
    year: str
    dois: tuple[str, ...]


@dataclass
class PdfInfo:
    path: str
    sha256: str
    filename_norm: str
    title_norm: str
    author_norm: str
    year: str
    text_head_norm: str
    text_norm: str
    dois: tuple[str, ...]


@dataclass
class Match:
    reference: Reference
    pdf: PdfInfo | None
    score: float
    reason: str
    location: str


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def clean_doi(value: str) -> str:
    return value.casefold().rstrip(".,;:)]}\u00bb")


def tokens(value: str) -> set[str]:
    return {
        token for token in norm(value).split()
        if len(token) > 2 and token not in STOPWORDS and not token.isdigit()
    }


def word_paragraphs(docx: Path) -> list[str]:
    with zipfile.ZipFile(docx) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    paragraphs: list[str] = []
    for paragraph in root.iter(f"{{{W_NS}}}p"):
        text = "".join(node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t"))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def extract_title(rest: str) -> str:
    # APA entries in this manuscript place the work title immediately after
    # the year.  The title normally ends at the first sentence boundary.
    protected = rest.replace("U.S.", "U§S§")
    title = re.split(r"\.\s+(?=[A-ZÀ-ÖØ-Þ\[])|\.\s+https?://", protected, maxsplit=1)[0]
    return title.replace("U§S§", "U.S.").rstrip(". ")


def parse_references(docx: Path) -> list[Reference]:
    paragraphs = word_paragraphs(docx)
    try:
        start = paragraphs.index("Referências Bibliográficas") + 1
    except ValueError as exc:
        raise RuntimeError("Não foi encontrada a secção 'Referências Bibliográficas'.") from exc

    end = next(
        (idx for idx in range(start, len(paragraphs)) if paragraphs[idx].startswith("ANEXO A")),
        len(paragraphs),
    )
    entries = paragraphs[start:end]
    references: list[Reference] = []
    for entry in entries:
        year_match = YEAR_RE.search(entry)
        if not year_match:
            continue
        rest = entry[year_match.end():]
        title = extract_title(rest)
        author_prefix = entry[:year_match.start()].strip()
        author = author_prefix.split(",", 1)[0].strip()
        dois = tuple(sorted({clean_doi(match.group(0)) for match in DOI_RE.finditer(entry)}))
        references.append(Reference(
            number=len(references) + 1,
            entry=entry,
            title=title,
            author=author,
            year=year_match.group(1),
            dois=dois,
        ))
    return references


def pdf_info(path: Path) -> PdfInfo | None:
    try:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
    except FileNotFoundError:
        # The library may be reorganised in another process while the scan is
        # running.  A disappeared source is ignored and the current location
        # will be found on the next execution.
        return None
    metadata: dict[str, str] = {}
    text_parts: list[str] = []
    try:
        document = fitz.open(path)
        metadata = {key: value or "" for key, value in (document.metadata or {}).items()}
        for page_number in range(min(3, len(document))):
            text_parts.append(document[page_number].get_text("text"))
        document.close()
    except Exception:
        pass
    text = "\n".join(text_parts)
    doi_source = "\n".join((metadata.get("subject", ""), metadata.get("keywords", ""), text))
    dois = tuple(sorted({clean_doi(match.group(0)) for match in DOI_RE.finditer(doi_source)}))
    year_match = re.search(r"(?:19|20)\d{2}", metadata.get("creationDate", ""))
    return PdfInfo(
        path=str(path.relative_to(ROOT)),
        sha256=digest,
        filename_norm=norm(path.stem),
        title_norm=norm(metadata.get("title", "")),
        author_norm=norm(metadata.get("author", "")),
        year=year_match.group(0) if year_match else "",
        text_head_norm=norm(text[:3500]),
        text_norm=norm(text[:18000]),
        dois=dois,
    )


def similarity(reference: Reference, pdf: PdfInfo) -> tuple[float, str]:
    title_norm = norm(reference.title)
    title_tokens = tokens(reference.title)
    if not title_tokens:
        return 0.0, "sem termos de título suficientes"

    candidates = [pdf.filename_norm, pdf.title_norm]
    structured_scores: list[float] = []
    for candidate in candidates:
        if not candidate:
            continue
        candidate_tokens = tokens(candidate)
        intersection = len(title_tokens & candidate_tokens)
        recall = intersection / len(title_tokens)
        precision = intersection / len(candidate_tokens) if candidate_tokens else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        score = max(recall * 92.0, f1 * 100.0)
        if title_norm and (title_norm in candidate or candidate in title_norm) and min(len(title_norm), len(candidate)) >= 24:
            score = max(score, 98.0)
        structured_scores.append(score)

    structured = max(structured_scores, default=0.0)
    author_norm = norm(reference.author)
    author_structured = bool(author_norm and (
        author_norm in pdf.author_norm
        or author_norm in pdf.filename_norm
    ))
    author_head = bool(author_norm and author_norm in pdf.text_head_norm)
    author_present = author_structured or author_head
    year_present = reference.year in pdf.text_norm or reference.year == pdf.year
    doi_match = bool(set(reference.dois) & set(pdf.dois))

    score = structured
    reasons: list[str] = []
    if doi_match:
        # Exact DOI is decisive when it is corroborated by either the title or
        # the first author, preventing a DOI found only in a reference list
        # from creating a false match.
        if score >= 35.0 or author_present:
            score = max(score, 100.0)
            reasons.append("DOI idêntico")
    if structured >= 70.0:
        reasons.append("título no nome/metadados")
    if title_norm and title_norm in pdf.text_head_norm and author_head:
        score = max(score, 98.0)
        reasons.append("título e autor na primeira página")
    if author_present:
        score += 3.0
        reasons.append("primeiro autor confirmado")
    if year_present:
        score += 1.0
        reasons.append("ano confirmado")

    return min(score, 103.0), ", ".join(reasons) or "sem confirmação suficiente"


def best_match(reference: Reference, pdfs: list[PdfInfo]) -> tuple[PdfInfo | None, float, str]:
    ranked = sorted(
        ((pdf, *similarity(reference, pdf)) for pdf in pdfs),
        key=lambda item: item[1],
        reverse=True,
    )
    if not ranked:
        return None, 0.0, "sem candidatos"
    for pdf, score, reason in ranked:
        # Require an exact/corroborated DOI, a near-exact structured title, or
        # a strong structured title accompanied by the first author.  A title
        # occurring only in the body/reference list of another paper is not
        # accepted.
        if "DOI idêntico" in reason:
            return pdf, score, reason
        if score >= 98.0 and (
            "título no nome/metadados" in reason
            or "título e autor na primeira página" in reason
        ):
            return pdf, score, reason
        if (
            score >= 78.0
            and "título no nome/metadados" in reason
            and "primeiro autor confirmado" in reason
            and "ano confirmado" in reason
        ):
            return pdf, score, reason
    pdf, score, reason = ranked[0]
    return None, score, reason


def destination_for(source: Path, target: Path) -> Path:
    destination = target / source.name
    if not destination.exists():
        return destination
    if hashlib.sha256(destination.read_bytes()).digest() == hashlib.sha256(source.read_bytes()).digest():
        return destination
    stem, suffix = source.stem, source.suffix
    counter = 2
    while True:
        candidate = target / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def report_text(
    docx: Path,
    matches: list[Match],
    copied: list[tuple[str, str]],
    current_pdf_count: int,
    baseline_count: int | None,
) -> str:
    existing = [match for match in matches if match.location == "já presente"]
    available = [match for match in matches if match.location == "biblioteca local"]
    unmatched = [match for match in matches if match.pdf is None]
    non_pdf = [
        match for match in unmatched
        if (norm(match.reference.author).lstrip("- "), match.reference.year) in NON_PDF_RESOURCES
    ]
    unavailable_documents = [match for match in unmatched if match not in non_pdf]
    lines = [
        "# Consolidação dos PDFs referenciados no DOCX",
        "",
        f"Última verificação: {date.today().isoformat()}.",
        "",
        f"- Documento analisado: `{docx.relative_to(ROOT)}`",
        f"- Entradas bibliográficas identificadas: **{len(matches)}**",
        f"- Entradas com PDF já presente na pasta consolidada: **{len(existing)}**",
        f"- Entradas com PDF validado noutra pasta local: **{len(available)}**",
        f"- PDFs existentes na pasta consolidada: **{current_pdf_count}**",
        f"- Documentos citados sem texto integral local: **{len(unavailable_documents)}**",
        f"- Recursos digitais ou conjuntos de dados sem PDF autónomo esperado: **{len(non_pdf)}**",
        "",
        "A ausência de correspondência nesta lista não significa necessariamente que falte um *paper*: a bibliografia inclui igualmente páginas institucionais, normas apenas referenciadas por catálogo, conjuntos de dados e outros recursos sem PDF local.",
        "",
    ]
    if baseline_count is not None:
        lines.insert(9, f"- PDFs acrescentados desde o inventário inicial ({baseline_count}): **{current_pdf_count - baseline_count}**")
    if copied:
        lines.extend((
            "## PDFs copiados",
            "",
            "| Origem | Destino |",
            "| --- | --- |",
        ))
        lines.extend(f"| `{source}` | `{destination}` |" for source, destination in copied)
        lines.append("")

    lines.extend((
        "## Correspondências validadas",
        "",
        "| Referência | PDF consolidado | Critério |",
        "| --- | --- | --- |",
    ))
    for match in matches:
        if match.pdf is None:
            continue
        pdf_name = Path(match.pdf.path).name.replace("|", "\\|")
        reference = f"{match.reference.author} ({match.reference.year})"
        lines.append(f"| {reference} | `{pdf_name}` | {match.reason} |")

    lines.extend((
        "",
        "## Documentos citados sem texto integral local",
        "",
        "| Referência | Título |",
        "| --- | --- |",
    ))
    for match in unavailable_documents:
        reference = f"{match.reference.author} ({match.reference.year})"
        title = match.reference.title.replace("|", "\\|")
        lines.append(f"| {reference} | *{title}* |")
    lines.extend((
        "",
        "## Recursos sem PDF autónomo esperado",
        "",
        "| Referência | Recurso |",
        "| --- | --- |",
    ))
    for match in non_pdf:
        reference = f"{match.reference.author} ({match.reference.year})"
        title = match.reference.title.replace("|", "\\|")
        lines.append(f"| {reference} | *{title}* |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--apply", action="store_true", help="copiar PDFs e gravar o relatório")
    parser.add_argument("--json", type=Path, help="gravar também os resultados estruturados")
    parser.add_argument(
        "--baseline-count", type=int,
        help="número de PDFs no destino antes da operação, para registar o acréscimo total",
    )
    args = parser.parse_args()

    references = parse_references(args.docx)
    target_paths = sorted(args.target.glob("*.pdf"))
    library_paths = sorted(args.library.rglob("*.pdf"))
    print(f"Referências: {len(references)}; destino: {len(target_paths)} PDFs; biblioteca: {len(library_paths)} PDFs")

    unique_paths = list(dict.fromkeys(target_paths + library_paths))
    with ThreadPoolExecutor(max_workers=8) as executor:
        infos = [info for info in executor.map(pdf_info, unique_paths) if info is not None]

    target_prefix = str(args.target.relative_to(ROOT)) + "/"
    target_infos = [info for info in infos if info.path.startswith(target_prefix)]
    library_infos = [info for info in infos if not info.path.startswith(target_prefix)]

    matches: list[Match] = []
    info_by_path = {info.path: info for info in infos}
    for reference in references:
        known_path = KNOWN_PDFS.get((norm(reference.author), reference.year))
        if known_path and known_path in info_by_path:
            known_pdf = info_by_path[known_path]
            location = "já presente" if known_path.startswith(target_prefix) else "biblioteca local"
            matches.append(Match(reference, known_pdf, 103.0, "associação documental previamente auditada", location))
            continue
        pdf, score, reason = best_match(reference, target_infos)
        if pdf is not None:
            matches.append(Match(reference, pdf, score, reason, "já presente"))
            continue
        pdf, score, reason = best_match(reference, library_infos)
        if pdf is not None:
            matches.append(Match(reference, pdf, score, reason, "biblioteca local"))
        else:
            matches.append(Match(reference, None, score, reason, "sem correspondência"))

    copied: list[tuple[str, str]] = []
    if args.apply:
        args.target.mkdir(parents=True, exist_ok=True)
        for match in matches:
            if match.location != "biblioteca local" or match.pdf is None:
                continue
            source = ROOT / match.pdf.path
            destination = destination_for(source, args.target)
            if not destination.exists():
                shutil.copy2(source, destination)
                copied.append((match.pdf.path, str(destination.relative_to(ROOT))))
            match.pdf.path = str(destination.relative_to(ROOT))
            match.location = "já presente"
        current_pdf_count = len(list(args.target.glob("*.pdf")))
        args.report.write_text(
            report_text(args.docx, matches, copied, current_pdf_count, args.baseline_count),
            encoding="utf-8",
        )
        compact_manifest = [
            {
                "reference": f"{match.reference.author} ({match.reference.year})",
                "title": match.reference.title,
                "pdf": match.pdf.path,
                "criterion": match.reason,
            }
            for match in matches if match.pdf is not None
        ]
        (args.target / "copied_matches.json").write_text(
            json.dumps(compact_manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    if args.json:
        payload = [
            {
                "reference": asdict(match.reference),
                "pdf": asdict(match.pdf) if match.pdf else None,
                "score": round(match.score, 2),
                "reason": match.reason,
                "location": match.location,
            }
            for match in matches
        ]
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    existing = sum(match.location == "já presente" for match in matches)
    available = sum(match.location == "biblioteca local" for match in matches)
    missing = sum(match.pdf is None for match in matches)
    print(f"Já presentes: {existing}; disponíveis para copiar: {available}; sem correspondência validada: {missing}")
    for match in matches:
        if match.location == "biblioteca local" and match.pdf:
            print(f"COPIAR\t{match.reference.author} {match.reference.year}\t{match.pdf.path}\t{match.score:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
