#!/usr/bin/env python3
"""Corrige a proveniência das Figuras 2.3/2.8 e as referências associadas."""

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

FIGURE_23_OLD_DOCX = (
    "Figura 2.3 — Fluxo digital entre aquisição, CAD/CAM e fabrico aditivo em "
    "próteses e ortóteses."
)
FIGURE_23_NEW = (
    "Figura 2.3 — Comparação entre os fluxos tradicional, CAD/CAM e de fabrico "
    "aditivo na produção de dispositivos protésicos."
)
FIGURE_23_TABLE_OLD = (
    "| Figura 2.3 | Fluxo digital entre aquisição, CAD/CAM e fabrico aditivo em "
    "próteses e ortóteses. |"
)
FIGURE_23_TABLE_NEW = (
    "| Figura 2.3 | Comparação entre os fluxos tradicional, CAD/CAM e de fabrico "
    "aditivo na produção de dispositivos protésicos. |"
)
FIGURE_28_OLD_DOCX = (
    "Figura 2.8 — Distribuição dos estudos por nível de prontidão tecnológica (TRL) "
    "e categoria de aplicação. O gráfico distingue estudos sobre próteses em geral, "
    "próteses de membro inferior produzidas por impressão 3D (LL 3DP), próteses de "
    "membro inferior desenvolvidas com recurso a CAD/CAM (LL CAD/CAM), outras "
    "abordagens aplicadas ao membro inferior (LL other), próteses de membro superior "
    "produzidas por impressão 3D (UL 3DP) e outros casos não enquadrados nas categorias "
    "anteriores."
)
FIGURE_28_OLD_MD = FIGURE_28_OLD_DOCX.replace("(LL other)", "(*LL other*)")
FIGURE_28_NEW = (
    "Figura 2.8 — Número de artigos por nível de prontidão tecnológica (TRL) e "
    "categoria de aplicação. O gráfico distingue próteses de membro inferior "
    "produzidas por impressão 3D (MI 3DP), próteses de membro inferior desenvolvidas "
    "com recurso a CAD/CAM (MI CAD/CAM), outras aplicações de membro inferior (MI "
    "outras), próteses de membro superior produzidas por impressão 3D (MS 3DP) e "
    "outras aplicações de membro superior (MS outras)."
)
FIGURE_28_TABLE_OLD = "| Figura 2.8 | " + FIGURE_28_OLD_MD.removeprefix("Figura 2.8 — ") + " |"
FIGURE_28_TABLE_NEW = "| Figura 2.8 | " + FIGURE_28_NEW.removeprefix("Figura 2.8 — ") + " |"

CHAINANDO_OLD = (
    "Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., "
    "Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing "
    "techniques to produce upper limb prostheses: Bibliometric analysis and scoping "
    "review. Prosthesis, 7(2), 26. "
    "https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517"
)
CHAINANDO_NEW_BEFORE_JOURNAL = (
    "Chainando, N., Martawidjaja, M., Darius, R. A., Yahya, L. C., Yemima, S., Tan, "
    "W. S., Harito, C., Chandra, R. C., Andhini, G. K., Putra, K. B., Lumban Tobing, "
    "C. C., Syafi’i, M., & Syafrudin, M. (2025). Applying 3D scanning and printing "
    "techniques to produce upper limb prostheses: Bibliometric analysis and scoping "
    "review. "
)
CHAINANDO_JOURNAL = "Prosthesis, 7"
CHAINANDO_NEW_AFTER_JOURNAL = (
    "(2), Article 26. https://doi.org/10.3390/prosthesis7020026"
)
CHAINANDO_NEW_MD = (
    CHAINANDO_NEW_BEFORE_JOURNAL
    + "*"
    + CHAINANDO_JOURNAL
    + "*"
    + CHAINANDO_NEW_AFTER_JOURNAL
)
CHAINANDO_NEW_DOCX = (
    CHAINANDO_NEW_BEFORE_JOURNAL
    + CHAINANDO_JOURNAL
    + CHAINANDO_NEW_AFTER_JOURNAL
)

