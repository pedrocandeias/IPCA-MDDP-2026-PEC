#!/usr/bin/env python3
"""Constrói o pacote mínimo de suplementos entregue com a dissertação.

O programa copia evidências seleccionadas das áreas de trabalho sem alterar os
originais. Gera ainda um guia geral e um manifesto rastreável.
"""

from __future__ import annotations

import csv
import shutil
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "suplementos"
PLATFORM = Path("/home/pec/dev/ai-parametric-prosthetic-hand-generator")
PLATFORM_ARCHIVE = Path("/home/pec/dev/backuptese/ai-parametric-prosthetic-hand-generator")


ROOT_GUIDE = """# Suplementos da dissertação

Este directório constitui o pacote de material suplementar entregue com a
dissertação. Reúne apenas os ficheiros necessários para consultar e auditar os
dados e resultados mencionados no manuscrito.

| Identificador | Suplemento | Conteúdo principal |
|---|---|---|
| S1 | Dados antropométricos | Três conjuntos CSV usados para estruturar a base local |
| S2 | Avaliação técnica da plataforma | Protocolos, metadados e resultados seleccionados das campanhas técnicas e da avaliação da IA |
| S3 | Parametrização e percurso numérico | Dicionário integral de 42 parâmetros e exemplo rastreável entre perfil, cálculos e malhas |
| S4 | Preparação para impressão e protótipos | Projetos 3MF, resultados das Séries A e B, geometria, medições, montagem e fotografias originais |

## Consulta

- `manifesto_ficheiros.csv` identifica o suplemento, o caminho entregue, a
  origem e a função de cada ficheiro.
- Cada subpasta inclui um ficheiro `descricao_do_suplemento_*.md` que delimita o
  respectivo conteúdo e a sua interpretação.

## Critério de selecção

Não foram incluídos os DOCX/PDF autónomos dos anexos, modelos de relatório por
preencher, folhas vazias, tabelas preliminares substituídas, programas auxiliares
de geração, ficheiros temporários ou representações duplicadas. Nas campanhas da
plataforma conservaram-se os metadados e os resultados estruturados que sustentam
as afirmações do manuscrito; foram omitidos agregados internos e estados
intermédios redundantes. Na preparação para impressão conservaram-se os quatro
projetos com parâmetros próprios, os resultados completos em CSV e as fotografias
originais, sem duplicar as 116 exportações individuais já resumidas nos registos.

Os suplementos documentam o processo técnico realizado. Não demonstram adequação
clínica, conforto, segurança, durabilidade ou eficácia protésica.
"""

S1_GUIDE = """# S1 — Dados antropométricos

Este suplemento contém os três CSV usados na preparação da base antropométrica
local da plataforma: a fonte ANSUR completa, o subconjunto da mão e do membro
superior e a compilação multipopulacional da mão.

Os três ficheiros são mantidos porque o manuscrito distingue as linhas de origem
dos perfis agregados posteriormente pela aplicação. Os programas que os geraram
permanecem na área de trabalho do projeto, mas não são necessários para consultar
ou verificar os dados entregues e, por isso, não integram este pacote mínimo.
"""

S2_GUIDE = """# S2 — Avaliação técnica da plataforma

Este suplemento reúne o protocolo geral, a matriz de casos e as evidências
seleccionadas das campanhas de repetição, recuperação e acessibilidade. Inclui os
metadados com datas, comandos e identificadores técnicos mencionados no Capítulo
8, bem como os resultados estruturados necessários à leitura do Anexo B.

A subpasta `avaliacao_ia_antropometrica/` conserva os pedidos, metadados e
resultados que sustentam os cenários apresentados na Secção 8.2. A grelha manual
de acessibilidade é entregue em Markdown e DOCX, correspondendo às evidências
ANNEX-B-014 e ANNEX-B-015.

Foram excluídos modelos de relatório por preencher, resultados agregados do
executor que duplicavam os ficheiros seleccionados e estados intermédios sem
utilização directa no manuscrito. Não são incluídas credenciais ou chaves de API.
"""

