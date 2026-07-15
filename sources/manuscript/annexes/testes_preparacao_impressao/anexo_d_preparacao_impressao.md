# Anexo D — Preparação para fabrico e verificação dos protótipos

## D.1 Finalidade

Este anexo reúne evidência verificável sobre a **preparação para impressão** das
mãos protésicas paramétricas geradas pela plataforma HandFab, no contexto de uma
dissertação de **Design e Desenvolvimento de Produto**. O objectivo não é
demonstrar desempenho mecânico nem validar uma impressão física, mas sim
caracterizar, sob condições documentadas, as **exigências de fabrico digital** que o
sistema paramétrico coloca a jusante do projecto: quanto material, quanto tempo,
quantas placas de impressão e que condições de preparação decorrem de cada modelo
e de cada dimensão antropométrica. O anexo apresenta também a comparação entre
entrada, malha e peça física e prepara a observação da montagem e articulação. A
comparação dimensional inclui as palmas em PLA e PETG; a montagem e a articulação
permanecem dependentes de observações sistemáticas nos protótipos correspondentes.

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

Os valores de tempo, comprimento de filamento, massa, volume e custo deste anexo
são **estimativas produzidas por programas de preparação para impressão 3D** (Bambu Studio e
PrusaSlicer). A Secção D.4.4 apresenta, em separado, **medições físicas** das
extensões X, Y e Z das palmas produzidas em PLA e PETG, realizadas à temperatura
ambiente e comparadas com as dimensões das malhas correspondentes.

Em consequência, e de forma explícita:

- **As estimativas de preparação não são medições de impressões reais.** Uma impressão física difere por
  factores de máquina, humidade do filamento, calibração e temperatura.
- **Não são indicadores de desempenho estrutural.** O tempo ou a massa estimados
  nada dizem sobre a resistência da peça.
- **A verificação de malha é geométrica, não mecânica.** «Estanque/manifold» e
  «faces degeneradas» descrevem a integridade do ficheiro 3D; não são medida da
  robustez do objecto impresso.
- **As estimativas dependem da versão e do perfil.** Trocar de versão do programa,
  de perfil de processo ou de firmware altera os números.

As estimativas de tempo, material, volume e custo devem, pois, ser lidas como
**indicadores comparativos de exigência de preparação**, e não como propriedades
físicas do produto final. Esta restrição não abrange os valores dimensionais da
Secção D.4.4, que correspondem a medições das palmas impressas.

## D.3 Variáveis, controlos e materiais

Foram conduzidas duas séries de ensaios complementares. A documentação técnica
associada ao anexo reúne as versões, as condições de preparação e os resultados
completos no material suplementar da dissertação.

**Programas:** Bambu Studio `01.10.02.76`; PrusaSlicer `2.8.1`.
Análise geométrica em Python 3.12 / NumPy 2.4 (sem preparação para impressão).

### D.3.1 Série A — projectos de preparação digital para impressão 3D com configuração analisada

Quatro projectos de preparação digital para impressão 3D foram **processados com
a configuração própria de cada caso**, mantendo a disposição e a orientação.
Os projectos conservavam a geometria, as definições e a disposição na placa, mas
não os resultados do processamento; as trajectórias e as estimativas tiveram de
ser recalculadas.

| # | Modelo | Idade | Material | Programa / Impressora |
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
de ensaio (`child_8`, `teen_15`, `adult_28`, `elderly_70`), processados sob **uma única
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

A orientação de cada peça exportada foi mantida; o programa apenas dispôs as peças
na placa, criando automaticamente uma segunda placa A1 quando não cabiam numa.
Esta série de ensaios constitui uma **comparação digital controlada da exigência de preparação** —
**não** representa uma impressão física nem uma recomendação de imprimibilidade.

Na análise geométrica, `n_corpos` designa o número de objectos de malha encontrados
no recipiente 3MF, e não uma contagem de componentes topológicos desligados. Uma
face foi classificada como degenerada quando a sua área era inferior a 10⁻⁹ mm².
A estanquidade foi examinada pela correspondência das arestas orientadas, sem
fusão prévia de vértices coincidentes. Estes resultados descrevem, portanto, a
codificação geométrica dos ficheiros e devem ser interpretados em conjunto com o
resultado da preparação para impressão.

