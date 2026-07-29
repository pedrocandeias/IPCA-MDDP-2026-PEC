#!/usr/bin/env python3
"""Corrige a leitura comparativa PLA/PETG e integra as fontes da versão 0.4.51."""

from __future__ import annotations

import argparse
import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

MATERIAL_CONTEXT = (
    "Sobre a leitura estrutural dos parâmetros, importa distinguir os resultados desta dissertação "
    "do enquadramento da literatura. As estimativas do programa não medem resistência e a "
    "integridade de malha é geométrica, não mecânica. Hsueh et al. (2021) observaram, nas "
    "condições ensaiadas, maior módulo de Young e resistência no PLA e maior resistência à "
    "deformação térmica no PETG. Martins et al. (2024) registaram maior deformação até à rotura "
    "no PETG, correspondente a um comportamento mais dúctil, mas maior resistência à fadiga no "
    "PLA nas condições específicas do respectivo ensaio. Assim, o PETG pode ser contextualizado "
    "como mais dúctil e, nas condições estudadas, mais resistente à deformação térmica, mas não "
    "como material universalmente mais resistente e durável. Nesta dissertação, a observação "
    "física limita-se a que as peças em PETG foram impressas, manipuladas e medidas sem "
    "dificuldades impeditivas do procedimento. Não foi realizada uma comparação mecânica entre "
    "materiais."
)

CAN_AFFIRM = (
    "- Que as peças em PETG foram impressas, manipuladas e medidas sem dificuldades impeditivas "
    "do procedimento. Como enquadramento da literatura, o PETG apresentou maior resistência à "
    "deformação térmica no estudo de Hsueh et al. (2021) e maior ductilidade no estudo de Martins "
    "et al. (2024); estas propriedades não constituem resultados experimentais desta dissertação."
)

CANNOT_AFFIRM = (
    "- Que o PETG é, de forma geral, mais resistente, mais durável ou mais resistente à fadiga do "
    "que o PLA; essas comparações dependem do tipo de solicitação e das condições de fabrico e "
    "exigem ensaios mecânicos comparáveis."
)

HSUEH = (
    "Hsueh, M.-H., Lai, C.-J., Wang, S.-H., Zeng, Y.-S., Hsieh, C.-H., Pan, C.-Y., & Huang, "
    "W.-C. (2021). Effect of printing parameters on the thermal and mechanical properties of "
    "3D-printed PLA and PETG, using fused deposition modeling. Polymers, 13(11), 1758. "
    "https://doi.org/10.3390/polym13111758"
)

MARTINS = (
    "Martins, R. F., Branco, R., Martins, M., Macek, W., Marciniak, Z., Silva, R., Trindade, D., "
    "Moura, C., Franco, M., & Malça, C. (2024). Mechanical properties of additively manufactured "
    "polymeric materials—PLA and PETG—for biomechanical applications. Polymers, 16(13), 1868. "
    "https://doi.org/10.3390/polym16131868"
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS)).strip()


def paragraph_style(paragraph: etree._Element) -> str:
    values = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return values[0] if values else ""


def set_paragraph_text(paragraph: etree._Element, value: str) -> None:
    properties = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not properties:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value


def find_one(document: etree._Element, prefix: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_text(paragraph).startswith(prefix)
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo iniciado por {prefix!r}; encontrados {len(matches)}")
    return matches[0]


def insert_before(reference: etree._Element, template: etree._Element, value: str) -> None:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, value)
    reference.addprevious(paragraph)


def insert_after(reference: etree._Element, template: etree._Element, value: str) -> None:
    paragraph = deepcopy(template)
    set_paragraph_text(paragraph, value)
    reference.addnext(paragraph)


def update_annex_d_table_pages(document: etree._Element) -> int:
    pages = {"Tabela D.1": "157", "Tabela D.2": "158", "Tabela D.3": "163"}
    updated = 0
    for prefix, page in pages.items():
        matches = [
            paragraph
            for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
            if paragraph_style(paragraph).startswith("ndice")
            and paragraph_text(paragraph).startswith(prefix)
        ]
        if len(matches) != 1:
            raise RuntimeError(f"Esperada uma entrada local para {prefix}; encontradas {len(matches)}")
        nodes = matches[0].xpath(".//w:t", namespaces=NS)
        if len(nodes) < 2:
            raise RuntimeError(f"A entrada {prefix} não conserva a página num nó separado")
        nodes[-1].text = page
        updated += 1
    return updated


def apply(path: Path, bibliography: bool) -> dict[str, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = etree.fromstring(files["word/document.xml"])

    d44 = find_one(document, "D.4.4 Comparação entre entrada, malha e peça física")
    integrity = find_one(document, "Sobre integridade de malha:")
    context_matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if paragraph_text(paragraph).startswith("Sobre a leitura estrutural dos parâmetros")
    ]
    if len(context_matches) > 1:
        raise RuntimeError("Foi encontrado mais de um parágrafo de leitura estrutural")
    if context_matches:
        set_paragraph_text(context_matches[0], MATERIAL_CONTEXT)
    else:
        insert_before(d44, integrity, MATERIAL_CONTEXT)

    if not any(
        paragraph_text(paragraph).startswith("- Que as peças em PETG foram impressas")
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        old_can_start = find_one(document, "- Que, de forma qualitativa e relativa")
        old_can_end = old_can_start.getnext()
        if old_can_end is None or not paragraph_text(old_can_end).startswith("comportamento mecânico esperado:"):
            raise RuntimeError("Não foi localizado o segundo parágrafo da afirmação antiga sobre PETG")
        set_paragraph_text(old_can_start, CAN_AFFIRM)
        old_can_end.getparent().remove(old_can_end)

    first_limit_end = find_one(document, "reais das impressões, ou que as medições dimensionais")
    if not any(
        paragraph_text(paragraph).startswith("- Que o PETG é, de forma geral")
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
    ):
        insert_after(first_limit_end, first_limit_end, CANNOT_AFFIRM)

    inserted = 0
    if bibliography:
        all_text = [
            paragraph_text(paragraph)
            for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        ]
        if not any(text.startswith("Hsueh, M.-H.") for text in all_text):
            hu = find_one(document, "Hu, H., Li, Z.")
            insert_before(hu, hu, HSUEH)
            inserted += 1
        if not any(text.startswith("Martins, R. F., Branco") for text in all_text):
            menaka = find_one(document, "Menaka, S., Raja")
            insert_before(menaka, menaka, MARTINS)
            inserted += 1
        update_annex_d_table_pages(document)

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for item in items:
                output.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return {"bibliography_entries": inserted}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--bibliography", action="store_true")
    args = parser.parse_args()
    result = apply(args.docx.resolve(), args.bibliography)
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Entradas bibliográficas inseridas: {result['bibliography_entries']}")


if __name__ == "__main__":
    main()
