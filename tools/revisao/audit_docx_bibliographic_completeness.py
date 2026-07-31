#!/usr/bin/env python3
"""Audit citation-to-reference completeness in the canonical DOCX.

The DOCX is the sole citation authority.  The Markdown mirror is deliberately
not read.  The audit decodes live Mendeley controls, parses the materialised
Word bibliography, detects manually written attributions and records the
small set of source-identity conflicts that require human bibliographic
judgement.
"""

from __future__ import annotations

import argparse
import base64
import difflib
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
DEFAULT_REPORT = (
    ROOT / "docs/revisoes/bibliografia/auditoria_completude_bibliografica_docx_0_4_112.md"
)

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
MENDELEY_CITATION_PREFIX = "MENDELEY_CITATION_v3_"
MENDELEY_BIBLIOGRAPHY_PREFIX = "MENDELEY_BIBLIOGRAPHY"

STOPWORDS = {
    "a",
    "an",
    "and",
    "article",
    "as",
    "for",
    "from",
    "in",
    "of",
    "on",
    "part",
    "proceedings",
    "the",
    "to",
    "vol",
    "volume",
    "with",
}

# Mendeley records whose visible author-year label currently has no coherent
# counterpart in the materialised DOCX bibliography.  Each item was inspected
# against its embedded CSL metadata and the body passage in which it occurs.
SOURCE_IDENTITY_ISSUES = {
    "02570bfd-49a3-3157-8d0e-9b7583534869": (
        "alvo de citação incompatível",
        "O controlo aponta para o artigo de Østlie et al. (2011), mas a passagem, "
        "a legenda e a bibliografia usam o estudo distinto de Østlie et al. (2012).",
    ),
    "3efcdd41-7315-3bd3-be78-ae28d50a6612": (
        "entrada ausente",
        "O Regulamento (UE) 2017/745 é citado duas vezes, mas não possui entrada "
        "na bibliografia materializada do DOCX.",
    ),
    "b21e0e62-2b43-3c80-8f12-d4ed24572eea": (
        "alvo de citação incompatível",
        "O controlo aponta para Resnik et al. (2022), sobre satisfação com próteses, "
        "enquanto a passagem regulatória e a bibliografia correspondem a Resnik et al. (2010).",
    ),
    "db475489-60f4-3495-ae9e-3bb529fb2944": (
        "alvo de citação incompatível",
        "O controlo contém a ISO 8549-3:2020, relativa a ortóteses; o texto e a "
        "bibliografia invocam a ISO 8549-1:2020.",
    ),
    "f01624c1-21db-3080-95a2-ba9cfa4f2463": (
        "entrada ausente",
        "Li et al. (2020), DOI 10.1017/dsd.2020.273, é citado, mas não possui "
        "entrada bibliográfica.",
    ),
    "d7bbc303-4164-3475-bfae-7db1006bbed7": (
        "entrada ausente",
        "Mikołajewska e Mikołajewski (2014), DOI 10.2478/s11536-013-0254-6, "
        "é citado, mas não possui entrada bibliográfica.",
    ),
    "cb84651b-cbaa-3385-90e4-46913f2db71d": (
        "entrada ausente",
        "The Design Council (2007), *The Double Diamond*, é citado; a bibliografia "
        "contém apenas a fonte institucional distinta do Design Council (2020).",
    ),
    "a2836313-ad42-3238-8ab2-943ecfb32af2": (
        "entrada ausente e colisão autor–ano",
        "Biddiss e Chau (2007), DOI 10.1080/03093640600994581, é uma obra "
        "distinta da entrada Biddiss, Beaton e Chau (2007) já existente.",
    ),
    "35f97957-bba4-3b0d-b0d3-557adbe94641": (
        "alvo de citação incompatível",
        "O controlo de Gonzalez Avila (2024) contém *Faciliting programming based "
        "3D Computer-aided design using bidirectional programming*, mas a entrada "
        "bibliográfica corresponde a *Understanding the challenges of OpenSCAD users for 3D printing*.",
    ),
}

