# As minhas notas para a defesa

Versão 1.6. 25/10/2026. Pedro Miguel Candeias da Silva. Mestrado em Design e Desenvolvimento de Produto, Universidade Politécnica do Cávado e do Ave (UPCA).

Estas notas ajudam-me a ensaiar e a acompanhar os 30 diapositivos. Termino a exposição no diapositivo 23. Os restantes ficam para a discussão, conforme as perguntas do júri.

Em **O que quero dizer**, tenho uma proposta de fala que posso adaptar ao meu ritmo. **Se precisar de desenvolver** guarda explicações para o ensaio mais longo ou para uma pergunta. **Lembrar-me** contém apontamentos pessoais que não leio ao júri.

Os tempos são referências para o ensaio de 20 minutos e para a preparação de 30 minutos. Tenho de os confirmar a falar, com tempo para explicar as imagens. Quero manter uma linguagem direta, sem frases de efeito nem enumerações forçadas.

Base anterior, preservada nos restantes blocos: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`, confrontado com os registos dos suplementos. O PDF `a30759_pedro-candeias-projeto-mestrado-mdddp-ipca-v10060211.pdf` é a referência de paginação. O manuscrito permanece inalterado. Os critérios de seleção das referências estão no README da apresentação.

As perguntas aprovadas mantêm a formulação original no diapositivo 24. Os sete objetivos estão no diapositivo 5.


A motivação e a metodologia foram conferidas no ODT `…23102026-1047.odt` e no arquivo local `material/investigacao/elicit/`. A abertura apresenta as barreiras de acesso como motivação para desenvolver o projeto; os seus efeitos socioeconómicos não foram medidos.

## 01. Da medida à peça física

Tempo previsto: 0:35 no percurso principal; 0:40 no treino desenvolvido.

### O que quero dizer

Bom dia. Sou o Pedro Candeias e este é o projeto que desenvolvi com a orientação do Doutor Demétrio Matos.

Quis perceber como podemos configurar uma mão protésica para impressão 3D e verificar se as escolhas feitas no ecrã chegam à peça como esperamos. Para estudar isso, desenvolvi o HandFab, com modelos paramétricos e apoio de inteligência artificial. Vou mostrar algumas decisões que tomei e o que aprendi ao testar o resultado.

### Se precisar de desenvolver

Posso começar pela fotografia. É uma montagem feita durante o projeto e ajuda-me a mostrar logo a ligação entre a configuração no ecrã e a peça física.

### Lembrar-me

Começar com calma e olhar para o júri. O título já está no ecrã; posso passar diretamente ao que quis estudar. Ajustar a saudação à hora da prova.

## 02. O que motivou o desenvolvimento do projeto?

Tempo previsto: 1:15 no percurso principal; 1:50 no treino desenvolvido.

### O que quero dizer

A motivação parte das dificuldades de acesso a próteses adaptadas às necessidades das pessoas, particularmente em contextos de baixos e médios rendimentos. O custo é uma barreira, a que se juntam a disponibilidade de técnicos, a adaptação e a manutenção dos dispositivos.

A impressão 3D e os modelos abertos oferecem possibilidades de produção e modificação. Mas disponibilizar um ficheiro não resolve a forma de o ajustar. Muitos modelos exigem alterações manuais, conhecimento de modelação e decisões que nem sempre ficam documentadas.

Foi esta dificuldade que motivou o desenvolvimento do HandFab: organizar a passagem das medidas para modelos configuráveis e verificar o efeito das escolhas até à peça física.

O projeto explora uma base técnica para apoiar esse percurso. A redução de custos e a melhoria do acesso nesses contextos continuam por avaliar.

### Se precisar de desenvolver

A secção 1.1 associa a motivação aos obstáculos de custo, adaptação anatómica e dependência de técnicos especializados. A Lacuna 5 do estado da arte acrescenta as dificuldades de durabilidade, manutenção e infraestrutura em contextos de baixos e médios rendimentos. Isto ajuda-me a explicar por que razão desenvolver um processo de configuração mais explícito é relevante. Não fiz uma implantação nesses países nem uma comparação económica que permita afirmar uma melhoria de acesso. O apoio técnico e clínico continua necessário.

### Lembrar-me

Começar pela necessidade que motivou o desenvolvimento. Ligar as barreiras de acesso à possibilidade de configurar modelos abertos. Apresentar o HandFab como resposta de investigação ao problema delimitado. Não atribuir o projeto a uma experiência pessoal nem anunciar uma redução de custos demonstrada.

## 03. Como passar de uma medida a uma peça?

Tempo previsto: 1:00 no percurso principal; 1:10 no treino desenvolvido.

### O que quero dizer

O ponto de partida é simples: introduzo uma largura e espero obter uma peça com uma dimensão correspondente. O problema está no que acontece entre esses dois momentos.

O valor entra num parâmetro e passa pelas regras do modelo. Uma regra pode aumentar a mão inteira. Outra pode alterar só uma parte. Preciso de perceber qual destas situações estou a controlar.

Há ainda uma diferença importante entre medir uma mão e medir a dimensão exterior de uma peça. Mesmo que ambos os valores estejam em milímetros, podem representar coisas diferentes.

Foi aqui que situei o problema de design: definir o que pode ser alterado e verificar o efeito dessa escolha. Quem usa a configuração precisa de perceber até onde o modelo consegue responder ao pedido.

### Se precisar de desenvolver

Se precisar de um exemplo, usar a largura e o comprimento:

→ Posso querer aumentar só a largura, mas a regra do modelo também aumentar o comprimento. Tenho de decidir se essa ligação faz sentido e explicar o efeito a quem configura.

### Lembrar-me

Apontar primeiro para os controlos do HandFab e depois para os dedos impressos. Este exemplo prepara o caso do Paraglider, mais à frente.

## 04. Perguntas de investigação e âmbito da avaliação

Tempo previsto: 0:40 no percurso principal; 1:00 no treino desenvolvido.

### O que quero dizer

As perguntas orientaram a personalização com controlo sobre as decisões, a avaliação dos resultados e a relação entre requisitos do produto e experiência das pessoas.

A primeira articula design, parametrização e IA. A segunda pergunta como examinar a eficácia, a usabilidade, a durabilidade e a reprodução dos resultados. A terceira inclui a aceitação, a dignidade e a autonomia.

A resposta empírica ficou na configuração e na verificação técnica e dimensional. A experiência de utilização e o desempenho clínico exigem estudos com participantes. As perguntas integrais estão nos diapositivos de apoio.

### Se precisar de desenvolver

Se me perguntarem qual é a diferença entre verificar o funcionamento técnico e avaliar a experiência de utilização, posso explicar com um exemplo: medir uma peça permite comparar as suas dimensões com as da malha digital. Para perceber se é confortável, preciso de observar a sua utilização e ouvir a pessoa que a usa. Na interface, os testes verificam se a tarefa é executada. Para perceber se os controlos são fáceis de compreender, preciso de observar pessoas a realizar essa tarefa.

### Lembrar-me

Dizer claramente onde ficou o estudo e seguir em frente. Não preciso de repetir a lista de limitações em todos os diapositivos. Se pedirem a formulação exata de uma pergunta, ir ao diapositivo 24.

## 05. Objetivo geral e objetivos específicos

Tempo previsto: 1:05 no percurso principal; 1:50 no treino desenvolvido.

### O que quero dizer

O objetivo geral foi produzir conhecimento através do desenvolvimento e da avaliação técnica de um sistema paramétrico com apoio de IA para configurar modelos de mão protésica.

Os sete objetivos específicos orientaram esse trabalho: compreender a tradução das necessidades em decisões de design; organizar os dados antropométricos com a sua origem; adaptar modelos abertos; integrar a configuração numa plataforma web; delimitar o papel da IA; examinar a coerência entre dados, geometria e peças; e identificar as condições necessárias para uma avaliação posterior com utilizadores.

Vou mostrar como estas tarefas se articularam no processo de investigação e nas decisões tomadas no HandFab.

### Se precisar de desenvolver

Posso ligar um objetivo a uma decisão concreta. Ao organizar os dados, tive de conservar a origem de cada valor para conseguir interpretá-lo na configuração. Ao adaptar os modelos, precisei de tornar as regras explícitas para verificar o efeito desses valores. É essa ligação que os objetivos me ajudam a acompanhar.

### Lembrar-me

Apresentar o objetivo geral antes de percorrer a lista. Seguir a numeração da coluna esquerda para a direita. Estes pontos resumem a secção 1.3 do manuscrito; os resultados vêm depois.

## 06. Como organizei a investigação e o desenvolvimento

Tempo previsto: 1:20 no percurso principal; 2:05 no treino desenvolvido.

### O que quero dizer

Organizei a investigação através do projeto, ou Research Through Design. Construir o HandFab permitiu-me examinar decisões de configuração e aprender com os efeitos observados nos modelos e nas peças.

O Double Diamond ajudou a organizar esse percurso. Na descoberta, explorei a literatura, os modelos e as necessidades. Na definição, delimitei o problema, os requisitos e o que conseguiria avaliar. O desenvolvimento reuniu a adaptação dos modelos e a plataforma. A entrega incluiu exportações, protótipos e verificação dos resultados.

Estes momentos admitiam regressos. No Paraglider, os ensaios mostraram que a palma não acompanhava a escala esperada. Procurei a causa, alterei a regra e voltei a examinar a geometria.

A aprendizagem está nessa relação documentada entre problema, decisão e resultado. A pesquisa bibliográfica e as ferramentas de IA apoiaram o percurso, como explico a seguir.

### Se precisar de desenvolver

Research Through Design enquadra a produção de conhecimento através do desenvolvimento e da análise do artefacto. O Double Diamond organiza a exploração e a convergência das decisões. Não são métodos equivalentes. No exemplo do Paraglider, o requisito era propagar a largura introduzida para a palma. A alteração do ponto de aplicação da escala modificou o resultado geométrico. Os registos permitem relacionar a alteração com o resultado e compreender uma restrição do modelo. A Tabela 4 documenta outros ciclos.

### Lembrar-me

Percorrer as quatro fases no esquema e terminar no ciclo inferior. Usar o Paraglider como exemplo breve. A avaliação realizada é técnica e dimensional; não apresentar a fase de entrega como implantação clínica ou comercial.

## 07. Como integrei a IA na investigação

Tempo previsto: 0:55 no percurso principal; 1:25 no treino desenvolvido.

### O que quero dizer

A IA teve dois papéis no projeto.

Durante a investigação, usei o Elicit para apoiar a pesquisa e agregar bibliografia por tema. Recorri também ao ChatGPT, ao Codex e ao Claude no apoio à organização da informação, à escrita e revisão e ao desenvolvimento e depuração de código. Este uso está declarado no manuscrito.

Dentro do HandFab, a IA constitui uma componente estudada: propõe valores iniciais para parâmetros existentes, que podem ser revistos antes de gerar a geometria.

Em ambos os casos, mantive a responsabilidade pela seleção do que utilizo e pela verificação dos resultados. No caso da bibliografia, isso exige voltar às publicações que sustentam as afirmações.

### Se precisar de desenvolver

Posso distinguir uma síntese usada para localizar referências de uma afirmação fundamentada num artigo. A primeira ajuda a orientar a pesquisa; a segunda exige examinar a fonte e os seus limites. Também distingo o código produzido com apoio de IA do comportamento verificado nos ensaios. Não quantifiquei ganhos de produtividade atribuíveis a estas ferramentas.

### Lembrar-me

Apresentar as ferramentas pelas tarefas em que apoiaram o trabalho. O Elicit recebe um exemplo no diapositivo seguinte. Os pormenores da IA dentro do HandFab são desenvolvidos mais adiante.

## 08. Elicit: da pergunta à bibliografia organizada

Tempo previsto: 1:30 no percurso principal; 2:30 no treino desenvolvido.

### O que quero dizer

No Elicit, parti de perguntas ligadas a secções do manuscrito. Fiz pesquisas dirigidas e usei relatórios para aprofundar temas e reunir referências relacionadas. As sínteses ajudaram a organizar a leitura e a identificar trabalhos a examinar.

Um exemplo é a pesquisa sobre o papel da IA. Precisava de distinguir os estudos sobre controlo da prótese, como o reconhecimento de movimentos, dos estudos sobre configuração e tradução de dados antropométricos em parâmetros. Os registos mostram resultados fora do foco, incluindo próteses dentárias, que exigiram avaliação de pertinência.

A agregação não terminava na lista devolvida. Era necessário consultar as publicações, conferir o que sustentavam e selecionar a informação relevante para a síntese crítica.

Guardei localmente as perguntas, resultados, relatórios e listas de fontes, com notas organizadas por secção. Assim, a bibliografia e as razões da seleção permanecem consultáveis para além da ferramenta.

### Se precisar de desenvolver

O pacote da secção 6.1 conserva pesquisas dirigidas e um relatório de síntese. A pesquisa 03 regista a presença de resultados de próteses dentárias e de trabalhos centrados no controlo, mostrando por que foi necessário filtrar a pertinência. As sessões locais incluem listas de fontes em CSV ou XLSX, textos e exportações, consoante o material disponível. A conferência dos originais evita atribuir à literatura uma conclusão que só aparece numa síntese automática. Posso mostrar estes registos se me pedirem um exemplo. A utilização do Elicit, por si só, não transforma toda a revisão numa revisão sistemática; só devo atribuir esse estatuto a procedimentos efetivamente documentados.

### Lembrar-me

Percorrer o esquema da pergunta até à síntese. Dar o exemplo da distinção entre controlo e configuração. Explicar o trabalho de seleção e verificação do investigador. Não apresentar contagens de pesquisas ou estudos como um processo PRISMA consolidado, nem prometer que todas as fontes sugeridas foram incluídas.

## 09. Como a literatura orienta o projeto

Tempo previsto: 0:40 no percurso principal; 0:50 no treino desenvolvido.

### O que quero dizer

A bibliografia selecionada ajudou a fundamentar decisões. Cross enquadra o conhecimento de design; Frayling e Zimmerman ajudam a discutir a aprendizagem através do artefacto.

Fischer permite examinar as condições de modificação do sistema. Manero e Cabibihan contextualizam as próteses impressas em 3D e a necessidade de avaliar os dispositivos.

Ligo estas obras à função que têm no argumento. Os estudos citados não avaliaram o HandFab, e a existência de parâmetros editáveis não demonstra participação de utilizadores.

### Se precisar de desenvolver

Se me perguntarem por um autor, voltar à função que tem neste argumento. Posso usar Zimmerman para explicar por que preciso de analisar o que aprendi ao construir o protótipo. Com Fischer, posso discutir as condições de modificação do sistema. Evitar atribuir a estas obras uma avaliação do HandFab que elas não fizeram.

### Lembrar-me

Não ler a tabela como uma lista de nomes. Ligar cada referência à ideia que me ajuda a explicar. A ordem da exposição é uma escolha para esta apresentação; não preciso de inventar uma história sobre quando conheci cada autor.

## 10. HandFab: um percurso com decisões explícitas

Tempo previsto: 0:45 no percurso principal; 0:55 no treino desenvolvido.

### O que quero dizer

Aqui está o HandFab que desenvolvi. Começo pela escolha do modelo. Estão disponíveis quatro modelos, cada um com as suas regras de configuração.

A partir daqui, posso trabalhar com uma referência antropométrica ou ajustar os valores. A IA pode ajudar a propor um ponto de partida. Continuo a poder rever os parâmetros antes de gerar e exportar a geometria.

Pensei no utilizador base como qualquer pessoa. Os cargos técnicos permitem moderar e apoiar as suas escolhas. A forma como esse apoio funciona na prática fica para a avaliação com utilizadores.

### Se precisar de desenvolver

Se houver dúvidas sobre a IA, esclarecer que o seu uso é opcional e depende de um serviço externo. O sistema já tem modelos e parâmetros definidos. A IA sugere valores para esses parâmetros. Isso permite-me separar a análise da sugestão da análise da geometria gerada pelo modelo.

### Lembrar-me

Mostrar os quatro modelos no catálogo. Explicar o percurso enquanto aponto para o modelo escolhido. Reservar os detalhes de configuração para as capturas seguintes.

## 11. Fontes antropométricas e critérios de utilização

Tempo previsto: 0:45 no percurso principal; 1:05 no treino desenvolvido.

### O que quero dizer

Usei fontes antropométricas como referência inicial para a configuração. Os levantamentos ANSUR de 1988 e ANSUR II são distintos, tal como os conjuntos kima1993, geron1998 e dined2004 da DINED.

A ISO 7250-1 ajuda a definir as medidas e os pontos anatómicos. Para interpretar um valor, conservei a população, a idade, a unidade, a estatística e o protocolo de origem.

Uma referência populacional não substitui a medição da pessoa. Também preciso de verificar se o parâmetro do modelo corresponde à medida descrita pela fonte.

### Se precisar de desenvolver

Se surgir uma dúvida sobre percentis, explicar com o percentil cinquenta: metade dos valores fica de cada lado. As medidas de uma pessoa não têm de corresponder todas ao mesmo percentil. Posso também comparar uma população militar adulta com uma população infantil para mostrar por que a origem dos dados importa. A citação da norma não garante que todos os estudos tenham usado o mesmo protocolo.

### Lembrar-me

Apontar para os campos do formulário, sobretudo a origem e a unidade. Relacionar cada valor com a população e a medida de onde veio. As referências completas estão no diapositivo 30.

## 12. Da base consolidada aos perfis do HandFab

Tempo previsto: 0:45 no percurso principal; 1:05 no treino desenvolvido.

### O que quero dizer

Na plataforma documentada existiam 100 perfis: 97 importados em lote, dois por CSV e um criado manualmente.

A tabela permite consultar e editar referências antropométricas. A contribuição do projeto está na organização dos dados e na sua ligação à configuração, conservando a origem e o significado dos valores.

Estes perfis são referências estatísticas. Não correspondem a 100 participantes do estudo, nem a uma única população. As diferentes vias de entrada também impedem tratar cada linha dos ficheiros de origem como um perfil automaticamente equivalente.

### Se precisar de desenvolver

Se me perguntarem pelos ficheiros, lembrar que o subconjunto ANSUR repete parte da extração completa. Somar as linhas dos dois daria uma contagem enganadora. A compilação multipopulacional tem 1790 linhas, das quais 852 são DINED. Estes números contam registos estatísticos. Os cem perfis referem-se ao estado documentado da aplicação.

### Lembrar-me

Apontar para a tabela de perfis e explicar a contagem ao lado. Os 100 perfis são o estado documentado da aplicação; as linhas das bases estatísticas representam outra coisa.

## 13. Cada modelo exige regras próprias

Tempo previsto: 1:00 no percurso principal; 1:25 no treino desenvolvido.

### O que quero dizer

O Paraglider e o Phoenix mostraram limites diferentes.

No Paraglider, os dedos respondiam à configuração, mas a palma mantinha a escala interna da biblioteca. Corrigi o ponto de aplicação da escala e verifiquei a resposta geométrica.

No Phoenix, a largura fica limitada a cerca de 82 milímetros. Pedir menos mantém o modelo nesse mínimo, pelo que a dimensão pretendida fica por satisfazer.

Estes casos mostram por que precisei de examinar as regras de cada modelo e tornar explícitas as restrições da configuração. Os modelos de origem mantêm a autoria dos seus criadores.

### Se precisar de desenvolver

Lembrar que os modelos já existiam e mantêm a autoria dos seus criadores. O meu trabalho foi integrá-los e verificar as relações usadas no HandFab. Os oitenta e dois milímetros dizem respeito ao Phoenix que examinei. Numa revisão futura, posso estudar como assinalar esse limite e orientar a escolha de outro modelo quando o pedido fica fora da cobertura.

### Lembrar-me

Usar as fotografias para identificar os modelos. Explicar a correção da palma e o limite de largura a partir dos registos, sem apresentar estas imagens como uma comparação histórica antes e depois.

## 14. A IA propõe um ponto de partida

Tempo previsto: 0:55 no percurso principal; 1:25 no treino desenvolvido.

### O que quero dizer

Aqui está o papel que dei à IA: receber uma descrição e sugerir valores para parâmetros que o sistema já conhece. Quem configura pode rever a proposta antes de a aplicar.

No primeiro conjunto de ensaios reais, as cinco respostas cumpriram o formato esperado. O percurso funcionou nessas condições. Para saber se os valores são adequados a uma pessoa, seria necessária outra avaliação.

Uma decisão concreta foi retirar a lateralidade da inferência. A escolha entre mão esquerda e direita passou a seguir uma regra explícita e ficou fora do pedido de sugestões.

O que estudei foi a integração desta proposta editável no percurso. Não fiz uma comparação experimental com a configuração manual que permitisse afirmar uma vantagem de tempo ou de qualidade.

### Se precisar de desenvolver

Se me perguntarem pela qualidade da resposta, separar o formato dos valores. Conseguir ler a resposta é uma verificação. Saber que efeito os valores têm no modelo exige examinar a geometria. A adequação à utilização terá de ser estudada depois.

### Lembrar-me

Apontar para a caixa do pedido e para o botão de sugestão. A imagem mostra a interface documentada. Explicar oralmente a revisão dos valores e a regra da lateralidade.

## 15. Configuração e pré-visualização no HandFab

Tempo previsto: 0:45 no percurso principal; 1:10 no treino desenvolvido.

### O que quero dizer

Aqui consigo mostrar melhor os controlos da configuração. Tenho os parâmetros do lado esquerdo e a pré-visualização do modelo do lado direito.

O que me interessa explicar é a ligação entre um valor e a forma que aparece. Posso rever os valores e gerar novamente a geometria para examinar o resultado. Foi ao comparar estas alterações que encontrei diferenças importantes nas regras dos modelos.

Esta sequência usa capturas guardadas durante o projeto. Para a defesa, ajuda-me a mostrar o percurso sem depender de uma ligação ao serviço de IA.

### Se precisar de desenvolver

Se tiver tempo, percorrer uma alteração pelas imagens: identificar o controlo disponível e explicar o que se deve observar na geometria. Para avaliar a compreensão, posso futuramente pedir a alguém que faça uma alteração e depois lhe perguntar como interpretou o resultado. Aqui estou a usar capturas existentes, sem relatar uma tarefa realizada com participantes.

### Lembrar-me

Apontar para um controlo de dimensão e depois para a pré-visualização. Dar tempo ao júri para observar o modelo. Continuar para as cores e para a exportação.

## 16. Escolher cores e materiais no HandFab

Tempo previsto: 0:20 no percurso principal; 0:30 no treino desenvolvido.

### O que quero dizer

Nesta parte posso escolher as cores dos componentes e ver o resultado no modelo. A interface também reúne opções de material.

Quis dar espaço a escolhas sobre a aparência da prótese. A forma como cada pessoa valoriza essas opções terá de ser estudada com utilizadores.

### Se precisar de desenvolver

Posso usar os dedos com cores diferentes para mostrar que a configuração atua em componentes identificados. A escolha que aparece no ecrã ainda precisa de ser concretizada e verificada na preparação para impressão.

### Lembrar-me

Apontar para uma cor e para o componente correspondente. Deixar a imagem explicar as opções, sem ler a lista de controlos.

## 17. Da geometria gerada à exportação

Tempo previsto: 0:30 no percurso principal; 0:45 no treino desenvolvido.

### O que quero dizer

Depois de rever a configuração, consigo examinar a geometria gerada e exportar a malha. Esta imagem mostra também o código OpenSCAD associado ao modelo.

A exportação permite continuar o trabalho no programa de preparação para impressão. A partir desse momento, entram as escolhas do equipamento e das condições de fabrico. Foi por isso que acompanhei o processo até às peças físicas.

### Se precisar de desenvolver

Se precisar de explicar a diferença, a malha descreve a superfície do objeto. O programa de preparação usa essa geometria para calcular as trajetórias de impressão. As estimativas de tempo ou material pertencem a essa preparação.

### Lembrar-me

Apontar para a pré-visualização e para Export. Evitar ler código ao júri. A imagem seguinte mostra trabalho de impressão já realizado.

## 18. A avaliação acompanhou etapas diferentes

Tempo previsto: 0:50 no percurso principal; 1:05 no treino desenvolvido.

### O que quero dizer

A avaliação acompanhou a plataforma, as sugestões de IA, as malhas e as peças físicas.

Na preparação digital, a Série A reuniu quatro projetos em condições diferentes. A Série B comparou doze casos numa condição comum: três modelos e quatro perfis.

A comparação física reuniu 72 medições, combinando modelos, perfis, eixos e materiais. Fiz uma leitura por combinação.

As fotografias documentam as peças produzidas. Para compreender a correspondência dimensional, comparei as medidas físicas com as malhas exportadas.

### Se precisar de desenvolver

Se houver dúvidas nas contagens, ir ao diapositivo 25. A plataforma tem quatro modelos disponíveis, mas a comparação física principal abrange três. Preciso de manter esta diferença quando explico o alcance dos resultados.

### Lembrar-me

Começar pelas peças na placa e pela palma impressa. Explicar os conjuntos sem confundir projetos de preparação, casos digitais e leituras dimensionais. Os detalhes das contagens estão no diapositivo 25.

## 19. Comparar peças de diferentes perfis

Tempo previsto: 0:40 no percurso principal; 1:00 no treino desenvolvido.

### O que quero dizer

Aqui vê-se melhor o que imprimi para comparar os perfis. À esquerda estão dedos do Flexy Beast. À direita estão os do Paraglider.

As marcações identificam os perfis de referência de 8, 15, 28 e 70 anos. Usei esses perfis para examinar como cada modelo responde a diferentes valores.

As fotografias ajudam a observar a variação entre as peças. Para comparar dimensões, usei os registos de medição que resumo no gráfico seguinte.

### Se precisar de desenvolver

Posso apontar para duas peças da mesma série e explicar que a diferença depende da regra de parametrização. Os perfis são referências para o ensaio, não pessoas que tenham participado no estudo.

### Lembrar-me

Dar alguns segundos para observar as duas séries. Dizer o nome de cada modelo e explicar as marcações. Passar depois ao gráfico, que apresenta os valores medidos.

## 20. Peça e malha: diferenças medidas, com limites

Tempo previsto: 1:15 no percurso principal; 2:00 no treino desenvolvido.

### O que quero dizer

Neste gráfico comparei as dimensões das peças com as dimensões correspondentes da malha exportada.

Cada segmento vai do menor ao maior desvio registado para um modelo e material. Reúne doze valores, relativos a quatro perfis e três eixos. As cores distinguem PLA e PETG.

Calculei a diferença subtraindo a dimensão digital à física. Os valores negativos indicam que medi dimensões físicas inferiores às digitais correspondentes. No conjunto, os desvios vão aproximadamente de menos 0,53 a menos 0,08 milímetros.

Fiz uma leitura por combinação. Por isso, estes registos não permitem estimar a variação de medições repetidas. O intervalo apresentado também não é uma precisão garantida pelo processo.

Como os grupos juntam eixos e dimensões diferentes, o gráfico não permite escolher o melhor material nem identificar uma causa única para as diferenças.

O que retiro daqui é a necessidade de medir o que foi produzido. A avaliação funcional exigiria trabalho adicional, como ajuda a enquadrar a referência de Cabibihan.

### Se precisar de desenvolver

Posso usar o Flexy Beast em PLA como exemplo: os extremos são menos 0,398 e menos 0,108 milímetros. São doze comparações. Se quiser estudar a consistência de uma condição concreta, preciso de repetir as medições e controlar as condições. Tenho a tabela com os extremos no apoio e os registos individuais no CSV.

### Lembrar-me

Mostrar primeiro o zero e depois um segmento. Ler os valores decimais devagar. Não preciso de ler todos os grupos. Se houver uma pergunta sobre uma dimensão concreta, consultar o CSV em vez de tirar uma conclusão geral do intervalo.

## 21. Phoenix: uma montagem observada em bancada

Tempo previsto: 0:45 no percurso principal; 1:10 no treino desenvolvido.

### O que quero dizer

Esta é a Phoenix que montei em PLA, para o perfil de referência de 15 anos. Observei em bancada o movimento manual e o retorno dos dedos. Durante essa montagem, substituí os elásticos.

A fotografia da direita deixa ver melhor a articulação. Foi uma forma de observar como as peças funcionavam em conjunto. Ficou por estudar o comportamento ao longo de uma utilização prolongada, com um protocolo próprio.

### Se precisar de desenvolver

Tenho o registo de um espécime. O número de ciclos não foi registado e os testes com cilindros não foram realizados. Os 15 anos identificam o perfil de configuração; não houve um participante com essa idade. Se me perguntarem pelo uso protésico, explicar que essa avaliação ficou para trabalho futuro.

### Lembrar-me

Apontar para a mão montada e depois para o pormenor da articulação. Dizer o que observei em bancada. Não simular uma demonstração de movimento a partir destas imagens estáticas.

## 22. O contributo para a configuração do produto

Tempo previsto: 1:25 no percurso principal; 2:35 no treino desenvolvido.

### O que quero dizer

O contributo está em organizar escolhas de configuração e examinar o seu efeito na forma.

Para a primeira pergunta, demonstrei um percurso com parâmetros editáveis e revisão das sugestões. O conforto e a adequação individual exigem avaliação própria.

Para a segunda, documentei verificações técnicas e comparações dimensionais. A usabilidade com participantes e a durabilidade permanecem por estudar.

Para a terceira, traduzi requisitos em regras e opções de configuração. A aceitação e os efeitos na autonomia exigem estudos com as pessoas.

Os casos do Paraglider e do Phoenix mostram o conhecimento obtido: cada modelo tem relações e limites próprios. Registar essas condições permite compreender as decisões tomadas e preparar novas avaliações.

### Se precisar de desenvolver

Se me perguntarem se isto se aplica a qualquer prótese, delimitar a resposta aos modelos e condições documentados. Para alargar o trabalho, preciso de novas verificações. A avaliação com pessoas será necessária para perceber se esta organização ajuda a compreender as escolhas durante uma tarefa.

### Lembrar-me

Aqui quero tornar o contributo claro, sem voltar a explicar toda a plataforma. Usar o Paraglider se precisar de um exemplo. Cross ajuda-me a enquadrar o conhecimento de design, e a investigação através do projeto enquadra a aprendizagem obtida com o protótipo.

## 23. As regras de cada modelo condicionam o resultado

Tempo previsto: 0:20 no percurso principal; 0:30 no treino desenvolvido.

### O que quero dizer

O que retiro deste trabalho é que configurar exige conhecer as regras de cada modelo e verificar o seu efeito na peça. O próximo passo é avaliar o HandFab com as pessoas que o irão utilizar. Obrigado.

### Se precisar de desenvolver

Se precisar de desenvolver a conclusão, voltar à relação entre a escolha e o efeito na forma. Os casos examinados ajudam-me a decidir que verificações acrescentar. A experiência das pessoas terá de ser estudada nas tarefas de configuração e na utilização.

### Lembrar-me

Terminar com a fotografia do protótipo e olhar para o júri. Deixar este diapositivo no ecrã durante o início da discussão.

## 24. Perguntas de investigação aprovadas

Diapositivo de apoio à discussão.

### O que quero dizer

Aqui tenho as perguntas aprovadas na formulação completa. Durante a exposição usei versões mais curtas.

A primeira pergunta é: «Como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo sobre as decisões de projeto?»

A segunda é: «Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a possibilidade de reproduzir os resultados de próteses impressas em 3D?»

A terceira é: «Como é que o design industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?»

As minhas respostas dizem respeito à parte técnica e dimensional que consegui estudar. As outras dimensões continuam por avaliar.

### Lembrar-me

Abrir este diapositivo se pedirem a formulação exata de uma pergunta. Ler só a que estiver em discussão e explicar até onde consegui responder. Manter o texto aprovado tal como está.

## 25. Os números representam conjuntos diferentes

Diapositivo de apoio à discussão.

### O que quero dizer

Estes números correspondem a conjuntos diferentes.

Na Série A, preparei quatro projetos em condições distintas. Isso limita as comparações diretas entre equipamentos.

Na Série B, os doze casos resultam de três modelos combinados com quatro perfis, numa condição digital comum. A preparação ficou concluída, com os avisos registados.

As setenta e duas medições combinam três modelos, quatro perfis, três eixos e dois materiais. Houve uma leitura por combinação. Não são setenta e duas repetições da mesma medida.

As idades de oito, quinze, vinte e oito e setenta anos identificam perfis de ensaio. Não tive participantes com essas idades.

### Lembrar-me

Começar pelo número sobre o qual me perguntaram. Se a dúvida for o número de modelos, explicar que havia quatro na plataforma e três na comparação física principal.

## 26. Valores registados: amplitude por grupo

Diapositivo de apoio à discussão.

### O que quero dizer

Esta tabela contém os valores que usei no gráfico. Para cada modelo e material, apresenta o menor e o maior desvio entre a dimensão física e a digital.

No Flexy Beast em PLA, por exemplo, os extremos são menos 0,398 e menos 0,108 milímetros. O grupo reúne doze valores, relativos a quatro perfis e três eixos.

A tabela descreve as medições que fiz. Como não repeti as leituras por combinação, não consigo estimar a incerteza a partir destes dados. Também não defini aqui uma tolerância de aceitação.

Se a pergunta for sobre uma dimensão específica, posso consultar o registo correspondente no CSV.

### Lembrar-me

Usar um grupo para explicar a leitura. Os restantes ficam para consulta conforme a pergunta. Lembrar-me de dizer «desvio observado», sem o transformar numa garantia de precisão.

## 27. As falhas também definem o próximo passo

Diapositivo de apoio à discussão.

### O que quero dizer

Os testes também mostraram falhas que preciso de resolver.

Num ensaio com uma resposta simulada, um valor acima do limite chegou ao estado interno da aplicação. Esse caso mostrou um ponto em que o controlo não estava a funcionar como devia.

Na verificação manual de acessibilidade, cinco dos doze itens falharam. Identifiquei, portanto, barreiras no percurso de interação.

Estes resultados ajudam-me a decidir onde rever o sistema e o que voltar a testar. A robustez global e a acessibilidade continuam por demonstrar; o funcionamento nas condições ensaiadas não chega para as garantir.

### Se precisar de desenvolver

Se me perguntarem pelo valor fora do limite, esclarecer que foi uma resposta preparada para testar o comportamento do sistema. É diferente de uma chamada real à IA. Na acessibilidade, usei critérios e inspeção. Para compreender as dificuldades das pessoas durante uma tarefa, preciso de complementar isso com observação de utilização.

### Lembrar-me

Explicar o efeito de cada falha no desenvolvimento. Não ficar só pela lista de problemas: mostrar o que os registos me permitem rever.

## 28. Repetição e acessibilidade: resultados delimitados

Diapositivo de apoio à discussão.

### O que quero dizer

Nos ensaios de repetição, concluí sete exportações do Flexy Beast, cinco do Paraglider e cinco do Phoenix. Os ficheiros foram idênticos dentro de cada configuração testada. O objetivo de dez exportações por modelo ficou por atingir.

Isto documenta consistência nessas execuções. Para generalizar a outras configurações, teria de as testar.

Na verificação manual de acessibilidade, sete itens foram considerados conformes e cinco falharam. São os resultados da lista examinada, sem uma certificação global de acessibilidade.

No WebKit, o bloqueio de autenticação impediu concluir a avaliação. Esse resultado ficou inconclusivo.

### Lembrar-me

Usar só a parte relevante para a pergunta. No caso do WebKit, explicar o bloqueio encontrado sem o apresentar como prova de incompatibilidade geral.

## 29. Referências: design e investigação

Diapositivo de apoio à discussão.

### O que quero dizer

Tenho aqui as referências que me ajudam a explicar o enquadramento de design e a metodologia.

Cross permite-me discutir o conhecimento produzido através do design. Fischer ajuda-me a pensar nas condições de modificação do sistema. Com Frayling e Zimmerman, enquadro a investigação através do desenvolvimento e análise do artefacto. O Design Council ajuda a explicar a organização do processo.

A seleção foi feita para apoiar o argumento desta apresentação. A revisão completa está no manuscrito.

### Lembrar-me

Ir diretamente ao autor relevante para a pergunta. A entrada completa de Frayling ainda precisa de ser conferida antes da prova. O ano mantém o que está no manuscrito.

## 30. Referências: próteses e antropometria

Diapositivo de apoio à discussão.

### O que quero dizer

Estas são as referências de apoio ao domínio das próteses e aos dados antropométricos.

Manero enquadra a impressão 3D no desenvolvimento de próteses. Cabibihan examina a funcionalidade e a durabilidade de mãos abertas. Gordon documenta os levantamentos antropométricos. Na DINED, identifico os conjuntos consultados, e a ISO 7250-1 ajuda a definir as medidas.

Os dados publicados pertencem a essas fontes. O meu trabalho foi prepará-los para o HandFab e avaliar o percurso implementado. Os registos estão no manuscrito e nos suplementos.

### Lembrar-me

Identificar a fonte que responde à pergunta. A norma ajuda-me a definir as medidas; não garante a conformidade de todos os dados. Para avaliar uma pessoa concreta, os perfis populacionais são apenas uma referência de partida.
