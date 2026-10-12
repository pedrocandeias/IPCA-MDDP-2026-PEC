# Guião da apresentação

Versão 0.5. 11/10/2026. Estrutura de trabalho para 30 minutos, adaptável aos 20 minutos indicados para a prova.

A [apresentação gráfica revista](apresentacao/README.md) concretiza os 17 blocos deste guião num percurso principal de 20 minutos, com oito diapositivos adicionais de apoio. O PPTX inclui notas de fala e indicações de aprofundamento para treino de 30 minutos. Os tempos continuam sujeitos a ensaio.

## Critério de redação

Usar frases diretas, explicando a relação entre cada decisão e o resultado observado. Evitar enumerações retóricas em três elementos, travessões e construções de contraste enfático. Manter as formulações integrais das perguntas aprovadas e as enumerações necessárias à descrição dos dados.

## Mensagem central

O contributo do projeto está na organização e na verificação de um percurso de configuração de modelos protésicos: a relação entre uma medida de entrada e a peça produzida depende das regras e dos limites de cada modelo. A plataforma torna essa relação examinável e permite usar sugestões de IA sob controlo humano.

## Enquadramento em Design e Desenvolvimento de Produto

Em cada exemplo, explicitar o requisito, a decisão tomada, a consequência para a configuração ou para a forma e a evidência usada para a examinar. A plataforma é o artefacto que permite desenvolver e estudar esse processo. A argumentação deverá destacar o contributo autoral para a organização da variação, as interfaces entre componentes, a preparação para fabrico e a distribuição do controlo.

Identificar o papel de quem configura e a pessoa a quem o dispositivo se destinaria. As escolhas de forma e cor podem ser mostradas como possibilidades do sistema; a experiência de aceitação e os significados atribuídos ao produto permanecem por estudar. A preparação da discussão académica inclui a experiência das pessoas com produtos personalizados, conforme o [contexto público do arguente](contexto_arguente.md).

A objeção «onde entra o design?» deve ficar respondida ao longo da apresentação. No bloco 2, formular o problema de configuração do produto; nos blocos 6 e 10, mostrar uma decisão justificada e o seu efeito; no bloco 16, explicitar o conhecimento produzido. Uma correção de código não constitui, por si só, evidência suficiente de investigação em design. Deve ser relacionada com o requisito, a regra do modelo, a consequência geométrica ou material e a reflexão obtida. As perguntas 23 a 26 do guião de discussão desenvolvem esta objeção.

## Estrutura e tempos

Os tempos incluem transições e explicação dos elementos visuais. São metas para o ensaio, não tempos já medidos. Cada bloco pode corresponder a um diapositivo; o percurso da plataforma pode usar uma sequência de imagens ou um vídeo.

| Bloco | Título | Mensagem a transmitir | Versão 30 min | Versão 20 min |
|---:|---|---|---:|---:|
| 1 | Da medida à peça física | Apresentar o problema e o âmbito. | 1:00 | 0:30 |
| 2 | Como passar de uma medida a uma peça? | Explicar a passagem entre medida e peça. | 1:30 | 1:00 |
| 3 | Perguntas de investigação e âmbito da avaliação | Distinguir perguntas aprovadas e avaliação realizada. | 1:30 | 1:00 |
| 4 | Objetivo geral e objetivos específicos | Explicitar o propósito e os sete objetivos da investigação. | 2:00 | 1:30 |
| 5 | Como a literatura orienta o projeto | Relacionar referências com o argumento da exposição. | 1:30 | 1:00 |
| 6 | Investigar através do desenvolvimento do protótipo | Explicar a aprendizagem obtida ao verificar uma decisão. | 1:30 | 1:15 |
| 7 | HandFab: um percurso com decisões explícitas | Mostrar sugestão, revisão, regras e exportação. | 1:30 | 1:15 |
| 8 | Fontes antropométricas e critérios de utilização | Identificar fontes dos dados e definição das medidas. | 1:30 | 1:00 |
| 9 | Da base consolidada aos perfis do HandFab | Explicar como os dados publicados são preparados para a aplicação. | 1:30 | 1:15 |
| 10 | Cada modelo exige regras próprias | Explicar a escala Paraglider e o limite Phoenix. | 2:00 | 1:30 |
| 11 | A IA propõe um ponto de partida | Delimitar o papel das sugestões. | 2:00 | 1:15 |
| 12 | Configuração e pré-visualização no HandFab | Acompanhar a configuração até à pré-visualização. | 2:00 | 1:00 |
| 13 | A avaliação acompanhou etapas diferentes | Distinguir os conjuntos de avaliação. | 2:00 | 1:30 |
| 14 | Peça e malha: diferenças medidas, com limites | Interpretar os desvios sem extrapolar precisão. | 2:30 | 1:45 |
| 15 | As falhas também definem o próximo passo | Relacionar falhas com revisões necessárias. | 2:00 | 1:00 |
| 16 | O contributo para a configuração do produto | Explicar o contributo a partir dos resultados obtidos. | 3:00 | 1:45 |
| 17 | As regras de cada modelo condicionam o resultado | Fixar o contributo e o próximo passo. | 1:00 | 0:30 |
| | **Total** | | **30:00** | **20:00** |