# These year discrepancies are not inferred from title similarity: the cited
# record and the bibliography were already paired by DOI, title, author set or
# the earlier source audit.  They therefore remain explicit and reviewable.
YEAR_ISSUES = {
    "3793cba7-b3b4-3f3b-bc23-33d95d6ae016": ("2018", "van Niekerk et al."),
    "ce809d93-3338-3a25-ad8b-56ad8e4fb9b2": ("2022", "Howard, Fisher, et al."),
    "467e30ae-97a2-3c10-a268-d11fe98d839a": ("2022", "Howard, Davies, et al."),
    "a3dee2a6-07fc-3124-ae56-75d9e9b08f7d": ("2020", "Kuhl et al."),
    "01554c94-531e-30af-b157-c42df1c2cb0d": ("2023", "Thorsen et al."),
    "1a2295d2-4d2f-3af4-9026-0c52b605b186": ("2016", "Frangos et al."),
    "cc63e55d-8a2b-3d0a-80a5-545f4d18c383": ("2022", "Marinelli et al."),
    "d90b8563-bae7-33b0-9722-0ed4ef7d80a8": ("2025", "Henao et al."),
    "40d870bf-ed0a-35ee-bed5-1e3c9c937214": ("2026", "ELhadad et al."),
    "8bc5d517-64f4-3003-ac69-215d38612f5e": ("2020", "Barredo Arrieta et al."),
    "8caca03a-e0a3-3277-9d13-e43b652fc727": ("2015", "Gordon et al."),
}

# Curated equivalences used only to avoid false orphan classifications when a
# Mendeley record describes a containing volume, repeats a title or contains a
# historical metadata defect.  Identity problems listed above are not hidden
# by this map.
CURATED_BIBLIOGRAPHY_MATCHES = {
    "059eb607-af35-3d39-b673-99f86afd8715": "Brooks, C.",
    "1cb4c4dd-c471-35ad-a5f2-5e2383832828": "Fischer, G., Fogli",
    "216ce21f-22a6-35cd-a0f1-f6835714919d": "Sims, T.",
    "29afdb93-a366-311b-89b4-06aae0cc885f": "Silva, L. A. da",
    "3793cba7-b3b4-3f3b-bc23-33d95d6ae016": "van Niekerk, K.",
    "40d870bf-ed0a-35ee-bed5-1e3c9c937214": "ELhadad, N.",
    "602be58a-8168-34f4-adc7-a6b5cd40622a": "Guo, M.",
    "6400540d-14d9-394a-97df-bdd6324bfaed": "Costabile, M. F.",
    "7762cae9-873d-3817-a4ca-7c698c285867": "Millet, A.",
    "a3dee2a6-07fc-3124-ae56-75d9e9b08f7d": "Kuhl, M.",
    "ab2cc864-94ee-30e7-9f59-ad7e4f4e088a": "International Electrotechnical Commission.",
    "c436ae9b-8dea-36a9-a4d8-00c767eab0d1": "Burnap, A.",
    "cf048cd3-259e-31df-a6a1-2493d3bc2136": "Fischer, G., Giaccardi",
    "d0c66a10-d96d-3c69-9cc2-248ed8560630": "Herbst, Y.",
    "d46ebaa4-3cb9-3288-9db8-3028c7a39a24": "Cole, E.",
    "f6ce7567-8cf7-3727-ab01-58ef49ca49d2": "Silva, L. A. da",
    "fac41718-05f8-31a3-b1d7-c350af0f844f": "Menaka, S.",
}

MANUAL_ATTRIBUTION_ISSUES = (
    (
        "M. Mendenhall (2020)",
        "entrada ausente",
        "A origem do Paraglider/Flexible Flyer é indicada em formato autor–ano, "
        "mas não existe referência completa.",
    ),
    (
        "Fonte: artigo metodológico sobre reconstrução de modelos corporais 3D",
        "citação e entrada ausentes",
        "A fonte foi identificada como Zhou et al. (2016), DOI "
        "10.1016/j.ergon.2015.10.007, mas continua anónima no Anexo A.",
    ),
    (
        "MakerBlock/e-NABLE; CC BY-NC-SA 3.0",
        "referência técnica incompleta",
        "A atribuição do Cyborg Beast não identifica URL, versão, revisão nem "
        "uma entrada bibliográfica completa.",
    ),
    (
        "UnLimbited/e-NABLE; CC BY-NC-SA 4.0",
        "referência técnica incompleta",
        "A atribuição deve identificar Stephen Robert Davies, Drew Murray, Team "
        "UnLimbited, a versão V1.0, o URL e a revisão consultada.",
    ),
)

