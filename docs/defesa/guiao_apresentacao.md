# Guião da apresentação

Versão 0.7. 25/10/2026. Estrutura de trabalho para 30 minutos, adaptável aos 20 minutos indicados para a prova.

A [apresentação gráfica revista](apresentacao/README.md) concretiza os 23 blocos deste guião num percurso principal de 20 minutos, com sete diapositivos adicionais de apoio. O PPTX inclui notas de fala e indicações de aprofundamento para treino de 30 minutos. Os tempos continuam sujeitos a ensaio.

## Critério de redação

Usar frases diretas, explicando a relação entre cada decisão e o resultado observado. Evitar enumerações retóricas em três elementos, travessões e construções de contraste enfático. Manter as formulações integrais das perguntas aprovadas e as enumerações necessárias à descrição dos dados.

## Mensagem central

O contributo do projeto está na organização e na verificação de um percurso de configuração de modelos protésicos: a relação entre uma medida de entrada e a peça produzida depende das regras e dos limites de cada modelo. A plataforma torna essa relação examinável e permite usar sugestões de IA sob controlo humano.

## Enquadramento em Design e Desenvolvimento de Produto

Em cada exemplo, explicitar o requisito, a decisão tomada, a consequência para a configuração ou para a forma e a evidência usada para a examinar. A plataforma é o artefacto que permite desenvolver e estudar esse processo. A argumentação deverá destacar o contributo autoral para a organização da variação, as interfaces entre componentes, a preparação para fabrico e a distribuição do controlo.

Identificar o papel de quem configura e a pessoa a quem o dispositivo se destinaria. As escolhas de forma e cor podem ser mostradas como possibilidades do sistema; a experiência de aceitação e os significados atribuídos ao produto permanecem por estudar. A preparação da discussão académica inclui a experiência das pessoas com produtos personalizados, conforme o [contexto público do arguente](contexto_arguente.md).

A objeção «onde entra o design?» deve ficar respondida ao longo da apresentação. No bloco 2, explicar a motivação e as barreiras de acesso; no bloco 3, formular o problema de configuração; nos blocos 6 e 13, mostrar uma decisão e o seu efeito; no bloco 22, explicitar o conhecimento produzido. Uma correção de código não constitui, por si só, evidência suficiente de investigação em design. Deve ser relacionada com o requisito, a regra do modelo, a consequência geométrica ou material e a reflexão obtida. As perguntas 23 a 26 do guião de discussão desenvolvem esta objeção.

## Estrutura e tempos

Os tempos incluem transições e explicação dos elementos visuais. São metas para o ensaio, não tempos já medidos. Cada bloco pode corresponder a um diapositivo; o percurso da plataforma pode usar uma sequência de imagens ou um vídeo.

| Bloco | Título | Versão 30 min | Versão 20 min |
|---:|---|---:|---:|
| 1 | Da medida à peça física | 0:40 | 0:35 |
| 2 | O que motivou o desenvolvimento do projeto? | 1:50 | 1:15 |
| 3 | Como passar de uma medida a uma peça? | 1:10 | 1:00 |
| 4 | Perguntas de investigação e âmbito da avaliação | 1:00 | 0:40 |
| 5 | Objetivo geral e objetivos específicos | 1:50 | 1:05 |
| 6 | Como organizei a investigação e o desenvolvimento | 2:05 | 1:20 |
| 7 | Como integrei a IA na investigação | 1:25 | 0:55 |
| 8 | Elicit: da pergunta à bibliografia organizada | 2:30 | 1:30 |
| 9 | Como a literatura orienta o projeto | 0:50 | 0:40 |
| 10 | HandFab: um percurso com decisões explícitas | 0:55 | 0:45 |
| 11 | Fontes antropométricas e critérios de utilização | 1:05 | 0:45 |
| 12 | Da base consolidada aos perfis do HandFab | 1:05 | 0:45 |
| 13 | Cada modelo exige regras próprias | 1:25 | 1:00 |
| 14 | A IA propõe um ponto de partida | 1:25 | 0:55 |
| 15 | Configuração e pré-visualização no HandFab | 1:10 | 0:45 |
| 16 | Escolher cores e materiais no HandFab | 0:30 | 0:20 |
| 17 | Da geometria gerada à exportação | 0:45 | 0:30 |
| 18 | A avaliação acompanhou etapas diferentes | 1:05 | 0:50 |
| 19 | Comparar peças de diferentes perfis | 1:00 | 0:40 |
| 20 | Peça e malha: diferenças medidas, com limites | 2:00 | 1:15 |
| 21 | Phoenix: uma montagem observada em bancada | 1:10 | 0:45 |
| 22 | O contributo para a configuração do produto | 2:35 | 1:25 |
| 23 | As regras de cada modelo condicionam o resultado | 0:30 | 0:20 |
| | **Total** | **30:00** | **20:00** |

