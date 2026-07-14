# Anexo D — Preparação para fabrico e verificação dos protótipos

## D.1 Finalidade

Este anexo reúne evidência verificável sobre a **preparação para impressão** das
mãos protésicas paramétricas geradas pela plataforma HandFab, no contexto de uma
dissertação de **Design e Desenvolvimento de Produto**. O objectivo não é
demonstrar desempenho mecânico nem validar uma impressão física, mas sim
caracterizar, sob condições documentadas, as **exigências de fabrico digital** que o
sistema paramétrico coloca a jusante do projecto: quanto material, quanto tempo,
quantas placas de impressão e que condições de preparação decorrem de cada modelo
e de cada dimensão antropométrica. O anexo prepara também a comparação entre
entrada, malha e peça física e a observação da montagem e articulação; estes dois
ensaios só produzirão resultados depois de serem efectuadas as medições e
observações nos protótipos correspondentes.

As duas séries aqui apresentadas constituem verificações técnicas complementares
da fase empírica prevista na metodologia aprovada. Não introduzem novas perguntas,
hipóteses ou fases metodológicas; aprofundam a documentação da passagem entre
configuração paramétrica, geometria digital e preparação para fabrico.

A preparação para impressão é uma etapa própria do processo de desenvolvimento de
produto: liga a decisão de projecto, expressa na geometria paramétrica, ao meio de
produção por impressão FFF. A estimativa do tempo, do material e do número de
placas permite caracterizar a **exigência de preparação** e apoiar o planeamento
do fabrico. Estes indicadores não demonstram, por si só, acessibilidade económica,
viabilidade de implementação ou capacidade de utilização por não especialistas.

## D.2 Distinção entre estimativa e medição real

Todos os valores numéricos deste anexo — tempo, comprimento de filamento, massa,
volume, custo — são **estimativas produzidas por software de fatiamento** (Bambu
Studio e PrusaSlicer). São o resultado do planeamento de trajectórias que o
fatiador faz antes de existir qualquer objecto físico.

Em consequência, e de forma explícita:

- **Não são medições de impressões reais.** Uma impressão física difere por
  factores de máquina, humidade do filamento, calibração e temperatura.
- **Não são indicadores de desempenho estrutural.** O tempo ou a massa estimados
  nada dizem sobre a resistência da peça.
- **A verificação de malha é geométrica, não mecânica.** «Estanque/manifold» e
  «faces degeneradas» descrevem a integridade do ficheiro 3D; não são medida da
  robustez do objecto impresso.
- **As estimativas dependem da versão e do perfil.** Trocar de versão de fatiador,
  de perfil de processo ou de firmware altera os números.

Estes valores devem, pois, ser lidos como **indicadores comparativos de exigência
de preparação**, e não como propriedades físicas do produto final.

## D.3 Variáveis, controlos e materiais

Foram conduzidas duas séries de ensaios complementares. Os comandos exactos, versões e
*checksums* estão no repositório do projecto (`docs/print-validation/slicer-evaluation/`).

**Programas:** Bambu Studio `01.10.02.76`; PrusaSlicer `2.8.1`.
Análise geométrica em Python 3.12 / NumPy 2.4 (sem fatiamento).

### D.3.1 Série A — projectos arquivados (fatiados como preparados)

Quatro projectos de impressão previamente preparados e preservados foram
**re-fatiados com o seu próprio perfil embebido**, mantendo layout e orientação.
(Observação metodológica: os ficheiros guardavam geometria, definições e
disposição na placa, mas **não** os resultados de fatiamento; estes tiveram de ser
recalculados.)

| # | Modelo | Idade | Material | Fatiador / Impressora |
|---|---|---|---|---|
| 1 | Flexy Beast | 15 | PLA | Bambu Studio / Bambu Lab A1 |
| 2 | UnLimbited Phoenix | 15 | PLA | Bambu Studio / Bambu Lab A1 |
| 3 | UnLimbited Phoenix | 15 | PETG | Bambu Studio / Bambu Lab A1 |
| 4 | Paraglider Hand | 15 | PLA | PrusaSlicer / Prusa MINI |

