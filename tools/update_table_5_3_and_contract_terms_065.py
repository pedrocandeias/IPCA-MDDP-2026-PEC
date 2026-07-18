#!/usr/bin/env python3
"""Synchronise the 0.4.65 table and terminology edits in the DOCX.

The script removes the non-integrated ``pec Phoenix hand`` entry, limits
Table 5.3 to the four models present in the platform and replaces the
software-engineering use of ``contrato`` with explicit Portuguese wording.
It also rewrites Table 8.1 around design-relevant evidence and clarifies the
repeated-export procedure formerly described as frozen configurations.
"""

from __future__ import annotations

import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}


TEXT_REPLACEMENTS = {
    "Especificação técnica dos modelos de IA e do contrato de sugestão paramétrica": (
        "Especificação técnica dos modelos de IA e da estrutura da sugestão paramétrica",
        2,
    ),
    "contratos internos irrelevantes": (
        "pormenores internos de integração irrelevantes",
        1,
    ),
    "Contrato de resposta": ("Estrutura da resposta", 1),
    "Estas alterações incidem no contrato entre configuração e interface": (
        "Estas alterações incidem na correspondência entre os campos da configuração e os controlos da interface",
        1,
    ),
    "declarada no contrato de parâmetros": ("explicitada na especificação dos parâmetros", 1),
    "Depois desse estado, a braçadeira do Flexy Beast mudou de contrato paramétrico.": (
        "Depois desse estado, a estrutura paramétrica da braçadeira do Flexy Beast foi alterada.",
        1,
    ),
    "Evidência técnica do funcionamento da plataforma": (
        "Evidência do funcionamento da plataforma no processo de projeto",
        2,
    ),
    "Inspeção computacional de malhas na configuração infantil": (
        "Inspeção computacional das malhas geradas para um perfil antropométrico de 8 anos",
        1,
    ),
    "Inspecção computacional de malhas na configuração infantil": (
        "Inspeção computacional das malhas geradas para um perfil antropométrico de 8 anos",
        1,
    ),
    "Dois projectos com camada de 0,24 mm, duas paredes e 15% de enchimento: peças atribuídas, respectivamente, a PLA e a Bambu PETG Basic; no PETG, bico a 255 °C e mesa a 70 °C": (
        "Dois ficheiros de preparação com camada de 0,24 mm, duas paredes e 15% de enchimento: peças atribuídas, respetivamente, a PLA e a Bambu PETG Basic; no PETG, bico a 255 °C e mesa a 70 °C",
        1,
    ),
    "Oito conjuntos de peças em cada projecto; programa regista 0 arestas corrigidas e 0 faces degeneradas": (
        "Oito conjuntos de peças em cada ficheiro; o programa regista 0 arestas corrigidas e 0 faces degeneradas",
        1,
    ),
    "projecto Bambu A1": ("ficheiro de preparação para a Bambu Lab A1", 2),
    "projecto Prusa MINI": ("ficheiro de preparação para a Prusa MINI", 1),
}


MODEL_CELL_REPLACEMENTS = {
    "Modelo e estado": "Modelo",
    "Flexy Beast; activo no estado usado nos ensaios principais": "Flexy Beast",
    "Paraglider/Flexible Flyer; activo no estado usado nos ensaios principais": "Paraglider/Flexible Flyer",
    "UnLimbited Phoenix V1.0; activo no estado usado nos ensaios principais": "UnLimbited Phoenix V1.0",
    "Cyborg Beast; activo no estado usado nos ensaios principais": "Cyborg Beast",
}