## Desenvolvimento dos blocos

### 1. Da medida à peça física

No diapositivo: título oficial, autor, orientador, curso e uma imagem própria dos protótipos. Confirmar a identificação institucional antes da exportação final. Usar a Figura 27, 28 ou 29 como ponto de partida visual, mantendo a identificação dos modelos.

Abertura proposta para ensaio:

> Este projeto investiga como o design de produto pode organizar a configuração preliminar de modelos de mão protésica destinados à impressão 3D. Desenvolvi o HandFab para configurar modelos paramétricos a partir de referências antropométricas. A plataforma permite também solicitar sugestões iniciais de inteligência artificial. A investigação acompanhou esse percurso até à preparação para impressão e à observação e medição de peças físicas. Vou apresentar as decisões tomadas e a aprendizagem obtida ao verificar os seus efeitos.

### 2. O que motivou o desenvolvimento do projeto?

A motivação parte das dificuldades de acesso a próteses adaptadas às necessidades das pessoas, particularmente em contextos de baixos e médios rendimentos. O custo é uma barreira, a que se juntam a disponibilidade de técnicos, a adaptação e a manutenção dos dispositivos.

A impressão 3D e os modelos abertos oferecem possibilidades de produção e modificação. Mas disponibilizar um ficheiro não resolve a forma de o ajustar. Muitos modelos exigem alterações manuais, conhecimento de modelação e decisões que nem sempre ficam documentadas.

Foi esta dificuldade que motivou o desenvolvimento do HandFab: organizar a passagem das medidas para modelos configuráveis e verificar o efeito das escolhas até à peça física.

O projeto explora uma base técnica para apoiar esse percurso. A redução de custos e a melhoria do acesso nesses contextos continuam por avaliar.

Base: secções 1.1–1.2 e Lacuna 5 do estado da arte. Apresentar as barreiras de acesso como motivação, sem atribuir ao projeto uma redução de custos ou uma implantação em países de baixos rendimentos.

### 3. Como passar de uma medida a uma peça?

Mostrar uma cadeia curta: medida de entrada, parâmetro, regra geométrica e dimensão da peça. Explicar que o nome de um parâmetro pode sugerir uma correspondência direta que a arquitetura geométrica não assegura.

Base: 1.2, 4.3 e 4.4. Mostrar o problema através de um modelo utilizado no projeto; evitar abrir com uma longa classificação de próteses. Os custos e o acesso são parte do enquadramento, não resultados de redução de custos demonstrados pelo protótipo.

### 4. Perguntas de investigação e âmbito da avaliação

Apresentar os três eixos em forma abreviada, identificados como síntese das perguntas aprovadas: configuração e controlo; avaliação e possibilidade de reproduzir resultados; requisitos e experiência humana. Manter a formulação integral num diapositivo de apoio.

Perguntas aprovadas:

1. «Como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo sobre as decisões de projeto?»
2. «Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a possibilidade de reproduzir os resultados de próteses impressas em 3D?»
3. «Como é que o design industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?»

Explicar oralmente: a avaliação incidiu na configuração, na propagação dos parâmetros, na exportação e na verificação técnica e dimensional. O estudo não incluiu participantes. A eficácia protésica e a experiência de utilização quotidiana ficaram por avaliar.