Nesta série, cada projecto conserva as suas próprias definições (variáveis
**não** controladas entre casos): notavelmente, os três casos Bambu usam **camada
de 0,24 mm** e **suportes em árvore orgânica**, enquanto o caso PrusaSlicer usa
**camada de 0,20 mm** e **sem suportes**. A Série A serve para documentar os
projectos tal como foram preparados, não para os comparar entre si.

### D.3.2 Série B — comparação digital controlada

Três modelos (Flexy Beast, Paraglider Hand, UnLimbited Phoenix) × quatro perfis
simulados (`child_8`, `teen_15`, `adult_28`, `elderly_70`), fatiados sob **uma única
condição virtual comum**, para isolar o efeito do **modelo** e da **dimensão**:

| Variável | Estatuto | Valor |
|---|---|---|
| Impressora | controlada | Bambu Lab A1, bico 0,4 mm |
| Filamento | controlada | Bambu PLA Basic |
| Altura de camada | controlada | 0,20 mm |
| Paredes | controlada | 2 |
| Enchimento | controlada | 15%, grelha |
| Suportes | controlada (política única) | **desligados** |
| Aba | controlada | automática |
| Modelo e conjunto dimensional do perfil | variáveis de comparação | 3 × 4 |

A orientação de cada peça exportada foi mantida; o fatiador apenas dispôs as peças
na placa, criando automaticamente uma segunda placa A1 quando não cabiam numa.
Esta série de ensaios constitui uma **comparação digital controlada da exigência de preparação** —
**não** representa uma impressão física nem uma recomendação de imprimibilidade.

Na análise geométrica, `n_corpos` designa o número de objectos de malha encontrados
no recipiente 3MF, e não uma contagem de componentes topológicos desligados. Uma
face foi classificada como degenerada quando a sua área era inferior a 10⁻⁹ mm².
A estanquidade foi examinada pela correspondência das arestas orientadas, sem
fusão prévia de vértices coincidentes. Estes resultados descrevem, portanto, a
codificação geométrica dos ficheiros e devem ser interpretados em conjunto com o
resultado do fatiamento.

## D.4 Resultados

Os dados completos estão nos ficheiros CSV que acompanham este anexo:
`resultados_projectos_arquivados.csv`, `resultados_campanha_controlada.csv` e
`resultados_geometria.csv`.

### D.4.1 Série A

Tabela D.1 — Estimativas dos projectos de impressão arquivados

| Modelo | Perfil | Material | Impressora | Camada | Enchimento | Suportes | Tempo estimado | Filamento estimado | Massa estimada | Custo (36,29 €/kg) |
|---|---|---|---|---:|---|---|---:|---:|---:|---:|
| Flexy Beast | `teen_15` | PLA | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 2 h 21 min 50 s | 18 645,87 mm | 56,51 g | 2,05 € |
| UnLimbited Phoenix | `teen_15` | PLA | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 5 h 12 min 44 s | 40 756,68 mm | 123,52 g | 4,48 € |
| UnLimbited Phoenix | `teen_15` | PETG | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 5 h 51 min 52 s | 39 094,09 mm | 117,54 g | 4,27 € |
| Paraglider Hand | `teen_15` | PLA | Prusa MINI, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 2 h 32 min 11 s | 12 727,61 mm | 37,96 g | 1,38 € |

O custo é calculado a **36,29 €/kg** (preço do perfil Prusament PLA emitido pelo
PrusaSlicer), **assumido igual para ambos os fatiadores e todos os materiais**
(`custo = massa / 1000 × 36,29 €`). No Paraglider, o valor calculado (1,38 €)
coincide com o custo emitido pelo próprio PrusaSlicer, validando a taxa.

Leitura descritiva: entre os projectos arquivados, o Phoenix apresentou valores
estimados de tempo e material superiores aos do Flexy Beast para o perfil de 15
anos. Os dois projectos Phoenix (PLA e PETG) partilham modelo, impressora,
geometria, altura de camada (0,24 mm), paredes, enchimento e política de suportes,
diferindo **apenas no material** (verificado nas configurações embebidas); a sua
comparação é, por isso, um contraste de material legítimo, ainda que de um único
caso: o PETG estimou mais tempo (5 h 51 min vs 5 h 12 min) e menos massa (117,5 g
vs 123,5 g) que o PLA, coerente com as definições próprias de cada filamento e com
a ligeira diferença de densidade. Já a comparação entre modelos diferentes
(Phoenix vs Flexy) ou entre fatiadores/impressoras distintos (Paraglider vs os
casos Bambu) não é válida. O aviso de baixa aderência surgiu no Paraglider
preparado sem suportes nem aba, indicando a necessidade de rever a estratégia de
adesão antes da impressão.