## Desenvolvimento dos blocos

### 1. Da medida à peça física

No diapositivo: título oficial, autor, orientador, curso e uma imagem própria dos protótipos. Confirmar a identificação institucional antes da exportação final. Usar a Figura 27, 28 ou 29 como ponto de partida visual, mantendo a identificação dos modelos.

Abertura proposta para ensaio:

> Este projeto investiga como o design de produto pode organizar a configuração preliminar de modelos de mão protésica destinados à impressão 3D. Desenvolvi o HandFab para configurar modelos paramétricos a partir de referências antropométricas. A plataforma permite também solicitar sugestões iniciais de inteligência artificial. A investigação acompanhou esse percurso até à preparação para impressão e à observação e medição de peças físicas. Vou apresentar as decisões tomadas e a aprendizagem obtida ao verificar os seus efeitos.

### 2. Como passar de uma medida a uma peça?

Mostrar uma cadeia curta: medida de entrada, parâmetro, regra geométrica e dimensão da peça. Explicar que o nome de um parâmetro pode sugerir uma correspondência direta que a arquitetura geométrica não assegura.

Base: 1.2, 4.3 e 4.4. Mostrar o problema através de um modelo utilizado no projeto; evitar abrir com uma longa classificação de próteses. Os custos e o acesso são parte do enquadramento, não resultados de redução de custos demonstrados pelo protótipo.

### 3. Perguntas de investigação e âmbito da avaliação

Apresentar os três eixos em forma abreviada, identificados como síntese das perguntas aprovadas: configuração e controlo; avaliação e possibilidade de reproduzir resultados; requisitos e experiência humana. Manter a formulação integral num diapositivo de apoio.

Perguntas aprovadas:

1. «Como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo sobre as decisões de projeto?»
2. «Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a possibilidade de reproduzir os resultados de próteses impressas em 3D?»
3. «Como é que o design industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?»

Explicar oralmente: a avaliação incidiu na configuração, na propagação dos parâmetros, na exportação e na verificação técnica e dimensional. O estudo não incluiu participantes. A eficácia protésica e a experiência de utilização quotidiana ficaram por avaliar.

### 4. Objetivo geral e objetivos específicos

Apresentar o objetivo geral e os sete objetivos específicos da secção 1.3. Distinguir o conhecimento produzido através do design das tarefas de organização dos dados, adaptação dos modelos, integração da plataforma e delimitação da IA. Fechar com a avaliação técnica e a identificação das condições para estudos posteriores. O diapositivo contém uma síntese dos sete pontos, sem alterar o âmbito do manuscrito.

### 5. Como a literatura orienta o projeto

Destacar Cross, Frayling e Zimmerman, Fischer, Manero e Cabibihan pela função no argumento: conhecimento de design, investigação através do projeto, modificação de sistemas e avaliação de próteses. As obras foram selecionadas pela sua utilidade para justificar as opções do projeto e interpretar os resultados. Não afirmar participação ou codesign a partir da simples existência de parâmetros editáveis.

### 6. Investigar através do desenvolvimento do protótipo

Usar um caso da Tabela 4 como evidência de Research Through Design. Exemplo: a palma do Paraglider permanecia na escala da biblioteca; a comparação com os dedos e as malhas revelou o problema; a alteração do ponto de aplicação da escala modificou a resposta geométrica; os perfis foram novamente examinados.

