#!/usr/bin/env python3
"""Generate the authoritative list of cited papers without local full text.

The generator reconciles Section 4 of the reference-audit report with the
canonical bibliography.  DOI links come from the bibliography or from the
audit record; when no DOI or stable source URL is available, the output links
to a title search in Crossref and marks the DOI as unverified.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata
import urllib.parse
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANUSCRIPT = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DEFAULT_AUDIT = ROOT / "docs/revisoes/auditoria_referencias_texto_papers_061.md"
DEFAULT_OUTPUT = ROOT / "projecto_completo_bibliografia/pdfs_em_falta.md"


@dataclass
class MissingSource:
    reference: str
    title: str
    evidence: list[str] = field(default_factory=list)
    bibliography: str = ""
    doi: str = ""
    source_url: str = ""


def strip_markdown(value: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = value.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", value).strip()


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", strip_markdown(value)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def title_key(value: str) -> str:
    return normalized(value)


# DOI confirmed against publisher, repository, PubMed or Crossref metadata on
# 2026-07-16.  Keeping this map in the generator makes the report reproducible
# without turning a future network search result into an automatic assertion.
VERIFIED_DOIS = {
    title_key("Functionality and comfort design of lower-limb prosthetics: A review"): "10.57197/jdr-2023-0031",
    title_key("A narrative review of prosthesis design decision making after lower-limb amputation for developing shared decision-making resources"): "10.1007/s40141-024-00432-y",
    title_key("Adjustable prosthetic sockets: A systematic review of industrial and research design characteristics and their justifications"): "10.1186/s12984-023-01270-0",
    title_key("Technological advances in prosthesis design and rehabilitation following upper extremity limb loss"): "10.1007/s12178-020-09656-6",
    title_key("Design for all, design for disabled: How important is anthropometry?"): "10.3233/WOR-211106",
    title_key("Improving access to prosthetic limbs in Germany: An explorative review"): "10.1097/PXR.0000000000000254",
    title_key("Technology for monitoring everyday prosthesis use: A systematic review"): "10.1186/s12984-020-00711-4",
    title_key("Artificial intelligence (AI) in the design process: A review and analysis on generative AI perspectives"): "10.1017/pds.2025.10077",
    title_key("Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design"): "10.1109/TIPTEKNO56568.2022.9960218",
    title_key("Design for additive manufacturing: Review and framework proposal"): "10.37868/sei.v5i1.id185",
    title_key("Literature review on needs of upper limb prosthesis users"): "10.3389/fnins.2016.00209",
    title_key("Meta-design to Face Co-evolution and Communication Gaps Between Users and Designers"): "10.1007/978-3-540-73279-2_6",
    title_key("Accessible prosthetic arms: Victoria Hand Project and the impact of 3D printing"): "10.33137/cpoj.v6i2.42142",
    title_key("Low limb prostheses and complex human prosthetic interaction: A systematic literature review"): "10.3389/frobt.2023.1032748",
    title_key("AI in design idea development: A workshop on creativity and human-AI collaboration"): "10.21606/drs.2022.414",
    title_key("Prosthesis options and management in upper extremity amputation"): "10.1016/j.oto.2023.101061",
    title_key("Human-centered design for medical devices and diagnostics in global health"): "10.15641/ghi.v3i1.762",
    title_key("Satisfying heterogeneous user needs via innovation toolkits: The case of Apache security software"): "10.1016/S0048-7333(03)00049-0",
    title_key("Revisiting and Broadening the Meta-design Framework for End-user Development"): "10.1007/978-3-319-60291-2_4",
    title_key("Guidelines and recommendations to investigate the efficacy of a lower-limb prosthetic device: A systematic review"): "10.1109/TMRB.2019.2949855",
    title_key("Issues affecting the level of prosthetics research evidence: Secondary analysis of a systematic review"): "10.1177/0309364614550264",
    title_key("Assessing the Use of Co-design to Produce Bespoke Assistive Technology Solutions Within a Current Healthcare Service"): "10.1080/17483107.2022.2060355",
    title_key("3D Printing in LMICs: Functional Design for Upper Limb Prosthetics in Uganda"): "10.3390/prosthesis5010011",
    title_key("Integrating parametric design and additive manufacturing knowledge in industrial design education"): "10.1016/j.matpr.2022.10.124",
    title_key("A Participatory Model for Cocreating Accessible Rehabilitation Technology for Stroke Survivors: User-centered Design Approach"): "10.2196/57227",
    title_key("Mapping artificial intelligence-based methods to engineering design stages: A focused literature review"): "10.1017/s0890060423000203",
    title_key("Deep learning for automated product design"): "10.5445/IR/1000127884",
    title_key("Design of Personalized Devices: The Tradeoff Between Individual Value and Personalization Workload"): "10.3390/app11010241",
    title_key("An additive manufacturing process model for product family design"): "10.1080/09544828.2016.1228101",
    title_key("A review of user needs to inform the development of lower-limb prostheses"): "10.1186/s12984-022-01097-1",
    title_key("Personalization of the 3D-printed Upper Limb Exoskeleton Design: Mechanical and IT Aspects"): "10.3390/app13127236",
    title_key("Design methodology for mass personalisation enabled by digital manufacturing"): "10.1017/dsj.2022.3",
    title_key("Special issue: Machine learning for engineering design"): "10.1115/1.4044690",
    title_key("U.S. Food and Drug Administration regulation of prosthetic research, development, and testing"): "10.1097/JPO.0b013e3181d427b7",
    title_key("User experience of transtibial prosthetic liners: A systematic review"): "10.1177/0309364616631343",
    title_key("Parametric design for online user customization of 3D printed assistive technology for rheumatic diseases"): "10.1007/978-3-030-58468-9_14",
    title_key("Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework"): "10.61186/ist.202401.01.09",
    title_key("Effects of lower limb prosthesis on activity, participation, and quality of life: A systematic review"): "10.1177/0309364611432794",
    title_key("Upper limb prostheses by the level of amputation: A systematic review"): "10.3390/prosthesis6020022",
    title_key("User involvement in healthcare technology development and assessment: Structured literature review"): "10.1108/09526860610687619",
    title_key("A review on 3D scanners studies for producing customized orthoses"): "10.3390/s24051373",
    title_key("Participatory Design of Pediatric Upper Limb Prostheses: Qualitative Methods and Prototyping"): "10.1017/S0266462317000836",
    title_key("The importance of rehabilitation concerning upper extremity amputees: A systematic review"): "10.12669/pjms.325.9922",
    title_key("Applying the principles of universal design to medical devices"): "10.1201/9781420006223-6",
    title_key("From Patient to Maker: A Workflow Including People With Cerebral Palsy in Co-creating Assistive Devices Using 3D Printing Technologies"): "10.1080/17483107.2023.2177754",
    title_key("Product customization and generative design"): "10.35925/j.multi.2021.4.10",
    title_key("A framework to study human-AI collaborative design space exploration"): "10.1115/DETC2021-67619",
    title_key("Demystifying upper limb hybrid prostheses: A scoping review"): "10.3389/fresc.2025.1610336",
    title_key("Developing innovative solutions for universal design in healthcare and other sectors"): "10.3233/SHTI220858",
    title_key("Design for additive manufacturing: A review of available design methods and software"): "10.1108/RPJ-10-2018-0262",
    title_key("The healthcare design dilemma: Perils of a technology-driven design process for medical products"): "10.1017/dsd.2020.133",
    title_key("Active lower limb prosthetics: A systematic review of design issues and solutions"): "10.1186/s12938-016-0284-9",
    title_key("A cost-driven design methodology for additive manufactured variable platforms in product families"): "10.1115/1.4032504",
    title_key("Review of artificial intelligence applications in engineering design perspective"): "10.1016/j.engappai.2022.105697",
}


def source_key(reference: str) -> tuple[str, str]:
    year_match = re.search(r"\b(19|20)\d{2}\b", reference)
    year = year_match.group(0) if year_match else ""
    author = re.split(r"\s+et al\.|\s+e\s+|,", strip_markdown(reference), maxsplit=1)[0]
    if normalized(author) == "abbas alili":
        author = "Alili"
    author_tokens = normalized(author).split()
    return (author_tokens[-1] if author_tokens else "", year)


def extract_section(text: str, start: str, end: str) -> str:
    start_pos = text.index(start)
    end_pos = text.index(end, start_pos)
    return text[start_pos:end_pos]


def add_source(store: dict[str, MissingSource], reference: str, title: str, evidence: str) -> None:
    reference = strip_markdown(reference)
    title = strip_markdown(title)
    key = title_key(title)
    if not key:
        return
    item = store.setdefault(key, MissingSource(reference=reference, title=title))
    if evidence and evidence not in item.evidence:
        item.evidence.append(evidence)


def parse_missing_sources(audit_text: str) -> tuple[list[MissingSource], MissingSource]:
    section = extract_section(
        audit_text,
        "## 4. *Papers* citados sem texto integral consultado",
        "## 5. Fontes normativas, técnicas e institucionais",
    )
    sources: dict[str, MissingSource] = {}

    # The first seven entries use prose blocks instead of compact tables.
    block_pattern = re.compile(
        r"(?ms)^### 4\.(?P<number>[1-7])\s+(?P<reference>[^\n]+)\n"
        r"(?P<body>.*?)(?=^### 4\.|\Z)"
    )
    for match in block_pattern.finditer(section):
        body = match.group("body")
        title_match = re.search(r"\*\*Título indicado na bibliografia:\*\*\s*\*([^*]+)\*", body)
        if not title_match:
            raise RuntimeError(f"Missing title in audit subsection 4.{match.group('number')}")
        evidence = " ".join(re.findall(r"\*\*(?:Pesquisa local|Mendeley):\*\*\s*([^\n]+)", body))
        add_source(sources, match.group("reference"), title_match.group(1), strip_markdown(evidence))

    # Remaining subsections use tables. Repeated sources are merged by title.
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "Referência" or set(cells[0]) <= {"-", ":"}:
            continue
        reference, title = cells[0], cells[1]
        if (
            not title
            or title.startswith("Trechos")
            or title.startswith("Título")
            or normalized(title) == "mesmo titulo"
        ):
            continue
        add_source(sources, reference, title, strip_markdown(" | ".join(cells[2:])))

    # Walker is present in the historical pending section but was later obtained
    # and directly checked. Ghali is a book chapter, not one of the 81 papers.
    walker_key = next(
        (key for key in sources if key.startswith("towards including end users in the design of prosthetic hands")),
        "",
    )
    sources.pop(walker_key, None)
    ghali_key = next((key for key in sources if key.startswith("constructive solid geometry")), "")
    if not ghali_key:
        raise RuntimeError("Could not locate the Ghali book-chapter entry")
    ghali = sources.pop(ghali_key)

    # Mistarihi is the only new paper missing from the annex audit and therefore
    # does not appear in the body-only Section 4.
    add_source(
        sources,
        "Mistarihi (2020)",
        "A data set on anthropometric measurements and degree of discomfort of physically disabled workers for ergonomic requirements in work space design",
        "Anexo A: cinco ocorrências; PDF não localizado; sem correspondência Mendeley.",
    )

    result = sorted(sources.values(), key=lambda item: normalized(item.reference))
    if len(result) != 81:
        labels = "\n".join(f"- {item.reference}: {item.title}" for item in result)
        raise RuntimeError(f"Expected 81 missing papers, found {len(result)}:\n{labels}")
    return result, ghali


def parse_bibliography(manuscript_text: str) -> list[tuple[str, str, str]]:
    section = extract_section(manuscript_text, "## Bibliografia", "## Anexo A")
    entries: list[tuple[str, str, str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith('<a id="ref-'):
            continue
        anchor_match = re.match(r'<a id="([^"]+)"></a>\s*(.*)', line)
        if anchor_match:
            entries.append((anchor_match.group(1), anchor_match.group(2), normalized(anchor_match.group(2))))
    return entries


def best_bibliography_match(source: MissingSource, entries: list[tuple[str, str, str]]) -> str:
    key = title_key(source.title)
    exact = [entry for _, entry, entry_norm in entries if key and key in entry_norm]
    if len(exact) == 1:
        return exact[0]
    author, year = source_key(source.reference)
    candidates = [
        entry
        for anchor, entry, entry_norm in entries
        if year and anchor.endswith(f"-{year}") and author and author in normalized(anchor)
    ]
    if len(candidates) == 1:
        return candidates[0]
    # Fall back to the first-author/year pair in the entry text.
    candidates = [
        entry
        for _, entry, entry_norm in entries
        if year and f" {year} " in f" {entry_norm} " and author and entry_norm.startswith(author)
    ]
    return candidates[0] if len(candidates) == 1 else ""


def extract_doi(value: str) -> str:
    match = re.search(r"(?:https?://doi\.org/|doi:\s*)(10\.\d{4,9}/[^\s<>)\]]+)", value, flags=re.I)
    if not match:
        match = re.search(r"\b(10\.\d{4,9}/[^\s<>)\]]+)", value, flags=re.I)
    if not match:
        return ""
    doi = re.split(r"[?#&]", match.group(1), maxsplit=1)[0].rstrip(".,;")
    return re.sub(r"\.pdf$", "", doi, flags=re.I)


def extract_url(value: str) -> str:
    urls = re.findall(r"https?://[^\s<>)\]]+", value)
    for url in urls:
        url = url.rstrip(".,;")
        if "doi.org/" not in url and "semanticscholar.org/" not in url:
            return url
    return ""


def enrich_sources(sources: list[MissingSource], entries: list[tuple[str, str, str]]) -> None:
    for source in sources:
        source.bibliography = best_bibliography_match(source, entries)
        combined = " ".join([source.bibliography, *source.evidence])
        source.doi = extract_doi(combined) or VERIFIED_DOIS.get(title_key(source.title), "")
        source.source_url = extract_url(source.bibliography)


def destination(source: MissingSource) -> tuple[str, str]:
    if source.doi:
        return f"[https://doi.org/{source.doi}](https://doi.org/{source.doi})", "DOI identificado"
    if source.source_url:
        return f"[{source.source_url}]({source.source_url})", "URL bibliográfico; DOI não identificado"
    query = urllib.parse.quote(f'"{source.title}"')
    url = f"https://search.crossref.org/?q={query}"
    return f"[Pesquisar no Crossref]({url})", "DOI não identificado"


def short_evidence(source: MissingSource) -> str:
    if title_key(source.title) == title_key(
        "Prosthesis options and management in upper extremity amputation"
    ):
        return (
            "Foram localizados apenas o índice e a lista de colaboradores do volume 33(3), "
            "que confirmam o artigo 101061; o texto integral do artigo não está presente."
        )
    evidence = " ".join(source.evidence)
    evidence_folded = evidence.casefold()
    if (
        "file_attached" in evidence
        or "registo com anexo" in evidence_folded
        or "anexo não consultado" in evidence_folded
    ):
        return "Existe indicação de anexo Mendeley, mas não há PDF local validado."
    if "incorrecto" in evidence_folded or "incompatível" in evidence_folded:
        return "O ficheiro local associado contém outra publicação."
    return "PDF não localizado localmente nem obtido na auditoria."


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(sources: list[MissingSource], ghali: MissingSource, audit: Path, manuscript: Path) -> str:
    doi_count = sum(bool(source.doi) for source in sources)
    url_count = sum(bool(source.source_url and not source.doi) for source in sources)
    search_count = len(sources) - doi_count - url_count
    lines = [
        "# PDFs em falta — referências citadas",
        "",
        "Este é o registo autoritativo das fontes citadas na dissertação cujo texto integral não foi localizado em `material/` ou em `projecto_completo_bibliografia/` e não ficou disponível para confronto directo durante a auditoria bibliográfica.",
        "",
        f"Última verificação: {date.today().isoformat()}. A lista foi reconciliada com `docs/revisoes/auditoria_referencias_texto_papers_061.md` após consulta de 514 registos da API Mendeley.",
        "",
        "## Síntese",
        "",
        f"- *Papers* sem texto integral: **{len(sources)}**.",
        f"- Com DOI identificado: **{doi_count}**.",
        f"- Com URL bibliográfico, mas sem DOI identificado: **{url_count}**.",
        f"- Sem DOI ou URL bibliográfico confirmado: **{search_count}**; é fornecida uma pesquisa por título no Crossref, não um DOI presumido.",
        "- Os links DOI usam sempre a forma canónica `https://doi.org/...`.",
        "",
        "## Lista integral",
        "",
        "| N.º | Referência | Título | DOI ou localização provável | Estado |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for index, source in enumerate(sources, start=1):
        link, link_status = destination(source)
        title = source.title.replace("|", "\\|")
        reference = source.reference.replace("|", "\\|")
        state = f"{link_status}. {short_evidence(source)}"
        lines.append(f"| {index} | {reference} | *{title}* | {link} | {state} |")

    ghali_link, ghali_status = destination(ghali)
    lines.extend(
        [
            "",
            "## Documento académico não classificado como *paper*",
            "",
            "A auditoria identificou ainda um capítulo de livro sem texto integral. Não integra a contagem dos 81 *papers*, mas deve ser obtido para verificar a citação correspondente.",
            "",
            "| Referência | Título | DOI ou localização provável | Estado |",
            "| --- | --- | --- | --- |",
            f"| {ghali.reference} | *{ghali.title}* | {ghali_link} | {ghali_status}; capítulo de livro não localizado. |",
            "",
            "## Critério e rastreabilidade",
            "",
            "- A presença de um DOI nesta lista significa apenas que foi identificado na bibliografia, na auditoria ou nos metadados do editor, de um repositório ou de um índice bibliográfico; não significa que o PDF seja de acesso aberto.",
            "- Uma ligação «Pesquisar no Crossref» é uma pesquisa pelo título e não deve ser tratada como confirmação de DOI.",
            "- Walker et al. foi retirado da lista porque o texto integral foi posteriormente obtido e confrontado. Mistarihi (2020) foi acrescentado a partir do Anexo A.",
            "- Para Fink e Diamond (2023), os ficheiros locais `Table-of-Contents--pick-up-from-previous-is_2023_Operative-Techniques-in-Ort.pdf` e `Contributors--pick-up-from-previous-issue-_2023_Operative-Techniques-in-Orth.pdf` apenas identificam o artigo 101061; nenhum deles contém o texto integral.",
            "- Fontes normativas, páginas *web*, repositórios de código e conjuntos DINED sem PDF autónomo não são contabilizados como PDFs científicos em falta.",
            "",
            f"- SHA-256 do relatório de auditoria usado: `{sha256(audit)}`.",
            f"- SHA-256 do manuscrito usado: `{sha256(manuscript)}`.",
            "- Método de geração: `python3 tools/generate_missing_pdfs_report.py`.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", type=Path, default=DEFAULT_MANUSCRIPT)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    audit_text = args.audit.read_text(encoding="utf-8")
    manuscript_text = args.manuscript.read_text(encoding="utf-8")
    sources, ghali = parse_missing_sources(audit_text)
    entries = parse_bibliography(manuscript_text)
    enrich_sources([*sources, ghali], entries)
    args.output.write_text(render(sources, ghali, args.audit, args.manuscript), encoding="utf-8")
    print(f"Wrote {args.output} with {len(sources)} missing papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