## D.4 Resultados

Os resultados quantitativos completos e os registos geométricos encontram-se no
material suplementar associado a este anexo.

### D.4.1 Série A

Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada

| Modelo | Perfil | Material | Impressora | Camada | Enchimento | Suportes | Tempo estimado | Filamento estimado | Massa estimada | Custo (36,29 €/kg) |
|---|---|---|---|---:|---|---|---:|---:|---:|---:|
| Flexy Beast | `teen_15` | PLA | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 2 h 21 min 50 s | 18 645,87 mm | 56,51 g | 2,05 € |
| UnLimbited Phoenix | `teen_15` | PLA | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 5 h 12 min 44 s | 40 756,68 mm | 123,52 g | 4,48 € |
| UnLimbited Phoenix | `teen_15` | PETG | Bambu Lab A1, bico 0,4 mm | 0,24 mm | 15%, grelha | Árvore orgânica | 5 h 51 min 52 s | 39 094,09 mm | 117,54 g | 4,27 € |
| Paraglider Hand | `teen_15` | PLA | Prusa MINI, bico 0,4 mm | 0,20 mm | 15%, grelha | Não | 2 h 32 min 11 s | 12 727,61 mm | 37,96 g | 1,38 € |

O custo é calculado a **36,29 €/kg** (preço do perfil Prusament PLA emitido pelo
PrusaSlicer), **assumido igual para ambos os programas e todos os materiais**
(`custo = massa / 1000 × 36,29 €`). No Paraglider, o valor calculado (1,38 €)
coincide com o custo emitido pelo próprio PrusaSlicer, validando a taxa.

