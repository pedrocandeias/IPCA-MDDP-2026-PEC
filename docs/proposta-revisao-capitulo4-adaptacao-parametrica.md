# Proposta de revisão do Capítulo 4 — adaptação paramétrica dos modelos

## 1. Síntese da análise

O diagnóstico original do Capítulo 4 já não corresponde integralmente ao manuscrito actual. Foram acrescentados cabeçalhos às tabelas, fórmulas por modelo, um dicionário operacional de parâmetros e um percurso numérico até às malhas. A revisão agora necessária deve preservar essas correcções, evitar repetir o suplemento da versão 14.67.0 e integrar as adaptações posteriores com uma delimitação clara entre versão avaliada e evolução subsequente.

Tabela 1 — Estado actual dos problemas identificados no relatório académico

| Observação do relatório | Estado | Evidência actual | Acção ainda necessária |
| --- | --- | --- | --- |
| A secção 4.1 percorre requisitos de próteses activas antes de delimitar o artefacto | Parcialmente resolvido | Existe um parágrafo que limita a operacionalização a geometria, construção e fabrico | Colocar a delimitação no primeiro parágrafo e condensar actuadores, sensores, energia e desempenho não avaliados |
| Tabelas 4.1 e 4.2 sem cabeçalhos | Resolvido | Ambas possuem cabeçalhos semânticos no Markdown actual | Confirmar apenas a repetição dos cabeçalhos no DOCX final |
| Tabelas 4.5–4.7 apenas conceptuais | Maioritariamente resolvido | Tabelas 4.8–4.10 apresentam fórmulas, dicionário e caso completo | Remeter a especificação extensa para o Anexo C e actualizar as relações posteriores à versão 14.67.0 |
| Origem de parâmetros derivados não demonstrada | Parcialmente resolvido | Flexy, Paraglider e Phoenix possuem fórmulas; o suplemento conserva 42 declarações | Acrescentar Cyborg Beast, nova braçadeira Flexy, dependência dupla do Phoenix e campos contextuais do Paraglider |
| Uso de «adequação anatómica» e «equilíbrio funcional» sem comparação individual | Parcialmente resolvido | O texto já distingue coerência geométrica de validação clínica em vários pontos | Substituir as ocorrências remanescentes por «coerência geométrica», «relação dimensional codificada» ou «comportamento esperado» |
| Falta de parâmetros, limites, dependências e critérios por modelo | Parcialmente resolvido | Existe dicionário 14.67.0 para os três modelos comparados | Usar o Anexo C como complemento para os quatro modelos e assinalar tudo o que não é confirmável |
| Falta de tolerâncias, folgas e espessuras implementadas | Parcialmente resolvido | O código confirma algumas folgas e constantes | Registar apenas os valores confirmáveis; declarar que não existe ensaio dimensional geral nem tolerância consolidada por modelo |
| Falta de exemplo numérico completo | Resolvido | Secção 4.3.5 e suplemento do Flexy Beast | Não repetir o exemplo no Anexo C; usar exemplos complementares para dependências não descritas |
| Falta de figura própria de propagação | Não resolvido no corpo | Foi criada a Figura C.1 | Integrar a figura no Anexo C e referi-la na secção 4.3 |
| Revisão antropométrica repete o Capítulo 2 e antecipa o Anexo A | Não resolvido | A secção 4.2 continua extensa e reproduz fontes, extracção e normalização | Condensar para dados usados, regra de correspondência e limitações que afectam a modelação; remeter o método documental para o Anexo A |
| Secção 4.4 repete a teoria de RtD sem episódios verificáveis | Não resolvido | A secção continua predominantemente genérica | Substituir por uma cronologia de decisões com versão, problema, alteração e aprendizagem |
| Crítica à escala uniforme não reconciliada com Paraglider e Phoenix | Parcialmente resolvido | A secção 4.3.3 já justifica as excepções | Explicitar que a escala uniforme é preservada localmente para proteger interfaces e que no Phoenix também afecta os comprimentos digitais |
| Circunferência do antebraço associada genericamente ao encaixe | Parcialmente resolvido | O Cyborg e o Flexy usam agora `wrist_circumference_mm` para a braçadeira | Distinguir braçadeira do antebraço de encaixe clínico; o estudo não desenvolveu nem avaliou um encaixe individual |
| Restrições de fabrico sem valores confrontáveis | Parcialmente resolvido | Existem constantes e parâmetros mecânicos no código | Separar limites declarados, constantes herdadas e valores efectivamente examinados; não apresentar expectativas de fabrico como ensaios |

