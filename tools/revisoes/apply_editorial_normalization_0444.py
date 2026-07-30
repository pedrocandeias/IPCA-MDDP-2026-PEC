#!/usr/bin/env python3
"""Aplica ao DOCX a normalização editorial da versão 0.4.44."""

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

FRAGMENTS = (
    ("### A.1 Contexto e Objectivo", "### A.2 Estratégia de Pesquisa Bibliográfica", "A.1 Contexto e Objectivo", "A.2 Estratégia de Pesquisa Bibliográfica", "editorial_a1"),
    ("### A.8 Escrita do Código de Geração", "### A.10 Cobertura Global da Base de Dados e Lacunas", "A.8 Escrita do Código de Geração", "A.10 Cobertura Global da Base de Dados e Lacunas", "editorial_a8_a9"),
    ("## B.1 Finalidade", "## B.2 Âmbito e limites", "B.1 Finalidade", "B.2 Âmbito e limites", "editorial_b1"),
    ("## B.9 Ficha técnica e proveniência das evidências", "## B.10 Referências normativas", "B.9 Ficha técnica e proveniência das evidências", "B.10 Referências normativas", "editorial_b9"),
    ("## C.11 Fontes técnicas consultadas", "## C.12 Verificações executadas", "C.11 Fontes técnicas consultadas", "C.12 Verificações executadas", "editorial_c11"),
    ("### D.3.1 Série A — projectos de preparação digital para impressão 3D com configuração analisada", "### D.3.2 Série B — comparação digital controlada", "D.3.1 Série A — projectos de preparação digital para impressão 3D com configuração analisada", "D.3.2 Série B — comparação digital controlada", "editorial_d31"),
    ("### D.3.2 Série B — comparação digital controlada", "## D.4 Resultados", "D.3.2 Série B — comparação digital controlada", "D.4 Resultados", "editorial_d32"),
    ("### D.4.2 Série B (condição comum)", "### D.4.3 Geometria — tamanho do conjunto vs tamanho da peça", "D.4.2 Série B (condição comum)", "D.4.3 Geometria — tamanho do conjunto vs tamanho da peça", "editorial_d42"),
    ("## D.5 Compatibilidade com orientações de dimensionamento", "## D.6 Limites de comparabilidade", "D.5 Compatibilidade com orientações de dimensionamento", "D.6 Limites de comparabilidade", "editorial_d5"),
)