INFORMALLY_USED_REFERENCES = {
    "Base local consolidada de dados antropométricos da mão e do membro superior distal.",
    "daprice.",
}


@dataclass
class BibliographyEntry:
    paragraph: int
    text: str
    author: str
    year: str
    title: str
    doi: str


@dataclass
class MendeleyItem:
    identifier: str
    data: dict
    occurrences: int
    displays: tuple[str, ...]


@dataclass(frozen=True)
class PlainCitation:
    paragraph: int
    label: str
    year: str
    context: str


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def tokens(value: str) -> set[str]:
    return set(norm(value).split()) - STOPWORDS


def title_score(title: str, entry: str) -> float:
    left = tokens(title)
    right = tokens(entry)
    coverage = len(left & right) / len(left) if left else 0.0
    sequence = difflib.SequenceMatcher(None, norm(title), norm(entry)).ratio()
    return max(coverage, sequence)


def extract_doi(value: str) -> str:
    match = re.search(r"(?:https?://doi\.org/)?(10\.\d{4,9}/[^\s<>)\]]+)", value, re.I)
    return match.group(1).rstrip(".,;").casefold() if match else ""


def issued_year(item: dict) -> str:
    parts = (item.get("issued") or {}).get("date-parts") or []
    return str(parts[0][0]) if parts and parts[0] else "?"


def parse_bibliography_entry(paragraph: int, value: str) -> BibliographyEntry:
    match = re.search(
        r"\(((?:19|20)\d{2}|n\.d\.)(?:-[a-z])?(?:,\s*[^)]*)?\)\.\s+",
        value,
        re.I,
    )
    if not match:
        raise RuntimeError(f"Entrada bibliográfica sem ano reconhecível no parágrafo {paragraph}: {value}")
    author = value[: match.start()].rstrip(". ")
    year = match.group(1).casefold()
    rest = value[match.end() :]
    protected = rest.replace("U.S.", "U§S§")
    title = re.split(
        r"\.\s+(?=[A-ZÀ-ÖØ-Þ\[])|\.\s+https?://",
        protected,
        maxsplit=1,
    )[0].replace("U§S§", "U.S.").rstrip(". ")
    return BibliographyEntry(
        paragraph=paragraph,
        text=value,
        author=author,
        year=year,
        title=title,
        doi=extract_doi(value),
    )


def load_docx(path: Path) -> tuple[etree._Element, etree._Element]:
    with ZipFile(path) as archive:
        return (
            etree.fromstring(archive.read("word/document.xml")),
            etree.fromstring(archive.read("word/footnotes.xml")),
        )


def bibliography(
    root: etree._Element,
) -> tuple[list[BibliographyEntry], int, int, list[int]]:
    paragraphs = root.xpath("//w:body//w:p", namespaces=NS)
    start = next(
        index
        for index, paragraph in enumerate(paragraphs)
        if text_of(paragraph) == "Referências Bibliográficas"
    )
    end = next(
        index
        for index in range(start + 1, len(paragraphs))
        if text_of(paragraphs[index]).startswith("Anexo A —")
    )
    logical: list[tuple[int, str]] = []
    continuations: list[int] = []
    for index in range(start + 1, end):
        value = text_of(paragraphs[index])
        if not value:
            continue
        if re.match(r"^https?://", value, re.I) and logical:
            prior_index, prior_value = logical[-1]
            logical[-1] = (prior_index, f"{prior_value} {value}")
            continuations.append(index)
        else:
            logical.append((index, value))
    return (
        [parse_bibliography_entry(index, value) for index, value in logical],
        start,
        end,
        continuations,
    )


