#!/usr/bin/env python3
"""Integra no manuscrito as referências normativas assinaladas nos comentários."""

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

OLD_REGULATION_MD = (
    "As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas "
    "à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância "
    "ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pelo "
    "Regulamento ([^2]EU) 2017/745 (MDR) - "
    "https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng, que classifica os dispositivos nas Classes "
    "I, IIa, IIb e III. Dispositivos terapêuticos activos, incluindo próteses mioeléctricas, "
    "enquadram-se geralmente nas classes intermédias ou superiores, o que exige avaliação por um "
    "organismo notificado para efeitos de marcação CE[^3] (Parlamento Europeu e Conselho da União "
    "Europeia, 2017)."
)
NEW_REGULATION_MD = (
    "As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas "
    "à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância "
    "ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pelo "
    "Regulamento (UE) 2017/745 (MDR), que classifica os dispositivos nas Classes I, IIa, IIb e III. "
    "Dispositivos terapêuticos activos, incluindo próteses mioeléctricas, enquadram-se geralmente "
    "nas classes intermédias ou superiores, o que exige avaliação por um organismo notificado para "
    "efeitos de marcação CE (Parlamento Europeu & Conselho da União Europeia, 2017)."
)

OLD_TC_MD = (
    "A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de "
    "biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de *software* e "
    "consideração explícita de factores humanos e de usabilidade. Normas desenvolvidas no âmbito "
    "do comité técnico ISO/TC 168[^4] contribuem para a padronização de requisitos aplicáveis a "
    "próteses e ortóteses. Adicionalmente, os fabricantes devem implementar sistemas de vigilância "
    "pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o "
    "que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar "
    "a sua evolução em evidência (Parlamento Europeu & Conselho da União Europeia, 2017; Resnik et "
    "al., 2010)."
)
NEW_TC_MD = (
    "A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de "
    "biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de *software* e "
    "consideração explícita de factores humanos e de usabilidade. O comité técnico ISO/TC 168 "
    "normaliza aspectos como o desempenho, a segurança, os factores ambientais e a possibilidade "
    "de intercâmbio entre componentes de próteses e ortóteses (ISO, n.d.). A ISO 8549-1:2020, "
    "preparada por este comité, estabelece a "
    "terminologia geral deste domínio (ISO, 2020). Adicionalmente, os fabricantes devem implementar sistemas de vigilância "
    "pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o "
    "que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar "
    "a sua evolução em evidência (Parlamento Europeu & Conselho da União Europeia, 2017; Resnik et "
    "al., 2010)."
)

OLD_STORY_MARKER = "Ron Mace[^5]"
NEW_STORY_MARKER = "Ron Mace"

OLD_IEC_MD = (
    "O *design* centrado no humano (*Human-Centred Design* – HCD) amplia esta perspectiva ao "
    "integrar dimensões culturais, contextuais e sistémicas. No desenvolvimento de dispositivos "
    "médicos, o HCD é associado a práticas como etnografia, *design* participativo, mapeamento de "
    "jornadas (*journey maps*), mapeamento de *stakeholders* e avaliação de factores humanos. A "
    "norma ISO 62366 define requisitos específicos para a aplicação da engenharia de usabilidade a "
    "dispositivos médicos, reforçando a integração formal de avaliações formativas, realizadas "
    "durante o desenvolvimento para orientar melhorias, e de avaliações finais de validação, "
    "destinadas a verificar o resultado do processo. (Fisher & Johansen, 2020; Millet et al., 2018)."
)
NEW_IEC_MD = (
    "O *design* centrado no humano (*Human-Centred Design* – HCD) amplia esta perspectiva ao "
    "integrar dimensões culturais, contextuais e sistémicas. No desenvolvimento de dispositivos "
    "médicos, o HCD é associado a práticas como etnografia, *design* participativo, mapeamento de "
    "jornadas (*journey maps*), mapeamento de *stakeholders* e avaliação de factores humanos. A "
    "norma IEC 62366-1:2015 estabelece um processo de engenharia de usabilidade para "
    "analisar, especificar, desenvolver e avaliar a utilização segura de dispositivos médicos "
    "(International Electrotechnical Commission [IEC], 2015). Este processo integra avaliações "
    "realizadas durante o desenvolvimento, destinadas a orientar melhorias, e uma avaliação final "
    "da interface no contexto de utilização previsto (Fisher & Johansen, 2020; Millet et al., 2018)."
)