TOKEN_REPLACEMENTS = (
    ("A.1.1 Localização, versão e integridade dos ficheiros", "A.1.1 Versão, rastreabilidade e integridade do suplemento"),
    ("B.9 Ficha técnica e localização das evidências", "B.9 Ficha técnica e proveniência das evidências"),
    ("C.11 Ficheiros consultados", "C.11 Fontes técnicas consultadas"),
    ("Projectos de preparação para impressão arquivados", "Projectos de preparação digital para impressão 3D com configuração analisada"),
    ("Estimativas dos projectos de impressão arquivados", "Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada"),
    ("Série A — projectos arquivados (fatiados como preparados)", "Série A — projectos de preparação digital para impressão 3D com configuração analisada"),
    ("Série A — projectos arquivados", "Série A — projectos de preparação digital para impressão 3D com configuração analisada"),
    ("quatro projectos arquivados", "quatro projectos de preparação digital para impressão 3D com configuração analisada"),
    ("4/4 projectos arquivados", "4/4 projectos com configuração analisada"),
    ("entre os projectos arquivados", "entre os projectos com configuração analisada"),
    ("perfis sintéticos", "perfis de ensaio"),
    ("Perfis sintéticos", "Perfis de ensaio"),
    ("perfis simulados", "perfis de ensaio"),
    ("Perfis simulados", "Perfis de ensaio"),
    ("perfil simulado", "perfil de ensaio"),
    ("software de fatiamento", "programas de preparação para impressão 3D"),
    ("do fatiador", "do programa"),
    ("o fatiador", "o programa"),
    ("de fatiador", "do programa"),
    ("ambos os fatiadores", "ambos os programas"),
    ("fatiadores/impressoras distintos", "programas/equipamentos distintos"),
    ("fatiadores (Bambu/Prusa)", "programas (Bambu Studio/PrusaSlicer)"),
    ("fatiadores e todos os materiais", "programas e todos os materiais"),
    ("aceites pelos fatiadores", "aceites pelos programas de preparação"),
    ("modelos, fatiadores ou", "modelos, programas ou"),
    ("fatiadores/perfis", "programas/configurações"),
    ("fatiados sob", "processados sob"),
    ("resultado do fatiamento", "resultado da preparação para impressão"),
    ("A conclusão do fatiamento", "A conclusão do processamento"),
    ("robustez de fatiamento", "robustez da preparação para impressão"),
    ("Que o fatiamento concluído", "Que o processamento concluído"),
    ("sem fatiamento", "sem preparação para impressão"),
    ("models/models-config.json", "catálogo versionado dos modelos"),
    ("models-config.json", "catálogo versionado dos modelos"),
    ("data/app.db", "base local da aplicação"),
    ("app.db", "base local da aplicação"),
    ("server/services/profileMapping.js", "serviço determinístico de correspondência de perfis"),
    ("Normal_Gauntlet_w_Tensioner.stl", "geometria de referência da braçadeira normal com tensionador"),
    ("data/ansur_1988_complete.csv", "conjunto ANSUR completo"),
    ("ansur_1988_complete.csv", "conjunto ANSUR completo"),
    ("data/ansur_1988_hand_arm.csv", "subconjunto ANSUR mão–braço"),
    ("ansur_1988_hand_arm.csv", "subconjunto ANSUR mão–braço"),
    ("data/multi_population_hand.csv", "base multipopulacional da mão"),
    ("multi_population_hand.csv", "base multipopulacional da mão"),
    ("data/generate_ansur_csv.py", "procedimento de geração ANSUR"),
    ("generate_ansur_csv.py", "procedimento de geração ANSUR"),
    ("data/generate_multi_population_hand_csv.py", "procedimento de geração multipopulacional"),
    ("generate_multi_population_hand_csv.py", "procedimento de geração multipopulacional"),
    ("componentes/anexos/dados_antropometricos_v14.67.0/", "material suplementar da dissertação"),
    ("componentes/anexos/dicionario_parametros_v14.67.0/example_flexy_beast_child_8/", "material suplementar associado ao Anexo C"),
    ("componentes/anexos/dicionario_parametros_v14.67.0/parameter_dictionary.csv", "dicionário integral no material suplementar do Anexo C"),
    ("componentes/anexos/dicionario_parametros_v14.67.0/", "material suplementar associado ao Anexo C"),
    ("componentes/anexos/testes_plataforma/evidencias/", "material suplementar associado ao Anexo B"),
    ("test-results/thesis-evaluation/", "material suplementar associado ao Anexo B"),
    ("docs/relatorio-adaptacao-antropometrica.md", "relatório técnico de adaptação antropométrica"),
    ("docs/relatorio-revisao-academica-integral-dissertacao-2026-07-13.md", "relatório integral de revisão académica"),
    ("projecto-completo.md", "manuscrito consolidado"),
)