## 2. Estrutura proposta para o Capítulo 4

Recomenda-se manter as quatro secções principais, com a seguinte função:

1. **4.1 — Delimitação do artefacto e requisitos considerados:** identificar imediatamente os quatro modelos de mão passiva e separar requisitos da literatura de requisitos implementados.
2. **4.2 — Dados antropométricos usados na configuração:** conservar apenas unidade de análise, medidas activas, regra de correspondência, tratamento de ausência e limites; remeter extracção, fontes e normalização para o Anexo A.
3. **4.3 — Relações paramétricas implementadas:** apresentar uma síntese por modelo e remeter fórmulas, constantes, folgas e excepções para o Anexo C; conservar o exemplo 4.3.5 sem o duplicar.
4. **4.4 — Iterações e conhecimento de projecto:** substituir o ensaio genérico sobre RtD por uma cronologia de episódios concretos.

## 3. Texto exacto para abrir o Capítulo 4

Inserir imediatamente depois de `## Capítulo 4 — Desenvolvimento do Modelo Paramétrico` e antes do actual primeiro parágrafo de 4.1:

> Este capítulo trata um subconjunto delimitado do problema das próteses de membro superior: a adaptação paramétrica de modelos mecânicos passivos de mão destinados à exploração técnica e à prototipagem por fabrico aditivo. O trabalho implementado não inclui actuadores, sensores, fontes de energia, controlo mioeléctrico, desenho clínico de encaixes ou avaliação funcional com utilizadores. Esses temas permanecem no enquadramento geral da literatura, mas não constituem propriedades demonstradas pelo artefacto.
>
> A biblioteca examinada compreende quatro modelos registados na plataforma: Flexy Beast, Paraglider Hand, UnLimbited Phoenix Hand e Cyborg Beast. Os três primeiros integram a comparação dimensional e os ensaios descritos no Capítulo 8. O Cyborg Beast foi integrado posteriormente e é analisado como evolução projectual, sem ser incluído nas séries comparativas ou físicas. A reconstrução `pec Phoenix hand` permanece material de desenvolvimento e fica fora do âmbito deste capítulo.
>
> A unidade de análise é a relação entre um vector de parâmetros, a regra geométrica específica de cada modelo e a malha gerada. «Adaptação paramétrica» designa aqui a capacidade de modificar dimensões dentro das relações e limites codificados. Não designa ajuste anatómico validado, conforto, eficácia protésica ou segurança clínica.

### 3.1 Tabela de delimitação a inserir no início de 4.1

Tabela 4.X — Modelos abrangidos pelo desenvolvimento paramétrico

| Modelo | Estado no estudo | Estratégia de adaptação | Evidência considerada |
| --- | --- | --- | --- |
| Flexy Beast | activo; incluído na comparação | escala da palma pela fórmula Cyborg Beast, comprimentos digitais relativos e braçadeira independente | geração, exportação, malhas, preparação e série física |
| Paraglider Hand | activo; incluído na comparação | escala uniforme da palma e escalas próprias de parte dos dedos | geração, exportação, malhas, preparação e série física |
| UnLimbited Phoenix Hand | activo; incluído na comparação | escala global limitada e alongamento localizado dos segmentos digitais | geração, exportação, malhas e preparação |
| Cyborg Beast | activo; evolução posterior | escala da palma, curvas calibradas dos dedos, divisão proximal–distal e braçadeira pelo punho | integração e geração; excluído da comparação principal |