def decode_mendeley(root: etree._Element) -> tuple[int, int, dict[str, MendeleyItem]]:
    controls = 0
    occurrences: Counter[str] = Counter()
    item_data: dict[str, dict] = {}
    displays: defaultdict[str, set[str]] = defaultdict(set)
    for control in root.xpath("//w:sdt", namespaces=NS):
        tags = control.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
        if not tags or not tags[0].startswith(MENDELEY_CITATION_PREFIX):
            continue
        controls += 1
        payload = tags[0][len(MENDELEY_CITATION_PREFIX) :]
        payload += "=" * ((4 - len(payload) % 4) % 4)
        decoded = json.loads(base64.urlsafe_b64decode(payload))
        display = html.unescape(text_of(control))
        for citation_item in decoded.get("citationItems", []):
            data = citation_item.get("itemData", {})
            identifier = data.get("id") or citation_item.get("id")
            if not identifier:
                raise RuntimeError("Item Mendeley sem identificador")
            item_data[identifier] = data
            occurrences[identifier] += 1
            displays[identifier].add(display)
    items = {
        identifier: MendeleyItem(
            identifier=identifier,
            data=data,
            occurrences=occurrences[identifier],
            displays=tuple(sorted(displays[identifier])),
        )
        for identifier, data in item_data.items()
    }
    return controls, sum(occurrences.values()), items


def item_matches(
    items: dict[str, MendeleyItem],
    entries: list[BibliographyEntry],
) -> dict[str, int]:
    matches: dict[str, int] = {}
    for identifier, item in items.items():
        if identifier in SOURCE_IDENTITY_ISSUES:
            continue
        doi = extract_doi(item.data.get("DOI", ""))
        exact_doi = [
            index
            for index, entry in enumerate(entries)
            if doi and entry.doi and doi == entry.doi
        ]
        if len(exact_doi) == 1:
            matches[identifier] = exact_doi[0]
            continue
        ranked = sorted(
            (
                (title_score(item.data.get("title", ""), entry.text), index)
                for index, entry in enumerate(entries)
            ),
            reverse=True,
        )
        if ranked and ranked[0][0] >= 0.75:
            matches[identifier] = ranked[0][1]
            continue
        prefix = CURATED_BIBLIOGRAPHY_MATCHES.get(identifier)
        if prefix:
            candidates = [
                index for index, entry in enumerate(entries) if entry.text.startswith(prefix)
            ]
            if len(candidates) == 1:
                matches[identifier] = candidates[0]
    return matches


def content_paragraphs(
    root: etree._Element,
    bibliography_start: int,
    bibliography_end: int,
) -> list[tuple[int, str]]:
    paragraphs = root.xpath("//w:body//w:p", namespaces=NS)
    result: list[tuple[int, str]] = []
    for index, paragraph in enumerate(paragraphs):
        if bibliography_start <= index < bibliography_end:
            continue
        style = " ".join(
            paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        ).casefold()
        if "ndice" in style:
            continue
        value = norm(text_of(paragraph))
        if value:
            result.append((index, value))
    return result


def text_without_mendeley_citations(paragraph: etree._Element) -> str:
    cleaned = deepcopy(paragraph)
    for control in cleaned.xpath(".//w:sdt", namespaces=NS):
        tags = control.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
        if tags and tags[0].startswith(MENDELEY_CITATION_PREFIX):
            parent = control.getparent()
            if parent is not None:
                parent.remove(control)
    return text_of(cleaned)


def context_excerpt(value: str, start: int, end: int, radius: int = 180) -> str:
    left = max(0, start - radius)
    right = min(len(value), end + radius)
    prefix = "…" if left else ""
    suffix = "…" if right < len(value) else ""
    return f"{prefix}{value[left:right].strip()}{suffix}"


