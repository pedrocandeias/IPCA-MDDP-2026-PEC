#!/usr/bin/env python3
"""Delimita as duas utilizações de Chainando et al. na Secção 2.5."""

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

OLD_1_DOCX = (
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
OLD_1_MD = OLD_1_DOCX.replace("no design protésico", "no *design* protésico", 1)

NEW_1_PARTS = (
    ("A antropometria constitui um fundamento técnico e metodológico central no ", False),
    ("design", True),
    (" protésico, porque a adequação geométrica do dispositivo ao corpo do utilizador "
     "condiciona directamente o conforto, a segurança, o desempenho funcional e a "
     "aceitação. Em próteses de membro superior, observa-se uma utilização crescente de "
     "processos digitais de captura da geometria corporal, incluindo a digitalização 3D e "
     "a fotogrametria. Estes métodos permitem obter medições destinadas à personalização "
     "das próteses, ajustar o desenho em ", False),
    ("software", True),
    (" e produzir componentes por impressão 3D (Chainando et al., 2025). Nesta "
     "investigação, estes passos são organizados numa cadeia de trabalho composta por "
     "aquisição anatómica, modelação ou rectificação em CAD, fabrico aditivo e "
     "pós-processamento. Esta cadeia corresponde à organização metodológica adoptada no "
     "projecto e não a um protocolo único estabelecido pela revisão.", False),
)

OLD_2 = (
    "– Próteses de membro superior: coexistência de tomografia computorizada (CT), "
    "scanners comerciais e fotogrametria como métodos de captura; estudos comparativos "
    "indicam que medições obtidas por digitalização 3D podem ser fiáveis e consistentes "
    "face a métodos tradicionais quando bem implementadas. Destacam-se também fluxos "
    "automatizados que adaptam modelos CAD inteligentes a dados de digitalização, "
    "reduzindo o intervalo entre a captura anatómica e a obtenção de um modelo pronto "
    "para fabrico (Chainando et al., 2025; Çıklaçandır et al., 2022)."
)
NEW_2 = (
    "– Próteses de membro superior: Chainando et al. (2025) identificam a tomografia "
    "computorizada (CT), os digitalizadores 3D comerciais e a fotogrametria como os três "
    "principais métodos digitais de captura. A revisão assinala que estas técnicas permitem "
    "obter medições destinadas à personalização, mas também apresentam diferenças de "
    "precisão, custo, acessibilidade e requisitos técnicos. Num estudo que comparou "
    "medições tradicionais, ressonância magnética e digitalização 3D, Çıklaçandır et al. "
    "(2022) não encontraram diferenças estatisticamente significativas entre os métodos. A "
    "digitalização 3D apresentou resultados próximos dos obtidos por ressonância magnética "
    "e vantagens potenciais relacionadas com o custo, o tempo, a fiabilidade e a "
    "repetibilidade."
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


def replace_paragraph(
    root: etree._Element, old: str, parts: tuple[tuple[str, bool], ...]
) -> None:
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == old
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperava um parágrafo no DOCX; encontrei {len(matches)}")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError("O parágrafo contém uma estrutura sensível")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count("Versão do documento: 0.4.86") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(OLD_1_MD) != 1 or markdown.count(OLD_2) != 1:
        raise RuntimeError("Passagens originais não localizadas de forma única no Markdown")
    new_1_md = "".join(
        f"*{value}*" if italic else value for value, italic in NEW_1_PARTS
    )
    markdown = markdown.replace(
        "Versão do documento: 0.4.86", "Versão do documento: 0.4.87", 1
    )
    return markdown.replace(OLD_1_MD, new_1_md, 1).replace(OLD_2, NEW_2, 1)


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
    replace_paragraph(root, OLD_1_DOCX, NEW_1_PARTS)
    replace_paragraph(root, OLD_2, ((NEW_2, False),))
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    new_1_docx = "".join(value for value, _ in NEW_1_PARTS)
    if any(body.count(old) != 0 for old in (OLD_1_DOCX, OLD_2)):
        raise RuntimeError("Uma passagem original permaneceu no DOCX")
    if body.count(new_1_docx) != 1 or body.count(NEW_2) != 1:
        raise RuntimeError("As substituições no DOCX não ficaram íntegras")

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
        "Chainando et al. delimitado em duas passagens; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
