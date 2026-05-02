# Extracção e Codificação de Dados Antropométricos da Mão: Metodologia

## 1. Contexto e Objectivo

O desenvolvimento de um gerador paramétrico de próteses de mão requer dados antropométricos da mão humana que sejam suficientemente variados para cobrir diferentes populações, sexos e grupos etários. O objectivo deste processo foi construir uma base de dados estruturada em formato CSV que servisse de entrada directa ao modelo paramétrico, contendo medições reais retiradas de literatura científica publicada e de relatórios militares de referência.

Foram produzidos três ficheiros CSV complementares:

- `ansur_1988_complete.csv` — 2.726 linhas, 47 dimensões corporais do estudo ANSUR 1988 (Gordon et al., 1989), população militar norte-americana
- `ansur_1988_hand_arm.csv` — 696 linhas, subconjunto do ANSUR restrito às medições da mão, antebraço e braço
- `multi_population_hand.csv` — 1.790 linhas, dados de onze estudos populacionais independentes de nove países diferentes

---

## 2. Estratégia de Pesquisa Bibliográfica

### 2.1 Plataforma Elicit e revisões sistemáticas

A pesquisa de literatura foi conduzida na plataforma Elicit, utilizando sessões de agente com questões orientadas para identificar estudos de antropometria da mão com dados primários tabelados. As questões-chave incluíam variações de:

> *"hand anthropometry normative data population study percentiles"*
> *"hand dimensions measurement ergonomics working population"*
> *"anthropometric survey finger length breadth caliper"*

As sessões produziram listas de referências exportadas, que foram ingeridas localmente em pastas organizadas por capítulo da tese. Os ficheiros exportados (relatórios, citações, listas bibliográficas) foram cruzados com a colecção local de PDFs para identificar lacunas.

### 2.2 Base ANSUR 1988

O relatório ANSUR 1988 (Gordon et al., 1989) foi identificado como fonte de referência fundamental por ser um dos estudos antropométricos com maior dimensão amostral disponíveis publicamente (n=9.068 militares norte-americanos). Os dados foram extraídos directamente das tabelas estatísticas detalhadas do relatório (Appendix B), que fornece, para cada dimensão e por sexo, a média, o desvio-padrão, os percentis P5, P10, P25, P50, P75, P90, P95, o mínimo e o máximo.

---

## 3. Critérios de Inclusão e Exclusão de Estudos

Para cada estudo identificado, a decisão de incluir ou excluir os seus dados na base CSV seguiu critérios explícitos.

### 3.1 Critérios de inclusão

Um estudo foi incluído se satisfazia simultaneamente as seguintes condições:

1. **Dados primários** — o estudo apresenta medições recolhidas pelos seus próprios autores sobre participantes reais, não reutilizando tabelas de terceiros sem transformação.
2. **Dimensões da mão ou do membro superior** — pelo menos uma medição refere-se à mão, dedos, palma, antebraço ou punho.
3. **Estatística descritiva legível** — a tabela do artigo fornece, no mínimo, a média. A presença de desvio-padrão e/ou percentis constituía um critério de preferência.
4. **Identificação clara da população** — o artigo especifica país, sexo, dimensão amostral e método de medição.

### 3.2 Critérios de exclusão

Um estudo foi excluído nas seguintes situações:

- **Dados secundários sem valor acrescentado** — por exemplo, o trabalho de Moreo (2016) apresenta valores percentílicos de comprimento de dedo extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas), sem recolha própria. A Tabela 6.1 desse trabalho serve apenas para validar as escolhas de design do protótipo, não constituindo uma fonte primária codificável de forma independente.
- **Artigos de engenharia sem tabelas antropométricas** — estudos centrados em materiais, análise de elementos finitos ou fabrico aditivo que referenciam dimensões da mão apenas de forma incidental e sem estatística descritiva.
- **Dimensões não da mão em estudos mistos** — medições de outras regiões corporais presentes no mesmo artigo foram excluídas se não existia uma razão directa para a prótese de mão (excepção: comprimento cotovelo-ponta dos dedos, incluído por ser relevante para o encaixe do socket).

---

## 4. Processo de Extracção de Dados

### 4.1 Leitura dos PDFs e localização das tabelas