OLD_7250_MD = (
    "Historicamente, a antropometria aplicada ao *design* baseou-se em medidas escalares "
    "(comprimentos, larguras, perímetros), obtidas com instrumentos como paquímetros, compassos "
    "antropométricos e fitas métricas, muitas vezes segundo procedimentos normalizados (por "
    "exemplo, a norma ISO 7250). Contudo, no *design* protésico — particularmente em interfaces "
    "corpo–dispositivo, como o encaixe (*socket*) — a literatura sublinha que a “forma” (*shape*) "
    "desempenha um papel determinante, pois pequenas variações volumétricas e distribuições de "
    "pressão podem gerar desconforto, lesões cutâneas e abandono do dispositivo. Estudos e revisões "
    "referem que o ajuste protésico pode exigir tolerâncias muito reduzidas e que a complexidade "
    "anatómica, bem como trajetórias de carga e zonas de alívio, não é devidamente capturada por um "
    "conjunto limitado de medidas lineares (Albin & Molenbroek, 2023; Young et al., 2023)."
)
NEW_7250_MD = (
    "Historicamente, a antropometria aplicada ao *design* baseou-se em medidas escalares "
    "(comprimentos, larguras, perímetros), obtidas com instrumentos como paquímetros, compassos "
    "antropométricos e fitas métricas, muitas vezes segundo procedimentos normalizados, como os "
    "definidos pela norma ISO 7250-1:2017 (ISO, 2017). Contudo, no *design* protésico — "
    "particularmente em interfaces corpo–dispositivo, como o encaixe (*socket*) — a literatura "
    "sublinha que a “forma” (*shape*) desempenha um papel determinante, pois pequenas variações "
    "volumétricas e distribuições de pressão podem gerar desconforto, lesões cutâneas e abandono do "
    "dispositivo. Estudos e revisões referem que o ajuste protésico pode exigir tolerâncias muito "
    "reduzidas e que a complexidade anatómica, bem como trajetórias de carga e zonas de alívio, não "
    "é devidamente capturada por um conjunto limitado de medidas lineares (Albin & Molenbroek, "
    "2023; Young et al., 2023)."
)

BIB_ANCHOR_MD = (
    '<a id="ref-idris-2024"></a> Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, '
    'N. (2024). Exploring the integration of artificial intelligence in co-design framework for '
    'designer. https://ebpj.e-iph.co.uk/index.php/EBProceedings/article/download/6348/3640'
)
BIB_BLOCK_MD = """<a id="ref-iec-62366-1-2015"></a> International Electrotechnical Commission. (2015). *Medical devices—Part 1: Application of usability engineering to medical devices* (IEC Standard No. 62366-1:2015). https://webstore.iec.ch/en/publication/21863

<a id="ref-iso-tc-168"></a> International Organization for Standardization. (n.d.). *ISO/TC 168: Prosthetics and orthotics*. Retrieved July 20, 2026, from https://www.iso.org/committee/53630.html

<a id="ref-iso-7250-1-2017"></a> International Organization for Standardization. (2017). *Basic human body measurements for technological design—Part 1: Body measurement definitions and landmarks* (ISO Standard No. 7250-1:2017). https://www.iso.org/standard/65246.html

<a id="ref-iso-8549-1-2020"></a> International Organization for Standardization. (2020). *Prosthetics and orthotics—Vocabulary—Part 1: General terms for external limb prostheses and external orthoses* (ISO Standard No. 8549-1:2020). https://www.iso.org/standard/79495.html"""

