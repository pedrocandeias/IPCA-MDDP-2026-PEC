#!/usr/bin/env python3
"""Corrige Manz et al. (2022) e explicita o âmbito de membro inferior."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

OLD_SCOPE = (
    "Cordella et al. (2016) e Manz et al. (2022) identificam uma articulação "
    "insuficiente entre as necessidades expressas pelos utilizadores, como conforto, "
    "controlo intuitivo, aparência e participação social; os indicadores objectivos "
    "habitualmente medidos, como desempenho em testes funcionais, parâmetros "
    "biomecânicos e métricas instrumentadas de uso da prótese; e os resultados "
    "desejáveis, como autonomia e qualidade de vida. As revisões salientam que estas "
    "necessidades são contextuais e interdependentes, e que as medições laboratoriais "
    "nem sempre reflectem tarefas relevantes do quotidiano, contribuindo para "
    "contradições entre resultados subjectivos e objectivos (Cordella et al., 2016; "
    "Manz et al., 2022)."
)
NEW_SCOPE = (
    "Embora incidam em segmentos distintos — Cordella et al. (2016) no membro "
    "superior e Manz et al. (2022) no membro inferior — ambas as revisões identificam "
    "uma articulação insuficiente entre as necessidades expressas pelos utilizadores, "
    "como conforto, controlo intuitivo, aparência e participação social; os indicadores "
    "objectivos habitualmente medidos, como desempenho em testes funcionais, parâmetros "
    "biomecânicos e métricas instrumentadas de uso da prótese; e os resultados "
    "desejáveis, como autonomia e qualidade de vida. Salientam igualmente que estas "
    "necessidades são contextuais e interdependentes e que as medições laboratoriais "
    "nem sempre reflectem tarefas relevantes do quotidiano, contribuindo para "
    "contradições entre resultados subjectivos e objectivos (Cordella et al., 2016; "
    "Manz et al., 2022)."
)
OLD_TRANSITION = "Esta desarticulação tem implicações directas para o "
NEW_TRANSITION = "A convergência entre os dois domínios tem implicações directas para o "
OLD_TABLE_23 = (
    "Desalinhamento entre necessidades, métricas objectivas e qualidade de vida "
    "(Cordella et al., 2016; Manz et al., 2022)"
)
NEW_TABLE_23 = (
    "Desalinhamento entre necessidades, métricas objectivas e qualidade de vida, "
    "identificado em revisões dos membros superior e inferior (Cordella et al., 2016; "
    "Manz et al., 2022)"
)
OLD_TABLE_88 = (
    "A separação evita usar indicadores internos como substitutos de conforto, "
    "satisfação ou qualidade de vida, respondendo ao desalinhamento discutido por "
    "Cordella et al. (2016) e Manz et al. (2022)"
)
NEW_TABLE_88 = (
    "A separação evita usar indicadores internos como substitutos de conforto, "
    "satisfação ou qualidade de vida, respondendo ao desalinhamento discutido em "
    "revisões sobre próteses dos membros superior e inferior (Cordella et al., 2016; "
    "Manz et al., 2022)"
)
OLD_ENTRY = (
    "Manz, S. M., Menges, M. M., Schaffernicht, E., Mattes, K., & Kannenberg, A. "
    "(2022). A review of user needs to inform the development of lower-limb prostheses."
)
ENTRY_PREFIX = (
    "Manz, S., Valette, R., Damonte, F., Avanci Gaudio, L., Gonzalez-Vargas, J., "
    "Sartori, M., Dosen, S., & Rietman, J. (2022). A review of user needs to drive "
    "the development of lower limb prostheses. "
)
ENTRY_JOURNAL = "Journal of NeuroEngineering and Rehabilitation, 19"
ENTRY_SUFFIX = ", Article 119. https://doi.org/10.1186/s12984-022-01097-1"
NEW_ENTRY_DOCX = ENTRY_PREFIX + ENTRY_JOURNAL + ENTRY_SUFFIX
NEW_ENTRY_MD = ENTRY_PREFIX + f"*{ENTRY_JOURNAL}*" + ENTRY_SUFFIX


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def find_paragraph(root: etree._Element, exact: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == exact]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo para {exact[:70]!r}; encontrei {len(matches)}")
    return matches[0]


def replace_fragment(paragraph: etree._Element, old: str, new: str) -> None:
    nodes = paragraph.xpath(".//w:t", namespaces=NS)
    full = "".join(node.text or "" for node in nodes)
    if full.count(old) != 1:
        raise RuntimeError(f"Fragmento não unívoco: {old!r}")
    start = full.index(old)
    end = start + len(old)
    positions: list[tuple[etree._Element, int, int]] = []
    cursor = 0
    for node in nodes:
        value = node.text or ""
        positions.append((node, cursor, cursor + len(value)))
        cursor += len(value)
    first_node, first_start, _ = next(item for item in positions if item[2] > start)
    last_node, last_start, _ = next(item for item in positions if item[2] >= end and item[1] < end)
    prefix = (first_node.text or "")[: start - first_start]
    suffix = (last_node.text or "")[end - last_start :]
    if first_node is last_node:
        first_node.text = prefix + new + suffix
        set_space(first_node)
        return
    first_node.text = prefix + new
    set_space(first_node)
    clearing = False
    for node, _, _ in positions:
        if node is first_node:
            clearing = True
            continue
        if not clearing:
            continue
        if node is last_node:
            node.text = suffix
            set_space(node)
            break
        node.text = ""
        set_space(node)


def replace_full_text(paragraph: etree._Element, value: str) -> None:
    ppr = paragraph.find(qn("pPr"))
    ppr_copy = deepcopy(ppr) if ppr is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if ppr_copy is not None:
        paragraph.append(ppr_copy)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def add_run(paragraph: etree._Element, value: str, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        rpr = etree.SubElement(run, qn("rPr"))
        etree.SubElement(rpr, qn("i"))
        etree.SubElement(rpr, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_bibliography(paragraph: etree._Element) -> None:
    ppr = paragraph.find(qn("pPr"))
    ppr_copy = deepcopy(ppr) if ppr is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if ppr_copy is not None:
        paragraph.append(ppr_copy)
    add_run(paragraph, ENTRY_PREFIX)
    add_run(paragraph, ENTRY_JOURNAL, italic=True)
    add_run(paragraph, ENTRY_SUFFIX)


def state(root: etree._Element) -> dict[str, int]:
    text = text_of(root)
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "manz_citations": text.count("Manz et al., 2022")
        + text.count("Manz et al. (2022)"),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    replacements = [
        ("Versão do documento: 0.4.77", "Versão do documento: 0.4.78"),
        (OLD_SCOPE, NEW_SCOPE),
        (OLD_TRANSITION, NEW_TRANSITION),
        (OLD_TABLE_23, NEW_TABLE_23),
        (OLD_TABLE_88, NEW_TABLE_88),
        (OLD_ENTRY, NEW_ENTRY_MD),
    ]
    for old, new in replacements:
        if markdown.count(old) != 1:
            raise RuntimeError(f"Ocorrência Markdown inesperada para {old[:70]!r}")
        markdown = markdown.replace(old, new, 1)
    citation_count = markdown.count("Manz et al., 2022") + markdown.count(
        "Manz et al. (2022)"
    )
    if citation_count != 5:
        raise RuntimeError("A contagem das citações de Manz foi alterada no Markdown")
    return markdown


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
    before = state(root)
    if before["manz_citations"] != 5:
        raise RuntimeError(f"Contagem inicial inesperada: {before}")

    replace_full_text(find_paragraph(root, OLD_SCOPE), NEW_SCOPE)
    transition_matches = [
        p for p in root.xpath("//w:p", namespaces=NS) if OLD_TRANSITION in text_of(p)
    ]
    if len(transition_matches) != 1:
        raise RuntimeError("A transição de âmbito não é única no DOCX")
    replace_fragment(transition_matches[0], OLD_TRANSITION, NEW_TRANSITION)
    replace_full_text(find_paragraph(root, OLD_TABLE_23), NEW_TABLE_23)
    replace_full_text(find_paragraph(root, OLD_TABLE_88), NEW_TABLE_88)
    replace_bibliography(find_paragraph(root, OLD_ENTRY))
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível ou citações alteradas: {before} -> {after}")
    if text_of(root).count(NEW_ENTRY_DOCX) != 1:
        raise RuntimeError("A nova entrada bibliográfica não ficou íntegra no DOCX")

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
        "Manz et al. corrigido; âmbito explicitado; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, citações={after['manz_citations']}"
    )


if __name__ == "__main__":
    main()
