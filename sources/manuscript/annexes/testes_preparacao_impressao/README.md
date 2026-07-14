# Anexo D — Preparação para fabrico e verificação dos protótipos

Esta pasta contém o Anexo D e os dados verificáveis que o sustentam. Os valores
são **estimativas de software de fatiamento** (Bambu Studio e PrusaSlicer), **não
medições físicas** nem indicadores de desempenho estrutural.

| Ficheiro | Descrição |
|---|---|
| `anexo_d_preparacao_impressao.md` | Texto do Anexo D (preparação para impressão, comparação dimensional, orientações de dimensionamento e protocolos físicos ainda por preencher) |
| `resultados_projectos_arquivados.csv` | Série A — 4 projectos arquivados fatiados com o perfil embebido |
| `resultados_campanha_controlada.csv` | Série B — 12 casos (3 modelos × 4 perfis) sob condição virtual comum; o nome do ficheiro conserva a designação técnica original |
| `resultados_geometria.csv` | Geometria: montagem sólida vs palma vs placa disposta; volume, manifold, faces degeneradas |
| `tabela_projectos_arquivados_impressao.csv` | Selecção dos projectos arquivados, incluindo PLA, PETG e as duas impressoras |
| `tabela_preparacao_impressao.csv` | Estimativas seleccionadas dos 12 casos controlados |
| `tabela_comparacao_dimensional.csv` | Entrada, extensões X/Y/Z da malha e campos para três leituras físicas por ponto |
| `protocolo_medicao_dimensional_fisica.md` | Instrumento, referencial, três repetições e cálculo dos desvios |
| `protocolo_montagem_articulacao.md` | Verificação em bancada limitada aos protótipos efectivamente completos |
| `folha_montagem_articulacao.csv` | Folha ainda não preenchida para registar montagem, movimento, fecho e retorno |
| `avaliacao_compatibilidade_dimensionamento.md` | Comparação delimitada com o gráfico Cyborg Beast e a folha Phoenix, sem inferir adequação anatómica |
| `guia_execucao_ensaios_fisicos.md` | Sequência operacional para inventariar, medir, fotografar e observar a montagem dos protótipos |
| `inventario_especimes_fisicos.csv` | Folha vazia para associar cada peça física ao modelo, perfil, material e ficheiro digital |
| `tools/calcular_resultados_dimensionais_fisicos.py` | Programa executado a partir da raiz do repositório depois de preencher as três leituras físicas; calcula média, amplitude e desvios sem substituir a folha original |

**Proveniência.** Gerado em 2026-07-14. Os comandos exactos, versões, *checksums*
e saídas brutas estão no repositório da plataforma, em
`docs/print-validation/slicer-evaluation/` (`protocolo.md`, `comandos_e_versoes.txt`,
`raw/`). Os três CSV são idênticos aos aí depositados.

**Fatiadores:** Bambu Studio `01.10.02.76`; PrusaSlicer `2.8.1`.

**Registo fotográfico (secção D.9).** As fotografias dos protótipos impressos
(peças na placa, série dimensional por perfil, componentes soltos e a mão Phoenix
montada) estão em cópias **redimensionadas** (máx. 1600 px, ~5,5 MB no total) na
subpasta local `figuras/` deste anexo, referenciadas por caminho relativo simples.
Os originais em alta resolução permanecem em `figuras/teste-impressao-*` na raiz do
repositório. São evidência visual qualitativa — não acrescentam medições.

Ver a secção D.8 do anexo para a síntese explícita do que pode e não pode ser
afirmado a partir destes dados.