Na integração, esta tabela deve substituir a repetição equivalente da Tabela 5.2 ou ser reduzida no Capítulo 5 a uma remissão para o inventário do Capítulo 4.

## 4. Condensação exacta de 4.1

Depois da nova delimitação, conservar apenas um parágrafo de enquadramento geral e substituir os parágrafos que enumeram actuadores, sensores, energia, forças, binários e autonomia pela seguinte formulação:

> A literatura descreve requisitos funcionais, ergonómicos, técnicos, produtivos e psicossociais que devem convergir num dispositivo protésico. Neste estudo, porém, apenas três grupos foram traduzidos em propriedades observáveis do protótipo: dimensões e relações geométricas; preservação de interfaces mecânicas herdadas; e preparação preliminar para fabrico aditivo. Conforto, usabilidade, força, amplitude funcional, durabilidade, segurança, aceitação e incorporação corporal não foram operacionalizados nem avaliados.
>
> Os requisitos implementados foram, assim, formulados como condições de projecto: aceitar um conjunto explícito de entradas; aplicar relações determinísticas; preservar furos, eixos e zonas de montagem quando a geometria varia; manter os valores dentro da gama declarada; permitir isolar e exportar componentes; e tornar visíveis as situações em que um perfil ultrapassa a cobertura do modelo. Estas condições permitem examinar coerência e comportamento geométrico, mas não substituem requisitos clínicos ou funcionais.

Substituir a frase «exercício de optimização sujeito a múltiplas restrições» por:

> processo de configuração condicionado por relações e limites explícitos

Não existe uma função objectivo nem comparação sistemática de alternativas que sustente o termo «optimização».

## 5. Condensação de 4.2 e remissão para o Anexo A

### 5.1 Conteúdo a manter no corpo

Manter:

- definição das medidas principais da mão;
- diferença entre medida individual e referência populacional;
- limitação do escalonamento proporcional;
- correspondência entre perfil e parâmetros;
- mapa canónico de campos;
- ausência de populações específicas e tratamento de campos em falta;
- limites decorrentes de dados de pessoas sem amputação.

### 5.2 Conteúdo a deslocar

Deslocar para o Anexo A, evitando repetição no corpo:

- inventário detalhado das doze fontes;
- critérios completos de inclusão e exclusão;
- descrição extensa do formato longo;
- contagens por tipo de estatística;
- discussão fonte a fonte de representatividade;
- relato completo da extracção HTML e das conversões de unidade.

### 5.3 Texto de substituição para o bloco extenso sobre a base

Substituir o bloco iniciado por «Bases de dados antropométricas, extracção e normalização» até antes de «Correspondência entre perfil populacional e parâmetros do modelo» por:

> A configuração recorre a uma base local em formato longo, na qual cada linha representa uma estatística associada a uma medida e a um grupo, e não uma pessoa. O conjunto combina fontes populacionais heterogéneas quanto a idade, sexo, país, amostra, protocolo e estatísticas disponíveis. Por esse motivo, os valores funcionam como referências iniciais e não como substitutos da medição individual.
>
> Para a modelação, a base cumpre três funções: identificar medidas recorrentes; apoiar a definição de intervalos de configuração; e fornecer casos populacionais para examinar a propagação dos parâmetros. A origem documental, a população, a unidade e as notas de qualidade permanecem associadas a cada valor, permitindo regressar à fonte quando surgem incompatibilidades.
>
> A extracção, a selecção das fontes, a normalização para milímetros, a cobertura populacional e as limitações documentais são apresentadas integralmente no Anexo A. No corpo do capítulo conservam-se apenas as regras que alteram decisões geométricas: medidas disponíveis, correspondência com os campos do modelo, tratamento de ausência e limites de utilização.
>
> A maior parte dos dados descreve pessoas sem amputação e não representa a forma do membro residual, a deformação dos tecidos ou a interface corpo–dispositivo. Uma referência populacional pode apoiar uma configuração inicial; uma adaptação individual exige medidas directas, eventual digitalização tridimensional e avaliação própria.

