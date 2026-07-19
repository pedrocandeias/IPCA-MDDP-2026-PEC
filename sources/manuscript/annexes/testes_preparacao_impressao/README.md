# Anexo D — Preparação para fabrico e verificação dos protótipos

Esta pasta contém o Anexo D e os dados que o sustentam. Os valores de tempo,
filamento, massa, volume e custo são **estimativas dos programas de preparação
para impressão 3D**. A comparação dimensional contém **medições físicas** das
palmas em PLA e PETG. Nenhum destes resultados constitui um indicador de
desempenho estrutural.

A selecção destinada à entrega encontra-se em
`suplementos/04_preparacao_impressao_prototipos/`. Inclui os quatro projectos 3MF,
os resultados completos, os protocolos necessários, a observação de montagem
preenchida e as fotografias originais, sem folhas vazias ou tabelas substituídas.

| Ficheiro | Descrição |
|---|---|
| `anexo_d_preparacao_impressao.md` | Texto do Anexo D (preparação para impressão, comparação dimensional em PLA e PETG, orientações de dimensionamento e observação parcial da montagem da UnLimbited Phoenix) |
| `resultados_projectos_arquivados.csv` | Série A — 4 projectos de preparação digital para impressão 3D processados com a configuração própria de cada caso; o nome técnico do ficheiro conserva a designação histórica |
| `resultados_campanha_controlada.csv` | Série B — 12 casos (3 modelos × 4 perfis) sob condição virtual comum; o nome do ficheiro conserva a designação técnica original |
| `resultados_geometria.csv` | Geometria: montagem sólida vs palma vs placa disposta; volume, manifold, faces degeneradas |
| `tabela_projectos_arquivados_impressao.csv` | Selecção dos projectos de preparação digital para impressão 3D com configuração analisada, incluindo PLA, PETG e as duas impressoras; o nome técnico do ficheiro conserva a designação histórica |
| `tabela_preparacao_impressao.csv` | Estimativas seleccionadas dos 12 casos controlados |
| `tabela_comparacao_dimensional.csv` | 72 comparações entre as extensões X/Y/Z das malhas e um valor medido por eixo nas palmas em PLA e PETG |
| `tabela_estimativa_dimensional_teorica.csv` | Cenário teórico de planeamento anterior, substituído nos resultados pelas medições físicas; conservado apenas como registo histórico da preparação do ensaio |
| `protocolo_medicao_dimensional_fisica.md` | Instrumento, referencial e procedimento opcional para uma futura caracterização metrológica com três leituras por eixo |
| `protocolo_montagem_articulacao.md` | Verificação em bancada limitada aos protótipos efectivamente completos |
| `folha_montagem_articulacao.csv` | Registo parcial da UnLimbited Phoenix `teen_15` em PLA: montagem, movimento dos cinco dedos, fecho e retorno observados; substituição dos elásticos após alargamento em ensaios repetidos; Flexy Beast e Paraglider Hand por preencher |
| `avaliacao_compatibilidade_dimensionamento.md` | Comparação delimitada com o gráfico Cyborg Beast e a folha Phoenix, sem inferir adequação anatómica |
| `guia_execucao_ensaios_fisicos.md` | Sequência operacional opcional para aprofundar as medições, fotografar os pontos de contacto e observar a montagem dos protótipos |
| `inventario_especimes_fisicos.csv` | Folha vazia para associar cada peça física ao modelo, perfil, material e ficheiro digital |
| `tools/calcular_resultados_dimensionais_fisicos.py` | Programa executado a partir da raiz do repositório depois de preencher as três leituras físicas; calcula média, amplitude e desvios sem substituir a folha original |

**Origem dos dados.** Os resultados de preparação e geometria foram gerados em
2026-07-14, com as versões e condições registadas no material técnico da
plataforma. A comparação dimensional foi actualizada em 2026-07-15 com as
medições físicas das palmas em PLA e PETG e, por esse motivo, substitui a folha
inicial que continha apenas os valores das malhas e campos de medição vazios.

**Programas de preparação para impressão 3D:** Bambu Studio `01.10.02.76`; PrusaSlicer `2.8.1`.

**Montagem e articulação.** A folha contém uma observação da UnLimbited
Phoenix em PLA, no perfil `teen_15`. A montagem foi concluída sem correcção permanente
das peças, os pinos foram colocados sem dano, os cinco dedos apresentaram
movimento livre e foram observados o fecho por cabo e o retorno. Após ensaios
repetidos, os elásticos das articulações alargaram e tiveram de ser substituídos;
o funcionamento foi restabelecido depois da substituição. O número exacto de
ciclos e o envolvimento dos cilindros
não ficaram registados, pelo que esta observação não deve ser apresentada como
ensaio sistemático de durabilidade ou preensão.

**Registo fotográfico (secção D.9).** As fotografias dos protótipos impressos
(peças na placa, série dimensional por perfil, componentes soltos e a mão Phoenix
montada) estão em cópias **redimensionadas** (máx. 1600 px, ~5,5 MB no total) na
subpasta local `figuras/` deste anexo, referenciadas por caminho relativo simples.
Os originais em alta resolução permanecem em `figuras/teste-impressao-*` na raiz do
repositório. São evidência visual qualitativa; os valores dimensionais resultam da
medição directa das peças, não das fotografias.

Ver a secção D.8 do anexo para a síntese explícita do que pode e não pode ser
afirmado a partir destes dados.
