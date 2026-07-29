#!/usr/bin/env python3
"""Delimita a enumeração metodológica a Shah e Robinson (2006)."""

from __future__ import annotations

import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import NS, replace_paragraph, sensitive_state, text_of


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD_MD = (
    "Fisher e Johansen (2020) e Shah e Robinson (2006) descrevem que as abordagens "
    "inclusivas e centradas no utilizador recorrem a repertórios metodológicos "
    "diversificados, incluindo personas, simulação de limitações, prototipagem "
    "iterativa, oficinas participativas e análise de ecossistemas de *stakeholders* "
    "(Fisher & Johansen, 2020; Shah & Robinson, 2006)."
)
OLD_DOCX = OLD_MD.replace("*", "")
NEW_MD = (
    "Shah e Robinson (2006) mostram que o envolvimento dos utilizadores no "
    "desenvolvimento de tecnologias de saúde pode ocorrer nas fases de definição do "
    "conceito, desenvolvimento, teste e implementação, recorrendo a métodos como "
    "entrevistas, questionários, testes de usabilidade, simulações, actividades "
    "colaborativas de definição e desenvolvimento de soluções e discussões orientadas "
    "em grupo."
)
NEW_PARTS = (
    (
        "Shah e Robinson (2006) mostram que o envolvimento dos utilizadores no "
        "desenvolvimento de tecnologias de saúde pode ocorrer nas fases de definição do "
        "conceito, desenvolvimento, teste e implementação, recorrendo a métodos como "
        "entrevistas, questionários, testes de usabilidade, simulações, actividades "
        "colaborativas de definição e desenvolvimento de soluções e discussões orientadas "
        "em grupo.",
        False,
    ),
)
NEW_DOCX = "".join(value for value, _ in NEW_PARTS)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    for value, expected in (
        ("Versão do documento: 0.4.99", 1),
        (OLD_MD, 1),
        (NEW_MD, 0),
    ):
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada: {actual} != {expected} para {value[:70]!r}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.99", "Versão do documento: 0.4.100", 1
    )
    return markdown.replace(OLD_MD, NEW_MD, 1)


def main() -> None:
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    before = sensitive_state(root)
    replace_paragraph(root, OLD_DOCX, NEW_PARTS)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if OLD_DOCX in body or body.count(NEW_DOCX) != 1:
        raise RuntimeError("A actualização não ficou íntegra no DOCX")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Enumeração metodológica delimitada a Shah e Robinson; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
