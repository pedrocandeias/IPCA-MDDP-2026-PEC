#!/usr/bin/env python3
"""Retrieve missing bibliography PDFs attached to matching Mendeley records."""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import fitz

from consolidate_docx_referenced_pdfs import DOI_RE, clean_doi, norm, tokens

# Os scripts Mendeley vivem no submódulo tools/mendeley-tools (repositório
# github.com/pedrocandeias/mendeley-tools), cujo nome com hífen não é
# importável directamente.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mendeley-tools"))
from mendeley_enrich import MendeleyAPI, load_credentials  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RESULTS = Path("/tmp/consolidation_verify2.json")
DEFAULT_TARGET = ROOT / "material/bibliografia"


def document_dois(document: dict) -> set[str]:
    identifiers = document.get("identifiers") or {}
    values: list[str] = []
    if isinstance(identifiers, dict):
        values.extend(str(value) for value in identifiers.values() if value)
    return {
        clean_doi(match.group(0))
        for value in values
        for match in DOI_RE.finditer(value)
    }


def reference_dois(reference: dict) -> set[str]:
    return {clean_doi(value) for value in reference.get("dois", [])}


def document_authors(document: dict) -> str:
    authors = document.get("authors") or []
    return " ".join(
        " ".join(str(author.get(key, "")) for key in ("first_name", "last_name"))
        for author in authors if isinstance(author, dict)
    )


def document_year(document: dict) -> str:
    year = document.get("year")
    if year:
        return str(year)
    return str(document.get("created") or "")[:4]


def document_match(reference: dict, document: dict) -> tuple[float, str]:
    ref_title = norm(reference.get("title", ""))
    doc_title = norm(document.get("title", ""))
    if not ref_title or not doc_title:
        return 0.0, ""
    ref_dois = reference_dois(reference)
    doc_dois = document_dois(document)
    if ref_dois & doc_dois:
        return 1.0, "DOI"
    ratio = SequenceMatcher(None, ref_title, doc_title).ratio()
    author = norm(reference.get("author", ""))
    author_ok = bool(author and author in norm(document_authors(document)))
    year_ok = reference.get("year", "") == document_year(document)
    if ratio >= 0.88 and author_ok and year_ok:
        return ratio, "título, autor e ano"
    if ratio >= 0.96 and author_ok:
        return ratio, "título e autor"
    return 0.0, ""


def validate_pdf(content: bytes, reference: dict) -> tuple[bool, str]:
    if not content.startswith(b"%PDF"):
        return False, "conteúdo não é PDF"
    try:
        document = fitz.open(stream=content, filetype="pdf")
        text = "\n".join(
            document[page].get_text("text") for page in range(min(3, len(document)))
        )
        metadata = document.metadata or {}
        document.close()
    except Exception as exc:
        return False, f"PDF inválido: {exc}"

    doi_source = "\n".join((metadata.get("subject", ""), text))
    pdf_dois = {clean_doi(match.group(0)) for match in DOI_RE.finditer(doi_source)}
    if reference_dois(reference) & pdf_dois:
        return True, "DOI confirmado no PDF"

    title_tokens = tokens(reference.get("title", ""))
    head = norm(text[:5000])
    author = norm(reference.get("author", ""))
    recall = len(title_tokens & tokens(head)) / len(title_tokens) if title_tokens else 0.0
    if recall >= 0.8 and author and author in head:
        return True, "título e autor confirmados no PDF"
    return False, "conteúdo do anexo não corresponde de forma segura"


def safe_filename(file_record: dict, reference: dict) -> str:
    supplied = str(file_record.get("file_name") or file_record.get("name") or "").strip()
    if supplied.lower().endswith(".pdf"):
        name = Path(supplied).name
    else:
        name = re.sub(r"[^\w .()\[\]-]+", "_", reference.get("title", ""), flags=re.UNICODE).strip()
        name = f"{name}.pdf"
    return name[:230]


def unique_destination(target: Path, name: str) -> Path:
    destination = target / name
    if not destination.exists():
        return destination
    counter = 2
    while True:
        candidate = target / f"{destination.stem} ({counter}){destination.suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


async def main_async(args: argparse.Namespace) -> int:
    payload = json.loads(args.results.read_text(encoding="utf-8"))
    references = [item["reference"] for item in payload if item.get("pdf") is None]

    api = MendeleyAPI(load_credentials())
    try:
        documents = await api.get_all_documents()
        matches: list[tuple[dict, dict, float, str]] = []
        for reference in references:
            ranked = sorted(
                ((document, *document_match(reference, document)) for document in documents),
                key=lambda item: item[1],
                reverse=True,
            )
            if ranked and ranked[0][1] > 0:
                document, score, reason = ranked[0]
                matches.append((reference, document, score, reason))

        print(f"Referências sem PDF local: {len(references)}; correspondências Mendeley seguras: {len(matches)}")
        downloaded = 0
        for reference, document, score, reason in matches:
            response = await api._req(
                "GET", "/files", accept="application/vnd.mendeley-file.1+json",
                params={"document_id": document["id"]},
            )
            files = response.json()
            pdf_files = [
                file for file in files
                if "pdf" in str(file.get("mime_type", "")).casefold()
                or str(file.get("file_name", "")).casefold().endswith(".pdf")
            ]
            print(
                f"{reference['author']} ({reference['year']}): {document.get('title')} "
                f"[{reason}; anexos PDF: {len(pdf_files)}]"
            )
            if not args.apply or not pdf_files:
                continue
            file_record = pdf_files[0]
            download = await api._req(
                "GET", f"/files/{file_record['id']}", accept="application/pdf"
            )
            valid, validation = validate_pdf(download.content, reference)
            if not valid:
                print(f"  IGNORADO: {validation}")
                continue
            destination = unique_destination(args.target, safe_filename(file_record, reference))
            destination.write_bytes(download.content)
            downloaded += 1
            print(f"  GRAVADO: {destination.relative_to(ROOT)} ({validation})")

        print(f"PDFs descarregados e validados: {downloaded}")
        return 0
    finally:
        await api.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    sys.exit(main())