### 5. Objetivo geral e objetivos específicos

Apresentar o objetivo geral e os sete objetivos específicos da secção 1.3. Distinguir o conhecimento produzido através do design das tarefas de organização dos dados, adaptação dos modelos, integração da plataforma e delimitação da IA. Fechar com a avaliação técnica e a identificação das condições para estudos posteriores. O diapositivo contém uma síntese dos sete pontos, sem alterar o âmbito do manuscrito.

### 6. Como organizei a investigação e o desenvolvimento

Organizei a investigação através do projeto, ou Research Through Design. Construir o HandFab permitiu-me examinar decisões de configuração e aprender com os efeitos observados nos modelos e nas peças.

O Double Diamond ajudou a organizar esse percurso. Na descoberta, explorei a literatura, os modelos e as necessidades. Na definição, delimitei o problema, os requisitos e o que conseguiria avaliar. O desenvolvimento reuniu a adaptação dos modelos e a plataforma. A entrega incluiu exportações, protótipos e verificação dos resultados.

Estes momentos admitiam regressos. No Paraglider, os ensaios mostraram que a palma não acompanhava a escala esperada. Procurei a causa, alterei a regra e voltei a examinar a geometria.

A aprendizagem está nessa relação documentada entre problema, decisão e resultado. A pesquisa bibliográfica e as ferramentas de IA apoiaram o percurso, como explico a seguir.

Research Through Design enquadra a produção de conhecimento através do desenvolvimento e da análise do artefacto. O Double Diamond organiza a exploração e a convergência das decisões. Não são métodos equivalentes. No exemplo do Paraglider, o requisito era propagar a largura introduzida para a palma. A alteração do ponto de aplicação da escala modificou o resultado geométrico. Os registos permitem relacionar a alteração com o resultado e compreender uma restrição do modelo. A Tabela 4 documenta outros ciclos.

### 7. Como integrei a IA na investigação

A IA teve dois papéis no projeto.

Durante a investigação, usei o Elicit para apoiar a pesquisa e agregar bibliografia por tema. Recorri também ao ChatGPT, ao Codex e ao Claude no apoio à organização da informação, à escrita e revisão e ao desenvolvimento e depuração de código. Este uso está declarado no manuscrito.

Dentro do HandFab, a IA constitui uma componente estudada: propõe valores iniciais para parâmetros existentes, que podem ser revistos antes de gerar a geometria.

Em ambos os casos, mantive a responsabilidade pela seleção do que utilizo e pela verificação dos resultados. No caso da bibliografia, isso exige voltar às publicações que sustentam as afirmações.

### 8. Elicit: da pergunta à bibliografia organizada

No Elicit, parti de perguntas ligadas a secções do manuscrito. Fiz pesquisas dirigidas e usei relatórios para aprofundar temas e reunir referências relacionadas. As sínteses ajudaram a organizar a leitura e a identificar trabalhos a examinar.

Um exemplo é a pesquisa sobre o papel da IA. Precisava de distinguir os estudos sobre controlo da prótese, como o reconhecimento de movimentos, dos estudos sobre configuração e tradução de dados antropométricos em parâmetros. Os registos mostram resultados fora do foco, incluindo próteses dentárias, que exigiram avaliação de pertinência.

A agregação não terminava na lista devolvida. Era necessário consultar as publicações, conferir o que sustentavam e selecionar a informação relevante para a síntese crítica.

Guardei localmente as perguntas, resultados, relatórios e listas de fontes, com notas organizadas por secção. Assim, a bibliografia e as razões da seleção permanecem consultáveis para além da ferramenta.

O pacote da secção 6.1 conserva pesquisas dirigidas e um relatório de síntese. A pesquisa 03 regista a presença de resultados de próteses dentárias e de trabalhos centrados no controlo, mostrando por que foi necessário filtrar a pertinência. As sessões locais incluem listas de fontes em CSV ou XLSX, textos e exportações, consoante o material disponível. A conferência dos originais evita atribuir à literatura uma conclusão que só aparece numa síntese automática. Posso mostrar estes registos se me pedirem um exemplo. A utilização do Elicit, por si só, não transforma toda a revisão numa revisão sistemática; só devo atribuir esse estatuto a procedimentos efetivamente documentados.