PARAGRAPH_REPLACEMENTS = {
    "A biblioteca examinada compreende quatro modelos registados na plataforma:": (
        "A biblioteca examinada compreende quatro modelos integrados na plataforma: Flexy Beast, "
        "Paraglider Hand, UnLimbited Phoenix Hand e Cyborg Beast. Os três primeiros integram a comparação "
        "dimensional e os ensaios descritos no Capítulo 8. O Cyborg Beast foi integrado posteriormente e "
        "é analisado como evolução do projeto, sem ser incluído nas séries comparativas ou físicas. O "
        "inventário dos modelos, com origem, licença, estratégia de escala e evidência disponível, é "
        "apresentado na Tabela 5.3."
    ),
    "A biblioteca organiza diferentes famílias como modelos registados": (
        "A biblioteca organiza quatro famílias integradas na plataforma, cada uma com parâmetros, "
        "dependências, limites e modos de visualização próprios: Flexy Beast, UnLimbited Phoenix Hand, "
        "Paraglider Hand e Cyborg Beast. Os ensaios dimensionais comparativos abrangem os três primeiros; "
        "o Cyborg Beast foi integrado posteriormente e não entra nas séries comparativas. Esta distinção "
        "separa o conjunto disponível na plataforma do subconjunto abrangido pelos ensaios comparativos."
    ),
    "O estado usado nos ensaios principais foi inspec": (
        "O funcionamento da plataforma foi examinado através das funções que sustentam o percurso entre "
        "dados antropométricos, configuração, visualização e preparação para fabrico. A Tabela 8.1 "
        "sintetiza a evidência observada e explicita a sua relevância para o processo de projeto e os "
        "respetivos limites. Os comandos, datas de execução e identificadores internos dos testes são "
        "conservados apenas no material técnico suplementar."
    ),
    "Na repetição de configurações congeladas": (
        "Para verificar a consistência da geração, cada modelo foi exportado repetidamente, mantendo "
        "inalterados os valores dos parâmetros. Foram concluídas sete exportações do Flexy Beast, cinco "
        "do Paraglider Hand e cinco da UnLimbited Phoenix. Em cada modelo, todas as exportações concluídas "
        "produziram ficheiros exatamente iguais ao nível dos dados binários, isto é, com a mesma sequência "
        "de zeros e uns que constitui o seu conteúdo digital, e conservaram as mesmas dimensões e métricas "
        "geométricas. O critério previamente definido exigia dez exportações concluídas por modelo; como "
        "algumas tentativas foram interrompidas por bloqueios e tempos-limite no ambiente de ensaio, o "
        "resultado é parcial. A evidência sustenta a consistência das exportações concluídas, mas não "
        "permite considerar cumprido o critério definido para a totalidade das repetições."
    ),
    "A preparação para impressão converte a geometria numa sequência de camadas": (
        "A preparação para impressão converte a geometria numa sequência de camadas e trajectórias de "
        "deposição, definindo altura de camada, paredes, enchimento, suportes, temperaturas e orientação. "
        "A Série A constitui uma verificação técnica complementar da fase empírica aprovada e documenta "
        "quatro ficheiros de preparação: três foram configurados no Bambu Studio 01.10.02.76 para a "
        "impressora Bambu Lab A1 — Flexy Beast em PLA e UnLimbited Phoenix em PLA e PETG — e um foi "
        "configurado no PrusaSlicer 2.8.1 para a Prusa MINI — Paraglider Hand em PLA. Os ficheiros "
        "preparados no Bambu Studio usam camada de 0,24 mm, duas paredes, enchimento de 15% em grelha e "
        "suporte em árvore orgânica; o ficheiro preparado no PrusaSlicer usa camada de 0,20 mm, dois "
        "perímetros, enchimento de 15% e suporte desactivado. Como geometria, programa, impressora, "
        "material e condições não são equivalentes, esta série descreve cada preparação e não permite "
        "comparar desempenho entre equipamentos ou materiais."
    ),
    "Os quatro projectos da Série A foram novamente processados": (
        "Os quatro ficheiros de preparação da Série A foram novamente processados com as definições neles "
        "conservadas. Em todos foram geradas trajectórias e estimativas. O Flexy Beast em PLA apresentou "
        "2 h 21 min 50 s e 56,51 g; o Phoenix apresentou 5 h 12 min 44 s e 123,52 g em PLA e 5 h 51 min "
        "52 s e 117,54 g em PETG; o Paraglider apresentou 2 h 32 min 11 s e 37,96 g em PLA. Estes valores "
        "são estimativas dos programas e não medições de impressões reais. Como os ficheiros usam "
        "condições distintas, não permitem concluir que um modelo, material, programa ou equipamento seja "
        "mais rápido ou económico."
    ),
    "Uma inspecção complementar com trimesh": (
        "Uma inspecção complementar com trimesh, arquivada com os cenários de 29 de Junho de 2026, "
        "examinou as malhas geradas a partir do perfil antropométrico de ensaio de 8 anos. Os critérios "
        "foram fecho da superfície, carácter múltiplo da geometria, número de corpos e faces de área nula. "
        "A Tabela 8.3 mostra que a preparação aceite pelo programa não implica que a malha de origem seja "
        "um sólido fechado sem defeitos."
    ),
    "Os projectos Bambu registam zero arestas corrigidas": (
        "Nos ficheiros de preparação configurados para a Bambu Lab A1, o diagnóstico do Bambu Studio "
        "regista zero arestas corrigidas e zero faces degeneradas nas peças importadas. Este indicador "
        "refere-se apenas aos ficheiros concretos examinados e resulta de um procedimento diferente do "
        "utilizado na inspecção computacional da Tabela 8.3. A diferença entre os registos deve ser "
        "mantida, pois nenhum dos resultados autoriza a concluir que todas as variantes de cada modelo "
        "possuem a mesma qualidade de malha."
    ),
}


