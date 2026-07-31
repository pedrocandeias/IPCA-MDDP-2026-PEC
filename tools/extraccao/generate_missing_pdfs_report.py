#!/usr/bin/env python3
"""Generate the missing-full-text report from the canonical DOCX.

The DOCX bibliography is the sole source of bibliographic entries.  The
Markdown manuscript mirror is deliberately not read.  This script checks the
materialised Word bibliography against PDFs in ``material/bibliografia`` and
the wider ``material`` library, while separating resources for which no
standalone PDF is expected.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.bibliografia.consolidate_docx_referenced_pdfs import (  # noqa: E402
    DEFAULT_DOCX,
    DEFAULT_LIBRARY,
    DEFAULT_TARGET,
    KNOWN_PDFS,
    NON_PDF_RESOURCES,
    Match,
    best_match,
    norm,
    parse_references,
    pdf_info,
)


DEFAULT_OUTPUT = DEFAULT_TARGET / "pdfs_em_falta.md"


def collect_matches(docx: Path, target: Path, library: Path) -> list[Match]:
    references = parse_references(docx)
    target_paths = sorted(target.glob("*.pdf"))
    library_paths = sorted(library.rglob("*.pdf"))
    unique_paths = list(dict.fromkeys(target_paths + library_paths))
    with ThreadPoolExecutor(max_workers=8) as executor:
        infos = [info for info in executor.map(pdf_info, unique_paths) if info is not None]

    target_prefix = str(target.relative_to(ROOT)) + "/"
    target_infos = [info for info in infos if info.path.startswith(target_prefix)]
    library_infos = [info for info in infos if not info.path.startswith(target_prefix)]
    info_by_path = {info.path: info for info in infos}

    matches: list[Match] = []
    for reference in references:
        known_path = KNOWN_PDFS.get((norm(reference.author), reference.year))
        if known_path and known_path in info_by_path:
            known_pdf = info_by_path[known_path]
            location = (
                "já presente"
                if known_path.startswith(target_prefix)
                else "biblioteca local"
            )
            matches.append(
                Match(
                    reference,
                    known_pdf,
                    103.0,
                    "associação documental previamente auditada",
                    location,
                )
            )
            continue
        pdf, score, reason = best_match(reference, target_infos)
        if pdf is not None:
            matches.append(Match(reference, pdf, score, reason, "já presente"))
            continue
        pdf, score, reason = best_match(reference, library_infos)
        if pdf is not None:
            matches.append(Match(reference, pdf, score, reason, "biblioteca local"))
        else:
            matches.append(
                Match(reference, None, score, reason, "sem correspondência")
            )
    return matches


def is_non_pdf_resource(match: Match) -> bool:
    key = (norm(match.reference.author).lstrip("- "), match.reference.year)
    return key in NON_PDF_RESOURCES


def destination(match: Match) -> tuple[str, str]:
    if match.reference.dois:
        doi = match.reference.dois[0]
        return f"[https://doi.org/{doi}](https://doi.org/{doi})", "DOI confirmado na entrada"
    urls = re.findall(r"https?://[^\s<>)\]]+", match.reference.entry)
    if urls:
        url = urls[0].rstrip(".,;")
        return f"[{url}]({url})", "URL da entrada bibliográfica"
    query = urllib.parse.quote(f'"{match.reference.title}"')
    url = f"https://search.crossref.org/?q={query}"
    return "[Pesquisar no Crossref](" + url + ")", "DOI não identificado"


def render(docx: Path, matches: list[Match]) -> str:
    with_pdf = [match for match in matches if match.pdf is not None]
    non_pdf = [
        match
        for match in matches
        if match.pdf is None and is_non_pdf_resource(match)
    ]
    missing = [
        match
        for match in matches
        if match.pdf is None and not is_non_pdf_resource(match)
    ]
    lines = [
        "# PDFs em falta — bibliografia do DOCX",
        "",
        "Este relatório verifica a disponibilidade local do texto integral para as "
        "entradas materializadas na bibliografia do DOCX canónico. O Markdown que "
        "replica o manuscrito não é lido.",
        "",
        f"Última verificação: {date.today().isoformat()}.",
        "",
        "## Síntese",
        "",
        f"- Documento: `{docx.relative_to(ROOT)}`.",
        f"- SHA-256 do DOCX: `{hashlib.sha256(docx.read_bytes()).hexdigest()}`.",
        f"- Entradas bibliográficas: **{len(matches)}**.",
        f"- Entradas com PDF local validado: **{len(with_pdf)}**.",
        f"- Recursos sem PDF autónomo esperado: **{len(non_pdf)}**.",
        f"- Entradas sem texto integral local: **{len(missing)}**.",
        "",
        "## Entradas sem texto integral local",
        "",
    ]
    if missing:
        lines.extend(
            [
                "| N.º | Referência | Título | Localização bibliográfica | Estado |",
                "| ---: | --- | --- | --- | --- |",
            ]
        )
        for index, match in enumerate(missing, start=1):
            link, link_state = destination(match)
            reference = f"{match.reference.author} ({match.reference.year})"
            title = match.reference.title.replace("|", "\\|")
            lines.append(
                f"| {index} | {reference} | *{title}* | {link} | "
                f"{link_state}; PDF local não localizado. |"
            )
    else:
        lines.append(
            "Não existem entradas da bibliografia materializada cujo texto integral "
            "continue por localizar."
        )

    lines.extend(
        [
            "",
            "## Recursos sem PDF autónomo esperado",
            "",
            "| Referência | Recurso |",
            "| --- | --- |",
        ]
    )
    for match in non_pdf:
        reference = f"{match.reference.author} ({match.reference.year})"
        title = match.reference.title.replace("|", "\\|")
        lines.append(f"| {reference} | *{title}* |")

    lines.extend(
        [
            "",
            "## Limite desta verificação",
            "",
            "Este inventário responde apenas à pergunta «existe texto integral local "
            "para cada entrada bibliográfica?». Não demonstra que todas as citações "
            "do DOCX tenham uma entrada correcta. As citações ausentes, os controlos "
            "ligados à obra errada, as divergências de ano e as entradas potencialmente "
            "órfãs são registados em "
            "`docs/revisoes/bibliografia/auditoria_completude_bibliografica_docx_0_4_112.md`.",
            "",
            "As duas entradas actualmente sem texto integral também figuram como "
            "potencialmente órfãs nessa auditoria. A decisão editorial sobre a sua "
            "manutenção deve preceder uma nova tentativa de obtenção.",
            "",
            "## Método reproduzível",
            "",
            "```bash",
            "python3 tools/extraccao/generate_missing_pdfs_report.py",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    matches = collect_matches(args.docx, args.target, args.library)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(args.docx, matches), encoding="utf-8")
    missing = sum(
        match.pdf is None and not is_non_pdf_resource(match) for match in matches
    )
    print(
        f"Wrote {args.output}: {len(matches)} bibliography entries, "
        f"{missing} without local full text."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