## 6. Revisão de 4.3

### 6.1 Nota de versão a inserir antes da Tabela 4.8

> As relações seguintes distinguem três estados. A versão 14.67.0 corresponde ao fecho dos ensaios principais e ao dicionário suplementar arquivado. A versão 14.71.0 acrescentou a braçadeira comum do Flexy Beast e relações mais completas do Cyborg Beast. A versão 14.72.0 uniformizou os grupos e os nomes dos controlos equivalentes, sem modificar as relações geométricas avaliadas. Estes desenvolvimentos não são retroactivamente apresentados como parte dos ensaios concluídos na versão 14.67.0.

### 6.2 Substituição da Tabela 4.8

Tabela 4.8 — Síntese das relações implementadas e respectivas limitações

| Modelo | Entradas activas principais | Transformação implementada | Limitação que deve acompanhar a leitura |
| --- | --- | --- | --- |
| Flexy Beast | largura da palma; comprimentos dos cinco dedos; circunferência do punho | `xScaleFactor = (palm_breadth_mm + 5) / 55`; o médio define o multiplicador digital e os restantes dedos definem proporções; a braçadeira deriva de circunferência/π mais folga | a largura introduzida alimenta uma fórmula herdada e não coincide directamente com a extensão transversal da malha |
| Cyborg Beast | largura da palma; comprimentos totais e proximais; circunferência do punho | escala global pela fórmula Cyborg Beast; curvas calibradas para os segmentos; braçadeira dimensionada independentemente da mão | as curvas são calibrações da geometria e possuem limites internos; o modelo não integrou a comparação principal |
| Paraglider Hand | largura da palma; comprimentos dos dedos; opções de hardware | `overall_scale = palm_breadth_mm / 66,4`; correcção `overall_scale / 1,25` na palma Reborn; escalas próprias para indicador, médio, anelar e mindinho | palma uniforme para preservar furos; comprimento e espessura da palma são contextuais; o polegar ainda usa a escala do médio |
| UnLimbited Phoenix Hand | largura da palma; comprimentos totais e proximais dos dedos | `HandPerc` limitado a 100%–160%; alongamento localizado de zonas sem furos | perfis inferiores a 82 mm ficam no piso; os comprimentos digitais são novamente afectados pela escala global |

### 6.3 Texto sobre escala uniforme a substituir no final de 4.3.3

> O escalonamento uniforme não foi eliminado em todos os modelos. Foi mantido onde a arquitectura herdada exigia preservar furos circulares, espaçamentos e componentes montados como conjunto. No Paraglider, esta opção protege a palma e os pinos enquanto parte dos dedos recebe escalas próprias. No Phoenix, a montagem completa conserva uma escala uniforme e os dedos são alongados apenas em faixas sem furos; como o alongamento antecede a escala global, o comprimento final depende das duas operações.
>
> A crítica ao escalonamento proporcional aplica-se, portanto, ao seu uso como substituto de todas as diferenças antropométricas. Uma transformação uniforme local pode constituir uma restrição mecânica legítima, desde que o texto identifique o que preserva, o que deixa de adaptar e como afecta as restantes dimensões.

### 6.4 Remissão para o novo anexo

Inserir no final de 4.3.4:

> O Anexo C complementa o dicionário da versão 14.67.0 com as adaptações posteriores, as relações internas do Cyborg Beast, os valores de folga e espessura confirmáveis, as excepções da escala uniforme e os campos que ainda não produzem uma transformação geométrica própria. O anexo distingue valores directos, derivados, fixos e contextuais e assinala expressamente as propriedades que não podem ser confirmadas pelos ficheiros examinados.

### 6.5 Exemplo numérico