Leitura descritiva: entre os projectos com configuração analisada, o Phoenix apresentou valores
estimados de tempo e material superiores aos do Flexy Beast para o perfil de 15
anos. Os dois projectos Phoenix (PLA e PETG) partilham modelo, impressora,
geometria, altura de camada (0,24 mm), paredes, enchimento e política de suportes,
diferindo **apenas no material** (verificado nas configurações embebidas); a sua
comparação é, por isso, um contraste de material legítimo, ainda que de um único
caso: o PETG estimou mais tempo (5 h 51 min vs 5 h 12 min) e menos massa (117,5 g
vs 123,5 g) que o PLA, coerente com as definições próprias de cada filamento e com
a ligeira diferença de densidade. Já a comparação entre modelos diferentes
(Phoenix vs Flexy) ou entre programas/equipamentos distintos (Paraglider vs os
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
34 min (Flexy Beast, `adult_28`). Nos 12 casos, o programa gerou trajectórias e
estimativas. Contudo, assinalou regiões suspensas nos quatro casos Flexy Beast e
no Paraglider `elderly_70`, uma consequência relevante da política comum sem
suportes. Não foram emitidos avisos nos quatro casos Phoenix. A conclusão do
processamento não demonstra, por si só, que a impressão física possa ser realizada
sem rever a orientação ou activar suportes. Os dados completos — tempo, filamento,
camadas, ocupação por placa e avisos — constam do registo suplementar da Série B.

Duas leituras de projecto sobressaem:

1. **A exigência de preparação variou com as dimensões de entrada, e não com a
   idade isoladamente.** Na condição comum, a massa e o tempo aumentaram do perfil
   infantil para o adulto. O perfil adulto do Flexy Beast apresentou a maior massa
   estimada (169,2 g). O perfil de 70 anos produziu valores inferiores aos do
   adulto porque as suas dimensões de entrada eram menores; a idade funciona aqui
   apenas como identificador do perfil de ensaio.
2. **O número de placas depende da geometria, da orientação e da disposição
   automática.** Nas condições usadas pelo Bambu Studio, o Paraglider foi disposto
   numa placa, o Flexy ocupou duas placas nos dois perfis de maiores dimensões e o
   Phoenix ocupou duas placas em todos os perfis. Estes resultados apoiam o
   planeamento das sessões de fabrico, mas podem alterar-se com orientação ou
   disposição manual diferentes.

### D.4.3 Geometria — tamanho do conjunto vs tamanho da peça

A análise geométrica distingue **três noções de tamanho** que não devem ser
confundidas; os valores completos constam do registo geométrico suplementar:

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
preparação para impressão, **não** para desempenho estrutural.

**Sobre a leitura estrutural dos parâmetros.** Importa separar três coisas
distintas. (i) As *estimativas do programa* (tempo, filamento, massa) não medem
resistência. (ii) A *integridade de malha* é geométrica, não mecânica. (iii) Os
*parâmetros de impressão* e o material influenciam o comportamento mecânico das
peças FFF, mas os resultados da literatura não sustentam uma hierarquia geral
entre PLA e PETG. Hsueh et al. (2021) observaram, nas condições ensaiadas, maior
módulo de Young e resistência no PLA e maior resistência à deformação térmica no
PETG. Martins et al. (2024) registaram maior deformação até à rotura no PETG,
correspondente a um comportamento mais dúctil, mas maior resistência à fadiga no
PLA nas condições específicas do respectivo ensaio. Por conseguinte, o PETG pode
ser contextualizado como mais dúctil e, nas condições estudadas, mais resistente à
deformação térmica, mas não como material universalmente «mais resistente e
durável». Nesta dissertação, a observação física limita-se a que as peças em PETG
foram impressas, manipuladas e medidas sem dificuldades impeditivas do procedimento.
Não foi realizada uma comparação mecânica entre materiais. Também não podem ser
atribuídos valores absolutos de resistência, rigidez ou vida em fadiga, nem pode
certificar-se que uma peça concreta suporta uma carga ou um número de ciclos de
preensão determinados: isso depende do grau do material, da orientação das camadas,
da adesão entre camadas, de eventuais defeitos, dos restantes parâmetros de
impressão e das condições reais de carga, que só um ensaio mecânico mede.

### D.4.4 Comparação entre entrada, malha e peça física

A comparação dimensional incidiu nas doze combinações entre três modelos e quatro
perfis de ensaio. Para cada combinação, as extensões X, Y e Z da malha isolada da
palma foram comparadas com as dimensões das peças produzidas em PLA e PETG. As
peças encontravam-se à temperatura ambiente. Cada valor físico corresponde a uma
medição registada no eixo e material indicados, perfazendo 72 comparações: 36 em
PLA e 36 em PETG.

Tabela D.3 — Comparação dimensional da palma no eixo X em PLA e PETG

| Modelo | Perfil etário | Malha X | PLA X | Desvio PLA | PETG X | Desvio PETG |
|---|---|---:|---:|---:|---:|---:|
| Flexy Beast | 8 anos | 97,385 mm | 97,101 mm | −0,284 mm | 97,024 mm | −0,361 mm |
| Flexy Beast | 15 anos | 117,144 mm | 116,798 mm | −0,346 mm | 116,688 mm | −0,456 mm |
| Flexy Beast | 28 anos | 134,081 mm | 133,690 mm | −0,391 mm | 133,554 mm | −0,527 mm |
| Flexy Beast | 70 anos | 125,612 mm | 125,214 mm | −0,398 mm | 125,091 mm | −0,521 mm |
| Paraglider Hand | 8 anos | 76,513 mm | 76,277 mm | −0,236 mm | 76,204 mm | −0,309 mm |
| Paraglider Hand | 15 anos | 94,730 mm | 94,431 mm | −0,299 mm | 94,377 mm | −0,353 mm |
| Paraglider Hand | 28 anos | 109,304 mm | 108,972 mm | −0,332 mm | 108,841 mm | −0,463 mm |
| Paraglider Hand | 70 anos | 102,017 mm | 101,690 mm | −0,327 mm | 101,593 mm | −0,424 mm |
| UnLimbited Phoenix | 8 anos | 82,165 mm | 81,940 mm | −0,225 mm | 81,839 mm | −0,326 mm |
| UnLimbited Phoenix | 15 anos | 88,177 mm | 87,908 mm | −0,269 mm | 87,807 mm | −0,370 mm |
| UnLimbited Phoenix | 28 anos | 90,181 mm | 89,914 mm | −0,267 mm | 89,832 mm | −0,349 mm |
| UnLimbited Phoenix | 70 anos | 84,169 mm | 83,929 mm | −0,240 mm | 83,831 mm | −0,338 mm |

A Tabela D.3 resume o eixo X; a folha suplementar de comparação dimensional
conserva as 72 linhas correspondentes aos três eixos. Em todas as medições, a
dimensão física ficou abaixo da extensão da malha. Em PLA, os desvios percentuais
variaram entre −0,321% e −0,274%; em PETG, variaram entre −0,425% e −0,369%.
Estes intervalos descrevem os exemplares medidos e não demonstram uma taxa geral
de contracção dos materiais.

Nos casos Paraglider, os valores `palm_length_mm` e `palm_thickness_mm` são
conservados como contexto do perfil, mas não controlam isoladamente as extensões Y
e Z; no Flexy Beast e no Phoenix não existe, nestas configurações, um parâmetro de
entrada correspondente a esses dois eixos. Esta diferença encontra-se identificada
no campo `estado_parametro` da folha suplementar.

As colunas «Entrada» e «Malha» não representam, em todos os modelos, o mesmo
limite geométrico. No Flexy Beast e no Paraglider, a medida antropométrica alimenta
uma regra de escala aplicada a uma geometria-base cuja extensão total inclui abas,
interfaces e margens para montagem. No Phoenix, a largura de referência coincide
aproximadamente com a extensão X da palma-base, pelo que os valores são próximos.
Assim, a diferença entre entrada e malha descreve a transformação projectual e não
constitui erro. O desvio dimensional foi calculado entre a malha e a peça física,
medidas no mesmo referencial:

```text
desvio malha–peça = medida da peça física − medida da malha
desvio percentual = 100 × (medida da peça física − medida da malha) / medida da malha
```

Como existe apenas um valor registado por eixo e por peça, não são calculadas a
média entre repetições, a amplitude ou a incerteza de medição. Esta limitação é
assumida na interpretação descritiva. Uma eventual caracterização metrológica
futura exigiria o reposicionamento do paquímetro e leituras independentes, mas não
é necessária para a comparação apresentada nesta dissertação.

### D.4.5 Registo fotográfico dos protótipos

As Figuras 8.1 a 8.3 do manuscrito reúnem o registo fotográfico das peças produzidas: componentes separados e em montagem parcial, séries dimensionais de segmentos Paraglider Hand e Flexy Beast, e sete vistas de uma UnLimbited Phoenix montada para o perfil de ensaio de 15 anos. Os originais integram o material suplementar; os painéis apresentados foram compostos sem alteração do conteúdo visual. Três fotografias das séries dimensionais foram apenas rodadas 90° para permitir a leitura correcta da orientação e das identificações manuscritas.

Este registo confirma a existência material dos componentes fotografados e permite observar diferenças de escala, estados de montagem e relações visuais entre peças. Como não inclui escala métrica comum, pontos de medição assinalados, repetições controladas ou aplicação de carga, as fotografias não são usadas para calcular os desvios dimensionais nem para inferir resistência, conforto, adequação anatómica ou desempenho funcional. Os desvios apresentados na Secção D.4.4 resultam dos valores medidos nas peças, e não da interpretação das imagens.

## D.5 Compatibilidade com orientações de dimensionamento

Os referenciais de dimensionamento disponíveis permitem duas comparações delimitadas. No
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
equivalentes. Não existe uma tabela específica para o Paraglider. O detalhe e os
limites destas comparações constam da nota técnica suplementar de compatibilidade
dimensional. Os resultados mostram
compatibilidade com orientações de escala; não demonstram adequação anatómica
individual nem funcionamento.

## D.6 Limites de comparabilidade

- **Estimativas de preparação, não medições físicas** (ver D.2): os valores de tempo, filamento, massa, volume e custo não devem ser citados como propriedades medidas nas impressões.
- **A Série A não permite comparação directa entre modelos/máquinas:** mistura
  programas (Bambu Studio/PrusaSlicer), impressoras (A1/MINI), alturas de camada (0,24/0,20 mm)
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
  programas e todos os materiais; para o Paraglider coincide com o valor emitido
  pelo próprio PrusaSlicer (1,38 €). Não é, pois, um custo emitido pelo Bambu, mas
  uma estimativa derivada com pressuposto declarado.
- **Contagem de camadas do caso PrusaSlicer:** não reportada no cabeçalho de
  G-code no mesmo formato do Bambu; deixada em branco.
- **Montagem sólida do Phoenix por perfil:** inexistente na exportação da
  plataforma (só peças soltas), pelo que só está disponível para teen_15.
- **Repetições das medições dimensionais:** foi incorporado um valor por eixo e
  por palma em PLA e PETG. Não foram registadas três leituras independentes por
  ponto, pelo que não se calculam amplitude entre repetições nem incerteza de
  reposicionamento do paquímetro.
- **Verificação de montagem e articulação:** o protocolo e a folha de registo
  foram preparados, mas não existem ainda observações preenchidas que permitam
  apresentar resultados de movimento, fecho ou retorno.
- **Medições mecânicas ou de ajuste ao utilizador:** não realizadas; exigiriam
  procedimentos e condições diferentes dos ensaios aqui descritos.

## D.8 O que pode e não pode ser afirmado na dissertação

**Pode afirmar-se:**

- Que os ficheiros foram aceites pelos programas de preparação e permitiram gerar trajectórias
  e estimativas em 4/4 projectos com configuração analisada e 12/12 casos controlados.
- Que a **exigência de preparação** (material, tempo, número de placas) foi
  **estimada** sob condições declaradas e variou com o modelo e com as dimensões
  dos perfis de ensaio.
- Que, na orientação analisada, uma dimensão da caixa envolvente de vários modelos
  montados excedeu a dimensão nominal da placa, apoiando a decisão de disponibilizar
  os componentes segmentados.
- Que a Série B permite comparar os valores estimados dos modelos sob uma
  condição digital comum.
- Que o par Phoenix PLA vs PETG (Série A) constitui um contraste de material
  controlado, por partilhar modelo, impressora, geometria, camada e processo.
- Que foram comparadas 72 dimensões físicas das palmas em PLA e PETG com as
  extensões X/Y/Z das respectivas malhas e que, nos exemplares medidos, todos os
  desvios foram negativos e inferiores a 0,5% em valor absoluto.
- Que as peças em PETG foram impressas, manipuladas e medidas sem dificuldades
  impeditivas do procedimento. Como enquadramento da literatura, o PETG apresentou
  maior resistência à deformação térmica no estudo de Hsueh et al. (2021) e maior
  ductilidade no estudo de Martins et al. (2024); estas propriedades não constituem
  resultados experimentais desta dissertação.

**Não pode afirmar-se:**

- Que as estimativas de tempo, filamento, massa, volume e custo são **medições
  reais** das impressões, ou que as medições dimensionais demonstram **valores
  absolutos** de resistência, rigidez, durabilidade ou ajuste anatómico.
  (A leitura estrutural admissível é apenas qualitativa e relativa — ver acima e
  o parágrafo «Sobre a leitura estrutural dos parâmetros» em D.4.3; valores
  absolutos exigem ensaio mecânico físico.)
- Que o PETG é, de forma geral, mais resistente, mais durável ou mais resistente à
  fadiga do que o PLA; essas comparações dependem do tipo de solicitação e das
  condições de fabrico e exigem ensaios mecânicos comparáveis.
- Que os casos da **Série A** são comparáveis entre modelos, programas ou
  impressoras diferentes (a única comparação válida na Série A é o par Phoenix
  PLA vs PETG, que só difere no material).
- Que a **integridade de malha** implica qualidade mecânica da peça.
- Que o processamento concluído demonstra sucesso de impressão, montagem, adequação
  funcional ou utilização segura.
- Que os custos são preços de mercado reais: assentam numa taxa única assumida de
  36,29 €/kg (o PETG usa a mesma taxa do PLA); um preço real distinto por
  fornecedor ou no tempo altera-os proporcionalmente.

## D.9 Registo fotográfico dos protótipos impressos

As imagens seguintes documentam **impressões físicas reais** dos modelos, obtidas
na impressora Bambu Lab A1. Complementam as estimativas digitais das secções
anteriores como **evidência visual e qualitativa** da preparação e do fabrico:
mostram que os ficheiros gerados pela plataforma foram impressos, montados e
articulados. As imagens não acrescentam medições quantitativas. As dimensões X, Y
e Z apresentadas em D.4.4 foram obtidas por medição directa das palmas. Uma
caracterização metrológica com leituras independentes e a verificação sistemática
da montagem constituem extensões possíveis, mas não integram o âmbito descritivo
adoptado nesta dissertação.

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
> Qualquer correcção posterior de orientação deve ser aplicada ao original
> conservado no material suplementar, sem alterar a referência da figura.