Distinguir os papéis: Research Through Design enquadra a produção de conhecimento através do artefacto; Double Diamond organiza momentos de abertura e convergência. Não é necessário explicar extensamente ambos os modelos na fala principal. Conservar as referências do manuscrito no diapositivo ou nas notas.

### 7. HandFab: um percurso com decisões explícitas

Redesenhar um esquema simples a partir das Figuras 17 e 18: perfil ou descrição; proposta e revisão de parâmetros; geração em OpenSCAD no navegador; visualização; exportação; preparação para impressão.

Assinalar visualmente onde atua o serviço de IA, onde se aplicam regras determinísticas e onde a pessoa confirma ou altera valores. Explicar apenas os componentes necessários para compreender as decisões; detalhes de Node.js, Express e persistência ficam para os diapositivos de apoio.

### 8. Fontes antropométricas e critérios de utilização

Apresentar Gordon et al. (1989; 2014), distinguindo ANSUR 1988 e ANSUR II; DINED, com kima1993, geron1998 e dined2004; e ISO 7250-1:2017, para definições das medidas. Explicar as funções próprias de cada fonte. A norma não certifica os dados nem estabelece adequação individual.

### 9. Da base consolidada aos perfis do HandFab

Mostrar a sequência: estudos originais, base local consolidada, perfis na aplicação. Os CSV registam indicadores estatísticos com proveniência. Média e desvio-padrão da mesma medida são duas linhas; não são duas pessoas. Os 100 perfis são o estado documentado da aplicação: 97 importados em lote, dois por CSV e um criado manualmente. As contagens de linhas não equivalem às de perfis. A base ANSUR completa e o seu subconjunto não devem ser somados como fontes independentes. O Suplemento 1 e a secção 4.2 sustentam esta distinção.

### 10. Cada modelo exige regras próprias

Caso principal: correção da escala da palma no Paraglider. Mostrar a mesma configuração antes/depois apenas se existirem imagens ou malhas históricas comparáveis; não reconstruir uma imagem como se fosse evidência original. Na ausência desses elementos, usar um esquema identificado como explicação da regra.

Caso complementar: no UnLimbited Phoenix, a largura da palma tem um limite mínimo de cerca de 82 mm. Um perfil menor não implica uma peça com essa largura. Mostrar a consequência para a configuração e para a mensagem ao utilizador.

Base: 4.4, 8.3, Tabelas 28 a 29 e Anexo C. Na versão de 20 minutos, desenvolver o Paraglider e resumir o Phoenix numa frase.

### 11. A IA propõe um ponto de partida

Mostrar uma descrição de ensaio e um excerto legível da resposta estruturada. Assinalar os parâmetros válidos e a necessidade de revisão. Explicar como se verifica o formato da resposta e o efeito dos valores no modelo. A adequação anatómica exige uma avaliação própria.

A lateralidade é um exemplo forte: uma decisão crítica foi separada da sugestão probabilística e passou para uma regra determinística. O manuscrito refere cinco execuções no primeiro conjunto experimental; não transformar esse resultado numa taxa geral de precisão. As respostas simuladas usadas em ensaios de recuperação constituem outro conjunto de evidência.

### 12. Configuração e pré-visualização no HandFab

Percurso proposto, ainda não gravado: selecionar um modelo; escolher uma referência ou introduzir parâmetros; mostrar a origem dos valores; rever uma configuração; gerar a geometria; exportar; mostrar o ficheiro de preparação e uma peça correspondente.

Usar um caso já documentado. Se surgir uma resposta de IA previamente guardada, identificá-la como tal. A versão principal pode usar imagens ou vídeo local; uma demonstração ao vivo fica dependente das condições da sala e do tempo. O guião não pressupõe nova execução do serviço externo nem gravações já existentes.

O diapositivo 12 dispõe de um minuto no percurso principal e de dois minutos no treino desenvolvido. O tempo inclui a observação das capturas e a explicação do efeito geométrico.

### 13. A avaliação acompanhou etapas diferentes

Apresentar uma matriz simples: objeto examinado, método e evidência. Quatro linhas: funcionamento da plataforma; sugestões de IA; geometria exportada; preparação e peças físicas.