Conservar a actual secção 4.3.5 e a Tabela 4.10. Não as repetir no Anexo C. Acrescentar apenas a seguinte frase final:

> Os exemplos complementares do Anexo C mostram duas dependências que este percurso não cobre: o parâmetro de comprimento do polegar do Paraglider ainda não controla uma escala própria e, no Phoenix, a escala global volta a multiplicar os comprimentos definidos localmente.

## 7. Substituição integral da secção 4.4

Substituir o texto actual de 4.4 pela versão seguinte.

### 4.4 Iterações e decisões de projecto

> A evolução dos modelos foi documentada através de episódios em que uma configuração, uma malha ou uma montagem tornou visível uma limitação e conduziu a uma alteração específica. A Tabela 4.11 resume os episódios com maior influência na estrutura paramétrica. As versões posteriores ao fecho da comparação principal são apresentadas como desenvolvimento subsequente e não como resultados retroactivos dos ensaios anteriores.

Tabela 4.11 — Cronologia das principais iterações paramétricas

| Data e versão | Problema observado | Decisão introduzida | Aprendizagem de projecto |
| --- | --- | --- | --- |
| 15–16 Jun. 2026; 14.10–14.11 | ficheiros Paraglider dispersos e nomes incompatíveis com a plataforma | consolidação da família num modelo com componentes e duas palmas | integrar um modelo aberto exige declarar dependências, variantes e campos comuns antes de expor parâmetros |
| 28 Jun. 2026; 14.16–14.17 | a palma Reborn permanecia no tamanho médio apesar de variar `palm_breadth_mm` | compensação da escala 1,25 preservada no módulo carregado por `use` | a resposta de um controlo não pode ser inferida pelo nome; deve ser confirmada na malha gerada |
| 29 Jun. 2026; 14.18 | `HandPerc_override` permitia ao Phoenix contornar o piso de 100% | aplicação do mesmo limite de 100%–160% aos dois percursos | limites equivalentes devem actuar em todas as entradas que conduzem à mesma transformação |
| 29 Jun. 2026; 14.19 | a IA alterava a lateralidade apesar de esta ser uma decisão binária do projecto | lateralidade transferida para a interface determinística e excluída das sugestões | decisões inequívocas e críticas não devem permanecer num processo probabilístico |
| 9–10 Jul. 2026; 14.32–14.37 | integração do Cyborg Beast sem controlo independente dos segmentos e com desalinhamentos | calibração do alcance, divisão proximal–distal e reposicionamento sobre os eixos MCP/PIP | a personalização exige preservar interfaces articulares enquanto se altera o alcance dos segmentos |
| 10 Jul. 2026; 14.40–14.44 | braçadeira desligada da circunferência do punho e polegar sem correspondência estável | braçadeira dimensionada por circunferência/π, assentamento automático no pino e calibração do polegar | mão, punho e antebraço não devem depender de uma única escala global |
| 10–11 Jul. 2026; 14.48 | dedos Phoenix constituídos por malhas fixas | divisão das colunas e alongamento apenas das faixas sem furos | modelos de malha podem receber variação local se as zonas funcionais forem isoladas |
| 14 Jul. 2026; versão 14.71.0 | braçadeira Flexy parametrizada por dimensões próprias, sem ligação directa ao mapa do punho | adopção da braçadeira comum do Cyborg e de `wrist_circumference_mm` | a gramática comum deve ligar a mesma medida corporal a funções equivalentes entre modelos, sem apagar as diferenças geométricas |
| 14 Jul. 2026; versão 14.72.0 | grupos e nomes de controlos equivalentes variavam entre modelos | adopção de uma ordem comum; `LeftRight` passou a `mirrored` no Phoenix e `show_assembled` passou a `print_layout` no Paraglider | a coerência da interface beneficia de nomes comuns quando a decisão é equivalente, sem obrigar a uniformizar diferenças geométricas legítimas |