Cada artigo foi lido integralmente, com foco nas secções de *Methods* (para identificar o instrumento de medição, a mão medida, e a posição do participante) e *Results* (para localizar as tabelas com estatística descritiva). A página exacta de cada tabela foi registada no campo `source_page` do CSV.

Quando um artigo reportava medições em mais do que uma tabela (por exemplo, comprimentos numa tabela e larguras noutra), cada tabela foi processada separadamente.

### 4.2 Identificação das unidades e conversão

Os artigos consultados reportam medições em milímetros (mm), centímetros (cm) ou, no caso do ANSUR, em polegadas (in). O CSV armazena sempre os três sistemas em simultâneo (`value_mm`, `value_cm`, `value_in`), calculados a partir de uma única unidade-fonte:

- Se o artigo reporta em mm: `value_cm = value_mm / 10`; `value_in = value_cm / 2.54`
- Se o artigo reporta em cm: `value_mm = value_cm × 10`; `value_in = value_cm / 2.54`

Esta redundância elimina conversões em tempo de execução por parte do modelo paramétrico.

### 4.3 Decomposição em linhas atómicas

Cada célula de uma tabela estatística origina **uma linha independente** no CSV. Assim, para uma dada dimensão, população e sexo, existem tantas linhas quantos os indicadores estatísticos disponíveis: por exemplo, se um artigo reporta média, desvio-padrão, P5, P50 e P95, são criadas cinco linhas — cada uma com o campo `stat_type` definido como `mean`, `std_dev` ou `percentile`, e o campo `percentile` preenchido apenas nas linhas de tipo `percentile`.

Esta estrutura longa (*long format*) permite filtrar e agregar por qualquer combinação de variáveis sem necessidade de transformação prévia.

### 4.4 Registo fiel do contexto da medição

O campo `measurement_method_note` regista, para cada estudo, informações sobre:

- O instrumento utilizado (e.g., "paquímetro digital Vernier 200 mm, resolução 0,01 mm")
- A mão medida (direita/esquerda/dominante)
- A posição da mão durante a medição (estendida e plana, em posição de repouso, sentado)
- O ponto de referência do comprimento (e.g., "da prega palmar proximal à ponta do dedo")

Esta informação é crítica porque estudos diferentes definem as mesmas dimensões com protocolos diferentes: por exemplo, "comprimento da mão" pode ser medido desde a prega do pulso até à ponta do dedo médio (Rodríguez-Vega et al., 2024) ou desde o processo estilóide até à mesma ponta (Anacleto Filho et al., 2023), produzindo valores não directamente comparáveis.

---

## 5. Decisões por Estudo

### 5.1 ANSUR 1988 — EUA, militares (Gordon et al., 1989)

**Fonte:** Tabelas de dados detalhados do relatório técnico do U.S. Army Natick Research Center (março de 1989), 47 dimensões corporais, separadas por sexo (n=2.208 mulheres, n=6.682 homens). As dimensões da mão e do membro superior foram codificadas na íntegra: comprimento da mão, largura da mão, comprimentos dos dedos, circunferência do pulso, comprimento do antebraço, entre outras.

**Decisão:** Incluição total. A dimensão amostral, a abrangência estatística (11 indicadores por dimensão) e a origem militar controlada tornam-no a âncora de referência da base de dados.

**Notas:** Sete valores no relatório original apresentavam inconsistências tipográficas (e.g., percentil aparentemente invertido ou unidade suspeita); todos foram corrigidos com anotação inline no campo `data_quality_note`.

### 5.2 Turquia — jovens adultos (Chatzioglou et al., 2024)

**Fonte:** *Anatomy & Cell Biology*, 57:172–182. n=51 (32F, 19M), idade 18–30, Izmir e Istanbul. Método foto-antropométrico com ImageJ (pixel → mm via factor de calibração 0,08618 ×). Comprimentos dos cinco dedos da mão direita, por sexo e amostra total, Tabela 1.

**Decisão:** Incluição. Primeiro estudo de foto-antropometria da mão na base de dados; o método é documentado de forma rigorosa e o artigo é publicado em revista indexada com revisão por pares. Os valores mínimo e máximo (mas não percentis) são reportados; foram codificados como `stat_type = min` e `max`.

### 5.3 México — população geral (Rodríguez-Vega & Rodríguez-Vega, 2024)