### D.4.2 Série B (condição comum)

Tabela D.2 — Estimativas de preparação para impressão na condição digital comum

| Modelo | Perfil | Material | Impressora | Camada | Enchimento | Suportes | Tempo estimado | Filamento estimado | Massa estimada | Custo (36,29 €/kg) | Placas A1 |
|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|
| Flexy Beast | `child_8` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 6 h 39 min 34 s | 27 387,6 mm | 83,00 g | 3,01 € | 1 |
| Flexy Beast | `teen_15` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 9 h 51 min 52 s | 43 180,9 mm | 130,87 g | 4,75 € | 1 |
| Flexy Beast | `adult_28` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 12 h 34 min 14 s | 55 811,9 mm | 169,15 g | 6,14 € | 2 |
| Flexy Beast | `elderly_70` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 10 h 52 min 57 s | 47 602,0 mm | 144,27 g | 5,24 € | 2 |
| Paraglider Hand | `child_8` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 4 h 22 min 47 s | 16 522,2 mm | 50,07 g | 1,82 € | 1 |
| Paraglider Hand | `teen_15` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 6 h 45 min 18 s | 27 695,5 mm | 83,94 g | 3,05 € | 1 |
| Paraglider Hand | `adult_28` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 8 h 55 min 41 s | 38 449,4 mm | 116,53 g | 4,23 € | 1 |
| Paraglider Hand | `elderly_70` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 7 h 09 min 05 s | 29 627,5 mm | 89,79 g | 3,26 € | 1 |
| UnLimbited Phoenix | `child_8` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 7 h 29 min 44 s | 30 673,7 mm | 92,96 g | 3,37 € | 2 |
| UnLimbited Phoenix | `teen_15` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 8 h 30 min 45 s | 36 335,2 mm | 110,12 g | 4,00 € | 2 |
| UnLimbited Phoenix | `adult_28` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 8 h 56 min 20 s | 38 179,8 mm | 115,71 g | 4,20 € | 2 |
| UnLimbited Phoenix | `elderly_70` | Bambu PLA Basic | Bambu Lab A1, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 7 h 49 min 09 s | 32 412,0 mm | 98,23 g | 3,56 € | 2 |

Os tempos estimados variaram entre 4 h 22 min (Paraglider, `child_8`) e 12 h
34 min (Flexy Beast, `adult_28`). Nos 12 casos, o fatiador gerou trajectórias e
estimativas. Contudo, assinalou regiões suspensas nos quatro casos Flexy Beast e
no Paraglider `elderly_70`, uma consequência relevante da política comum sem
suportes. Não foram emitidos avisos nos quatro casos Phoenix. A conclusão do
fatiamento não demonstra, por si só, que a impressão física possa ser realizada
sem rever a orientação ou activar suportes. Os dados completos — tempo, filamento,
camadas, ocupação por placa e avisos — constam de
`resultados_campanha_controlada.csv`.

Duas leituras de projecto sobressaem:

1. **A exigência de preparação variou com as dimensões de entrada, e não com a
   idade isoladamente.** Na condição comum, a massa e o tempo aumentaram do perfil
   infantil para o adulto. O perfil adulto do Flexy Beast apresentou a maior massa
   estimada (169,2 g). O perfil de 70 anos produziu valores inferiores aos do
   adulto porque as suas dimensões de entrada eram menores; a idade funciona aqui
   apenas como identificador do perfil simulado.
2. **O número de placas depende da geometria, da orientação e da disposição
   automática.** Nas condições usadas pelo Bambu Studio, o Paraglider foi disposto
   numa placa, o Flexy ocupou duas placas nos dois perfis de maiores dimensões e o
   Phoenix ocupou duas placas em todos os perfis. Estes resultados apoiam o
   planeamento das sessões de fabrico, mas podem alterar-se com orientação ou
   disposição manual diferentes.

