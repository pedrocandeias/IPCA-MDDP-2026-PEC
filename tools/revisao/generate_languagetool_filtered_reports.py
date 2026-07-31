#!/usr/bin/env python3
"""Gera relatórios temáticos e filtrados a partir do LanguageTool local."""

from __future__ import annotations

import html
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile

from lxml import etree

from audit_docx_languagetool import (
    DEFAULT_DOCX,
    DEFAULT_JAVA,
    DEFAULT_LT_HOME,
    NS,
    extract_paragraphs,
    join_paragraphs,
    run_languagetool,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "docs/revisoes/linguagem/languagetool"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

AGREEMENT_RULES = {
    "GENERAL_NUMBER_AGREEMENT_ERRORS",
    "GENERAL_GENDER_AGREEMENT_ERRORS",
    "GENERAL_VERB_AGREEMENT_ERRORS",
    "REFLEXIVE_VERB_SE_AGREEMENT",
    "LINKING_VERB_PREDICATE_AGREEMENT",
}
PUNCTUATION_NOISE = {"FINAL_STOPS", "PUNCTUATION_PARAGRAPH_END"}
STYLE_NOISE = {"BARBARISMS_PT_PT_V3"}
FORMAL_NOISE = {"APENAS_SOMENTE"}
TECHNICAL_AGREEMENT_NOISE = re.compile(
    r"\b(?:open|web|python|id|bambu|prusa|prusaslicer|openscad)\b", re.IGNORECASE
)


@dataclass
class Metadata:
    in_table: bool
    in_list: bool
    style: str


@dataclass
class Candidate:
    paragraph: int
    rule: str
    matched: str
    message: str
    suggestions: list[str]
    context: str


REPORTS = {
    "concordancia": (
        "Concordância",
        "Possíveis problemas de concordância de número, género, pessoa verbal, construção reflexa ou predicativo.",
    ),
    "gramatica": (
        "Gramática",
        "Outros avisos classificados pelo LanguageTool como gramática geral.",
    ),
    "clareza": (
        "Clareza",
        "Construções que o LanguageTool considera susceptíveis de formulação mais directa ou objectiva.",
    ),
    "redundancia": (
        "Redundância",
        "Repetições semânticas, pleonasmos e construções potencialmente redundantes.",
    ),
    "concisao": (
        "Concisão",
        "Sugestões de encurtamento ou simplificação da frase.",
    ),
    "registo_formal": (
        "Registo formal e académico",
        "Sugestões relacionadas com formalidade e adequação ao registo académico.",
    ),
    "pontuacao": (
        "Pontuação",
        "Avisos de pontuação após exclusão de títulos, listas, tabelas e regras de ponto final estrutural.",
    ),
    "estilo": (
        "Estilo",
        "Avisos gerais de estilo após exclusão da regra lexical que assinala estrangeirismos e nomes técnicos.",
    ),
}


def metadata_by_paragraph(path: Path) -> dict[int, Metadata]:
    with ZipFile(path) as source:
        document = etree.fromstring(source.read("word/document.xml"))
    metadata: dict[int, Metadata] = {}
    for number, paragraph in enumerate(document.xpath("//w:p", namespaces=NS), start=1):
        styles = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        metadata[number] = Metadata(
            in_table=bool(paragraph.xpath("ancestor::w:tbl", namespaces=NS)),
            in_list=bool(paragraph.xpath("./w:pPr/w:numPr", namespaces=NS)),
            style=str(styles[0]) if styles else "",
        )
    return metadata


def structural_noise(number: int, meta: Metadata, text: str) -> bool:
    style = meta.style.lower()
    excluded_style = any(
        marker in style
        for marker in ("heading", "title", "caption", "toc", "índice", "index", "legenda")
    )
    if number < 300 or meta.in_table or meta.in_list or excluded_style:
        return True
    if re.match(r"^(?:[-•]\s+|Tabela\s|Figura\s|Quadro\s|Anexo\s)", text.strip(), re.IGNORECASE):
        return True
    if len(text.strip()) < 45 and not re.search(r"[.!?…][\]\)»”']?$", text.strip()):
        return True
    return False


def report_key(match: dict[str, object]) -> str | None:
    rule = match.get("rule", {})
    rule_id = str(rule.get("id", ""))
    category = str(rule.get("category", {}).get("id", ""))
    if rule_id in AGREEMENT_RULES:
        return "concordancia"
    if category == "GRAMMAR":
        return "gramatica"
    if category in {"CLARITY", "OBJECTIVE"}:
        return "clareza"
    if category in {"REDUNDANCY", "REDUNDANCY_PT_PT"}:
        return "redundancia"
    if category in {"SHORTEN_IT", "SHORTEN_IT_PT_PT"}:
        return "concisao"
    if (
        category in {"FORMAL", "FORMAL_SPEECH_PT_PT", "ACADEMIC"}
        and rule_id not in FORMAL_NOISE
    ):
        return "registo_formal"
    if category == "PUNCTUATION" and rule_id not in PUNCTUATION_NOISE:
        return "pontuacao"
    if category == "STYLE" and rule_id not in STYLE_NOISE:
        return "estilo"
    return None


def context_snippet(text: str, local_offset: int, length: int) -> str:
    start = max(0, local_offset - 180)
    end = min(len(text), local_offset + length + 180)
    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
    if start:
        snippet = "…" + snippet
    if end < len(text):
        snippet += "…"
    return snippet


def escape(value: str) -> str:
    return html.escape(value.replace("|", "\\|").replace("\n", " "))


def main() -> None:
    paragraphs = extract_paragraphs(DEFAULT_DOCX)
    text, spans = join_paragraphs(paragraphs)
    result, _ = run_languagetool(text, DEFAULT_JAVA, DEFAULT_LT_HOME)
    matches = result.get("matches", [])
    metadata = metadata_by_paragraph(DEFAULT_DOCX)
    paragraph_lookup = {paragraph.number: paragraph for paragraph in paragraphs}
    candidates: dict[str, list[Candidate]] = {key: [] for key in REPORTS}
    seen: dict[str, set[tuple[int, str]]] = {key: set() for key in REPORTS}

    span_index = 0
    for match in sorted(matches, key=lambda item: int(item.get("offset", 0))):
        key = report_key(match)
        if key is None:
            continue
        offset = int(match.get("offset", 0))
        while span_index + 1 < len(spans) and offset > spans[span_index].end:
            span_index += 1
        span = spans[span_index]
        paragraph = paragraph_lookup.get(span.paragraph.number)
        meta = metadata.get(span.paragraph.number)
        if (
            paragraph is None
            or meta is None
            or structural_noise(paragraph.number, meta, paragraph.text)
        ):
            continue
        rule = match.get("rule", {})
        rule_id = str(rule.get("id", ""))
        length = int(match.get("length", 0))
        matched = text[offset : offset + length]
        if key == "concordancia" and TECHNICAL_AGREEMENT_NOISE.search(matched):
            continue
        signature = (paragraph.number, rule_id)
        if signature in seen[key]:
            continue
        seen[key].add(signature)
        replacements = [
            str(item.get("value", ""))
            for item in match.get("replacements", [])[:8]
            if item.get("value")
        ]
        candidates[key].append(
            Candidate(
                paragraph=paragraph.number,
                rule=rule_id,
                matched=matched,
                message=str(match.get("message", "")),
                suggestions=replacements,
                context=context_snippet(
                    paragraph.text,
                    max(0, offset - span.start),
                    length,
                ),
            )
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# Relatórios filtrados do LanguageTool",
        "",
        "Os relatórios contêm candidatos automáticos para revisão humana; não representam erros confirmados nem autorizam substituições automáticas.",
        "",
        "Foram excluídos o *Abstract*, a bibliografia, tabelas, listas, índices, títulos, legendas, linhas de fonte, endereços isolados e avisos lexicais, incluindo os referentes a estrangeirismos, nomes técnicos e nomes de modelos. Estes termos podem surgir naturalmente no contexto de um aviso relativo a outra expressão, mas nunca constituem o segmento assinalado para revisão.",
        "",
        "A aplicação humana das propostas na versão 0.4.61 está documentada em [Decisões editoriais](decisoes_editoriais_061.md).",
        "",
        "| Relatório | Ocorrências filtradas |",
        "| --- | ---: |",
    ]

    for key, (title, description) in REPORTS.items():
        items = candidates[key]
        index_lines.append(f"| [{title}]({key}.md) | {len(items)} |")
        rule_counts = Counter(item.rule for item in items)
        lines = [
            f"# LanguageTool — {title}",
            "",
            description,
            "",
            f"Ocorrências filtradas: **{len(items)}**.",
            "",
            "Estes avisos são candidatos para leitura humana. O contexto académico e técnico prevalece sobre a sugestão automática.",
            "",
        ]
        if rule_counts:
            lines.extend(
                [
                    "## Regras representadas",
                    "",
                    "| Regra | Ocorrências |",
                    "| --- | ---: |",
                ]
            )
            for rule, count in rule_counts.most_common():
                lines.append(f"| `{escape(rule)}` | {count} |")
            lines.extend(
                [
                    "",
                    "## Ocorrências",
                    "",
                    "| # | Parágrafo DOCX | Segmento assinalado | Regra | Mensagem | Sugestões | Contexto |",
                    "| ---: | ---: | --- | --- | --- | --- | --- |",
                ]
            )
            for number, item in enumerate(items, start=1):
                suggestions = ", ".join(item.suggestions) or "—"
                lines.append(
                    f"| {number} | {item.paragraph} | «{escape(item.matched)}» | `{escape(item.rule)}` | "
                    f"{escape(item.message)} | {escape(suggestions)} | {escape(item.context)} |"
                )
        else:
            lines.append("Nenhuma ocorrência permaneceu depois da filtragem estrutural.")
        (OUTPUT_DIR / f"{key}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (OUTPUT_DIR / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"LanguageTool {result.get('software', {}).get('version')} / pt-PT")
    for key, (title, _) in REPORTS.items():
        print(f"{title}: {len(candidates[key])}")


if __name__ == "__main__":
    main()
