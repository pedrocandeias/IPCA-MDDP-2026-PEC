#!/usr/bin/env python3
"""Integra as revisões DOCX de 19-07-2026 na versão canónica 0.4.69.

A gravação revista pelo autor partiu de uma cópia aberta anterior à versão
0.4.69. Este script executa uma comparação de três vias entre essa base, a
gravação do autor e a exportação 0.4.69, preservando as revisões que não
conflituam. Os dois conflitos da Secção 8.2 são resolvidos explicitamente.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
from collections import defaultdict
from copy import deepcopy
from difflib import SequenceMatcher
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
BASE = ROOT / (
    "docs/versoes/backups/"
    "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto-"
    "2026-07-18_22-22-10-before-recovery-stale-save-069.docx"
)
USER_SAVE = ROOT / (
    "docs/versoes/backups/"
    "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto-"
    "2026-07-19_12-14-26-before-merge-user-edits-070.docx"
)
HEAD_069 = ROOT / (
    "docs/versoes/exportacoes/2026-07-18_18-09-20-reducao-setas-069/"
    "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
)

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}
XML = "http://www.w3.org/XML/1998/namespace"

VERSION_OLD = "Versão do documento: 0.4.69"
VERSION_NEW = "Versão do documento: 0.4.70"
DISCLAIMER = (
    "O ensaio examina o fluxo perante informação incompleta; não permite "
    "concluir que as dimensões correspondam à mão de uma pessoa concreta ou "
    "que a plataforma seja fácil de usar por pessoas sem formação técnica."
)
SUMMARY_TO_DELETE = (
    "Em síntese, o protótipo responde directamente à fragmentação do processo "
    "técnico e à insuficiência do respectivo registo, oferece respostas "
    "parciais às lacunas de tradução dimensional, controlo da configuração e "
    "dependência de ferramentas, e não responde empiricamente às lacunas de "
    "utilização real, conforto, participação, manutenção ou impacto "
    "socioeconómico. Esta posição relativa ao estado da arte delimita o "
    "contributo como integração técnica e conhecimento de projecto documentado, "
    "e não como validação de uma solução protésica pronta para utilização."
)


def read_package(path: Path) -> tuple[list, dict[str, bytes]]:
    with ZipFile(path) as archive:
        items = archive.infolist()
        files = {item.filename: archive.read(item.filename) for item in items}
    return items, files


def parse_document(path: Path) -> tuple[list, dict[str, bytes], etree._Element]:
    items, files = read_package(path)
    return items, files, etree.fromstring(files["word/document.xml"])


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def paragraphs(document: etree._Element) -> list[etree._Element]:
    return document.xpath("//w:p", namespaces=NS)


def write_jsonl(path: Path, values: list[str]) -> None:
    path.write_text(
        "".join(json.dumps(value, ensure_ascii=False) + "\n" for value in values),
        encoding="utf-8",
    )


def parse_conflicted_jsonl(lines: list[str]) -> list[str]:
    result: list[str] = []
    index = 0
    conflicts = 0
    while index < len(lines):
        line = lines[index]
        if not line.startswith("<<<<<<<"):
            result.append(json.loads(line))
            index += 1
            continue

        ours: list[str] = []
        theirs: list[str] = []
        index += 1
        while index < len(lines) and not lines[index].startswith("======="):
            ours.append(json.loads(lines[index]))
            index += 1
        if index == len(lines):
            raise RuntimeError("Conflito sem separador central")
        index += 1
        while index < len(lines) and not lines[index].startswith(">>>>>>>"):
            theirs.append(json.loads(lines[index]))
            index += 1
        if index == len(lines):
            raise RuntimeError("Conflito sem marcador final")
        index += 1

        ours_nonempty = [value for value in ours if value]
        theirs_nonempty = [value for value in theirs if value]
        if ours_nonempty and ours_nonempty[0].startswith(
            "O primeiro conjunto experimental incidiu"
        ):
            if not theirs_nonempty or DISCLAIMER not in theirs_nonempty[0]:
                raise RuntimeError("A ressalva metodológica esperada não foi localizada")
            ours_nonempty[0] = f"{ours_nonempty[0]} {DISCLAIMER}"
            result.extend(ours_nonempty)
        elif ours_nonempty and ours_nonempty[0].startswith(
            "Verificar a adaptação do sistema"
        ):
            result.extend(ours_nonempty)
        else:
            raise RuntimeError(
                "Conflito não reconhecido: "
                + repr((ours_nonempty[:2], theirs_nonempty[:2]))
            )
        conflicts += 1

    if conflicts != 2:
        raise RuntimeError(f"Esperavam-se 2 conflitos; foram encontrados {conflicts}")
    return result


def editorial_corrections(value: str) -> str:
    if value == "Anexo C — Adaptação paramétrica dos mODELOS140":
        return "Anexo C — Adaptação paramétrica dos modelos de mão protésica140"
    value = value.replace(
        "configurar modelos de membro superior com base",
        "configurar modelos de prótese de membro superior com base",
    )
    value = value.replace("membro superior especifico", "membro superior específico")
    return value


def three_way_texts(
    base_texts: list[str], user_texts: list[str], head_texts: list[str]
) -> list[str]:
    with tempfile.TemporaryDirectory(prefix="merge-docx-070-") as directory:
        temporary = Path(directory)
        base_path = temporary / "base.jsonl"
        user_path = temporary / "user.jsonl"
        head_path = temporary / "head.jsonl"
        write_jsonl(base_path, base_texts)
        write_jsonl(user_path, user_texts)
        write_jsonl(head_path, head_texts)
        process = subprocess.run(
            [
                "git",
                "merge-file",
                "-p",
                str(user_path),
                str(base_path),
                str(head_path),
            ],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if process.returncode not in {0, 1, 2}:
            raise RuntimeError(process.stderr or "git merge-file falhou")
        merged = parse_conflicted_jsonl(process.stdout.splitlines())
    return [editorial_corrections(value) for value in merged]


def replace_full_text(paragraph: etree._Element, value: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if not nodes:
        run = etree.SubElement(paragraph, f"{{{W}}}r")
        node = etree.SubElement(run, f"{{{W}}}t")
        node.text = value
        return
    nodes[0].text = value
    if value.startswith(" ") or value.endswith(" "):
        nodes[0].set(f"{{{XML}}}space", "preserve")
    for node in nodes[1:]:
        node.text = ""


def source_variants(value: str) -> list[str]:
    variants = [value]
    variants.append(
        value.replace(
            "modelos de prótese de membro superior",
            "modelos de membro superior",
        )
    )
    variants.append(value.replace("membro superior específico", "membro superior especifico"))
    if value.endswith(DISCLAIMER):
        variants.append(value[: -len(DISCLAIMER)].rstrip())
    return list(dict.fromkeys(variants))


def choose_source(
    value: str,
    user_paragraphs: list[etree._Element],
    user_texts: list[str],
    head_index: int,
    head_count: int,
) -> etree._Element:
    candidates: list[int] = []
    variants = source_variants(value)
    for candidate_index, candidate_text in enumerate(user_texts):
        if candidate_text in variants:
            candidates.append(candidate_index)
    if not candidates:
        raise RuntimeError(f"Parágrafo revisto não localizado na gravação do autor: {value!r}")
    expected = head_index / max(1, head_count) * len(user_texts)
    selected = min(candidates, key=lambda candidate: abs(candidate - expected))
    source = deepcopy(user_paragraphs[selected])
    source_text = paragraph_text(source)
    if source_text != value:
        replace_full_text(source, value)
    if source.xpath(
        ".//w:commentReference | .//w:footnoteReference | .//w:drawing | .//*[@r:id]",
        namespaces=NS,
    ):
        raise RuntimeError(f"Parágrafo revisto contém relações não portáveis: {value!r}")
    return source


def build_replacements(
    head_texts: list[str], desired_texts: list[str]
) -> tuple[list[tuple[int, str, str]], list[int]]:
    replacements: list[tuple[int, str, str]] = []
    deletions: list[int] = []
    matcher = SequenceMatcher(None, head_texts, desired_texts, autojunk=False)
    for tag, head_start, head_end, desired_start, desired_end in matcher.get_opcodes():
        if tag == "equal":
            continue
        old_values = [
            (index, head_texts[index])
            for index in range(head_start, head_end)
            if head_texts[index]
        ]
        new_values = [
            value for value in desired_texts[desired_start:desired_end] if value
        ]
        if len(old_values) == len(new_values):
            replacements.extend(
                (index, old, new)
                for (index, old), new in zip(old_values, new_values, strict=True)
                if old != new
            )
            continue
        if (
            len(old_values) == 1
            and not new_values
            and old_values[0][1] == SUMMARY_TO_DELETE
        ):
            deletions.append(old_values[0][0])
            continue
        raise RuntimeError(
            "Alteração estrutural não prevista: "
            f"{tag} {old_values!r} -> {new_values!r}"
        )
    return replacements, deletions


def update_docx(
    head_items: list,
    head_files: dict[str, bytes],
    head_document: etree._Element,
    user_document: etree._Element,
    desired_texts: list[str],
) -> tuple[int, int]:
    head_paragraphs = paragraphs(head_document)
    head_texts = [paragraph_text(value) for value in head_paragraphs]
    user_paragraphs = paragraphs(user_document)
    user_texts = [paragraph_text(value) for value in user_paragraphs]
    replacements, deletions = build_replacements(head_texts, desired_texts)

    for head_index, _old, new in replacements:
        target = head_paragraphs[head_index]
        source = choose_source(
            new, user_paragraphs, user_texts, head_index, len(head_paragraphs)
        )
        target.getparent().replace(target, source)

    for head_index in deletions:
        target = head_paragraphs[head_index]
        target.getparent().remove(target)

    version_paragraphs = [
        value
        for value in paragraphs(head_document)
        if paragraph_text(value) == VERSION_OLD
    ]
    if len(version_paragraphs) > 1:
        raise RuntimeError("A versão 0.4.69 ocorre mais de uma vez no DOCX")
    if version_paragraphs:
        replace_full_text(version_paragraphs[0], VERSION_NEW)

    final_texts = [paragraph_text(value) for value in paragraphs(head_document)]
    if "mODELOS" in "\n".join(final_texts):
        raise RuntimeError("O lapso mODELOS permaneceu no DOCX")
    if SUMMARY_TO_DELETE in final_texts:
        raise RuntimeError("O parágrafo removido permaneceu no DOCX")
    if version_paragraphs and VERSION_NEW not in final_texts:
        raise RuntimeError("A versão 0.4.70 não foi aplicada ao DOCX")

    head_files["word/document.xml"] = etree.tostring(
        head_document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in head_items:
            output.writestr(item, head_files[item.filename])
    os.replace(temporary, DOCX)
    return len(replacements), len(deletions)


def plain_markdown(value: str) -> str:
    value = re.sub(r"^#{1,6}\s+", "", value.strip())
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("*", "").replace("`", "")
    return value.strip()


def markdownize(value: str) -> str:
    result = value
    terms = (
        "Research Through Design",
        "WebAssembly",
        "co-design",
        "hardware",
        "software",
        "design",
        "web",
    )
    for term in terms:
        result = re.sub(
            rf"(?<![\w*]){re.escape(term)}(?![\w*])",
            f"*{term}*",
            result,
        )
    return result


def update_markdown(
    replacements: list[tuple[int, str, str]], deletions: list[int]
) -> int:
    text = MARKDOWN.read_text(encoding="utf-8")
    if text.count(VERSION_OLD) != 1:
        raise RuntimeError("A versão 0.4.69 não ocorre uma única vez no Markdown")
    text = text.replace(VERSION_OLD, VERSION_NEW)
    blocks = re.split(r"(\n\s*\n)", text)
    changed = 0

    def replace_visible(old: str, new: str | None) -> int:
        matches = 0
        for block_index in range(0, len(blocks), 2):
            block = blocks[block_index]
            if not block.strip():
                continue
            if plain_markdown(block) == old:
                heading = re.match(r"^(#{1,6}\s+)", block)
                prefix = heading.group(1) if heading else ""
                blocks[block_index] = (
                    "" if new is None else prefix + markdownize(new)
                )
                matches += 1
                continue
            if block.lstrip().startswith("|"):
                cells = block.split("|")
                for cell_index, cell in enumerate(cells):
                    if plain_markdown(cell) == old:
                        if new is None:
                            raise RuntimeError("Não é permitido eliminar uma célula isolada")
                        cells[cell_index] = f" {markdownize(new)} "
                        matches += 1
                blocks[block_index] = "|".join(cells)
        return matches

    for head_index, old, new in replacements:
        if head_index < 1000:
            continue
        count = replace_visible(old, new)
        if count != 1:
            raise RuntimeError(
                f"Substituição Markdown com {count} correspondências: {old!r}"
            )
        changed += count
    for head_index in deletions:
        if head_index < 1000:
            continue
        count = replace_visible(SUMMARY_TO_DELETE, None)
        if count != 1:
            raise RuntimeError(
                f"Eliminação Markdown com {count} correspondências: {SUMMARY_TO_DELETE!r}"
            )
        changed += count

    merged = "".join(blocks)
    merged = re.sub(r"\n{3,}", "\n\n", merged)
    if VERSION_NEW not in merged or "mODELOS" in merged:
        raise RuntimeError("A validação final do Markdown falhou")
    if SUMMARY_TO_DELETE in plain_markdown(merged):
        raise RuntimeError("O parágrafo removido permaneceu no Markdown")
    MARKDOWN.write_text(merged, encoding="utf-8")
    return changed


def validate_annotations(files: dict[str, bytes], document: etree._Element) -> None:
    comments = etree.fromstring(files["word/comments.xml"])
    comment_defs = comments.xpath("count(//w:comment)", namespaces=NS)
    comment_refs = document.xpath("count(//w:commentReference)", namespaces=NS)
    footnote_refs = document.xpath("count(//w:footnoteReference)", namespaces=NS)
    if (int(comment_defs), int(comment_refs), int(footnote_refs)) != (14, 14, 12):
        raise RuntimeError(
            "Anotações inesperadas: "
            f"comentários={int(comment_defs)}/{int(comment_refs)}, "
            f"notas={int(footnote_refs)}"
        )


def main() -> None:
    for path in (MARKDOWN, BASE, USER_SAVE, HEAD_069):
        if not path.is_file():
            raise FileNotFoundError(path)

    _base_items, _base_files, base_document = parse_document(BASE)
    _user_items, _user_files, user_document = parse_document(USER_SAVE)
    head_items, head_files, head_document = parse_document(HEAD_069)
    base_texts = [paragraph_text(value) for value in paragraphs(base_document)]
    user_texts = [paragraph_text(value) for value in paragraphs(user_document)]
    head_texts = [paragraph_text(value) for value in paragraphs(head_document)]
    desired_texts = three_way_texts(base_texts, user_texts, head_texts)
    replacements, deletions = build_replacements(head_texts, desired_texts)
    docx_replacements, docx_deletions = update_docx(
        head_items, head_files, head_document, user_document, desired_texts
    )
    markdown_changes = update_markdown(replacements, deletions)
    validate_annotations(head_files, head_document)
    print(
        "Integração concluída: "
        f"{docx_replacements} parágrafos substituídos, "
        f"{docx_deletions} removido, "
        f"{markdown_changes} blocos/células Markdown actualizados."
    )


if __name__ == "__main__":
    main()
