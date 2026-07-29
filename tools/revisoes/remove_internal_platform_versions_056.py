#!/usr/bin/env python3
"""Remove identificadores internos de versão da plataforma no manuscrito 0.4.56."""

from __future__ import annotations

import os
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


REPLACEMENTS = [
    ("Versão do documento: 0.4.55", "Versão do documento: 0.4.56"),
    ("Exportação em placa nas versões 14.15.0 e seguintes", "Ensaios de exportação em placa"),
    (", versão 14.16.0", ""),
    (", versão 14.17.0", ""),
    (", versão 14.18.0", ""),
    (", versões 14.19.0–14.20.0", ""),
    (", versão 14.22.0", ""),
    ("Registo de versões, dez testes unitários aprovados na versão 14.67.0", "Registo das iterações, dez testes unitários aprovados"),
    ("As versões são identificadas por actividade.", "Os estados examinados são identificados pela actividade a que correspondem."),
    ("Os ensaios iniciais de correspondência e geometria incidiram na versão 14.67.0", "Os ensaios iniciais de correspondência e geometria incidiram no estado usado nos ensaios principais"),
    ("as séries complementares da plataforma do Anexo B foram executadas na versão 14.69.0", "as séries complementares da plataforma do Anexo B foram executadas num estado posterior"),
    ("e o estado actual examinado corresponde à versão 14.72.0", "e a descrição técnica considera o estado final examinado"),
    ("origem, licença, versão, estratégia de escala", "origem, licença, estado de integração, estratégia de escala"),
    ("A versão 14.67.0 corresponde ao fecho dos ensaios principais e ao dicionário suplementar arquivado.", "O estado usado nos ensaios principais corresponde ao dicionário suplementar arquivado."),
    ("A versão 14.71.0 acrescentou", "Uma revisão posterior acrescentou"),
    ("A versão 14.72.0 uniformizou", "O estado final examinado uniformizou"),
    ("concluídos na versão 14.67.0", "concluídos anteriormente"),
    ("Na versão 14.72.0", "No estado final examinado"),
    ("O dicionário corresponde à versão 14.67.0 da plataforma.", "O dicionário corresponde ao estado da plataforma usado nos ensaios principais."),
    ("O Anexo C complementa o dicionário da versão 14.67.0", "O Anexo C complementa o dicionário usado nos ensaios principais"),
    ("As versões posteriores ao fecho da comparação principal", "As alterações posteriores ao fecho da comparação principal"),
    ("; 14.10–14.11", ""),
    ("; 14.16–14.17", ""),
    ("; 14.18", ""),
    ("; 14.19", ""),
    ("; 14.32–14.37", ""),
    ("; 14.40–14.44", ""),
    ("; 14.48", ""),
    ("; 14.71", ""),
    ("; 14.72", ""),
    ("O estado actual examinado corresponde à versão 14.72.0, em 14 de Julho de 2026.", "O estado final examinado corresponde a 14 de Julho de 2026."),
    ("Os ensaios principais incidiram na versão 14.67.0 e a série complementar de interface na versão 14.69.0.", "Os ensaios principais e a série complementar de interface incidiram em estados anteriores da plataforma."),
    ("Os ensaios principais incidiram na versão 14.67.0 e a série complementar de ensaios de interface na versão 14.69.0.", "Os ensaios principais e a série complementar de interface incidiram em estados anteriores da plataforma."),
    ("Versão actual 14.72.0; ensaios principais em 14.67.0 e complementares em 14.69.0", "Estado final examinado; ensaios principais e complementares realizados em estados anteriores"),
    ("A evolução entre versões impede", "A evolução do protótipo impede"),
    ("Na versão 14.67.0, quatro modelos surgem no ficheiro de configuração", "No estado usado nos ensaios principais, quatro modelos surgem no ficheiro de configuração"),
    ("Os quatro permanecem registados na versão 14.72.0.", "Os quatro permanecem registados no estado final examinado."),
    ("; plataforma 14.67.0; registado e activo", "; registado e activo no estado usado nos ensaios principais"),
    ("não registado na plataforma 14.67.0", "não registado no estado usado nos ensaios principais"),
    ("As contagens da Tabela 5.3 referem-se às declarações presentes no catálogo versionado dos modelos da plataforma 14.67.0.", "As contagens da Tabela 5.3 referem-se às declarações presentes no catálogo de modelos usado nos ensaios principais."),
    ("Versões examinadas", "Estados examinados"),
    ("A avaliação inicial incidiu sobre a versão 14.67.0. A série complementar de controlo da interface e dos dados submetidos foi executada na versão 14.69.0.", "A avaliação inicial incidiu sobre o estado usado nos ensaios principais. A série complementar de controlo da interface e dos dados submetidos foi executada num estado posterior."),
    ("A versão 14.67.0 foi inspeccionada no fecho do estudo.", "O estado usado nos ensaios principais foi inspeccionado no fecho do estudo."),
    ("registos de ensaios de versões anteriores", "registos de ensaios anteriores"),
    ("documentadas nas versões correspondentes", "documentadas nos registos correspondentes"),
    ("A bateria Playwright da versão 14.67.0", "A bateria Playwright dos ensaios principais"),
    ("A versão 14.19.0 retirou", "A alteração subsequente retirou"),
    ("no estado versionado da plataforma 14.67.0", "no estado da plataforma usado nos ensaios principais"),
    ("**Versão avaliada:** HandFab 14.69.0", "**Estado avaliado:** HandFab durante a série complementar"),
    ("Versão avaliada: HandFab 14.69.0", "Estado avaliado: HandFab durante a série complementar"),
    ("As séries de ensaios correspondem à versão 14.69.0 da plataforma.", "As séries de ensaios correspondem ao estado da plataforma usado na avaliação complementar."),
    ("O estado examinado corresponde à versão 14.72.0 da plataforma em 14 de Julho de 2026.", "O estado final examinado corresponde a 14 de Julho de 2026."),
    ("A versão 14.71.0 integrou", "Uma revisão imediatamente anterior integrou"),
    ("e alterou o dicionário da versão 14.67.0:", "e alterou o dicionário usado nos ensaios principais:"),
    ("Coerência dos controlos na versão 14.72.0", "Coerência dos controlos no estado final examinado"),
    ("A versão 14.72.0 aplicou", "O estado final examinado aplicou"),
    ("suplemento 14.67.0", "suplemento dos ensaios principais"),
    ("no estado 14.72.0", "no estado final examinado"),
    ("Relação com o suplemento da versão 14.67.0", "Relação com o suplemento dos ensaios principais"),
    ("fotografia da versão 14.67.0", "fotografia do estado usado nesses ensaios"),
    ("Depois dessa versão", "Depois desse estado"),
    ("não descrevem o estado 14.72.0", "não descrevem o estado final examinado"),
    ("nota de versão", "nota de evolução"),
    ("confronto entre a versão 14.67.0 do suplemento e a versão 14.72.0", "confronto entre o suplemento dos ensaios principais e o estado final examinado"),
    ("; plataforma 14.67.0; activo", "; activo no estado usado nos ensaios principais"),
    ("catálogo versionado dos modelos no estado versionado da plataforma 14.67.0", "catálogo de modelos usado nos ensaios principais"),
    ("Relação com o suplemento da versão 14.67.0140", "Relação com o suplemento dos ensaios principais140"),
    ("Componentes, versões e limites do protótipo examinado", "Componentes, estados e limites do protótipo examinado"),
    ("Registo de versões, casos, parâmetros, exportações, preparação e protótipos físicos", "Registo de iterações, casos, parâmetros, exportações, preparação e protótipos físicos"),
    ("decisão, versão e resultado", "decisão, alteração e resultado"),
    ("Versão, problema observado, alteração e novo ensaio", "Estado, problema observado, alteração e novo ensaio"),
    ("catálogo versionado dos modelos", "catálogo de modelos"),
    ("Data e versão", "Data"),
    ("As versões são registadas porque condicionam a leitura dos ensaios", "Os estados e componentes são registados porque condicionam a leitura dos ensaios"),
    ("Modelo, versão e estado", "Modelo e estado"),
    ("catálogo de configuração da versão estudada", "catálogo de configuração do estado estudado"),
    ("numa versão anterior", "num estado anterior"),
    ("versão avaliada", "estado avaliado"),
    ("versão de código", "estado do código"),
    ("versões específicas do código", "estados específicos do código"),
    ("A versão actual da plataforma", "O estado final da plataforma"),
    ("A versão actual reutiliza", "O estado final reutiliza"),
    ("catálogo versionado de configuração dos modelos", "catálogo de configuração dos modelos"),
    ("parâmetros do catálogo versionado", "parâmetros do catálogo"),
]