**Fonte:** *European Public & Social Innovation Review*, 9:1–15. n=2.837 (2.275M, 562F), Noroeste do México, idade 15–59. Quatro dimensões: comprimento da mão (HL), comprimento da palma (PL), largura da mão (HB) e diâmetro de preensão (HGD). Tabela 3 (amostra geral) e Tabela 4 (oito grupos etários: 15–19, 20–24, …, 50–54).

**Decisão:** Incluição, com marcação de qualidade nos subgrupos de pequena dimensão. A desagregação por grupo etário é única na base de dados e de grande valor para modelação por faixa etária. Foram detectados dois casos problemáticos na Tabela 4: o subgrupo feminino 50–54 tem n=3 (SD=0,00 reportado para HB, provavelmente artefacto de arredondamento); o subgrupo feminino 45–49 tem n=10. Ambos foram incluídos mas marcados no campo `data_quality_note`.

### 5.4 Índia — mulheres trabalhadoras (Nag et al., 2003)

**Fonte:** *Indian Journal of Medical Research*, 117:260–269. n=95 mulheres, trabalhadores informais (indústria de bidis, agarbattis e vestuário), Ahmedabad. 51 dimensões da mão direita em cinco tabelas (comprimentos, larguras, circunferências, profundidades, extensões e folgas), com P5, P50 e P95 reportados.

**Decisão:** Incluição total. É o estudo com maior granularidade de dimensões da mão na base de dados, e o único com dados de profundidade e circunferência por articulação. A restrição a mulheres e a uma população laboral informal específica é documentada na coluna `population`.

### 5.5 Portugal — trabalhadores industriais (Anacleto Filho et al., 2023)

**Fonte:** *International Journal of Industrial Ergonomics*, 97:103473. n=343 (169M, 174F), trabalhadores industriais do Norte de Portugal, 2021. De um conjunto de 27 dimensões corporais, apenas duas são da mão: comprimento da mão e largura da mão (metacarpal II–V). Tabela 3, P5, P50, P95 por sexo.

**Decisão:** Incluição. Embora apenas duas dimensões da mão sejam disponibilizadas, trata-se da única fonte de dados antropométricos da mão para população portuguesa adulta identificada na literatura, o que a torna indispensável para a contextualização nacional desta tese.

**Nota metodológica:** O estudo mediu o lado esquerdo por limitação de instalações; este facto é registado em `measurement_method_note`.

### 5.6 Nigéria — atletas universitários (Ibiwari et al., 2025)

**Fonte:** *International Journal of Science Academic Research*, 6(8):10513–10517. n=80: basquetebol (n=41: 21M, 20F) e voleibol (n=39: 20M, 19F), Universidade de Port Harcourt, idade 19–30. Quatro dimensões da mão direita por desporto e sexo: comprimento da mão, largura da mão, comprimento palmar e comprimento do 3.º dígito. Tabelas 3 e 4.

**Decisão:** Incluição com marcação de subgrupo desportivo. Dois subgrupos apresentam desvio-padrão atipicamente elevado (e.g., comprimento da mão no voleibol masculino: SD=37,49 mm), sugerindo a presença de outliers na amostra original. Estes casos foram marcados com nota de qualidade; os valores não foram excluídos porque provêm de tabelas publicadas e revistas.

**Nota:** A população de atletas não é representativa da população geral; os valores reflectem uma selecção físicamente activa e potencialmente com mãos de dimensões superiores à média.

### 5.7 Jordânia — trabalhadores com deficiência (Mistarihi, 2020)

**Fonte:** *Data in Brief*, 30:105420. n=40 trabalhadores com deficiência física, governorate de Irbid, Jordânia, idade 20–40. Sexos combinados (sem desagregação por sexo em Tabela 4). Comprimento da mão (mm) e comprimento cotovelo-ponta dos dedos (cm) com P5 e P95 na Tabela 4; largura da mão (cm, média apenas) a partir da Figura 2.

**Decisão:** Inclusão parcial. A dimensão amostral reduzida (n=40) e a ausência de desagregação por sexo limitam a utilidade directa dos dados. No entanto, é o único estudo com dados de uma população do Médio Oriente e com uma população com deficiência, o que justifica a inclusão para representatividade demográfica. A largura da mão (apenas média, sem SD, retirada de um diagrama de figura e não de uma tabela) foi incluída com marcação explícita de qualidade.