S3_GUIDE = """# S3 — Parametrização e percurso numérico

Este suplemento preserva o dicionário integral dos 42 parâmetros numéricos dos
três modelos comparados nos ensaios principais e um percurso rastreável do perfil
de ensaio de 8 anos do Flexy Beast.

O percurso inclui os parâmetros aplicados, os cálculos derivados e três malhas
3MF. Corresponde ao estado usado nos ensaios principais; as alterações posteriores
encontram-se descritas no Anexo C e não devem ser projectadas retroactivamente
sobre estes ficheiros.
"""

S4_GUIDE = """# S4 — Preparação para impressão e protótipos

Este suplemento reúne os quatro projetos 3MF da Série A, os resultados completos
das Séries A e B, o registo geométrico, as 72 comparações dimensionais, os
protocolos relevantes e a observação de montagem da UnLimbited Phoenix produzida
em PLA para o perfil de ensaio de 15 anos.

A folha de montagem entregue contém apenas o espécime efectivamente observado;
as linhas vazias dos modelos não ensaiados foram retiradas. As 19 fotografias são
os originais correspondentes às imagens qualitativas apresentadas no Capítulo 8
e no Anexo D. Não foram incluídas tabelas teóricas substituídas por medições,
folhas de inventário vazias, guias opcionais ou tabelas-resumo duplicadas.

Os tempos, o filamento, a massa e os custos são estimativas dos programas de
preparação. A observação de montagem não constitui ensaio sistemático de
durabilidade ou preensão.
"""


def ensure_source(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"Fonte não encontrada: {path}")


def copy_file(
    source: Path,
    target_relative: str,
    supplement: str,
    description: str,
    records: list[dict[str, str]],
    source_label: str | None = None,
) -> None:
    ensure_source(source)
    target = OUT / target_relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    records.append(
        {
            "suplemento": supplement,
            "caminho_entrega": target_relative,
            "ficheiro_origem": source_label or str(source.relative_to(ROOT)),
            "descricao": description,
        }
    )


def write_generated(
    target_relative: str,
    content: str,
    supplement: str,
    description: str,
    records: list[dict[str, str]],
) -> None:
    target = OUT / target_relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    records.append(
        {
            "suplemento": supplement,
            "caminho_entrega": target_relative,
            "ficheiro_origem": "gerado para o pacote de entrega",
            "descricao": description,
        }
    )


def prepare_output() -> None:
    if OUT.exists():
        marker = OUT / "guia_dos_suplementos.md"
        recognised = marker.is_file() and "Suplementos da dissertação" in marker.read_text(
            encoding="utf-8", errors="replace"
        )
        if not recognised:
            raise RuntimeError(
                "A pasta suplementos já existe e não foi reconhecida como saída deste programa"
            )
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)


def add_s1(records: list[dict[str, str]]) -> None:
    base = ROOT / "sources/manuscript/annexes/dados_antropometricos_v14.67.0"
    write_generated(
        "01_dados_antropometricos/descricao_do_suplemento_1.md",
        S1_GUIDE,
        "S1",
        "Índice e limite de interpretação dos dados antropométricos",
        records,
    )
    for name, description in (
        ("ansur_1988_complete.csv", "Fonte ANSUR completa usada na preparação dos dados"),
        ("ansur_1988_hand_arm.csv", "Subconjunto ANSUR da mão e do membro superior"),
        ("multi_population_hand.csv", "Compilação multipopulacional de medidas da mão"),
    ):
        copy_file(
            base / name,
            f"01_dados_antropometricos/{name}",
            "S1",
            description,
            records,
        )


