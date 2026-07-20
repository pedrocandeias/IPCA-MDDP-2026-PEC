#!/usr/bin/env python3
"""Condensa o enquadramento do ISO/TC 168 sem remover as novas referências."""

from __future__ import annotations

import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from integrate_normative_references_096 import NEW_TC_MD as COMPACT_MD


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

LONG_MD = (
    "A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de "
    "biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de *software* e "
    "consideração explícita de factores humanos e de usabilidade. Normas desenvolvidas no âmbito "
    "do comité técnico ISO/TC 168 abrangem aspectos como o desempenho, a segurança, os factores "
    "ambientais e a compatibilidade entre componentes de próteses e ortóteses (International "
    "Organization for Standardization [ISO], n.d.). A ISO 8549-1:2020, preparada por este comité, "
    "estabelece a terminologia geral aplicável às próteses externas de membro e às ortóteses "
    "externas (ISO, 2020). Adicionalmente, os fabricantes devem implementar sistemas de vigilância "
    "pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o "
    "que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar "
    "a sua evolução em evidência (Parlamento Europeu & Conselho da União Europeia, 2017; Resnik et "
    "al., 2010)."
)

OLD_PREFIX = (
    " e consideração explícita de fatores humanos e de usabilidade. Normas desenvolvidas no âmbito "
    "do comité técnico "
)
NEW_PREFIX = " e consideração explícita de fatores humanos e de usabilidade. O comité técnico "
OLD_SUFFIX = (
    " abrangem aspetos como o desempenho, a segurança, os fatores ambientais e a compatibilidade "
    "entre componentes de próteses e ortóteses (International Organization for Standardization "
    "[ISO], n.d.). A ISO 8549-1:2020, preparada por este comité, estabelece a terminologia geral "
    "aplicável às próteses externas de membro e às ortóteses externas (ISO, 2020). Adicionalmente, "
    "os fabricantes devem implementar sistemas de vigilância pós-comercialização, recolhendo dados "
    "de uso real ao longo do ciclo de vida do dispositivo, o que reforça a natureza regulada e "
    "iterativa deste domínio, bem como a necessidade de sustentar a sua evolução em evidência "
    "(Parlamento Europeu & Conselho da União Europeia, 2017; Resnik et al., 2010)."
)
NEW_SUFFIX = (
    " normaliza aspetos como o desempenho, a segurança e a compatibilidade entre componentes de "
    "próteses e ortóteses (ISO, n.d.). A ISO 8549-1:2020, preparada por este comité, estabelece a "
    "terminologia geral deste domínio (ISO, 2020). Adicionalmente, os fabricantes devem implementar "
    "sistemas de vigilância pós-comercialização, recolhendo dados de uso real ao longo do ciclo de "
    "vida do dispositivo, o que reforça a natureza regulada e iterativa deste domínio, bem como a "
    "necessidade de sustentar a sua evolução em evidência (Parlamento Europeu & Conselho da União "
    "Europeia, 2017; Resnik et al., 2010)."
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
    }


def replace_text(root: etree._Element, old: str, new: str) -> None:
    matches = [node for node in root.xpath("//w:t", namespaces=NS) if (node.text or "") == old]
    if len(matches) != 1:
        raise RuntimeError(f"Segmento DOCX inesperado: {len(matches)} ocorrências")
    matches[0].text = new
    set_space(matches[0])


def main() -> None:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count(LONG_MD) != 1 or COMPACT_MD in markdown:
        raise RuntimeError("Estado Markdown inesperado")
    markdown = markdown.replace(LONG_MD, COMPACT_MD, 1)

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
    replace_text(root, OLD_PREFIX, NEW_PREFIX)
    replace_text(root, OLD_SUFFIX, NEW_SUFFIX)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")

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
        "Enquadramento normativo condensado; "
        f"comentários={after['comments']}, notas={after['footnotes']}"
    )


if __name__ == "__main__":
    main()