def plain_author_year_citations(
    root: etree._Element,
    bibliography_start: int,
    bibliography_end: int,
) -> list[PlainCitation]:
    """Find author-year mentions written directly in Word.

    Text held inside Mendeley citation controls is removed first because those
    sources are decoded from their embedded CSL metadata elsewhere.
    """

    paragraphs = root.xpath("//w:body//w:p", namespaces=NS)
    citations: set[PlainCitation] = set()
    narrative = re.compile(
        r"(?<![\wÀ-ÿ])"
        r"(?P<label>(?:[A-ZÀ-Ý][\wÀ-ÿ'’\-]+|[A-Z]\.)"
        r"(?:\s+(?:&|e|et|al\.|[A-ZÀ-Ý][\wÀ-ÿ'’\-]+|[A-Z]\.)){0,5})"
        r"\s*\((?P<year>(?:19|20)\d{2})[a-z]?\)"
    )
    parenthetical_group = re.compile(r"\((?P<group>[^()\n]{1,500})\)")
    parenthetical_item = re.compile(
        r"^\s*(?P<label>[A-ZÀ-Ý][^,;()]{1,120}?),\s*"
        r"(?P<year>(?:19|20)\d{2})[a-z]?\b(?![–-]\d)"
    )
    for index, paragraph in enumerate(paragraphs):
        if bibliography_start <= index < bibliography_end:
            continue
        style = " ".join(
            paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        ).casefold()
        if "ndice" in style:
            continue
        value = text_without_mendeley_citations(paragraph)
        if not value:
            continue
        for match in narrative.finditer(value):
            if len(norm(match.group("label"))) < 3:
                continue
            citations.add(
                PlainCitation(
                    paragraph=index,
                    label=match.group("label").strip(),
                    year=match.group("year"),
                    context=context_excerpt(value, match.start(), match.end()),
                )
            )
        for group_match in parenthetical_group.finditer(value):
            for segment in group_match.group("group").split(";"):
                match = parenthetical_item.match(segment)
                if not match:
                    continue
                citations.add(
                    PlainCitation(
                        paragraph=index,
                        label=match.group("label").strip(),
                        year=match.group("year"),
                        context=context_excerpt(
                            value, group_match.start(), group_match.end()
                        ),
                    )
                )
    return sorted(citations, key=lambda citation: (citation.paragraph, citation.label))


def classify_plain_citations(
    citations: list[PlainCitation],
    entries: list[BibliographyEntry],
) -> tuple[list[PlainCitation], list[PlainCitation]]:
    unmatched: list[PlainCitation] = []
    year_conflicts: list[PlainCitation] = []
    for citation in citations:
        label = norm(citation.label)
        author_matches: list[BibliographyEntry] = []
        for entry in entries:
            first_author = norm(entry.author.split(",", maxsplit=1)[0])
            surname = first_author.split()[-1] if first_author else ""
            full_author_match = bool(
                first_author
                and re.search(
                    rf"(?:^|\s){re.escape(first_author)}(?:$|\s)",
                    label,
                )
            )
            surname_match = bool(
                surname
                and len(surname) > 2
                and label.split()
                and label.split()[-1] == surname
            )
            if first_author and (
                full_author_match
                or label.endswith(first_author)
                or surname_match
            ):
                author_matches.append(entry)
        if not author_matches:
            unmatched.append(citation)
        elif not any(entry.year == citation.year for entry in author_matches):
            year_conflicts.append(citation)
    return unmatched, year_conflicts


def potential_orphans(
    entries: list[BibliographyEntry],
    matches: dict[str, int],
    content: list[tuple[int, str]],
) -> list[BibliographyEntry]:
    used = set(matches.values())
    for index, entry in enumerate(entries):
        if index in used or any(entry.text.startswith(prefix) for prefix in INFORMALLY_USED_REFERENCES):
            used.add(index)
            continue
        first_author = norm(entry.author.split(",", maxsplit=1)[0])
        title = norm(entry.title)
        for _, paragraph in content:
            if entry.year == "n.d.":
                if (
                    first_author
                    and len(first_author) > 4
                    and first_author in paragraph
                    or title
                    and len(title) > 12
                    and title in paragraph
                ):
                    used.add(index)
                    break
            elif (
                norm(entry.year) in paragraph
                and first_author
                and re.search(rf"\b{re.escape(first_author)}\b", paragraph)
            ):
                used.add(index)
                break
    return [entry for index, entry in enumerate(entries) if index not in used]


