#!/usr/bin/env python3
"""Reformula as nove formas prioritárias da auditoria LanguageTool na versão 0.4.58."""

from __future__ import annotations

import os
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


REPLACEMENTS = [
    ("Versão do documento: 0.4.57", "Versão do documento: 0.4.58"),
    (
        "o que reforça a natureza regulada, iterativa e evidencial deste domínio",
        "o que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar a sua evolução em evidência",
    ),
    (
        "reforçando a integração formal de avaliações formativas e sumativas no processo regulado de desenvolvimento",
        "reforçando a integração formal de avaliações formativas, realizadas durante o desenvolvimento para orientar melhorias, e de avaliações sumativas, destinadas a verificar o resultado final",
    ),
    (
        "a autoridade decisional permanece frequentemente concentrada",
        "o poder de decisão permanece frequentemente concentrado",
    ),
    (
        "a participação como estrutura desenhável",
        "a participação como estrutura que pode ser planeada e configurada deliberadamente",
    ),
    (
        "a configurabilidade não garante aceitação",
        "a possibilidade de configuração não garante aceitação",
    ),
    (
        "o ficheiro-fonte pode ser versionado, comparado, analisado e reutilizado",
        "o ficheiro-fonte pode ser mantido sob controlo de versões, comparado, analisado e reutilizado",
    ),
    ("Catálogo versionado dos modelos", "Catálogo de modelos"),
    ("para o renderizador e para a camada de IA", "para o módulo de visualização tridimensional e para a camada de IA"),
    (
        "conjunto multipopulacional da mão — 1.790 linhas de dados, provenientes de fontes e subconjuntos populacionais de nove países",
        "conjunto de dados da mão proveniente de várias populações — 1.790 linhas, provenientes de fontes e subconjuntos populacionais de nove países",
    ),
    (
        "procedimento multipopulacional — gera o conjunto de dados da mão a partir de secções correspondentes às fontes e aos subconjuntos incluídos",
        "procedimento de integração dos dados — gera o conjunto de dados da mão a partir de secções correspondentes às fontes e aos subconjuntos incluídos",
    ),
    ("Base multipopulacional da mão", "Base de dados da mão com dados de várias populações"),
    (
        "A base multipopulacional da mão cobre nove países",
        "A base de dados da mão reúne informação proveniente de nove países",
    ),
    (
        "A base multipopulacional da mão foi construída para reunir diferenças antropométricas da mão em várias dimensões geográficas, demográficas, etárias e estatísticas",
        "A base de dados da mão foi construída para reunir dados de várias populações e representar a diversidade antropométrica da mão em termos geográficos, demográficos, etários e estatísticos",
    ),
    (
        "**não** representa uma impressão física nem uma recomendação de imprimibilidade",
        "**não** representa uma impressão física nem confirma que o modelo possa ser impresso com sucesso",
    ),
]


DOCX_REPLACEMENTS = (
    REPLACEMENTS[1:7]
    + REPLACEMENTS[8:13]
    + [
        (
            "Material de apoio da investigação, base multipopulacional da mão, repositório da plataforma",
            "Material de apoio da investigação, base de dados da mão com dados de várias populações, repositório da plataforma",
        ),
        (
            "A base de dados base multipopulacional da mão foi construída para reunir diferenças antropométricas da mão em várias dimensões geográficas, demográficas, etárias e estatísticas",
            "A base de dados da mão foi construída para reunir dados de várias populações e representar a diversidade antropométrica da mão em termos geográficos, demográficos, etários e estatísticos",
        ),
        (
            "não representa uma impressão física nem uma recomendação de imprimibilidade",
            "não representa uma impressão física nem confirma que o modelo possa ser impresso com sucesso",
        ),
    ]
)


REMOVED_TERMS = re.compile(
    r"\b(?:evidencial|decisional|desenhável|configurabilidade|versionado|renderizador|multipopulacional|imprimibilidade)\b",
    re.IGNORECASE,
)


def replace_in_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        occurrences = text.count(old)
        if occurrences:
            text = text.replace(old, new)
            count += occurrences
    return text, count


def replace_in_element(element: etree._Element, old: str, new: str) -> int:
    count = 0
    while True:
        nodes = element.xpath(".//w:t", namespaces=NS)
        full_text = "".join(node.text or "" for node in nodes)
        start = full_text.find(old)
        if start < 0:
            return count
        end = start + len(old)
        offset = 0
        inserted = False
        for node in nodes:
            value = node.text or ""
            node_start, node_end = offset, offset + len(value)
            overlap_start = max(start, node_start)
            overlap_end = min(end, node_end)
            if overlap_start < overlap_end:
                local_start = overlap_start - node_start
                local_end = overlap_end - node_start
                prefix = value[:local_start]
                suffix = value[local_end:]
                if not inserted:
                    node.text = prefix + new + suffix
                    inserted = True
                else:
                    node.text = prefix + suffix
                if node.text.startswith(" ") or node.text.endswith(" "):
                    node.set(f"{{{XML}}}space", "preserve")
            offset = node_end
        count += 1


def validate_text(text: str, source: str, require_version: bool = False) -> None:
    remaining = REMOVED_TERMS.findall(text)
    if remaining:
        raise RuntimeError(f"Termos ainda presentes em {source}: {remaining}")
    if text.count("avaliações sumativas, destinadas a verificar o resultado final") != 1:
        raise RuntimeError(f"A explicação de «sumativas» não ficou estável em {source}")
    if require_version and text.count("Versão do documento: 0.4.58") != 1:
        raise RuntimeError(f"A versão 0.4.58 não ficou única em {source}")


def update_markdown() -> int:
    original = MARKDOWN.read_text(encoding="utf-8")
    if (
        "Versão do documento: 0.4.58" in original
        and not REMOVED_TERMS.search(original)
        and "avaliações sumativas, destinadas a verificar o resultado final" in original
    ):
        validate_text(original, "Markdown", require_version=True)
        return 0
    updated, count = replace_in_text(original)
    if count != len(REPLACEMENTS):
        raise RuntimeError(
            f"Esperavam-se {len(REPLACEMENTS)} substituições no Markdown; foram feitas {count}"
        )
    validate_text(updated, "Markdown", require_version=True)
    MARKDOWN.write_text(updated, encoding="utf-8")
    return count


def update_docx() -> int:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])
    count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        for old, new in DOCX_REPLACEMENTS:
            count += replace_in_element(paragraph, old, new)

    full_text = "\n".join(
        "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))
        for paragraph in document.xpath("//w:p", namespaces=NS)
    )
    if count != len(DOCX_REPLACEMENTS):
        raise RuntimeError(
            f"Esperavam-se {len(DOCX_REPLACEMENTS)} substituições no DOCX; foram feitas {count}"
        )
    validate_text(full_text, "DOCX")

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, DOCX)
    return count


def main() -> None:
    markdown_changes = update_markdown()
    docx_changes = update_docx()
    print(f"Markdown: {markdown_changes} substituições")
    print(f"DOCX: {docx_changes} substituições")


if __name__ == "__main__":
    main()