OLDFREY_OLD = (
    "Oldfrey, B., Ramirez, D. Z. M., Miodownik, M., et al. (2024). A scoping review "
    "of digital fabrication techniques applied to prosthetics and orthotics: Part 1 "
    "of 2—Prosthetics. Prosthetics and Orthotics International. "
    "https://doi.org/10.1097/PXR.0000000000000351"
)
OLDFREY_NEW_BEFORE_JOURNAL = (
    "Oldfrey, B. M., Morgado Ramirez, D. Z., Miodownik, M., Wassall, M., Ramstrand, "
    "N., Wong, M. S., Danemayer, J., Dickinson, A., Kenney, L., Nester, C., Lemaire, "
    "E., Gholizadeth, H., Diment, L. E., Donovan-Hall, M. K., & Holloway, C. (2024). "
    "A scoping review of digital fabrication techniques applied to prosthetics and "
    "orthotics: Part 1 of 2—Prosthetics. "
)
OLDFREY_JOURNAL = "Prosthetics and Orthotics International, 48"
OLDFREY_NEW_AFTER_JOURNAL = (
    "(5), 574–589. https://doi.org/10.1097/PXR.0000000000000351"
)
OLDFREY_NEW_MD = (
    OLDFREY_NEW_BEFORE_JOURNAL
    + "*"
    + OLDFREY_JOURNAL
    + "*"
    + OLDFREY_NEW_AFTER_JOURNAL
)
OLDFREY_NEW_DOCX = (
    OLDFREY_NEW_BEFORE_JOURNAL + OLDFREY_JOURNAL + OLDFREY_NEW_AFTER_JOURNAL
)

SOURCE_23_NEW = "Adaptado da Figura 1 de Oldfrey et al. (2024, p. 575)."
SOURCE_28_NEW = "Adaptado da Figura 10 de Oldfrey et al. (2024, p. 582)."

BODY_SENTENCE_23 = (
    "Esta articulação é representada com clareza na Figura 2.3, que resume o "
    "encadeamento entre aquisição digital, modelação/rectificação e fabrico, "
    "evidenciando que a personalização depende da integração das várias etapas do "
    "fluxo de trabalho."
)
BODY_PARAGRAPH_CHAINANDO = (
    "A antropometria constitui um fundamento técnico e metodológico central no design "
    "protésico, porque a adequação geométrica do dispositivo ao corpo do utilizador "
    "condiciona directamente o conforto, a segurança, o desempenho funcional e a "
    "aceitação. Em próteses e tecnologias de apoio, a literatura recente evidencia uma "
    "transição progressiva de medições manuais baseadas em marcos anatómicos para "
    "processos digitais de captura de superfície (digitalização 3D e fotogrametria), "
    "integrados com fluxos CAD/CAM e com fabrico aditivo. Esta evolução é frequentemente "
    "descrita como uma cadeia “aquisição anatómica → modelação/retificação em CAD → "
    "fabrico aditivo → pós-processamento”, embora também se reconheça que muitos estudos "
    "permanecem em fases de prova de conceito e carecem de validação longitudinal e em "
    "larga escala (Chainando et al., 2025)."
)
BODY_PROSTHESES_CHAINANDO = (
    "– Próteses de membro superior: coexistência de tomografia computorizada (CT), "
    "scanners comerciais e fotogrametria como métodos de captura; estudos comparativos "
    "indicam que medições obtidas por digitalização 3D podem ser fiáveis e consistentes "
    "face a métodos tradicionais quando bem implementadas. Destacam-se também fluxos "
    "automatizados que adaptam modelos CAD inteligentes a dados de digitalização, "
    "reduzindo o intervalo entre a captura anatómica e a obtenção de um modelo pronto "
    "para fabrico (Chainando et al., 2025; Çıklaçandır et al., 2022)."
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


def rebuild_paragraph(
    paragraph: etree._Element, runs: list[tuple[str, bool]]
) -> None:
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo a substituir contém uma estrutura sensível")
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in runs:
        add_run(paragraph, value, italic=italic)


def replace_unique_paragraph(
    root: etree._Element,
    old: str,
    runs: list[tuple[str, bool]],
    *,
    label: str,
) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == old
    ]
    if len(matches) != 1:
        raise RuntimeError(f"{label}: esperava um parágrafo; encontrei {len(matches)}")
    rebuild_paragraph(matches[0], runs)