PARAGRAPH_REPLACEMENTS = {
    "A evidência de fabrico inclui 116 ficheiros 3MF gerados para três modelos e quatro perfis sintéticos, quatro projectos com parâmetros de preparação e fotografias de peças físicas. Os 116 ficheiros representam exportações digitais, distribuídas por placas combinadas e peças individuais; esse total não corresponde a 116 impressões físicas. Os quatro projectos encontram-se em docs/print-validation/bambulaba1_flexy_beast_teen_15_print.3mf, docs/print-validation/bambulaba1_unlimbed_phoenix_hand_teen_15_print_project.3mf, docs/print-validation/unlimbed_phoenix_hand_teen_15_print_project_PETG.3mf e docs/print-validation/prusa_mini_paraglider_15_teen_print_profile.3mf. Cada projecto identifica um perfil de 15 anos, o material configurado e a impressora usada. Esta Série A documenta os projectos individualmente; não pressupõe condições comparáveis entre eles.":
    "A evidência de fabrico inclui 116 ficheiros 3MF gerados para três modelos e quatro perfis de ensaio, quatro projectos com parâmetros de preparação e fotografias de peças físicas. Os 116 ficheiros representam exportações digitais, distribuídas por placas combinadas e peças individuais; esse total não corresponde a 116 impressões físicas. Os quatro projectos de preparação digital para impressão 3D com configuração analisada integram o material suplementar da Série A. Cada projecto identifica um perfil de 15 anos, o material configurado e a impressora usada. A série documenta os projectos individualmente e não pressupõe condições comparáveis entre eles.",
    "Fonte: elaboração própria a partir dos prompts registados em docs/ai_anthropometric_validation.md, dos metadados em docs/flexy-beast-ai-sim/run-metadata.json, docs/paraglider-ai-sim/run-metadata.json e docs/phoenix-ai-sim/run-metadata.json, e dos cenários em docs/ucd-ai-sim/. A coluna apresenta a descrição do caso simulado enviada no pedido; o pedido completo incluía o esquema actual do modelo, os intervalos permitidos e a instrução de devolver apenas JSON válido.":
    "Fonte: elaboração própria a partir dos pedidos, metadados e cenários conservados no material suplementar da avaliação. A coluna apresenta a descrição do caso de ensaio enviada no pedido; o pedido completo incluía o esquema actual do modelo, os intervalos permitidos e a instrução de devolver apenas JSON válido.",
    "Os ficheiros params.json, palm.3mf, middle_base.3mf, middle_tip.3mf e trace.json, os respectivos valores SHA-256 e o dicionário completo encontram-se em componentes/anexos/dicionario_parametros_v14.67.0/. O percurso é reproduzível ao nível do artefacto arquivado e do cálculo; permanece uma verificação técnica com perfil simulado, sem avaliação de conforto, função, segurança ou validade clínica.":
    "Os registos de parâmetros, as malhas, o percurso de transformação e o dicionário completo integram o material suplementar do Anexo C. O percurso é reproduzível ao nível do artefacto e do cálculo; permanece uma verificação técnica com perfil de ensaio, sem avaliação de conforto, função, segurança ou validade clínica.",
    "Foram conduzidas duas séries de ensaios complementares. Os comandos exactos, versões e checksums estão no repositório do projecto (docs/print-validation/slicer-evaluation/).":
    "Foram conduzidas duas séries de ensaios complementares. A documentação técnica associada ao anexo reúne as versões, as condições de preparação e os resultados completos no material suplementar da dissertação.",
    "Os dados completos estão nos ficheiros CSV que acompanham este anexo: resultados_projectos_arquivados.csv, resultados_campanha_controlada.csv e resultados_geometria.csv.":
    "Os resultados quantitativos completos e os registos geométricos encontram-se no material suplementar associado a este anexo.",
    "A análise geométrica distingue três noções de tamanho que não devem ser confundidas (detalhe em resultados_geometria.csv):":
    "A análise geométrica distingue três noções de tamanho que não devem ser confundidas; os valores completos constam do registo geométrico suplementar:",
    "A comparação dimensional foi preparada a partir dos mesmos quatro perfis. Em cada caso, o valor palm_breadth_mm foi lido do ficheiro params.json aplicado pela plataforma e a extensão total no eixo X foi medida directamente na malha 3MF isolada da palma. A futura medição da peça física deverá reproduzir essa extensão total, com a peça orientada segundo os eixos do ficheiro, usando os mesmos extremos geométricos.":
    "A comparação dimensional foi preparada a partir dos mesmos quatro perfis. Em cada caso, o valor palm_breadth_mm foi lido no registo de parâmetros aplicado pela plataforma e a extensão total no eixo X foi medida directamente na malha 3MF isolada da palma. A futura medição da peça física deverá reproduzir essa extensão total, com a peça orientada segundo os eixos do ficheiro, usando os mesmos extremos geométricos.",
    "A Tabela D.3 resume a extensão total no eixo X, por ser o único eixo associado a um parâmetro activo nos três modelos. A medição física e o respectivo desvio observado permanecem por preencher. A folha completa tabela_comparacao_dimensional.csv conserva as 36 linhas de medição física ainda por executar. A folha tabela_estimativa_dimensional_teorica.csv apresenta, em separado, as 36 estimativas teóricas para as extensões X, Y e Z das doze combinações modelo–perfil. Nos casos Paraglider, os valores palm_length_mm e palm_thickness_mm são conservados como contexto do perfil, mas não controlam isoladamente as extensões Y e Z; no Flexy Beast e no Phoenix não existe, nestas configurações, um parâmetro de entrada correspondente a esses dois eixos. Esta diferença encontra-se identificada no campo estado_parametro da folha.":
    "A Tabela D.3 resume a extensão total no eixo X, por ser o único eixo associado a um parâmetro activo nos três modelos. A medição física e o respectivo desvio observado permanecem por preencher. A folha suplementar de comparação dimensional conserva as 36 linhas de medição física ainda por executar. Uma segunda folha suplementar apresenta, em separado, as 36 estimativas teóricas para as extensões X, Y e Z das doze combinações modelo–perfil. Nos casos Paraglider, os valores palm_length_mm e palm_thickness_mm são conservados como contexto do perfil, mas não controlam isoladamente as extensões Y e Z; no Flexy Beast e no Phoenix não existe, nestas configurações, um parâmetro de entrada correspondente a esses dois eixos. Esta diferença encontra-se identificada no registo suplementar.",
    "As Figuras 8.1 a 8.3 reúnem o registo fotográfico das peças produzidas: componentes separados e em montagem parcial, séries dimensionais de segmentos Paraglider Hand e Flexy Beast, e sete vistas de uma UnLimbited Phoenix montada para o perfil simulado de 15 anos. As fotografias originais são conservadas na pasta componentes/figuras/ com o prefixo teste-impressao-; os painéis integrados no documento foram compostos a partir desses ficheiros, sem alteração do conteúdo visual. Três fotografias das séries dimensionais foram apenas rodadas 90° para permitir a leitura correcta da orientação e das identificações manuscritas.":
    "As Figuras 8.1 a 8.3 reúnem o registo fotográfico das peças produzidas: componentes separados e em montagem parcial, séries dimensionais de segmentos Paraglider Hand e Flexy Beast, e sete vistas de uma UnLimbited Phoenix montada para o perfil de ensaio de 15 anos. Os originais integram o material suplementar; os painéis apresentados foram compostos sem alteração do conteúdo visual. Três fotografias das séries dimensionais foram apenas rodadas 90° para permitir a leitura correcta da orientação e das identificações manuscritas.",
}


