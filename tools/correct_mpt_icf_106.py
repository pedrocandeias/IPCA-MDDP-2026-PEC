#!/usr/bin/env python3
"""Corrige as fontes da passagem sobre MPT e ICF na Secção 2.2."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import NS, qn, sensitive_state, set_space, text_of


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

OLD_MD = (
    "Em contextos de tecnologias de apoio, modelos como o *Matching Person and "
    "Technology* (MPT) e quadros conceptuais baseados na Classificação Internacional de "
    "Funcionalidade (ICF) são utilizados para apoiar decisões de selecção e de adequação "
    "tecnológica, promovendo o alinhamento entre as características do utilizador, do "
    "ambiente e do dispositivo (White & Mosca, 2022)."
)
OLD_DOCX = OLD_MD.replace("*", "")
NEW_MD = (
    "Na selecção de tecnologias de apoio, o modelo *Matching Person and Technology* "
    "(MPT) procura relacionar as capacidades e perspectivas da pessoa com uma tecnologia "
    "específica e com o ambiente em que será utilizada (van Niekerk et al., 2018). De "
    "forma complementar, a Classificação Internacional de Funcionalidade, Incapacidade e "
    "Saúde (ICF) considera a interacção entre a condição de saúde e os factores pessoais e "
    "ambientais, entre os quais se incluem os produtos e as tecnologias (Howard, Fisher, "
    "et al., 2022). Para o *design*, estes enquadramentos mostram que a adequação do "
    "dispositivo não depende apenas das suas características técnicas, mas também da "
    "correspondência com as necessidades e o contexto de utilização da pessoa."
)
NEW_BODY_PARTS = (
    ("Na selecção de tecnologias de apoio, o modelo ", False),
    ("Matching Person and Technology", True),
    (
        " (MPT) procura relacionar as capacidades e perspectivas da pessoa com uma "
        "tecnologia específica e com o ambiente em que será utilizada (van Niekerk et "
        "al., 2018). De forma complementar, a Classificação Internacional de "
        "Funcionalidade, Incapacidade e Saúde (ICF) considera a interacção entre a "
        "condição de saúde e os factores pessoais e ambientais, entre os quais se "
        "incluem os produtos e as tecnologias (Howard, Fisher, et al., 2022). Para o ",
        False,
    ),
    ("design", True),
    (
        ", estes enquadramentos mostram que a adequação do dispositivo não depende "
        "apenas das suas características técnicas, mas também da correspondência com "
        "as necessidades e o contexto de utilização da pessoa.",
        False,
    ),
)
NEW_DOCX = "".join(value for value, _ in NEW_BODY_PARTS)

HOWARD_ANCHOR = (
    '<a id="ref-howard-2022"></a> Howard, D., Davies, L., Dwyer, A., & Williams, J. '
    "(2022). Assessing the use of co-design to produce bespoke assistive technology "
    "solutions within a current healthcare service: A service evaluation."
)
HOWARD_NEW_MD = (
    '<a id="ref-howard-fisher-2022"></a> Howard, J., Fisher, Z., Kemp, A. H., Lindsay, '
    "S., Tasker, L. H., & Tree, J. J. (2022). Exploring the barriers to using assistive "
    "technology for individuals with chronic conditions: A meta-synthesis review. "
    "*Disability and Rehabilitation: Assistive Technology, 17*(4), 390–408. "
    "https://doi.org/10.1080/17483107.2020.1788181"
)
HOWARD_NEW_PARTS = (
    (
        "Howard, J., Fisher, Z., Kemp, A. H., Lindsay, S., Tasker, L. H., & Tree, J. J. "
        "(2022). Exploring the barriers to using assistive technology for individuals "
        "with chronic conditions: A meta-synthesis review. ",
        False,
    ),
    ("Disability and Rehabilitation: Assistive Technology, 17", True),
    ("(4), 390–408. https://doi.org/10.1080/17483107.2020.1788181", False),
)
HOWARD_NEW_DOCX = "".join(value for value, _ in HOWARD_NEW_PARTS)

NAG_ANCHOR = (
    '<a id="ref-nag-2003"></a> Nag, A., Nag, P. K., & Desai, H. (2003). Hand '
    "anthropometry of Indian women. Indian Journal of Medical Research, 117, 260-269."
)
VAN_NIEKERK_NEW_MD = (
    '<a id="ref-van-niekerk-2018"></a> van Niekerk, K., Dada, S., Tönsing, K., & '
    "Boshoff, K. (2018). Factors perceived by rehabilitation professionals to influence "
    "the provision of assistive technology to children: A systematic review. *Physical "
    "& Occupational Therapy in Pediatrics, 38*(2), 168–189. "
    "https://doi.org/10.1080/01942638.2017.1337661"
)
VAN_NIEKERK_NEW_PARTS = (
    (
        "van Niekerk, K., Dada, S., Tönsing, K., & Boshoff, K. (2018). Factors perceived "
        "by rehabilitation professionals to influence the provision of assistive "
        "technology to children: A systematic review. ",
        False,
    ),
    ("Physical & Occupational Therapy in Pediatrics, 38", True),
    ("(2), 168–189. https://doi.org/10.1080/01942638.2017.1337661", False),
)
VAN_NIEKERK_NEW_DOCX = "".join(value for value, _ in VAN_NIEKERK_NEW_PARTS)


def add_run(paragraph: etree._Element, value: str, *, italic: bool) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_paragraph(
    root: etree._Element, old: str, parts: tuple[tuple[str, bool], ...]
) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == old
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo MPT/ICF inesperado no DOCX: {len(matches)}")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo MPT/ICF contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


def insert_bibliography_paragraph(
    root: etree._Element,
    anchor_text: str,
    parts: tuple[tuple[str, bool], ...],
) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == anchor_text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Âncora bibliográfica inesperada no DOCX: {len(matches)}")
    anchor = matches[0]
    paragraph = deepcopy(anchor)
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)
    anchor.addnext(paragraph)


def replace_version(root: etree._Element) -> None:
    old = "Versão do documento: 0.4.105"
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == old
    ]
    if len(matches) > 1:
        raise RuntimeError(f"Versão inesperada no DOCX: {len(matches)}")
    if matches:
        replace_paragraph(root, old, (("Versão do documento: 0.4.106", False),))


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = (
        ("Versão do documento: 0.4.105", 1),
        (OLD_MD, 1),
        (NEW_MD, 0),
        (HOWARD_ANCHOR, 1),
        (HOWARD_NEW_MD, 0),
        (NAG_ANCHOR, 1),
        (VAN_NIEKERK_NEW_MD, 0),
    )
    for value, expected in checks:
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada: {actual} != {expected} para {value[:80]!r}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.105", "Versão do documento: 0.4.106", 1
    )
    markdown = markdown.replace(OLD_MD, NEW_MD, 1)
    markdown = markdown.replace(
        HOWARD_ANCHOR, f"{HOWARD_ANCHOR}\n\n{HOWARD_NEW_MD}", 1
    )
    markdown = markdown.replace(
        NAG_ANCHOR, f"{NAG_ANCHOR}\n\n{VAN_NIEKERK_NEW_MD}", 1
    )
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
    before = sensitive_state(root)

    replace_paragraph(root, OLD_DOCX, NEW_BODY_PARTS)
    replace_version(root)
    insert_bibliography_paragraph(
        root,
        HOWARD_ANCHOR.split("></a> ", 1)[1],
        HOWARD_NEW_PARTS,
    )
    insert_bibliography_paragraph(
        root,
        NAG_ANCHOR.split("></a> ", 1)[1],
        VAN_NIEKERK_NEW_PARTS,
    )

    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    paragraphs = [text_of(p) for p in root.xpath("//w:p", namespaces=NS)]
    for value, expected in (
        (OLD_DOCX, 0),
        (NEW_DOCX, 1),
        (HOWARD_NEW_DOCX, 1),
        (VAN_NIEKERK_NEW_DOCX, 1),
    ):
        actual = paragraphs.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Validação DOCX inesperada: {actual} != {expected} para {value[:80]!r}"
            )

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
        "Passagem MPT/ICF e duas referências corrigidas; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