### D.4.3 Geometria — tamanho do conjunto vs tamanho da peça

A análise geométrica distingue **três noções de tamanho** que não devem ser
confundidas (detalhe em `resultados_geometria.csv`):

- **Montagem sólida (mão estendida):** a caixa envolvente do corpo único do modelo
  montado, com dedos e punho estendidos. É o *vão anatómico*.
- **Palma (peça):** a caixa envolvente da palma isolada.
- **Placa disposta:** a área ocupada pelas peças efectivamente colocadas na placa.

Achado central: **na orientação analisada, uma dimensão da caixa envolvente do
modelo montado ultrapassa a dimensão nominal da placa.** O corpo único do Flexy
atinge 259 mm (teen), 296 mm (adult) e 273 mm (elderly), enquanto os conjuntos
Paraglider medem 331–372 mm de comprimento. O ensaio não incluiu uma procura
exaustiva de rotações ou de disposições alternativas. Ainda assim, os resultados
justificam a exportação segmentada disponibilizada pela plataforma e mostram que
a dimensão da montagem estendida não deve ser confundida com a ocupação efectiva
das peças dispostas na placa.

Sobre integridade de malha: os corpos do Flexy são estanques e sem faces
degeneradas; o Paraglider apresenta faces degeneradas residuais; a palma do
Phoenix apresenta pequenas arestas de fronteira (não totalmente estanque). Estas
são propriedades **geométricas** dos ficheiros — relevantes para robustez de
fatiamento, **não** para desempenho estrutural.

**Sobre a leitura estrutural dos parâmetros.** Importa separar três coisas
distintas. (i) As *estimativas do fatiador* (tempo, filamento, massa) não medem
resistência. (ii) A *integridade de malha* é geométrica, não mecânica. (iii) Os
*parâmetros de impressão* — número de paredes, densidade e padrão de enchimento e
material — são, esses sim, determinantes reconhecidos do comportamento mecânico de
peças FFF: a literatura mostra que, a igual geometria, mais paredes e maior
enchimento aumentam a rigidez e a resistência. Quanto ao material, e comparado com
o PLA, o PETG é mais tenaz, mais dúctil e mais resistente ao impacto e à fadiga, e
suporta temperaturas mais altas (maior temperatura de transição vítrea); o PLA, em
contrapartida, é mais rígido e tem maior resistência à tracção pura. Para uma
prótese de mão — sujeita a flexão repetida, a impactos e ao calor do corpo — são a
tenacidade, a resistência à fadiga e a resistência térmica que mais relevam, pelo
que, **nesse sentido funcional, o PETG é o material mais resistente e durável** (uma
leitura qualitativa, não um valor medido). É, por isso, legítimo afirmar de forma
**qualitativa e relativa** que a configuração da Série B (2 paredes, 15% de
enchimento) é de *serviço ligeiro* e que aumentar paredes ou enchimento aumentaria
a robustez esperada. O que **não** é legítimo, sem ensaio físico, é
atribuir **valores absolutos** de resistência, rigidez ou vida em fadiga, nem
certificar que uma peça concreta suporta uma carga ou um número de ciclos de
preensão determinados: isso depende do material, da orientação das camadas
(anisotropia), da adesão entre camadas, de eventuais defeitos e das condições
reais de carga, que só um ensaio mecânico mede.

### D.4.4 Comparação entre entrada, malha e peça física

A comparação dimensional foi preparada a partir dos mesmos quatro perfis. Em
cada caso, o valor `palm_breadth_mm` foi lido do ficheiro `params.json` aplicado
pela plataforma e a extensão total no eixo X foi medida directamente na malha
3MF isolada da palma. A futura medição da peça física deverá reproduzir essa
extensão total, com a peça orientada segundo os eixos do ficheiro, usando os
mesmos extremos geométricos.

Tabela D.3 — Preparação da comparação dimensional da palma