BIB_ENTRIES_DOCX = (
    (
        ("International Electrotechnical Commission. (2015). ", False),
        ("Medical devices—Part 1: Application of usability engineering to medical devices", True),
        (
            " (IEC Standard No. 62366-1:2015). "
            "https://webstore.iec.ch/en/publication/21863",
            False,
        ),
    ),
    (
        ("International Organization for Standardization. (n.d.). ", False),
        ("ISO/TC 168: Prosthetics and orthotics", True),
        (
            ". Retrieved July 20, 2026, from https://www.iso.org/committee/53630.html",
            False,
        ),
    ),
    (
        ("International Organization for Standardization. (2017). ", False),
        (
            "Basic human body measurements for technological design—Part 1: Body measurement "
            "definitions and landmarks",
            True,
        ),
        (
            " (ISO Standard No. 7250-1:2017). https://www.iso.org/standard/65246.html",
            False,
        ),
    ),
    (
        ("International Organization for Standardization. (2020). ", False),
        (
            "Prosthetics and orthotics—Vocabulary—Part 1: General terms for external limb "
            "prostheses and external orthoses",
            True,
        ),
        (
            " (ISO Standard No. 8549-1:2020). https://www.iso.org/standard/79495.html",
            False,
        ),
    ),
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


def add_run(paragraph: etree._Element, value: str, *, italic: bool) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_run_text(root: etree._Element, old: str, new: str) -> None:
    matches = [
        node for node in root.xpath("//w:t", namespaces=NS) if (node.text or "") == old
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Segmento DOCX inesperado para {old[:70]!r}: {len(matches)}")
    matches[0].text = new
    set_space(matches[0])


def sensitive_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnotes": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comments": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
        "tables": int(root.xpath("count(//w:tbl)", namespaces=NS)),
    }


def update_docx_text(root: etree._Element) -> None:
    replace_run_text(
        root,
        "Regulamento 2017/745 (MDR) - https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng",
        "Regulamento (UE) 2017/745 (MDR)",
    )
    replace_run_text(
        root,
        "CE (Parlamento Europeu e Conselho da União Europeia, 2017).",
        "CE (Parlamento Europeu & Conselho da União Europeia, 2017).",
    )
    replace_run_text(
        root,
        (
            " e consideração explícita de fatores humanos e de usabilidade. Normas desenvolvidas "
            "no âmbito do comité técnico "
        ),
        " e consideração explícita de fatores humanos e de usabilidade. O comité técnico ",
    )
    replace_run_text(
        root,
        (
            " contribuem para a padronização de requisitos aplicáveis a próteses e ortóteses. "
            "Adicionalmente, os fabricantes devem implementar sistemas de vigilância "
            "pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do "
            "dispositivo, o que reforça a natureza regulada e iterativa deste domínio, bem como a "
            "necessidade de sustentar a sua evolução em evidência (Parlamento Europeu & Conselho "
            "da União Europeia, 2017; Resnik et al., 2010)."
        ),
        (
            " normaliza aspetos como o desempenho, a segurança, os fatores ambientais e a "
            "possibilidade de intercâmbio entre componentes de próteses e ortóteses (ISO, n.d.). "
            "A ISO 8549-1:2020, preparada por este comité, estabelece a terminologia geral deste "
            "domínio (ISO, 2020). Adicionalmente, os "
            "fabricantes devem implementar "
            "sistemas de vigilância pós-comercialização, recolhendo dados de uso real ao longo do "
            "ciclo de vida do dispositivo, o que reforça a natureza regulada e iterativa deste "
            "domínio, bem como a necessidade de sustentar a sua evolução em evidência (Parlamento "
            "Europeu & Conselho da União Europeia, 2017; Resnik et al., 2010)."
        ),
    )
    replace_run_text(root, "ISO 62366", "IEC 62366-1:2015")
    replace_run_text(
        root,
        (
            " define requisitos específicos para a aplicação da engenharia de usabilidade a "
            "dispositivos médicos, reforçando a integração formal de avaliações formativas, "
            "realizadas durante o desenvolvimento para orientar melhorias, e de avaliações finais "
            "de validação, destinadas a verificar o resultado do processo. (Fisher & Johansen, "
            "2020; Millet et al., 2018)."
        ),
        (
            " estabelece um processo de engenharia de usabilidade para analisar, especificar, "
            "desenvolver e avaliar a utilização segura de dispositivos médicos (International "
            "Electrotechnical Commission [IEC], 2015). Este processo integra avaliações realizadas "
            "durante o desenvolvimento, destinadas a orientar melhorias, e uma avaliação final da "
            "interface no contexto de utilização previsto (Fisher & Johansen, 2020; Millet et al., "
            "2018)."
        ),
    )
    before_7250 = [
        node
        for node in root.xpath("//w:t", namespaces=NS)
        if (node.text or "").endswith(
            "muitas vezes segundo procedimentos normalizados (por exemplo, a norma "
        )
    ]
    if len(before_7250) != 1:
        raise RuntimeError(f"Prefixo ISO 7250 inesperado: {len(before_7250)}")
    before_7250[0].text = (before_7250[0].text or "").replace(
        "muitas vezes segundo procedimentos normalizados (por exemplo, a norma ",
        "muitas vezes segundo procedimentos normalizados, como os definidos pela norma ",
    )
    set_space(before_7250[0])
    replace_run_text(root, "ISO 7250", "ISO 7250-1:2017")
    after_7250 = [
        node
        for node in root.xpath("//w:t", namespaces=NS)
        if (node.text or "").startswith("). Contudo, no ")
    ]
    if len(after_7250) != 1:
        raise RuntimeError(f"Sufixo ISO 7250 inesperado: {len(after_7250)}")
    after_7250[0].text = (after_7250[0].text or "").replace(
        "). Contudo, no ", " (ISO, 2017). Contudo, no ", 1
    )
    set_space(after_7250[0])


def insert_docx_bibliography(root: etree._Element) -> None:
    anchors = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph).startswith(
            "Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, N. (2024)."
        )
    ]
    if len(anchors) != 1:
        raise RuntimeError(f"Âncora bibliográfica inesperada: {len(anchors)}")
    anchor = anchors[0]
    properties = anchor.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    current = anchor
    for parts in BIB_ENTRIES_DOCX:
        paragraph = etree.Element(qn("p"))
        if properties_copy is not None:
            paragraph.append(deepcopy(properties_copy))
        for value, italic in parts:
            add_run(paragraph, value, italic=italic)
        current.addnext(paragraph)
        current = paragraph


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    checks = {
        "Versão do documento: 0.4.95": 1,
        OLD_REGULATION_MD: 1,
        NEW_REGULATION_MD: 0,
        OLD_TC_MD: 1,
        NEW_TC_MD: 0,
        OLD_STORY_MARKER: 1,
        OLD_IEC_MD: 1,
        NEW_IEC_MD: 0,
        OLD_7250_MD: 1,
        NEW_7250_MD: 0,
        BIB_ANCHOR_MD: 1,
        BIB_BLOCK_MD: 0,
    }
    for value, expected in checks.items():
        actual = markdown.count(value)
        if actual != expected:
            raise RuntimeError(
                f"Contagem Markdown inesperada para {value[:70]!r}: {actual} != {expected}"
            )
    markdown = markdown.replace(
        "Versão do documento: 0.4.95", "Versão do documento: 0.4.96", 1
    )
    for old, new in (
        (OLD_REGULATION_MD, NEW_REGULATION_MD),
        (OLD_TC_MD, NEW_TC_MD),
        (OLD_STORY_MARKER, NEW_STORY_MARKER),
        (OLD_IEC_MD, NEW_IEC_MD),
        (OLD_7250_MD, NEW_7250_MD),
    ):
        markdown = markdown.replace(old, new, 1)
    return markdown.replace(BIB_ANCHOR_MD, f"{BIB_ANCHOR_MD}\n\n{BIB_BLOCK_MD}", 1)


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
    update_docx_text(root)
    insert_docx_bibliography(root)
    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    for required in (
        "Regulamento (UE) 2017/745 (MDR)",
        "IEC 62366-1:2015",
        "ISO 7250-1:2017",
        "International Organization for Standardization. (2020). Prosthetics and orthotics",
    ):
        if required not in body:
            raise RuntimeError(f"Conteúdo DOCX em falta: {required}")

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
        "Referências normativas integradas; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