def manual_issues(
    root: etree._Element,
    entries: list[BibliographyEntry],
) -> list[tuple[int, str, str, str]]:
    paragraphs = root.xpath("//w:body//w:p", namespaces=NS)
    bibliography_text = "\n".join(entry.text for entry in entries)
    found: list[tuple[int, str, str, str]] = []
    for marker, classification, explanation in MANUAL_ATTRIBUTION_ISSUES:
        locations = [
            index for index, paragraph in enumerate(paragraphs) if marker in text_of(paragraph)
        ]
        if not locations:
            raise RuntimeError(f"Marcador manual não localizado no DOCX: {marker}")
        if marker.startswith("M. Mendenhall") and "Mendenhall," in bibliography_text:
            continue
        if marker.startswith("Fonte: artigo") and "Zhou," in bibliography_text:
            continue
        found.append((locations[0], marker, classification, explanation))
    return found


def display_anomalies(items: dict[str, MendeleyItem]) -> list[tuple[int, str, str]]:
    displays: Counter[str] = Counter()
    for item in items.values():
        for display in item.displays:
            displays[display] += 1
    anomalies: list[tuple[int, str, str]] = []
    for display, count in displays.items():
        reasons: list[str] = []
        if display.count("(") != display.count(")"):
            reasons.append("parênteses desequilibrados")
        if "sem data" in display.casefold():
            reasons.append("ano apresentado como «sem data»")
        if re.search(r"\bet al\.,\s*\(", display):
            reasons.append("vírgula indevida antes do ano")
        if display and display[0].islower():
            reasons.append("início truncado")
        if ";" in display and not display.startswith("(") and display.endswith(")"):
            reasons.append("abertura do grupo ausente")
        if reasons:
            anomalies.append((count, display, "; ".join(reasons)))
    return sorted(anomalies, key=lambda item: (item[2], item[1]))


def bibliography_integrity(
    root: etree._Element,
    entries: list[BibliographyEntry],
) -> tuple[int, list[str], list[str]]:
    bibliography_controls = 0
    for control in root.xpath("//w:sdt", namespaces=NS):
        tags = control.xpath("./w:sdtPr/w:tag/@w:val", namespaces=NS)
        if tags and tags[0].startswith(MENDELEY_BIBLIOGRAPHY_PREFIX):
            bibliography_controls += 1
    duplicate_dois: list[str] = []
    doi_counts = Counter(entry.doi for entry in entries if entry.doi)
    duplicate_dois.extend(doi for doi, count in doi_counts.items() if count > 1)
    duplicate_titles: list[str] = []
    title_counts = Counter(norm(entry.title) for entry in entries if entry.title)
    duplicate_titles.extend(title for title, count in title_counts.items() if count > 1)
    return bibliography_controls, duplicate_dois, duplicate_titles


def source_issue_rows(items: dict[str, MendeleyItem]) -> list[tuple[MendeleyItem, str, str]]:
    rows: list[tuple[MendeleyItem, str, str]] = []
    for identifier, (classification, explanation) in SOURCE_IDENTITY_ISSUES.items():
        if identifier not in items:
            raise RuntimeError(f"Item Mendeley auditado deixou de existir: {identifier}")
        rows.append((items[identifier], classification, explanation))
    return rows


