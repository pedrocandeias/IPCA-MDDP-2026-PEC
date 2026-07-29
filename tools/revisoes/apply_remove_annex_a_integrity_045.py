#!/usr/bin/env python3
"""Remove do DOCX a subsecção técnica A.1.1 e actualiza a versão 0.4.45."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from apply_approved_questions_annex_d import import_fragment, replace_range
from integrate_annexes_bc import NS, element_text, paragraph_style, replace_paragraph_text


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"

PARAGRAPH_REPLACEMENTS = {
    "As versões são identificadas por actividade. Os ensaios iniciais de correspondência e geometria incidiram na versão 14.67.0; as séries complementares da plataforma do Anexo B foram executadas na versão 14.69.0; e o estado actual examinado corresponde à versão 14.72.0 da branch staging, confirmação Git 3a7b2f1. A preparação para fabrico do Anexo D incidiu sobre os ficheiros 3MF arquivados e identifica autonomamente as versões dos programas usados. Esta separação evita apresentar o estado actual do protótipo como se correspondesse exactamente ao estado de todas as execuções preservadas.":
    "As versões são identificadas por actividade. Os ensaios iniciais de correspondência e geometria incidiram na versão 14.67.0; as séries complementares da plataforma do Anexo B foram executadas na versão 14.69.0; e o estado actual examinado corresponde à versão 14.72.0. A preparação para fabrico do Anexo D incidiu sobre os projectos de preparação digital para impressão 3D com configuração analisada e identifica autonomamente as versões dos programas usados. Esta separação evita apresentar o estado actual do protótipo como se correspondesse exactamente ao estado de todas as execuções preservadas.",
    "Para tornar auditável a passagem entre dados, configuração e geometria, a Tabela 4.9 consolida os parâmetros numéricos com efeito antropométrico, geométrico ou mecânico nos três modelos comparados. O dicionário corresponde à plataforma 14.67.0, confirmação Git bcef0db. A unidade é o milímetro, excepto quando a tabela indica percentagem ou razão adimensional. Os valores iniciais constituem a configuração de referência do modelo; os intervalos são limites de implementação, não limites clínicos.":
    "Para tornar auditável a passagem entre dados, configuração e geometria, a Tabela 4.9 consolida os parâmetros numéricos com efeito antropométrico, geométrico ou mecânico nos três modelos comparados. O dicionário corresponde à versão 14.67.0 da plataforma. A unidade é o milímetro, excepto quando a tabela indica percentagem ou razão adimensional. Os valores iniciais não são médias universais: constituem a configuração de referência do modelo. Os intervalos são limites de implementação e não limites clínicos.",
    "Os registos de parâmetros, as malhas, o percurso de transformação, as respectivas somas de verificação e o dicionário completo integram o material suplementar do Anexo C. O percurso é reproduzível ao nível do artefacto e do cálculo; permanece uma verificação técnica com perfil de ensaio, sem avaliação de conforto, função, segurança ou validade clínica.":
    "Os registos de parâmetros, as malhas, o percurso de transformação e o dicionário completo integram o material suplementar do Anexo C. O percurso é reproduzível ao nível do artefacto e do cálculo; permanece uma verificação técnica com perfil de ensaio, sem avaliação de conforto, função, segurança ou validade clínica.",
    "O estado actual examinado corresponde à versão 14.72.0 da branch staging, confirmação Git 3a7b2f1, em 14 de Julho de 2026. Os ensaios principais incidiram na versão 14.67.0 e a série complementar de ensaios de interface na versão 14.69.0. Esta separação temporal é mantida porque a plataforma continuou a evoluir depois dos ensaios, nomeadamente na organização e nomenclatura dos controlos, sem que essas alterações posteriores possam ser apresentadas como parte dos resultados anteriores.":
    "O estado actual examinado corresponde à versão 14.72.0, em 14 de Julho de 2026. Os ensaios principais incidiram na versão 14.67.0 e a série complementar de ensaios de interface na versão 14.69.0. Esta separação temporal é mantida porque a plataforma continuou a evoluir depois dos ensaios, nomeadamente na organização e nomenclatura dos controlos, sem que essas alterações posteriores possam ser apresentadas como parte dos resultados anteriores.",
    "Versão actual 14.72.0, branch staging, confirmação 3a7b2f1; ensaios principais em 14.67.0 e complementares em 14.69.0":
    "Versão actual 14.72.0; ensaios principais em 14.67.0 e complementares em 14.69.0",
    "A versão 14.67.0 da branch staging, commit d5b6f0d5a41950663d54c70b9ab9bad7f8c2d53b, foi inspeccionada no fecho do estudo. A Tabela 8.1 distingue resultados executados nesta verificação, dados observados na base local e ensaios arquivados de versões anteriores.":
    "A versão 14.67.0 foi inspeccionada no fecho do estudo. A Tabela 8.1 distingue resultados executados nesta verificação, dados observados na base local e registos de ensaios de versões anteriores.",
    "Os registos da IA correspondem a conjuntos finitos de execuções e a versões específicas do código. Não foi realizado um estudo estatístico com amostras extensas por cenário. A versão actual da branch staging foi inspeccionada e os dez ensaios unitários disponíveis foram concluídos, mas a bateria completa no navegador não foi novamente executada no fecho da dissertação.":
    "Os registos da IA correspondem a conjuntos finitos de execuções e a versões específicas do código. Não foi realizado um estudo estatístico com amostras extensas por cenário. A versão actual da plataforma foi inspeccionada e os dez ensaios unitários disponíveis foram concluídos, mas a bateria completa no navegador não foi novamente executada no fecho da dissertação.",
    "Estes totais foram confirmados pela regeneração do suplemento dados_antropometricos_v14.67.0, associado à confirmação Git bcef0db. A contagem de 12 corresponde a documentos-fonte ou subconjuntos identificados pelo gerador e não implica 12 estudos primários independentes.":
    "Estes totais foram confirmados pela regeneração dos três conjuntos de dados. A contagem de 12 corresponde a documentos-fonte ou subconjuntos identificados pelo procedimento de geração e não implica 12 estudos primários independentes.",
    "As séries de ensaios registam a versão 14.69.0, a branch staging e o commit 7e604558b337d02fff979169f057d6cbd0c80c0a. A árvore de trabalho continha alterações locais associadas à preparação dos testes. Esta condição limita a possibilidade de reconstruir o estado avaliado apenas a partir do commit; por isso, o código de ensaio, os resultados estruturados e os manifestos de integridade foram preservados em conjunto.":
    "As séries de ensaios correspondem à versão 14.69.0 da plataforma. O código de ensaio, os resultados estruturados e os registos necessários à interpretação das execuções foram conservados em conjunto no material suplementar.",
    "Os resultados estruturados, os manifestos de integridade e as saídas brutas de maior dimensão integram o material suplementar associado ao Anexo B, organizados pelos identificadores técnicos originais de cada série.":
    "Os resultados estruturados e as saídas brutas de maior dimensão integram o material suplementar associado ao Anexo B, organizados pelos identificadores técnicos originais de cada série.",
    "O estado examinado corresponde ao pacote da plataforma identificado como versão 14.72.0 em 14 de Julho de 2026, assente na confirmação Git 3a7b2f1. A versão 14.71.0 integrou a braçadeira revista do Flexy Beast e alterou o dicionário da versão 14.67.0: os antigos parâmetros de largura, comprimento e parede da braçadeira foram substituídos por circunferência do punho, inclinação, multiplicador de comprimento e furos de correia. A versão 14.72.0 uniformizou a organização dos grupos e os nomes dos controlos equivalentes, sem modificar as relações geométricas descritas neste anexo.":
    "O estado examinado corresponde à versão 14.72.0 da plataforma em 14 de Julho de 2026. A versão 14.71.0 integrou a braçadeira revista do Flexy Beast e alterou o dicionário da versão 14.67.0: os antigos parâmetros de largura, comprimento e parede da braçadeira foram substituídos por circunferência do punho, inclinação, multiplicador de comprimento e furos de correia. A versão 14.72.0 uniformizou a organização dos grupos e os nomes dos controlos equivalentes, sem modificar as relações geométricas descritas neste anexo.",
    "O modelo de desenvolvimento pec Phoenix hand não integra este anexo. Embora exista no repositório, não pertence ao conjunto de quatro modelos registados que sustenta a comparação principal da dissertação.":
    "O modelo de desenvolvimento pec Phoenix hand não integra este anexo. Embora tenha sido desenvolvido no âmbito do projecto, não pertence ao conjunto de quatro modelos registados que sustenta a comparação principal da dissertação.",
    "Foram conduzidas duas séries de ensaios complementares. A documentação técnica associada ao anexo reúne os comandos exactos, as versões, as somas de verificação e as saídas brutas no material suplementar da dissertação.":
    "Foram conduzidas duas séries de ensaios complementares. A documentação técnica associada ao anexo reúne as versões, as condições de preparação e os resultados completos no material suplementar da dissertação.",
}


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}")
    return matches[0]


def apply(path: Path) -> tuple[int, int, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])
    markdown = MARKDOWN.read_text(encoding="utf-8")

    replaced = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        current = element_text(paragraph)
        if current in PARAGRAPH_REPLACEMENTS:
            replace_paragraph_text(paragraph, PARAGRAPH_REPLACEMENTS[current])
            replaced += 1

    elements = import_fragment(
        markdown,
        "### A.1 Contexto e Objectivo",
        "### A.2 Estratégia de Pesquisa Bibliográfica",
        "remove_a11_045",
        document,
        relationships,
        files,
    )
    replace_range(
        find_body_paragraph(document, "A.1 Contexto e Objectivo"),
        find_body_paragraph(document, "A.2 Estratégia de Pesquisa Bibliográfica"),
        elements,
    )

    removed_index = 0
    for paragraph in list(document.xpath("//w:body/w:p", namespaces=NS)):
        if paragraph_style(paragraph).startswith("ndice") and element_text(paragraph).startswith("A.1.1 "):
            paragraph.getparent().remove(paragraph)
            removed_index += 1

    version_matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph).startswith("Versão do documento:")
    ]
    if len(version_matches) > 1:
        raise RuntimeError(f"Esperado no máximo um parágrafo de versão; encontrados {len(version_matches)}")
    if version_matches:
        replace_paragraph_text(version_matches[0], "Versão do documento: 0.4.45")

    files["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )
    files["word/_rels/document.xml.rels"] = etree.tostring(
        relationships, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for name, data in files.items():
                output.writestr(name, data)
        temporary.replace(path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)

    return len(elements), removed_index, replaced


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    imported, removed_index, replaced = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Elementos importados para A.1: {imported}")
    print(f"Entradas A.1.1 removidas do índice: {removed_index}")
    print(f"Parágrafos com metadados internos removidos: {replaced}")


if __name__ == "__main__":
    main()