| Modelo | Perfil | Ponto medido | Entrada | Malha | Peça física | Desvio malha–peça |
|---|---|---|---:|---:|---:|---:|
| Flexy Beast | `child_8` | Largura metacarpal de entrada; extensão total X da palma | 64,0 mm | 97,385 mm | — | — |
| Flexy Beast | `teen_15` | Largura metacarpal de entrada; extensão total X da palma | 78,0 mm | 117,144 mm | — | — |
| Flexy Beast | `adult_28` | Largura metacarpal de entrada; extensão total X da palma | 90,0 mm | 134,081 mm | — | — |
| Flexy Beast | `elderly_70` | Largura metacarpal de entrada; extensão total X da palma | 84,0 mm | 125,612 mm | — | — |
| Paraglider Hand | `child_8` | Largura metacarpal de entrada; extensão total X da palma | 63,0 mm | 76,513 mm | — | — |
| Paraglider Hand | `teen_15` | Largura metacarpal de entrada; extensão total X da palma | 78,0 mm | 94,730 mm | — | — |
| Paraglider Hand | `adult_28` | Largura metacarpal de entrada; extensão total X da palma | 90,0 mm | 109,304 mm | — | — |
| Paraglider Hand | `elderly_70` | Largura metacarpal de entrada; extensão total X da palma | 84,0 mm | 102,017 mm | — | — |
| UnLimbited Phoenix | `child_8` | Largura metacarpal de entrada; extensão total X da palma | 82,0 mm | 82,165 mm | — | — |
| UnLimbited Phoenix | `teen_15` | Largura metacarpal de entrada; extensão total X da palma | 88,0 mm | 88,177 mm | — | — |
| UnLimbited Phoenix | `adult_28` | Largura metacarpal de entrada; extensão total X da palma | 90,0 mm | 90,181 mm | — | — |
| UnLimbited Phoenix | `elderly_70` | Largura metacarpal de entrada; extensão total X da palma | 84,0 mm | 84,169 mm | — | — |

A Tabela D.3 resume o eixo X, por ser o único eixo associado a um parâmetro
activo nos três modelos. A folha completa
`tabela_comparacao_dimensional.csv` contém 36 linhas de medição: extensões X, Y e
Z para as doze combinações modelo–perfil. Nos casos Paraglider, os valores
`palm_length_mm` e `palm_thickness_mm` são conservados como contexto do perfil,
mas não controlam isoladamente as extensões Y e Z; no Flexy Beast e no Phoenix
não existe, nestas configurações, um parâmetro de entrada correspondente a esses
dois eixos. Esta diferença encontra-se identificada no campo
`estado_parametro` da folha.

As colunas «Entrada» e «Malha» não representam, em todos os modelos, o mesmo
limite geométrico. No Flexy Beast e no Paraglider, a medida antropométrica alimenta
uma regra de escala aplicada a uma geometria-base cuja extensão total inclui abas,
interfaces e margens para montagem. No Phoenix, a largura de referência coincide
aproximadamente com a extensão X da palma-base, pelo que os valores são próximos.
Assim, a diferença entre entrada e malha descreve a transformação projectual e não
constitui erro. O desvio dimensional será calculado apenas entre a malha e a peça
física, depois de ambas serem medidas no mesmo referencial:

```text
desvio malha–peça = medida da peça física − medida da malha
desvio percentual = 100 × (medida da peça física − medida da malha) / medida da malha
```

### D.4.5 Registo fotográfico dos protótipos

As Figuras 8.1 a 8.3 do manuscrito reúnem o registo fotográfico das peças produzidas: componentes separados e em montagem parcial, séries dimensionais de segmentos Paraglider Hand e Flexy Beast, e sete vistas de uma UnLimbited Phoenix montada para o perfil simulado de 15 anos. As fotografias originais são conservadas na pasta `figuras/` com o prefixo `teste-impressao-`; os painéis integrados no documento foram compostos a partir desses ficheiros, sem alteração do conteúdo visual. Três fotografias das séries dimensionais foram apenas rodadas 90° para permitir a leitura correcta da orientação e das identificações manuscritas.

Este registo confirma a existência material dos componentes fotografados e permite observar diferenças de escala, estados de montagem e relações visuais entre peças. Como não inclui escala métrica comum, pontos de medição assinalados, repetições controladas ou aplicação de carga, não é usado para calcular desvios dimensionais nem para inferir resistência, conforto, adequação anatómica ou desempenho funcional. A medição física mantém-se dependente do protocolo definido na Secção D.4.4.