> Estes episódios produziram quatro conclusões circunscritas. Primeiro, a integração de um modelo aberto exige examinar o âmbito das variáveis dentro de cada ficheiro, e não apenas os controlos apresentados. Segundo, preservar uma interface mecânica pode justificar escala uniforme local ou alongamento selectivo. Terceiro, um intervalo declarado na interface não substitui verificações dentro da transformação geométrica. Quarto, a equivalência nominal entre uma medida e um parâmetro deve ser confirmada na malha, porque fórmulas herdadas e escalas sucessivas podem alterar a dimensão final.
>
> A iteração funcionou, assim, como instrumento de investigação através do design: cada falha alterou a compreensão do objecto configurável e conduziu a uma regra mais explícita. O resultado não é uma metodologia universal de personalização protésica, mas um conjunto documentado de decisões para integrar modelos heterogéneos, preservar as suas interfaces e tornar visíveis os respectivos limites.

## 8. Correcções terminológicas localizadas

Aplicar no Capítulo 4:

| Formulação a evitar | Formulação proposta |
| --- | --- |
| adequação anatómica | coerência face às medidas introduzidas; correspondência dimensional por verificar |
| equilíbrio funcional | relação geométrica ou mecânica codificada |
| modelo funcional | geometria gerada; protótipo técnico; modelo montável, quando demonstrado |
| geometria do encaixe | geometria da braçadeira do antebraço, salvo quando exista um encaixe individual efectivamente modelado |
| optimização | configuração condicionada; ajuste paramétrico |
| garantir fabrico e robustez | limitar combinações e apoiar a preparação para fabrico |
| personalização anatómica | configuração baseada em medida ou referência antropométrica |

Evitar afirmar que limites declarados «garantem» robustez. O texto deve distinguir:

- intervalo apresentado na interface;
- limitação aplicada no cálculo;
- constante herdada do modelo;
- valor observado numa malha;
- propriedade ainda por ensaiar na peça física.

## 9. Integração do Anexo C

Ficheiros preparados:

- `sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.md`;
- `sources/manuscript/annexes/adaptacao_parametrica_modelos/figura_c1_fluxo_adaptacao_parametrica.svg`.

Título proposto na dissertação:

> **Anexo C — Adaptação paramétrica dos modelos de mão protésica**

Remissões mínimas:

- final de 4.3.3: mecanismos e excepções por modelo;
- final de 4.3.4: parâmetros, valores fixos, folgas e campos contextuais;
- final de 4.3.5: exemplos complementares e limitações descobertas;
- Capítulo 8: discussão das correcções Paraglider e Phoenix.

## 10. Ficheiros consultados

- `/home/pec/dev/ai-parametric-prosthetic-hand-generator/docs/relatorio-adaptacao-antropometrica.md`;
- `/home/pec/dev/ai-parametric-prosthetic-hand-generator/models/models-config.json`;
- modelos OpenSCAD activos de Flexy Beast, Cyborg Beast, Paraglider Hand e UnLimbited Phoenix;
- `server/services/profileMapping.js` e `server/services/anthropometricImporter.js`;
- `projecto-completo.md`, secções 4.1–4.4 e inventário 5.2;
- `docs/relatorio-revisao-academica-integral-dissertacao-2026-07-13.md`;
- `sources/manuscript/annexes/dicionario_parametros_v14.67.0/`.

## 11. Verificações executadas

- confirmação dos modelos registados e respectivos parâmetros numéricos;
- comparação entre configuração, mapa antropométrico e variáveis OpenSCAD;
- confirmação das fórmulas e limites internos descritos;
- recálculo dos exemplos complementares de Cyborg Beast, Paraglider e Phoenix;
- comparação do suplemento 14.67.0 com a versão 14.72.0;
- identificação de campos contextuais sem efeito geométrico confirmado;
- pesquisa das palavras excluídas pelo utilizador nos dois documentos produzidos;
- verificação da sintaxe XML da figura SVG.