### 9. Como a literatura orienta o projeto

Destacar Cross, Frayling e Zimmerman, Fischer, Manero e Cabibihan pela função no argumento: conhecimento de design, investigação através do projeto, modificação de sistemas e avaliação de próteses. As obras foram selecionadas pela sua utilidade para justificar as opções do projeto e interpretar os resultados. Não afirmar participação ou codesign a partir da simples existência de parâmetros editáveis.

### 10. HandFab: um percurso com decisões explícitas

Mostrar o catálogo real com quatro modelos e explicar como se inicia a configuração. O utilizador base pode ser qualquer pessoa, com cargos técnicos para moderação e apoio às escolhas. As capturas seguintes desenvolvem o percurso até à exportação.

### 11. Fontes antropométricas e critérios de utilização

Apresentar Gordon et al. (1989; 2014), distinguindo ANSUR 1988 e ANSUR II; DINED, com kima1993, geron1998 e dined2004; e ISO 7250-1:2017, para definições das medidas. Explicar as funções próprias de cada fonte. A norma não certifica os dados nem estabelece adequação individual.

Mostrar o formulário de criação de um perfil, apontando para os campos de origem e de medição.

### 12. Da base consolidada aos perfis do HandFab

Mostrar a sequência: estudos originais, base local consolidada, perfis na aplicação. Os CSV registam indicadores estatísticos com proveniência. Média e desvio-padrão da mesma medida são duas linhas; não são duas pessoas. Os 100 perfis são o estado documentado da aplicação: 97 importados em lote, dois por CSV e um criado manualmente. As contagens de linhas não equivalem às de perfis. A base ANSUR completa e o seu subconjunto não devem ser somados como fontes independentes. O Suplemento 1 e a secção 4.2 sustentam esta distinção.

Usar a captura da tabela de perfis da aplicação e a contagem resumida ao lado.

### 13. Cada modelo exige regras próprias

Caso principal: correção da escala da palma no Paraglider. Mostrar a mesma configuração antes/depois apenas se existirem imagens ou malhas históricas comparáveis; não reconstruir uma imagem como se fosse evidência original. As fotografias selecionadas identificam os modelos e ilustram o trabalho. A correção da escala é explicada a partir dos registos; as fotografias não são apresentadas como antes/depois.

Caso complementar: no UnLimbited Phoenix, a largura da palma tem um limite mínimo de cerca de 82 mm. Um perfil menor não implica uma peça com essa largura. Mostrar a consequência para a configuração e para a mensagem ao utilizador.

Base: 4.4, 8.3, Tabelas 28 a 29 e Anexo C. Na versão de 20 minutos, desenvolver o Paraglider e resumir o Phoenix numa frase.

### 14. A IA propõe um ponto de partida

Mostrar a captura existente do painel de assistência de IA. Apontar para a introdução do pedido e explicar a necessidade de revisão dos valores. A captura não documenta uma nova execução do serviço. Explicar como se verifica o formato da resposta e o efeito dos valores no modelo. A adequação anatómica exige uma avaliação própria.

A lateralidade é um exemplo forte: uma decisão crítica foi separada da sugestão probabilística e passou para uma regra determinística. O manuscrito refere cinco execuções no primeiro conjunto experimental; não transformar esse resultado numa taxa geral de precisão. As respostas simuladas usadas em ensaios de recuperação constituem outro conjunto de evidência.

### 15. Configuração e pré-visualização no HandFab

Mostrar em grande os controlos à esquerda e a geometria à direita. Relacionar um parâmetro com a forma gerada. A sequência usa capturas documentadas; não pressupõe uma demonstração ao vivo. As opções de cor e a exportação têm agora diapositivos próprios.

### 16. Escolher cores e materiais no HandFab

Mostrar a captura das opções de cor e material com a pré-visualização. Apontar para os componentes coloridos e explicar o espaço de escolha que a interface oferece. A aceitação dessas opções precisa de avaliação com utilizadores.

