#!/usr/bin/env python3
"""Corrige o texto, a legenda e a fonte da Figura 2.2 no Markdown e no DOCX."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

OLD_LIST = (
    "Figura 2.2 — Utilização, rejeição primária e rejeição secundária de próteses "
    "do membro superior adquiridas."
)
NEW_LIST = (
    "Figura 2.2 — Utilização continuada, rejeição primária e rejeição secundária "
    "de próteses numa amostra de adultos com amputação adquirida do membro superior."
)
OLD_TEXT = (
    "A Figura 2.2 sintetiza claramente esta persistência do abandono ao relacionar "
    "o uso, a rejeição primária e a rejeição secundária. Esta relação mostra que o "
    "problema não é marginal, mas estrutural no campo das próteses de membro superior."
)
NEW_TEXT = (
    "A Figura 2.2 apresenta a distribuição observada por Østlie et al. (2012) numa "
    "amostra populacional de 224 adultos com amputação adquirida do membro superior. "
    "Nesse estudo, 4,5% dos participantes apresentavam rejeição primária da prótese e "
    "13,4% dos 209 participantes que tinham iniciado a sua utilização interromperam-na "
    "posteriormente. Estes resultados permitem distinguir a rejeição anterior à "
    "primeira utilização da rejeição ocorrida após a adoção inicial do dispositivo."
)
OLD_SOURCE_MD = (
    "Reproduzido de Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design "
    "priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive "
    "Technology, 2(6), 346-357. "
    "[https://doi.org/10.1080/17483100701714733]"
    "(https://doi.org/10.1080/17483100701714733)"
)
OLD_SOURCE_DOCX = (
    "Reproduzido de Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design "
    "priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive "
    "Technology, 2(6), 346-357. https://doi.org/10.1080/17483100701714733 "
    "(https://doi.org/10.1080/17483100701714733)"
)
NEW_SOURCE_PARTS = (
    (
        "Adaptado da Figura 1 de Østlie, K., Lesjø, I. M., Franklin, R. J., Garfelt, "
        "B., Skjeldal, O. H., & Magnus, P. (2012). Prosthesis rejection in acquired "
        "major upper-limb amputees: A population-based survey. ",
        False,
    ),
    ("Disability and Rehabilitation: Assistive Technology, 7", True),
    ("(4), 294–303. https://doi.org/10.3109/17483107.2011.635405", False),
)
NEW_SOURCE_MD = "".join(
    f"*{value}*" if italic else value for value, italic in NEW_SOURCE_PARTS
)
OLD_BIB = (
    "Oldfrey, B. M., Morgado Ramirez, D. Z., Miodownik, M., Wassall, M., Ramstrand, "
    "N., Wong, M. S., Danemayer, J., Dickinson, A., Kenney, L., Nester, C., Lemaire, "
    "E., Gholizadeth, H., Diment, L. E., Donovan-Hall, M. K., & Holloway, C. (2024). "
    "A scoping review of digital fabrication techniques applied to prosthetics and "
    "orthotics: Part 1 of 2—Prosthetics. Prosthetics and Orthotics International, "
    "48(5), 574–589. https://doi.org/10.1097/PXR.0000000000000351"
)
NEW_BIB_PARTS = (
    (
        "Østlie, K., Lesjø, I. M., Franklin, R. J., Garfelt, B., Skjeldal, O. H., & "
        "Magnus, P. (2012). Prosthesis rejection in acquired major upper-limb "
        "amputees: A population-based survey. ",
        False,
    ),
    ("Disability and Rehabilitation: Assistive Technology, 7", True),
    ("(4), 294–303. https://doi.org/10.3109/17483107.2011.635405", False),
)
NEW_BIB_MD = (
    '<a id="ref-ostlie-2012"></a> '
    + "".join(f"*{value}*" if italic else value for value, italic in NEW_BIB_PARTS)
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_space(node: etree._Element) -> None:
    value = node.text or ""
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")
    else:
        node.attrib.pop(XML_SPACE, None)


def add_run(paragraph: etree._Element, value: str, *, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def unique_paragraph(root: etree._Element, text: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == text]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo para {text[:60]!r}; encontrei {len(matches)}")
    return matches[0]


def replace_paragraph(
    root: etree._Element, old: str, parts: tuple[tuple[str, bool], ...]
) -> None:
    paragraph = unique_paragraph(root, old)
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo a substituir contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


def replace_list_entry(root: etree._Element) -> None:
    paragraph = unique_paragraph(root, OLD_LIST + "8")
    texts = paragraph.xpath(".//w:t", namespaces=NS)
    if len(texts) != 2 or (texts[1].text or "") != "8":
        raise RuntimeError("Estrutura inesperada na entrada da lista de figuras")
    texts[0].text = NEW_LIST


def insert_bibliography_entry(root: etree._Element) -> None:
    oldfrey = unique_paragraph(root, OLD_BIB)
    paragraph = deepcopy(oldfrey)
    for child in list(paragraph):
        if child.tag != qn("pPr"):
            paragraph.remove(child)
    for value, italic in NEW_BIB_PARTS:
        add_run(paragraph, value, italic=italic)
    oldfrey.addnext(paragraph)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = {
        "Versão do documento: 0.4.87": 1,
        f"| {OLD_LIST.replace(' — ', ' | ', 1)} | 8 |": 1,
        OLD_TEXT: 1,
        OLD_LIST: 1,
        OLD_SOURCE_MD: 1,
        '<a id="ref-oldfrey-2024"></a> ': 1,
        '<a id="ref-ostlie-2012"></a> ': 0,
    }
    for value, expected in checks.items():
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada para {value[:70]!r}: {actual} != {expected}"
            )
    old_list_row = f"| {OLD_LIST.replace(' — ', ' | ', 1)} | 8 |"
    new_list_row = f"| {NEW_LIST.replace(' — ', ' | ', 1)} | 8 |"
    markdown = markdown.replace(
        "Versão do documento: 0.4.87", "Versão do documento: 0.4.88", 1
    )
    markdown = markdown.replace(old_list_row, new_list_row, 1)
    markdown = markdown.replace(OLD_TEXT, NEW_TEXT, 1)
    markdown = markdown.replace(OLD_LIST, NEW_LIST, 1)
    markdown = markdown.replace(OLD_SOURCE_MD, NEW_SOURCE_MD, 1)
    marker = '<a id="ref-openscad-community-nd"></a> '
    if markdown.count(marker) != 1:
        raise RuntimeError("Ponto de inserção bibliográfico não localizado")
    markdown = markdown.replace(marker, NEW_BIB_MD + "\n\n" + marker, 1)
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

    replace_list_entry(root)
    replace_paragraph(root, OLD_TEXT, ((NEW_TEXT, False),))
    replace_paragraph(root, OLD_LIST, ((NEW_LIST, False),))
    replace_paragraph(root, OLD_SOURCE_DOCX, NEW_SOURCE_PARTS)
    insert_bibliography_entry(root)

    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    new_source = "".join(value for value, _ in NEW_SOURCE_PARTS)
    new_bib = "".join(value for value, _ in NEW_BIB_PARTS)
    for old in (OLD_TEXT, OLD_SOURCE_DOCX):
        if old in body:
            raise RuntimeError(f"Permaneceu no DOCX a passagem original {old[:60]!r}")
    if body.count(NEW_TEXT) != 1 or body.count(new_source) != 1 or body.count(new_bib) != 2:
        raise RuntimeError("As novas passagens não ficaram íntegras no DOCX")
    if body.count(NEW_LIST) != 2:
        raise RuntimeError("A legenda nova não ficou sincronizada na lista e no corpo")

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
        "Figura 2.2 atribuída a Østlie et al. (2012); "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
