#!/usr/bin/env python3
"""Precisa a síntese dos resultados clínicos de Atallah et al. na Secção 2.4."""

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

OLD = (
    "A evidência disponível, contudo, obriga a uma leitura cautelosa. As revisões "
    "sistemáticas sobre próteses de membro superior impressas em 3D indicam que os "
    "resultados são promissores, mas continuam limitados por amostras pequenas, ausência "
    "de ensaios controlados, períodos curtos de acompanhamento e heterogeneidade nos "
    "instrumentos de avaliação. A literatura existente não demonstra superioridade "
    "robusta face a próteses convencionais nem permite concluir sobre efeitos de longo "
    "prazo em conforto, durabilidade ou qualidade de vida (Diment et al., 2018). Uma "
    "revisão mais recente sobre resultados clínicos de próteses impressas em 3D reforça "
    "a mesma cautela: há sinais de melhoria em destreza, satisfação e adequação, mas a "
    "qualidade da evidência permanece limitada e pouco comparável entre estudos "
    "(Atallah et al., 2025)."
)
NEW = (
    "A evidência disponível, contudo, obriga a uma leitura cautelosa. As revisões "
    "sistemáticas sobre próteses de membro superior impressas em 3D indicam que os "
    "resultados são promissores, mas continuam limitados por amostras pequenas, ausência "
    "de ensaios controlados, períodos curtos de acompanhamento e heterogeneidade nos "
    "instrumentos de avaliação. A literatura existente não demonstra superioridade "
    "robusta face a próteses convencionais nem permite concluir sobre efeitos de longo "
    "prazo em conforto, durabilidade ou qualidade de vida (Diment et al., 2018). Uma "
    "revisão mais recente dos resultados clínicos de próteses impressas em 3D reforça a "
    "mesma cautela. Nos estudos sobre o membro superior, foram relatadas melhorias na "
    "preensão global, na destreza manual e na satisfação dos utilizadores, tendo sido "
    "também avaliados o conforto, a facilidade de utilização e o uso quotidiano. Contudo, "
    "os estudos são geralmente pequenos, metodologicamente heterogéneos e difíceis de "
    "comparar entre si (Atallah et al., 2025)."
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


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
    if markdown.count("Versão do documento: 0.4.85") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    if markdown.count(OLD) != 1:
        raise RuntimeError("Parágrafo original não localizado de forma única no Markdown")
    markdown = markdown.replace(
        "Versão do documento: 0.4.85", "Versão do documento: 0.4.86", 1
    )
    return markdown.replace(OLD, NEW, 1)


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
    matches = [
        paragraph
        for paragraph in root.xpath("//w:p", namespaces=NS)
        if text_of(paragraph) == OLD
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
    before = state(root)
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = NEW
    after = state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    body = text_of(root)
    if body.count(OLD) != 0 or body.count(NEW) != 1:
        raise RuntimeError("A substituição no DOCX não ficou íntegra")

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
        "Síntese de Atallah et al. revista; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}"
    )


if __name__ == "__main__":
    main()