def replace_toc_title(root: etree._Element, old: str, new: str) -> None:
    matches = [
        node
        for node in root.xpath("//w:p[w:pPr/w:pStyle[@w:val='TOC1']]//w:t", namespaces=NS)
        if node.text == old
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Índice de figuras: esperava um título {old!r}; encontrei {len(matches)}"
        )
    matches[0].text = new
    set_space(matches[0])


def state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count("Versão do documento: 0.4.81") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(FIGURE_23_OLD_DOCX) != 1:
        raise RuntimeError("Número inesperado de títulos antigos da Figura 2.3")
    if markdown.count(FIGURE_28_OLD_MD) != 1:
        raise RuntimeError("Número inesperado de títulos antigos da Figura 2.8")
    if markdown.count(FIGURE_23_TABLE_OLD) != 1:
        raise RuntimeError("Entrada antiga da Figura 2.3 no índice não localizada")
    if markdown.count(FIGURE_28_TABLE_OLD) != 1:
        raise RuntimeError("Entrada antiga da Figura 2.8 no índice não localizada")
    if markdown.count(CHAINANDO_OLD) != 2:
        raise RuntimeError("Número inesperado de fontes Chainando sem marcação Markdown")
    chainando_source_link = (
        "Adaptado de "
        + CHAINANDO_OLD.replace(
            "https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517",
            "[https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517]"
            "(https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517)",
        )
    )
    chainando_source_plain = "Adaptado de " + CHAINANDO_OLD
    if markdown.count(chainando_source_link) != 1:
        raise RuntimeError("Fonte antiga da Figura 2.3 não localizada")
    if markdown.count(chainando_source_plain) != 1:
        raise RuntimeError("Fonte antiga da Figura 2.8 não localizada")
    chainando_bibliography = '<a id="ref-chainando-2025"></a> ' + CHAINANDO_OLD
    oldfrey_bibliography = '<a id="ref-oldfrey-2024"></a> ' + OLDFREY_OLD
    if markdown.count(chainando_bibliography) != 1:
        raise RuntimeError("Entrada Chainando antiga não localizada")
    if markdown.count(oldfrey_bibliography) != 1:
        raise RuntimeError("Entrada Oldfrey antiga não localizada")
    if markdown.count(BODY_SENTENCE_23) != 1:
        raise RuntimeError("Frase da Figura 2.3 que deve ser preservada não localizada")
    body_paragraph_md = BODY_PARAGRAPH_CHAINANDO.replace("design", "*design*", 1)
    if markdown.count(body_paragraph_md) != 1:
        raise RuntimeError("Parágrafo antropométrico que deve ser preservado não localizado")
    if markdown.count(BODY_PROSTHESES_CHAINANDO) != 1:
        raise RuntimeError("Síntese sobre próteses que deve ser preservada não localizada")

    markdown = markdown.replace(
        "Versão do documento: 0.4.81", "Versão do documento: 0.4.82", 1
    )
    markdown = markdown.replace(FIGURE_23_OLD_DOCX, FIGURE_23_NEW)
    markdown = markdown.replace(FIGURE_28_OLD_MD, FIGURE_28_NEW)
    markdown = markdown.replace(FIGURE_23_TABLE_OLD, FIGURE_23_TABLE_NEW, 1)
    markdown = markdown.replace(FIGURE_28_TABLE_OLD, FIGURE_28_TABLE_NEW, 1)
    markdown = markdown.replace(chainando_source_link, SOURCE_23_NEW, 1)
    markdown = markdown.replace(chainando_source_plain, SOURCE_28_NEW, 1)
    markdown = markdown.replace(
        chainando_bibliography,
        '<a id="ref-chainando-2025"></a> ' + CHAINANDO_NEW_MD,
        1,
    )
    markdown = markdown.replace(
        oldfrey_bibliography,
        '<a id="ref-oldfrey-2024"></a> ' + OLDFREY_NEW_MD,
        1,
    )
    if markdown.count(BODY_SENTENCE_23) != 1:
        raise RuntimeError("A frase da Figura 2.3 foi alterada inadvertidamente")
    if markdown.count(body_paragraph_md) != 1:
        raise RuntimeError("O parágrafo antropométrico foi alterado inadvertidamente")
    if markdown.count(BODY_PROSTHESES_CHAINANDO) != 1:
        raise RuntimeError("A síntese sobre próteses foi alterada inadvertidamente")
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
    body_before = text_of(root)
    if body_before.count(BODY_SENTENCE_23) != 1:
        raise RuntimeError("Frase da Figura 2.3 não localizada no DOCX")
    if body_before.count(BODY_PARAGRAPH_CHAINANDO) != 1:
        raise RuntimeError("Parágrafo antropométrico não localizado no DOCX")
    if body_before.count(BODY_PROSTHESES_CHAINANDO) != 1:
        raise RuntimeError("Síntese sobre próteses não localizada no DOCX")

    replace_toc_title(root, FIGURE_23_OLD_DOCX, FIGURE_23_NEW)
    replace_toc_title(root, FIGURE_28_OLD_DOCX, FIGURE_28_NEW)
    replace_unique_paragraph(
        root, FIGURE_23_OLD_DOCX, [(FIGURE_23_NEW, False)], label="Legenda 2.3"
    )
    replace_unique_paragraph(
        root, FIGURE_28_OLD_DOCX, [(FIGURE_28_NEW, False)], label="Legenda 2.8"
    )

    source_matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph).startswith("Adaptado de Chainando, N., Faephu, C.")
    ]
    if len(source_matches) != 2:
        raise RuntimeError(
            f"Esperava duas fontes Chainando nas figuras; encontrei {len(source_matches)}"
        )
    # A consulta XPath devolve a ordem documental: Figura 2.3, seguida da Figura 2.8.
    rebuild_paragraph(source_matches[0], [(SOURCE_23_NEW, False)])
    rebuild_paragraph(source_matches[1], [(SOURCE_28_NEW, False)])

    replace_unique_paragraph(
        root,
        CHAINANDO_OLD,
        [
            (CHAINANDO_NEW_BEFORE_JOURNAL, False),
            (CHAINANDO_JOURNAL, True),
            (CHAINANDO_NEW_AFTER_JOURNAL, False),
        ],
        label="Bibliografia Chainando",
    )
    replace_unique_paragraph(
        root,
        OLDFREY_OLD,
        [
            (OLDFREY_NEW_BEFORE_JOURNAL, False),
            (OLDFREY_JOURNAL, True),
            (OLDFREY_NEW_AFTER_JOURNAL, False),
        ],
        label="Bibliografia Oldfrey",
    )

    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body_after = text_of(root)
    checks = {
        FIGURE_23_NEW: 2,
        FIGURE_28_NEW: 2,
        SOURCE_23_NEW: 1,
        SOURCE_28_NEW: 1,
        CHAINANDO_NEW_DOCX: 1,
        OLDFREY_NEW_DOCX: 1,
        BODY_SENTENCE_23: 1,
        BODY_PARAGRAPH_CHAINANDO: 1,
        BODY_PROSTHESES_CHAINANDO: 1,
    }
    for expected, count in checks.items():
        actual = body_after.count(expected)
        if actual != count:
            raise RuntimeError(
                f"Validação DOCX falhou para {expected[:50]!r}: {actual} != {count}"
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
        "Figuras 2.3 e 2.8 e bibliografia corrigidas; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
