#!/usr/bin/env python3
"""Add internal links from inline citations to bibliography entries in Markdown."""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


BIBLIOGRAPHY_HEADING = "## Bibliografia"

# Manual disambiguations for author-year collisions that cannot be inferred
# safely from the inline citation text alone.
MANUAL_ALIASES = {
    "Romero et al., 2025": "ref-da-silveira-romero-2025",
    "Romero et al. (2025)": "ref-da-silveira-romero-2025",
}


@dataclass
class BibliographyEntry:
    text: str
    anchor: str
    aliases: set[str]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only.strip().lower()).strip("-")
    return slug or "entry"


def normalize_citation_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def split_document(text: str) -> tuple[str, str]:
    marker = f"\n{BIBLIOGRAPHY_HEADING}\n"
    if marker not in text:
        raise SystemExit(f"Missing bibliography heading: {BIBLIOGRAPHY_HEADING}")
    body, bibliography = text.split(marker, 1)
    return body, bibliography


def strip_existing_body_links(body: str) -> str:
    return re.sub(r"\[([^\]]+)\]\(#ref-[^)]+\)", r"\1", body)


def strip_existing_bibliography_markup(bibliography: str) -> str:
    lines: list[str] = []
    for line in bibliography.splitlines():
        if re.fullmatch(r'\s*<a id="ref-[^"]+"></a>\s*', line):
            continue
        lines.append(line)
    return "\n".join(lines)


def extract_entries(bibliography: str) -> list[str]:
    entries: list[str] = []
    current: list[str] = []
    for line in bibliography.splitlines():
        if line.strip():
            current.append(line)
            continue
        if current:
            entries.append("\n".join(current))
            current = []
    if current:
        entries.append("\n".join(current))
    return entries


def first_author_and_year(entry: str) -> tuple[str, str] | None:
    first_line = entry.splitlines()[0]
    match = re.match(r"(.+?)\s*\((\d{4})\)\.", first_line)
    if not match:
        return None
    return match.group(1).strip(), match.group(2)


def split_authors(author_text: str) -> list[str]:
    matches = re.findall(r"(?:^|, |& | e )([^,]+),\s*(?:[A-Z])", author_text)
    if matches:
        return [match.strip() for match in matches]

    protected = author_text.replace(", & ", "|||").replace(" & ", "|||").replace(" e ", "|||")
    return [part.strip() for part in protected.split("|||") if part.strip()]


def surname_from_author(author: str) -> str:
    if "," in author:
        return author.split(",", 1)[0].strip()
    return author.strip().rstrip(".")


def display_name_for_author(author: str) -> str:
    surname = surname_from_author(author)
    tokens = surname.split()
    if not tokens:
        return surname
    return tokens[-1]


def aliases_for_entry(author_text: str, year: str) -> set[str]:
    authors = split_authors(author_text)
    if not authors:
        return set()

    if len(authors) == 1:
        name = surname_from_author(authors[0])
        short = display_name_for_author(authors[0])
        if "," not in authors[0] and len(name.split()) > 1:
            # Institutional author
            return {
                f"{name}, {year}",
                f"{name} ({year})",
                f"{name.replace('&', 'e')}, {year}",
                f"{name.replace('&', 'e')} ({year})",
            }
        aliases = {f"{short}, {year}", f"{short} ({year})"}
        if name != short:
            aliases.update({f"{name}, {year}", f"{name} ({year})"})
        return aliases

    if len(authors) == 2:
        left_full = surname_from_author(authors[0])
        right_full = surname_from_author(authors[1])
        left = display_name_for_author(authors[0])
        right = display_name_for_author(authors[1])
        aliases = {
            f"{left} & {right}, {year}",
            f"{left} & {right} ({year})",
            f"{left} e {right}, {year}",
            f"{left} e {right} ({year})",
        }
        if left_full != left or right_full != right:
            aliases.update(
                {
                    f"{left_full} & {right_full}, {year}",
                    f"{left_full} & {right_full} ({year})",
                    f"{left_full} e {right_full}, {year}",
                    f"{left_full} e {right_full} ({year})",
                }
            )
        return aliases

    first_full = surname_from_author(authors[0])
    first = display_name_for_author(authors[0])
    aliases = {
        f"{first} et al., {year}",
        f"{first} et al. ({year})",
    }
    if first_full != first:
        aliases.update(
            {
                f"{first_full} et al., {year}",
                f"{first_full} et al. ({year})",
            }
        )
    return aliases