TABLE_8_1_ROWS = [
    ["Função examinada", "Evidência observada", "Relevância para o processo de projeto", "Limite de interpretação"],
    [
        "Correspondência entre descrição e perfil",
        "As descrições de ensaio foram relacionadas com referências populacionais segundo sexo, idade, grupo etário e disponibilidade geográfica",
        "Permite introduzir uma referência antropométrica inicial no percurso de configuração",
        "A referência é populacional, não individual, e não demonstra adequação anatómica",
    ],
    [
        "Seleção de modelos",
        "Quatro modelos com parâmetros próprios podem ser selecionados e configurados na mesma interface",
        "Demonstra que a plataforma acomoda famílias geométricas com regras distintas num percurso comum",
        "Apenas três modelos integram a comparação dimensional principal",
    ],
    [
        "Base antropométrica",
        "A aplicação reúne 100 perfis agregados por população, sexo, idade e tipo de estatística",
        "Disponibiliza referências mensuráveis para iniciar ou contextualizar decisões paramétricas",
        "A cobertura geográfica e etária é desigual e os perfis não substituem medições diretas",
    ],
    [
        "Conservação de configurações",
        "Perfis, valores paramétricos e configurações podem ser guardados e recuperados",
        "Permite retomar, documentar e comparar variantes ao longo do processo de projeto",
        "Não foram avaliados utilização intensiva, acessos simultâneos ou práticas reais de colaboração",
    ],
    [
        "Visualização e exportação",
        "As configurações examinadas produziram pré-visualizações tridimensionais e ficheiros STL e 3MF",
        "Mantém continuidade entre alteração de parâmetros, observação da geometria e preparação para fabrico",
        "A exportação não garante imprimibilidade, montagem, segurança ou adequação clínica",
    ],
    [
        "Sugestão apoiada por IA",
        "A descrição e a referência antropométrica podem originar uma proposta inicial de valores, posteriormente editável",
        "Apoia a exploração preliminar sem retirar ao utilizador o controlo da configuração",
        "Depende de serviços externos e não decide nem valida a geometria final",
    ],
]


def element_text(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def set_paragraph_text(paragraph: etree._Element, value: str) -> None:
    paragraph_properties = paragraph.find(f"{{{W_NS}}}pPr")
    first_run_properties = paragraph.find(f"{{{W_NS}}}r/{{{W_NS}}}rPr")
    for child in list(paragraph):
        if child is not paragraph_properties:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, f"{{{W_NS}}}r")
    if first_run_properties is not None:
        run.append(deepcopy(first_run_properties))
    text_node = etree.SubElement(run, f"{{{W_NS}}}t")
    text_node.text = value


def set_cell_text(cell: etree._Element, value: str) -> None:
    paragraphs = cell.xpath("./w:p", namespaces=NS)
    if not paragraphs:
        raise RuntimeError(f"Célula sem parágrafo: {element_text(cell)!r}")
    set_paragraph_text(paragraphs[0], value)
    for paragraph in paragraphs[1:]:
        cell.remove(paragraph)


def prevent_row_split(row: etree._Element) -> None:
    row_properties = row.find(f"{{{W_NS}}}trPr")
    if row_properties is None:
        row_properties = etree.Element(f"{{{W_NS}}}trPr")
        row.insert(0, row_properties)
    if row_properties.find(f"{{{W_NS}}}cantSplit") is None:
        row_properties.append(etree.Element(f"{{{W_NS}}}cantSplit"))