### 5.8 EUA — dedo indicador (Lim et al., 2018)

**Fonte:** Trabalho académico UC Berkeley. n=50 adultos, idade 18–30. Apenas duas dimensões do dedo indicador (D2): comprimento MCP-ponta (média=90,9 mm) e largura na articulação PIP (média=16,9 mm). Apenas médias reportadas, sem SD ou percentis.

**Decisão:** Inclusão limitada. A ausência de desvio-padrão e percentis reduz significativamente a utilidade estatística. No entanto, o estudo foi incluído porque é especificamente orientado para a customização de próteses de dedo e fornece valores de referência para o design de um dedo índice protésico — directamente relevantes para o objectivo desta tese. O coeficiente de determinação R²=0,18 entre comprimento e largura do dedo é marcado como indicador de correlação fraca.

### 5.9 Estudo excluído: Moreo (2016)

O trabalho de Moreo (2016), dissertação de mestrado sobre design paramétrico de prótese de mão para crianças, foi lido na íntegra (55 páginas). A Tabela 6.1 apresenta valores percentílicos de comprimento de dedo por grupo etário, mas estes valores são extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas) — não constituindo uma recolha primária por parte da autora. Incluir estes valores equivaleria a duplicar uma fonte secundária sem rastreabilidade directa ao estudo DINED original. **Decisão: excluído.**

### 5.10 EUA — militares ANSUR II (Gordon et al., 2015)

**Fonte:** Relatório técnico NATICK/TR-15/007, U.S. Army Natick Soldier Research, Development and Engineering Center. n=6.068 militares activos (4.082M, 1.986F), idade 17–58, grande diversidade étnica. Os dados brutos individuais foram disponibilizados em acesso público em 2017 (licença CC BY 4.0). As estatísticas foram calculadas a partir dos CSVs individuais (não do relatório impresso), usando Python puro sem dependências externas, por forma a garantir reprodutibilidade exacta.

**Decisão:** Inclusão total. É o maior conjunto de dados individuais de antropometria da mão disponível publicamente. A disponibilidade de dados brutos individuais (em vez de apenas tabelas sumárias) permitiu calcular o conjunto completo de 11 indicadores por dimensão (média, SD, mínimo, máximo, P5, P10, P25, P50, P75, P90, P95). Sete medições codificadas: comprimento da mão, largura da mão (metacarpal), circunferência da mão, comprimento da palma, circunferência do pulso, comprimento antebraço-ponta do dedo médio e comprimento antebraço-centro de preensão.

**Nota:** A medição `wristheight` foi excluída — corresponde à distância do chão ao pulso em posição de pé, uma dimensão postural e não uma medição da mão.

### 5.11 Países Baixos — DINED (TU Delft, 1993–2004)

**Fonte:** Base de dados antropométrica do Delft Institute for Ergonomics and Design, acessível via conta institucional em dined.io.tudelft.nl. Três sub-datasets distintos, com dados de mão disponíveis:

- **kima1993**: crianças neerlandesas, idades 2–12 (grupos por ano), por sexo e combinado; 8 medições da mão por grupo etário.
- **geron1998**: idosos neerlandeses, idades 50–80+ (bandas de 5 anos), por sexo e combinado; 5 medições da mão.
- **dined2004**: adultos neerlandeses, grupos etários 20–30, 31–60, 60+, por sexo e combinado; 6–7 medições da mão.

Os dados foram extraídos a partir do HTML da interface web (padrões `id="mean{col}_{row}"` / `id="sd{col}_{row}"`), mapeando índices de coluna para combinações (sub-dataset, sexo, grupo etário) e índices de linha para nomes de medição.

**Decisão:** Inclusão total (três sub-datasets). Apenas média e desvio-padrão estão disponíveis; percentis não são fornecidos pela interface DINED. O grupo combinado 20–60 do dined2004 foi excluído por ser redundante relativamente aos grupos 20–30 e 31–60. Primeiro dataset pediátrico e o dataset de idosos mais granular da base de dados.

### 5.12 China — idosos de Pequim (Hu et al., 2007)