## D.5 Compatibilidade com orientações de dimensionamento

Os ficheiros locais de dimensionamento permitem duas comparações delimitadas. No
Flexy Beast, a plataforma usa a fórmula de escala herdada da família Cyborg Beast,
`(palm_breadth_mm + 5) / 55`. O gráfico etário do Cyborg Beast indica 126% aos 8
anos e 133% aos 15 anos; as larguras introduzidas nos perfis Flexy originaram,
respectivamente, 125,5% e 150,9%. A proximidade do primeiro caso é apenas
contextual. A diferença no segundo mostra que uma regra baseada numa medida da
mão e uma regressão baseada somente na idade não são equivalentes.

No Phoenix, a regra `palm_breadth_mm / 82 × 100`, limitada a 100%–160%, produziu
as seguintes escalas:

| Perfil | Largura introduzida | Escala calculada | Gama da folha Phoenix |
|---|---:|---:|---:|
| `child_8` | 82 mm | 100,0% | 100%–165% |
| `teen_15` | 88 mm | 107,3% | 100%–165% |
| `adult_28` | 90 mm | 109,8% | 100%–165% |
| `elderly_70` | 84 mm | 102,4% | 100%–165% |

Os quatro valores situam-se na gama de factores da folha Phoenix. A largura-base
de 65 mm indicada nessa folha não foi comparada directamente com os 82 mm da
plataforma, porque os documentos não demonstram que os pontos de medição sejam
equivalentes. Não existe uma tabela local específica para o Paraglider. O detalhe
e os limites destas comparações constam de
`avaliacao_compatibilidade_dimensionamento.md`. Os resultados mostram
compatibilidade com orientações de escala; não demonstram adequação anatómica
individual nem funcionamento.

## D.6 Limites de comparabilidade

- **Estimativa, não medição** (ver D.2): não citar como valores físicos.
- **A Série A não permite comparação directa entre modelos/máquinas:** mistura
  fatiadores (Bambu/Prusa), impressoras (A1/MINI), alturas de camada (0,24/0,20 mm)
  e política de suportes. O Paraglider, em particular, não é comparável com os
  casos Bambu. **Excepção:** os dois projectos Phoenix (PLA e PETG) partilham tudo
  excepto o material, pelo que constituem um contraste de material válido.
- **Série A ≠ Série B:** condições de ensaio distintas (a Série A com suportes
  e 0,24 mm; a B sem suportes e 0,20 mm).
- **Só a Série B permite comparação entre modelos**, por partilharem condição.
- **Assimetria de exportação:** a plataforma exporta Flexy e Paraglider também como
  corpo montado único, mas o Phoenix apenas em peças soltas (não há 3MF de montagem
  por perfil, excepto `teen_15`). A comparação da Série B foi feita, de forma
  homogénea, sobre os **conjuntos de peças** de cada modelo.

## D.7 Campos que não puderam ser obtidos

- **Custo monetário directo do Bambu Studio:** não emitido pelo programa nas
  condições usadas. O custo apresentado nas Tabelas D.1 e D.2 foi por isso
  **calculado** a partir da massa estimada e de uma taxa única de **36,29 €/kg**
  (preço do perfil Prusament PLA do PrusaSlicer), assumida igual para ambos os
  fatiadores e todos os materiais; para o Paraglider coincide com o valor emitido
  pelo próprio PrusaSlicer (1,38 €). Não é, pois, um custo emitido pelo Bambu, mas
  uma estimativa derivada com pressuposto declarado.
- **Contagem de camadas do caso PrusaSlicer:** não reportada no cabeçalho de
  G-code no mesmo formato do Bambu; deixada em branco.
- **Montagem sólida do Phoenix por perfil:** inexistente na exportação da
  plataforma (só peças soltas), pelo que só está disponível para teen_15.
- **Medições dimensionais físicas:** ainda não incorporadas nos resultados. O
  protocolo e a folha de três leituras por ponto foram preparados, mas as colunas
  permanecem vazias até as peças serem medidas com paquímetro.