def find_unique_paragraph(root: etree._Element, value: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if element_text(paragraph) == value
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo {value!r}: encontrados {len(matches)}; esperado 1")
    return matches[0]


def find_unique_paragraph_prefix(root: etree._Element, prefix: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if element_text(paragraph).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Prefixo {prefix!r}: encontrados {len(matches)}; esperado 1")
    return matches[0]


def update_model_table(root: etree._Element) -> None:
    caption = find_unique_paragraph_prefix(root, "Tabela 5.3 — Modelos integrados na plataforma")
    table = caption.getnext()
    while table is not None and table.tag != f"{{{W_NS}}}tbl":
        table = table.getnext()
    if table is None:
        raise RuntimeError("Tabela 5.3 não localizada após a legenda")

    found = set()
    removed = 0
    for row in list(table.xpath("./w:tr", namespaces=NS)):
        cells = row.xpath("./w:tc", namespaces=NS)
        if not cells:
            continue
        first_cell = cells[0]
        value = element_text(first_cell)
        if value == "pec Phoenix hand; desenvolvimento; não registado":
            table.remove(row)
            removed += 1
            continue
        if value in MODEL_CELL_REPLACEMENTS:
            set_cell_text(first_cell, MODEL_CELL_REPLACEMENTS[value])
            found.add(value)

    missing = set(MODEL_CELL_REPLACEMENTS) - found
    if missing:
        raise RuntimeError(f"Células esperadas não localizadas na Tabela 5.3: {sorted(missing)}")
    if removed != 1:
        raise RuntimeError(f"Linhas removidas da Tabela 5.3: {removed}; esperado 1")

    rows = table.xpath("./w:tr", namespaces=NS)
    if len(rows) != 5:
        raise RuntimeError(f"A Tabela 5.3 deveria conter cabeçalho e quatro modelos; contém {len(rows)} linhas")
    for row in rows:
        prevent_row_split(row)


def update_table_8_1(root: etree._Element) -> None:
    prefix = "Tabela 8.1 — Evidência do funcionamento da plataforma no processo de projeto"
    candidates = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if element_text(paragraph).startswith(prefix)
        and paragraph.getnext() is not None
        and paragraph.getnext().tag == f"{{{W_NS}}}tbl"
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"Legendas da Tabela 8.1 antes de tabela: {len(candidates)}; esperado 1")
    table = candidates[0].getnext()

    rows = table.xpath("./w:tr", namespaces=NS)
    if len(rows) != len(TABLE_8_1_ROWS):
        raise RuntimeError(
            f"A Tabela 8.1 contém {len(rows)} linhas; esperadas {len(TABLE_8_1_ROWS)}"
        )
    for row, values in zip(rows, TABLE_8_1_ROWS, strict=True):
        cells = row.xpath("./w:tc", namespaces=NS)
        if len(cells) != len(values):
            raise RuntimeError(
                f"Linha da Tabela 8.1 com {len(cells)} células; esperadas {len(values)}"
            )
        for cell, value in zip(cells, values, strict=True):
            set_cell_text(cell, value)
        prevent_row_split(row)


def prevent_table_8_3_row_splits(root: etree._Element) -> None:
    prefix = "Tabela 8.3 — Inspeção computacional das malhas geradas para um perfil antropométrico de 8 anos"
    candidates = [
        paragraph
        for paragraph in root.xpath(".//w:p", namespaces=NS)
        if element_text(paragraph).startswith(prefix)
        and paragraph.getnext() is not None
        and paragraph.getnext().tag == f"{{{W_NS}}}tbl"
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"Legendas da Tabela 8.3 antes de tabela: {len(candidates)}; esperado 1")
    for row in candidates[0].getnext().xpath("./w:tr", namespaces=NS):
        prevent_row_split(row)


def apply(path: Path) -> None:
    original_mode = path.stat().st_mode
    with ZipFile(path, "r") as source:
        items = source.infolist()
        files = {item.filename: source.read(item.filename) for item in items}

    document = files["word/document.xml"].decode("utf-8")
    for old, (new, expected) in TEXT_REPLACEMENTS.items():
        found = document.count(old)
        if found != expected:
            raise RuntimeError(f"Ocorrências de {old!r}: {found}; esperado: {expected}")
        document = document.replace(old, new)

    root = etree.fromstring(document.encode("utf-8"))
    for prefix, replacement in PARAGRAPH_REPLACEMENTS.items():
        paragraph = find_unique_paragraph_prefix(root, prefix)
        set_paragraph_text(paragraph, replacement)

    paragraph = find_unique_paragraph_prefix(root, "O modelo de desenvolvimento pec Phoenix hand")
    paragraph.getparent().remove(paragraph)
    update_model_table(root)
    update_table_8_1(root)
    prevent_table_8_3_row_splits(root)

    final_text = element_text(root)
    for forbidden in (
        "pec Phoenix hand",
        "configurações congeladas",
        "npm run test:unit",
        "projectos Bambu",
        "configuração infantil",
    ):
        if forbidden in final_text:
            raise RuntimeError(f"Expressão removida ainda presente no DOCX: {forbidden!r}")
    if "contrato" in final_text.lower():
        raise RuntimeError("O termo técnico 'contrato' ainda está presente no DOCX")

    files["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )

    fd, temporary_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in items:
                target.writestr(item, files[item.filename])
        os.replace(temporary, path)
        os.chmod(path, original_mode)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    repository = Path(__file__).resolve().parent.parent
    canonical = repository / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
    apply(canonical)
    print("DOCX actualizado para a versão 0.4.65")