**Fonte:** *International Journal of Industrial Ergonomics*, 37(4):303–311. DOI: 10.1016/j.ergon.2006.11.006. n=108 (58F, 50M), idade 65–85, residentes na área de Pequim, recrutados por conveniência entre reformados. Medições com paquímetro deslizante e paquímetro de pontas, segundo a norma chinesa GB/T 5703-1999 (equivalente à ISO 7250:1996). Tabela 1 (média e desvio-padrão) e Tabela 2 (P1, P5, P50, P95, P99).

**Decisão:** Inclusão parcial (cinco medições de mão/antebraço: largura da mão no metacarpal, largura máxima da mão, comprimento da mão, comprimento do dedo, comprimento antebraço-ponta dos dedos). P5, P50 e P95 codificados a partir da Tabela 2. A medição "Finger length" usa a designação do padrão GB/T 5703 sem especificar o dígito; assume-se o dedo médio, documentado em `data_quality_note`.

**Nota de cobertura:** Primeira fonte de dados de idosos chineses e, simultaneamente, a única fonte da Ásia Oriental na base de dados (após a verificação de que a referência "Zhuang et al. 2013" não era verificável).

### 5.13 Estudo excluído: Zhou et al. (2016)

**Fonte:** *International Journal of Industrial Ergonomics*, 53:27–36. DOI: 10.1016/j.ergon.2015.10.007. Artigo metodológico sobre reconstrução de modelos corporais 3D a partir de fotografias ortogonais, usando deformação de forma livre (FFD).

**Decisão: excluído.** O artigo não é um estudo de antropometria populacional: apresenta um método de modelação e valida-o sobre um único sujeito. A Figura 12 do artigo compara valores do modelo com valores do participante real para 22 dimensões — não constituindo estatística descritiva de uma amostra. Não há média, desvio-padrão nem percentis de uma população. Incluir o valor de comprimento de mão do sujeito de validação (17 cm, lido do gráfico) seria metodologicamente incorrecto.

---

## 6. Estrutura do CSV e Schema

### 6.1 Campos

| Campo | Tipo | Descrição |
|---|---|---|
| `source_document` | string | Título abreviado do artigo ou relatório fonte |
| `source_page` | int | Página da tabela de origem no documento |
| `source_citation` | string | Citação completa em estilo APA |
| `measurement_name` | string | Nome da dimensão, incluindo especificações de método quando relevante |
| `body_region` | string | Região corporal (`hand`, `forearm`, `upper_arm`, `lower_limb`, `torso`, `head`) |
| `measurement_method_note` | string | Instrumento, mão medida, posição e protocolo de medição |
| `population` | string | Descrição da população (e.g., "Young adults (age 18-30)") |
| `country` | string | País de recolha dos dados |
| `sex` | string | `male`, `female` ou `combined` |
| `age_group` | string | Intervalo etário da (sub)amostra |
| `sample_size` | int | Número de participantes na (sub)amostra |
| `stat_type` | string | Tipo de estatística: `mean`, `std_dev`, `percentile`, `min`, `max` |
| `percentile` | string | Valor do percentil (5, 10, 25, 50, 75, 90, 95) — vazio se não aplicável |
| `value_cm` | float | Valor em centímetros |
| `value_mm` | float | Valor em milímetros |
| `value_in` | float | Valor em polegadas (calculado automaticamente) |
| `data_quality_note` | string | Notas sobre limitações, artefactos ou incertezas do valor |

### 6.2 Formato longo (*long format*)

A opção pelo formato longo — uma linha por estatística, e não uma linha por dimensão com colunas `mean`, `sd`, `p5`, etc. — permite:

- Filtrar facilmente por tipo de estatística sem tratamento especial de colunas opcionais
- Incluir estudos que reportam apenas subconjuntos de estatísticas (e.g., apenas média, sem percentis) sem introduzir células vazias em colunas estruturais
- Acrescentar novos tipos de estatística (e.g., intervalo de confiança) sem alterar o schema

O custo é a repetição dos campos de identificação (país, sexo, dimensão) em cada linha — aceitável dado o volume total de dados (< 5 MB).

---

## 7. Controlo de Qualidade dos Dados

### 7.1 Marcação inline de limitações

O campo `data_quality_note` é preenchido sempre que existe uma das seguintes situações:

- Valor extraído de uma figura (diagrama ou gráfico) em vez de uma tabela
- Subgrupo com n ≤ 10
- Desvio-padrão ausente ou atipicamente elevado
- Valor estimado a partir de estatísticas adjacentes por ilegibilidade da tabela
- Correlação fraca entre variáveis reportada pelo próprio estudo
- Inconsistência tipográfica no documento original, corrigida com nota