- **Verificação de montagem e articulação:** o protocolo e a folha de registo
  foram preparados, mas não existem ainda observações preenchidas que permitam
  apresentar resultados de movimento, fecho ou retorno.
- **Medições mecânicas ou de ajuste ao utilizador:** não realizadas; exigiriam
  procedimentos e condições diferentes dos ensaios aqui descritos.

## D.8 O que pode e não pode ser afirmado na dissertação

**Pode afirmar-se:**

- Que os ficheiros foram aceites pelos fatiadores e permitiram gerar trajectórias
  e estimativas em 4/4 projectos arquivados e 12/12 casos controlados.
- Que a **exigência de preparação** (material, tempo, número de placas) foi
  **estimada** sob condições declaradas e variou com o modelo e com as dimensões
  dos perfis simulados.
- Que, na orientação analisada, uma dimensão da caixa envolvente de vários modelos
  montados excedeu a dimensão nominal da placa, apoiando a decisão de disponibilizar
  os componentes segmentados.
- Que a Série B permite comparar os valores estimados dos modelos sob uma
  condição digital comum.
- Que o par Phoenix PLA vs PETG (Série A) constitui um contraste de material
  controlado, por partilhar modelo, impressora, geometria, camada e processo.
- Que, de forma **qualitativa e relativa**, os parâmetros de impressão informam o
  comportamento mecânico esperado: mais paredes ou mais enchimento aumentam a
  robustez; o PETG é funcionalmente mais resistente e durável do que o PLA (mais
  tenaz e mais resistente a impacto, fadiga e calor), sendo o PLA mais rígido; e a
  configuração da Série B (2 paredes, 15%) é de serviço ligeiro — tudo sem
  quantificar valores absolutos.

**Não pode afirmar-se:**

- Que estes valores estimados são **medições reais** de impressões, ou que medem
  **valores absolutos** de resistência, rigidez, durabilidade ou ajuste anatómico.
  (A leitura estrutural admissível é apenas qualitativa e relativa — ver acima e
  o parágrafo «Sobre a leitura estrutural dos parâmetros» em D.4.3; valores
  absolutos exigem ensaio mecânico físico.)
- Que os casos da **Série A** são comparáveis entre modelos, fatiadores ou
  impressoras diferentes (a única comparação válida na Série A é o par Phoenix
  PLA vs PETG, que só difere no material).
- Que a **integridade de malha** implica qualidade mecânica da peça.
- Que o fatiamento concluído demonstra sucesso de impressão, montagem, adequação
  funcional ou utilização segura.
- Que os custos são preços de mercado reais: assentam numa taxa única assumida de
  36,29 €/kg (o PETG usa a mesma taxa do PLA); um preço real distinto por
  fornecedor ou no tempo altera-os proporcionalmente.

## D.9 Registo fotográfico dos protótipos impressos

As imagens seguintes documentam **impressões físicas reais** dos modelos, obtidas
na impressora Bambu Lab A1. Complementam as estimativas digitais das secções
anteriores como **evidência visual e qualitativa** da preparação e do fabrico:
mostram que os ficheiros gerados pela plataforma foram impressos, montados e
articulados. Não acrescentam medições quantitativas — as medições dimensionais e
a verificação de montagem seguem os protocolos próprios (D.4.4 e anexos
associados) e permanecem por preencher até serem executadas sobre estes exemplares.

### D.9.1 Peças no processo de impressão (placa Bambu Lab A1)

![Segmentos de dedos do Flexy Beast na placa da Bambu Lab A1](figuras/teste-impressao-3d-dedos-flexy-beast.jpg)
*Figura D.1 — Segmentos de dedos (falanges) do Flexy Beast dispostos na placa da Bambu Lab A1, no fim da impressão.*

![Falanges sobre a placa texturada da A1](figuras/teste-impressao-09201343.jpg)
*Figura D.2 — Falanges (base e ponta) sobre a placa texturada da A1, antes da remoção.*

![Conjunto de dedos na placa da A1](figuras/teste-impressao-09201338.jpg)
*Figura D.3 — Conjunto de dedos ainda na placa da A1.*

![Conjunto de dedos na placa da A1, tomada alternativa](figuras/teste-impressao-09201340.jpg)
*Figura D.4 — O mesmo conjunto, tomada alternativa.*