def build_entries(bibliography: str) -> list[BibliographyEntry]:
    entries: list[BibliographyEntry] = []
    for raw_entry in extract_entries(bibliography):
        parsed = first_author_and_year(raw_entry)
        if not parsed:
            entries.append(BibliographyEntry(text=raw_entry, anchor=f"ref-{slugify(raw_entry[:32])}", aliases=set()))
            continue
        author_text, year = parsed
        anchor = f"ref-{slugify(surname_from_author(split_authors(author_text)[0]))}-{year}"
        entries.append(
            BibliographyEntry(
                text=raw_entry,
                anchor=anchor,
                aliases=aliases_for_entry(author_text, year),
            )
        )
    return entries


def alias_map(entries: list[BibliographyEntry]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for entry in entries:
        for alias in entry.aliases:
            aliases.setdefault(normalize_citation_text(alias), entry.anchor)
    for alias, anchor in MANUAL_ALIASES.items():
        aliases[normalize_citation_text(alias)] = anchor
    return aliases


def link_parenthetical_citations(body: str, aliases: dict[str, str]) -> str:
    def replace_group(match: re.Match[str]) -> str:
        group = match.group(0)
        if "http" in group or "doi.org" in group:
            return group
        inner = group[1:-1]
        parts = [part.strip() for part in inner.split(";")]
        replaced: list[str] = []
        changed = False
        for part in parts:
            normalized_part = normalize_citation_text(part)
            target = aliases.get(normalized_part)
            if target:
                replaced.append(f"[{part}](#{target})")
                changed = True
            else:
                replaced.append(part)
        if not changed:
            return group
        return "(" + "; ".join(replaced) + ")"

    pattern = re.compile(r"\(([^()\n]*\d{4}[^()\n]*)\)")
    return pattern.sub(replace_group, body)


def link_narrative_citations(body: str, aliases: dict[str, str]) -> str:
    narrative_aliases = [alias for alias in aliases if "(" in alias and ")" in alias]
    for alias in sorted(narrative_aliases, key=len, reverse=True):
        target = aliases[alias]
        body = re.sub(
            rf"(?<!\[){re.escape(alias)}(?!\]\(#)",
            f"[{alias}](#{target})",
            body,
        )
    return body


def render_bibliography(entries: list[BibliographyEntry]) -> str:
    rendered: list[str] = []
    for entry in entries:
        rendered.append(f'<a id="{entry.anchor}"></a>')
        rendered.append(entry.text)
        rendered.append("")
    return "\n".join(rendered).rstrip() + "\n"


def process_markdown(text: str) -> str:
    body, bibliography = split_document(text)
    body = strip_existing_body_links(body)
    bibliography = strip_existing_bibliography_markup(bibliography)
    entries = build_entries(bibliography)
    aliases = alias_map(entries)
    linked_body = link_parenthetical_citations(body, aliases)
    linked_body = link_narrative_citations(linked_body, aliases)
    linked_bibliography = render_bibliography(entries)
    return f"{linked_body}\n{BIBLIOGRAPHY_HEADING}\n\n{linked_bibliography}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add internal citation-to-bibliography links to a Markdown document.")
    parser.add_argument("input", type=Path, help="Markdown file to update in place.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.input.expanduser().resolve()
    text = path.read_text(encoding="utf-8")
    path.write_text(process_markdown(text), encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