### 7.2 Verificação de unidades

Todos os valores foram verificados pela coerência de ordem de grandeza. Por exemplo, um comprimento de mão adulta reportado em cm deve situar-se entre 15 e 22 cm; qualquer valor fora deste intervalo foi relido no artigo original antes de ser codificado.

### 7.3 Rastreabilidade total

Cada linha do CSV contém a citação completa (`source_citation`) e o número de página exacto (`source_page`), permitindo que qualquer valor seja verificado directamente na fonte primária sem necessidade de metadados externos.

---

## 8. Escrita do Código de Geração

Os dados foram codificados em dois scripts Python independentes:

- `generate_ansur_csv.py` — gera `ansur_1988_complete.csv` e `ansur_1988_hand_arm.csv` a partir de dicionários Python embutidos no script, um por tabela do relatório ANSUR
- `generate_multi_population_hand_csv.py` — gera `multi_population_hand.csv` a partir de dez secções numeradas, cada uma correspondente a um estudo ou conjunto de datasets

A escolha de embeber os dados directamente no código (em vez de, por exemplo, folhas de cálculo intermédias) serve três propósitos: (1) rastreabilidade — cada valor está imediatamente adjacente à sua citação e nota de método; (2) reprodutibilidade — executar o script regenera o CSV de forma determinista; (3) controlo de versão — alterações aos dados são visíveis em diff de git, com o contexto de que estudo foi modificado.

O script aplica automaticamente as conversões de unidade, calcula `value_in` a partir de `value_cm`, e valida que nenhuma linha é emitida sem pelo menos uma das colunas `value_mm` ou `value_cm` preenchida.

---

## 9. Resultado Final

| Ficheiro | Linhas (dados) | Países | Estudos | Dimensões distintas |
|---|---|---|---|---|
| `ansur_1988_complete.csv` | 2.726 | 1 (EUA) | 1 | 47 |
| `ansur_1988_hand_arm.csv` | 696 | 1 (EUA) | 1 | 17 |
| `multi_population_hand.csv` | 1.790 | 9 | 11 | ~85 |

O ficheiro `multi_population_hand.csv` cobre nove países (EUA, Países Baixos, Turquia, México, Índia, Portugal, Nigéria, Jordânia, China), ambos os sexos e grupos combinados, grupos etários desde os 2 até aos 80+ anos, e populações tão diversas como crianças em idade escolar, idosos, atletas universitários, trabalhadores industriais, trabalhadoras informais e militares.

---

## 10. Cobertura Global da Base de Dados e Lacunas

### 10.1 O que está coberto

A base de dados `multi_population_hand.csv` foi construída com o objectivo de representar a variabilidade antropométrica da mão humana em múltiplas dimensões: geográfica, demográfica, etária e estatística. A tabela seguinte sintetiza a cobertura actual.

#### 10.1.1 Cobertura geográfica

| Região | Países representados | Fonte(s) |
|---|---|---|
| Europa Ocidental | Portugal, Países Baixos | Anacleto Filho et al. (2023); DINED kima1993, geron1998, dined2004 |
| América do Norte | EUA | ANSUR 1988, ANSUR II 2012, Lim et al. (2018) |
| América Latina | México | Rodríguez-Vega et al. (2024) |
| Médio Oriente | Jordânia | Mistarihi (2020) |
| África | Nigéria | Ibiwari et al. (2025) |
| Sul da Ásia | Índia | Nag et al. (2003) |
| Ásia Oriental | China (Pequim) | Hu et al. (2007) |
| Europa do Sul / Ásia Menor | Turquia | Chatzioglou et al. (2024) |

Nove países estão representados, distribuídos por sete regiões do mundo. A cobertura é particularmente densa nos EUA (três fontes independentes) e nos Países Baixos (três sub-datasets DINED).

#### 10.1.2 Cobertura etária