INTERNAL_VERSION = re.compile(r"(?<![\d.])14\.\d+(?:\.\d+)?")


def replace_in_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        occurrences = text.count(old)
        if occurrences:
            text = text.replace(old, new)
            count += occurrences
    return text, count


def replace_in_element(element: etree._Element, old: str, new: str) -> int:
    count = 0
    while True:
        nodes = element.xpath(".//w:t", namespaces=NS)
        full_text = "".join(node.text or "" for node in nodes)
        start = full_text.find(old)
        if start < 0:
            return count
        end = start + len(old)
        offset = 0
        inserted = False
        for node in nodes:
            value = node.text or ""
            node_start, node_end = offset, offset + len(value)
            overlap_start = max(start, node_start)
            overlap_end = min(end, node_end)
            if overlap_start < overlap_end:
                local_start = overlap_start - node_start
                local_end = overlap_end - node_start
                prefix = value[:local_start]
                suffix = value[local_end:]
                if not inserted:
                    node.text = prefix + new + suffix
                    inserted = True
                else:
                    node.text = prefix + suffix
                if node.text.startswith(" ") or node.text.endswith(" "):
                    node.set(f"{{{XML}}}space", "preserve")
            offset = node_end
        count += 1


def update_markdown() -> int:
    original = MARKDOWN.read_text(encoding="utf-8")
    updated, count = replace_in_text(original)
    remaining = INTERNAL_VERSION.findall(updated)
    if remaining:
        raise RuntimeError(f"Versões internas ainda presentes no Markdown: {remaining}")
    MARKDOWN.write_text(updated, encoding="utf-8")
    return count


def update_docx() -> int:
    with ZipFile(DOCX) as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}
    document = etree.fromstring(files["word/document.xml"])
    count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        for old, new in REPLACEMENTS:
            count += replace_in_element(paragraph, old, new)

    full_text = "".join(document.xpath("//w:t/text()", namespaces=NS))
    remaining = INTERNAL_VERSION.findall(full_text)
    if remaining:
        contexts = []
        for paragraph in document.xpath("//w:p", namespaces=NS):
            paragraph_text = "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))
            if INTERNAL_VERSION.search(paragraph_text):
                contexts.append(paragraph_text)
        raise RuntimeError(
            f"Versões internas ainda presentes no DOCX: {remaining}\n"
            + "\n".join(contexts)
        )

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    temporary = DOCX.with_suffix(DOCX.suffix + ".tmp")
    with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
        for item in items:
            output.writestr(item, files[item.filename])
    os.replace(temporary, DOCX)
    return count


def main() -> None:
    print(f"Markdown: {update_markdown()} substituições")
    print(f"DOCX: {update_docx()} substituições")


if __name__ == "__main__":
    main()