### 17. Da geometria gerada à exportação

Mostrar o código e a pré-visualização com o comando de exportação. Explicar a passagem da malha para o programa de preparação da impressão. Evitar ler código durante a exposição.

### 18. A avaliação acompanhou etapas diferentes

Mostrar as fotografias das peças na placa de impressão e da palma impressa. Explicar oralmente as verificações da plataforma, das sugestões de IA, da geometria e das peças físicas.

Distinguir a Série A, com quatro projetos em condições diferentes, da Série B, com 12 casos numa condição digital comum. A comparação física contém 72 medições dimensionais, uma leitura por eixo e peça/material. Não são 72 participantes ou 72 repetições da mesma medição.

### 19. Comparar peças de diferentes perfis

Mostrar as fotografias originais das séries Flexy Beast e Paraglider. As marcações correspondem aos perfis de referência de 8, 15, 28 e 70 anos. Observar a variação entre peças e preparar a leitura do gráfico dimensional.

### 20. Peça e malha: diferenças medidas, com limites

As séries físicas são mostradas no diapositivo anterior. Usar o gráfico calculado a partir de `comparacao_dimensional_72_medicoes.csv`. O gráfico apresenta a amplitude dos desvios por modelo e material, reunindo os eixos e perfis de cada grupo. Comparar a medida de entrada com a extensão da malha. Explicar depois como foi medida a peça física.

Os desvios físicos face à malha são descritivos; não se estimou a incerteza por repetição. O processamento dos 12 casos da Série B gerou trajetórias, com avisos em alguns casos. Os valores produzidos pelo programa, incluindo tempo, massa e custo, são estimativas de preparação para impressão.

### 21. Phoenix: uma montagem observada em bancada

Mostrar a montagem completa e o pormenor da articulação. Existe um registo de bancada de um espécime PLA configurado para o perfil de 15 anos. Explicar o movimento manual observado e a substituição de elásticos. O número de ciclos não foi registado e não foram realizados os ensaios com cilindros. A idade identifica o perfil, sem um participante com essa idade.

### 22. O contributo para a configuração do produto

Usar uma versão reduzida da Tabela 31, com uma linha por pergunta e duas colunas: evidência obtida e dimensão ainda não avaliada.

- Pergunta 1: configuração editável e controlo das sugestões demonstrados; conforto e adequação funcional individual não avaliados.
- Pergunta 2: os métodos permitiram verificação técnica e comparação dimensional descritiva. A eficácia protésica e a durabilidade exigem outros ensaios, bem como estudos de usabilidade com participantes.
- Pergunta 3: requisitos traduzidos em opções de configuração e regras de controlo. A experiência de utilização quotidiana permanece por estudar, incluindo a aceitação e as implicações para a dignidade e autonomia.

Explicar o conhecimento obtido ao verificar as regras de cada modelo. Usar um caso concreto para mostrar como essa aprendizagem condiciona as opções de configuração e a revisão das sugestões de IA. Não afirmar originalidade absoluta relativamente a toda a literatura.

### 23. As regras de cada modelo condicionam o resultado

Fecho proposto:

> O projeto permitiu construir e examinar um percurso de configuração que liga dados antropométricos, parâmetros, geometria e peças físicas. Os ensaios mostraram que a personalização depende das regras de cada modelo e da verificação dos seus efeitos. A IA apoiou a sugestão inicial de valores, mantendo as decisões críticas sob regras explícitas e revisão humana. O passo seguinte é aprofundar a caracterização física e avaliar o processo com os grupos de utilizadores previstos. O contributo deste trabalho é a base técnica e metodológica documentada para desenvolver essa investigação.

## Diapositivos de apoio

- 24. Perguntas de investigação aprovadas.
- 25. Os números representam conjuntos diferentes.
- 26. Valores registados: amplitude por grupo.
- 27. As falhas também definem o próximo passo.
- 28. Repetição e acessibilidade: resultados delimitados.
- 29. Referências: design e investigação.
- 30. Referências: próteses e antropometria.