| Faixa etária | Cobertura | Fonte(s) |
|---|---|---|
| 2–12 anos | Países Baixos | DINED kima1993 (por ano de idade) |
| 15–19 anos | México | Rodríguez-Vega et al. (2024), subgrupo |
| 18–30 anos | EUA, Turquia | Lim et al. (2018); Chatzioglou et al. (2024) |
| 17–58 anos | EUA | ANSUR II 2012 |
| 15–59 anos | México | Rodríguez-Vega et al. (2024), 8 grupos etários |
| 19–30 anos | Nigéria | Ibiwari et al. (2025) |
| 20–40 anos | Jordânia | Mistarihi (2020) |
| 20–60+ anos | Países Baixos | DINED dined2004 (3 grupos) |
| 50–80+ anos | Países Baixos | DINED geron1998 (7 grupos de 5 anos) |
| 65–85 anos | China | Hu et al. (2007) |

A cobertura pediátrica (2–12 anos) existe apenas para os Países Baixos. A adolescência (13–17 anos) está ausente como grupo dedicado — o subgrupo mexicano 15–19 é o mais próximo, mas cobre uma faixa mais alargada. A idade adulta activa (20–60) está bem coberta em múltiplos países. Os idosos estão representados nos Países Baixos (50–80+) e na China (65–85), mas não noutras geografias.

#### 10.1.3 Cobertura estatística

A profundidade estatística varia consideravelmente entre fontes:

| Nível de detalhe | Estudos |
|---|---|
| Média, SD, min, max, P5–P95 (11 indicadores) | ANSUR 1988, ANSUR II 2012 |
| Média, SD, P5, P50, P95 (5 indicadores) | DINED (3 sub-datasets), Hu et al. (2007) |
| P5, P50, P95 (3 indicadores) | Nag et al. (2003), Anacleto Filho et al. (2023), Rodríguez-Vega et al. (2024) |
| Média, SD, min, max (4 indicadores) | Chatzioglou et al. (2024), Ibiwari et al. (2025) |
| Média apenas | Mistarihi (2020) — largura da mão; Lim et al. (2018) |

A maioria das fontes não-americanas fornece apenas subconjuntos de estatísticas. Percentis intermédios (P10, P25, P75, P90) estão disponíveis exclusivamente nos datasets ANSUR. Esta assimetria é uma limitação real: para populações não-americanas, o modelo paramétrico pode interpolar entre P5 e P95, mas não dispõe de percentis de granularidade fina.

---

### 10.2 Onde a cobertura falha

#### 10.2.1 Lacunas geográficas

As regiões mais populosas do mundo estão sub-representadas ou ausentes:

- **Ásia Oriental** — China tem uma única fonte (n=108, apenas idosos de Pequim). Japão e Coreia do Sul estão completamente ausentes, apesar de serem países com literatura ergonómica activa. O conjunto ANSUR é amplamente usado como proxy para populações ocidentais, mas os valores diferem sistematicamente das populações do leste asiático (mãos tendencialmente mais pequenas nos estudos disponíveis).
- **Ásia do Sudeste** — Nenhum país representado (Indonésia, Filipinas, Vietname, Tailândia, etc.), apesar de concentrarem uma fracção significativa da população mundial e de apresentarem diferenças antropométricas documentadas relativamente às populações sul-asiáticas.
- **África Subsaariana** — Apenas a Nigéria, com uma amostra de atletas universitários (n=80) que não é representativa da população geral. Angola, Moçambique, e outros países de língua portuguesa estão ausentes, o que é particularmente relevante numa tese desenvolvida em Portugal.
- **América do Sul** — Completamente ausente. Brasil, Colômbia e Argentina têm literatura ergonómica publicada mas não foram identificadas fontes acessíveis com dados de mão codificáveis.
- **Europa Central e de Leste** — Ausente. Os Países Baixos e Portugal representam a Europa, mas há variabilidade antropométrica documentada entre populações do norte, sul e leste do continente.

#### 10.2.2 Lacunas demográficas

- **Adolescentes (13–17 anos)** — a transição da mão infantil para a adulta não está coberta por nenhum estudo dedicado. O kima1993 chega aos 12 anos e o ANSUR começa aos 17.
- **Amputados** — a mão de referência para uma prótese unilateral é a mão contralateral intacta do próprio utilizador. Não foi identificado nenhum estudo com estatística descritiva da mão intacta de utilizadores de próteses. Esta é a lacuna de maior impacto directo para o objectivo desta tese: sem estes dados, a personalização paramétrica baseia-se em populações saudáveis como aproximação.
- **Pessoas com deficiência física** — apenas o estudo de Mistarihi (2020) cobre esta população (n=40, sexos combinados, Jordânia). A dimensão amostral é insuficiente para ser estatisticamente representativa.
- **Idosos fora da Europa e China** — a prevalência de amputação de membro superior é mais elevada em contextos de baixo rendimento (causas traumáticas, diabetes, doença vascular), mas os dados de idosos disponíveis limitam-se a populações europeias e chinesas.