def add_s2(records: list[dict[str, str]]) -> None:
    base = ROOT / "sources/manuscript/annexes/testes_plataforma"
    write_generated(
        "02_avaliacao_plataforma/descricao_do_suplemento_2.md",
        S2_GUIDE,
        "S2",
        "Índice e limite de interpretação da avaliação técnica",
        records,
    )
    copy_file(
        base / "protocolo_geral_avaliacao_plataforma.md",
        "02_avaliacao_plataforma/protocolo_geral.md",
        "S2",
        "Protocolo geral da avaliação técnica",
        records,
    )
    copy_file(
        base / "matriz_casos_teste.csv",
        "02_avaliacao_plataforma/matriz_casos_teste.csv",
        "S2",
        "Matriz dos casos e critérios de ensaio",
        records,
    )

    evidence = base / "evidencias"
    selected = (
        (
            "2026-07-13_23-22-21_repetition/metadados.json",
            "repeticao/metadados.json",
            "ANNEX-B-001 — metadados, datas, comandos e identificadores da repetição",
        ),
        (
            "2026-07-13_23-22-21_repetition/results/REP-DET-001.json",
            "repeticao/REP-DET-001.json",
            "ANNEX-B-002 — repetição Flexy Beast",
        ),
        (
            "2026-07-13_23-22-21_repetition/results/REP-DET-002.json",
            "repeticao/REP-DET-002.json",
            "ANNEX-B-003 — repetição Paraglider Hand",
        ),
        (
            "2026-07-13_23-22-21_repetition/results/REP-DET-003.json",
            "repeticao/REP-DET-003.json",
            "ANNEX-B-004 — repetição UnLimbited Phoenix",
        ),
        (
            "2026-07-13_23-22-21_repetition/results/xbr-comparison.json",
            "repeticao/comparacao_navegadores.json",
            "ANNEX-B-005 — comparação entre navegadores",
        ),
        (
            "2026-07-14_00-02-40_robustness/metadados.json",
            "robustez/metadados.json",
            "ANNEX-B-006 — metadados, comando e identificadores da robustez",
        ),
        (
            "2026-07-14_00-02-40_robustness/results/robustness-api.json",
            "robustez/resultados_api.json",
            "ANNEX-B-007 — resultados dos pedidos directos",
        ),
        (
            "2026-07-14_00-02-40_robustness/results/robustness-ui.json",
            "robustez/resultados_interface.json",
            "ANNEX-B-008 — resultados de recuperação na interface",
        ),
        (
            "2026-07-14_00-03-19_a11y-local/metadados.json",
            "acessibilidade/metadados_local.json",
            "ANNEX-B-009 — metadados da avaliação automática local",
        ),
        (
            "2026-07-14_00-03-19_a11y-local/results/a11y-local-summary.json",
            "acessibilidade/resultados_automaticos_local.json",
            "ANNEX-B-010 — síntese automática local",
        ),
        (
            "2026-07-14_00-06-48_a11y-public/metadados.json",
            "acessibilidade/metadados_publico.json",
            "ANNEX-B-012 — metadados da avaliação automática pública",
        ),
        (
            "2026-07-14_00-06-48_a11y-public/results/a11y-public.json",
            "acessibilidade/resultados_automaticos_publico.json",
            "ANNEX-B-013 — síntese automática da página pública",
        ),
        (
            "lista_verificacao_manual_acessibilidade_wcag_2_2.md",
            "acessibilidade/verificacao_manual_wcag_2_2.md",
            "ANNEX-B-014 — resultado editável da avaliação manual",
        ),
        (
            "lista_verificacao_manual_acessibilidade_wcag_2_2.docx",
            "acessibilidade/verificacao_manual_wcag_2_2.docx",
            "ANNEX-B-015 — representação DOCX da avaliação manual",
        ),
    )
    for source_rel, target_rel, description in selected:
        copy_file(
            evidence / source_rel,
            f"02_avaliacao_plataforma/evidencias/{target_rel}",
            "S2",
            description,
            records,
        )

    ai_files = [PLATFORM / "docs/ai_anthropometric_validation.md"]
    for directory in (
        "flexy-beast-ai-sim",
        "paraglider-ai-sim",
        "phoenix-ai-sim",
        "ucd-ai-sim",
    ):
        ai_files.extend(sorted((PLATFORM / "docs" / directory).glob("*")))
    for source in ai_files:
        relative = source.relative_to(PLATFORM / "docs")
        copy_file(
            source,
            f"02_avaliacao_plataforma/avaliacao_ia_antropometrica/{relative}",
            "S2",
            "Pedido, metadados ou resultado da avaliação antropométrica por IA",
            records,
            source_label=f"ai-parametric-prosthetic-hand-generator/docs/{relative}",
        )