Distinguir a Série A, com quatro projetos em condições diferentes, da Série B, com 12 casos numa condição digital comum. A comparação física contém 72 medições dimensionais, uma leitura por eixo e peça/material. Não são 72 participantes ou 72 repetições da mesma medição.

### 14. Peça e malha: diferenças medidas, com limites

Usar a Figura 28 e um gráfico a construir a partir de `comparacao_dimensional_72_medicoes.csv`. A imagem mostra as peças; o gráfico deve identificar modelo, perfil, material e eixo. Comparar a medida de entrada com a extensão da malha. Explicar depois como foi medida a peça física.

Os desvios físicos face à malha são descritivos; não se estimou a incerteza por repetição. O processamento dos 12 casos da Série B gerou trajetórias, com avisos em alguns casos. Os valores produzidos pelo programa, incluindo tempo, massa e custo, são estimativas de preparação para impressão.

Se for mostrada a Phoenix montada, dizer que existe observação de bancada num espécime. O registo corresponde a uma observação de bancada. A avaliação clínica e a durabilidade exigem outros ensaios; o número exato de ciclos não foi registado. A divergência de redação das conclusões deve ser resolvida antes da versão final dos diapositivos.

### 15. As falhas também definem o próximo passo

Selecionar dois resultados: o valor simulado acima do limite que chegou ao estado interno e uma barreira de acessibilidade identificada no percurso autenticado. Explicar o que cada falha revela sobre a distribuição dos controlos e sobre a interface.

Conservar em apoio os resultados da repetição de exportações: sete Flexy Beast, cinco Paraglider e cinco Phoenix concluídas com resultados idênticos dentro de cada configuração; objetivo de dez por modelo não cumprido. Evitar apresentar o conjunto como aprovação integral da robustez ou da compatibilidade entre navegadores.

### 16. O contributo para a configuração do produto

Usar uma versão reduzida da Tabela 31, com uma linha por pergunta e duas colunas: evidência obtida e dimensão ainda não avaliada.

- Pergunta 1: configuração editável e controlo das sugestões demonstrados; conforto e adequação funcional individual não avaliados.
- Pergunta 2: os métodos permitiram verificação técnica e comparação dimensional descritiva. A eficácia protésica e a durabilidade exigem outros ensaios, bem como estudos de usabilidade com participantes.
- Pergunta 3: requisitos traduzidos em opções de configuração e regras de controlo. A experiência de utilização quotidiana permanece por estudar, incluindo a aceitação e as implicações para a dignidade e autonomia.

Explicar o conhecimento obtido ao verificar as regras de cada modelo. Usar um caso concreto para mostrar como essa aprendizagem condiciona as opções de configuração e a revisão das sugestões de IA. Não afirmar originalidade absoluta relativamente a toda a literatura.

### 17. As regras de cada modelo condicionam o resultado

Fecho proposto:

> O projeto permitiu construir e examinar um percurso de configuração que liga dados antropométricos, parâmetros, geometria e peças físicas. Os ensaios mostraram que a personalização depende das regras de cada modelo e da verificação dos seus efeitos. A IA apoiou a sugestão inicial de valores, mantendo as decisões críticas sob regras explícitas e revisão humana. O passo seguinte é aprofundar a caracterização física e avaliar o processo com os grupos de utilizadores previstos. O contributo deste trabalho é a base técnica e metodológica documentada para desenvolver essa investigação.

## Diapositivos de apoio a preparar

Perguntas e hipóteses aprovadas; matriz metodológica; fontes antropométricas; fórmulas e limites por modelo; distinção entre ensaios reais e simulados de IA; configuração das Séries A e B; medições físicas; repetição e navegadores; acessibilidade; registo da montagem Phoenix; declaração de utilização de IA; referências essenciais.

## Primeiro ensaio

Ensaiar a explicação do problema e a sua ligação ao caso do Paraglider, nos blocos 2 e 10. Verificar depois se a conclusão do bloco 16 é sustentada por esses exemplos. Cronometrar depois o percurso completo. Na versão de 20 minutos, reduzir exemplos e detalhe conforme a tabela, mantendo as conclusões e os limites. A passagem entre as duas versões deve ser feita por seleção de conteúdo, sem depender de acelerar a fala.
