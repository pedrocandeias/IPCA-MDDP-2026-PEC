#!/usr/bin/env python3
"""Audita lexicalmente o DOCX canónico com o LanguageTool oficial em modo local.

O manuscrito não é alterado nem enviado para serviços externos. O relatório conserva
a localização e o contexto dos avisos lexicais para validação humana posterior.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
DEFAULT_OUTPUT = Path("/tmp/languagetool_resultado_bruto.md")
DEFAULT_LT_HOME = Path("/tmp/languagetool-6.6/LanguageTool-6.6")
DEFAULT_JAVA = Path(
    "/snap/libreoffice/current/usr/lib/jvm/java-21-openjdk-amd64/bin/java"
)
TEMP_TEXT = Path("/tmp/languagetool-docx-audit.txt")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
SOURCE_PREFIXES = (
    "Fonte:",
    "Reproduzido de",
    "Adaptado de",
    "Produção própria",
)


@dataclass
class Paragraph:
    number: int
    text: str


@dataclass
class Span:
    start: int
    end: int
    paragraph: Paragraph


def extract_paragraphs(path: Path) -> list[Paragraph]:
    with ZipFile(path) as source:
        document = etree.fromstring(source.read("word/document.xml"))

    paragraphs: list[Paragraph] = []
    in_abstract = False
    in_bibliography = False
    for number, element in enumerate(document.xpath("//w:p", namespaces=NS), start=1):
        text = "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()
        if not text:
            continue
        if text.upper() == "ABSTRACT":
            in_abstract = True
            continue
        if text in {"Lista de acrónimos", "Lista de Abreviaturas e/ou Siglas"}:
            in_abstract = False
        if text in {"Bibliografia", "Referências Bibliográficas"}:
            in_bibliography = True
            continue
        if text.startswith("Anexo A —") and not text[-1:].isdigit():
            in_bibliography = False
        if in_abstract or in_bibliography:
            continue
        if text.startswith(SOURCE_PREFIXES):
            continue
        if re.fullmatch(r"https?://\S+", text):
            continue
        paragraphs.append(Paragraph(number=number, text=text))
    return paragraphs


def join_paragraphs(paragraphs: list[Paragraph]) -> tuple[str, list[Span]]:
    parts: list[str] = []
    spans: list[Span] = []
    offset = 0
    for paragraph in paragraphs:
        parts.append(paragraph.text)
        spans.append(
            Span(start=offset, end=offset + len(paragraph.text), paragraph=paragraph)
        )
        parts.append("\n\n")
        offset += len(paragraph.text) + 2
    return "".join(parts), spans


def run_languagetool(
    text: str, java: Path, lt_home: Path
) -> tuple[dict[str, object], str]:
    jar = lt_home / "languagetool-commandline.jar"
    if not java.is_file():
        raise RuntimeError(f"Java não encontrado: {java}")
    if not jar.is_file():
        raise RuntimeError(f"LanguageTool não encontrado: {jar}")
    TEMP_TEXT.write_text(text, encoding="utf-8")
    command = [
        str(java),
        "-jar",
        str(jar),
        "-l",
        "pt-PT",
        "--json",
        "-u",
        "--level",
        "PICKY",
        str(TEMP_TEXT),
    ]
    completed = subprocess.run(
        command,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    start = completed.stdout.find("{")
    if start < 0:
        raise RuntimeError("O LanguageTool não devolveu um resultado JSON")
    return json.loads(completed.stdout[start:]), completed.stderr


def paragraph_for_offset(spans: list[Span], offset: int) -> Paragraph | None:
    for span in spans:
        if span.start <= offset <= span.end:
            return span.paragraph
    return None


def is_lexical(match: dict[str, object]) -> bool:
    rule = match.get("rule", {})
    rule_id = str(rule.get("id", ""))
    issue_type = str(rule.get("issueType", ""))
    category = str(rule.get("category", {}).get("id", ""))
    return (
        issue_type.lower() == "misspelling"
        or "MORFOLOGIK" in rule_id
        or rule_id in {"HUNSPELL_RULE", "PT_COMPOUNDS"}
        or category.upper() in {"TYPOS", "CASING"}
    )


def escape_cell(value: str) -> str:
    return html.escape(value.replace("|", "\\|").replace("\n", " "))


def preserved_editorial_section(path: Path) -> list[str]:
    """Conserva a triagem humana quando a listagem automática é regenerada."""
    if not path.is_file():
        return []
    existing = path.read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^## Verificação do LanguageTool\n.*?(?=^## Termos assinalados\n)",
        existing,
    )
    if not match:
        return []
    return match.group(0).rstrip().splitlines()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--lt-home", type=Path, default=DEFAULT_LT_HOME)
    parser.add_argument("--java", type=Path, default=DEFAULT_JAVA)
    args = parser.parse_args()

    paragraphs = extract_paragraphs(args.docx)
    text, spans = join_paragraphs(paragraphs)
    result, _ = run_languagetool(text, args.java, args.lt_home)
    matches = result.get("matches", [])
    findings: list[dict[str, object]] = []

    for match in matches:
        if not is_lexical(match):
            continue
        offset = int(match.get("offset", 0))
        paragraph = paragraph_for_offset(spans, offset)
        if paragraph is None:
            continue
        length = int(match.get("length", 0))
        term = text[offset : offset + length]
        replacements = [
            str(item.get("value", ""))
            for item in match.get("replacements", [])[:8]
            if item.get("value")
        ]
        findings.append(
            {
                "term": term,
                "paragraph": paragraph.number,
                "context": paragraph.text,
                "rule": str(match.get("rule", {}).get("id", "")),
                "message": str(match.get("message", "")),
                "suggestions": replacements,
            }
        )

    counts = Counter(str(item["term"]).lower() for item in findings)
    examples: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in findings:
        term = str(item["term"]).lower()
        if len(examples[term]) < 3:
            examples[term].append(item)

    software = result.get("software", {})
    language = result.get("language", {})
    editorial_section = preserved_editorial_section(args.output)
    lines = [
        "# Auditoria lexical do DOCX com LanguageTool",
        "",
        "## Método e alcance",
        "",
        f"- Fonte: `{args.docx.name}`.",
        f"- Motor: **LanguageTool {software.get('version', 'desconhecido')}**, distribuição oficial autónoma executada localmente.",
        f"- Variante confirmada pelo motor: **{language.get('name', 'Portuguese (Portugal)')}** (`pt-PT`); nível: `PICKY`.",
        f"- Parágrafos analisados: **{len(paragraphs)}**; caracteres: **{len(text)}**.",
        f"- Avisos totais devolvidos: **{len(matches)}**; ocorrências lexicais seleccionadas: **{len(findings)}**.",
        "- Foram excluídos o *Abstract*, a bibliografia, linhas de fonte e endereços isolados.",
        "- Todo o processamento foi local: nenhuma passagem do manuscrito foi enviada para a API Premium ou para outro serviço externo.",
        "- O manuscrito não foi alterado. Os avisos indicam palavras ausentes do dicionário interno; não demonstram, por si só, que uma palavra seja inventada ou inadequada.",
        "",
    ]
    if editorial_section:
        lines.extend(editorial_section + [""])
    lines.extend(
        [
            "## Termos assinalados",
            "",
            "| Termo | Ocorrências | Regra | Sugestões do LanguageTool | Primeiro contexto |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    for term, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        first = examples[term][0]
        suggestions = ", ".join(first["suggestions"]) or "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{escape_cell(term)}`",
                    str(count),
                    f"`{escape_cell(str(first['rule']))}`",
                    escape_cell(suggestions),
                    escape_cell(str(first["context"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Ocorrências e localização",
            "",
            "| Termo | Parágrafo DOCX | Mensagem | Sugestões | Contexto |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    for item in findings:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{escape_cell(str(item['term']))}`",
                    str(item["paragraph"]),
                    escape_cell(str(item["message"])),
                    escape_cell(", ".join(item["suggestions"]) or "—"),
                    escape_cell(str(item["context"])),
                ]
            )
            + " |"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"LanguageTool {software.get('version')} / {language.get('name')}")
    print(f"Avisos totais: {len(matches)}")
    print(f"Ocorrências lexicais: {len(findings)}")
    print(f"Termos únicos: {len(counts)}")
    print(f"Relatório: {args.output}")


if __name__ == "__main__":
    main()