def add_s3(records: list[dict[str, str]]) -> None:
    base = ROOT / "sources/manuscript/annexes/dicionario_parametros_v14.67.0"
    write_generated(
        "03_parametrizacao_percurso/descricao_do_suplemento_3.md",
        S3_GUIDE,
        "S3",
        "Índice e limite de interpretação do percurso paramétrico",
        records,
    )
    copy_file(
        base / "parameter_dictionary.csv",
        "03_parametrizacao_percurso/dicionario_parametros.csv",
        "S3",
        "Dicionário integral dos 42 parâmetros numéricos",
        records,
    )
    example = base / "example_flexy_beast_child_8"
    descriptions = {
        "params.json": "Perfil de ensaio e parâmetros aplicados",
        "trace.json": "Limites, cálculos, métricas e resumos de integridade",
        "palm.3mf": "Malha 3MF da palma",
        "middle_base.3mf": "Malha 3MF do segmento proximal do dedo médio",
        "middle_tip.3mf": "Malha 3MF do segmento distal do dedo médio",
    }
    for name, description in descriptions.items():
        copy_file(
            example / name,
            f"03_parametrizacao_percurso/percurso_flexy_beast_8_anos/{name}",
            "S3",
            description,
            records,
        )


def add_s4(records: list[dict[str, str]]) -> None:
    base = ROOT / "sources/manuscript/annexes/testes_preparacao_impressao"
    write_generated(
        "04_preparacao_impressao_prototipos/descricao_do_suplemento_4.md",
        S4_GUIDE,
        "S4",
        "Índice e limite de interpretação da preparação e dos protótipos",
        records,
    )
    data_files = (
        (
            "resultados_projectos_arquivados.csv",
            "resultados_serie_a.csv",
            "Resultados completos dos quatro projetos da Série A",
        ),
        (
            "resultados_campanha_controlada.csv",
            "resultados_serie_b.csv",
            "Resultados completos dos doze casos da Série B",
        ),
        (
            "resultados_geometria.csv",
            "resultados_geometria.csv",
            "Registo geométrico das montagens, palmas e placas",
        ),
        (
            "tabela_comparacao_dimensional.csv",
            "comparacao_dimensional_72_medicoes.csv",
            "Comparação entre malha e peça nos três eixos e dois materiais",
        ),
        (
            "protocolo_medicao_dimensional_fisica.md",
            "protocolo_medicao_dimensional.md",
            "Protocolo e referencial da medição dimensional",
        ),
        (
            "protocolo_montagem_articulacao.md",
            "protocolo_montagem_articulacao.md",
            "Protocolo de montagem e articulação em bancada",
        ),
        (
            "avaliacao_compatibilidade_dimensionamento.md",
            "compatibilidade_dimensionamento.md",
            "Nota técnica de compatibilidade com orientações de dimensionamento",
        ),
    )
    for source_name, target_name, description in data_files:
        copy_file(
            base / source_name,
            f"04_preparacao_impressao_prototipos/registos/{target_name}",
            "S4",
            description,
            records,
        )

    montage_source = base / "folha_montagem_articulacao.csv"
    ensure_source(montage_source)
    with montage_source.open(encoding="utf-8", newline="") as source_stream:
        reader = csv.DictReader(source_stream)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise RuntimeError("A folha de montagem não tem cabeçalho")
        completed = [row for row in reader if row.get("identificador_especime", "").strip()]
    if len(completed) != 1:
        raise RuntimeError(
            f"Esperava uma única observação de montagem preenchida; encontrei {len(completed)}"
        )
    montage_target_rel = (
        "04_preparacao_impressao_prototipos/registos/montagem_phoenix_15_anos.csv"
    )
    montage_target = OUT / montage_target_rel
    montage_target.parent.mkdir(parents=True, exist_ok=True)
    with montage_target.open("w", encoding="utf-8", newline="") as target_stream:
        writer = csv.DictWriter(target_stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(completed)
    records.append(
        {
            "suplemento": "S4",
            "caminho_entrega": montage_target_rel,
            "ficheiro_origem": str(montage_source.relative_to(ROOT)),
            "descricao": "Observação preenchida da montagem da Phoenix; linhas vazias omitidas",
        }
    )

    project_base = PLATFORM_ARCHIVE / "docs/print-validation"
    for name, description in (
        ("flexy_beast_teen_15_print.3mf", "Projeto Flexy Beast, perfil de 15 anos, PLA"),
        (
            "unlimbed_phoenix_hand_teen_15_print_project.3mf",
            "Projeto UnLimbited Phoenix, perfil de 15 anos, PLA",
        ),
        (
            "unlimbed_phoenix_hand_teen_15_print_project_PETG.3mf",
            "Projeto UnLimbited Phoenix, perfil de 15 anos, PETG",
        ),
        (
            "paraglider_15_teen_prusa_print_profile.3mf",
            "Projeto Paraglider Hand, perfil de 15 anos, PLA",
        ),
    ):
        copy_file(
            project_base / name,
            f"04_preparacao_impressao_prototipos/projectos_preparacao/{name}",
            "S4",
            description,
            records,
            source_label=f"ai-parametric-prosthetic-hand-generator/docs/print-validation/{name}",
        )

    photo_names = (
        "teste-impressao-08214702.jpg",
        "teste-impressao-08214912.jpg",
        "teste-impressao-09201338.jpg",
        "teste-impressao-09201340.jpg",
        "teste-impressao-09201343.jpg",
        "teste-impressao-12185320.jpg",
        "teste-impressao-12185529.jpg",
        "teste-impressao-12185532.jpg",
        "teste-impressao-3d-dedos-flexy-beast.jpeg",
        "teste-impressao-dedos-flexy-beast-v1.jpeg",
        "teste-impressao-dedos-flexy-beast-v2.jpeg",
        "teste-impressao-dedos-paraglider-hand-v1.jpeg",
        "teste-impressao-phoenix-15-anos-13221108.jpg",
        "teste-impressao-phoenix-15-anos-13221111.jpg",
        "teste-impressao-phoenix-15-anos-13221117.jpg",
        "teste-impressao-phoenix-15-anos-13221145.jpg",
        "teste-impressao-phoenix-15anos-0008.jpeg",
        "teste-impressao-phoenix-15anos-0010.jpeg",
        "teste-impressao-phoenix-15anos-0012.jpeg",
    )
    for name in photo_names:
        copy_file(
            ROOT / "figuras" / name,
            f"04_preparacao_impressao_prototipos/fotografias_originais/{name}",
            "S4",
            "Fotografia original dos protótipos e componentes produzidos",
            records,
        )


def validate_and_write_manifest(records: list[dict[str, str]]) -> None:
    for record in records:
        path = OUT / record["caminho_entrega"]
        record["tamanho_bytes"] = str(path.stat().st_size)

    manifest = OUT / "manifesto_ficheiros.csv"
    fields = (
        "suplemento",
        "caminho_entrega",
        "ficheiro_origem",
        "descricao",
        "tamanho_bytes",
    )
    with manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(records, key=lambda row: row["caminho_entrega"]))

    # Valida os projectos 3MF, os CSV e a ausência de ficheiros de trabalho.
    for path in OUT.rglob("*.3mf"):
        with ZipFile(path) as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Projeto ou malha 3MF corrompido: {path}")
    for path in OUT.rglob("*.csv"):
        with path.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream))
        if not rows or not rows[0]:
            raise RuntimeError(f"CSV vazio ou sem cabeçalho: {path}")
    forbidden = {"__pycache__", ".DS_Store"}
    if any(path.name in forbidden or path.suffix == ".tmp" for path in OUT.rglob("*")):
        raise RuntimeError("O pacote contém ficheiros de trabalho proibidos")


def main() -> None:
    prepare_output()
    records: list[dict[str, str]] = []
    write_generated(
        "guia_dos_suplementos.md",
        ROOT_GUIDE,
        "GERAL",
        "Índice geral e critério de selecção do pacote",
        records,
    )
    add_s1(records)
    add_s2(records)
    add_s3(records)
    add_s4(records)
    validate_and_write_manifest(records)
    file_count = sum(1 for path in OUT.rglob("*") if path.is_file())
    total_size = sum(path.stat().st_size for path in OUT.rglob("*") if path.is_file())
    print(
        f"Pacote criado em {OUT}: {file_count} ficheiros, "
        f"{total_size / (1024 * 1024):.1f} MiB"
    )


if __name__ == "__main__":
    main()