#### 10.2.3 Limitações qualitativas dos dados existentes

Para além das lacunas por ausência, existem limitações nos dados já presentes:

- **Heterogeneidade de protocolos** — "comprimento da mão" é medido desde pontos de referência distintos consoante o estudo (prega distal do pulso, processo estilóide do rádio, articulação metacarpo-falângica). Os valores não são directamente comparáveis entre fontes sem ajuste, o que limita a integração directa para inferência de valores fora da base de dados.
- **Amostras de conveniência** — a maioria dos estudos não é probabilística: Chatzioglou et al. (2024) recrutou estudantes universitários de Izmir e Istanbul; Ibiwari et al. (2025) recrutou atletas universitários; Hu et al. (2007) recrutou reformados da área de Pequim. A representatividade nacional é, em todos estes casos, questionável.
- **Desequilíbrio de dimensões** — o comprimento da mão e a largura da mão (metacarpal) estão presentes em quase todas as fontes; comprimentos por falange individual, profundidade da palma, e ângulos de abdução dos dedos estão ausentes excepto no ANSUR.
- **Mão medida** — a maioria dos estudos mede a mão dominante ou a mão direita; o estudo português mede a mão esquerda por limitação de instalações. Esta inconsistência é registada nos metadados mas não pode ser corrigida post-hoc.

---

### 10.3 Fontes Identificadas para Expansão Futura

#### 10.3.1 Prioridade alta

**Ran et al. (2009) — China, crianças**
*Lecture Notes in Computer Science* (ICDHM 2009), 5620:46–54. DOI: 10.1007/978-3-642-02809-0_6. n=20.000 crianças chinesas, idades 4–17 anos. Oito dimensões da mão com média, desvio-padrão, P5 e P95. Preencheria a lacuna pediátrica para a Ásia Oriental e complementaria o kima1993 neerlandês com uma população de outra origem.

**Dianat et al. (2014) — Irão, trabalhadores industriais**
*International Journal of Industrial Ergonomics*, 44:107–114. n=200 (100M, 100F), trabalhadores de Tabriz, Irão. Cobriria o Médio Oriente com maior dimensão amostral e desagregação por sexo, em contraste com o estudo de Mistarihi (2020), que tem apenas n=40 e sexos combinados.

**SIZE KOREA — Coreia do Sul, base de dados pública**
Base de dados antropométrica governamental da Korean Agency for Technology and Standards. Disponível em acesso aberto, cobre adultos e crianças com dados da mão. Completaria a cobertura da Ásia Oriental.

#### 10.3.2 Prioridade média

**Greiner (1991) — EUA, mão (relatório técnico Natick)**
Relatório técnico "Hand Anthropometry of U.S. Army Personnel" (TR-91/010). Complemento ao ANSUR com dimensões da mão muito mais granulares: comprimentos por falange, profundidades por articulação, ângulos de preensão. Acrescentaria detalhe anatómico de alta relevância para o design de dedos protésicos articulados.

**Chen, Wang & Liu (2022) — China, adultos (3D scanning)**
*Lecture Notes in Computer Science* (HCII 2022), 13322. DOI: 10.1007/978-3-031-05900-1_26. n=937 adultos (468M, 469F), 6 regiões da China, idades 22–60. Método de escaneamento 3D semi-automático. Complementaria o Hu et al. (2007) com uma amostra de adultos em idade activa e maior cobertura geográfica dentro da China.

#### 10.3.3 Pertinência directa para o tema da tese

**Dados de amputados — mão contralateral intacta**
Esta é a lacuna de maior impacto. Para o design de próteses de mão personalizada, a referência correcta é a mão intacta do próprio utilizador — não a média de uma população saudável. Não foi identificada nenhuma fonte publicada com estatística descritiva desta população específica. A condução de uma recolha primária de dados (mesmo com n reduzido) seria metodologicamente mais valiosa do que acrescentar novas populações saudáveis.