def year_issue_rows(items: dict[str, MendeleyItem]) -> list[tuple[MendeleyItem, str, str]]:
    rows: list[tuple[MendeleyItem, str, str]] = []
    for identifier, (bibliography_year, label) in YEAR_ISSUES.items():
        if identifier not in items:
            raise RuntimeError(f"Item Mendeley com ano auditado deixou de existir: {identifier}")
        rows.append((items[identifier], bibliography_year, label))
    return rows


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render(
    docx: Path,
    root: etree._Element,
    footnotes: etree._Element,
    entries: list[BibliographyEntry],
    bibliography_start: int,
    bibliography_end: int,
    continuations: list[int],
    controls: int,
    item_occurrences: int,
    items: dict[str, MendeleyItem],
    matches: dict[str, int],
    orphans: list[BibliographyEntry],
    manual: list[tuple[int, str, str, str]],
    plain_citations: list[PlainCitation],
    unmatched_plain: list[PlainCitation],
    plain_year_conflicts: list[PlainCitation],
) -> str:
    source_rows = source_issue_rows(items)
    year_rows = year_issue_rows(items)
    anomalies = display_anomalies(items)
    bibliography_controls, duplicate_dois, duplicate_titles = bibliography_integrity(
        root, entries
    )
    comments = int(root.xpath("count(//w:commentReference)", namespaces=NS))
    footnote_refs = int(root.xpath("count(//w:footnoteReference)", namespaces=NS))
    footnote_defs = len(footnotes.xpath("//w:footnote[number(@w:id) > 0]", namespaces=NS))
    unresolved_count = len(source_rows) + len(manual)
    lines = [
        "# Auditoria da completude bibliográfica do DOCX canónico",
        "",
        f"- Documento: `{docx.relative_to(ROOT)}`",
        f"- SHA-256: `{hashlib.sha256(docx.read_bytes()).hexdigest()}`",
        "- Fonte autoritativa das citações: **DOCX canónico**; o Markdown não foi lido.",
        f"- Intervalo materializado da bibliografia: parágrafos XML {bibliography_start + 1}–{bibliography_end - 1}.",
        f"- Entradas bibliográficas lógicas: **{len(entries)}**.",
        f"- Controlos de citação Mendeley: **{controls}**.",
        f"- Itens citados nos controlos: **{item_occurrences} ocorrências; {len(items)} fontes únicas**.",
        f"- Menções autor–ano fora dos controlos Mendeley: **{len(plain_citations)}**.",
        f"- Notas de rodapé: **{footnote_refs} referências; {footnote_defs} definições**.",
        f"- Comentários: **{comments}**.",
        "",
        "## Veredicto",
        "",
        "**A bibliografia do DOCX não está completa nem internamente coerente.** "
        f"Foram confirmadas {unresolved_count} lacunas ou incompatibilidades de fonte: "
        f"{len(source_rows)} fontes vivas sem entrada coerente ou ligadas à obra errada "
        f"e {len(manual)} atribuições manuais sem formalização bibliográfica suficiente. "
        f"Acrescem {len(year_rows)} divergências de ano, anomalias formais nas citações "
        "e problemas materiais na lista de referências; estes pontos também impedem "
        "a aprovação da completude bibliográfica.",
        "",
        "A disponibilidade local de PDFs é uma dimensão separada. Deve ser lida em "
        "`material/bibliografia/consolidacao_referencias_docx.md`, gerado directamente "
        "a partir desta mesma bibliografia do Word.",
        "",
        "## 1. Fontes vivas sem entrada coerente ou com alvo incompatível",
        "",
        "| Ocorrências | Citação apresentada | Fonte incorporada no Mendeley | Classificação | Diagnóstico |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for item, classification, explanation in source_rows:
        title = item.data.get("title", "")
        lines.append(
            f"| {item.occurrences} | {esc(' / '.join(item.displays))} | "
            f"*{esc(title)}* | {classification} | {esc(explanation)} |"
        )
    lines.extend(
        [
            "",
            "## 2. Atribuições manuais sem formalização suficiente",
            "",
            "| Parágrafo XML | Marcador localizado | Classificação | Diagnóstico |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for paragraph, marker, classification, explanation in manual:
        lines.append(
            f"| {paragraph} | `{esc(marker)}` | {classification} | {esc(explanation)} |"
        )
    lines.extend(
        [
            "",
            "O varrimento automático das menções autor–ano escritas directamente no "
            f"Word encontrou **{len(plain_citations)}** ocorrências fora dos controlos "
            f"Mendeley; foram identificadas **{len(unmatched_plain)}** sem autor "
            "correspondente na bibliografia materializada e "
            f"**{len(plain_year_conflicts)}** com autor correspondente, mas ano "
            "divergente:",
            "",
            "| Estado | Parágrafo XML | Menção | Contexto |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for citation in unmatched_plain:
        lines.append(
            f"| autor ausente | {citation.paragraph} | "
            f"{esc(citation.label)} ({citation.year}) | "
            f"{esc(citation.context)} |"
        )
    for citation in plain_year_conflicts:
        lines.append(
            f"| ano divergente | {citation.paragraph} | "
            f"{esc(citation.label)} ({citation.year}) | "
            f"{esc(citation.context)} |"
        )
    lines.extend(
        [
            "",
            "## 3. Anos apresentados que divergem da entrada bibliográfica auditada",
            "",
            "| Fonte | Ano incorporado | Ano bibliográfico auditado | Citações apresentadas |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for item, bibliography_year, label in year_rows:
        lines.append(
            f"| {label} | {issued_year(item.data)} | {bibliography_year} | "
            f"{esc(' / '.join(item.displays))} |"
        )
    lines.extend(
        [
            "",
            "## 4. Integridade material da lista bibliográfica",
            "",
            f"- Controlos Mendeley de bibliografia encontrados: **{bibliography_controls}**; "
            "o controlo existente está vazio e as entradas são parágrafos normais, pelo que "
            "um *Refresh* não garante a preservação da lista actual.",
            f"- Parágrafos autónomos que são continuação por URL/DOI: **{len(continuations)}** "
            f"({', '.join(map(str, continuations))}).",
            f"- DOI duplicados: **{len(duplicate_dois)}**.",
            f"- Títulos normalizados duplicados: **{len(duplicate_titles)}**.",
            "- A entrada da IEC 62366-1:2015 está mutilada: «International "
            "Electrotechnical Commission. (2015). Internacional» seguida do URL.",
            "",
            "## 5. Entradas potencialmente órfãs",
            "",
            "A lista seguinte é conservadora: exclui as correspondências por DOI/título "
            "dos itens Mendeley e as citações autor–ano detectadas fora da bibliografia. "
            "Exige decisão humana porque alguns recursos técnicos podem ser mencionados "
            "sem a forma autor–ano.",
            "",
            "| Parágrafo XML | Entrada |",
            "| ---: | --- |",
        ]
    )
    for entry in orphans:
        lines.append(f"| {entry.paragraph} | {esc(entry.text)} |")
    lines.extend(
        [
            "",
            "## 6. Anomalias formais nas citações Mendeley",
            "",
            "| Itens citados no grupo | Texto apresentado | Anomalia |",
            "| ---: | --- | --- |",
        ]
    )
    for count, display, reason in anomalies:
        lines.append(f"| {count} | `{esc(display)}` | {reason} |")
    lines.extend(
        [
            "",
            "## 7. Critério de aprovação",
            "",
            "A completude só poderá ser aprovada quando:",
            "",
            "1. cada fonte viva tiver uma única entrada correspondente à obra efectivamente citada;",
            "2. as atribuições de Zhou, Mendenhall, MakerBlock e Team UnLimbited estiverem formalizadas;",
            "3. os anos das citações e das entradas estiverem uniformizados;",
            "4. as entradas potencialmente órfãs forem citadas justificadamente ou removidas;",
            "5. a bibliografia deixar de conter entradas mutiladas ou continuações autónomas;",
            "6. a auditoria for repetida sobre o DOCX final e não devolver problemas impeditivos.",
            "",
            "## 8. Método reproduzível",
            "",
            "```bash",
            "python3 tools/revisao/audit_docx_bibliographic_completeness.py",
            "python3 tools/bibliografia/consolidate_docx_referenced_pdfs.py --apply",
            "```",
            "",
            f"Itens Mendeley automaticamente associados a entradas: **{len(matches)} de {len(items)}**; "
            "as nove excepções de identidade são mantidas fora desta contagem por decisão auditada.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root, footnotes = load_docx(args.docx)
    entries, bibliography_start, bibliography_end, continuations = bibliography(root)
    controls, item_occurrences, items = decode_mendeley(root)
    matches = item_matches(items, entries)
    content = content_paragraphs(root, bibliography_start, bibliography_end)
    orphans = potential_orphans(entries, matches, content)
    manual = manual_issues(root, entries)
    plain_citations = plain_author_year_citations(
        root, bibliography_start, bibliography_end
    )
    unmatched_plain, plain_year_conflicts = classify_plain_citations(
        plain_citations, entries
    )
    report = render(
        args.docx,
        root,
        footnotes,
        entries,
        bibliography_start,
        bibliography_end,
        continuations,
        controls,
        item_occurrences,
        items,
        matches,
        orphans,
        manual,
        plain_citations,
        unmatched_plain,
        plain_year_conflicts,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(
        f"Wrote {args.output}: {len(entries)} references, {controls} citation controls, "
        f"{len(items)} unique Mendeley items, "
        f"{len(SOURCE_IDENTITY_ISSUES) + len(manual)} blocking issues."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