### D.9.2 Série dimensional física — o mesmo componente aos quatro perfis

Estas imagens são a contraparte física do escalonamento antropométrico discutido
em D.4.2: o mesmo dedo, impresso aos quatro perfis (8, 15, 28 e 70 anos),
cresce proporcionalmente com a dimensão de entrada.

![Dedos articulados do Flexy Beast aos quatro perfis](figuras/teste-impressao-dedos-flexy-beast-v1.jpg)
*Figura D.5 — Dedos articulados do Flexy Beast impressos aos quatro perfis (8, 15, 28 e 70 anos).*

![Dedos do Flexy Beast aos quatro perfis, tomada alternativa](figuras/teste-impressao-dedos-flexy-beast-v2.jpg)
*Figura D.6 — O mesmo conjunto, tomada alternativa.*

![Dedos do Paraglider Hand aos quatro perfis](figuras/teste-impressao-dedos-paraglider-hand-v1.jpg)
*Figura D.7 — Dedos do Paraglider Hand impressos aos quatro perfis.*

![Falanges distais aos quatro perfis, rotuladas por idade](figuras/teste-impressao-12185320.jpg)
*Figura D.8 — Falanges distais aos quatro perfis, rotuladas por idade.*

![Dedos articulados base+ponta aos quatro perfis](figuras/teste-impressao-12185529.jpg)
*Figura D.9 — Dedos articulados (base + ponta) aos quatro perfis, mostrando o crescimento proporcional.*

![Dedos articulados aos quatro perfis, tomada alternativa](figuras/teste-impressao-12185532.jpg)
*Figura D.10 — O mesmo conjunto, tomada alternativa.*

### D.9.3 Componentes soltos

![Palma impressa, vista dorsal, com padrão de enchimento visível](figuras/teste-impressao-08214912.jpg)
*Figura D.11 — Palma impressa (vista dorsal): visíveis os canais dos dedos e o padrão de enchimento — o mesmo tipo de parâmetro (paredes/enchimento) cuja leitura estrutural qualitativa se discute em D.4.3.*

![Componentes do antebraço/punho impressos](figuras/teste-impressao-08214702.jpg)
*Figura D.12 — Componentes do antebraço/punho (gauntlet), em três exemplares.*

### D.9.4 Mão UnLimbited Phoenix montada (perfil de 15 anos)

![Mão Phoenix montada](figuras/teste-impressao-phoenix-15-anos-13221108.jpg)
*Figura D.13 — Mão UnLimbited Phoenix montada (perfil de 15 anos): palma, dedos, polegar e punho articulados.*

![Mão Phoenix montada, segunda vista](figuras/teste-impressao-phoenix-15-anos-13221111.jpg)
*Figura D.14 — A mesma mão, segunda vista.*

![Mão Phoenix montada com polegar em oposição](figuras/teste-impressao-phoenix-15-anos-13221117.jpg)
*Figura D.15 — A mesma mão, com o polegar em oposição.*

![Mão Phoenix, vista do punho/antebraço](figuras/teste-impressao-phoenix-15-anos-13221145.jpg)
*Figura D.16 — A mesma mão, vista do lado do punho/antebraço.*

![Mão Phoenix montada, vista dorsal segura na mão](figuras/teste-impressao-phoenix-15anos-0008.jpg)
*Figura D.17 — Mão Phoenix montada, vista dorsal.*

![Pormenor da articulação do polegar e charneira dos dedos](figuras/teste-impressao-phoenix-15anos-0010.jpg)
*Figura D.18 — Pormenor da articulação do polegar e da charneira dos dedos.*

![Vista palmar da mão Phoenix com enchimento visível através da palma](figuras/teste-impressao-phoenix-15anos-0012.jpg)
*Figura D.19 — Vista palmar: o padrão de enchimento é visível através da palma, ilustrando o parâmetro de enchimento usado.*

> **Nota sobre orientação das figuras.** As imagens foram integradas na orientação
> em que os seus pixéis se apresentam (todas verticais/corretas na revisão feita).
> Se alguma precisar de ser rodada na versão final, indique-se o ficheiro e o
> sentido; a rotação é aplicada ao ficheiro em `figuras/` sem alterar a referência.