def update_index_paragraph(paragraph: etree._Element, old: str, new: str) -> bool:
    changed = False
    for node in paragraph.xpath(".//w:t", namespaces=NS):
        if node.text and old in node.text:
            node.text = node.text.replace(old, new)
            changed = True
    return changed


def find_body_paragraph(document: etree._Element, text: str) -> etree._Element:
    matches = [
        paragraph
        for paragraph in document.xpath("//w:body/w:p", namespaces=NS)
        if element_text(paragraph) == text
        and not paragraph_style(paragraph).startswith("ndice")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Esperado um parágrafo de corpo {text!r}; encontrados {len(matches)}"
        )
    return matches[0]


def apply(path: Path) -> tuple[int, int, int]:
    original_mode = path.stat().st_mode
    with ZipFile(path) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}
    document = etree.fromstring(files["word/document.xml"])
    relationships = etree.fromstring(files["word/_rels/document.xml.rels"])

    exact_count = 0
    token_count = 0
    for paragraph in document.xpath("//w:p", namespaces=NS):
        current = element_text(paragraph)
        if current in PARAGRAPH_REPLACEMENTS:
            replace_paragraph_text(paragraph, PARAGRAPH_REPLACEMENTS[current])
            exact_count += 1
            continue
        updated = current
        for old, new in TOKEN_REPLACEMENTS:
            updated = updated.replace(old, new)
        if updated == current:
            continue
        if paragraph_style(paragraph).startswith("ndice"):
            for old, new in TOKEN_REPLACEMENTS:
                update_index_paragraph(paragraph, old, new)
        else:
            replace_paragraph_text(paragraph, updated)
        token_count += 1

    markdown = MARKDOWN.read_text(encoding="utf-8")
    imported_count = 0
    for md_start, md_end, docx_start, docx_end, label in FRAGMENTS:
        elements = import_fragment(
            markdown,
            md_start,
            md_end,
            label,
            document,
            relationships,
            files,
        )
        replace_range(
            find_body_paragraph(document, docx_start),
            find_body_paragraph(document, docx_end),
            elements,
        )
        imported_count += len(elements)

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
    return exact_count, token_count, imported_count


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    exact, token, imported = apply(args.docx.resolve())
    print(f"DOCX actualizado: {args.docx.resolve()}")
    print(f"Parágrafos substituídos integralmente: {exact}")
    print(f"Parágrafos com normalização terminológica: {token}")
    print(f"Elementos importados das fontes Markdown: {imported}")


if __name__ == "__main__":
    main()
