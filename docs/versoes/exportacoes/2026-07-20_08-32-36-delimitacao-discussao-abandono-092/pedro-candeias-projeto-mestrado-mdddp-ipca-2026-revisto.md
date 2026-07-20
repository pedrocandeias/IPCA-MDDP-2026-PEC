Projecto completo

Versão do documento: 0.4.92

## INTEGRAÇÃO DO *DESIGN* E DA INTELIGÊNCIA ARTIFICIAL EM PROCESSOS PARAMÉTRICOS PARA O DESENVOLVIMENTO DE PRÓTESES DE MEMBROS SUPERIORES EM IMPRESSÃO 3D.

## Resumo

A personalização de próteses de membros superiores continua condicionada por custos elevados, competências técnicas especializadas e dificuldades na tradução de dados antropométricos para geometrias configuráveis e fabricáveis. Esta dissertação investiga de que modo o *design* industrial, articulado com modelação paramétrica e inteligência artificial, pode apoiar a configuração preliminar de modelos de mão protésica destinados à impressão 3D. A investigação adopta uma abordagem de *Research Through Design*, combinando revisão crítica da literatura, análise de soluções *open source*, estruturação de uma base local de dados antropométricos, desenvolvimento de modelos em OpenSCAD, integração numa plataforma *web* e avaliação técnica por cenários simulados, exportação de geometrias e prototipagem física. O protótipo de investigação converte descrições e medidas em sugestões paramétricas, apresenta a geometria no navegador e exporta ficheiros nos formatos *Stereolithography* (STL) e *3D Manufacturing Format* (3MF). A avaliação incidiu sobre a conformidade das sugestões com o esquema de parâmetros, a propagação dos valores para a geometria, o funcionamento dos principais módulos da plataforma, a preparação dos ficheiros e a produção de peças físicas. Os ensaios permitiram detectar e corrigir problemas de correspondência de perfis, lateralidade e escala em modelos específicos. Os resultados sustentam a coerência técnica do fluxo nas condições documentadas e mostram limites próprios de cada modelo. Conforto, usabilidade com participantes, eficácia funcional, segurança, durabilidade e adequação clínica ficaram fora da avaliação. O contributo principal reside num processo de investigação através do projecto que articula dados antropométricos, regras geométricas, apoio de IA, execução no navegador e verificação material, mantendo a decisão final sob supervisão humana.

**Palavras-chave:** *design* industrial; próteses de membro superior; *design* paramétrico; inteligência artificial; impressão 3D; dados antropométricos; fabrico digital.

## Abstract

The personalisation of upper-limb prostheses remains constrained by high costs, specialised technical skills, and difficulties in translating anthropometric data into configurable and manufacturable geometries. This dissertation investigates how industrial design, combined with parametric modelling and artificial intelligence, can support the preliminary configuration of prosthetic hand models for 3D printing. The research follows a Research Through Design approach, combining a critical literature review, analysis of open-source solutions, the structuring of a local anthropometric database, development of OpenSCAD models, integration into a web platform, and technical evaluation through simulated scenarios, geometry export, and physical prototyping. The research prototype converts descriptions and measurements into parametric suggestions, displays geometry in the browser, and exports STL and 3MF files. Evaluation covered suggestion compliance with the parameter schema, value propagation into geometry, operation of the main platform modules, file preparation, and production of physical parts. The tests identified and supported corrections to profile matching, laterality, and model-specific scaling. The results support the technical coherence of the workflow under the documented conditions and reveal constraints specific to each model. Comfort, usability with participants, functional effectiveness, safety, durability, and clinical suitability were outside the evaluation scope. The main contribution is a design-research process that connects anthropometric data, geometric rules, AI support, browser execution, and material verification while keeping final decisions under human supervision.

**Keywords:** industrial design; upper-limb prostheses; parametric design; artificial intelligence; 3D printing; anthropometric data; digital fabrication.

## Lista de acrónimos

| Acrónimo | Designação/explicação |

| --- | --- |

| 2D | Bidimensional. |

| 3D | Tridimensional. |

| 3DP | *3D Printing*; impressão 3D. |

| 3MF | *3D Manufacturing Format*; formato de ficheiro para fabrico aditivo. |

| AMS | *Automatic Material System*; sistema automático de alimentação de filamento usado em impressoras Bambu Lab. |

| ANSUR | *Anthropometric Survey of U.S. Army Personnel*; inquérito antropométrico do Exército dos Estados Unidos. |

| API | *Application Programming Interface*; interface de programação de aplicações. |

| ASTM | *American Society for Testing and Materials*; organismo internacional de normalização. |

| CAD | *Computer-Aided Design*; desenho ou projecto assistido por computador. |

| CAM | *Computer-Aided Manufacturing*; fabrico assistido por computador. |

| CE | Conformité Européenne; marcação europeia de conformidade. |

| CSG | *Constructive Solid Geometry*; geometria sólida construtiva. |

| CSV | *Comma-Separated Values*; formato de valores separados por vírgulas. |

| CT | *Computed Tomography*; tomografia computorizada. |

| DfAM | *Design for Additive Manufacturing*; *design* para fabrico aditivo. |

| DINED | *Delft Institute of Ergonomics and Design*; base de dados antropométrica da TU Delft. |

| DOI | *Digital Object Identifier*; identificador digital de objecto. |

| EMG | Eletromiografia; registo da actividade elétrica muscular. |

| EU | *European Union*; União Europeia. |

| EUA | Estados Unidos da América. |

| FA/FdA | Fabrico aditivo. |

| FDA | *Food and Drug Administration*; agência reguladora dos Estados Unidos para alimentos, medicamentos e dispositivos médicos. |

| FDM | *Fused Deposition Modelling*; modelação por deposição fundida. |

| FEA | *Finite Element Analysis*; análise por elementos finitos. |

| FEM | *Finite Element Method*; método dos elementos finitos. |

| FFF | *Fused Filament Fabrication*; fabrico por filamento fundido. |

| FFD | *Free-Form Deformation*; deformação de forma livre. |

| GB/T | Norma nacional recomendada chinesa. |

| HB | *Hand Breadth*; largura da mão. |

| HCD | *Human-Centred Design*; *design* centrado no humano. |

| HGD | *Hand Grip Diameter*; diâmetro de preensão da mão. |

| HL | *Hand Length*; comprimento da mão. |

| HTML | *HyperText Markup Language*; linguagem de marcação de hipertexto. |

| IA | Inteligência Artificial. |

| ICF | *International Classification of Functioning, Disability and Health*; Classificação Internacional de Funcionalidade, Incapacidade e Saúde. |

| IEEE | *Institute of Electrical and Electronics Engineers*; associação técnico-científica e entidade editorial/de normalização. |

| ISO | *International Organization for Standardization*; Organização Internacional de Normalização. |

| JSON | *JavaScript Object Notation*; formato leve de intercâmbio de dados. |

| JWT | *JSON Web Token*; *token* *web* em formato JSON para autenticação e autorização. |

| LL | *Lower Limb*; membro inferior. |

| MCP | *Metacarpophalangeal*; articulação metacarpofalângica. |

| MDR | *Medical Device Regulation*; Regulamento Europeu dos Dispositivos Médicos. |

| MPT | *Matching Person and Technology*; modelo de adequação entre pessoa e tecnologia. |

| MRI | *Magnetic Resonance Imaging*; ressonância magnética. |

| PCA | *Principal Component Analysis*; análise de componentes principais. |

| PDF | *Portable Document Format*; formato portátil de documento. |

| PIP | *Proximal Interphalangeal*; articulação interfalângica proximal. |

| PL | *Palm Length*; comprimento da palma. |

| PRISMA | *Preferred Reporting Items for Systematic Reviews and Meta-Analyses*; diretrizes para reporte de revisões sistemáticas e meta-análises. |

| RTD | *Research Through Design*; investigação através do *design*. |

| SD | *Standard Deviation*; desvio-padrão. |

| SLA | *Stereolithography*; estereolitografia. |

| SLS | *Selective Laser Sintering*; sinterização selectiva a laser. |

| SSM | *Statistical Shape Modelling*; modelação estatística da forma. |

| SQLite | Motor leve de base de dados relacional baseado em SQL, autónomo e incorporável na aplicação. |

| STL | *Stereolithography*; formato de ficheiro de malha tridimensional usado em impressão 3D. |

| TC | *Technical Committee*; comité técnico. |

| TRL | *Technology Readiness Level*; nível de prontidão tecnológica. |

| UCD | *User-Centred Design*; *design* centrado no utilizador. |

| UI | *User Interface*; interface do utilizador. |

| UL | *Upper Limb*; membro superior. |

| UX | *User Experience*; experiência do utilizador. |

| WASM | *WebAssembly*; tecnologia para execução de código compilado no navegador. |

| XAI | *Explainable Artificial Intelligence*; inteligência artificial explicável. |

## Lista de tabelas

| Identificação | Descrição | Página |
| --- | --- | --- |
| Tabela 2.1 | Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos | 11 |
| Tabela 2.2 | Elementos centrais na configuração da participação em sistemas configuráveis | 30 |
| Tabela 2.3 | Correspondência entre lacunas do estado da arte, resposta da investigação e limites de avaliação | 38 |
| Tabela 3.1 | Ciclos de *Research Through Design* documentados no desenvolvimento | 40 |
| Tabela 3.2 | Correspondência entre perguntas, actividades, evidência e limites | 43 |
| Tabela 3.3 | Métodos, unidades de análise, critérios e localização dos resultados | 44 |
| Tabela 4.1 | Principais parâmetros antropométricos da mão e do membro superior relevantes para modelação paramétrica | 51 |
| Tabela 4.2 | Conjuntos mínimos de parâmetros por nível de amputação | 52 |
| Tabela 4.3 | Métodos de recolha de dados antropométricos e suas características | 54 |
| Tabela 4.4 | Funções e limites da base antropométrica na configuração | 55 |
| Tabela 4.5 | Estrutura hierárquica dos parâmetros no modelo paramétrico | 56 |
| Tabela 4.6 | Mapeamento entre parâmetros antropométricos e elementos do modelo | 58 |
| Tabela 4.7 | Estrutura técnica em camadas de um modelo paramétrico em OpenSCAD para próteses personalizadas | 60 |
| Tabela 4.8 | Síntese das relações implementadas e respectivas limitações | 62 |
| Tabela 4.9 | Dicionário operacional dos parâmetros numéricos dos modelos avaliados | 63 |
| Tabela 4.10 | Exemplo da transformação das medidas antropométricas em geometria digital no Flexy Beast | 65 |
| Tabela 4.11 | Cronologia das principais iterações paramétricas | 66 |
| Tabela 5.1 | Fluxo de dados e responsabilidades da plataforma | 71 |
| Tabela 5.2 | Componentes, estados e limites do protótipo examinado | 62 |
| Tabela 5.3 | Modelos integrados na plataforma e respectiva avaliação | 68 |
| Tabela 6.1 | Especificação técnica dos modelos de IA e da estrutura da sugestão paramétrica | 88 |
| Tabela 6.2 | Distribuição de tarefas entre regras, IA e supervisão humana | 90 |
| Tabela 8.1 | Evidência do funcionamento da plataforma no processo de projecto | 97 |
| Tabela 8.2 | Projectos de preparação digital para impressão 3D com configuração analisada | 100 |
| Tabela 8.3 | Inspecção computacional das malhas geradas para um perfil antropométrico de 8 anos | 102 |
| Tabela 8.4 | Descrições submetidas nos cenários de avaliação da IA | 106 |
| Tabela 8.5 | Síntese da avaliação das sugestões de IA | 107 |
| Tabela 8.6 | Modelos e mecanismos de escala avaliados | 109 |
| Tabela 8.7 | Factor de escala da maior dimensão da palma exportada relativamente à configuração de referência | 109 |
| Tabela 8.8 | Discussão dos resultados face às lacunas seleccionadas do estado da arte | 111 |
| Tabela 9.1 | Estado da resposta às perguntas de investigação aprovadas | 114 |

## Lista de figuras

| Identificação | Descrição | Página |
| --- | --- | --- |
| Figura 1.1 | Exemplos de próteses e dispositivos associados ao fabrico aditivo em contexto protésico. | 2 |
| Figura 2.1 | Exemplos de próteses de membro superior impressas em 3D, ilustrando diversidade tipológica e construtiva. | 7 |
| Figura 2.2 | Utilização continuada, rejeição primária e rejeição secundária de próteses numa amostra de adultos com amputação adquirida do membro superior. | 9 |
| Figura 2.3 | Comparação entre os fluxos tradicional, CAD/CAM e de fabrico aditivo na produção de dispositivos protésicos. | 14 |
| Figura 2.4 | Exemplo de configurador digital para personalização de uma prótese impressa em 3D. | 16 |
| Figura 2.5 | Marcos anatómicos e medidas de referência da mão para fins de personalização. | 21 |
| Figura 2.6 | Enquadramento de um fluxo de CAD apoiado por IA para desenvolvimento de produto. | 25 |
| Figura 2.7 | Modelo de processo para configurar participação em ecossistemas de inovação e cocriação. | 30 |
| Figura 2.8 | Número de artigos por nível de prontidão tecnológica (TRL) e categoria de aplicação. O gráfico distingue próteses de membro inferior produzidas por impressão 3D (MI 3DP), próteses de membro inferior desenvolvidas com recurso a CAD/CAM (MI CAD/CAM), outras aplicações de membro inferior (MI outras), próteses de membro superior produzidas por impressão 3D (MS 3DP) e outras aplicações de membro superior (MS outras). | 34 |
| Figura 3.1 | Processo interdisciplinar de desenvolvimento de uma prótese de membro superior impressa em 3D. | 41 |
| Figura 3.2 | Exemplo de recolha dimensional para ajuste de prótese impressa em 3D. | 47 |
| Figura 4.1 | Parâmetros antropométricos utilizados na modelação paramétrica de dedos protésicos. | 51 |
| Figura 4.2 | Comparação entre o escalonamento uniforme e a modelação paramétrica de dedo protésico. | 53 |
| Figura 4.3 | Relação entre modelo paramétrico digital, prototipagem e verificação de um dedo protésico. | 59 |
| Figura 5.1 | Fluxo geral de produção personalizada de próteses a partir de plataforma *web* – Hand Fab | 69 |
| Figura 5.2 | Painel de configuração dos perfis de utilizador na plataforma HandFab. | 70 |
| Figura 5.3 | Arquitectura da plataforma e fronteiras entre navegador, servidor, serviço externo de IA e preparação do fabrico. | 71 |
| Figura 5.4 | Sequência de dados e decisões desde o perfil ou descrição até à sugestão, confirmação, geração determinística e exportação. | 73 |
| Figura 5.5 | Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo. | 75 |
| Figura 5.6 | Visualização do código OpenSCAD e da geometria correspondente na plataforma HandFab. | 78 |
| Figura 5.7 | Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso. | 79 |
| Figura 5.8 | Interface de selecção, configuração paramétrica e materiais da plataforma HandFab. | 80 |
| Figura 6.1 | Relação entre desafios de compreensão das decisões e princípios de IA responsável. | 92 |
| Figura 7.1 | Exemplo publicado de teste de uma prótese impressa em 3D com um utilizador; esta actividade não integrou a avaliação da presente dissertação. | 95 |
| Figura 8.1 | Componentes impressos e estados preliminares de montagem: segmentos digitais articulados, palma e elementos separados. | 103 |
| Figura 8.2 | Séries físicas de segmentos identificados pelos perfis de ensaio de 8, 15, 28 e 70 anos. | 103 |
| Figura 8.3 | UnLimbited Phoenix configurada para o perfil de ensaio de 15 anos, apresentada em sete vistas da montagem física. | 104 |
| Figura 8.4 | Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior. | 105 |
| Figura C.1 | Fluxo entre dados de entrada, mapa comum, regras específicas dos modelos e geometria exportável. Produção própria. | 159 |

## Capítulo 1 — Introdução

### 1.1 Enquadramento geral, contexto e motivação

A perda de membros superiores provoca impactos funcionais, sociais e simbólicos, com efeitos nas tarefas quotidianas, na participação e na identidade. Este contexto exige soluções que considerem desempenho mecânico, conforto, aceitação estética e viabilidade económica. Apesar dos avanços em dispositivos médicos e no fabrico aditivo, persistem obstáculos relacionados com o custo, a adaptação anatómica e a dependência de técnicos especializados para o ajuste e a manutenção das próteses.

Nos últimos anos, a impressão 3D e as plataformas *open source* ampliaram o acesso a dispositivos protésicos, especialmente em contextos economicamente desfavorecidos. Muitos desses modelos dependem de geometrias fixas, isto é, formas predefinidas sem adaptação automática, ou de ajustes manuais pouco padronizados. Esta condição dificulta a expansão dos modelos, a repetição documentada do procedimento e a integração consistente de dados antropométricos.

A Figura 1.1 introduz visualmente este contexto, mostrando como o fabrico aditivo tem sido associado a soluções protésicas abertas e adaptáveis. Esta leitura enquadra a motivação inicial do projecto: a impressão 3D amplia o campo de possibilidades, enquanto a configuração dimensional continua a exigir modelos ajustáveis, critérios explícitos e mediação no desenvolvimento do projecto.

![](figuras/figura_1_1_proteses_fabrico_aditivo.jpeg)

Figura 1.1 — Exemplos de próteses e dispositivos associados ao fabrico aditivo em contexto protésico.

Fonte: produção própria, a partir de imagens publicadas no sítio *Enabling the Future*, nas páginas *Wrist Powered* e *Introducing the New 3D Printed Kinetic Hand Design* (consultadas em 20 de julho de 2026). https://enablingthefuture.org/wrist-powered/; https://enablingthefuture.org/2020/11/13/introducing-the-new-3d-printed-kinetic-hand-design/

Nesta dissertação, «prótese de membro superior» designa a categoria geral em que o estudo se inscreve; os artefactos implementados e avaliados são sobretudo modelos de mão protésica. «Modelo paramétrico» refere-se ao conjunto de variáveis, relações e restrições que gera a forma; «geometria exportada» designa o ficheiro resultante nos formatos *Stereolithography* (STL) ou *3D Manufacturing Format* (3MF); «plataforma *web*» identifica a aplicação que coordena parâmetros, visualização, dados e sugestões; e «protótipo físico» corresponde à peça impressa. A parametrização é a definição dessas relações, a configuração é a escolha de valores e a personalização individual exige dados da própria pessoa. Os perfis populacionais usados neste estudo fornecem referências iniciais e não equivalem a uma adaptação anatómica individual.

O *design* industrial assume uma função de mediação entre tecnologia, decisões de projecto e experiência humana. A presente investigação examina essa mediação por meio de um protótipo técnico desenvolvido e discutido segundo uma abordagem de *Research Through Design*.

### 1.2 Problema de investigação

Apesar da expansão do fabrico aditivo e da partilha de modelos abertos, persiste uma lacuna na articulação entre dados antropométricos, regras geométricas, configuração digital e preparação para fabrico. Muitos modelos de mão protésica continuam dependentes de escalonamento uniforme, ajustes manuais e conhecimento tácito, o que dificulta a identificação da origem dos valores e a avaliação do efeito de cada alteração na geometria.

O problema central consiste em compreender de que modo o *design* de produto pode articular modelação paramétrica, referências antropométricas, apoio de inteligência artificial e fabrico aditivo num fluxo técnico de configuração preliminar de modelos de mão protésica. Este fluxo deve manter explícitas as decisões, os limites dos modelos e a supervisão humana, sem pressupor adequação clínica ou funcional.

### 1.3 Objectivos da investigação

### 1.3.1 Objectivo geral

O objectivo geral é produzir conhecimento através da prática de *design* mediante o desenvolvimento e a avaliação técnica de um sistema paramétrico, apoiado por inteligência artificial, para a configuração preliminar de modelos de mão protésica destinados ao fabrico aditivo.

### 1.3.2 Objectivos específicos

Para concretizar este objectivo, a investigação procura:

- analisar o papel do *design* industrial na articulação entre requisitos humanos, decisões técnicas e condições de fabrico;
- organizar dados antropométricos provenientes de diferentes fontes, preservando população, protocolo, unidade, estatística e limitações;
- adaptar modelos abertos de mão protésica a uma estrutura paramétrica explícita em OpenSCAD;
- desenvolver uma plataforma *web* que integre configuração, visualização, gestão de versões, exportação e preparação para impressão;
- delimitar o papel da inteligência artificial na sugestão inicial de parâmetros, distinguindo-o das regras geométricas e das decisões humanas;
- avaliar a coerência técnica do percurso entre dados, parâmetros, geometria digital e protótipos físicos;
- identificar os limites da solução e as condições necessárias para avaliações clínicas, funcionais e de utilização posteriores.

A investigação procura responder às seguintes perguntas:

1. Como o *design* de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo sobre as decisões de projecto?
2. Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a possibilidade de reproduzir os resultados obtidos com próteses impressas em 3D?
3. Como o *design* industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?

Estas perguntas conservam o conteúdo aprovado para o projecto de investigação, com uniformização ortográfica para português europeu. O seu alcance é mais amplo do que a componente empírica realizada. Por esse motivo, a dissertação distingue os mecanismos de projecto desenvolvidos e verificados dos efeitos humanos que esses mecanismos procuram favorecer. Foram recolhidos dados sobre parametrização, coerência dimensional, geração geométrica, preparação para fabrico e materialização preliminar. Conforto percebido, usabilidade em utilização real, adequação funcional em uso, aceitação e impacto na dignidade ou na autonomia quotidiana não foram medidos junto de participantes.

### 1.4 Abordagem metodológica geral

O projecto adopta uma metodologia aplicada, baseada em *Research Through Design*, que reconhece o acto de projectar como uma forma de gerar conhecimento. Estrutura-se em fases conceptual, metodológica e empírica, articuladas pelo modelo *Double Diamond*, que promove ciclos iterativos de exploração, definição, desenvolvimento e avaliação.

A fase conceptual realiza uma revisão crítica da literatura e das plataformas, consolidando o quadro teórico e os requisitos técnicos. A fase metodológica estabelece a arquitectura do sistema paramétrico apoiado por inteligência artificial, integrando dados antropométricos e princípios de *design* para fabrico aditivo. A fase empírica operacionaliza a modelação paramétrica, a produção de protótipos por impressão 3D e a avaliação técnica preliminar, sem utilizar dados pessoais nem envolver participantes.

### 1.5 Estrutura da dissertação

A dissertação organiza-se em nove capítulos principais. O Capítulo 1 apresenta o enquadramento, o problema, os objectivos, as questões de investigação e a abordagem metodológica geral. O Capítulo 2 desenvolve o enquadramento teórico e o estado da arte. O Capítulo 3 explicita a metodologia de investigação. O Capítulo 4 descreve o desenvolvimento do modelo paramétrico. O Capítulo 5 aborda a plataforma *web* e a integração digital. O Capítulo 6 trata da integração da inteligência artificial. O Capítulo 7 apresenta os princípios de interface e as decisões de interacção implementadas. O Capítulo 8 reúne a avaliação e a discussão dos resultados. Por fim, o Capítulo 9 sintetiza as conclusões e os trabalhos futuros.

## Capítulo 2 — Enquadramento Teórico e Estado da Arte

### 2.1 Prótese de membro superior e dispositivos médicos

Prótese de membro superior é um dispositivo médico externo que substitui um segmento ausente devido à amputação ou a uma deficiência  congénita. Vai além da restituição formal: recupera funções, facilita actividades diárias, melhora a autonomia e reduz o impacto psicossocial da perda (Fink & Diamond, 2023; Segura et al., 2024).

A perda total ou parcial de um membro superior provoca consequências físicas, funcionais, sociais e emocionais profundas. "Perda total" refere-se à ausência completa do membro, enquanto "perda parcial" indica ausência apenas de parte dele. A mão humana incorpora capacidades motoras e sensoriais complexas, abrangendo o alcance (movimento do membro para tocar ou agarrar objectos), a preensão (acto de segurar objectos), a manipulação fina (habilidade para movimentos precisos), a estabilização (manter objectos ou posições), a coordenação bimanual (uso de ambas as mãos em colaboração) e a exploração táctil (detecção de propriedades dos objectos pelo contacto). Replicar artificialmente estas funções continua a ser um desafio significativo nos dispositivos médicos e na reabilitação. O desenvolvimento e a prescrição de próteses envolvem compromissos permanentes entre funcionalidade, peso, robustez, conforto, controlo intuitivo, manutenção e custo.

Nas últimas décadas, o sector evoluiu de soluções maioritariamente cosméticas e mecânicas para sistemas com maior sofisticação electromecânica, integração electrónica e capacidade de configuração. Ainda assim, persistem desafios estruturais, como desconforto, dificuldade de controlo, ausência de resposta sensorial e taxas elevadas de abandono. Esta tensão entre potencial técnico e resultados práticos é fundamental para compreender o estado actual das próteses de membro superior como dispositivos médicos.

### Tipologias de próteses de membro superior

As próteses de membro superior podem ser classificadas segundo a fonte de energia e o mecanismo de controlo. Distinguem-se quatro categorias principais: passivas (cosméticas), mecânicas accionadas pelo corpo, mioeléctricas (externamente alimentadas) e híbridas. Cada tipo possui vantagens e limitações, o que reflecte diferentes equilíbrios entre desempenho funcional, conforto, durabilidade e custo   (Brack & Amalu, 2021).

.

Próteses passivas destinam-se à aparência e ao apoio estático em tarefas simples, sem preensão activa. Variam entre dispositivos rígidos e versões ajustáveis, nas quais os dedos ou os terminais podem ser movidos manualmente. São leves, simples, silenciosas e requerem pouca manutenção. Oferecem utilidade funcional limitada e são preferidas quando a estética é prioritária ou quando o utilizador procura um dispositivo discreto (Fink & Diamond, 2023; Segura et al., 2024).

### Próteses mecânicas accionadas pelo corpo (*body-powered*)

As próteses mecânicas utilizam um sistema de arnês e cabos que converte movimentos do ombro, do tronco ou da cintura escapular em acção no dispositivo terminal, tipicamente um gancho ou uma mão mecânica. São soluções tradicionalmente valorizadas pela robustez, pelo comportamento mecânico previsível, pelo menor custo e pela relativa facilidade de manutenção.

Um atributo particularmente relevante é o *feedback* proprioceptivo indireto proporcionado pela tensão transmitida pelo sistema de cabos, que pode contribuir para um controlo funcional mais previsível em determinadas tarefas. Contudo, estas próteses apresentam limitações expressivas: o arnês pode ser desconfortável e restritivo, os padrões de preensão tendem a ser mais limitados e a sua utilização exige esforço físico contínuo e aprendizagem motora específica (Engdahl et al., 2024; Fink & Diamond, 2023).

### Próteses mioeléctricas

As próteses mioeléctricas são dispositivos alimentados electricamente que utilizam sinais electromiográficos (EMG) captados por eléctrodos de superfície aplicados no membro residual. Estes sinais são processados electronicamente e activam os motores responsáveis pelo movimento da mão, do punho ou do cotovelo. Em comparação com as soluções mecânicas, apresentam habitualmente maior integração estética, ausência de arnês e potencial para padrões de movimento mais sofisticados. Em alguns casos, a sua utilização tem sido associada à redução da dor fantasma e a uma experiência de uso mais aceitável em contextos sociais. As suas limitações incluem maior peso, custo mais elevado, dependência de baterias, maior sensibilidade à humidade e a interferências, necessidade de calibração e ausência de resposta sensorial directa (Bates et al., 2020; Engdahl et al., 2024).

### Sistemas híbridos

Combinam mecanismos mecânicos e elétricos no mesmo dispositivo. São particularmente frequentes em amputações proximais, como amputações transumerais ou desarticulações do ombro, podendo associar, por exemplo, controlo mecânico do cotovelo e controlo mioelétrico do terminal. Esta configuração procura tirar partido das vantagens específicas de cada sistema, distribuindo o peso, as exigências funcionais e a complexidade de controlo. Em contrapartida, a aprendizagem, a adaptação e a manutenção podem tornar-se mais exigentes (Segura et al., 2024; Walters et al., 2025).

Uma representação visual útil desta diversidade tipológica é apresentada na Figura 2.1, que reúne exemplos de próteses impressas em 3D com soluções morfológicas e mecânicas distintas, ajudando a perceber como diferentes opções de configuração materializam compromissos distintos entre simplicidade, função e custo.

![](projecto-completo_media/image02.png)

Figura 2.1 — Exemplos de próteses de membro superior impressas em 3D, ilustrando diversidade tipológica e construtiva.

Reproduzido de ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

### Considerações clínicas e funcionais

A prescrição de uma prótese de membro superior constitui um processo clínico complexo, centrado no utilizador e conduzido por uma equipa multidisciplinar composta por médicos, técnicos de ortoprotesia, terapeutas e pela própria pessoa. A escolha do dispositivo terminal envolve uma avaliação integrada de factores físicos, funcionais, ocupacionais e psicossociais (Fink & Diamond, 2023; Soyer et al., 2016).

Entre os factores físicos incluem-se o nível de amputação, o comprimento e a condição do membro residual, a integridade cutânea, a amplitude articular e a força muscular. Amputações de nível mais proximal implicam desafios acrescidos em termos de controlo e do peso do sistema protésico.

Os factores individuais, como idade, comorbilidades, dominância manual, literacia técnica, contexto profissional e actividades recreativas, influenciam significativamente a escolha da tipologia protésica. A título de exemplo, utilizadores envolvidos em trabalho manual intensivo ou em ambientes mais exigentes podem beneficiar de soluções mecânicas mais robustas, enquanto contextos profissionais e sociais em que a integração estética e a diversidade funcional são mais valorizadas podem favorecer dispositivos mioelétricos.

Os factores psicossociais, incluindo motivação, expectativas, imagem corporal, suporte social e capacidade cognitiva, são igualmente determinantes. Expectativas irrealistas relativamente às capacidades do dispositivo podem levar à insatisfação, ao uso intermitente e ao eventual abandono.

A reabilitação protésica desenvolve-se em fases — cuidados perioperatórios, preparação pré-protésica, treino com prótese definitiva e acompanhamento a longo prazo. O treino funcional é particularmente relevante em sistemas mioelétricos, exigindo fortalecimento muscular específico, aprendizagem da geração de sinais consistentes e integração progressiva do dispositivo em tarefas reais. A literatura sublinha recorrentemente a importância do seguimento continuado, da educação do utilizador e do ajustamento iterativo do dispositivo ao longo do tempo (Bates et al., 2020; Soyer et al., 2016).

### Medição de resultados e abandono protésico

A avaliação objetiva do sucesso protésico continua a ser um desafio. Persistem a escassez de instrumentos padronizados e a heterogeneidade de métricas, o que dificulta a comparação entre estudos, dispositivos e estratégias de reabilitação. São utilizadas ferramentas de avaliação registadas pelo utilizador, centradas na funcionalidade percebida, na satisfação e na qualidade de vida, bem como testes baseados em desempenho, orientados para a destreza, a velocidade de execução e o controlo funcional em tarefas estruturadas (Segura et al., 2024; Soyer et al., 2016).

Apesar da evolução tecnológica, o abandono de próteses de membro superior continua documentado. Smail et al. (2021) agrupam as razões identificadas sobretudo em duas áreas — conforto e função — e assinalam o peso, a temperatura e a transpiração entre os problemas de conforto mais persistentes. Biddiss et al. (2007) e Fink e Diamond (2023) acrescentam que o peso, o conforto, o controlo e o ajuste do encaixe são aspectos relevantes nas prioridades dos utilizadores e no processo de escolha e acompanhamento da prótese. Em conjunto, estes resultados mostram que a melhoria tecnológica, por si só, não garante a utilização continuada e que as decisões de *design* devem considerar a experiência física e funcional do utilizador.

A Figura 2.2 apresenta a distribuição observada por Østlie et al. (2012) numa amostra populacional de 224 adultos com amputação adquirida do membro superior. Nesse estudo, 4,5% dos participantes apresentavam rejeição primária da prótese e 13,4% dos 209 participantes que tinham iniciado a sua utilização interromperam-na posteriormente. Estes resultados permitem distinguir a rejeição anterior à primeira utilização da rejeição ocorrida após a adoção inicial do dispositivo.

![](figuras/figura_2_2_utilizacao_rejeicao_proteses_estilizada.jpeg)

Figura 2.2 — Utilização continuada, rejeição primária e rejeição secundária de próteses numa amostra de adultos com amputação adquirida do membro superior.

Adaptado da Figura 1 de Østlie, K., Lesjø, I. M., Franklin, R. J., Garfelt, B., Skjeldal, O. H., & Magnus, P. (2012). Prosthesis rejection in acquired major upper-limb amputees: A population-based survey. *Disability and Rehabilitation: Assistive Technology, 7*(4), 294–303. https://doi.org/10.3109/17483107.2011.635405

### Enquadramento regulatório enquanto dispositivo médico

As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pelo Regulamento ([^2]EU) 2017/745 (MDR) - https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng, que classifica os dispositivos nas Classes I, IIa, IIb e III. Dispositivos terapêuticos activos, incluindo próteses mioeléctricas, enquadram-se geralmente nas classes intermédias ou superiores, o que exige avaliação por um organismo notificado para efeitos de marcação CE[^3] (Parlamento Europeu e Conselho da União Europeia, 2017).

Nos Estados Unidos, a regulação é assegurada pela *Food and Drug Administration* (FDA) por meio de um sistema de classificação de risco. A maioria dos componentes protésicos convencionais enquadra-se nas classes de risco mais baixas, enquanto sistemas mais complexos, como próteses mioeléctricas avançadas, podem exigir controlos, documentação técnica mais extensa e, em certos casos, evidência clínica adicional (Resnik et al., 2010).

A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de *software* e consideração explícita de factores humanos e de usabilidade. Normas desenvolvidas no âmbito do comité técnico ISO/TC 168[^4] contribuem para a padronização de requisitos aplicáveis a próteses e ortóteses. Adicionalmente, os fabricantes devem implementar sistemas de vigilância pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar a sua evolução em evidência (Parlamento Europeu & Conselho da União Europeia, 2017; Resnik et al., 2010).

### 2.2 *Design* industrial, *design* inclusivo e *design* centrado no utilizador

O *design* industrial, no contexto da saúde e das tecnologias de apoio, é reconhecido progressivamente como uma disciplina mediadora entre as necessidades humanas, os contextos de utilização e os sistemas técnicos regulados.

A literatura revista evidencia que o *design* desempenha um papel estruturante na promoção da inclusão, da autonomia e da participação social, ao articular a configuração formal dos produtos com a modelação da relação entre indivíduos, ambientes, artefactos e sistemas.

Em particular, nas tecnologias de apoio, o *design* é descrito como um elemento que medeia a interacção entre os utilizadores e o seu meio envolvente, contribuindo para reduzir barreiras funcionais e sociais e, consequentemente, para melhorar os resultados de participação e a qualidade de vida (Clarkson & Coleman, 2010; Shah & Robinson, 2006).

Paralelamente, o *design* inclusivo é apresentado como um imperativo contemporâneo que visa minimizar a exclusão evitável decorrente de decisões de projecto que ignoram a diversidade populacional e as alterações de capacidades ao longo do tempo. Esta perspectiva alinha-se com a responsabilidade dos sistemas de saúde de responder a utilizadores heterogéneos, com diferentes condições físicas, cognitivas e contextuais (Clarkson & Coleman, 2010).

### *Design* industrial em dispositivos médicos

No domínio dos dispositivos médicos, o *design* industrial constitui uma prática metodológica centrada no utilizador e assume um papel colaborativo em equipas multidisciplinares de desenvolvimento. A literatura identifica, contudo, uma lacuna estrutural: muitos dispositivos médicos continuam a ser desenvolvidos predominantemente com base em abordagens de engenharia e em requisitos regulatórios, com participação limitada de profissionais com formação específica em metodologias de *design* centrado no uso. Esta assimetria contribui para soluções tecnicamente robustas, mas nem sempre optimizadas em termos de ergonomia, usabilidade ou integração na vida quotidiana (Fisher & Johansen, 2020; Wilke et al., 2020).

Neste contexto, o *design* industrial assume relevância na conceptualização, na definição de requisitos de utilização, na tradução de necessidades clínicas em soluções tangíveis e na articulação entre requisitos regulamentares e experiência do utilizador (Fisher & Johansen, 2020; Shah & Robinson, 2006).

Esta posição intermédia do *design* torna-se mais clara perante a multiplicidade de papéis que os profissionais de saúde podem assumir nos processos de desenvolvimento. Em vez de contribuírem apenas como validadores de soluções, estes agentes podem ser intervenientes do seu sector, utilizadores peritos, mediadores entre domínios e profissionais clínicos ou investigadores, como sintetiza a Tabela 2.1.

Tabela 2.1 — Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos

| Papel | Contributo no desenvolvimento | Domínio principal de decisão |

| --- | --- | --- |

| Utilizadores peritos | Fornecem experiência clínica situada e problemas de uso | Experiência do utilizador e adequação funcional |

| Mediadores | Traduzem linguagem, necessidades e constrangimentos entre equipas | Problemas técnicos, terminologia e entendimento partilhado |

| Profissionais clínicos e investigadores | Enquadram cuidados, testes e validação empírica | Resultados clínicos, ensaios e usabilidade |

Adaptado de Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. [https://doi.org/10.1080/14606925.2024.2420152](https://doi.org/10.1080/14606925.2024.2420152)

### *Design* inclusivo e *design* universal

O *design* inclusivo representa uma mudança conceptual significativa ao deslocar o foco da deficiência enquanto atributo individual para a compreensão da deficiência como resultado de desajustes entre capacidades humanas e ambientes projectados (Clarkson & Coleman, 2010).

Esta perspectiva aproxima-se dos modelos sociais e relacionais da deficiência, enfatizando que a exclusão pode ser produzida por decisões de projecto que não contemplam a diversidade de utilizadores (Clarkson & Coleman, 2010).

Enquanto campo de prática e investigação, o *design* inclusivo desenvolveu ferramentas e orientações destinadas a apoiar equipas de projecto na consideração sistemática da diversidade populacional. Estas incluem estratégias de segmentação, análise de capacidades e critérios de acessibilidade aplicáveis a produtos e sistemas, incluindo tecnologias digitais em saúde (Clarkson & Coleman, 2010).

O *design* universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente aplicada no *design* industrial, tendo como princípio orientador a concepção de produtos e ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações ou de *design* especializado. Os Sete Princípios do *design* universal, propostos por Ron Mace[^5], são amplamente citados como um quadro normativo para avaliar equidade, flexibilidade, simplicidade, tolerância ao erro e redução do esforço físico (Story, 2006).

Na área da saúde, o *design* universal é associado a abordagens centradas na pessoa e avaliado segundo critérios orientados a resultados, como a participação, a inclusão e a igualdade de acesso. A convergência entre *design* inclusivo e *design* universal revela-se particularmente evidente na ênfase comum na redução de barreiras ambientais e na ampliação do conceito de usabilidade para uma população mais ampla (Story, 2006; White & Mosca, 2022).

### *Design* centrado no utilizador e *design* centrado no humano

O *design* centrado no utilizador (*User-Centred Design* – UCD) é descrito como uma abordagem que envolve os utilizadores finais ao longo de todo o processo de desenvolvimento, para assegurar que o produto seja funcionalmente adequado, compreensível e valorizado. Esta abordagem mobiliza métodos como entrevistas, personas, protocolos de *think-aloud*, prototipagem iterativa e grupos focais, promovendo ciclos sucessivos de recolha de requisitos e de validação (Fisher & Johansen, 2020; Shah & Robinson, 2006).

O *design* centrado no humano (*Human-Centred Design* – HCD) amplia esta perspectiva ao integrar dimensões culturais, contextuais e sistémicas. No desenvolvimento de dispositivos médicos, o HCD é associado a práticas como etnografia, *design* participativo, mapeamento de jornadas (*journey maps*), mapeamento de *stakeholders* e avaliação de factores humanos. A norma ISO 62366 define requisitos específicos para a aplicação da engenharia de usabilidade a dispositivos médicos, reforçando a integração formal de avaliações formativas, realizadas durante o desenvolvimento para orientar melhorias, e de avaliações finais de validação, destinadas a verificar o resultado do processo. (Fisher & Johansen, 2020; Millet et al., 2018).

A incorporação de factores humanos é igualmente reforçada por diretivas e normas que exigem a redução dos riscos de uso inadequado, articulando segurança, ergonomia e usabilidade como dimensões indissociáveis do desenvolvimento de dispositivos médicos (Millet et al., 2018).

### *Design* Participativo e *Co-design*

O *design* participativo e o *co-design* representam um aprofundamento das abordagens centradas no utilizador, enfatizando a participação activa e o envolvimento dos utilizadores no processo de projecto. Nestes modelos, os utilizadores contribuem para a definição de problemas, a geração de soluções e a avaliação de protótipos (Chapman et al., 2025).

Revisões sistemáticas apontam para a necessidade de maior transparência e rigor na descrição dos processos de *co-design*, de modo a fortalecer a sua validade metodológica e eficácia prática. Nas tecnologias de apoio, observa-se uma evolução discursiva dos modelos centrados no utilizador para paradigmas de cocriação, nos quais as experiências dos utilizadores assumem um estatuto central na tomada de decisão (Chapman et al., 2025). Persistem tensões entre ideais participativos e contextos regulatórios altamente estruturados, nos quais o poder de decisão permanece frequentemente concentrado em profissionais clínicos e em equipas técnicas (Chapman et al., 2025; Wilke et al., 2020).

### Metodologias, instrumentos e avaliação

Fisher e Johansen (2020) e Shah e Robinson (2006) descrevem que as abordagens inclusivas e centradas no utilizador recorrem a repertórios metodológicos diversificados, incluindo personas, simulação de limitações, prototipagem iterativa, oficinas participativas e análise de ecossistemas de *stakeholders* (Fisher & Johansen, 2020; Shah & Robinson, 2006).

No domínio hospitalar e dos serviços de saúde, ferramentas de avaliação baseadas em critérios de *design* universal e de *design* para todos (*Design for All*) introduzem sistemas de análise multicritério e listas de verificação estruturadas para aferir os níveis de inclusão (White & Mosca, 2022).

Em contextos de tecnologias de apoio, modelos como o *Matching Person and Technology* (MPT) e quadros conceptuais baseados na Classificação Internacional de Funcionalidade (ICF) são utilizados para apoiar decisões de selecção e de adequação tecnológica, promovendo o alinhamento entre as características do utilizador, do ambiente e do dispositivo (White & Mosca, 2022).

A avaliação da evidência tem sido igualmente reforçada através do uso de protocolos sistemáticos, como o PRISMA, que orienta a identificação, selecção e apresentação transparente dos estudos analisados, bem como de instrumentos de avaliação crítica. Esta evolução reflecte uma preocupação crescente em fundamentar decisões de *design* numa base empírica robusta. (Chapman et al., 2025).

### Desafios e lacunas

Entre os principais desafios identificados destacam-se a articulação entre normalização e personalização em dispositivos médicos regulamentados, a distância entre modelos teóricos de UCD e as restrições institucionais da prática em saúde. Somam-se a passagem de processos participativos para contextos de implementação e a integração de factores sociais e culturais na investigação e no desenvolvimento (Fisher & Johansen, 2020; Oldfrey et al., 2024; Shah & Robinson, 2006).

Estas lacunas evidenciam que o *design* industrial em dispositivos médicos não pode ser compreendido apenas como uma prática formal ou estética, mas como uma disciplina estratégica que articula inclusão, regulação, implementação e experiência do utilizador.

### 2.3 Fabrico Aditivo e parametrização no *design* de produto

A convergência entre modelação paramétrica e fabrico aditivo (FdA) tem sido amplamente reconhecida como um dos principais vetores de transformação no *design* contemporâneo, particularmente em contextos que exigem personalização, adaptação morfológica e produção de variantes em pequena escala. A literatura posiciona estas duas abordagens como complementares: a modelação paramétrica permite gerar múltiplas variações controladas a partir de um modelo-base, enquanto a fabrico aditivo viabiliza a materialização de geometrias complexas sem necessidade de moldes ou ferramentas dedicadas (Lei et al., 2016; Ozdemir et al., 2022; van Stralen, 2018).

Esta articulação é representada com clareza na Figura 2.3, que resume o encadeamento entre aquisição digital, modelação/rectificação e fabrico, evidenciando que a personalização depende da integração das várias etapas do fluxo de trabalho.

![](figuras/figura_2_3_fluxo_digital_proteses_estilizada.png)

Figura 2.3 — Comparação entre os fluxos tradicional, CAD/CAM e de fabrico aditivo na produção de dispositivos protésicos.

Adaptado da Figura 1 de Oldfrey et al. (2024, p. 575).

Neste enquadramento, a personalização deixa de ser entendida como excepção e passa a constituir uma estratégia estruturada, operacionalizada por meio de modelos-base parametrizados. Estes modelos preservam uma arquitectura estável, expondo simultaneamente um conjunto limitado de variáveis ajustáveis, frequentemente acessíveis por meio de interfaces digitais ou de configuradores destinados a utilizadores não especialistas (Ozdemir et al., 2022; van Stralen, 2018).

### Modelação Paramétrica e Espaços de Variação

Os modelos paramétricos desempenham duas funções centrais. Em primeiro lugar, codificam a lógica geométrica do produto — relações, restrições e regras —, assegurando que alterações nos valores dos parâmetros gerem novas variantes sem comprometer a integridade estrutural nem a coerência funcional. Em segundo lugar, permitem explorar espaços de variação extensos, frequentemente descritos como quase contínuos, o que possibilita a criação de famílias de produtos ajustáveis por meio da modificação de variáveis dimensionais ou funcionais (Lei et al., 2016; Ozdemir et al., 2022).

No contexto da adaptação ao utilizador, a literatura destaca que a parametrização torna-se particularmente eficaz quando associada a dados mensuráveis, como a antropometria ou as digitalizações tridimensionais.

Em vez de recorrer a um escalonamento uniforme, que pode introduzir desvios significativos, a definição de parâmetros independentes, como comprimento e largura, permite ajustes mais precisos e maior controlo dimensional em intervalos reduzidos. Em aplicações protésicas, esta abordagem revelou maior proximidade às cinemáticas naturais e melhor adequação morfológica face a modelos ajustados apenas por escala global. (Lim et al., 2018).

### Integração com Fabrico Aditivo e *Design for Additive Manufacturing*

A eficácia da personalização depende da integração precoce dos constrangimentos do processo de fabrico aditivo no processo de projecto. A literatura sobre *Design for Additive Manufacturing* (DfAM) sublinha que a incorporação antecipada de limitações de processo — tolerâncias, resistência mecânica, espessuras mínimas, orientação de impressão — reduz falhas de fabrico e encurta os ciclos iterativos (Chtioui et al., 2023; Wiberg et al., 2019).

Wiberg et al. (2019) demonstram, no sistema que avaliaram, que a determinação experimental dos constrangimentos do processo e a sua incorporação no modelo paramétrico permitiram gerar milhares de variantes com elevada taxa de sucesso funcional e reduzir reimpressões. [^9]

Esta evidência reforça a necessidade de uma ligação sistemática entre as fases de *design* e fabrico, contrariando abordagens que tratam o fabrico como etapa posterior e correctiva (Chtioui et al., 2023; Wiberg et al., 2019).

As tecnologias de fabrico aditivo (FA) utilizadas incluem modelação por deposição fundida (FDM) e fabrico por filamento fundido (FFF), ambos baseados na extrusão de termoplásticos, SLS (fusão selectiva a laser), SLA (estereolitografia) e processos industriais metálicos, o que reflecte a diversidade de rotas produtivas para componentes personalizados. Cada tecnologia implica requisitos específicos de projecto, reforçando a importância de integrar critérios técnicos no modelo paramétrico desde o início (Chtioui et al., 2023; Wiberg et al., 2019).[^10]

### Configuradores e Cocriação Digital

A articulação entre modelação paramétrica e interfaces digitais possibilita novos modelos de cocriação e de produção distribuída. Configuradores *web* ou interfaces baseadas em CAD expõem um conjunto delimitado de parâmetros, permitindo ao utilizador ajustar dimensões ou características nos intervalos válidos, frequentemente com *feedback* em tempo real sobre viabilidade (Ozdemir et al., 2022; van Stralen, 2018).

A Figura 2.4 mostra um exemplo especialmente relevante desta lógica: a personalização mediada por interface, em que o utilizador atua sobre atributos visuais e formais num espaço de variação previamente estruturado. Este tipo de configurador ajuda a compreender como a cocriação digital pode ser operacionalizada sem exigir domínio directo de ferramentas CAD complexas.

![](projecto-completo_media/image05.png)

Figura 2.4 — Exemplo de configurador digital para personalização de uma prótese impressa em 3D.

Reproduzido de Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

Este modelo “*file-to-factory*” viabiliza fluxos digitais em que o ficheiro parametrizado é convertido directamente em instruções de fabrico, seja localmente (impressão 3D descentralizada) ou por meio de uma encomenda *online*[^11]. A literatura associa esta lógica à democratização do *design* e à expansão de estratégias de customização em massa (*mass customization*) e personalização em massa (*mass personalization*), reduzindo custos marginais ao dispensar moldes e dispositivos específicos de fabrico.[^12] (Lei et al., 2016; van Stralen, 2018).

Contudo, enfatiza-se que configuradores eficazes devem limitar o número de parâmetros expostos e fornecer orientação clara sobre os limites válidos, evitando complexidade excessiva ou escolhas superficiais (Ozdemir et al., 2022).

### Optimização, Geração e Avaliação de Desempenho

A parametrização é frequentemente combinada com métodos de optimização topológica, de geração de estruturas reticuladas e de abordagens multiobjectivo. Estas estratégias permitem gerir compromissos entre peso, resistência, custo e tempo de fabrico, explorando fronteiras de Pareto para selecionar soluções alinhadas com objectivos específicos (Lei et al., 2016; Yao et al., 2016).

Em próteses impressas em 3D, a parametrização permite ajustar de modo independente dimensões como o comprimento e a largura dos componentes, evitando as limitações do escalonamento uniforme (Lim et al., 2018). Em famílias de produtos destinadas ao fabrico aditivo, a optimização topológica permite gerar geometrias a partir de requisitos e restrições, que podem depois ser avaliadas pelo método dos elementos finitos (FEM) e por critérios de custo (Lei et al., 2016). No domínio específico das próteses de membros, Xu e Qin (2022) identificam aplicações de *design* generativo que utilizam optimização topológica para reduzir o peso e FEM para validar o desempenho estrutural. Esta passagem de parâmetros explicitamente definidos para a geração e avaliação algorítmica de alternativas estabelece uma ligação conceptual com as abordagens de inteligência artificial discutidas nas secções seguintes.

Este cruzamento entre parametrização, simulação e FA evidencia um ecossistema digital integrado que sustenta personalização técnica com base quantitativa (Lei et al., 2016; Yao et al., 2016).

### Implicações para o *design* industrial

A literatura converge para a ideia de que a robustez do modelo paramétrico é uma condição crítica para a personalização em escala. Modelos mal estruturados ou com dependências inconsistentes podem comprometer a simulação, a optimização e a configuração de famílias de produto (Lei et al., 2016; Wiberg et al., 2019).

Assim, a qualidade da definição paramétrica desempenha um papel estratégico para a viabilidade de sistemas adaptáveis (Ozdemir et al., 2022).

Em termos económicos, a Fabrico Aditivo permite reduzir [^13]penalizações tradicionais associadas à variação de produto, sustentando modelos de personalização acessíveis. Estudos orientados para famílias de produto indicam que a integração de modelos paramétricos com análises de custo e desempenho pode manter os custos relativamente estáveis mesmo com elevada diversidade geométrica (Lei et al., 2016; Yao et al., 2016).

No plano educativo e profissional, recomenda-se a integração de DfAM nos currículos de *design* industrial, promovendo competências que articulem a concepção, a simulação e a fabrico digital em fluxo contínuo (Kandikjan et al., 2022).

### 2.4 Próteses *open source* de membro superior passíveis de impressão 3D

As próteses *open source* de membro superior passíveis de impressão 3D constituem um caso particularmente relevante para esta investigação, porque articulam fabrico aditivo, partilha digital de ficheiros, reprodução distribuída e adaptação local. Estes modelos circulam frequentemente sob a forma de ficheiros digitais editáveis ou imprimíveis, acompanhados por documentação comunitária, como instruções de fabrico e montagem. A disponibilização de modelos tridimensionais através da Internet favoreceu a formação de comunidades de criadores capazes de reproduzir e avaliar estes dispositivos (Manero et al., 2019). Nas soluções abertas analisadas por Wendo et al. (2022), a disponibilidade dos ficheiros de desenho e impressão e de instruções claras de fabrico e montagem constitui um requisito essencial. Estes recursos facilitam a reprodução, o redimensionamento e a adaptação dos dispositivos, mas não garantem, por si só, a qualidade funcional de cada solução, que continua a exigir avaliação.

O projecto e-NABLE constitui um exemplo relevante deste movimento e enquadra directamente vários dos modelos analisados nesta investigação. Na revisão do catálogo e-NABLE, Wendo et al. (2022) agruparam os dispositivos em duas categorias: modelos de mão e modelos de braço. Todos os modelos de mão incluídos na revisão eram accionados pelo corpo através do movimento de um punho funcional. Entre os modelos de braço analisados, o *Unlimbited Arm v2.1* e o *Kwawu Arm* eram accionados pelo movimento do cotovelo, enquanto o *El Medallo Bionic Arm* utilizava accionamento eléctrico controlado por sinais musculares. Para o *design* de próteses de membro superior, esta distinção é importante porque evidencia a necessidade de relacionar o tipo de dispositivo e o respectivo mecanismo de accionamento com o movimento que a pessoa conserva.

Este enquadramento é importante porque vários modelos usados ou analisados nesta investigação pertencem directamente a esta linhagem. Este conjunto inclui Cyborg Beast, Raptor Reloaded, Flexy Hand, Flexy Beast, Paraglider Hand/Flexible Flyer, Phoenix Hand e Unlimbited Phoenix Hand. Estes modelos não devem ser entendidos como objectos isolados, mas como variações de um ecossistema e-NABLE em que cada modelo traduz compromissos diferentes entre simplicidade de impressão, facilidade de montagem, robustez, custo, aparência e adequação anatómica. O Cyborg Beast, por exemplo, foi descrito como uma mão protésica infantil de baixo custo, accionada pelo punho e ajustável por procedimentos remotos de medição e escala (Zuniga et al., 2015). Já modelos posteriores, como a Phoenix/Unlimbited Phoenix e derivados como o Paraglider, procuram simplificar a montagem, melhorar a manutenção e estabilizar geometrias recorrentes. Para o presente projecto, isto tem uma consequência directa: a integração de modelos e-NABLE numa plataforma paramétrica não é apenas uma operação técnica de importação de ficheiros, mas uma tentativa de explicitar e controlar regras geométricas que, nos modelos originais, aparecem muitas vezes como escalas globais, limites empíricos ou decisões embebidas no próprio ficheiro.

O Victoria Hand Project representa uma alternativa complementar ao modelo comunitário e *maker* do e-NABLE. Em vez de depender sobretudo de voluntários dispersos, organiza-se como uma estrutura de prestação de cuidados baseada em parcerias locais, formação técnica, fabrico descentralizado e acompanhamento por profissionais ou clínicas parceiras. A sua relevância está em mostrar que a impressão 3D pode ser integrada num modelo de serviço mais estruturado, no qual a criação digital de componentes, a selecção modular, a adaptação de encaixes e a circulação de *feedback* entre parceiros locais e equipa central funcionam como infraestrutura de aprendizagem contínua (Dechev et al., 2023). Assim, enquanto o e-NABLE evidencia o potencial da comunidade aberta e da documentação partilhada, o Victoria Hand Project evidencia a importância da mediação clínica, da formação e da qualidade controlada em contextos de baixo acesso a cuidados protésicos.

A evidência disponível, contudo, obriga a uma leitura cautelosa. As revisões sistemáticas sobre próteses de membro superior impressas em 3D indicam que os resultados são promissores, mas continuam limitados por amostras pequenas, ausência de ensaios controlados, períodos curtos de acompanhamento e heterogeneidade nos instrumentos de avaliação. A literatura existente não demonstra superioridade robusta face a próteses convencionais nem permite concluir sobre efeitos de longo prazo em conforto, durabilidade ou qualidade de vida (Diment et al., 2018). Uma revisão mais recente dos resultados clínicos de próteses impressas em 3D reforça a mesma cautela. Nos estudos sobre o membro superior, foram relatadas melhorias na preensão global, na destreza manual e na satisfação dos utilizadores, tendo sido também avaliados o conforto, a facilidade de utilização e o uso quotidiano. Contudo, os estudos são geralmente pequenos, metodologicamente heterogéneos e difíceis de comparar entre si (Atallah et al., 2025).

As limitações técnicas também são relevantes para o *design*. Estudos mecânicos sobre mãos *open source* mostram que a acessibilidade e o baixo custo coexistem com restrições claras de desempenho, repertório de preensões, resistência, durabilidade e segurança funcional. No caso do Raptor Reloaded, por exemplo, uma mão corporalmente accionada pode ser útil para tarefas simples, mas permanece distante da diversidade de movimentos e preensões de uma mão humana (Cabibihan et al., 2021). Esta constatação não diminui o valor social destes modelos, mas impede que sejam apresentados como substitutos clínicos universais. Pelo contrário, reforça a necessidade de os tratar como plataformas de desenvolvimento, aprendizagem e personalização progressiva.

Para esta investigação, o interesse das próteses *open source* impressas em 3D está precisamente nessa tensão. Modelos como o Flexy Beast, o Paraglider Hand e a Unlimbited Phoenix Hand oferecem bases abertas, documentadas e compatíveis com fabrico distribuído. A sua configuração continua frequentemente dependente de escalonamento, adaptação manual e conhecimento tácito da comunidade. A proposta de um sistema paramétrico apoiado por inteligência artificial situa-se nesse intervalo: procura transformar modelos abertos em objectos configuráveis com regras explícitas, limites dimensionais visíveis, apoio à escolha do modelo e ligação mais clara entre dados antropométricos, geometria gerada e critérios de fabrico. Deste modo, o ecossistema e-NABLE e o Victoria Hand Project constituem antecedentes históricos e referências críticas para compreender o que a plataforma deve preservar, corrigir e tornar mais verificável.

### 2.5 Antropometria aplicada ao *design* protésico

A antropometria constitui um fundamento técnico e metodológico central no *design* protésico, porque a adequação geométrica do dispositivo ao corpo do utilizador condiciona directamente o conforto, a segurança, o desempenho funcional e a aceitação. Em próteses de membro superior, observa-se uma utilização crescente de processos digitais de captura da geometria corporal, incluindo a digitalização 3D e a fotogrametria. Estes métodos permitem obter medições destinadas à personalização das próteses, ajustar o desenho em *software* e produzir componentes por impressão 3D (Chainando et al., 2025). Nesta investigação, estes passos são organizados numa cadeia de trabalho composta por aquisição anatómica, modelação ou rectificação em CAD, fabrico aditivo e pós-processamento. Esta cadeia corresponde à organização metodológica adoptada no projecto e não a um protocolo único estabelecido pela revisão.

### Da dimensão linear à “forma” como dado de projecto

Historicamente, a antropometria aplicada ao *design* baseou-se em medidas escalares (comprimentos, larguras, perímetros), obtidas com instrumentos como paquímetros, compassos antropométricos e fitas métricas, muitas vezes segundo procedimentos normalizados (por exemplo, a norma ISO 7250). Contudo, no *design* protésico — particularmente em interfaces corpo–dispositivo, como o encaixe (*socket*) — a literatura sublinha que a “forma” (*shape*) desempenha um papel determinante, pois pequenas variações volumétricas e distribuições de pressão podem gerar desconforto, lesões cutâneas e abandono do dispositivo. Estudos e revisões referem que o ajuste protésico pode exigir tolerâncias muito reduzidas e que a complexidade anatómica, bem como trajetórias de carga e zonas de alívio, não é devidamente capturada por um conjunto limitado de medidas lineares (Albin & Molenbroek, 2023; Young et al., 2023).

Assim, observa-se uma valorização crescente de métodos capazes de capturar geometria tridimensional de alta resolução e de traduzir essa informação em modelos CAD passíveis de retificação, parametrização e fabrico (Squibb et al., 2024).

Mesmo assim, a medição linear continua a ser indispensável para estruturar o modelo paramétrico, sobretudo quando se pretende definir um conjunto mínimo de entradas robustas e replicáveis. A Figura 2.5 ilustra precisamente este nível basal: os marcos anatómicos e os comprimentos de referência que sustentam medições comparáveis da mão.

![](projecto-completo_media/image06.png)

Figura 2.5 — Marcos anatómicos e medidas de referência da mão para fins de personalização.

Reproduzido de Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

### Métodos de recolha antropométrica em próteses e tecnologias de apoio

A literatura organiza os métodos de recolha em famílias, cada uma com potencialidades e limitações específicas para o *design* protésico:

A antropometria manual inclui medições em posturas normalizadas, com instrumentos clínicos e de ergonomia. Mantém relevância em contextos de acessibilidade clínica e de monitorização simples, por exemplo, pela medição de circunferências para acompanhar variações do membro residual. Contudo, estas medidas podem representar apenas parcialmente as alterações reais de volume, uma vez que dependem da geometria do segmento e da distribuição dos tecidos, o que reduz a precisão necessária para decisões de ajuste fino. (Ibrahim et al., 2024).

2. A digitalização 3D por *scanning* óptico, permite captar a superfície corporal sob a forma de nuvens de pontos ou malhas, posteriormente limpas e convertidas em modelos utilizáveis em CAD e fabrico, frequentemente no formato STL. Esta tecnologia facilita fluxos de personalização e pode ser combinada com processos de automatização, como a correspondência de características anatómicas, para reduzir o trabalho manual. A consistência dos resultados pode, contudo, variar conforme a complexidade da forma, sobretudo em geometrias irregulares, como segmentos residuais complexos. (Squibb et al., 2024).

3. Fotogrametria: reconstrói modelos 3D a partir de fotografias 2D, incluindo soluções baseadas em *smartphones*. É apresentada como um método promissor pela rapidez de captura e pelo potencial de acesso alargado, embora possa exigir mais tempo de processamento e cuidados com a iluminação e a cobertura da imagem (Silva et al., 2024).

4. As imagens médicas, como tomografia computorizada (CT) ou ressonância magnética (MRI: *Magnetic Resonance Imaging*), permitem obter geometria externa e, em alguns casos, informação interna, por exemplo, sobre estruturas ósseas. Esta informação pode sustentar modelos mais ricos e abordagens como a modelação estatística de forma. Contudo, estas técnicas implicam maior custo e menor acessibilidade e, no caso do CT, exigem ainda considerar a exposição à radiação e a dependência de contexto hospitalar.

5. Medições complementares da interface (pressão, termografia, bioimpedância) A literatura enfatiza que, em próteses, a adequação não é apenas geométrica: depende do comportamento da interface durante o uso. Por isso, surgem métodos adjuntos que quantificam sinais de ajuste, como a distribuição de pressão e de cisalhamento, zonas de aquecimento localizado (*Thermal hot spots*) e flutuações de volume do membro residual. Estes métodos ajudam a ligar decisões de forma/retificação a desfechos de conforto e segurança, embora, em muitos casos, sejam descritos como ainda experimentais e com barreiras à adopção clínica (Ibrahim et al., 2024; Young et al., 2023).

### Interpretação e aplicação de dados antropométricos no projecto

A passagem de dados antropométricos para critérios de projecto ocorre por diferentes vias analíticas:

– Dimensionamento estatístico por percentis e avaliação de incompatibilidades dimensionais: método típico no *design* ergonómico para definir dimensões que acomodam uma percentagem da população; aplicado sobretudo a produtos de uso “externo” (por exemplo, cadeiras de rodas e interfaces).

– Métodos multivariados e aprendizagem estatística: usados quando se trabalha com dados de alta dimensionalidade (malhas, secções, nuvens de pontos), permitindo extrair padrões de retificação ou modos de variação.

– Modelos preditivos e modelação estatística de forma (SSM): aplicados para reconstruir a geometria a partir de medições reduzidas e inferir relações entre a superfície e a anatomia interna, com análise de componentes principais (PCA) e regressões como ferramentas frequentes, embora limitados por tamanhos amostrais reduzidos em vários estudos (Sunderland et al., 2024).

Em *design* protésico, a aplicação mais crítica recai sobre o encaixe e as zonas de contacto, onde a geometria capturada é submetida a processos de retificação (diferenças propositadas entre o corpo e o dispositivo) e, depois, validada por critérios de conforto e de interface. A literatura é explícita ao considerar a captura dimensional/geométrica do membro como etapa decisiva para a qualidade do encaixe (Kannenberg et al., 2024; Young et al., 2023).

### Evidência por tipo de dispositivo

Embora os princípios sejam transversais, os estudos analisados distinguem requisitos e métodos segundo o tipo de dispositivo:

– Encaixes protésicos e ortóteses: forte ênfase na digitalização 3D, na análise quantitativa de malhas e na validação com métricas de interface e/ou de simulação por elementos finitos (FEA). Em fluxos digitais de fabrico, verificam-se diferenças geométricas relevantes entre soluções manuais e digitais, reforçando que a digitalização implica uma transformação do próprio processo de ajuste e pode alterar o resultado (Kannenberg et al., 2024; Silva et al., 2024).

– Próteses de membro superior: Chainando et al. (2025) identificam a tomografia computorizada (CT), os digitalizadores 3D comerciais e a fotogrametria como os três principais métodos digitais de captura. A revisão assinala que estas técnicas permitem obter medições destinadas à personalização, mas também apresentam diferenças de precisão, custo, acessibilidade e requisitos técnicos. Num estudo que comparou medições tradicionais, ressonância magnética e digitalização 3D, Çıklaçandır et al. (2022) não encontraram diferenças estatisticamente significativas entre os métodos. A digitalização 3D apresentou resultados próximos dos obtidos por ressonância magnética e vantagens potenciais relacionadas com o custo, o tempo, a fiabilidade e a repetibilidade.

– Produtos de assistência definidos por zonas de alcance funcional (ex.: cadeiras de rodas e acessórios): a antropometria é frequentemente operacionalizada como critério de posicionamento e de acessibilidade, com mapeamentos de alcance e critérios percentílicos.

### Limitações, lacunas e recomendações

Apesar do avanço metodológico, a literatura identifica limitações consistentes: amostras pequenas em estudos aplicados, inconsistência no registo das etapas de retificação e de pós-processamento e falta de validação em contexto real e de longo prazo.

Um problema estrutural particularmente relevante para o *design* inclusivo é a escassez de bases de dados antropométricas normalizadas para pessoas com deficiência, o que dificulta estimativas de acomodação e pode perpetuar desajustes de *design* em populações sub-representadas (Paul et al., 2022).

Como orientação prática, emergem recomendações claras: selecionar o método de medição em função da questão de *design* — captura de forma, monitorização de volume ou validação de interface —, garantir a consistência da medição mediante posturas padronizadas e da marcação coerente dos pontos de referência anatómicos, e utilizar bases de dados antropométricas alinhadas com a população-alvo quando se pretende definir critérios de acomodação e ajuste (ASTM International, 2024; Ibrahim et al., 2024).

Acresce a recomendação de distinguir o ajuste estático (em posturas padronizadas) do ajuste dinâmico (durante a amplitude de movimento funcional), reconhecendo que ajuste e conforto são conceitos relacionados, mas não equivalentes (ASTM International, 2024).

### Estruturação de dados

A antropometria aplicada ao *design* protésico evoluiu para um paradigma digital centrado na captura e na interpretação tridimensionais, complementado por métricas de interface que aproximam a medição do desempenho real de uso. Esta abordagem favorece a integração entre dados dimensionais, CAD, parametrização e fabrico aditivo, abrindo caminho para fluxos de adaptação parcialmente automatizados. Contudo, a consolidação destas práticas exige procedimentos mais padronizados, amostras mais amplas, bases de dados antropométricas representativas e identificação clara da origem dos valores utilizados (Paul et al., 2022; Sunderland et al., 2024).

No contexto desta investigação, esta necessidade foi operacionalizada através da construção de uma base local consolidada de medidas da mão e do membro superior distal. A descrição detalhada da selecção das fontes, da extracção dos valores, da normalização dos dados e da sua tradução para parâmetros de projecto é retomada no Capítulo 4, onde esses dados deixam de funcionar apenas como enquadramento teórico e passam a integrar a metodologia de desenvolvimento do modelo paramétrico.

### 2.6 Inteligência Artificial no processo de *design*

A integração de Inteligência Artificial (IA) no *design* tornou-se um tema central devido ao surgimento de novas ferramentas e à alteração da relação entre criatividade, análise, decisão e automatização. Contudo, a rápida disseminação do termo «IA» também gerou alguma imprecisão conceptual. Em muitos contextos, a mesma designação é usada para sistemas de previsão, algoritmos de optimização, modelos generativos e interfaces conversacionais, embora estes mecanismos tenham funções e modos de operação distintos. Numa dissertação de *design* industrial, importa começar por uma clarificação introdutória: esta secção explica, de forma acessível, o que é a IA, como funciona em termos gerais, que formas assume no *design* e por que razão deve ser entendida como instrumento de apoio sujeito à decisão do designer (Choudhury et al., 2025; Saeidnia & Ausloos, 2024; Yüksel et al., 2023).

Para efeitos de enquadramento, a Figura 2.6 é útil porque mostra a IA não como um bloco monolítico, mas como uma camada integrada num fluxo CAD mais amplo, em que a recolha de dados, a modelação, a optimização e a avaliação permanecem articuladas com a decisão de projecto.

![](figuras/figura_2_6_fluxo_cad_ia_estilizado.png)

Figura 2.6 — Enquadramento de um fluxo de CAD apoiado por IA para desenvolvimento de produto.

Adaptado de Menaka, S., Raja, A. W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s).

### O que é a Inteligência Artificial

Em termos gerais, a IA pode ser entendida como um conjunto de métodos computacionais orientados para executar tarefas que requerem aprendizagem, reconhecimento de padrões, inferência ou geração de respostas com base em dados. Neste contexto, inferência designa o processo pelo qual um sistema aplica padrões aprendidos durante o treino a novos dados de entrada, produzindo uma classificação, previsão, recomendação ou resposta compatível com esses padrões. Esta definição evita tratar a IA como uma entidade única ou como sinónimo de inteligência humana generalizada. A maioria dos sistemas actuais opera sobre tipos específicos de problemas a partir de exemplos, regularidades e relações estatísticas aprendidas durante o treino, sem possuir uma capacidade geral de pensamento (Choudhury et al., 2025; Yüksel et al., 2023).

Dentro deste campo, a aprendizagem automática designa as abordagens em que o sistema aprende a partir de dados, em vez de depender exclusivamente de regras explicitamente escritas. A aprendizagem profunda corresponde a um subconjunto desta família e baseia-se em redes neuronais artificiais com múltiplas camadas, particularmente adequadas para tratar dados complexos, como imagens e texto. Já a IA generativa refere-se a modelos capazes de produzir novos conteúdos — por exemplo, texto, imagens, composições formais ou variantes de projecto — com base nos padrões que aprenderam. Esta distinção é particularmente importante para o *design*, pois diferentes tipos de IA apoiam diferentes tarefas: algumas ajudam a analisar informação, outras a prever resultados, outras a optimizar soluções e outras ainda a gerar alternativas (Khanolkar et al., 2023; Li et al., 2021). No desenvolvimento de produtos, por exemplo, estas técnicas podem identificar padrões em modelos tridimensionais e gerar novas variantes de forma a partir de requisitos previamente definidos (Krahe et al., 2020).

### Como funciona: dados, treino, inferência e geração

O funcionamento básico da maioria dos sistemas actuais de IA pode ser explicado em quatro etapas: dados, treino, inferência e, em certos casos, geração. Em primeiro lugar, o sistema necessita de dados de entrada, isto é, exemplos a partir dos quais possa aprender padrões. Em segundo lugar, durante o treino, o modelo ajusta os seus parâmetros internos para captar padrões recorrentes nos dados. Em terceiro lugar, após o treino, o modelo passa a realizar inferência, produzindo previsões, classificações, recomendações ou respostas a novos casos. Em modelos generativos, há ainda um quarto momento: a produção de novos conteúdos compatíveis com os padrões aprendidos, em vez de simples classificação ou previsão (Ao et al., 2025; Menaka et al., 2025; Panchal et al., 2019).

Nos modelos de linguagem, o texto é processado em unidades designadas por *tokens*. Um *token* pode corresponder a uma palavra completa, a parte de uma palavra, a um número ou a um sinal de pontuação. O limite de *tokens* define a extensão máxima da resposta que o modelo pode produzir, não a sua qualidade ou exactidão. A temperatura é um parâmetro de geração que condiciona a distribuição usada na escolha de cada unidade seguinte: valores mais baixos concentram a selecção nas alternativas mais prováveis e tendem a reduzir a variação, enquanto valores mais elevados admitem alternativas menos prováveis e tendem a produzir respostas mais diversas. A temperatura não representa confiança, qualidade ou precisão, e o valor zero não garante, por si só, respostas integralmente idênticas.

Esta lógica distingue a IA contemporânea dos sistemas puramente baseados em regras. Num sistema baseado em regras, o comportamento é prescrito antecipadamente: se ocorrer determinada condição, executa-se determinada acção. Num sistema treinado com dados, pelo contrário, o comportamento emerge da exposição a exemplos. Esta diferença ajuda a explicar a sua força e fragilidade. A força reside na capacidade de lidar com grande complexidade, diversidade e volume de informação. A fragilidade resulta da dependência dos dados de treino, que podem conter enviesamentos, simplificações e erros reproduzidos pelo sistema (Panchal et al., 2019; Yüksel et al., 2023).

Nos modelos generativos, este processo torna-se particularmente visível. O sistema aprende distribuições de forma, linguagem, composição ou estilo e, a partir daí, produz novas saídas em resposta a condições ou prompts. Isto permite criar imagens, textos ou alternativas formais que não existiam previamente naquela forma exacta. O resultado pode parecer coerente e ainda assim ser inadequado, derivativo ou tecnicamente frágil. Para o *design*, esta distinção é decisiva: gerar muitas alternativas não equivale a resolver bem o problema de projecto (Burnap et al., 2019; Choudhury et al., 2025; Li et al., 2021).

### Formas de IA mais relevantes para o *design*

A literatura identifica várias famílias de aplicações da IA com relevância directa para o *design*. Uma primeira família é a do apoio à decisão, na qual sistemas analíticos ajudam a interpretar grandes volumes de informação, a comparar alternativas e a reduzir a carga cognitiva em problemas multivariados. Uma segunda é a optimização, particularmente importante na engenharia de produto, na parametrização e no fabrico, na qual algoritmos exploram combinações possíveis e sugerem soluções com melhor desempenho estrutural, funcional ou produtivo. Uma terceira é a visão por computador, usada quando o sistema precisa interpretar imagens, formas ou padrões visuais. Uma quarta é o processamento de linguagem natural, que permite interagir com sistemas complexos por meio de descrições semânticas, em vez de comandos técnicos rígidos. Finalmente, a quinta família, hoje mais visível, corresponde aos sistemas generativos capazes de produzir texto, imagem, forma ou variantes de projecto em resposta a condições de entrada (Ao et al., 2025; Khanolkar et al., 2023; Wang & Hu, 2024).

Para o *design* industrial, estas famílias não têm exactamente o mesmo peso. A IA generativa tornou-se especialmente relevante na ideação, na comunicação visual e na rápida exploração de alternativas. A optimização e os modelos preditivos assumem maior importância quando o problema envolve desempenho, simulação, restrições de fabrico ou espaços paramétricos amplos. Já o processamento de linguagem natural ganha interesse crescente enquanto camada de acesso a sistemas mais complexos, sobretudo quando se pretende que utilizadores menos especializados consigam formular intenções ou restrições sem depender de *software* CAD avançado ou de uma sintaxe demasiado técnica (Ao et al., 2025; Menaka et al., 2025; Wang & Hu, 2024).

### IA ao longo do processo de *design*

Uma das conclusões mais consistentes da literatura é que a IA não atua apenas numa fase isolada do processo de projecto. Nas fases iniciais, pode apoiar a pesquisa, a síntese de informação e o enquadramento do problema, ajudando a identificar padrões nas necessidades dos utilizadores, tendências, dados de mercado ou requisitos de contexto. Na ideação, pode ampliar o espaço de procura, reduzir fixação prematura e produzir rapidamente múltiplas alternativas de partida. No desenvolvimento, pode acelerar a iteração, gerar variantes paramétricas e articular a exploração formal às restrições técnicas. Em fases posteriores, pode apoiar a prototipagem, a simulação, a previsão de desempenho e a comparação entre opções concorrentes. Também pode reforçar a comunicação e a documentação, produzindo representações mais rápidas de cenários, conceitos e soluções (Khanolkar et al., 2023; Saeidnia & Ausloos, 2024; Verganti et al., 2020).

A eficácia da IA varia consoante a etapa do processo de *design*. A literatura sugere que o seu valor tende a ser maior em tarefas de exploração divergente, análise extensiva e automatização parcial, enquanto as etapas de convergência, enquadramento contextual, decisão ética e validação final exigem avaliação humana qualificada. A IA pode ampliar o campo de exploração e acelerar a comparação entre alternativas, mas a decisão sobre o que faz sentido desenvolver, para quem, em que contexto e com que consequências permanece uma responsabilidade humana. (Ao et al., 2025; Choudhury et al., 2025; Virós-i-Martin & Selva, 2021).

### Papel do designer, riscos e necessidade de supervisão humana

A integração da IA no processo de *design* exige uma redefinição do papel do designer, sobretudo quando a geração de alternativas, a análise de dados ou a sugestão de soluções passam a ser parcialmente mediadas por sistemas computacionais. Neste contexto, a questão central desloca-se da autoria formal para a capacidade de orientar, interpretar e avaliar criticamente os resultados produzidos. A literatura consultada descreve, assim, uma evolução do designer enquanto gerador exclusivo de forma para um papel mais híbrido, no qual assume funções de orientação, curadoria, interpretação e decisão estratégica. O papel humano torna-se particularmente exigente em tarefas como a formulação do problema, a definição de critérios, a leitura contextual, a selecção entre alternativas e a justificação das decisões. Esta transformação é especialmente relevante em domínios sensíveis, nos quais a adequação ao utilizador, a responsabilidade técnica e a aceitabilidade ética exigem supervisão humana qualificada (Figoli et al., 2022; Kadenhe et al., 2025; Virós-i-Martin & Selva, 2021).

É também neste ponto que emergem os principais riscos. Um primeiro risco é o enviesamento, já que modelos treinados com dados históricos ou desequilibrados podem reproduzir exclusões, preferências dominantes e padrões culturais pouco representativos. Um segundo risco é a opacidade: muitos sistemas produzem resultados eficazes, mas são difíceis de explicar em termos do seu raciocínio interno, o que dificulta a confiança e a responsabilização. Um terceiro risco é o erro, incluindo respostas aparentemente coerentes, mas incorrectas, simplificações abusivas e sugestões sem fundamento técnico suficiente. A estes somam-se riscos de dependência excessiva, homogeneização formal, enfraquecimento de competências críticas e incerteza quanto à autoria e originalidade dos resultados produzidos com apoio algorítmico (Burnap et al., 2019; Panchal et al., 2019; Yüksel et al., 2023).

Por estas razões, a literatura converge para a defesa de modelos com supervisão humana explícita. A integração mais robusta da IA não assenta em autonomia plena, mas em ciclos apoiados, em que o sistema acelera a análise, a geração ou a previsão e o humano mantém autoridade sobre critérios, validação e consequências da decisão. Em termos práticos, isto implica preservar mecanismos de controlo, a comparação entre alternativas, a explicitação de limites, a verificação técnica e a capacidade de recusar ou reformular sugestões produzidas pela máquina. Em *design*, a supervisão humana não é um complemento opcional; é a condição que transforma a IA em instrumento ao serviço do projecto e não em fonte acrítica de soluções aparentes (Ao et al., 2025; Kadenhe et al., 2025; Verganti et al., 2020).

### 2.7 Plataformas digitais e sistemas configuráveis

A evolução recente do desenvolvimento de produto, particularmente em contextos de saúde e de tecnologias de apoio, tem sido acompanhada pelo crescimento de plataformas digitais configuráveis e de sistemas participativos orientados para a personalização. A literatura caracteriza estes sistemas como infraestruturas sociotécnicas que articulam três dimensões principais: enquadramentos conceptuais que legitimam e estruturam a participação dos utilizadores; recursos técnicos de personalização, como parametrização, modularidade e interfaces de configuração;  e fluxos participativos que traduzem a experiência vivida em requisitos, protótipos e iterações de projecto. (Fischer et al., 2004; von Hippel & Katz, 2002; Howard et al., 2022).

Em domínios como a reabilitação e as tecnologias de apoio, a personalização é frequentemente descrita como uma necessidade funcional, distinta da diferenciação de mercado. A adequação do produto ao utilizador pode ser determinante para a segurança, a usabilidade e a adopção sustentada, deslocando o foco do *design* de uma solução «média» para sistemas capazes de acomodar diferenças individuais segundo regras definidas (Fischer et al., 2017; Kerr et al., 2024; Zhu & Zhong, 2022).

### Fundamentos conceptuais: *toolkits*, *meta-design* e *end-user development*.

Uma linha teórica relevante é a dos “*toolkits for user innovation*”, que entende os sistemas configuráveis como ferramentas coordenadas e acessíveis que transferem parte do trabalho de *design* relacionado com as necessidades dos utilizadores, enquanto fabricantes e especialistas retêm tarefas de resolução e de produção. A distinção entre configuradores, centrados em seleccionar opções, e *toolkits*, centrados em desenhar num espaço de projecto delimitado, é central: a participação pode variar entre escolher alternativas predefinidas e criar configurações num espaço de projecto delimitado, com regras, simulação e avaliação iterativa dos resultados (Franke & von Hippel, 2003; von Hippel & Katz, 2002).

O *meta-design* aprofunda esta lógica ao defender a participação “em uso”, estabelecendo condições técnicas e sociais para que os utilizadores se tornem *co-designers* e o sistema evolua ao longo do tempo. O modelo *Seeding, Evolutionary Growth, and Reseeding* formaliza este processo como alternância entre “sementes” iniciais, criadas por especialistas, evolução por meio do desenvolvimento do utilizador e reestruturações periódicas que consolidam as aprendizagens e reorganizam o sistema (Costabile et al., 2007; Fischer et al., 2004).

Para enquadrar estes fundamentos de forma mais operacional, a Figura 2.7 mostra um modelo de configuração da participação em *living labs*, útil porque desloca a discussão da participação como princípio abstrato para a participação como estrutura que pode ser planeada e configurada deliberadamente.

![](figuras/figura_2_7_participacao_cocriacao_estilizada.png)

Figura 2.7 — Modelo de processo para configurar participação em ecossistemas de inovação e cocriação.

Adaptado de Akasaka, F., Mitake, Y., Watanabe, K., & Shimomura, Y. (2022). A framework for ‘configuring participation’ in living labs. Design Science, 8, e28. [https://doi.org/10.1017/dsj.2022.22](https://doi.org/10.1017/dsj.2022.22) Licença: CC BY 4.0.

A literatura identifica, contudo, o risco de sobrecarga participativa, entendido como a transferência excessiva de trabalho, responsabilidade e decisão para os utilizadores. Este risco exige mecanismos de apoio, curadoria e reutilização que tornem a participação sustentável (Fischer et al., 2017).

Em paralelo, o conceito de *Software Shaping Workshop* operacionaliza o *meta-design*, entendido como uma abordagem que cria condições técnicas e sociais para que utilizadores finais participem ativamente na adaptação e evolução dos sistemas que utilizam. Neste enquadramento, o *Software Shaping Workshop* funciona como uma “oficina virtual”: um ambiente digital composto por ferramentas familiares, ajustadas à cultura, às práticas e às competências de uma comunidade específica. Em contextos de reabilitação e assistência, este paradigma manifesta-se em sistemas que fornecem a cuidadores e terapeutas interfaces do tipo editor, permitindo adaptar *scripts*, exercícios e conteúdos sem necessidade de programação especializada, respondendo de forma pragmática às necessidades de personalização (Costabile et al., 2007; Fischer et al., 2017).

Esta transição entre princípio e operação pode ser resumida pelos elementos nucleares apresentados na Tabela 2.2, que sistematiza dimensões recorrentes no desenho de participação mediada: quando participar, quem participa, por quais canais, através de quais pontos de contacto e com que mecanismos de motivação.

Tabela 2.2 — Elementos centrais na configuração da participação em sistemas configuráveis

| Elemento | Questão orientadora |

| --- | --- |

| Participantes | Que perfis participam, em que número e com que papel |

| Formato | Que canais, espaços e métodos suportam a colaboração |

| Contacto | Como se recrutam participantes e como se mantém a relação |

| Gestão da motivação | Que factores promovem adesão e que barreiras dificultam continuidade |

Adaptado de Akasaka, F., Mitake, Y., Watanabe, K., & Shimomura, Y. (2022). A framework for ‘configuring participation’ in living labs. Design Science, 8, e28. [https://doi.org/10.1017/dsj.2022.22](https://doi.org/10.1017/dsj.2022.22) Licença: CC BY 4.0.

### Mecanismos de personalização: modularidade, parametrização e adaptação individualizada

A literatura sintetiza a personalização por meio de mecanismos recorrentes que diferem quanto a “quem configura”, “o que é configurável” e “quando se configura”. Três mecanismos destacam-se pela relevância para sistemas protésicos e dispositivos médicos personalizados:

1. Selecção modular de componentes: a personalização resulta da combinação de módulos interoperáveis, permitindo adaptar a funcionalidade pela recombinação ou substituição dos módulos. A modularidade surge como estratégia para conciliar personalização, reutilização e expansão em ecossistemas de produto (Dechev et al., 2023; Peters & Richter, 2023).

2. Configuração paramétrica: o utilizador, ou um intermediário clínico, fornece entradas num espaço de parâmetros e o sistema gera automaticamente artefactos de *design*, como ficheiros CAD, com base nesses valores. Este mecanismo é mais adequado quando a personalização depende de atributos mensuráveis, ligando directamente dados antropométricos e cinemáticos a variáveis de projecto (Kuhl et al., 2020; Zhu & Zhong, 2022).

3. *Tailoring* por *toolkit*/editor: a personalização ocorre em tempo de uso, permitindo editar conteúdos, instruções, rotinas de treino ou componentes informacionais associados ao produto ou serviço. Em saúde, este mecanismo é particularmente relevante em plataformas de reabilitação e de telereabilitação, nas quais a adaptação de exercícios e de objectivos faz parte do cuidado contínuo (Cole, 2011; Fischer et al., 2017).

A selecção do mecanismo mais adequado depende da forma como o conhecimento relevante se distribui entre utilizadores, designers, profissionais técnicos ou clínicos e sistemas digitais. A modularidade é adequada quando as necessidades podem ser expressas através da combinação de módulos previamente definidos; a parametrização torna-se mais eficaz quando existem dados mensuráveis que podem ser traduzidos em variáveis de projecto; e os kits de ferramentas são particularmente relevantes quando a adaptação contínua em contexto é crítica e quando o utilizador ou um intermediário dispõe de conhecimento situado para ajustar o sistema. (von Hippel & Katz, 2002; Peters & Richter, 2023; Zhu & Zhong, 2022).

### Fluxos participativos e infra-estruturas remotas

Uma característica transversal é o recurso crescente à participação remota e aos processos mediados por meios digitais. A literatura documenta sessões de *co-design* por videoconferência, oficinas *online* e processos de co-fabrico à distância, em que o ciclo «definir → prototipar → fabricar → testar» ocorre com envio de protótipos para experimentação no contexto real do utilizador. Estes modelos são particularmente relevantes em tecnologias de apoio, nas quais a avaliação em contexto e a adaptação iterativa são determinantes para a adequação funcional e a aceitação (Dexter et al., 2013; Thorsen et al., 2023).

No entanto, a literatura sublinha que a tecnologia, por si só, não é suficiente. A eficácia destes sistemas depende de estruturas de governação, isto é, da definição clara de quem decide, o que decide e em que momento do processo. Depende igualmente da mediação exercida por clínicos, designers ou técnicos, bem como de mecanismos que permitam gerir a carga de trabalho, a comunicação e a coordenação entre intervenientes. Em modelos abertos e distribuídos, podem surgir riscos de incumprimento de compromissos e atrasos decorrentes da ausência de responsabilização clara, o que exige a definição explícita de regras, expectativas e responsabilidades. (Frangos et al., 2016; Hussaini et al., 2023; Kerr et al., 2024).

### Aplicações em saúde, reabilitação e próteses

Em saúde, plataformas baseadas em *digital twins* são descritas como sistemas de serviço personalizados que ligam participantes através da nuvem, integrando sensores, parâmetros de movimento e métricas de desempenho. Embora apresentem correlações elevadas em cenários controlados, a literatura assinala degradação de desempenho em contextos mais complexos, revelando diferenças entre os modelos e o movimento humano real. Estes sistemas mostram o potencial de integrar personalização, fabrico digital e monitorização remota, mas deixam claro que a robustez do modelo depende da qualidade dos dados e da diversidade dos cenários de uso (Mikołajewski et al., 2023; Zhu & Zhong, 2022).

Na reabilitação, plataformas de *virtual coaching*, *serious games* configuráveis e modelos de cocriação tecnológica são apresentados como formas de personalizar os tratamentos com base no estado clínico, nos objectivos terapêuticos e no *feedback* do utilizador. As avaliações indicam boa usabilidade e experiência do utilizador quando a participação é integrada no ciclo de desenvolvimento e abrangem a interface, a selecção de exercícios, o ritmo do programa e a mediação por profissionais de saúde (Cole, 2011; Kerr et al., 2024; Seregni et al., 2021).

No contexto protésico e das tecnologias de apoio, evidencia-se a relevância dos ecossistemas modulares e das cadeias de aprendizagem distribuída. Estudos sobre próteses pediátricas, serviços de reabilitação e modelos como o Victoria Hand Project mostram que a personalização pode combinar prototipagem iterativa, módulos intercambiáveis, criação digital de encaixes e circulação de comentários entre locais clínicos e equipas centrais de desenvolvimento. Neste enquadramento, a plataforma funciona como interface de configuração e infra-estrutura organizacional de aprendizagem e actualização contínua (Dechev et al., 2023; Howard et al., 2022; Sims et al., 2017).

Em contextos de baixos recursos, a literatura reforça que a impressão 3D pode ser um facilitador importante, mas só produz benefícios quando integrada a infraestruturas de apoio, confiança, manutenção e capacitação técnica. A simples disponibilização de tecnologia de fabrico não garante soluções adequadas nem adopção sustentada, pelo que os modelos participativos e a mediação local assumem um papel determinante na tradução do potencial técnico em valor real para os utilizadores (Hussaini et al., 2023; Thorsen et al., 2023).

### Limitações e lacunas: sustentabilidade, adopção e equilíbrio entre normalização e improviso

Apesar do potencial das plataformas configuráveis e dos fluxos participativos para apoiar a personalização de dispositivos médicos e tecnologias de apoio, a evidência empírica disponível baseia-se frequentemente em amostras reduzidas e em estudos de caso, o que limita a generalização dos resultados (Frangos et al., 2016; Howard et al., 2022; Thorsen et al., 2023). A literatura identifica ainda três tensões estruturais relevantes.

A primeira diz respeito à sustentabilidade da participação: processos participativos prolongados ou mal distribuídos podem gerar sobrecarga, fadiga e eventual desistência por parte dos utilizadores, exigindo mecanismos de apoio, curadoria e redistribuição da carga entre utilizadores, especialistas e intermediários técnicos ou clínicos (Fischer et al., 2017).

A segunda tensão situa-se entre normalização e personalização. Em domínios regulamentados, a adaptação individualizada deve preservar o registo da origem das decisões, a segurança e a qualidade, o que pode entrar em conflito com ajustamentos locais necessários para responder a necessidades específicas ou contextuais (Costabile et al., 2007; Fischer et al., 2004).

A terceira tensão relaciona-se com a adopção e o valor efectivamente realizado. A literatura sobre personalização em massa regista dificuldades recorrentes na conversão e adopção de configuradores; por analogia, em contextos de saúde e de tecnologias de apoio, a possibilidade de configuração não garante aceitação sem alinhamento com expectativas, confiança dos intervenientes e integração nos serviços existentes (Akasaka et al., 2022; Frangos et al., 2016).

### 2.8 Análise crítica do estado da arte e lacunas identificadas

A distância entre o potencial técnico destas abordagens e a sua consolidação prática torna-se particularmente visível na análise dos níveis de prontidão tecnológica descritos na literatura. A Figura 2.8 apresenta a distribuição dos estudos por nível de prontidão tecnológica, ou *Technology Readiness Level* (TRL), evidenciando que muitos contributos permanecem concentrados em fases ainda afastadas de uma adopção ampla e sustentada.

![](figuras/figura_2_8_distribuicao_trl.png)

Figura 2.8 — Número de artigos por nível de prontidão tecnológica (TRL) e categoria de aplicação. O gráfico distingue próteses de membro inferior produzidas por impressão 3D (MI 3DP), próteses de membro inferior desenvolvidas com recurso a CAD/CAM (MI CAD/CAM), outras aplicações de membro inferior (MI outras), próteses de membro superior produzidas por impressão 3D (MS 3DP) e outras aplicações de membro superior (MS outras).

Adaptado da Figura 10 de Oldfrey et al. (2024, p. 582).

A síntese das secções anteriores evidencia avanços técnicos significativos e limitações estruturais persistentes na investigação e no desenvolvimento de próteses e de tecnologias de apoio. Um tema transversal é o desfasamento entre o desenvolvimento tecnológico e a sua validação empírica. Muitos contributos permanecem em fase de protótipo, com testes realizados em amostras reduzidas e por períodos curtos, o que limita a demonstração da sua eficácia, segurança e adequação em contextos reais de utilização (Chadwell et al., 2020; Samuelsson et al., 2012; Windrich et al., 2016).

A predominância de estudos com amostras reduzidas, curta duração e validação limitada dificulta a comparação entre soluções, a generalização de conclusões e a tradução de melhorias laboratoriais em benefícios consistentes na vida quotidiana (Hafner & Sawers, 2016; Jones et al., 2023; Samuelsson et al., 2012).

### Lacuna 1 — Validação empírica limitada e fraca transposição para contextos reais de utilização

A revisão da literatura aponta repetidamente para a ausência de estudos comparativos consistentes e de ensaios clínicos que confrontem dispositivos avançados com soluções convencionalmente prescritas, particularmente no caso de próteses activas e externamente alimentadas. Em vários subdomínios, observa-se uma dependência significativa de protótipos e de amostras reduzidas, o que limita as inferências sobre eficácia, segurança e valor clínico. Em paralelo, predominam avaliações laboratoriais e tarefas pouco representativas, que não captam adequadamente o desempenho em contextos reais de utilização, marcados pela diversidade de ambientes, objectos manipulados e exigências funcionais (Ghillebert et al., 2019; Samuelsson et al., 2012; Windrich et al., 2016).

Esta lacuna é particularmente relevante porque a adaptação, a aprendizagem e o eventual abandono de uma prótese ocorrem ao longo do tempo e em contextos quotidianos, como o trabalho, a habitação e o espaço público. Quando a evidência disponível se baseia em períodos de observação curtos, torna-se difícil compreender trajetórias de adopção, padrões de uso e o surgimento progressivo de problemas relacionados com conforto, manutenção ou integração funcional (Chadwell et al., 2020; Samuelsson et al., 2012).

### Lacuna 2 — Desalinhamento entre necessidades identificadas, métricas objetivas, e qualidade de vida

Embora incidam em segmentos distintos — Cordella et al. (2016) no membro superior e Manz et al. (2022) no membro inferior — ambas as revisões identificam uma articulação insuficiente entre as necessidades expressas pelos utilizadores, como conforto, controlo intuitivo, aparência e participação social; os indicadores objectivos habitualmente medidos, como desempenho em testes funcionais, parâmetros biomecânicos e métricas instrumentadas de uso da prótese; e os resultados desejáveis, como autonomia e qualidade de vida. Salientam igualmente que estas necessidades são contextuais e interdependentes e que as medições laboratoriais nem sempre reflectem tarefas relevantes do quotidiano, contribuindo para contradições entre resultados subjectivos e objectivos (Cordella et al., 2016; Manz et al., 2022).

A convergência entre os dois domínios tem implicações directas para o *design*. A existência de métricas ecologicamente válidas e sensíveis às prioridades do utilizador é essencial para orientar decisões de projecto para benefícios significativos e sustentados. Como consequência, melhorias técnicas isoladas podem produzir ganhos limitados em termos de aceitação, integração funcional ou uso continuado da prótese (Manz et al., 2022; Samuelsson et al., 2012).

### Lacuna 3 — Persistência de problemas na interface corpo–prótese e no ajuste individualizado

Apesar dos avanços em componentes técnicos e sistemas de controlo, a literatura continua a identificar a interface corpo–prótese como um ponto crítico ainda insuficientemente resolvido. Problemas de ajuste, desconforto, irritação cutânea e dificuldade de adaptação persistem como factores determinantes de insatisfação e abandono. Nas revisões analisadas, a personalização é frequentemente descrita como insuficiente ou metodologicamente frágil, sendo a evidência difícil de sintetizar devido à heterogeneidade das intervenções e ao registo incompleto dos processos e resultados (Alluhydan et al., 2023; Baldock et al., 2023; Richardson & Dillon, 2017).

Um aspecto estruturante desta lacuna é a ausência de fluxos metodológicos consistentes e acessíveis que articulem medição, decisão de projecto e validação. Esta ausência dificulta a utilização de dados objectivos para orientar ajustes individualizados. Mesmo quando são propostas soluções baseadas em sensores e na monitorização do uso, persistem barreiras práticas, como o custo, a autonomia da bateria, a disponibilidade de equipamentos e a necessidade de formação técnica, o que limita a sua adopção como prática clínica regular (Chadwell et al., 2020; Richardson & Dillon, 2017).

### Lacuna 4 — Evolução limitada das estratégias de controlo e da interacção utilizador–prótese

No caso das próteses de membro superior, algumas revisões apontam para uma evolução limitada das estratégias de controlo em aplicações comerciais, marcada por uma progressão lenta desde as primeiras abordagens desenvolvidas no século XX. Persistem dificuldades relacionadas com a robustez dos sistemas e com a sua transferência entre cenários laboratoriais e contextos reais de utilização, bem como desafios associados ao esforço cognitivo, ao tempo de aprendizagem e à inconsistência do desempenho em situações quotidianas (Cordella et al., 2016; Marinelli et al., 2022).

Esta lacuna não é apenas técnica. Reflete também uma conceptualização ainda insuficiente da interacção utilizador–prótese enquanto sistema integrado, no qual controlo, informação sensorial, treino e contexto de uso devem ser considerados em conjunto (Domínguez-Ruiz et al., 2023; Marinelli et al., 2022).

### Lacuna 5 — Acesso, custo, manutenção e inequidades sistémicas

A acessibilidade surge como um constrangimento central e persistente, tanto em contextos de baixos recursos quanto em sistemas de saúde mais robustos. Revisões identificam barreiras associadas a custos elevados, à necessidade de formação especializada, a atrasos na prestação de cuidados e a pressões sistémicas que levam os utilizadores a negociar intensivamente para obter soluções adequadas. Em contextos de baixos e médios rendimentos, enfatizam-se ainda problemas de durabilidade e de manutenção, com compromissos claros: soluções biomecanicamente mais sofisticadas podem ser mais frágeis e difíceis de manter, comprometendo a sustentabilidade do uso (Alluhydan et al., 2023; Andrysek, 2010; Baumann & Maria, 2023).

Assim, a inovação pode agravar as inequidades ao introduzir dependências de infraestrutura, de apoio técnico e de cadeias de fornecimento indisponíveis para uma parcela significativa da população (Andrysek, 2010; Segura et al., 2024).

### Lacuna 6 — Envolvimento do utilizador e registo metodológico insuficiente

O envolvimento do utilizador permanece uma fragilidade metodológica e ética no desenvolvimento de próteses. As revisões relacionam processos pouco ajustados às necessidades individuais dos utilizadores com o abandono dos dispositivos e a dificuldade em responder a prioridades relevantes de uso. Em várias áreas, identifica-se ainda a ausência de métodos qualitativos sistemáticos para captar a experiência, a aceitação e os factores de rejeição, mesmo em componentes directamente associados ao conforto, como os revestimentos de interface. Esta limitação reduz a compreensão dos factores que condicionam a adopção, a continuidade de uso e a adequação da prótese à vida quotidiana (Marinelli et al., 2022; Richardson & Dillon, 2017; Walker et al., 2019).

Adicionalmente, a heterogeneidade metodológica e a ausência de critérios comuns de avaliação, como escalas partilhadas de utilidade e satisfação, dificultam a síntese dos resultados e a realização de meta-análises, mantendo o campo fragmentado e com baixa comparabilidade entre estudos (Cordella et al., 2016; Hafner & Sawers, 2016; Richardson & Dillon, 2017).

### Implicações para esta investigação

Em conjunto, estas lacunas apontam para a necessidade de abordagens que:

- reforcem a ligação entre personalização e validação empírica, através de fluxos integrados de aquisição de dados, geração de variantes e avaliação;

- privilegiem avaliações ecologicamente válidas e longitudinais, aproximando as métricas de desempenho dos resultados relacionados com participação, autonomia e qualidade de vida;

- tratem a interface corpo–prótese e o conforto como requisitos estruturantes do processo de projecto, e não como ajustes posteriores;

- incorporem o envolvimento do utilizador como elemento contínuo, documentável e passível de análise, articulando métodos qualitativos e quantitativos;

- considerem a acessibilidade, a manutenção e o contexto de serviço como dimensões constitutivas do problema de *design* (Anderson et al., 2024; Baumann & Maria, 2023; Chadwell et al., 2020).

Estas necessidades excedem, contudo, a evidência que uma prova de conceito técnica pode produzir. A presente investigação selecciona como unidade de análise o encadeamento entre dados, parâmetros, geometria, interface e materialização preliminar. Por conseguinte, não procura resolver integralmente as seis lacunas identificadas, mas examinar mecanismos de projecto e condições de verificabilidade que podem apoiar etapas posteriores de avaliação clínica, funcional e participativa. A Tabela 2.3 explicita esta delimitação e estabelece o quadro retomado na discussão dos resultados.

Tabela 2.3 — Correspondência entre lacunas do estado da arte, resposta da investigação e limites de avaliação

| Lacuna do estado da arte | Requisito seleccionado para o estudo | Resposta incorporada no protótipo ou no método | Evidência prevista | Dimensão excluída da avaliação |
| --- | --- | --- | --- | --- |
| Validação empírica limitada e fraca transposição para contextos reais (Chadwell et al., 2020; Samuelsson et al., 2012; Windrich et al., 2016) | Tornar verificável a cadeia técnica desde a entrada até à geometria e à preparação para fabrico | Registo de iterações, casos, parâmetros, exportações, preparação e protótipos físicos | Ensaios da plataforma, cenários simulados, medição digital e observação material preliminar | Eficácia, segurança, utilização quotidiana e avaliação longitudinal |
| Desalinhamento entre necessidades, métricas objectivas e qualidade de vida, identificado em revisões dos membros superior e inferior (Cordella et al., 2016; Manz et al., 2022) | Distinguir mecanismos de projecto observáveis de efeitos humanos esperados | Matriz entre perguntas, métodos, evidência e limites; separação entre configuração técnica e resultados humanos | Correspondência metodológica e discussão explícita do grau de resposta | Preferências, satisfação, participação, autonomia e qualidade de vida |
| Problemas persistentes na interface corpo–prótese e no ajuste individualizado (Alluhydan et al., 2023; Baldock et al., 2023; Richardson & Dillon, 2017) | Relacionar referências antropométricas, parâmetros editáveis e geometria gerada | Regras dimensionais, limites específicos dos modelos e verificação da propagação geométrica | Comparação de perfis de ensaio, extensões de malha e materialização de variantes | Ajuste ao membro residual, pressão de contacto, conforto e adequação anatómica individual |
| Evolução limitada do controlo e da interacção utilizador–prótese (Domínguez-Ruiz et al., 2023; Marinelli et al., 2022) | Delimitar o controlo humano sobre a configuração digital | Separação entre sugestão probabilística, regras determinísticas e decisão humana antes da exportação | Casos de aplicação, rejeição e recuperação de sugestões paramétricas | Controlo da prótese em utilização, aprendizagem motora e desempenho funcional |
| Barreiras de acesso, custo, manutenção e contexto de serviço (Andrysek, 2010; Baumann & Maria, 2023; Segura et al., 2024) | Explorar uma arquitectura configurável baseada em tecnologias *web*, modelos abertos e execução local da geometria | Plataforma no navegador, modelos parametrizados e exportação para ferramentas de fabrico aditivo | Funcionamento técnico dos módulos e preparação de ficheiros em dois ambientes registados | Custos totais, conectividade, competências, manutenção, implantação e escalabilidade socioeconómica |
| Envolvimento do utilizador e registo metodológico insuficiente (Hafner & Sawers, 2016; Richardson & Dillon, 2017; Walker et al., 2019) | Tornar documentáveis as decisões, iterações, falhas e limites do processo | Ciclos de *Research Through Design*, inventário de modelos, protocolos e anexos de suporte | Correspondência documentada entre problema observado, decisão, alteração e resultado | *Co-design*, avaliação de usabilidade e validação com participantes |

O âmbito empírico incide, assim, na verificabilidade técnica e no registo do processo. As dimensões clínicas, experienciais e socioeconómicas permanecem requisitos sustentados pela literatura e orientações para investigação futura, não resultados antecipados do presente estudo.

## Capítulo 3 — Metodologia de Investigação

### 3.1 Enquadramento metodológico e abordagem *Research Through Design*

A presente investigação é aplicada e segue o enquadramento de *Research Through Design* (RTD). Nesta abordagem, a concepção, a experimentação, a prototipagem e a reflexão crítica constituem actividades de investigação através das quais o artefacto permite formular e examinar conhecimento de projecto (Frayling, 1994; Zimmerman et al., 2007). O artefacto central é um protótipo de investigação: uma plataforma *web* que coordena modelos paramétricos de mão protésica, dados antropométricos, sugestões geradas por IA, visualização tridimensional e exportação para fabrico.

O conhecimento produzido decorre das relações e dos limites revelados durante a construção. A integração de modelos *open source* mostrou que cada família possui pressupostos dimensionais próprios; os ensaios de ponta a ponta revelaram falhas que a inspecção isolada dos valores não mostrava; e a impressão tornou visíveis condicionantes de orientação, escala, separação de peças e preparação. Estes resultados foram usados para reformular o sistema e, em seguida, voltar a examiná-lo. O RTD concretiza-se, assim, numa sequência explícita de situação problemática, decisão de *design*, artefacto, ensaio, resultado e alteração.

O modelo *Double Diamond* organiza os momentos de descoberta, definição, desenvolvimento e entrega, sem impor uma sequência linear. A sua função é estruturar a abertura e a convergência dos ciclos, enquanto o RTD enquadra a produção de conhecimento através desses ciclos (Design Council, 2020). A Tabela 3.1 apresenta as iterações técnicas com maior relevância para o argumento da dissertação.

Tabela 3.1 — Ciclos de *Research Through Design* documentados no desenvolvimento

| Situação examinada | Artefacto ou ensaio | Resultado observado | Decisão incorporada |
| --- | --- | --- | --- |
| Preparação de modelos compostos para impressão | Ensaios de exportação em placa | A posição montada originava peças suspensas ou exigia suportes desnecessários | Criação de modos de impressão planos e assentamento de cada peça em Z=0 |
| Selecção de referência antropométrica | Ensaios com descrições, unidades e grupos etários | Unidades como «mm» e «cm» podiam ser interpretadas como indicação de sexo masculino | Análise por palavras completas, reconhecimento multilingue e classificação etária |
| Propagação da largura da palma no Paraglider | Sugestão de IA, exportação e medição da malha | Os dedos respondiam ao perfil, mas a palma permanecia na escala interna da biblioteca | Aplicação da escala no ponto de chamada da palma Reborn |
| Limite dimensional do UnLimbited Phoenix | Perfil infantil e exportação | Um percurso alternativo aceitava uma escala inferior ao mínimo definido pelo modelo | Aplicação do intervalo de 100% a 160% nos dois percursos de escala |
| Definição do lado da mão | Cenários repetidos de mão esquerda e direita | A IA devolvia mão direita em pedidos explícitos de mão esquerda | Lateralidade retirada do conjunto sugerível e controlada pela interface |
| Informação de cor no fabrico | Exportação 3MF | O STL não preservava unidades e materiais por peça | Exportação 3MF com unidade em milímetros e materiais derivados das cores |

A Figura 3.1 apresenta um precedente interdisciplinar que inclui avaliação clínica e participação de utilizadores. No presente estudo, a figura funciona como referência para um processo futuro mais amplo; essas actividades clínicas e participativas não foram executadas nesta investigação (Silva et al., 2018).

![](figuras/figura_3_1_processo_interdisciplinar_estilizada.png)

Figura 3.1 — Processo interdisciplinar de desenvolvimento de uma prótese de membro superior impressa em 3D.

Adaptado de Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

### 3.2 O *design* industrial como prática de investigação

Com base no enquadramento do Capítulo 2, o *design* industrial é operacionalizado como prática de investigação através da explicitação e do ensaio das traduções entre fontes antropométricas, parâmetros editáveis, regras geométricas, estados da interface e peças fabricadas. Esta opção relaciona-se com os *designerly ways of knowing*, que reconhecem a experimentação material e a formulação do projecto como modos de produção de conhecimento (Cross, 1982). A unidade de análise é, portanto, a cadeia de decisões e transformações do protótipo, e não a experiência de uma pessoa utilizadora.

O contributo é examinado pela capacidade de localizar a origem de cada valor, observar a sua propagação e documentar falhas e alterações. Desempenho clínico e efeitos na experiência de pessoas amputadas não foram avaliados; a dimensão humana funciona neste estudo como requisito e limite ético fundamentado na literatura.

A hipótese principal sustenta que a integração de *design* paramétrico e de ferramentas de inteligência artificial permite desenvolver próteses mais adequadas às necessidades anatómicas e funcionais dos utilizadores, tornando o processo de personalização mais acessível e escalável, especialmente em contextos economicamente desfavorecidos. As hipóteses secundárias aprofundam esta perspetiva, sugerindo que a combinação de princípios de *design* inclusivo, *Design for Additive Manufacturing* (DfAM) e processos participativos pode melhorar a usabilidade, o conforto e a aceitação, ao mesmo tempo que reduz a dependência de especialistas.

Estas formulações correspondem às hipóteses aprovadas para o projecto e mantêm-se como orientação geral da investigação. A componente empírica não abrangeu participantes, comparação com um processo de referência, implantação em contextos economicamente desfavorecidos ou medição de conforto, usabilidade e aceitação. Assim, as hipóteses não são tratadas como integralmente confirmadas ou rejeitadas. O estudo examina o seu suporte ao nível dos mecanismos de projecto: configuração dimensional, visualização, controlo dos parâmetros, revisão humana das sugestões de IA, geração geométrica e preparação para fabrico. Os efeitos desses mecanismos na experiência e na utilização permanecem por avaliar.

### 3.3 Estrutura metodológica do projecto

A metodologia aprovada organiza-se em três fases interligadas — conceptual, metodológica e empírica —, articuladas por ciclos de divergência e convergência do *Double Diamond*. A fase conceptual reúne a revisão crítica da literatura, a análise de soluções *open source* e a definição dos requisitos. A fase metodológica estrutura a base antropométrica, integra os modelos OpenSCAD e implementa a plataforma e o módulo de IA. A fase empírica usa cenários simulados, registos de execução, malhas exportadas, perfis de preparação para impressão e protótipos físicos. Os resultados de cada fase regressam ao desenvolvimento através dos ciclos de *Research Through Design* apresentados na Tabela 3.1. As verificações complementares documentadas nos Anexos B e D aprofundam esta fase empírica sem alterar o desenho metodológico aprovado.

Tabela 3.2 — Correspondência entre perguntas, actividades, evidência e limites

| Pergunta de investigação | Actividades realizadas | Evidência produzida | Dimensões fora da avaliação |
| --- | --- | --- | --- |
| Personalização, conforto, adequação funcional, acessibilidade e controlo sobre o projecto | Definição de parâmetros, implementação da plataforma, cenários de IA, exportação e impressão | Regras documentadas, respostas JSON, malhas, correcções de escala, opções de controlo e peças físicas | Conforto percebido, adequação anatómica individual, desempenho funcional em uso e acessibilidade avaliada com participantes |
| Eficácia, usabilidade, durabilidade e possibilidade de reproduzir os resultados | RTD, ensaios unitários, cenários de ponta a ponta, inspecção geométrica, preparação para impressão e medição dimensional | Registo das iterações, dez testes unitários aprovados, quatro projectos de preparação digital para impressão 3D, doze casos sob condição digital comum, 36 extensões X/Y/Z das malhas e 72 medições físicas das palmas em PLA e PETG | Eficácia protésica, usabilidade com participantes, durabilidade, ensaios mecânicos, estimativa da incerteza de medição e montagem funcional completa |
| Conciliação de requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos | Revisão da literatura, selecção de parâmetros, separação de permissões, visualização e opções de cor | Decisões de projecto, grupos de parâmetros, escolhas visuais e exportação 3MF com materiais | Aceitação, dignidade, autonomia quotidiana e avaliação situada dos significados estéticos e simbólicos |

Foram seleccionados para a comparação o Flexy Beast, o Paraglider Hand e a UnLimbited Phoenix porque, no momento dos ensaios principais, constituíam os três modelos activos com conjuntos de peças exportáveis e representavam estratégias distintas de transformação: escala inicial com proporções digitais, escala herdada com correcções localizadas e escala global limitada por um valor mínimo. O Cyborg Beast foi integrado posteriormente e, por isso, permanece como evolução do projecto documentada no Anexo C, sem ser acrescentado retroactivamente às séries comparativas.

Os quatro perfis de ensaio — `child_8`, `teen_15`, `adult_28` e `elderly_70` — foram escolhidos para abranger conjuntos dimensionais diferentes, incluindo uma configuração reduzida, duas configurações progressivamente maiores e uma configuração posterior com dimensões inferiores às do adulto. As idades funcionam apenas como identificadores dos cenários. Não constituem a variável independente do ensaio, não representam grupos populacionais e não sustentam inferências sobre crescimento ou envelhecimento.

Os estados examinados são identificados pela actividade a que correspondem. Os ensaios iniciais de correspondência e geometria incidiram no estado usado nos ensaios principais; as séries complementares da plataforma do Anexo B foram executadas num estado posterior; e a descrição técnica considera o estado final examinado. A preparação para fabrico do Anexo D incidiu sobre os projectos de preparação digital para impressão 3D com configuração analisada e identifica autonomamente as versões dos programas usados. Esta separação evita apresentar o estado actual do protótipo como se correspondesse exactamente ao estado de todas as execuções preservadas.

Tabela 3.3 — Métodos, unidades de análise, critérios e localização dos resultados

| Método ou actividade | Unidade de análise | Dados e instrumento | Critério de leitura | Resultado ou localização |
| --- | --- | --- | --- | --- |
| Ciclos de *Research Through Design* | Episódio de desenvolvimento | Estado, problema observado, alteração e novo ensaio | Existência de uma relação explícita entre observação e decisão de projecto | Tabelas 3.1 e 4.11 |
| Verificação técnica da plataforma | Percurso ou caso definido | Ensaios automatizados, estados da interface e ficheiros exportados | Resultado esperado por caso; dez conclusões previstas na repetição de cada modelo | Capítulo 8 e Anexo B; critério de repetição parcialmente atingido |
| Sugestões de IA | Resposta individual e invariantes do esquema | Respostas JSON, metadados, intervalos e relações dimensionais | Estrutura válida, campos permitidos, limites e relações declaradas | Secção 8.2; sem estudo estatístico de chamadas reais repetidas |
| Inspecção geométrica | Malha ou peça digital exportada | Análise 3MF, `trimesh`, extensões X/Y/Z, volume, corpos e faces degeneradas | Descrição das propriedades geométricas e confirmação da propagação; não equivale a resistência | Secção 8.1.3 e Anexo D |
| Série A — projectos de preparação digital para impressão 3D com configuração analisada | Projecto de preparação | Quatro projectos, Bambu Studio 01.10.02.76 e PrusaSlicer 2.8.1 | Geração de trajectórias e de estimativas de tempo, filamento e massa | 4/4 projectos processados; valores não comparáveis directamente entre equipamentos |
| Série B — condição digital comum | Combinação modelo–perfil | Três modelos × quatro perfis; Bambu Lab A1 virtual, PLA, camada 0,20 mm, duas paredes, enchimento de 15% e suportes desligados | Trajectórias e estimativas geradas, com avisos preservados | 12/12 casos processados; comparação limitada à exigência digital de preparação |
| Observação dos protótipos existentes | Peça física identificada | Fotografias e registos de material | Existência da peça e observação visual da materialização | Secção 8.1.3; sem inferência dimensional ou mecânica |
| Medição física e montagem | Palma impressa ou protótipo completo | Paquímetro; um valor registado em X/Y/Z por palma em PLA e PETG; folha de cinco ciclos de articulação | Desvio malha–peça; colisões, fecho e retorno quando aplicáveis | 72 comparações dimensionais no Anexo D; montagem e articulação ainda sem resultados sistemáticos |

O material suplementar entregue com a dissertação encontra-se organizado na pasta
`suplementos/` em quatro conjuntos: Suplemento 1 — Dados antropométricos;
Suplemento 2 — Avaliação técnica da plataforma; Suplemento 3 — Parametrização e
percurso numérico; e Suplemento 4 — Preparação para impressão e protótipos. O
ficheiro `guia_dos_suplementos.md` apresenta o conteúdo de cada conjunto. O
ficheiro `manifesto_ficheiros.csv` relaciona cada elemento com a sua origem e
função.

### 3.4 Métodos de recolha e análise de dados

A recolha combinou análise documental, comparação de precedentes, inspecção do código, construção paramétrica, cenários automatizados, medição de malhas, preparação para impressão, observação de peças físicas e reflexão sobre cada ciclo. Os dados usados na análise foram: parâmetros e limites declarados no catálogo de modelos; respostas JSON e metadados de execução; dimensões das malhas exportadas; relatórios técnicos por modelo; ficheiros 3MF; quatro projectos com parâmetros de preparação; resultados de doze casos sob uma condição digital comum; fotografias dos protótipos; e registos de alterações do código.

A preparação para impressão converte a geometria numa sequência de camadas e trajectórias de deposição, definindo altura de camada, paredes, enchimento, suportes, temperaturas e orientação. A Série A constitui uma verificação técnica complementar da fase empírica aprovada e documenta quatro ficheiros de preparação: três foram configurados no Bambu Studio 01.10.02.76 para a impressora Bambu Lab A1 — Flexy Beast em PLA e UnLimbited Phoenix em PLA e PETG — e um foi configurado no PrusaSlicer 2.8.1 para a Prusa MINI — Paraglider Hand em PLA. Os ficheiros preparados no Bambu Studio usam camada de 0,24 mm, duas paredes, enchimento de 15% em grelha e suporte em árvore orgânica; o ficheiro preparado no PrusaSlicer usa camada de 0,20 mm, dois perímetros, enchimento de 15% e suporte desactivado. Como geometria, programa, impressora, material e condições não são equivalentes, esta série descreve cada preparação e não permite comparar desempenho entre equipamentos ou materiais.

A Série B complementa essa verificação sem constituir uma nova metodologia. Introduz uma condição digital comum para comparar a exigência de preparação dos três modelos nos quatro perfis. Foram fixados Bambu Lab A1 com bico de 0,4 mm, Bambu PLA Basic, camada de 0,20 mm, duas paredes, enchimento de 15% em grelha e suportes desligados. A orientação exportada foi mantida e o programa dispôs as peças nas placas. Os doze casos produziram trajectórias e estimativas de tempo, filamento e massa. Os avisos relativos a regiões suspensas foram mantidos como resultados; a conclusão do processamento não demonstra que a peça possa ser impressa fisicamente sem rever a orientação ou os suportes.

A análise dimensional incidiu nas palmas isoladas dos mesmos doze casos. Foram extraídas 36 extensões exteriores — X, Y e Z — a partir das malhas 3MF. Estes valores descrevem a caixa envolvente da peça. Não são automaticamente equivalentes a larguras, comprimentos ou espessuras anatómicas, porque as geometrias podem incluir abas, interfaces e margens de montagem. As mesmas extensões foram medidas nas palmas produzidas em PLA e PETG, à temperatura ambiente, num total de 72 valores físicos. O desvio dimensional foi calculado entre cada valor físico e a extensão correspondente da malha, no mesmo referencial, e não entre o parâmetro antropométrico e a caixa exterior.

A materialização recorreu a uma Bambu Lab A1 com sistema AMS e a uma Prusa MINI, ambas baseadas em fabrico por filamento fundido. As fotografias confirmam a existência das peças e permitem observar diferenças de escala entre os perfis. Os diagnósticos dos programas e a inspecção geométrica independente usam critérios diferentes e foram conservados separadamente: a aceitação pelo programa de preparação não implica uma malha fechada e sem faces degeneradas. As medições físicas sustentam a comparação dimensional das palmas nos eixos X, Y e Z. Porém, a ausência de leituras repetidas, ensaios de carga e registos completos de montagem impede estimar a incerteza de medição e não permite inferir resistência, conforto, segurança ou durabilidade.

O registo dimensional reúne um valor por eixo e por palma, obtido com paquímetro nas extensões X, Y e Z, à temperatura ambiente. Este conjunto permite calcular o desvio entre a malha e a peça, mas não a média, a amplitude entre repetições ou a incerteza associada ao reposicionamento do instrumento. A comparação é, por isso, assumida como descritiva. Três leituras independentes apenas seriam necessárias numa futura caracterização metrológica da dispersão e da incerteza, que não integra o âmbito deste estudo. A montagem sistemática também ficou fora da avaliação; consequentemente, os resultados não são usados para afirmar adequação anatómica ou funcional.

Não são recolhidos dados pessoais ou biométricos de utilizadores reais; utilizam-se exclusivamente conjuntos de dados antropométricos públicos, o que delimita o âmbito empírico ao domínio técnico e de desenvolvimento do projecto. Entre estes, destaca-se a base local consolidada de medidas da mão e do membro superior distal, usada como infraestrutura intermédia para a selecção, comparação e normalização de medidas relevantes para a parametrização geométrica. A organização dos dados preserva informação sobre país, amostra, tipo de medida, estatística, fonte documental e granularidade dos subconjuntos analisados, tornando explícitas a cobertura e as limitações de cada fonte antes da sua tradução em parâmetros de projecto.

Embora o presente estudo não utilize participantes, a literatura metodológica ajuda a esclarecer como medições lineares e procedimentos de ajuste são operacionalizados em contextos aplicados. A Figura 3.2 constitui um precedente para a tradução de medidas em parâmetros de projecto; não representa um procedimento realizado nesta investigação.

![](projecto-completo_media/image11.png)

Figura 3.2 — Exemplo de recolha dimensional para ajuste de prótese impressa em 3D.

Reproduzido de Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

### 3.5 Critérios de avaliação e limitações metodológicas

A avaliação usa seis critérios principais: conformidade da saída com o esquema; respeito pelos intervalos declarados; preservação das relações dimensionais definidas; aplicação dos valores na geometria; conclusão dos fluxos principais da plataforma; e preparação digital das peças. Cada critério tem uma evidência observável: resposta JSON, comparação numérica, malha exportada, estado da interface, ficheiro de projecto ou trajectórias geradas pelo programa de preparação. Na Série A, o critério foi a obtenção de trajectórias e estimativas nos quatro projectos com configuração analisada; na Série B, foi a obtenção desses resultados nos doze casos sob a condição comum, mantendo avisos e falhas. A estanquidade, os corpos e as faces degeneradas são descritores geométricos, não critérios de desempenho estrutural.

«Verificação» designa a confirmação de uma condição especificada; «avaliação» designa a interpretação conjunta dos resultados; «prova de conceito» designa o protótipo integrado. O termo «validação clínica» fica reservado a estudos com métodos, profissionais e participantes adequados, ausentes neste trabalho.

Como complemento à avaliação inicial, foram executadas, em 13 e 14 de Julho de 2026, séries automatizadas de ensaios orientadas para três qualidades relevantes do processo de *design*: consistência da geração paramétrica, capacidade de recuperação perante valores ou falhas previsíveis e acessibilidade técnica da interacção. Os ensaios locais decorreram numa instância isolada, com perfis de ensaio, para não alterar os dados de desenvolvimento ou da plataforma pública. A versão pública, disponível em `https://handfab.pedrocandeias.net/`, foi examinada apenas na superfície não autenticada. O protocolo, os casos e os resultados completos são apresentados no Anexo B. Estes ensaios avaliam o comportamento técnico do protótipo; não constituem avaliação de usabilidade com participantes nem certificação de acessibilidade.

No módulo de IA, os critérios incidem na estrutura da resposta, nos limites e nas relações dimensionais internas. Não existe uma medida individual de referência para calcular erro anatómico. As respostas geradas são sugestões iniciais e podem diferir entre execuções; o estudo documenta exemplos e invariantes, sem estimar uma distribuição estatística do comportamento do modelo de linguagem.

As limitações principais são a ausência de participantes, dados clínicos, medições directas da mão, repetições controladas das medições dimensionais, ensaios biomecânicos, protocolos normalizados de resistência, montagem funcional completa, estudo longitudinal de desgaste e avaliação de usabilidade. Os dados populacionais apresentam diferenças de população, idade, sexo, lateralidade e método de medição. Os casos simulados representam situações de teste e não pessoas. A plataforma é um protótipo de investigação em `staging`, sem certificação como dispositivo médico e sem prontidão demonstrada para utilização clínica ou doméstica. Estas limitações delimitam a força das conclusões, sem invalidar o estudo técnico que foi efectivamente realizado.

## Capítulo 4 — Desenvolvimento do Modelo Paramétrico

Este capítulo trata um subconjunto delimitado do problema das próteses de membro superior: a adaptação paramétrica de modelos mecânicos passivos de mão destinados à exploração técnica e à prototipagem por fabrico aditivo. O trabalho implementado não inclui actuadores, sensores, fontes de energia, controlo mioeléctrico, desenho clínico de encaixes ou avaliação funcional com utilizadores. Estes temas permanecem no enquadramento geral da literatura, mas não constituem propriedades demonstradas pelo artefacto.

A biblioteca examinada compreende quatro modelos integrados na plataforma: Flexy Beast, Paraglider Hand, UnLimbited Phoenix Hand e Cyborg Beast. Os três primeiros integram a comparação dimensional e os ensaios descritos no Capítulo 8. O Cyborg Beast foi integrado posteriormente e é analisado como evolução do projecto, sem ser incluído nas séries comparativas ou físicas. O inventário dos modelos, com origem, licença, estratégia de escala e evidência disponível, é apresentado na Tabela 5.3.

A unidade de análise é a relação entre um vector de parâmetros, a regra geométrica específica de cada modelo e a malha gerada. «Adaptação paramétrica» designa aqui a capacidade de modificar dimensões segundo as relações e os limites codificados. Não designa ajuste anatómico validado, conforto, eficácia protésica ou segurança clínica.

### 4.1 Definição do problema de *design* e requisitos

Como referido anteriormente, o desenvolvimento de próteses de membro superior é enquadrado na literatura como um problema de elevada complexidade, situado na intersecção entre desempenho biomecânico, integração corpo-dispositivo e experiência vivida do utilizador (Cordella et al., 2016; Guo, 2025; Peerdeman et al., 2011). Este desafio ultrapassa a replicação formal da mão ou do segmento ausente. Implica a concepção de dispositivos capazes de conciliar funcionalidade, conforto, leveza, funcionamento consistente, controlo compreensível, aceitação estética e custos compatíveis com a produção, adaptação, manutenção e acesso continuado à prótese, num contexto em que continuam a registar-se taxas elevadas de rejeição e abandono.

A literatura associa recorrentemente estas taxas a desconforto no encaixe, peso excessivo, limitações funcionais, baixa robustez e estratégias de controlo pouco intuitivas, evidenciando uma lacuna persistente entre a capacidade tecnológica dos dispositivos e as necessidades reais de uso (Biddiss et al., 2007; Cordella et al., 2016; Peerdeman et al., 2011).

A literatura descreve requisitos funcionais, ergonómicos, técnicos, produtivos e psicossociais que devem convergir num dispositivo protésico (Biddiss et al., 2007; Brack & Amalu, 2021; Henao et al., 2025; Walker et al., 2019). Neste estudo, porém, apenas três grupos foram traduzidos em propriedades observáveis do protótipo: dimensões e relações geométricas; preservação de interfaces mecânicas herdadas; e preparação preliminar para fabrico aditivo. Conforto, usabilidade, força, amplitude funcional, durabilidade, segurança, aceitação e incorporação corporal não foram operacionalizados nem avaliados.

Os requisitos implementados foram, assim, formulados como condições de projecto: aceitar um conjunto explícito de entradas; aplicar relações determinísticas; preservar furos, eixos e zonas de montagem quando a geometria varia; manter os valores na gama declarada; permitir isolar e exportar componentes; e tornar visíveis as situações em que um perfil ultrapassa a cobertura do modelo. Estas condições permitem examinar coerência e comportamento geométrico, mas não substituem requisitos clínicos ou funcionais.

No âmbito deste projecto, os limites de adaptação foram formalizados como relações explícitas entre medidas, componentes e restrições de fabrico. A verificação foi definida para incidir sobre a geometria efectivamente gerada, e não apenas sobre o nome do parâmetro ou o intervalo apresentado na interface.

### 4.2 Parâmetros antropométricos e estrutura do modelo

No desenvolvimento de sistemas protésicos personalizados, as medições corporais funcionam como elemento de ligação entre o corpo do utilizador e a configuração geométrica e funcional do modelo paramétrico. No contexto das próteses de membro superior, estas medições não devem ser tratadas como valores isolados, mas como componentes de um sistema estruturado capaz de descrever a morfologia da mão, dos dedos, do punho e, quando aplicável, do antebraço ou do membro residual. A literatura recente converge em dois pontos: a personalização eficaz depende de medidas anatomicamente relevantes, e não de escalonamentos genéricos; e essas medidas devem ser organizadas de modo a alimentar directamente a lógica do modelo digital (Chatzioglou et al., 2024; Moreo, 2016; Rodríguez-Vega & Rodríguez-Vega, 2024).

Esta exigência de organizar as medições em parâmetros operáveis é particularmente evidente nos modelos digitais do dedo e da mão. A Figura 4.1 mostra um exemplo de decomposição paramétrica em comprimentos, larguras e secções articulares e torna explícita a estrutura dimensional que sustenta a transição da antropometria para a geometria configurável.

![](figuras/figura_4_1_parametros_antropometricos_dedos.png)

Figura 4.1 — Parâmetros antropométricos utilizados na modelação paramétrica de dedos protésicos.

Adaptado de Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. [https://doi.org/10.1109/BioRob60516.2024.10719909](https://doi.org/10.1109/BioRob60516.2024.10719909)

Os parâmetros antropométricos mais relevantes concentram-se, em primeiro lugar, na definição da estrutura dimensional base da mão. Medidas como o comprimento da mão, a largura da mão e o comprimento da palma constituem descritores dimensionais primários, permitindo estabelecer a escala do modelo e definir a sua organização geral. Para além destas, incluem-se parâmetros relativos aos dedos, como comprimentos segmentares e proporções entre falanges, bem como as dimensões do polegar e do punho, essenciais para a funcionalidade e a integração da mão protésica no uso quotidiano (Chatzioglou et al., 2024; Nag et al., 2003).

Tabela 4.1 — Principais parâmetros antropométricos da mão e do membro superior relevantes para modelação paramétrica

| Região | Parâmetro | Definição dimensional | Utilização potencial no modelo |

| --- | --- | --- | --- |

| Mão | Largura da mão | Distância entre metacarpos II e V | Definição do volume da palma |

| Palma | Comprimento da palma | Base do dedo médio até ao punho | Estrutura e proporção da palma |

| Dedos | Comprimento dos dedos | MCP até ponta | Dimensionamento funcional |

| Dedos | Proporções falângicas | Relação entre segmentos | Definição cinemática |

| Dedos | Largura/profundidade | Secção transversal | Ajuste estrutural e estético |

| Polegar | Comprimento e orientação | Geometria e oposição | Preensão e usabilidade |

| Punho | Largura/profundidade | Dimensões do punho | Interface estrutural |

| Antebraço | Circunferência/comprimento residual | Medidas do membro residual | Ajuste do encaixe |

### Conjuntos mínimos de parâmetros por nível de amputação

O conjunto mínimo de parâmetros antropométricos varia em função do nível de amputação, dado que diferentes configurações protésicas exigem níveis distintos de detalhe dimensional. A redução das medições necessárias contribui para processos de personalização mais escaláveis e acessíveis, particularmente quando a recolha de dados é realizada fora de contextos clínicos especializados. (Moreo, 2016; Romero et al., 2025).

Tabela 4.2 — Conjuntos mínimos de parâmetros por nível de amputação

| Nível de ausência do membro | Conjunto mínimo proposto pela literatura |

| --- | --- |

| Desarticulação do punho | Largura e profundidade do punho, comprimento da mão |

| Parcial da mão | Comprimento da palma, dimensões dos dedos remanescentes |

| Dedos (parcial) | Comprimento e largura do dedo, proporções falângicas |

| Mão completa (cosmética/funcional) | Comprimento da mão, largura da palma, comprimento dos dedos |

Esta lógica permite estruturar o sistema paramétrico a partir de entradas essenciais, controlando a complexidade inicial do processo sem inviabilizar a geração de uma solução funcional. Importa, contudo, distinguir entre parâmetros mínimos de configuração e parâmetros de refinamento: os primeiros permitem gerar uma instância funcional do modelo; os segundos aumentam o grau de especificidade da configuração, permitindo afinar a coerência proporcional, a adequação geométrica ou o desempenho cinemático quando existem dados adicionais disponíveis.

### Limitações do redimensionamento proporcional

Uma limitação recorrente em abordagens simplificadas de modelação é o uso de redimensionamento proporcional (*uniform scaling*), no qual um modelo base é dimensionado proporcionalmente em todas as direções. Esta abordagem revela-se inadequada no contexto antropométrico, uma vez que as dimensões da mão apresentam correlações imperfeitas entre si e não variam de modo uniforme entre populações, sexos e grupos etários. Em consequência, indivíduos com largura de mão semelhante podem apresentar comprimentos digitais, proporções falângicas ou dimensões do polegar significativamente diferentes. A modelação paramétrica exige, por isso, parâmetros independentes que permitam derivar proporções locais sem pressupor uma homotetia global. Isto significa que as partes da prótese não são redimensionadas segundo uma proporção única nem mantêm invariáveis todas as relações geométricas entre si. (Lim et al., 2018; Nag et al., 2003; Rodríguez-Vega & Rodríguez-Vega, 2024).

Esta limitação torna-se visualmente evidente na Figura 4.2, que compara um modelo uniformemente escalado com outro parametrizado a partir de variáveis independentes. A diferença mostra que a configuração exige o controlo das relações geométricas internas, ultrapassando o simples aumento ou redução do modelo-base.

![](projecto-completo_media/image13.png)

Figura 4.2 — Comparação entre o escalonamento uniforme e a modelação paramétrica de dedo protésico.

Adaptado de Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. [https://doi.org/10.1115/DETC2018-85645](https://doi.org/10.1115/DETC2018-85645)

### Métodos de recolha de dados antropométricos

A recolha de dados pode ser realizada por diferentes métodos, com implicações directas na precisão das medições e na sua tradução para parâmetros de projecto. A escolha do método depende do objectivo da medição: parametrização dimensional básica, reconstrução geométrica fina, desenho do encaixe ou obtenção de relações internas entre superfícies e estruturas ósseas. Em termos práticos, Çıklaçandır et al. (2022) e Herbst et al. (2021) mostram que não há um método universalmente superior; há, sim, uma adequação diferencial entre método, custo, acessibilidade e o tipo de dados necessários (Çıklaçandır et al., 2022; Herbst et al., 2021).

Tabela 4.3 — Métodos de recolha de dados antropométricos e suas características

| Método | Dados obtidos | Vantagens | Limitações | Uso principal |

| --- | --- | --- | --- | --- |

| Digitalização 3D | Geometria superficial | Elevada precisão, rapidez | Equipamento e processamento necessários | Encaixe e forma |

| Imagiologia médica | Estrutura interna e externa | Dados anatómicos detalhados | Alto custo e menor acessibilidade | Modelação biomecânica |

| Fotogrametria | Geometria aproximada | Acessível, potencial remoto | Precisão variável | Aquisição preliminar |

### Bases de dados antropométricas, extracção e normalização

A configuração recorre a uma base local em formato longo, na qual cada linha representa uma estatística associada a uma medida e a um grupo, e não uma pessoa. O conjunto combina fontes populacionais heterogéneas quanto a idade, sexo, país, amostra, protocolo e estatísticas disponíveis. Por esse motivo, os valores funcionam como referências iniciais e não como substitutos da medição individual.

Para a modelação, a base cumpre três funções: identificar medidas recorrentes; apoiar a definição de intervalos de configuração; e fornecer casos populacionais para examinar a propagação dos parâmetros. A origem documental, a população, a unidade e as notas de qualidade permanecem associadas a cada valor, permitindo regressar à fonte quando surgem incompatibilidades.

A extracção, a selecção das fontes, a normalização para milímetros, a cobertura populacional e as limitações documentais são apresentadas integralmente no Anexo A. No corpo do capítulo conservam-se apenas as regras que alteram decisões geométricas: medidas disponíveis, correspondência com os campos do modelo, tratamento de ausência e limites de utilização.

A maior parte dos dados descreve pessoas sem amputação e não representa a forma do membro residual, a deformação dos tecidos ou a interface corpo–dispositivo. Uma referência populacional pode apoiar uma configuração inicial; uma adaptação individual exige medidas directas, eventual digitalização tridimensional e avaliação própria.

Tabela 4.4 — Funções e limites da base antropométrica na configuração

| Função no projecto | Dados utilizados | Limite de interpretação |
| --- | --- | --- |
| Identificar medidas recorrentes | designações, regiões corporais e protocolos das fontes | medidas com o mesmo nome podem usar pontos anatómicos diferentes |
| Definir intervalos iniciais | médias, dispersões e percentis disponíveis | os intervalos populacionais não constituem limites clínicos |
| Construir casos de ensaio | idade, sexo, país, grupo e estatística | o perfil agregado não representa uma pessoa nem assegura correspondência nacional |
| Preencher parâmetros disponíveis | valores positivos ligados ao mapa canónico do modelo | os campos ausentes permanecem por preencher e não devem ser inventados |

### Correspondência entre perfil populacional e parâmetros do modelo

A plataforma converte as linhas dos CSV em perfis agregados armazenados na base local da aplicação. No fecho do estudo existiam 100 perfis: 97 importados em lote, dois por importação CSV e um criado manualmente. A correspondência entre uma descrição e estes perfis é determinística e encontra-se implementada no serviço de correspondência de perfis.

O algoritmo extrai sexo e idade do texto, com apoio opcional de um modelo de linguagem quando esses campos ficam incompletos. Para cada perfil, calcula uma pontuação: +3 por coincidência de sexo e -3 por conflito explícito; +3 por coincidência da categoria etária e -2 por conflito; até +1,5 pela proximidade numérica da idade; +1,5 quando o país do perfil ocorre literalmente na descrição; +1 para grupos identificados como média, mediana ou percentil 50; e +1 quando o nome do grupo indica medições da mão. A idade representativa de um intervalo é o seu ponto médio; num intervalo aberto, como «65+», acrescentam-se cinco anos ao limite. O perfil só é seleccionado quando a pontuação atinge 3. Quando o país indicado está ausente da base, esse critério não acrescenta pontuação.

Depois da selecção, um mapa canónico liga cada parâmetro a um caminho da estrutura antropométrica. Entre as ligações principais encontram-se `palm_breadth_mm` a `palm.width_mm`, `palm_length_mm` a `palm.length_mm`, os comprimentos dos cinco dedos aos respectivos campos `digits.*.total_length_mm`, os comprimentos proximais a `digits.*.proximal_length_mm` e `wrist_circumference_mm` a `wrist.circumference_mm`. Só são aplicados parâmetros numéricos presentes no modelo e com medida positiva no perfil. Cada valor é arredondado a uma casa decimal e limitado pelo mínimo e máximo declarados; os campos ausentes são ignorados e permanecem disponíveis para introdução manual ou sugestão da IA.

Este processo selecciona uma referência inicial e não um equivalente individual. A pontuação é uma regra de correspondência construída para o protótipo; não representa distância antropométrica validada entre populações. Um exemplo é o cenário «*girl, 10 years old, ... Japan*»: como o Japão está ausente, o algoritmo usa sexo, idade, proximidade etária e qualidade do grupo, sem evidência nacional japonesa.

### Estrutura paramétrica e mapeamento de parâmetros

A estrutura do modelo paramétrico organiza os parâmetros segundo uma lógica hierárquica e relacional, distinguindo entre parâmetros primários, derivados, funcionais e construtivos. Esta distinção é metodologicamente importante porque impede que o modelo seja tratado como um conjunto plano de medidas independentes. Em vez disso, estabelece-se uma cadeia de transformação em que algumas variáveis funcionam como entradas principais do utilizador e outras como consequências geométricas, cinemáticas ou produtivas dessas entradas (Moreo, 2016; Romero et al., 2025).

Tabela 4.5 — Estrutura hierárquica dos parâmetros no modelo paramétrico

| Tipo de parâmetro | Exemplos | Função no modelo | Relação com outras variáveis |

| --- | --- | --- | --- |

| Derivados | Proporções das falanges | Construção geométrica | Dependentes |

| Funcionais | Amplitude de movimento, posição articular | Desempenho | Ligação cinemática |

| Construtivos | Espessuras, folgas, tolerâncias | Fabrico | Ajuste técnico |

A tradução destes parâmetros em geometria é realizada por meio de relações explícitas entre medições e componentes do modelo.

### OpenSCAD: enquadramento e justificação da escolha

Antes de avançar para a formalização do modelo, importa clarificar o que é o OpenSCAD e por que motivo foi escolhido como ambiente de modelação paramétrica neste projecto. O OpenSCAD é um ambiente livre e *open source* de CAD tridimensional baseado em ficheiros de *script*, orientado para a criação de geometria sólida e não para a modelação artística de superfícies. O modelo é descrito num ficheiro .scad, escrito numa linguagem própria, e esse ficheiro é interpretado pelo programa para gerar o sólido correspondente. Do ponto de vista geométrico, o OpenSCAD assenta numa lógica de *Constructive Solid Geometry* (CSG), na qual primitivas como cubos, cilindros, esferas e extrusões são combinadas por operações booleanas, transformações e relações hierárquicas entre módulos (OpenSCAD Project, n.d.-a; OpenSCAD Project, n.d.-b; Ghali, 2008).

Esta natureza programável distingue o OpenSCAD dos ambientes CAD convencionais baseados sobretudo em manipulação gráfica directa. Em muitos sistemas CAD, o utilizador constrói uma sequência de operações num histórico visual e parametriza algumas características desse histórico; no OpenSCAD, pelo contrário, a própria descrição textual é o modelo paramétrico. As variáveis, funções e módulos não são uma camada posterior aplicada à geometria, mas a estrutura que a gera. Esta diferença é relevante para a investigação, porque torna as relações entre parâmetros, componentes e restrições mais explícitas, reexecutáveis e documentáveis, embora implique uma curva de aprendizagem maior e dificuldades conhecidas em tarefas de navegação código-vista, validação e criação de formas orgânicas complexas (Trautmann, 2021; Gonzalez Avila et al., 2024).

A escolha do OpenSCAD resulta, em primeiro lugar, da sua adequação a processos documentados e consistentes de *design* paramétrico. Por ser texto simples, o ficheiro-fonte pode ser mantido sob controlo de versões, comparado, analisado e reutilizado, o que favorece o registo das decisões de modelação e a regeneração das variantes. Esta característica é valorizada em *hardware* científico e *open source*, porque a documentação do processo tem importância equivalente ao ficheiro final exportado. Além disso, o OpenSCAD pode ser executado por linha de comando, receber valores por parâmetros e exportar automaticamente geometrias para formatos de fabrico digital, como STL ou 3MF, tornando-o compatível com fluxos de geração em lote e configuradores digitais (Machado et al., 2019; OpenSCAD Community, n.d.).

Em segundo lugar, o OpenSCAD adapta-se bem à arquitectura *web* proposta nesta dissertação. A separação entre definição geométrica e interface permite que o ficheiro `.scad` permaneça como núcleo técnico do modelo, enquanto a plataforma apresenta ao utilizador os parâmetros relevantes. Esta lógica já foi explorada em configuradores *web* baseados em OpenSCAD, nos quais utilizadores sem domínio da linguagem podem gerar variantes imprimíveis a partir de modelos parametrizados por designers. A existência de implementações em *WebAssembly*, como o OpenSCAD *Web*, reforça esta escolha, porque demonstra que o motor de geração pode ser executado no navegador, associado a editores, visualizadores 3D e interfaces de personalização sem exigir a instalação local de *software* CAD completo (Nilsiam & Pearce, 2017; Brooks, 2026).

Em terceiro lugar, o OpenSCAD é particularmente compatível com um fluxo de *design* apoiado por inteligência artificial. Como a geometria é expressa em código curto, estruturado e relativamente legível, uma IA pode sugerir valores, explicar relações entre variáveis ou propor alterações ao *script* sem substituir a lógica paramétrica por uma geometria opaca. Trabalhos recentes sobre geração de modelos 3D a partir de linguagem natural e automação de desenho paramétrico mostram que modelos de linguagem podem atuar sobre *scripts* CAD, embora continuem a exigir revisão humana, verificação dimensional e validação técnica antes de qualquer aplicação produtiva ou clínica (ELhadad et al., 2026; Schöfer & Seibel, 2025; Gonzalez Avila et al., 2024).

No contexto específico das próteses e das tecnologias de apoio, esta escolha é ainda reforçada por estudos que usam modelação paramétrica para adaptar dedos protésicos, mãos mecânicas accionadas pelo corpo e outros dispositivos de apoio às medidas ou necessidades do utilizador.
Estes trabalhos não eliminam a necessidade de ensaios funcionais, avaliação ergonómica ou validação clínica, mas demonstram que a personalização geométrica pode ser estruturada por parâmetros explícitos e por modelos reexecutáveis. Para este projecto, o OpenSCAD é, portanto, adequado não porque resolva sozinho o problema da prótese personalizada, mas porque oferece uma base transparente para ligar medidas antropométricas, regras de modelação, interface *web*, sugestões de IA, exportação para fabrico aditivo e revisão humana (Lim et al., 2018; Bustamante et al., 2018; Romani & Levi, 2020).

Tabela 4.6 — Mapeamento entre parâmetros antropométricos e elementos do modelo

| Parâmetro antropométrico | Efeito geométrico previsto |

| --- | --- |

| Largura da palma | Volume da palma e espaçamento entre dedos |

| Comprimento dos dedos | Geometria das falanges |

| Circunferência do antebraço | Geometria do encaixe |

| Largura do punho | Interface palma-punho |

| Proporções falângicas | Relações cinemáticas dos mecanismos digitais |

Este mapeamento constitui a base da modelação paramétrica, permitindo converter dados antropométricos em configurações geométricas e funcionais. Em termos práticos, a passagem da medição para a geometria não deve ser entendida como uma transposição linear, mas como a definição de relações controladas: certos parâmetros regulam a escala geral, outros definem proporções locais e outros ainda atuam como restrições de consistência geométrica, desempenho funcional ou compatibilidade com o processo de fabrico.

Antes da tradução do modelo para o ambiente de modelação paramétrica, torna-se necessário estabilizar três níveis: os dados de entrada, as relações entre parâmetros e os limites técnicos que condicionam a sua transformação em forma.

No contexto desta investigação, o papel da secção 4.2 é, portanto, delimitado com clareza: identificar quais são os parâmetros antropométricos relevantes, como são recolhidos ou inferidos, e de que modo se organizam antes de entrarem na estrutura computacional do modelo. A secção seguinte retoma precisamente esta base para mostrar como esse sistema de entradas, dependências e restrições é formalizado em OpenSCAD como um modelo executável, modular e regenerável.

### 4.3 Modelação paramétrica em OpenSCAD

A modelação paramétrica em OpenSCAD corresponde, nesta investigação, ao momento em que a estrutura definida na secção anterior deixa de ser um quadro conceptual e passa a constituir um modelo operacional, capaz de traduzir parâmetros, relações e restrições em geometrias configuráveis. Os parâmetros antropométricos seleccionados, as relações hierárquicas entre variáveis e os limites de configuração são inscritos em código, de modo a gerar a mesma geometria para um mesmo conjunto de valores e versão do modelo. A transição para OpenSCAD constitui, assim, a continuação lógica do mesmo problema: transformar dados corporais e regras de projecto num modelo configurável que preserve coerência formal e produtiva.

A modelação paramétrica em OpenSCAD é aqui entendida como uma abordagem em que a geometria resulta de regras explícitas, parâmetros definidos em código e relações de dependência entre componentes, em vez da edição manual isolada de formas. No desenvolvimento de próteses personalizadas de membro superior, esta lógica permite compreender a prótese como um conjunto configurável de variantes que pode ser regenerado a partir de novos dados antropométricos, requisitos funcionais e limites de fabrico. Os estudos analisados sobre modelação paramétrica aplicada a próteses e sobre modelação CAD programável associam estas abordagens a melhor documentação das decisões, consistência entre variantes e automatização em fluxos de personalização digital (Machado et al., 2019; Moreo, 2016; Romero et al., 2025).

Ao contrário de ambientes centrados na manipulação gráfica directa, o OpenSCAD opera como uma especificação computacional do objecto. Esta característica permite compreender o modelo como resultado geométrico e estrutura explícita de projecto, onde ficam registadas as relações entre entradas antropométricas, módulos geométricos, restrições construtivas e decisões formais. A modelação baseada em código articula-se, assim, com *Research Through Design*, pois o próprio modelo pode ser lido, analisado, testado e documentado como uma estrutura de conhecimento técnico e de projecto.

A Figura 4.3 reforça esta passagem entre definição paramétrica, modelo virtual e protótipo físico. O seu valor para esta investigação não reside em replicar a solução apresentada, mas em tornar visível a cadeia que liga a decomposição dimensional do dedo, a modelação computacional e a verificação material, isto é, o mesmo tipo de continuidade que o modelo em OpenSCAD procura preservar (Nini et al., 2024).

![](projecto-completo_media/image14.png)

Figura 4.3 — Relação entre modelo paramétrico digital, prototipagem e verificação de um dedo protésico.

Reproduzido de Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. [https://doi.org/10.1109/BioRob60516.2024.10719909](https://doi.org/10.1109/BioRob60516.2024.10719909)

### 4.3.1 Estrutura técnica, parâmetros e restrições

Num modelo paramétrico baseado em OpenSCAD, a organização interna pode ser compreendida como uma arquitectura em camadas.

Numa primeira camada situam-se os dados de entrada, provenientes de medições lineares, de dados consolidados de referência ou de digitalização tridimensional. Numa segunda camada, esses dados são transformados em parâmetros geométricos derivados, responsáveis por estabelecer proporções, espessuras, posições articulares e relações entre subcomponentes. Segue-se uma camada funcional, na qual se definem exigências de mobilidade, montagem ou integração mecânica, e uma camada de restrições produtivas, na qual se enquadram espessuras mínimas, folgas, tolerâncias e limites de fabrico. Esta organização permite controlar a personalização sem comprometer a coerência interna do sistema (Moreo, 2016; Nini et al., 2024; Saldarriaga et al., 2024).

Tabela 4.7 — Estrutura técnica em camadas de um modelo paramétrico em OpenSCAD para próteses personalizadas

| Camada | Dados tratados | Função | Exemplos |

| --- | --- | --- | --- |

| Derivação geométrica | Parâmetros calculados a partir das entradas | Traduzir medidas em relações formais | Comprimentos segmentares, espessuras, offsets |

| Comportamento funcional | Parâmetros ligados ao uso e ao mecanismo | Regular movimento, montagem e desempenho | Amplitude articular, espaço para tendões, eixos |

| Restrições produtivas | Limites de fabrico e consistência | Garantir fabrico e robustez | Espessura mínima, folgas, raios mínimos |

Quando transposta para o ambiente de modelação em OpenSCAD, esta arquitectura tende a materializar-se em módulos relativamente autónomos. Em vez de concentrar toda a definição geométrica num único bloco de código, o modelo pode ser distribuído em módulos correspondentes à palma, aos dedos, às articulações, às interfaces de fixação ou ao encaixe. A modularidade apresenta aqui duas vantagens directas: reduz a opacidade do sistema e facilita a regeneração controlada de variantes. Num contexto protésico, isto permite que alterações nos parâmetros de entrada não se propaguem de forma arbitrária a todo o modelo, mas segundo relações previamente explicitadas e localizáveis. (Machado et al., 2019; Romero et al., 2025).

Outro aspecto central é a integração de restrições directamente na lógica paramétrica. Em vez de tratar a compatibilidade com o fabrico aditivo como uma etapa exclusivamente posterior, o modelo pode incorporar, desde o início, limites mínimos de espessura, folgas entre elementos móveis, margens de tolerância e verificações condicionais para evitar combinações inválidas.

Este princípio é particularmente relevante em próteses produzidas por fabrico aditivo, nas quais pequenas alterações dimensionais podem comprometer a montagem, a resistência ou a viabilidade de impressão. Estudos sobre modelação paramétrica de dedos e encaixes protésicos personalizados mostram que a estabilidade do sistema depende da articulação entre parâmetros antropométricos e restrições construtivas, em lugar de decorrer da liberdade de alteração geométrica (Nini et al., 2024; Saldarriaga et al., 2024).

A modelação em OpenSCAD pode ser articulada a fluxos de dados mais complexos, incluindo a digitalização tridimensional e a automatização parcial do desenho. Trabalhos como os de Herbst et al. (2021) e Saldarriaga et al. (2024) mostram que a personalização tende a aproximar a medição, a parametrização e o fabrico, reduzindo o intervalo entre a captura anatómica e a geração de modelos prontos para produção. No caso desta investigação, essa articulação usa a lógica explícita do código como núcleo organizador para integrar dados, restrições e interfaces de configuração de modo consistente e documentado.

### 4.3.2 Análise crítica da abordagem

A adopção do OpenSCAD neste projecto apresenta vantagens metodológicas relevantes, sobretudo pela forma como torna explícita a construção do modelo paramétrico. Ao ser definido por código, o modelo permite identificar relações entre variáveis, dependências e restrições com maior facilidade do que em muitos fluxos CAD baseados em operações gráficas. Esta condição favorece a transparência do processo, a análise crítica e a possibilidade de reconstituir as decisões de modelação, qualidades particularmente importantes num trabalho académico em que o modelo paramétrico constitui um instrumento de produção formal e um objecto de análise (Machado et al., 2019).

Uma segunda vantagem reside na afinidade entre a modelação baseada em código, a automatização e a partilha aberta. Os estudos analisados indicam que o OpenSCAD é particularmente adequado a fluxos de personalização digital em que o modelo é configurado por parâmetros, evitando a edição manual da geometria a cada alteração. Esta característica permite associar o ficheiro-fonte a interfaces *web*, gerar múltiplas variantes segundo regras explícitas e disponibilizar modelos reutilizáveis em comunidades distribuídas. A possibilidade de ajustar o modelo sem editar directamente o código em cada iteração reforça a sua pertinência em contextos de personalização e fabrico digital (Nilsiam & Pearce, 2017). Para um projecto que aproxima parametrização, interface e apoio computacional, esta característica é especialmente relevante.

Contudo, esta abordagem apresenta limitações importantes. Uma delas prende-se com a exigência técnica e conceptual associada à programação. Mesmo quando o modelo é modular e bem estruturado, a edição directa em OpenSCAD requer capacidade de interpretar transformações geométricas, dependências paramétricas e operações booleanas. Por essa razão, a utilidade do OpenSCAD aumenta quando o sistema é mediado por camadas intermédias de interface ou por procedimentos que exponham apenas os parâmetros necessários à configuração. A segunda limitação é de natureza geométrica. A modelação por combinação de sólidos, habitualmente designada por *Constructive Solid Geometry* (CSG), favorece a criação de peças mecânicas, modulares e relativamente discretas, mas tende a ser menos adequada à definição de superfícies orgânicas complexas ou de interfaces anatómicas altamente irregulares, sobretudo quando comparada com ferramentas orientadas para superfícies livres.

Há ainda uma limitação relacionada com a interoperabilidade. Os estudos comparativos sobre OpenSCAD sublinham que este ambiente de modelação está fortemente orientado para formatos baseados em malhas, nos quais a geometria é representada por uma aproximação poligonal da superfície, como acontece nos ficheiros STL. Esta orientação favorece fluxos de fabrico digital e impressão 3D, mas pode dificultar a integração com certos circuitos CAD industriais ou com ambientes que exijam a preservação completa da informação paramétrica em formatos normalizados (Machado et al., 2019). Isto não invalida a adequação do OpenSCAD ao presente projecto, mas significa que a sua adopção deve ser vista como uma escolha situada: muito eficaz para estruturar um núcleo paramétrico explícito, menos adequada quando o objectivo depende de plena continuidade com certos fluxos proprietários de engenharia.

Por fim, a avaliação da abordagem exige articular a geração da geometria com as etapas seguintes. Mesmo quando a lógica paramétrica é clara e as restrições estão integradas, a confirmação técnica do modelo depende da inspecção durante a preparação para impressão 3D, do controlo dimensional, de eventual simulação estrutural e da observação da peça física.

Em consequência, o valor do OpenSCAD nesta investigação não reside numa promessa de automatização total, mas na capacidade de fornecer uma infraestrutura técnica clara para ligar a personalização antropométrica, a modularidade, as restrições de fabrico e a documentação do processo. É precisamente essa combinação entre explicitação, reexecução e possibilidade de revisão crítica que justifica a sua escolha como base para a modelação paramétrica aqui desenvolvida.

### 4.3.3 Relações implementadas nos modelos avaliados

As relações gerais das Tabelas 4.5 e 4.6 foram concretizadas de forma diferente em cada família. O estado usado nos ensaios principais corresponde ao dicionário do Suplemento 3 — Parametrização e percurso numérico. Uma revisão posterior acrescentou a braçadeira comum do Flexy Beast e relações mais completas do Cyborg Beast. O estado final examinado uniformizou a organização dos grupos e os nomes dos controlos de lateralidade e disposição, sem alterar as relações geométricas avaliadas. Estes desenvolvimentos posteriores não são retroactivamente apresentados como parte dos ensaios concluídos anteriormente. As fórmulas descrevem a implementação; não representam relações anatómicas universais.

Tabela 4.8 — Síntese das relações implementadas e respectivas limitações

| Modelo | Entradas activas principais | Transformação implementada | Limitação que deve acompanhar a leitura |
| --- | --- | --- | --- |
| Flexy Beast | largura da palma; comprimentos dos cinco dedos; circunferência do punho | `xScaleFactor = (palm_breadth_mm + 5) / 55`; o médio define o multiplicador digital e os restantes dedos definem proporções; a braçadeira deriva de circunferência/π mais folga | a largura introduzida alimenta uma fórmula herdada e não coincide directamente com a extensão transversal da malha |
| Cyborg Beast | largura da palma; comprimentos totais e proximais; circunferência do punho | escala global pela fórmula Cyborg Beast; curvas calibradas para os segmentos; braçadeira dimensionada independentemente da mão | as curvas são calibrações da geometria e possuem limites internos; o modelo não integrou a comparação principal |
| Paraglider Hand | largura da palma; comprimentos dos dedos; opções de componentes | `overall_scale = palm_breadth_mm / 66,4`; correcção `overall_scale / 1,25` na palma Reborn; escalas próprias para indicador, médio, anelar e mindinho | a palma mantém escala uniforme para preservar os furos; comprimento e espessura da palma são contextuais; o polegar ainda usa a escala do médio |
| UnLimbited Phoenix Hand | largura da palma; comprimentos totais e proximais dos dedos | `HandPerc` limitado a 100%–160%; alongamento localizado das zonas sem furos | os perfis inferiores a 82 mm atingem o limite mínimo; os comprimentos digitais são novamente afectados pela escala global |

O escalonamento uniforme não foi eliminado em todos os modelos. Foi mantido onde a arquitectura herdada exigia preservar furos circulares, espaçamentos e componentes montados como conjunto. No Paraglider, esta opção protege a palma e os pinos enquanto parte dos dedos recebe escalas próprias. No Phoenix, a montagem completa conserva uma escala uniforme e os dedos são alongados apenas em faixas sem furos; como o alongamento antecede a escala global, o comprimento final depende das duas operações.

A crítica ao escalonamento proporcional aplica-se, portanto, ao seu uso como substituto de todas as diferenças antropométricas. Uma transformação uniforme local pode constituir uma restrição mecânica legítima, desde que o texto identifique o que preserva, o que deixa de adaptar e como afecta as restantes dimensões.

Os parâmetros de lateralidade constituem uma classe separada. No estado final examinado, os quatro modelos registados usam o campo booleano `mirrored`; a designação anterior `LeftRight` do Phoenix foi eliminada. Estes campos possuem o papel `laterality`, ficam fora do pedido de sugestões e são descartados caso surjam na resposta da IA. A regra geométrica permanece determinística e independente do texto gerado pelo modelo de linguagem.
### 4.3.4 Dicionário operacional de parâmetros

Para tornar auditável a passagem entre dados, configuração e geometria, a Tabela 4.9 consolida os parâmetros numéricos com efeito antropométrico, geométrico ou mecânico nos três modelos comparados. O dicionário corresponde ao estado da plataforma usado nos ensaios principais. A unidade é o milímetro, excepto quando a tabela indica percentagem ou razão adimensional. Os valores iniciais não são médias universais: constituem a configuração de referência do modelo. Os intervalos são limites de implementação e não limites clínicos.

O dicionário integral preservado no Suplemento 3 — Parametrização e percurso numérico contém as 42 declarações numéricas sem agrupamento, incluindo incremento, grupo funcional, designação e descrição em português, papel determinístico e exclusão da IA. A tabela no corpo agrupa apenas variáveis com a mesma origem, intervalo e transformação, para manter a leitura possível em página.

Tabela 4.9 — Dicionário operacional dos parâmetros numéricos dos modelos avaliados

| Modelo e parâmetro | Significado e origem | Inicial | Intervalo; incremento | Regra ou efeito geométrico |
| --- | --- | ---: | --- | --- |
| Flexy Beast — `palm_breadth_mm` | Largura metacarpal; `palm.width_mm` | 83 | 55–110; 1 | Escala uniforme da mão: `xScaleFactor = (valor + 5) / 55` |
| Flexy Beast — `middle_finger_length_mm` | Dobra MCP à ponta do dedo médio; `digits.middle.total_length_mm` | 72 | 40–120; 1 | Comprimento mestre: `fingerLength = valor / (37 × xScaleFactor)` |
| Flexy Beast — `index_finger_length_mm`; `ring_finger_length_mm` | Comprimento total do indicador e anelar | 68; 68 | 40–120; 1 | Proporção de cada dedo relativamente ao médio |
| Flexy Beast — `pinky_finger_length_mm`; `thumb_length_mm` | Comprimento total do mindinho e polegar | 55; 65 | 30–100; 1 e 35–100; 1 | Proporção local relativamente ao dedo médio |
| Flexy Beast — `joint_dia`; `joint_thick` | Diâmetro do furo e espessura da ranhura da junta flexível | 7; 4 | 4–10; 0,5 e 1–6; 0,5 | Dimensionam furos, ranhuras e conectores flexíveis; não são medidas corporais |
| Flexy Beast — `gauntlet_width_mm`; `gauntlet_length_mm`; `gauntlet_wall_mm` | Largura, comprimento e espessura da braçadeira do antebraço | 60; 108; 3 | 40–90; 1, 70–150; 1 e 2–5; 0,5 | Escala e espessura da braçadeira; a largura pode ser derivada da circunferência do punho com folga |
| Flexy Beast — `gauntlet_pos_adjust`; `strap_splay_adjust` | Ajuste longitudinal da braçadeira e afastamento das abas | 0; 0 | −25–25; 1 e −8–8; 0,5 | Correcções locais de posição e compatibilidade; introdução manual |
| Flexy Beast — `wrist_pin_dia`; `wrist_pin_clearance` | Diâmetro do pino do punho e folga de rotação | 7; 0,35 | 3–8; 0,5 e 0,10–0,80; 0,05 | Dimensionam a interface articulada entre palma e braçadeira |
| Paraglider — `palm_breadth_mm` | Largura metacarpal; `palm.width_mm` | 83 | 55–110; 1 | `overall_scale = valor / 66,4`; palma escalada uniformemente |
| Paraglider — `palm_length_mm`; `palm_thickness_mm` | Comprimento e espessura da palma | 95; 32 | 60–140; 1 e 18–50; 1 | Informação de perfil e contexto para a IA; não deforma independentemente a palma |
| Paraglider — `index_finger_length_mm`; `middle_finger_length_mm`; `ring_finger_length_mm` | Comprimentos totais do indicador, médio e anelar | 68; 72; 68 | 40–120; 1 | Escalas próprias dos dedos; o médio também define a escala-base digital |
| Paraglider — `pinky_finger_length_mm`; `thumb_length_mm` | Comprimentos totais do mindinho e polegar | 55; 65 | 30–100; 1 e 35–100; 1 | O mindinho recebe escala própria; o polegar acompanha a escala-base digital |
| Paraglider — `string_channel_scale`; `elastic_channel_scale` | Escala relativa dos canais de tracção e elástico | 0,9; 0,9 | 0,50–1,00; 0,05 e 0,50–1,50; 0,05 | Razões adimensionais aplicadas aos canais mecânicos |
| Paraglider — `ARM_HandLen`; `ARM_ForearmLen`; `ARM_BicepCircum`; `ARM_CuffLength` | Comprimento da mão e antebraço, circunferência do braço e comprimento da braçadeira | 135; 140; 160; 65 | 135–230; 1, 120–315; 1, 110–350; 1 e 65–90; 1 | Dimensionam a extensão opcional do braço; não participaram na comparação da mão isolada |
| Paraglider — `ARM_PinHoleDia` | Diâmetro dos furos das articulações do braço | 3 | 3–6; 1 | Interface mecânica da extensão opcional do braço |
| UnLimbited Phoenix — `palm_breadth_mm` | Largura metacarpal; `palm.width_mm` | 82 | 82–131; 1 | `HandPerc = valor / 82 × 100`, limitado a 100%–160% |
| UnLimbited Phoenix — `HandPerc_override` | Substituição manual da percentagem de escala | 0 | 0–160; 1 | Zero deriva a escala da palma; valores positivos continuam sujeitos ao limite mínimo de 100% |
| UnLimbited Phoenix — `index_finger_length_mm`; `middle_finger_length_mm`; `ring_finger_length_mm`; `pinky_finger_length_mm` | Comprimentos totais dos quatro dedos | 72 em cada | 55–115; 1 | Alongamento dos eixos dos segmentos, preservando circularidade dos furos |
| UnLimbited Phoenix — `index_base_length_mm`; `middle_base_length_mm`; `ring_base_length_mm`; `pinky_base_length_mm` | Comprimentos dos segmentos proximais | 31 em cada | 18–55; 1 | Divide o comprimento total entre segmento proximal e ponta |
| UnLimbited Phoenix — `thumb_length_mm`; `thumb_base_length_mm` | Comprimento total e proximal do polegar | 72; 31 | 45–80; 1 e 18–50; 1 | Alongamento do polegar e divisão proximal–distal |

O dicionário separa três categorias. Os parâmetros antropométricos podem receber medidas directas ou referências populacionais; os parâmetros derivados transformam essas entradas segundo fórmulas do modelo; e os parâmetros mecânicos representam escolhas de projecto, folgas ou interfaces que não devem ser inferidas como características anatómicas. Parâmetros booleanos de visibilidade, cores, disposição para impressão e lateralidade permanecem no ficheiro de configuração completo, mas não integram a Tabela 4.9 por não serem grandezas numéricas.

O Anexo C complementa o dicionário usado nos ensaios principais com as adaptações posteriores, as relações internas do Cyborg Beast, os valores de folga e espessura confirmáveis, as excepções da escala uniforme e os campos que ainda não produzem uma transformação geométrica própria. O anexo distingue valores directos, derivados, fixos e contextuais e assinala expressamente as propriedades que não podem ser confirmadas pelos ficheiros examinados.

### 4.3.5 Exemplo numérico completo: perfil infantil no Flexy Beast

A Tabela 4.10 apresenta um percurso integral preservado na série de ensaios de 8 de Julho de 2026. Para isolar a transformação geométrica, a entrada efectiva é o vector de medidas aplicado ao modelo, e não a nacionalidade ou a escolha da referência populacional. O perfil de ensaio descrevia um rapaz de oito anos, 26 kg, 128 cm de altura, do Brasil e com mãos pequenas. A base não contém uma população brasileira; embora o registo indique `grounded: true`, este caso não permite inferir adequação à população indicada. A sua função é demonstrar como valores aceites pelo esquema chegam a malhas mensuráveis.

Tabela 4.10 — Exemplo da transformação das medidas antropométricas em geometria digital no Flexy Beast

| Etapa | Operação ou evidência | Valor obtido |
| --- | --- | --- |
| 1. Vector aplicado | Palma; indicador; médio; anelar; mindinho; polegar | 64; 57; 60; 57; 46; 50 mm |
| 2. Verificação pelo esquema | Comparação com os intervalos da Tabela 4.9 | Todos os seis valores ficaram dentro dos intervalos; nenhuma limitação foi aplicada |
| 3. Escala global | `xScaleFactor = (64 + 5) / 55` | 1,254545 |
| 4. Multiplicador mestre dos dedos | `fingerLength = 60 / (37 × 1,254545)` | 1,292597 |
| 5. Proporções digitais | Indicador/60; médio/60; anelar/60; mindinho/60; polegar/60 | 0,950000; 1,000000; 0,950000; 0,766667; 0,833333 |
| 6. Parâmetros mecânicos aplicados | `joint_dia`; `joint_thick`; braçadeira largura × comprimento × parede; `wrist_pin_dia` | 5 mm; 2 mm; 47 × 80 × 2 mm; 5 mm; todos dentro dos limites |
| 7. Malha da palma | Caixa envolvente XYZ; volume; faces; estanquidade | 97,385 × 80,103 × 37,123 mm; 51,381 cm³; 11.186 faces; fechada |
| 8. Segmento proximal do dedo médio | Caixa envolvente XYZ; volume; faces; estanquidade | 37,451 × 14,913 × 14,775 mm; 5,225 cm³; 888 faces; fechada |
| 9. Segmento distal do dedo médio | Caixa envolvente XYZ; faces; estanquidade | 52,183 × 14,913 × 22,697 mm; 1.198 faces; aberta |

A ponta do dedo médio é uma casca aberta porque a configuração `finger_pads=true` reserva a cavidade destinada à almofada de aderência. Neste caso, a ausência de estanquidade não deve ser ocultada nem classificada automaticamente como falha de exportação; deve ser interpretada face à intenção construtiva da peça. A palma e o segmento proximal são sólidos fechados segundo a inspecção computacional realizada.

O percurso evidencia ainda que `palm_breadth_mm = 64` não pretende produzir uma caixa envolvente com exactamente 64 mm. O valor alimenta a fórmula herdada do Cyborg Beast e gera uma escala global aplicada a uma geometria-base; a caixa envolvente transversal medida foi 80,103 mm. Esta diferença é uma propriedade explícita da transformação implementada e mostra por que razão a correspondência entre nome antropométrico e dimensão final deve ser calibrada antes de qualquer afirmação de ajuste anatómico.

Os registos de parâmetros, as malhas, o percurso de transformação e o dicionário completo integram o Suplemento 3 — Parametrização e percurso numérico. O percurso é reproduzível ao nível do artefacto e do cálculo; permanece uma verificação técnica com perfil de ensaio, sem avaliação de conforto, função, segurança ou validade clínica.

Os exemplos complementares do Anexo C mostram duas dependências que este percurso não cobre: o parâmetro de comprimento do polegar do Paraglider ainda não controla uma escala própria e, no Phoenix, a escala global volta a multiplicar os comprimentos definidos localmente.

### 4.4 Iterações e decisões de projecto

A evolução dos modelos foi documentada com base em episódios em que uma configuração, uma malha ou uma montagem tornou visível uma limitação e conduziu a uma alteração específica. A Tabela 4.11 resume os episódios com maior influência na estrutura paramétrica. As alterações posteriores ao fecho da comparação principal são apresentadas como desenvolvimento subsequente e não como resultados retroactivos dos ensaios anteriores.

Tabela 4.11 — Cronologia das principais iterações paramétricas

| Data | Problema observado | Decisão introduzida | Aprendizagem de projecto |
| --- | --- | --- | --- |
| 15–16 Jun. 2026 | ficheiros Paraglider dispersos e nomes incompatíveis com a plataforma | consolidação da família num modelo com componentes e duas palmas | integrar um modelo aberto exige declarar dependências, variantes e campos comuns antes de expor parâmetros |
| 28 Jun. 2026 | a palma Reborn permanecia no tamanho médio apesar de variar `palm_breadth_mm` | compensação da escala 1,25 preservada no módulo carregado por `use` | a resposta de um controlo não pode ser inferida pelo nome; deve ser confirmada na malha gerada |
| 29 Jun. 2026 | `HandPerc_override` permitia ao Phoenix contornar o limite mínimo de 100% | aplicação do mesmo intervalo de 100%–160% aos dois percursos | limites equivalentes devem actuar em todas as entradas que conduzem à mesma transformação |
| 29 Jun. 2026 | a IA alterava a lateralidade apesar de esta ser uma decisão binária do projecto | lateralidade transferida para a interface determinística e excluída das sugestões | decisões inequívocas e críticas não devem permanecer num processo probabilístico |
| 9–10 Jul. 2026 | integração do Cyborg Beast sem controlo independente dos segmentos e com desalinhamentos | calibração do alcance, divisão proximal–distal e reposicionamento sobre os eixos MCP/PIP | a adaptação paramétrica exige preservar interfaces articulares enquanto se altera o alcance dos segmentos |
| 10 Jul. 2026 | braçadeira desligada da circunferência do punho e polegar sem correspondência estável | braçadeira dimensionada por circunferência/π, assentamento automático no pino e calibração do polegar | mão, punho e antebraço não devem depender de uma única escala global |
| 10–11 Jul. 2026 | dedos Phoenix constituídos por malhas fixas | divisão das colunas e alongamento apenas das faixas sem furos | modelos de malha podem receber variação local se as zonas funcionais forem isoladas |
| 14 Jul. 2026 | braçadeira Flexy parametrizada por dimensões próprias, sem ligação directa ao mapa do punho | adopção da braçadeira comum do Cyborg e de `wrist_circumference_mm` | uma gramática comum deve ligar a mesma medida corporal a funções equivalentes entre modelos, sem apagar as diferenças geométricas |
| 14 Jul. 2026 | grupos e nomes de controlos equivalentes variavam entre modelos | adopção de uma ordem comum; `LeftRight` passou a `mirrored` no Phoenix e `show_assembled` passou a `print_layout` no Paraglider | a coerência da interface beneficia de nomes comuns quando a decisão é equivalente, sem obrigar a uniformizar diferenças geométricas legítimas |

Estes episódios produziram quatro conclusões circunscritas. Primeiro, a integração de um modelo aberto exige examinar o âmbito das variáveis dentro de cada ficheiro, e não apenas os controlos apresentados. Segundo, preservar uma interface mecânica pode justificar escala uniforme local ou alongamento selectivo. Terceiro, um intervalo declarado na interface não substitui verificações na própria transformação geométrica. Quarto, a equivalência nominal entre uma medida e um parâmetro deve ser confirmada na malha, porque fórmulas herdadas e escalas sucessivas podem alterar a dimensão final.

A iteração funcionou, assim, como instrumento de investigação através do *design*: cada falha alterou a compreensão do objecto configurável e conduziu a uma regra mais explícita. O resultado não é uma metodologia universal de personalização protésica, mas um conjunto documentado de decisões para integrar modelos heterogéneos, preservar as suas interfaces e tornar visíveis os respectivos limites.
## Capítulo 5 — Plataforma *Web* e Integração Digital

### 5.1 Enquadramento conceptual e perfis de utilizador

A plataforma *web* desenvolvida no âmbito deste projecto constitui a camada de mediação entre o modelo paramétrico, os dados de entrada e a configuração digital da mão protésica. É um protótipo funcional de investigação e não um produto preparado para utilização clínica. A versão pública pode ser consultada em [https://handfab.pedrocandeias.net/](https://handfab.pedrocandeias.net/); a sua disponibilidade permite observar o artefacto, mas não demonstra usabilidade, acessibilidade global, segurança clínica ou aptidão para utilização autónoma.

O estado final examinado corresponde a 14 de Julho de 2026. Os ensaios principais e a série complementar de interface incidiram em estados anteriores da plataforma. Esta separação temporal é mantida porque a plataforma continuou a evoluir depois dos ensaios, nomeadamente na organização e nomenclatura dos controlos, sem que essas alterações posteriores possam ser apresentadas como parte dos resultados anteriores.

Do ponto de vista do *Design* e Desenvolvimento de Produto, a plataforma não constitui um fim autónomo: organiza a passagem entre intenção, dados, parâmetros, forma visualizada e ficheiro destinado ao fabrico. A interface expõe uma parte controlada do espaço de variação e evita que a configuração dependa da edição directa do código OpenSCAD. Esta leitura é coerente com os estudos sobre personalização digital e personalização em massa, que descrevem os configuradores como sistemas capazes de disponibilizar variação sem comprometer as relações do modelo-base (Ozdemir, Verlinden, & Cascini, 2022; van Stralen, 2018).

Do ponto de vista funcional, a plataforma foi concebida para suportar um processo progressivo de configuração, no qual a definição geométrica resulta da articulação entre a recolha de dados, a selecção do modelo, o ajustamento de parâmetros, a visualização do resultado e a eventual exportação para prototipagem. Esta organização aproxima etapas anteriormente dispersas num único percurso de projecto; não permite concluir que pessoas sem formação técnica o executam com menor esforço.

Em vez de exigir contacto directo com a estrutura interna do ficheiro OpenSCAD, o sistema disponibiliza controlos paramétricos, pré-visualização tridimensional e gestão de configurações. Neste capítulo, esta característica é descrita como uma decisão de interface; a sua facilidade de aprendizagem e a redução efectiva da dependência técnica permanecem por avaliar com participantes.

Tal opção aproxima-se de abordagens recentes em plataformas de personalização de próteses, nas quais a interface funciona como meio de tornar observável, configurável e progressivamente verificável um processo que, de outro modo, permaneceria dependente de *software* especializado ou de mediação exclusivamente técnica (Peixoto et al., 2025).

![](projecto-completo_media/image15.png)

Figura 5.1 — Fluxo geral de produção personalizada de próteses a partir de plataforma *web* – Hand Fab

Fonte: produção própria.

Neste sentido, a plataforma constitui uma infra-estrutura de mediação entre componentes técnicos, utilizadores e intervenientes especializados. A configuração é enquadrada como um processo distribuído, no qual diferentes intervenientes participam com graus distintos de responsabilidade, conhecimento e controlo.

Num contexto de próteses personalizadas, o resultado pode depender da articulação entre o utilizador final, o designer, o técnico ou o clínico, bem como de condicionantes produtivas e de critérios de validação. A plataforma procura, assim, oferecer uma infraestrutura digital que acomode essa pluralidade de agentes sem comprometer a consistência técnica da configuração paramétrica nem deslocar indevidamente a responsabilidade para o utilizador menos especializado (Bai, Yuan, Liu, Huang, & Feng, 2024; Quintero et al., 2018).

A definição dos perfis de utilizador constitui, por isso, uma decisão estruturante no desenho da plataforma, uma vez que determina como se distribuem responsabilidades, permissões e formas de intervenção no processo de personalização. O sistema organiza-se em três perfis principais: administrador, técnico e utilizador.

O perfil de administrador assegura a gestão global da plataforma, incluindo a criação de contas, a definição de permissões e a supervisão do ecossistema de configurações, incluindo da base de dados antropométricos. O perfil técnico, pensado para profissionais intermédios, como técnicos de ortoprotesia, clínicos ou operadores especializados, permite criar, editar e acompanhar configurações próprias e, quando aplicável, aceder às configurações dos utilizadores sob sua responsabilidade. O perfil de utilizador corresponde ao nível mais restrito, centrado na consulta das suas configurações, no acompanhamento do processo e em interacções delimitadas pelo sistema.

![](figuras/figura_5_2_painel_perfis_handfab.png)

Figura 5.2 — Painel de configuração dos perfis de utilizador na plataforma HandFab.

Fonte: produção própria.

Esta segmentação traduz uma lógica de controlo de acesso baseada em papéis, procurando equilibrar autonomia, segurança e responsabilidade distribuída ao tornar claros os limites de intervenção de cada perfil. A diferenciação participa directamente na forma como a plataforma enquadra a configuração.

Ao reservar certos parâmetros, decisões ou operações a perfis técnicos, o sistema reconhece que alguns aspectos da configuração exigem acesso condicionado. Em domínios sensíveis, como o das próteses, a interface deve tornar o processo visível e delimitar o campo de acção de acordo com critérios de supervisão e segurança. A literatura sobre interfaces clínicas e interacção em próteses inteligentes aponta para a necessidade de distinguir entre participação informada do utilizador e controlo técnico supervisionado. Esta distinção procura evitar a opacidade excessiva e a transferência imprudente de responsabilidade para agentes sem formação específica (Bai et al., 2024; Quintero et al., 2018).

Deste modo, o enquadramento conceptual articula três objectivos: tornar a lógica paramétrica operável em ambiente *web*, estruturar a configuração como uma sequência explícita e distribuir o acesso segundo papéis diferenciados. A plataforma implementa estas condições e permite conservar estados do processo; a compreensão da sequência e a adequação dos papéis permanecem por avaliar. É nesta articulação entre configuração, interface e responsabilidades que se fundamenta a arquitectura apresentada na secção seguinte.

### 5.2 Arquitectura geral do sistema

O sistema organiza-se numa estrutura em camadas que distingue interface, configuração, cálculo geométrico, visualização, persistência e serviços externos. Esta opção torna operável um modelo paramétrico tecnicamente exigente em ambiente *web* sem concentrar interacção, cálculo, armazenamento e controlo de acesso no mesmo componente. A Tabela 5.1 apresenta o fluxo completo antes da descrição de cada tecnologia.

Tabela 5.1 — Fluxo de dados e responsabilidades da plataforma

| Etapa | Componente | Entrada e saída | Responsabilidade |
| --- | --- | --- | --- |
| 1 | Interface *web* | Modelo, perfil e valores editados | Recolher escolhas, apresentar limites e manter o estado da configuração |
| 2 | Configuração do modelo | Catálogo de modelos | Declarar parâmetros, tipos, intervalos, etiquetas, dependências e campos excluídos da IA |
| 3 | Serviço de IA no servidor | Descrição, esquema e referência populacional; resposta JSON | Intermediar a chamada ao fornecedor e devolver sugestões; não gera geometria |
| 4 | *Web Worker* | Código OpenSCAD e valores | Executar o cálculo fora da tarefa principal da interface |
| 5 | OpenSCAD em *WebAssembly* | *Script* e dependências; saída OFF, STL ou 3MF | Gerar a geometria no navegador segundo regras determinísticas |
| 6 | Conversão para GLB e `model-viewer` | Geometria OFF ou 3MF | Apresentar a pré-visualização tridimensional e as cores por peça |
| 7 | Exportação | Malha STL ou pacote 3MF | Assentar peças em Z=0, preservar milímetros no 3MF e disponibilizar ficheiros para preparação |
| 8 | Programa de preparação e impressora FFF | STL/3MF, perfil de impressão e filamento | Definir camadas, orientação, suportes e trajectórias; produzir o protótipo físico |
| 9 | Servidor Express e SQLite | Utilizadores, configurações e relações de acesso | Autenticar, aplicar permissões e guardar estados da configuração |

A Figura 5.3 mostra a arquitectura implementada e as fronteiras entre navegador, servidor, fornecedor externo de IA e fabrico. A geometria é calculada no navegador; autenticação, dados e pedidos de IA passam pelo servidor; e a preparação para impressão ocorre fora da plataforma.

![](figuras/arquitectura_plataforma_parametrica.png)

Figura 5.3 — Arquitectura da plataforma e fronteiras entre navegador, servidor, serviço externo de IA e preparação do fabrico.

Fonte: produção própria.

A Figura 5.4 detalha a sequência operacional que a representação arquitectural não explicita. O perfil ou a descrição é primeiro relacionado, no servidor, com uma referência antropométrica; a IA externa apenas sugere valores iniciais condicionados pelo esquema do modelo; o servidor filtra a resposta; e a configuração só é aplicada após revisão humana. A geração da geometria permanece determinística no OpenSCAD executado no navegador, sendo a exportação uma decisão posterior à pré-visualização.

![](figuras/sequencia_perfil_ia_openscad_exportacao.png)

Figura 5.4 — Sequência de dados e decisões desde o perfil ou descrição até à sugestão, confirmação, geração determinística e exportação.

Fonte: produção própria.

A Tabela 5.2 identifica o estado técnico necessário para interpretar o artefacto sem converter esta dissertação numa descrição exaustiva da implementação. Os estados e componentes são registados porque condicionam a leitura dos ensaios; a sua enumeração não constitui comparação entre tecnologias.

Tabela 5.2 — Componentes, estados e limites do protótipo examinado

| Elemento do percurso | Implementação e estado examinado | Função no processo de *design* | Limite da evidência |
| --- | --- | --- | --- |
| Protótipo HandFab | Estado final examinado; ensaios principais e complementares realizados em estados anteriores | Reunir configuração, pré-visualização, conservação de variantes e exportação | A evolução do protótipo impede atribuir retroactivamente funções novas aos ensaios anteriores |
| Interface no navegador | Aplicação *web* com visualizador tridimensional; demonstração pública em `handfab.pedrocandeias.net` | Tornar visível a relação entre parâmetros, forma e decisão de exportar | Chromium e Firefox produziram o mesmo resultado no caso comparado; WebKit permaneceu inconclusivo; não foi demonstrada compatibilidade universal |
| Geração geométrica | OpenSCAD executado em *WebAssembly* num *Web Worker* | Aplicar as relações paramétricas e produzir a geometria sem instalação local de CAD | O tempo e a conclusão dependem do modelo e dos recursos do equipamento; não houve estudo comparativo de desempenho |
| Servidor e acesso | Node.js 22.14.0, Express 4.18.3 e autenticação por perfis | Guardar contas e configurações e intermediar os pedidos externos | O funcionamento foi examinado em casos delimitados; não foram avaliados carga, acessos simultâneos ou segurança integral |
| Dados guardados | SQLite integrado no Node.js | Conservar perfis, configurações e relações de atribuição | Adequado ao protótipo examinado; não foi comparado com outras soluções nem testado em utilização intensiva |
| Serviço externo de IA | Anthropic ou OpenAI, seleccionável; `claude-sonnet-4-6` no ensaio reportado | Sugerir valores iniciais condicionados pelo modelo activo | Depende da disponibilidade externa e da qualidade do pedido; não gera nem aprova a geometria |

A distribuição da informação segue as mesmas fronteiras. O navegador conserva o estado corrente da configuração, executa o modelo OpenSCAD e prepara a pré-visualização e os ficheiros de exportação. O servidor guarda contas, perfis e configurações e recebe os pedidos de sugestão. O fornecedor de IA recebe a descrição introduzida, o identificador e o esquema do modelo, os valores correntes e, quando existe, a referência populacional seleccionada; não recebe os ficheiros OpenSCAD, a malha gerada ou o ficheiro final de fabrico. Esta delimitação permite perceber quais as decisões locais, persistidas ou externas sem expor pormenores internos de integração irrelevantes para a argumentação do projecto.

Os estados de espera e falha foram igualmente tratados como parte do percurso. Durante a geração é apresentado um estado de processamento; um novo pedido de pré-visualização termina o cálculo anterior e cada geração ou exportação possui um limite temporal de 120 segundos. Uma falha da IA preserva a possibilidade de configuração manual; uma resposta inválida conserva o último estado válido; e uma falha de geração impede a obtenção do ficheiro até existir nova geometria válida. Os ensaios complementares confirmaram a recuperação após uma falha de geração, mas também revelaram controlos incompletos para tipos e valores fora do intervalo. Estes resultados são discutidos no Capítulo 8 e no Anexo B. Não foram executados ensaios de acessos simultâneos ou de desempenho sob carga.

A Figura 5.5 apresenta um precedente de arquitectura de produção personalizada em que a digitalização, o processamento de dados, a adaptação CAD e o fabrico aditivo são articulados num fluxo de ponta a ponta. No presente projecto, a continuidade é transferida para uma plataforma *web* e para modelos OpenSCAD executados localmente; a captura anatómica por digitalização não foi implementada (Górski et al., 2022).

![](figuras/figura_5_5_fluxo_producao_personalizada.png)

Figura 5.5 — Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo.

Adaptado de Górski, F., Zawadzki, P., Wichniarek, R., Kuczko, W., Słupińska, S., & Żukowska, M. (2022). Automated design and rapid manufacturing of low-cost customized upper limb prostheses. Journal of Physics: Conference Series, 2198, 012040. [https://doi.org/10.1088/1742-6596/2198/1/012040](https://doi.org/10.1088/1742-6596/2198/1/012040) Licença: CC BY 3.0.

No navegador do utilizador, a aplicação integra os componentes responsáveis pela interface, pela recolha e edição de parâmetros, pela gestão do estado da sessão e pela visualização local dos modelos. No servidor, um serviço desenvolvido em Node.js, com recurso à infra-estrutura Express.js, assegura a disponibilização de ficheiros estáticos, o processamento de pedidos à interface de programação de aplicações (*Application Programming Interface* — API), a autenticação de utilizadores, a aplicação de permissões e a comunicação com a camada de persistência. Esta distribuição de responsabilidades evita que a interface dependa de processamento remoto contínuo para todas as operações e, simultaneamente, impede que tarefas sensíveis, como a gestão de utilizadores, o controlo de acessos e a comunicação com serviços externos, fiquem expostas directamente no cliente. A arquitectura não corresponde, portanto, a uma simples divisão técnica entre cliente e servidor, mas sim a uma estratégia de contenção da complexidade e de delimitação explícita de responsabilidades.

A camada de persistência assenta numa base de dados SQLite, utilizada para armazenar contas de utilizador, configurações guardadas, relações de atribuição técnica e *tokens* de autenticação. A escolha desta solução responde ao carácter prototípico e funcional do sistema nesta fase da investigação, privilegiando a leveza de implementação, a portabilidade e a facilidade de manutenção. As configurações paramétricas são armazenadas como estruturas JSON associadas a um modelo e a um utilizador, permitindo preservar diferentes instâncias, recuperá-las em momentos posteriores e compará-las como estados distintos do processo de projecto. A base de dados funciona como repositório administrativo e sustenta a continuidade do processo, a gestão prática de versões e o acompanhamento das variantes produzidas.

Um dos aspectos mais relevantes da arquitectura é que a renderização geométrica não é executada no servidor. Em vez disso, o cálculo e a geração da geometria tridimensional ocorrem localmente no navegador, por meio de uma versão do OpenSCAD compilada para *WebAssembly*, tecnologia que permite executar código de elevado desempenho em ambiente *web*. Este processo é realizado num *Web Worker*, isto é, numa tarefa separada da interface principal, evitando que a geração do modelo bloqueie a interacção do utilizador com a plataforma. Esta decisão reduz a carga computacional do servidor, diminui a dependência de um serviço remoto de renderização e favorece uma interacção mais imediata durante a edição paramétrica. Ao mesmo tempo, preserva-se uma fronteira clara: o servidor mantém-se responsável pela autenticação, armazenamento, gestão de configurações e intermediação de chamadas a serviços de inteligência artificial, enquanto o cliente assume a computação geométrica intensiva. A arquitectura resultante é, assim, híbrida: centraliza funções de controlo e persistência, mas distribui localmente a geração formal do modelo.

O controlo de acesso diferencia administrador, técnico e utilizador por autenticação por *JSON Web Token* (JWT). Para a presente investigação, estes mecanismos interessam enquanto suporte da distribuição de papéis e da conservação das configurações, não como contributo autónomo de segurança informática. Os ensaios confirmam autenticação, permissões e recuperação de configurações nos casos documentados, mas não constituem avaliação integral de segurança. A sua pertinência para o projecto reside em impedir que todas as decisões e operações sejam apresentadas indistintamente a todos os perfis (Quintero et al., 2018; Bai et al., 2024).

### 5.3 Integração OpenSCAD via *WebAssembly* (WASM)

A integração do OpenSCAD por meio de *WebAssembly* permite executar localmente, no navegador, um modelo paramétrico baseado em código, sem depender de um serviço externo de geração contínua. O OpenSCAD define a geometria a partir de instruções, parâmetros e relações explícitas; o *WebAssembly* (WASM) permite executar esse núcleo no ambiente *web*. Para esta investigação, a articulação preserva a lógica do modelo e disponibiliza os seus controlos através da interface, sem demonstrar, por si só, acessibilidade ou facilidade de utilização (Machado et al., 2019; Nilsiam & Pearce, 2017).

Operacionalmente, a integração articula três elementos principais: os ficheiros `.scad`, formato de *script* utilizado pelo OpenSCAD para definir modelos geométricos por código; os parâmetros introduzidos ou ajustados na interface; e o ambiente de execução em *WebAssembly*. Quando o utilizador altera uma configuração, a plataforma envia os valores actualizados para um *Web Worker*, que aplica esses parâmetros ao modelo em OpenSCAD e gera a geometria tridimensional correspondente. O resultado é depois devolvido ao visualizador no navegador, permitindo observar os efeitos das alterações sem recorrer a *software* CAD instalado localmente. Este fluxo estabelece uma ligação directa entre edição paramétrica, cálculo geométrico e resposta visual, permitindo documentar, verificar e analisar o processo na plataforma.

Do ponto de vista metodológico, esta solução tem implicações importantes. Em primeiro lugar, preserva o estatuto do modelo paramétrico como especificação explícita e não como caixa negra geométrica. A plataforma não substitui o OpenSCAD por uma representação simplificada desligada do código; antes, torna o próprio núcleo algorítmico operável em ambiente *web*. Em segundo lugar, esta integração reduz a distância entre modelação e interacção, permitindo que a exploração formal decorra num contexto mais observável e iterativo. O utilizador não necessita de dominar a sintaxe do OpenSCAD para beneficiar da estrutura paramétrica do modelo, mas essa estrutura continua a ser a base efectiva da geometria apresentada. Neste sentido, a plataforma atua como uma camada intermédia entre a disciplina técnica do código e a experiência configurável descrita na literatura sobre configuradores e sistemas de personalização digital (Nilsiam & Pearce, 2017; Ozdemir et al., 2022).

O *Web Worker* separa o cálculo da tarefa principal da interface. Nos casos observados, esta decisão manteve os controlos disponíveis enquanto a geração decorria e permitiu terminar um cálculo anterior quando era iniciada uma nova pré-visualização. Não foram medidos tempos percebidos nem estabilidade em diferentes equipamentos. A geração permanece no navegador, enquanto o servidor conserva autenticação, persistência e mediação com serviços externos.

Esta integração tem valor estratégico no contexto da investigação, pois aproxima a modelação baseada em código da sua operação numa plataforma *web*. A literatura sobre OpenSCAD sublinha a sua afinidade com fluxos consistentes, configuradores digitais e partilha de modelos paramétricos em ambientes abertos, embora muitas vezes fora de contextos protésicos e clínicos (Machado et al., 2019; Nilsiam & Pearce, 2017). No presente projecto, a adopção de WASM integra, na mesma infra-estrutura, a transparência do modelo paramétrico, o acompanhamento das interacções e a actualização iterativa da geometria.

Esta solução introduz um compromisso de projecto. O desempenho depende da complexidade do modelo, dos valores escolhidos e dos recursos do equipamento, podendo prolongar a espera ou interromper a geração. O valor demonstrado não é um desempenho superior ao CAD instalado, mas a possibilidade de relacionar, no mesmo percurso, parâmetros, forma visualizada e exportação a partir de um núcleo geométrico explícito.

A Figura 5.6 documenta a relação entre o código OpenSCAD apresentado na plataforma e a geometria tridimensional produzida a partir da configuração activa.

![](figuras/figura_5_7_codigo_modelo_handfab.png)

Figura 5.6 — Visualização do código OpenSCAD e da geometria correspondente na plataforma HandFab.

Fonte: produção própria.

### 5.4 Estrutura funcional da plataforma

A estrutura funcional da plataforma organiza-se num conjunto de módulos interligados que suportam o ciclo de configuração paramétrica: selecção do modelo, introdução e edição de parâmetros, visualização tridimensional, sugestões apoiadas por IA, gestão de configurações e administração multiutilizador. Esta organização distribui as funções segundo a sequência projectada para o processo; a clareza dessa sequência para diferentes perfis não foi avaliada com participantes.

Em vez de expor o utilizador a um ambiente indiferenciado de opções, a plataforma reparte o trabalho por etapas e componentes com funções distintas. Esta organização é coerente com a literatura sobre configuradores digitais. Segundo essa literatura, a eficácia da personalização depende, em grande medida, da clareza com que o sistema delimita o espaço de acção disponível e articula *feedback* com decisão (Ozdemir et al., 2022; Peixoto et al., 2025).

A Figura 5.7 ilustra um precedente particularmente próximo desta lógica: uma ferramenta paramétrica orientada a terapeutas ocupacionais, na qual múltiplas variantes de produto podem ser configuradas a partir de dimensões, materiais e pesos ajustáveis. A sua pertinência para esta dissertação reside em demonstrar que a parametrização ganha valor quando é mediada por uma interface dirigida a profissionais que não são necessariamente especialistas em modelação CAD.

![](projecto-completo_media/image17.png)

Figura 5.7 — Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso.

Reproduzido de Li, M., & Aflatoony, L. (2025). Parametric design and three-dimensional printing: Enabling occupational therapists to develop custom hand grips. Disability and Rehabilitation: Assistive Technology, 20(6), 1829-1837. [https://doi.org/10.1080/17483107.2025.2483953](https://doi.org/10.1080/17483107.2025.2483953)

As vistas reunidas na Figura 5.8 documentam a selecção do modelo e diferentes grupos de controlos disponibilizados pela interface de configuração.

![](figuras/figura_5_8a_modelos_handfab.png)

![](figuras/figura_5_8b_configuracao_handfab.png)

![](figuras/figura_5_8c_parametros_handfab.png)

![](figuras/figura_5_8d_materiais_handfab.png)

Figura 5.8 — Interface de selecção, configuração paramétrica e materiais da plataforma HandFab.

Fonte: produção própria.

O ponto de entrada do sistema é o módulo de selecção de modelos. Cada modelo é descrito por um ficheiro de configuração que inclui o identificador, a descrição, o ficheiro OpenSCAD associado e a lista de parâmetros editáveis. A partir dessa estrutura, a interface gera os controlos correspondentes, incluindo campos numéricos, selectores, caixas de selecção e campos de texto. Esta opção permite acomodar famílias distintas sem desenhar manualmente um ecrã exclusivo para cada modelo. Em termos funcionais, o módulo converte a biblioteca e os respectivos parâmetros num conjunto visível de decisões de configuração.

O núcleo operativo da plataforma situa-se, depois, na articulação entre o módulo de edição paramétrica e o de visualização 3D. Quando os parâmetros são alterados, o sistema recompõe o código, aciona a renderização local e devolve ao utilizador a geometria actualizada. Esta ligação directa entre edição e pré-visualização é decisiva do ponto de vista funcional, pois transforma a manipulação de variáveis abstratas em observação imediata das suas consequências formais. Funções de reposição de valores por defeito, actualização incremental e exportação de ficheiros STL ou 3MF alargam esta utilidade para além da mera experimentação visual, aproximando a plataforma de um ambiente de prototipagem e de preparação para fabrico. A literatura sobre interfaces para configuração apoiada em contexto protésico sugere precisamente que a legibilidade do processo melhora quando o utilizador consegue relacionar a acção, a consequência geométrica e a possibilidade de validação num mesmo circuito de interacção (Peixoto et al., 2025; Quintero et al., 2018).

Sobre esta base opera o módulo de apoio por inteligência artificial, que introduz uma camada adicional de mediação sem substituir a lógica principal da configuração. A partir de uma descrição livre do utilizador, ou de medidas antropométricas parciais, a interface constrói dinamicamente um pedido que inclui o esquema actual do modelo seleccionado: nomes dos parâmetros, legendas, tipos, limites mínimos e máximos e valores correntes. Esse pedido é enviado ao servidor por uma rota autenticada, que atua como intermediário entre a plataforma e o serviço externo de IA. A resposta esperada é um objecto JSON simples, composto apenas por pares parâmetro-valor. A aplicação aceita apenas chaves existentes no esquema, descarta parâmetros desconhecidos e aplica os valores resultantes aos controlos antes de accionar uma nova renderização em OpenSCAD/*WebAssembly*.

Esta arquitectura corrige uma fragilidade identificada num estado anterior, em que o pedido à IA permanecia associado a um modelo já removido e podia devolver nomes de parâmetros inexistentes. Ao condicionar a sugestão pelo esquema actual, a IA passa a operar sobre os mesmos campos que a interface e o modelo OpenSCAD. O módulo propõe um ponto de partida editável; não foi medido se reduz tempo, esforço ou dificuldade de configuração. A IA permanece um apoio sob controlo humano e não gera autonomamente a prótese.

A evolução posterior do módulo acrescentou uma referência opcional baseada em dados populacionais. Quando a interface envia a descrição do utilizador e o identificador do modelo, o servidor procura o perfil antropométrico populacional com melhor pontuação segundo sexo, idade aproximada e país, e projecta as médias desse perfil sobre os parâmetros disponíveis no modelo activo. O bloco de referência é anexado ao pedido enviado à IA, permitindo orientar a sugestão sem se sobrepor a medições fornecidas pelo utilizador. Esta solução estabelece continuidade entre três formas de introdução de dados: selecção manual de um perfil populacional, importação de perfis antropométricos e sugestão apoiada por IA.

Outro componente central é o módulo de gestão de configurações. A possibilidade de nomear, guardar, recuperar, actualizar e eliminar instâncias é particularmente relevante num processo iterativo, em que diferentes variantes podem corresponder a hipóteses sucessivas ou a estados finais. Este módulo transforma a configuração de um acto momentâneo numa sequência acumulativa, na qual diferentes estados podem ser recuperados e comparados. A gestão de configurações integra, assim, a estrutura funcional que permite acompanhar o processo ao longo do tempo.

Por fim, o módulo administrativo suporta a criação de contas, a diferenciação de permissões e a atribuição de utilizadores a técnicos. A sua presença permite representar diferentes níveis de intervenção no protótipo; não confirma que esta distribuição corresponda às práticas profissionais ou às necessidades dos futuros utilizadores. Os resultados funcionais disponíveis são apresentados na Secção 8.1 e no Anexo B.

A biblioteca organiza quatro famílias integradas na plataforma, cada uma com parâmetros, dependências, limites e modos de visualização próprios: Flexy Beast, UnLimbited Phoenix Hand, Paraglider Hand e Cyborg Beast. Os ensaios dimensionais comparativos abrangem os três primeiros; o Cyborg Beast foi integrado posteriormente e não entra nas séries comparativas. Esta distinção separa o conjunto disponível na plataforma do subconjunto abrangido pelos ensaios comparativos.

Tabela 5.3 — Modelos integrados na plataforma e respectiva avaliação

| Modelo | Origem e licença | Parâmetros configuráveis | Mecanismo de escala implementado | Ensaios e evidência no estudo |
| --- | --- | --- | --- | --- |
| Flexy Beast | Adaptação do Flexy-Beast de `daprice`, combinação do Parametric Cyborg Beast e do Flexy Hand; CC BY-SA 4.0, indicada no ficheiro-fonte | 51 declarações, das quais 15 numéricas; largura da palma, comprimentos dos cinco dedos, articulações, *gauntlet*, pino e folga | Escala da palma derivada de `(palm_breadth_mm + 5) / 55`; comprimentos dos dedos controlados individualmente | Ensaios dimensionais, cenários de IA, exportação, inspecção de malha, ficheiro de preparação para a Bambu Lab A1 e série física |
| Paraglider Hand/Flexible Flyer | Marcus Mendenhall (2020), CC BY-SA 4.0; incorpora dependências Reborn Hand, CC BY 3.0, e UnLimbited Arm, CC BY-NC-SA 4.0 | 42 declarações, das quais 15 numéricas; palma, cinco dedos, canais e dimensões do braço | Escala uniforme da palma para preservar furos circulares de pinos; comprimentos digitais independentes | Ensaios dimensionais, cenários de IA, exportação, inspecção de malha, ficheiro de preparação para a Prusa MINI e série física |
| UnLimbited Phoenix Hand V1.0 | Equipa UnLimbited/e-NABLE; CC BY-NC-SA 4.0, indicada no ficheiro-fonte | 31 declarações, das quais 12 numéricas; largura da palma, percentagem de escala e comprimentos totais e basais dos dedos | Escala uniforme principal derivada da referência de 82 mm e limitada ao intervalo de 100%–160%; parâmetros digitais permanecem limitados pelo esquema | Ensaios dimensionais, cenários de IA, exportação, inspecção de malha e ficheiro de preparação para a Bambu Lab A1 |
| Cyborg Beast | Modelo Cyborg Beast de MakerBlock/e-NABLE; a licença não está explicitada no pacote local auditado | 50 declarações, das quais 17 numéricas; palma, segmentos dos dedos, punho, *gauntlet*, pino e folga | Escala da palma derivada de `(palm_breadth_mm + 5) / 55`, com controlo independente dos segmentos digitais | Integração e renderização na plataforma; excluído da comparação dimensional, dos projectos de preparação e das séries físicas deste estudo |

Na documentação original, o Flexy Beast é apresentado como uma combinação do Parametric Cyborg Beast, de MakerBlock, com o Flexy Hand, de Steve Wood/Gyrobot. Herda deste último juntas flexíveis que substituem os parafusos Chicago e os elásticos de retorno presentes em modelos anteriores. A fonte recomenda Filaflex ou silicone moldado para essas juntas e prevê almofadas removíveis de silicone nos dedos para aumentar a aderência. Trata-se, assim, de uma arquitectura material concebida para combinar componentes estruturais rígidos com elementos flexíveis funcionalmente diferenciados (daprice, n.d.). As vantagens de peso, custo, adaptação a escalas menores e facilidade de montagem referidas na documentação de origem são características declaradas pelo autor do modelo, não resultados avaliados nesta dissertação.

As contagens da Tabela 5.3 referem-se às declarações presentes no catálogo de modelos usado nos ensaios principais. O total inclui selectores, opções de visualização e controlos não geométricos; a contagem numérica identifica os campos do tipo `number`, sem pressupor que todos representem medidas antropométricas. A ausência de uma licença explícita no pacote local do Cyborg Beast é registada como lacuna documental e não como afirmação de inexistência de licença na fonte original.

A integração consistiu em traduzir cada modelo para uma interface comum de parâmetros e em manter as restrições mecânicas específicas. O facto de um modelo aparecer na plataforma confirma a sua integração técnica; não confirma adequação clínica nem equivalência funcional entre famílias.

No caso do Paraglider Hand, também conhecido como Flexible Flyer, a integração partiu de uma mão mecânica accionada pelo corpo, derivada da linhagem Phoenix e UnLimbited. O desafio principal não foi reconstruir a geometria dos dedos, já definida em OpenSCAD, mas alinhar a lógica original do modelo com os nomes canónicos usados pelo sistema. A palma passou a ser controlada pela largura metacarpal, enquanto os dedos foram associados a comprimentos digitais independentes. Esta separação foi importante porque a largura da palma e o comprimento dos dedos não variam necessariamente na mesma proporção. Ao mesmo tempo, a palma teve de manter escalonamento uniforme, uma vez que os furos cilíndricos para pinos metálicos não podem ser deformados em elipses sem comprometer a montagem. Assim, certas medidas, como o comprimento e a espessura da palma, foram mantidas como informação contextual para a IA e para o perfil antropométrico, mas não foram usadas como transformações geométricas activas nesse modelo.

A integração do Paraglider revelou limitações práticas da execução de OpenSCAD em *WebAssembly*. Alguns ficheiros originais usavam construções sintácticas sem suporte na versão compilada para navegador, o que impediu a definição de módulos durante a renderização. A solução foi manter cópias corrigidas dos ficheiros necessários, preservar a origem do modelo e controlar explicitamente as dependências carregadas para o sistema virtual de ficheiros do navegador. Esta etapa mostrou que a compatibilidade *web* depende da qualidade geométrica do modelo e da forma como bibliotecas, ficheiros importados e variantes de sintaxe são organizados no fluxo digital.

O trabalho realizado sobre modelos do tipo Cyborg Beast/Flexy Hand teve uma função complementar. Estes modelos foram usados como base exploratória para testar uma reparametrização mais ampla, em que a geometria original foi reorganizada em torno de medidas antropométricas da palma, dos dedos, do punho e do membro residual. A versão antropométrica resultante não foi tratada como simples escala global: incorporou comprimentos digitais, espessuras estruturais, canais internos, parâmetros de *hardware* e dimensões de encaixe derivadas de medidas do antebraço. Essa experiência permitiu clarificar a diferença entre adaptar um modelo existente por multiplicadores gerais e reconstruir a sua lógica dimensional em torno de uma estrutura antropométrica coerente. Mesmo quando determinados modelos permaneceram como material de desenvolvimento e comparação, contribuíram para estabilizar a taxonomia de parâmetros que a plataforma passou a exigir aos modelos activos.

Em conjunto, estes casos mostram que a expansão da plataforma depende menos da quantidade de modelos disponíveis e mais da existência de uma gramática comum de integração. Cada nova prótese a integrar no sistema exige três operações: identificar quais parâmetros antropométricos são relevantes, decidir que parâmetros podem alterar a geometria sem quebrar interfaces mecânicas e declarar essas relações de forma compreensível para a interface, para o módulo de visualização tridimensional e para a camada de IA. A biblioteca de modelos torna-se, assim, um campo de validação técnica da própria arquitectura: quanto mais heterogéneos forem os modelos integrados, mais clara se torna a necessidade de separar dados antropométricos, regras geométricas, restrições de fabrico e sugestões apoiadas.

### 5.5 Gestão de parâmetros, versões e expansão

Controlar parâmetros constitui uma das condições centrais para transformar um modelo paramétrico num sistema configurável e persistente. Os ficheiros de configuração descrevem cada parâmetro segundo nome, tipo, valor inicial, limites, incrementos e grupo temático. Esta estrutura liga o código OpenSCAD ao espaço de alteração apresentado na interface. Em termos metodológicos, aproxima-se da lógica dos configuradores e das famílias de produto, nas quais a variação depende da preservação das relações do modelo-base (Ozdemir et al., 2022; Lei et al., 2016).

Ao descrever os parâmetros em estruturas independentes do código geométrico principal, a plataforma obtém duas vantagens. Primeiro, permite identificar as variáveis editáveis, os seus intervalos e a articulação com a interface. Segundo, permite adaptar a estrutura do sistema: os parâmetros podem ser adicionados, removidos ou ajustados sem reescrever toda a lógica de interacção. A gestão de parâmetros funciona, assim, como camada intermédia entre a definição geométrica e a experiência de uso, mantendo o modelo tecnicamente explícito sem exigir contacto directo com a sintaxe interna.

A gestão de versões manifesta-se, neste estágio do projecto, sobretudo através do armazenamento de configurações. A plataforma conserva diferentes conjuntos de parâmetros associados ao mesmo modelo, atribuindo-lhes identificação, notas descritivas e associação a um utilizador. Embora esta solução seja mais simples do que os sistemas completos de gestão de versões usados no desenvolvimento de *software*, permite acompanhar a configuração ao longo do tempo, preservar variantes e comparar estados sucessivos. Cada configuração registada constitui uma instância documentada do processo, passível de recuperação e comparação. Esta capacidade é importante num contexto em que a configuração resulta de uma sequência de aproximações, testes e correcções.

Do ponto de vista funcional, a persistência dessas configurações em estruturas JSON associadas a modelos e utilizadores reforça a continuidade entre interacção, revisão e reutilização. O sistema deixa, assim, de limitar a configuração ao estado temporário da sessão e passa a preservar um registo das configurações realizadas, possibilitando retomar soluções anteriores, documentar alternativas exploradas e preparar comparações futuras entre versões. Esta forma de gestão prática de versões é coerente com o carácter experimental da plataforma: ainda não pretende substituir mecanismos mais sofisticados de gestão de revisões, mas fornece uma base suficiente para sustentar o acompanhamento iterativo do desenvolvimento e a análise reflexiva do processo.

Quanto à expansão, a separação entre modelos, parâmetros, interface, autenticação e persistência permite acrescentar modelos OpenSCAD sem redesenhar todo o percurso. A experiência com o Paraglider, o Phoenix, o Flexy Beast e o Cyborg Beast mostrou, contudo, que não basta adicionar um ficheiro `.scad`: é necessário declarar parâmetros, dependências, limites e modos de visualização e, em alguns casos, corrigir incompatibilidades ou preservar interfaces mecânicas herdadas. A expansão é, portanto, uma actividade controlada de adaptação do projecto, e não uma importação automática de geometrias (Lei et al., 2016; Ozdemir et al., 2022).

Esta lógica permanece limitada pelas condições do protótipo. A persistência em SQLite não foi ensaiada com utilização intensiva ou acessos simultâneos, e a geração local depende dos recursos do equipamento e da complexidade geométrica. A integração de novas funções e modelos exige, por isso, nova verificação do percurso, dos limites apresentados e dos ficheiros exportados.

O contributo deste capítulo reside no desenho de um percurso integrado entre dados, configuração, visualização e preparação para fabrico. A arquitectura torna explícito onde cada transformação ocorre e permite conservar variantes do processo. Os ensaios sustentam o funcionamento técnico nas condições documentadas; não demonstram prontidão de produto, facilidade de utilização, redução de carga cognitiva, segurança clínica ou funcionamento em escala.

## Capítulo 6 — Integração da Inteligência Artificial

### 6.1 Papel da IA no sistema proposto

No sistema desenvolvido, a IA desempenha uma função diferente da que predomina nos estudos sobre próteses de membro superior. Em vez de interpretar biosinais, reconhecer gestos ou controlar o dispositivo, o modelo de linguagem sugere valores iniciais para uma configuração geométrica já formalizada (Cordella et al., 2016; Marinelli et al., 2022; Peerdeman et al., 2011).

Esta aplicação responde à fragmentação identificada entre referências antropométricas, modelos paramétricos e interfaces de configuração. A plataforma reúne esses componentes, mas não atribui à IA a geração da geometria, a selecção autónoma do dispositivo ou a validação do resultado. Os precedentes de modelação ajustável e de métodos orientados por dados sustentam esta articulação sem constituírem equivalentes directos do sistema implementado (Gu et al., 2024; da Silveira Romero et al., 2025; Saldarriaga et al., 2024).

O fluxo organiza-se em três camadas. A primeira é determinística: identifica idade e sexo quando estão explicitamente descritos, procura uma referência populacional disponível, selecciona o esquema do modelo activo e preserva decisões fixadas na interface, como a lateralidade. A segunda é probabilística: o modelo de linguagem recebe a descrição textual e o contexto paramétrico, propondo valores para os campos autorizados. A terceira verifica e aplica a resposta: interpreta o objecto JSON, confronta os campos com o modelo seleccionado, apresenta os valores na interface e permite a sua revisão antes da geração geométrica.

A geometria não é produzida pela IA. Após a aceitação ou correcção da configuração, o OpenSCAD executa relações geométricas previamente codificadas e gera a forma correspondente. Esta separação permite localizar a origem de cada decisão: dados e regras definem o espaço de configuração; a IA propõe um ponto de partida; e o designer ou técnico decide se a proposta deve ser mantida, alterada ou rejeitada.

Os testes complementares mostraram que esta terceira camada ainda não aplica uniformemente todas as restrições. A lateralidade permaneceu protegida, mas um valor numérico acima do intervalo foi detectado sem ser impedido de chegar ao estado interno da aplicação. Por isso, os limites declarados são tratados neste capítulo como restrições pretendidas e parcialmente verificadas, e não como garantia integral. A discussão ética geral permanece na Secção 2.6; o presente capítulo concentra-se na forma como esses princípios foram concretizados e nos limites observados.

### 6.2 IA na parametrização, personalização e apoio à decisão

À luz das distinções estabelecidas nos Capítulos 2 e 4, a personalização apoiada por IA não designa variação livre da forma. No protótipo, designa a proposta de valores para parâmetros previamente definidos, com relações geométricas, intervalos e campos protegidos. A independência entre dimensões dos dedos e a insuficiência do escalonamento uniforme fundamentam o espaço paramétrico; não são decisões tomadas pelo modelo de linguagem (Lim et al., 2018; Saldarriaga et al., 2024; da Silveira Romero et al., 2025).

A operacionalização desta lógica ocorre em dois objectos distintos. O primeiro é um vector numérico de parâmetros geométricos, consumido directamente pela interface e pelos modelos OpenSCAD. O segundo é um contexto semântico para a IA, que descreve a origem das medições, campos em falta, incerteza, valores atípicos, tolerâncias, componentes de montagem seleccionados e notas sobre parâmetros derivados. Esta separação é importante porque impede confundir cálculo geométrico com raciocínio apoiado: os parâmetros numéricos alimentam o modelo; o contexto semântico ajuda a IA a explicar, ponderar ou sugerir ajustes, mas não substitui as regras determinísticas que geram a geometria.

No protótipo implementado, esta separação é materializada pela construção dinâmica do pedido enviado ao modelo de linguagem. O pedido inclui a descrição livre do utilizador, o esquema do modelo seleccionado, os nomes exactos dos parâmetros, as respectivas legendas, os tipos de dados, os limites declarados e os valores correntes. Quando existe correspondência com um perfil populacional importado, inclui também as médias desse grupo como referência explícita. O pedido determina ainda que a resposta contenha apenas um objecto JSON, sem texto adicional, e exclui os campos de lateralidade e cor.

As legendas influenciam a sugestão porque explicam ao modelo de linguagem a função de cada parâmetro. Nos parâmetros antropométricos, a legenda identifica a medida e a unidade. Nos componentes mecânicos, como folgas, diâmetros ou elementos de montagem, uma sugestão só possui fundamento determinístico quando existe uma regra codificada. Na ausência dessa regra, o valor resulta do intervalo, da legenda, do valor corrente e da inferência do modelo de linguagem; deve, portanto, ser entendido como proposta inicial a confirmar tecnicamente, e não como cálculo de engenharia.

A correspondência com os perfis populacionais também segue uma regra explícita. O sistema atribui maior peso à coincidência de sexo e de grupo etário, acrescenta a proximidade da idade e a referência ao país quando esta existe no texto, e usa a presença de medidas da mão e de estatísticas centrais como critérios secundários. Só é seleccionado um perfil quando a pontuação mínima é atingida. Caso contrário, o pedido é enviado sem referência populacional, ficando a sugestão assinalada como não apoiada por essa base. Mesmo quando existe correspondência, os dados populacionais constituem uma aproximação e não substituem medidas individuais.

Neste enquadramento, a IA pode interpretar descrições incompletas, propor valores iniciais para campos autorizados e preencher lacunas com apoio das referências disponíveis. Não pode escolher autonomamente o modelo protésico, definir a lateralidade, ultrapassar deliberadamente os limites do modelo, confirmar adequação anatómica ou clínica, gerar a forma final, nem aprovar a exportação ou o fabrico. Estas decisões permanecem nas regras do sistema e na intervenção humana.

A designação «modelo» é usada, nesta investigação, em dois sentidos técnicos distintos: o modelo de linguagem responsável pela sugestão paramétrica e o modelo CAD paramétrico ao qual essa sugestão é aplicada. Para evitar ambiguidade metodológica, a Tabela 6.1 explicita a configuração de IA efectivamente implementada no protótipo e a sua relação com os modelos paramétricos disponibilizados na plataforma.

Tabela 6.1 — Especificação técnica dos modelos de IA e da estrutura da sugestão paramétrica

| Elemento | Especificação no protótipo |
| --- | --- |
| Função da IA | Sugestão inicial de parâmetros antropométricos e geométricos a partir de descrições em linguagem natural; não gera autonomamente a geometria final nem valida clinicamente a prótese. |
| Ponto de integração | `POST /api/ai/suggest`, através de chamada autenticada e limitada por frequência, com as chaves de API mantidas no servidor. |
| Fornecedor e modelo usados na validação | Anthropic, com o modelo `claude-sonnet-4-6`, definido como opção predefinida no servidor do protótipo. |
| Modelo alternativo disponibilizado | OpenAI, com o modelo `gpt-4`, acessível através da mesma rota de sugestão paramétrica. |
| Selecção do fornecedor | A interface permite escolher entre `Anthropic (Claude)` e `OpenAI (GPT-4)`; o pedido enviado ao servidor identifica o fornecedor através do campo `provider`. |
| Parâmetros da chamada avaliada | Resposta limitada a 1024 *tokens*; o código não fixa a temperatura na chamada ao `claude-sonnet-4-6`, pelo que fica em vigor a configuração do fornecedor. O percurso OpenAI fixa a temperatura em 0,7, mas não integra a avaliação reportada. |
| Estrutura da resposta | Objecto JSON simples no formato parâmetro–valor. A lateralidade é ignorada e os campos desconhecidos não são aplicados. Os testes revelaram que a verificação de tipos e intervalos ainda não é uniforme em todos os percursos de submissão. |
| Enquadramento dos dados | O pedido inclui o esquema vivo do modelo, limites mínimos e máximos, valores correntes, legendas dos parâmetros e, quando disponível, médias de perfis antropométricos populacionais. |
| Estados examinados | A avaliação inicial incidiu sobre o estado usado nos ensaios principais. A série complementar de controlo da interface e dos dados submetidos foi executada num estado posterior. |
| Modelos CAD abrangidos | Flexy Beast, Paraglider Hand, UnLimbited Phoenix e Cyborg Beast estavam registados; a avaliação dimensional e de geração repetida abrangeu os três primeiros. |

Neste estudo, «apoio à decisão» tem um alcance operacional restrito: produzir uma configuração inicial editável e tornar explícitos os dados considerados. Não foi implementada uma função objectivo nem uma comparação automática de robustez, peso, montagem ou adequação anatómica. Por esse motivo, o processo é designado como sugestão inicial condicionada e não como optimização. A aceitação, correcção ou rejeição dos valores ocorre fora do modelo de linguagem e antecede a geração e a exportação da geometria.

### 6.3 Avaliação das sugestões paramétricas apoiadas por IA

A avaliação desta componente verifica a coerência das sugestões face ao esquema e aos intervalos de referência adoptados. O termo «antropométrica» descreve a origem dos campos e das referências; não significa que exista confirmação anatómica individual. Os resultados são apresentados no Capítulo 8, mantendo esta secção dedicada ao protocolo.

A avaliação utilizou o fornecedor Anthropic e o modelo `claude-sonnet-4-6`. A resposta estava limitada a 1024 *tokens* e o código não fixava a temperatura. O pedido incluía a descrição do cenário, o identificador do modelo, os nomes exactos dos parâmetros, os respectivos tipos, limites e valores correntes, etiquetas explicativas e, quando existia correspondência, uma referência populacional. O pedido exigia um objecto JSON com pares parâmetro–valor. Foram conservados o modelo utilizado, as condições da chamada, as descrições submetidas, as respostas e as decisões de correcção relevantes.

Foram usados cinco perfis baseados em indicadores demográficos e três cenários de ausência unilateral com diferentes níveis de detalhe: medidas completas da mão contralateral, uma medida directa e descrição demográfica. Uma bateria complementar reuniu 15 cenários construídos a partir de descrições vagas, comparativas, multilingues ou sem medidas. Para examinar a lateralidade, foram ainda arquivadas 12 execuções antes da correcção, correspondentes a pedidos de mão esquerda e direita repetidos quatro vezes. Os cenários representam descrições hipotéticas que poderiam ser submetidas ao sistema e não constituem avaliação centrada no utilizador, porque nenhuma pessoa participou no estudo.

Os critérios foram: JSON interpretável; chaves pertencentes ao esquema; valores nos intervalos; preservação das medidas fornecidas; ordem relativa dos dedos definida no protocolo; resposta diferenciada a idade e sexo quando a base continha referência compatível; e propagação dos valores para a geometria. Países ausentes da base, como Brasil, Japão e Alemanha, funcionaram como testes de resposta a cobertura incompleta. Nesses casos, o país não sustenta uma correspondência nacional: o mecanismo selecciona o perfil disponível com melhor pontuação noutros atributos ou prossegue sem referência quando a pontuação mínima não é atingida.

Numa série complementar de ensaios foram usadas respostas de IA simuladas e previamente controladas. Esta série não contactou um modelo de linguagem e, por isso, não mede a variação, a consistência entre repetições ou a precisão da IA. Serviu para observar o comportamento da plataforma perante uma resposta válida, JSON inválido, campos de lateralidade, valores fora do intervalo e nova tentativa após erro. A lateralidade foi preservada e uma resposta inválida não alterou o último estado válido. Em contrapartida, um valor acima do máximo foi detectado pelo ensaio, mas permaneceu no estado interno; foi também aceite por pedido directo um texto num campo definido como numérico. Estes dois casos são registados como fragilidades de controlo, não como respostas válidas.

A cadeia contém operações determinísticas e uma operação gerada por modelo de linguagem. A distinção é sintetizada na Tabela 6.2.

Tabela 6.2 — Distribuição de tarefas entre regras, IA e supervisão humana

| Tarefa | Mecanismo | Resultado |
| --- | --- | --- |
| Identificar sexo e idade explícitos | Analisador de texto e, quando faltam campos, extracção opcional por `claude-haiku-4-5-20251001` a temperatura 0 | Atributos para procurar uma referência populacional |
| Escolher o perfil disponível mais próximo | Pontuação por sexo, grupo etário, idade e país, com critérios de desempate de qualidade | Referência quantitativa; não corresponde a diagnóstico nem a correspondência nacional garantida |
| Sugerir campos em falta | `claude-sonnet-4-6` | Ponto de partida sujeito a alterações entre execuções |
| Declarar tipos e limites | Ficheiro de configuração do modelo | Intervalos e tipos disponíveis para a interface, para o pedido e para a verificação |
| Verificar a resposta antes da aplicação | Interpretação do JSON e confronto com o modelo activo | Campos desconhecidos e lateralidade excluídos; controlo de tipos e intervalos ainda incompleto na estado avaliado |
| Definir lateralidade | Controlo da interface com o papel `laterality` | Escolha fixa excluída das sugestões |
| Gerar a geometria | Regras OpenSCAD executadas em *WebAssembly* | Forma determinística para um mesmo conjunto de parâmetros e estado do código |
| Aceitar, corrigir ou rejeitar a configuração | Designer ou técnico responsável | Decisão humana antes da exportação e de qualquer utilização posterior |

O protocolo não mede exactidão clínica da IA, porque não existe uma referência individual para cada cenário. Também não compara fornecedores, modelos de linguagem, temperaturas ou estratégias de pedido. Como a série complementar utilizou respostas simuladas, esta também não sustenta conclusões sobre estabilidade do `claude-sonnet-4-6`. A interpretação limita-se ao comportamento observado nas execuções iniciais e à resposta da plataforma nos casos de controlo documentados. Os resultados consolidados são apresentados no Capítulo 8 e a matriz integral de casos consta do Anexo B.

### 6.4 Ajuste, verificação e limitações éticas e técnicas

Para interpretar as saídas do sistema, distinguem-se três estados: sugestão produzida pelo modelo de linguagem; configuração aceite ou corrigida na interface; e resultado submetido a verificação geométrica e de fabrico. A passagem entre estes estados não demonstra ajuste anatómico, conforto, segurança estrutural ou validade clínica.

Os riscos técnicos relevantes são respostas plausíveis para perfis pouco representados, campos sem fundamento suficiente e combinações que parecem respeitar parâmetros isolados, mas falham na geometria completa. A estado avaliado reduz parte destes riscos através do esquema activo, da exclusão de campos desconhecidos, do controlo determinístico da lateralidade e da inspecção posterior da malha. Contudo, os testes demonstraram que declarar um intervalo não basta: a mesma verificação deve actuar antes de o valor entrar no estado da aplicação, ser guardado ou seguir para a geração geométrica. As salvaguardas existentes tornam alguns erros localizáveis, mas não garantem adequação do resultado (Panchal et al., 2019; Yüksel et al., 2023).

A Figura 6.1 sintetiza esta tensão entre os desafios de compreensão das decisões e os princípios de IA responsável. No contexto desta investigação, a figura mostra que a responsabilidade depende do desempenho preditivo e de condições como transparência, possibilidade de examinar as decisões, privacidade, justiça e prestação de contas. Estes princípios reforçam a opção do sistema por uma IA de apoio, limitada por regras e sujeita a revisão humana (Barredo Arrieta et al., 2020).

![](figuras/figura_6_1_ia_responsavel_estilizada.png)

Figura 6.1 — Relação entre desafios de compreensão das decisões e princípios de IA responsável.

Adaptado de Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82-115. [https://doi.org/10.1016/j.inffus.2019.12.012](https://doi.org/10.1016/j.inffus.2019.12.012)

No plano ético, a arquitectura examinada usa referências antropométricas não clínicas e cenários simulados, mantém as chaves dos fornecedores no servidor e diferencia acessos. Permanecem por implementar ou avaliar a apresentação sistemática da origem das referências, a comunicação da incerteza, a minimização de dados num eventual uso com pessoas e a compreensão dos avisos pelos diferentes perfis. Estes requisitos correspondem às dimensões de transparência, privacidade e prestação de contas sintetizadas na Figura 6.1 (Barredo Arrieta et al., 2020).

Consequentemente, a evidência permite avaliar a integração e as salvaguardas técnicas da IA, mas não autoriza classificá-la como autoridade clínica nem como mecanismo autónomo de personalização. A qualidade das sugestões continua condicionada pela cobertura dos dados, pelo esquema do modelo e pela verificação das geometrias produzidas.

## Capítulo 7 — Princípios de Interface e Decisões de Interacção

### 7.1 Estratégia de interacção e decisões de UI/UX

A interface organiza o fluxo implementado em seis operações: seleccionar um modelo, introduzir ou obter valores iniciais, ajustar parâmetros, gerar e observar a geometria, guardar a configuração e exportar ficheiros. Esta sequência traduz a arquitectura técnica em tarefas visíveis; a sua facilidade de utilização não foi avaliada com participantes.

A composição é modular e orientada por tarefa. A selecção do modelo define o esquema activo; os controlos apresentam parâmetros editáveis e respectivos intervalos; a pré-visualização mostra a geometria efectivamente produzida; e as acções de guardar, recuperar e exportar preservam estados distintos. Esta organização procura manter uma relação identificável entre valor, acção e consequência formal (Colombo et al., 2015; Peixoto et al., 2025).

O espaço de configuração apresentado não é ilimitado. A interface expõe apenas os campos declarados para o modelo, apresenta os intervalos existentes e exclui decisões como a lateralidade do pedido enviado à IA. Esta contenção orienta a configuração, mas não garante, por si só, que todos os percursos de submissão respeitem as mesmas regras. Os testes complementares mostraram que um valor acima do intervalo podia permanecer no estado interno da aplicação e que um campo numérico podia receber texto por meio de um pedido directo. Assim, o controlo visual deve ser acompanhado pela verificação do valor antes de este ser aplicado, guardado ou enviado para a geometria.

A pré-visualização é calculada localmente por OpenSCAD em *WebAssembly*. O *Web Worker* separa essa execução da tarefa principal da interface, evitando o bloqueio directo durante o cálculo. Não foram medidos o tempo percebido, a compreensão dos estados nem a qualidade da interacção (Abbas Alili et al., 2023; Quintero et al., 2018).

A avaliação de acessibilidade combinou uma verificação automática de oito estados do percurso autenticado com uma verificação manual complementar. A análise automática identificou contraste insuficiente, ausência de associação programática entre alguns rótulos e controlos, elementos interactivos aninhados e falta de nome acessível num elemento de selecção. Na grelha manual, sete das doze verificações foram classificadas como conformes e cinco como não conformes. O percurso com o Orca revelou limitações na ordem e na descrição dos campos; a interface permaneceu apenas parcialmente utilizável com ampliação a 400%; e o visualizador tridimensional não apresentou uma alternativa textual reconhecível. A classificação manual do contraste como conforme não elimina as ocorrências detectadas automaticamente. Estes resultados localizam decisões de interface a rever, mas não demonstram a experiência de pessoas com diferentes capacidades nem conformidade global com as WCAG 2.2.

Assim, esta secção descreve uma especificação de projecto, as funções disponíveis e os limites já observados. Clareza, carga cognitiva, aprendizagem, acessibilidade percebida e adequação aos diferentes perfis permanecem questões para avaliação futura com participantes.

### 7.2 Papéis previstos e distribuição de decisões

Os fundamentos de participação e de distribuição de autoridade foram discutidos na Secção 2.7. Na implementação, traduzem-se em três perfis de acesso — administrador, técnico e utilizador — cuja adequação às práticas profissionais ainda não foi avaliada.

O administrador gere contas, permissões e relações de atribuição. O perfil técnico pode criar, editar, guardar e acompanhar configurações sob a sua responsabilidade. O utilizador dispõe de consulta, visualização e acompanhamento das configurações que lhe estão associadas. Esta distribuição descreve permissões do protótipo, não competências clínicas verificadas.

Os parâmetros apresentados dependem do modelo activo e do perfil de acesso. Valores geométricos editáveis são limitados pelo esquema; a lateralidade é controlada pela interface; e a aceitação de sugestões permanece uma acção distinta da sua geração. A plataforma não implementa decisões clínicas sobre encaixe, tolerância dos tecidos ou adequação funcional.

Esta separação materializa uma colaboração assimétrica: o perfil técnico possui maior capacidade de intervenção e o utilizador final acompanha o processo. Não foram medidos os efeitos desta distribuição sobre compreensão, confiança, rapidez ou qualidade da decisão (Bai et al., 2024; Colombo et al., 2015; Quintero et al., 2018).

A Figura 7.1 evidencia a importância de analisar a utilização concreta do dispositivo, para além da sua configuração digital. A avaliação com utilizadores permite identificar problemas relacionados com o ajuste ao corpo, o modo de activação, o conforto e a adequação funcional, aspectos que dificilmente podem ser avaliados adequadamente apenas com o modelo digital. Para esta investigação, a imagem constitui um ponto de referência metodológico: embora a plataforma possa tornar o processo mais claro e configurável, a validação futura continua a depender da observação do uso em contexto real (Silva et al., 2018).

![](projecto-completo_media/image19.png)

Figura 7.1 — Exemplo publicado de teste de uma prótese impressa em 3D com um utilizador; esta actividade não integrou a avaliação da presente dissertação.

Reproduzido de Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

### 7.3 Mediação do processo de *design* e reflexão crítica

A mediação fundamentada no Capítulo 2 torna-se observável, no protótipo, na sequência entre leitura dos dados, proposta de valores, geração da geometria, revisão e exportação. A interface não acrescenta uma nova teoria de personalização; materializa decisões sobre o que é mostrado, editado, guardado ou reservado.

Quatro mecanismos concretizam essa função: exposição selectiva dos parâmetros; apresentação dos respectivos limites; diferenciação de permissões; e separação visual entre sugestão, configuração e geometria gerada. Em conjunto, estes mecanismos permitem examinar parte da relação entre valor, controlo e resultado, mas também condicionam o conjunto de alternativas que pode ser explorado (Bai et al., 2024; Peixoto et al., 2025; Quintero et al., 2018).

Esta condição impede considerar a interface neutra. Um valor apresentado como sugestão pode adquirir aparência de validade, mesmo quando resulta de uma referência populacional incompleta ou de uma saída probabilística. Por isso, a origem, a incerteza e o estatuto de cada valor devem permanecer visíveis; a estado avaliado implementa apenas parte dessa comunicação.

A separação entre sugestão, configuração e geometria constitui uma decisão de projecto observável. Uma resposta de IA inválida preservou o último estado válido e permitiu nova tentativa, mostrando capacidade de recuperação nesse percurso. Contudo, a aplicação de um valor acima do intervalo revelou que a reversibilidade e a limitação do espaço paramétrico ainda não estão asseguradas em todos os percursos de submissão. A aprendizagem resultante é que mensagens, limites e regras devem permanecer coerentes para além dos controlos visíveis da interface.

A evidência disponível permite descrever a organização das decisões, identificar salvaguardas incorporadas e localizar barreiras técnicas de acessibilidade. Não permite concluir que os diferentes perfis compreendem os limites, tomam melhores decisões ou utilizam a plataforma com menor esforço. Essas questões exigem observação de tarefas com participantes.

O contributo desta camada de interface é, portanto, tornar operacional e discutível a distribuição de informação e controlo no fluxo técnico. A responsabilidade pela adequação da configuração e a validação do dispositivo permanecem fora da interface e do alcance demonstrado pelo estudo.

## Capítulo 8 — Avaliação e Discussão

### 8.1 Estratégia e critérios de avaliação

A avaliação foi organizada em quatro níveis: funcionamento dos componentes da plataforma; coerência das sugestões de IA; propagação dos parâmetros para a geometria; e passagem dos ficheiros para preparação e impressão. Os critérios foram definidos na Secção 3.5. Os resultados demonstram condições técnicas específicas e não equivalem a uma avaliação clínica, funcional ou de experiência de utilização.

### 8.1.1 Verificação técnica da plataforma

O funcionamento da plataforma foi examinado através das funções que sustentam o percurso entre dados antropométricos, configuração, visualização e preparação para fabrico. A Tabela 8.1 sintetiza a evidência observada e explicita a sua relevância para o processo de *design* e os respectivos limites. Os comandos, datas de execução e identificadores internos dos testes são conservados no Suplemento 2 — Avaliação técnica da plataforma.

Tabela 8.1 — Evidência do funcionamento da plataforma no processo de projecto

| Função examinada | Evidência observada | Relevância para o processo de *design* | Limite de interpretação |
| --- | --- | --- | --- |
| Correspondência entre descrição e perfil | As descrições de ensaio foram relacionadas com referências populacionais segundo sexo, idade, grupo etário e disponibilidade geográfica | Permite introduzir uma referência antropométrica inicial no percurso de configuração | A referência é populacional, não individual, e não demonstra adequação anatómica |
| Selecção de modelos | Quatro modelos com parâmetros próprios podem ser seleccionados e configurados na mesma interface | Demonstra que a plataforma acomoda famílias geométricas com regras distintas num percurso comum | Apenas três modelos integram a comparação dimensional principal |
| Base antropométrica | A aplicação reúne 100 perfis agregados por população, sexo, idade e tipo de estatística | Disponibiliza referências mensuráveis para iniciar ou contextualizar decisões paramétricas | A cobertura geográfica e etária é desigual e os perfis não substituem medições directas |
| Conservação de configurações | Perfis, valores paramétricos e configurações podem ser guardados e recuperados | Permite retomar, documentar e comparar variantes ao longo do processo de projecto | Não foram avaliados utilização intensiva, acessos simultâneos ou práticas reais de colaboração |
| Visualização e exportação | As configurações examinadas produziram pré-visualizações tridimensionais e ficheiros STL e 3MF | Mantém continuidade entre alteração de parâmetros, observação da geometria e preparação para fabrico | A exportação não garante imprimibilidade, montagem, segurança ou adequação clínica |
| Sugestão apoiada por IA | A descrição e a referência antropométrica podem originar uma proposta inicial de valores, posteriormente editável | Apoia a exploração preliminar sem retirar ao utilizador o controlo da configuração | Depende de serviços externos e não decide nem valida a geometria final |

Estes resultados confirmam a existência e a integração dos componentes examinados. Não demonstram desempenho sob carga, segurança integral, compatibilidade com todos os navegadores ou uso autónomo por pessoas sem formação técnica.

### 8.1.2 Avaliação complementar da consistência da geração, recuperação e acessibilidade

Para verificar a consistência da geração, cada modelo foi exportado repetidamente, mantendo inalterados os valores dos parâmetros. Foram concluídas sete exportações do Flexy Beast, cinco do Paraglider Hand e cinco da UnLimbited Phoenix. Em cada modelo, todas as exportações concluídas produziram ficheiros exactamente iguais ao nível dos dados binários, isto é, com a mesma sequência de zeros e uns que constitui o seu conteúdo digital, e conservaram as mesmas dimensões e métricas geométricas. O critério previamente definido exigia dez exportações concluídas por modelo; como algumas tentativas foram interrompidas por bloqueios e tempos-limite no ambiente de ensaio, o resultado é parcial. A evidência sustenta a consistência das exportações concluídas, mas não permite considerar cumprido o critério definido para a totalidade das repetições.

A mesma configuração da UnLimbited Phoenix produziu resultados idênticos no Chromium e no Firefox. Uma primeira tentativa com WebKit foi invalidada por uma opção de arranque aplicada incorrectamente pelo próprio instrumento de ensaio. Após a correcção dessa configuração, o navegador iniciou, mas o percurso parou na autenticação e não chegou à geração da geometria. A compatibilidade com WebKit permanece, por isso, inconclusiva; a falha não é classificada como incompatibilidade da plataforma.

Os cenários de recuperação abrangeram valores nos limites, dados inválidos, ausência de cobertura populacional directa, incompatibilidade entre perfil e modelo, indisponibilidade do serviço de IA, falha de renderização e tentativa de exportação sem geometria. A maioria dos percursos rejeitou os dados inválidos, preservou o último estado válido ou permitiu nova tentativa. Foram, contudo, identificadas duas fragilidades relevantes para o *design* do controlo: uma sugestão simulada de IA acima do limite foi detectável pelo esquema, mas chegou a ser aplicada ao valor interno; e a interface rejeitou texto num campo numérico enquanto o pedido directo à plataforma aceitou esse mesmo tipo de valor. Estes resultados mostram que a protecção não deve depender apenas do controlo visual e que as mesmas regras têm de actuar antes de qualquer valor ser guardado ou enviado para a geometria.

A auditoria automática de acessibilidade examinou oito estados do percurso local autenticado e identificou quatro categorias de barreira: contraste de cor insuficiente, ausência de associação programática entre rótulos e controlos, elementos interactivos aninhados e falta de nome acessível num elemento de selecção. A página pública não autenticada não apresentou violações automáticas nos elementos examinados, mas incluiu uma verificação inconclusiva e não representa os percursos internos. Na verificação manual complementar, sete das doze verificações foram classificadas como conformes e cinco como não conformes. O percurso com o Orca revelou problemas na ordenação e na descrição dos campos; a interface foi apenas parcialmente utilizável com ampliação a 400%; e o visualizador tridimensional não disponibilizou uma alternativa textual reconhecível. A classificação manual do contraste como conforme não invalida as ocorrências automáticas. Em conjunto, os resultados definem prioridades concretas de revisão, mas não demonstram conformidade global com as WCAG 2.2 nem acessibilidade percebida por utilizadores.

Em termos de *Design* Industrial, estas séries de ensaios acrescentam três aprendizagens ao desenvolvimento do artefacto. A consistência dos resultados depende de regras geométricas explícitas e de condições de execução suficientemente estáveis; a robustez exige que limites e mensagens sejam coerentes em todas as etapas do fluxo; e a acessibilidade deve ser tratada como qualidade verificável da interface, e não apenas como intenção inclusiva. O Anexo B conserva a matriz de casos, os resultados por execução e a ficha técnica mínima necessária para permitir a sua revisão crítica.

### 8.1.3 Preparação para impressão e protótipos físicos

A evidência de fabrico inclui 116 ficheiros 3MF gerados para três modelos e quatro perfis de ensaio, quatro projectos com parâmetros de preparação e fotografias de peças físicas. Os 116 ficheiros representam exportações digitais, distribuídas por placas combinadas e peças individuais; esse total não corresponde a 116 impressões físicas. Os quatro projectos de preparação digital para impressão 3D com configuração analisada são entregues na subpasta `projectos_preparacao/` do Suplemento 4 — Preparação para impressão e protótipos. Cada projecto identifica um perfil de 15 anos, o material configurado e a impressora usada. A série documenta os projectos individualmente e não pressupõe condições comparáveis entre eles.

Tabela 8.2 — Projectos de preparação digital para impressão 3D com configuração analisada

| Modelo e cenário | Impressora e programa | Parâmetros principais | Evidência observada |
| --- | --- | --- | --- |
| Flexy Beast, 15 anos | Bambu Lab A1, Bambu Studio 1.10.02.76 | Camada 0,24 mm; duas paredes; enchimento 15% em grelha; suporte em árvore; aba 5 mm; objectos atribuídos ao extrusor PLA | Dez segmentos digitais importados; programa regista 0 arestas corrigidas e 0 faces degeneradas |
| UnLimbited Phoenix, 15 anos | Bambu Lab A1, Bambu Studio 1.10.02.76 | Dois ficheiros de preparação com camada de 0,24 mm, duas paredes e 15% de enchimento: peças atribuídas, respectivamente, a PLA e a Bambu PETG Basic; no PETG, bico a 255 °C e mesa a 70 °C | Oito conjuntos de peças em cada ficheiro; o programa regista 0 arestas corrigidas e 0 faces degeneradas |
| Paraglider Hand, 15 anos | Prusa MINI, PrusaSlicer 2.8.1 | Camada 0,20 mm; duas paredes; enchimento 15% em grelha; PLA; bico 0,4 mm; mesa 60 °C; suporte e aba desactivados | Projecto 3MF com configuração da impressora, do filamento e da placa |

Os quatro ficheiros de preparação da Série A foram novamente processados com as definições neles conservadas. Em todos foram geradas trajectórias e estimativas. O Flexy Beast em PLA apresentou 2 h 21 min 50 s e 56,51 g; o Phoenix apresentou 5 h 12 min 44 s e 123,52 g em PLA e 5 h 51 min 52 s e 117,54 g em PETG; o Paraglider apresentou 2 h 32 min 11 s e 37,96 g em PLA. Estes valores são estimativas dos programas e não medições de impressões reais. Como os ficheiros usam condições distintas, não permitem concluir que um modelo, material, programa ou equipamento seja mais rápido ou económico.

Na Série B, as doze combinações entre três modelos e quatro perfis foram processadas numa condição digital comum: Bambu Lab A1, PLA, camada de 0,20 mm, duas paredes, enchimento de 15% em grelha e suportes desligados. Foram geradas trajectórias e estimativas em 12/12 casos. Os tempos variaram entre 4 h 22 min 47 s, no Paraglider `child_8`, e 12 h 34 min 14 s, no Flexy Beast `adult_28`; as massas estimadas variaram entre 50,07 g e 169,15 g nos mesmos casos. O programa assinalou regiões suspensas nos quatro casos Flexy Beast e no Paraglider `elderly_70`. Estes avisos mostram que a comparação digital não substitui a revisão da orientação e dos suportes antes da impressão.

A comparação dimensional reuniu 36 extensões X, Y e Z das palmas exportadas e 72 valores medidos nas peças correspondentes, metade em PLA e metade em PETG. No Phoenix, a largura de entrada e a extensão X da malha ficaram próximas; no Flexy Beast e no Paraglider, a extensão exterior inclui interfaces e margens decorrentes da geometria-base. Por isso, a diferença entre parâmetro e caixa exterior descreve a transformação decorrente do projecto e não é tratada como erro. Nas peças físicas, todos os valores ficaram abaixo das extensões das malhas: os desvios percentuais variaram entre −0,321% e −0,274% em PLA e entre −0,425% e −0,369% em PETG. O Anexo D apresenta os resultados completos e a compatibilidade delimitada com as orientações de escala. Como existe uma única leitura registada por eixo, os resultados não permitem quantificar a dispersão ou a incerteza de medição.

Foram produzidos exemplares em PLA e PETG, e as configurações analisadas identificam o material atribuído às peças preparadas. No caso da UnLimbited Phoenix, a configuração PETG atribui os oito conjuntos de peças ao perfil Bambu PETG Basic. As medições permitem uma comparação dimensional emparelhada das palmas produzidas nos dois materiais: nos exemplares registados, o PETG apresentou desvios negativos ligeiramente superiores aos do PLA. Como não existem leituras repetidas nem uma série experimental destinada a isolar o efeito do material, esta diferença não deve ser generalizada como taxa própria de contracção. Também não se retiram conclusões sobre resistência, fragilidade ou durabilidade relativas de PLA e PETG sem ensaios mecânicos comparáveis.

Embora a documentação de origem do Flexy Beast preveja juntas em filamento flexível ou silicone moldado, não foram produzidas juntas flexíveis nem almofadas de silicone dos dedos. Os exemplares rígidos em PLA ou PETG não substituem esses componentes. Por conseguinte, não foram avaliados o comportamento elástico das juntas, o retorno dos dedos, a aderência das almofadas ou a influência desses elementos na montagem e no funcionamento do dispositivo.

A utilização da Bambu Lab A1 e da Prusa MINI documenta a execução do fluxo em dois ambientes de fabrico, mas não constitui uma comparação entre equipamentos. Os modelos, os programas de preparação para impressão e parte das definições usadas diferem entre os projectos, e nenhuma geometria equivalente foi repetida nas duas impressoras sob condições controladas. Não é, por isso, possível isolar o efeito da impressora, comparar qualidade ou velocidade, nem concluir que o fluxo exige dois equipamentos.

Uma inspecção complementar com `trimesh`, arquivada com os cenários de 29 de Junho de 2026, examinou as malhas geradas a partir do perfil antropométrico de ensaio de 8 anos. Os critérios foram fecho da superfície, carácter múltiplo da geometria, número de corpos e faces de área nula. A Tabela 8.3 mostra que a preparação aceite pelo programa não implica que a malha de origem seja um sólido fechado sem defeitos.

Tabela 8.3 — Inspecção computacional das malhas geradas para um perfil antropométrico de 8 anos

| Modelo e peça | Fecho | Múltiplos corpos | N.º de corpos | Faces nulas | Interpretação |
| --- | --- | --- | --- | --- | --- |
| Flexy Beast, palma | Sim | Sim | 1 | 0 | Malha fechada segundo os critérios usados |
| Flexy Beast, dedo médio | Sim | Sim | 3 | 0 | Três corpos fechados, coerentes com a construção segmentada |
| Paraglider Hand, palma | Sim | Sim | 1 | 142 | A preparação pode aceitar a peça, mas a malha contém faces degeneradas |
| Paraglider Hand, dedo médio | Não | Sim | 4 | 26 | Requer inspecção ou reparação antes de uma conclusão sobre qualidade geométrica |
| UnLimbited Phoenix, palma | Não | Não | 5 | 6 | A malha original contém descontinuidades que o redimensionamento não elimina |

Nos ficheiros de preparação configurados para a Bambu Lab A1, o diagnóstico do Bambu Studio regista zero arestas corrigidas e zero faces degeneradas nas peças importadas. Este indicador refere-se apenas aos ficheiros concretos examinados e resulta de um procedimento diferente do utilizado na inspecção computacional da Tabela 8.3. A diferença entre os registos deve ser mantida, pois nenhum dos resultados autoriza a concluir que todas as variantes de cada modelo possuem a mesma qualidade de malha.

O registo fotográfico complementa os dados de preparação e a inspecção das malhas. As fotografias documentam peças efectivamente produzidas, a organização dos componentes e estados preliminares de montagem. Não substituem medições dimensionais, ensaios mecânicos ou avaliação com utilizadores.

![](figuras/teste-impressao-painel-componentes.jpg)

Figura 8.1 — Componentes impressos e estados preliminares de montagem: segmentos digitais articulados, palma e elementos separados. O painel documenta a materialização das geometrias e a compatibilidade visual entre componentes, sem demonstrar desempenho estrutural ou adequação funcional.

Fonte: produção própria.

![](figuras/teste-impressao-painel-series-dimensionais.jpg)

Figura 8.2 — Séries físicas de segmentos identificados pelos perfis de ensaio de 8, 15, 28 e 70 anos. À esquerda apresenta-se a série Paraglider Hand; ao centro e à direita, duas vistas da série Flexy Beast. As diferenças visíveis documentam a variação dimensional produzida, mas não constituem medição do desvio entre a malha e a peça.

Fonte: produção própria.

![](figuras/teste-impressao-painel-phoenix-montada.jpg)

Figura 8.3 — UnLimbited Phoenix configurada para o perfil de ensaio de 15 anos, apresentada em sete vistas da montagem física. As imagens documentam a reunião dos componentes e a mobilidade manual observável das articulações, sem equivaler a um protocolo de funcionamento, preensão ou utilização protésica.

Fonte: produção própria.

A Figura 8.4 apresenta um precedente de avaliação funcional baseado em tarefas quotidianas. No presente trabalho, funciona como enquadramento de uma etapa futura posterior à verificação técnica e material (Romero et al., 2025).

![](projecto-completo_media/image20.png)

Figura 8.4 — Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior.

Reproduzido de Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475

### 8.2 Avaliação da coerência das sugestões de IA

O primeiro conjunto experimental incidiu sobre cinco perfis de ensaio, construídos a partir de idade, sexo, altura, peso, país, comprimento do braço e constituição física. Como estes perfis não incluíam medições diretas da mão, a avaliação verificou a conformidade das respostas com o esquema, os intervalos e as relações dimensionais internas definidas. O ensaio examina o fluxo perante informação incompleta; não permite concluir que as dimensões correspondam à mão de uma pessoa concreta ou que a plataforma seja fácil de usar por pessoas sem formação técnica.

Nas cinco execuções documentadas, a IA produziu JSON válido, utilizou parâmetros existentes, respeitou os intervalos definidos no modelo e manteve a ordenação prevista entre os comprimentos dos dedos. Como Brasil, Japão e Alemanha não estão representados na base local, a indicação desses países não permitiu estabelecer uma correspondência populacional direta. Nestes casos, a seleção do perfil de referência passou a depender dos restantes atributos disponíveis e dos critérios de prioridade definidos no sistema. Este limite impede interpretar a indicação do país como adaptação antropométrica à população nacional mencionada.

Tabela 8.4 — Descrições submetidas nos cenários de avaliação da IA

| Conjunto experimental | Tipo de perfil criado | Descrição submetida | Finalidade da verificação |

| --- | --- | --- | --- |

| Ensaio 1 — indicadores populacionais indiretos | Adulto masculino com dados demográficos e regionais | *man, 28 years old, 82 kg, 180 cm height, Brazil, arm length 70 cm* | Testar a inferência paramétrica sem medições diretas da mão |

| Ensaio 1 — indicadores populacionais indiretos | Criança do sexo feminino, com estrutura corporal pequena | *girl, 10 years old, 32 kg, 138 cm height, Japan, small frame* | Examinar a redução das dimensões e dos componentes mecânicos perante uma idade inferior |

| Ensaio 1 — indicadores populacionais indiretos | Mulher idosa com dados demográficos e regionais | *woman, 65 years old, 68 kg, 160 cm height, Nigeria, arm length 62 cm* | Comparar os parâmetros com os limites do modelo num perfil adulto feminino e sénior |

| Ensaio 1 — indicadores populacionais indiretos | Adulto masculino com indicação qualitativa de mãos largas | *man, 50 years old, 95 kg, 175 cm height, Germany, broad hands, arm length 66 cm* | Verificar a resposta do sistema a uma característica anatómica descrita qualitativamente |

| Ensaio 1 — indicadores populacionais indiretos | Adolescente masculino alto e magro | *teenage boy, 15 years old, 60 kg, 168 cm height, India, slim build, arm length 67 cm* | Testar a fronteira entre perfil pediátrico e dimensões próximas de adulto |

| Ensaio 2 — amputação unilateral | Perfil com medições completas da mão intacta | Medições completas da mão esquerda intacta: palma 84 mm; indicador 72 mm; médio 78 mm; anelar 75 mm; mínimo 58 mm; polegar 64 mm; prótese necessária para a mão direita | Confirmar a preservação dos valores fornecidos e a geração contralateral |

| Ensaio 2 — amputação unilateral | Perfil com dados demográficos e uma medição directa | Homem, 40 anos; mão direita intacta; largura da palma 90 mm; prótese necessária para a mão esquerda | Confirmar a manutenção da medida fornecida e a estimativa proporcional dos campos em falta |

| Ensaio 2 — amputação unilateral | Perfil apenas demográfico | Mulher, 30 anos, asiática oriental, 158 cm; prótese necessária para a mão direita | Verificar a adaptação do sistema quando não existem medições diretas da mão |

Fonte: elaboração própria a partir dos pedidos, metadados e cenários conservados na subpasta `avaliacao_ia_antropometrica/` do Suplemento 2 — Avaliação técnica da plataforma. A coluna apresenta a descrição do caso de ensaio enviada no pedido; o pedido completo incluía o esquema actual do modelo, os intervalos permitidos e a instrução de devolver apenas JSON válido.

A leitura dos registos mostra respostas distintas consoante o detalhe da descrição submetida. Nos perfis adultos, os valores sugeridos permaneceram nos intervalos usados pelo sistema. No perfil infantil, os comprimentos e os parâmetros das articulações flexíveis foram reduzidos. Este comportamento corresponde às instruções presentes nas legendas do esquema; não constitui demonstração de ajuste anatómico. No perfil adolescente, uma regra preliminar assinalou a palma como excessiva. A comparação posterior com o intervalo de referência usado no ensaio mostrou que o limite do teste era demasiado rígido. A regra foi corrigida, mas a ausência de uma medição individual impede classificar a sugestão como exata.

O segundo conjunto experimental avaliou três cenários de ausência unilateral com graus distintos de informação. Quando foram fornecidas medições completas da mão intacta, esses valores foram preservados na resposta registada. No caso parcial, a largura da palma declarada foi mantida e os restantes comprimentos foram preenchidos. Nos ensaios baseados em indicadores demográficos, a IA devolveu o conjunto de parâmetros requerido. Estes resultados caracterizam as respostas observadas, mas não permitem concluir sobre a correção anatómica dos valores estimados.

A lateralidade foi examinada num ensaio separado, composto por 12 pedidos repetidos. Destes, onze produziram respostas interpretáveis e um não gerou uma resposta analisável. Nos sete pedidos de mão esquerda com resposta válida, a lateralidade foi incorretamente devolvida como mão direita; nos quatro pedidos de mão direita, a indicação foi mantida corretamente. Perante este resultado, a lateralidade foi retirada do conjunto de parâmetros sugeridos pela IA e transferida para um controlo determinístico da interface. Após esta alteração, as nove execuções subsequentes omitiram o campo de lateralidade, incluindo um cenário em que a descrição textual entrava em conflito com a escolha efetuada na interface.

Tabela 8.5 — Síntese da avaliação das sugestões de IA

| Eixo avaliado | Resultado observado | Interpretação |

| --- | --- | --- |

| Conformidade com o esquema | Respostas interpretáveis, campos previstos e valores dentro dos limites definidos | O esquema de parâmetros reduziu a ocorrência de sugestões inválidas |

| Relações dimensionais internas | Dedo médio mais longo, dedo mínimo mais curto e polegar inferior ao dedo médio nos casos arquivados | As relações definidas no protocolo foram respeitadas; o resultado não equivale a adequação anatómica individual |

| Descrições com medições completas | Medições fornecidas mantidas sem alteração | A IA preservou os valores diretamente declarados. |

| Descrições com uma medição direta | Campos em falta estimados a partir da medida fornecida | A resposta registada combinou o dado explícito com referências populacionais. |

| Descrições apenas demográficas | Conjunto completo de parâmetros dentro dos intervalos | Nos casos examinados, o fluxo gerou um ponto de partida que requer confirmação por medição ou por um profissional competente |

| Lateralidade antes da correção | 0/7 respostas corretas para pedidos de mão esquerda; 4/4 para mão direita; uma falha de análise | A IA não oferecia comportamento aceitável neste parâmetro |

| Lateralidade após a correção | Campo omitido em 9/9 execuções | A escolha passou a ser determinística e independente da resposta da IA |

A série complementar de ensaios reuniu 15 cenários construídos a partir de descrições vagas, comparativas, em diferentes línguas, sem medidas ou com valores fora dos limites definidos. Os registos preservam as descrições submetidas e as respostas obtidas, mas o estudo não reuniu repetições suficientes para estimar estatisticamente a estabilidade do modelo de linguagem. Em algumas execuções, foram sugeridos parâmetros de *hardware*; noutras, esses parâmetros permaneceram nos valores já definidos. Assim, a conclusão limita-se à conformidade dos casos registados e à importância das salvaguardas determinísticas. Descrições equivalentes podem originar valores numéricos ou conjuntos de campos diferentes, pelo que cada sugestão exige revisão antes de ser aplicada.

### 8.3 Verificação geométrica entre modelos

A verificação geométrica testou se os valores sugeridos chegavam à malha exportada em três modelos activos da plataforma: Flexy Beast, Paraglider Hand e UnLimbited Phoenix. Para cada modelo foram comparados um valor de referência por omissão e três perfis de ensaio: criança, mulher adulta e homem adulto. As execuções documentadas devolveram valores dentro dos intervalos definidos. O ensaio incide sobre a resposta dimensional das geometrias, sem avaliar o ajuste ao corpo, o conforto, a função ou a segurança.

Tabela 8.6 — Modelos e mecanismos de escala avaliados

| Modelo | Entradas antropométricas principais | Mecanismo de escala | Implicação observada |

| --- | --- | --- | --- |

| Flexy Beast | Largura da palma e comprimentos dos cinco dedos | Escalas independentes para palma e dedos | Aceitou os valores inferiores usados no ensaio |

| Paraglider Hand | Palma e dedos, com parâmetros adicionais de contexto | Escala geral da palma e ajustes por dedo | Respondeu aos três perfis após a correção da escala da palma |

| UnLimbited Phoenix | Largura da palma | Escala uniforme limitada por valor mínimo | Impediu reduções abaixo do limite definido no modelo |

Nota: o factor de escala resulta da divisão entre a maior dimensão da palma exportada e a dimensão correspondente da configuração de referência. Um valor de 1,000 indica igualdade; valores inferiores indicam redução e valores superiores indicam aumento relativamente à referência.

Os resultados mostraram que o Flexy Beast e o Paraglider Hand apresentaram respostas semelhantes aos mesmos perfis, reduzindo ou aumentando a maior dimensão da palma. O perfil infantil produziu fatores de escala de 0,761 e 0,747 relativamente à configuração de referência; a mulher adulta ficou em 0,932 e 0,928; e o homem adulto em 1,148 e 1,157. No Phoenix, o limite mínimo impediu a redução abaixo de cerca de 82 mm de largura da palma e manteve os perfis pequenos no tamanho mínimo previsto pelo modelo.

Tabela 8.7 — Factor de escala da maior dimensão da palma exportada relativamente à configuração de referência

| Perfil | Flexy Beast | Paraglider Hand | UnLimbited Phoenix |

| --- | --- | --- | --- |

| Valor de referência | 1,000 | 1,000 | 1,000 |

| Criança | 0,761 | 0,747 | 1,000 após a correcção |

| Mulher adulta | 0,932 | 0,928 | 1,000 |

| Homem adulto | 1,148 | 1,157 | 1,171 |

Antes da correção, um percurso alternativo do Phoenix produziu um fator de escala de 0,760 no perfil infantil. Esse valor foi rejeitado porque ultrapassava o limite mínimo declarado para o modelo; por isso, não integra a Tabela 8.7 como resultado aceite.

Esta verificação revelou três fragilidades técnicas que não eram visíveis na análise numérica isolada. A primeira estava no mecanismo de correspondência populacional: a análise inicial de sexo e idade era demasiado frágil, e certas abreviaturas presentes no texto de entrada podiam ser interpretadas incorretamente, confundindo unidades de medida com indicação de sexo masculino.

A correção passou por uma análise mais robusta do texto de entrada, capaz de reconhecer termos em diferentes línguas, respeitar fronteiras de palavra e classificar de forma mais fiável os grupos etários.

A segunda fragilidade foi identificada no modelo Paraglider. Neste caso, a dimensão da palma da mão protésica não respondia corretamente aos valores sugeridos, porque permanecia associada a uma escala interna herdada da biblioteca original. A correção consistiu em aplicar novamente a escala no ponto do código responsável pela geração dessa geometria. A terceira fragilidade surgiu no modelo UnLimbited Phoenix, onde um parâmetro alternativo permitia ultrapassar o limite mínimo de escala definido para o modelo. A correção passou por aplicar esse mesmo limite também a esse percurso alternativo de geração.

Esta etapa mostra que a avaliação das sugestões deve continuar para além da resposta em JSON. A malha exportada e a preparação para impressão podem revelar dependências internas, limites de escala, problemas de espessura, folgas insuficientes e heranças de código ausentes da análise numérica. Os modelos integrados apresentam respostas distintas aos mesmos perfis: o Flexy Beast aceitou a redução usada no ensaio, o Paraglider passou a propagar a escala para a palma após a correção e o Phoenix manteve o limite dimensional da biblioteca original. A seleção de um modelo para uma pessoa concreta exige critérios e dados que este ensaio não avaliou.

### 8.4 Discussão dos resultados face aos objetivos

Face aos objetivos, os resultados sustentam a integração técnica do *design* paramétrico, dos dados antropométricos, da interface *web* e da IA num protótipo de investigação. A informação textual pode originar um conjunto inicial de parâmetros editáveis e visualizáveis, desde que os valores sejam limitados pelo esquema, confirmados na geometria e revistos por uma pessoa competente. O estudo não mediu se este fluxo reduz esforço, tempo, custo ou dependência de especialistas.

A avaliação delimita o papel da IA. Uma resposta isolada não constitui prescrição; não existe uma medição clínica individual que permita calcular erro anatómico; e a lateralidade mostrou que parâmetros críticos devem permanecer sob regras determinísticas. A verificação geométrica identificou limites próprios de cada modelo. As peças físicas confirmaram que as configurações selecionadas podiam ser preparadas e produzidas nas condições registadas, e a medição das palmas quantificou a diferença dimensional face às malhas. Estes resultados não sustentam conclusões sobre ajuste, montagem completa, resistência, conforto ou uso continuado.

A literatura sobre próteses de membro superior agrupa as razões de abandono principalmente em problemas de conforto e de função, incluindo o peso, a temperatura e a transpiração (Smail et al., 2021). Biddiss et al. (2007) identificam o peso, o conforto e o controlo como prioridades expressas pelos utilizadores, enquanto Fink e Diamond (2023) destacam o ajuste do encaixe, o controlo, o peso, a facilidade de reparação e a estética entre os aspectos a considerar na escolha e no acompanhamento da prótese. Nesta investigação, estas preocupações foram traduzidas em requisitos de referência para o processo de *design*. A configuração dimensional, a visualização, a escolha formal e cromática, a edição dos parâmetros e a possibilidade de aceitar, alterar ou rejeitar sugestões de IA constituem respostas concretas a esses requisitos. Os ensaios confirmaram a presença e o funcionamento técnico destes mecanismos, mas não mediram os seus efeitos no conforto percebido, na aceitação ou na utilização continuada.

Esta distinção permite interpretar os resultados em três níveis. Foi demonstrada tecnicamente a capacidade de configurar dimensões, controlar parâmetros, gerar e exportar geometrias e preparar variantes para fabrico. A materialização das peças foi observada e as dimensões X, Y e Z das palmas foram comparadas com as malhas. Como existe uma leitura por eixo e peça, a interpretação dimensional permanece descritiva e não inclui estimativa da incerteza; montagem e articulação também ficaram fora do âmbito avaliado. Conforto, usabilidade com participantes, adequação funcional em utilização, aceitação, dignidade e autonomia constituem efeitos potencialmente decorrentes das decisões de projeto, sustentados como relevantes pela literatura, mas ainda não confirmados junto de utilizadores.

O resultado metodológico central é a sequência de controlo formada pelo esquema de parâmetros, limites, filtragem de campos, referência populacional, execução em OpenSCAD/*WebAssembly*, exportação, preparação e impressão. As correções de correspondência populacional, escala e lateralidade mostram que o conhecimento sobre o projecto surgiu da construção, do ensaio e da reformulação do artefacto, em coerência com *Research Through Design*. Esta sequência permite localizar falhas técnicas e explicitar onde termina a evidência produzida.

A comparação com as lacunas sintetizadas na Tabela 2.3 delimita a interpretação do funcionamento do protótipo, evitando que este seja entendido como resposta indistinta a problemas de natureza clínica, experiencial e socioeconómica. A Tabela 8.8 retoma o mesmo quadro e confronta cada requisito selecionado com os resultados observados.

Tabela 8.8 — Discussão dos resultados face às lacunas seleccionadas do estado da arte

| Lacuna e requisito selecionado | Evidência obtida | Interpretação face ao estado da arte | Aspetos não avaliados |
| --- | --- | --- | --- |
| Validação empírica: tornar verificável a cadeia técnica | Casos funcionais da plataforma, cenários simulados, exportações, medições digitais e físicas, preparação para impressão e registo fotográfico | O estudo acrescenta uma relação documentada entre entrada, decisão e artefacto, mas permanece no nível de prova de conceito técnica identificado como frequente na literatura (Chadwell et al., 2020; Samuelsson et al., 2012; Windrich et al., 2016) | Não demonstra eficácia, segurança, utilização quotidiana ou evolução longitudinal |
| Necessidades e métricas: separar mecanismos de efeitos humanos | As matrizes metodológicas e a discussão distinguem funcionamento técnico, comparação dimensional das palmas e efeitos humanos não medidos | A separação evita usar indicadores internos como substitutos de conforto, satisfação ou qualidade de vida, respondendo ao desalinhamento discutido em revisões sobre próteses dos membros superior e inferior (Cordella et al., 2016; Manz et al., 2022) | Não estabelece relações empíricas entre medidas objetivas, experiência e qualidade de vida |
| Interface corpo–prótese: relacionar dados, parâmetros e geometria | As configurações propagaram dimensões de modo específico por modelo e revelaram limites no Paraglider e no Phoenix | O protótipo explicita parte da tradução dimensional que antecede o ajuste, mas não resolve os problemas de encaixe e conforto salientados por Alluhydan et al. (2023), Baldock et al. (2023) e Richardson e Dillon (2017) | Sem medição do membro residual, contacto, pressão, conforto ou adequação anatómica individual. |
| Controlo e interação: preservar decisão humana na configuração | A lateralidade passou para controlo determinístico; sugestões inválidas puderam ser rejeitadas ou recuperadas; a exportação permaneceu uma decisão humana | O resultado delimita a interacção com o configurador, sem constituir avanço nas estratégias de controlo da prótese discutidas por Domínguez-Ruiz et al. (2023) e Marinelli et al. (2022) | Não avalia aprendizagem, esforço cognitivo, controlo em uso ou desempenho funcional |
| Acesso e manutenção: explorar uma arquitetura *web* e aberta | A plataforma executou a geração no navegador, conservou configurações e preparou ficheiros em ambientes de fabrico registados | A arquitetura reduz algumas dependências de *software* no percurso examinado, mas não demonstra redução de custos ou melhoria de acesso nos contextos descritos por Andrysek (2010), Baumann e Maria (2023) e Segura et al. (2024) | Não foram avaliados custos totais, conectividade, competências, reparação, manutenção ou implantação |
| Participação e registo: documentar decisões e iterações | O estudo conserva versões, protocolos, falhas, correções, inventários e anexos ligados aos ciclos de *Research Through Design* | A documentação do percurso reforça o registo metodológico, mas não responde à insuficiência de participação e de métodos qualitativos identificada por Hafner e Sawers (2016), Richardson e Dillon (2017) e Walker et al. (2019) | Não houve *co-design*, teste de usabilidade, entrevistas ou observação com participantes |

## Capítulo 9 — Conclusões e Trabalhos Futuros

### 9.1 Resposta ao problema e às perguntas de investigação

A investigação desenvolveu um protótipo de plataforma para configurar modelos de prótese de membro superior com base em parâmetros, referências antropométricas, sugestões de IA, execução de OpenSCAD no navegador e exportação para fabrico aditivo. A avaliação sustenta o funcionamento técnico deste fluxo nas condições registadas.

Relativamente à primeira pergunta de investigação, conclui-se que o *design* paramétrico e a IA apoiaram parcialmente a personalização, desempenhando funções distintas no processo de configuração. O esquema paramétrico definiu nomes, tipos, intervalos e valores correntes; a IA propôs conjuntos iniciais de parâmetros; as regras determinísticas controlaram a lateralidade e a geração geométrica; e a decisão final permaneceu sob responsabilidade humana. A alteração controlada das dimensões, a visualização do modelo e a possibilidade de rever as sugestões constituíram mecanismos orientados para o ajuste, para a acessibilidade do processo e para o controlo das decisões de projeto.

Relativamente à segunda pergunta de investigação, conclui-se que a combinação de ciclos de *Research Through Design*, ensaios unitários, cenários simulados, inspeção de respostas JSON, medição de malhas, exportação, preparação para impressão 3D, observação e medição de peças físicas permitiu avaliar parcialmente a coerência e a consistência técnica de diferentes etapas do processo. A Série de ensaios B acrescentou uma comparação digital em condição comum; a análise dimensional reuniu 36 extensões X/Y/Z das malhas e 72 medições das palmas impressas em PLA e PETG. Estes métodos, contudo, não avaliaram a eficácia protésica, a usabilidade com participantes ou a durabilidade. A comparação dimensional permanece descritiva e não estima a incerteza de medição.

Relativamente à terceira pergunta de investigação, conclui-se que o *design* industrial conciliou parcialmente os requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos através da organização dos parâmetros, da definição de permissões, da apresentação da geometria, das opções formais e cromáticas e da sequência entre configuração, visualização, exportação e preparação para fabrico. A manutenção do controlo humano e a possibilidade de aceitar, alterar ou rejeitar sugestões constituíram decisões orientadas para a participação, a autonomia e a dignidade do utilizador. Contudo, a aceitação da solução, a experiência de dignidade e o impacto na autonomia quotidiana não foram observados junto de utilizadores.

Tabela 9.1 — Estado da resposta às perguntas de investigação aprovadas

| Pergunta | Parcialmente respondida | Não avaliada empiricamente | Remetida para investigação futura |
| --- | --- | --- | --- |
| Personalização, conforto, adequação funcional, acessibilidade e controlo | Configuração dimensional, visualização, supervisão humana e preparação de variantes | Conforto percebido, ajuste individual, adequação funcional em uso e facilidade de utilização por participantes | Ajuste a utilizadores específicos, tarefas funcionais e estudo de utilização |
| Eficácia, usabilidade, durabilidade e possibilidade de reproduzir os resultados | Coerência do percurso, repetição técnica, preparação digital e comparação dimensional descritiva entre malhas e palmas em PLA e PETG | Eficácia protésica, usabilidade com participantes, resistência, desgaste, durabilidade e incerteza de medição | Montagem, ensaios mecânicos delimitados e avaliação com participantes |
| Requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos | Organização paramétrica, controlo humano, visualização e opções formais e cromáticas | Aceitação, experiência de dignidade e impacto na autonomia quotidiana | Investigação participativa e avaliação situada com os grupos previstos |

A hipótese principal recebeu apoio parcial ao nível dos mecanismos de projeto: a integração produziu um fluxo capaz de configurar, gerar, exportar e preparar variantes dos modelos estudados. Os dados não permitem concluir que essas variantes sejam mais adequadas anatómica ou funcionalmente, nem que o processo seja efetivamente mais acessível ou escalável em contextos economicamente desfavorecidos. Quanto às hipóteses secundárias, os princípios de *design* inclusivo e DfAM estão presentes nas decisões de interface, parametrização e fabrico, mas não foi realizado um processo participativo. As hipóteses aprovadas permanecem, portanto, parcialmente examinadas e não são apresentadas como integralmente confirmadas ou rejeitadas.

### 9.2 Contributos da investigação

O contributo no domínio do projeto é o protótipo integrado e a definição do seu fluxo: seleção do modelo, introdução ou sugestão de parâmetros, visualização, exportação e preparação para fabrico. A separação entre parâmetros antropométricos, parâmetros geométricos, escolhas de apresentação e lateralidade torna explícita a distribuição das decisões.

O contributo técnico é a integração de modelos OpenSCAD com uma configuração comum, execução no navegador, exportação STL/3MF, base antropométrica local e apoio de IA limitado pelo esquema ativo. As correções do mecanismo de correspondência, da escala da palma no Paraglider, do limite mínimo no Phoenix e da lateralidade mostram problemas concretos e as respetivas soluções.

O contributo metodológico é a documentação dos ciclos de *Research Through Design* que ligam situação, artefacto, ensaio, resultado e alteração. A passagem sucessiva pela resposta numérica, geometria exportada, projeto de preparação para impressão e peça física revelou falhas que ficariam ocultas num único nível de análise.

O contributo para o conhecimento em *design* industrial reside em duas conclusões delimitadas. Primeiro, a personalização paramétrica depende da correspondência explícita entre fonte antropométrica, nome do parâmetro, regra geométrica e resultado material. Segundo, a IA tem utilidade como apoio à configuração inicial quando as decisões críticas são protegidas por regras, limites e supervisão humana. Estas conclusões resultam do protótipo e dos casos estudados; a sua transferência para outros modelos ou regiões corporais requer nova implementação e nova avaliação.

### 9.3 Limitações

Os casos de teste são simulados e não incluem participantes, medições clínicas ou dados individuais de uma pessoa amputada. Por esse motivo, os valores sugeridos foram comparados com esquemas e referências populacionais, sem cálculo de erro face a um membro superior específico. A base antropométrica combina populações, idades, sexos, lados medidos e protocolos diferentes; alguns países mencionados nos cenários não estão nela representados.

Os registos da IA correspondem a conjuntos finitos de execuções e a estados específicos do código. Não foi realizado um estudo estatístico com amostras extensas por cenário. O estado final da plataforma foi inspecionado e os dez ensaios unitários disponíveis foram concluídos.

A avaliação de fabrico combina quatro projectos de preparação digital para impressão 3D com configuração analisada, doze casos sob condição digital comum, inspecção das malhas, 72 medições dimensionais e registo fotográfico das peças existentes. O consumo de filamento e a massa são estimativas dos programas, não medições reais. Os valores dimensionais foram registados uma única vez por eixo e peça, pelo que não permitem calcular dispersão entre leituras nem incerteza de medição. Também não foram realizados ensaios de carga, desgaste, conforto, segurança, montagem funcional completa ou utilização prolongada.

O estudo examinou em profundidade três modelos activos. O Cyborg Beast está registado na plataforma, mas não integra a comparação geométrica principal. Os resultados relativos ao Flexy Beast, Paraglider Hand e UnLimbited Phoenix dependem das respectivas bibliotecas, intervalos e mecanismos de escala.

### 9.4 Trabalho futuro

A comparação dimensional já realizada poderá ser aprofundada em trabalho futuro. Os valores introduzidos no sistema, as extensões X/Y/Z das malhas e um valor físico por eixo para as palmas em PLA e PETG encontram-se registados no Anexo D. Caso se pretenda calcular média, amplitude e incerteza associada à repetição da medição com o paquímetro, deverão ser efectuadas três leituras independentes por eixo. Esta extensão não é necessária para a comparação descritiva nem para as conclusões apresentadas nesta dissertação. As medições físicas incidiram sobre extremos geométricos das peças, não devendo esses pontos ser interpretados como pontos anatómicos sem demonstração da sua equivalência com referências corporais.

Uma extensão futura orientada para a consistência das respostas do modelo de linguagem poderá executar cada cenário várias vezes, registando o modelo utilizado, as condições de geração, a resposta completa, os erros, os campos omitidos e a taxa de cumprimento de cada regra. Esta análise permitiria caracterizar a dispersão entre execuções, mas não é necessária para as conclusões delimitadas apresentadas nesta dissertação. Independentemente dessa série de ensaios, a interface deverá apresentar a referência populacional utilizada, os dados em falta e avisos sempre que uma dimensão estimada fique fora do intervalo admissível do modelo escolhido. A validação do esquema JSON deverá ocorrer no servidor, antes de a sugestão ser disponibilizada na interface.

Uma segunda linha de trabalho futuro deve executar separadamente os protocolos de montagem e os ensaios mecânicos. A folha do Anexo D permite começar pela compatibilidade dos componentes, colisões e cinco ciclos de articulação nos protótipos completos. Comparações de materiais e impressoras exigem corpos de prova ou componentes equivalentes, condições controladas e medições próprias; carga, fadiga e desgaste requerem procedimentos adequados ao uso previsto. No Flexy Beast, esta etapa deve incluir a produção e caracterização das juntas em filamento flexível ou silicone, bem como a verificação do retorno dos dedos e da aderência das almofadas previstas no modelo original. Só depois desta caracterização deve avançar uma avaliação com participantes e profissionais, mediante enquadramento ético e clínico apropriado.

Uma terceira linha de trabalho futuro deve estudar a interface com os grupos de utilizadores previstos. As tarefas, erros, tempo, compreensão das sugestões, confiança e distribuição de responsabilidade devem ser avaliados com pessoas amputadas, designers, técnicos e profissionais de saúde. Esta etapa permitirá verificar se o fluxo facilita a configuração e se os avisos e controlos apoiam decisões informadas.

Por fim, a integração de novas regiões corporais deve começar pela definição de requisitos, dados, parâmetros e limites específicos. A arquitectura de configuração oferece uma base possível, mas ainda não demonstra que o sistema funcione para dispositivos destinados ao pé, à perna ou ao braço.

## Bibliografia

<a id="ref-akasaka-2022"></a> Akasaka, F., Mitake, Y., Watanabe, K., & Shimomura, Y. (2022). A framework for ‘configuring participation’ in living labs. Design Science, 8, e28. https://doi.org/10.1017/dsj.2022.22

<a id="ref-akyol-2021"></a> Akyol, E., Cabral Ramos Mota, R. C., & Somanath, S. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (Article 437, pp. 1-6). ACM. https://doi.org/10.1145/3411763.3451716

<a id="ref-albin-2023"></a> Albin, T., & Molenbroek, J. F. M. (2023). Introduction to the special issue, anthropometry in design. https://repository.tudelft.nl/file/Fileda5bfdc9-98bc-41d3-a402-553d5f0d0a63

<a id="ref-alili-2023"></a> Alili, A., Nalam, V., Li, M., Liu, M., Feng, J., Si, J., & Huang, H. (2023). A novel framework to facilitate user preferred tuning for a robotic knee prosthesis. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31, 895-903. https://doi.org/10.1109/TNSRE.2023.3236217

<a id="ref-alluhydan-2023"></a> Alluhydan, A., Alsaadi, S., Almutairi, A., & Alharbi, A. (2023). Functionality and comfort design of lower-limb prosthetics: A review.

<a id="ref-anacleto-filho-2023"></a> Anacleto Filho, P. C., da Silva, L., Mattos, D., Pombeiro, A., Castellucci, H. I., Colim, A., Carneiro, P., & Arezes, P. (2023). Establishing an anthropometric database: A case for the Portuguese working population. International Journal of Industrial Ergonomics, 97, 103473. https://doi.org/10.1016/j.ergon.2023.103473

<a id="ref-anderson-2024"></a> Anderson, C. B., Stephens, A. R., Scully, A., Pasquina, P. F., & Highsmith, M. J. (2024). A narrative review of prosthesis design decision making after lower-limb amputation for developing shared decision-making resources.

<a id="ref-andrysek-2010"></a> Andrysek, J. (2010). Lower-limb prosthetic technologies in the developing world: A review of literature from 1994-2010.

<a id="ref-ao-2025"></a> Ao, Y., Li, S., & Duan, H. (2025). Artificial intelligence-aided design (AIAD) for structures and engineering: A state-of-the-art review and future perspectives. Archives of Computational Methods in Engineering. https://link.springer.com/content/pdf/10.1007/s11831-025-10264-1.pdf

<a id="ref-astm-international-2024"></a> ASTM International. (2024). Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers. https://www.astm.org/f3661-24.html

<a id="ref-atallah-2025"></a> Atallah, H., Qufabz, T., Naeem, R., Bakhsh, H. R., Ferriero, G., Varga, D., Derkács, E., & Molics, B. (2025). The current state of 3D-printed prostheses clinical outcomes: A systematic review. Journal of Functional Biomaterials, 16(10), 370. https://doi.org/10.3390/jfb16100370

<a id="ref-bai-2024"></a> Bai, X., Yuan, J., Liu, M., Huang, H., & Feng, J. (2024). Human factors considerations of interaction between wearers and intelligent lower-limb prostheses: A prospective discussion. Journal of NeuroEngineering and Rehabilitation, 21, 187. https://doi.org/10.1186/s12984-024-01475-x

<a id="ref-baldock-2023"></a> Baldock, C., Greaves, M., Chockalingam, N., & Kark, L. (2023). Adjustable prosthetic sockets: A systematic review of industrial and research design characteristics and their justifications.

<a id="ref-baron-2020"></a> Baron, A., Gatzweiler, C., Geislinger, A., Huber, C., & Aszmann, O. C. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 274-287. https://doi.org/10.3390/prosthesis2040021

<a id="ref-arrieta-2020"></a> Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82-115. https://doi.org/10.1016/j.inffus.2019.12.012

<a id="ref-base-local-antropometrica-2026"></a> Base local consolidada de dados antropométricos da mão e do membro superior distal. (2026). [Conjunto de dados]. Suplemento 1 — Dados antropométricos.

<a id="ref-bates-2020"></a> Bates, T. J., Fergason, J. R., & Pierrie, S. N. (2020). Technological advances in prosthesis design and rehabilitation following upper extremity limb loss. Current Reviews in Musculoskeletal Medicine, 13(4), 485-493. https://doi.org/10.1007/s12178-020-09656-6

<a id="ref-baumann-2023"></a> Baumann, C., & Maria, P. (2023). Improving access to prosthetic limbs in Germany: An explorative review.

<a id="ref-biddiss-2007"></a> Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive Technology, 2(6), 346-357. https://doi.org/10.1080/17483100701714733

<a id="ref-brack-2021"></a> Brack, R., & Amalu, E. H. (2021). A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. Journal of Orthopaedics, 23, 88-96. https://doi.org/10.1016/j.jor.2020.12.009

<a id="ref-paul-2022"></a> Paul, G., Steffan, I. T., Itoh, N., Bowman, R., & Bradtmiller, B. (2022). Design for all—Design for disabled: How important is anthropometry? Work, 73, S57-S65. https://doi.org/10.3233/WOR-211106

<a id="ref-brooks-2026"></a> Brooks, C. (2026). OpenSCAD Web [Computer software]. GitHub. https://github.com/CameronBrooks11/openscad-web

<a id="ref-burnap-2019"></a> Burnap, A., Hauser, J. R., & Timoshenko, A. (2019). Design and evaluation of product aesthetics: A human-machine hybrid approach. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3421771

<a id="ref-bustamante-2018"></a> Bustamante, M., Vega-Centeno, R., Sanchez, M., & Mio, R. (2018). A parametric 3D-printed body-powered hand prosthesis based on the four-bar linkage mechanism. In International Conferences on Biological Information and Biomedical Engineering.

<a id="ref-cabibihan-2021"></a> Cabibihan, J.-J., Abubasha, M. K., & Thakor, N. V. (2021). Suitability of the openly accessible 3D printed prosthetic hands for war-wounded children. Frontiers in Robotics and AI, 7, 594196. https://doi.org/10.3389/frobt.2020.594196

<a id="ref-cabibihan-2018"></a> Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2831907

<a id="ref-chadwell-2020"></a> Chadwell, A., Kenney, L., Thies, S., Galpin, A., & Head, J. (2020). Technology for monitoring everyday prosthesis use: A systematic review.

<a id="ref-chainando-2025"></a> Chainando, N., Martawidjaja, M., Darius, R. A., Yahya, L. C., Yemima, S., Tan, W. S., Harito, C., Chandra, R. C., Andhini, G. K., Putra, K. B., Lumban Tobing, C. C., Syafi’i, M., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. *Prosthesis, 7*(2), Article 26. https://doi.org/10.3390/prosthesis7020026

<a id="ref-chapman-2025"></a> Chapman, K., Allen, C., & Kendall, E. (2025). Methods for co-designing health communication initiatives with people with disability: A scoping review. Health Communication. https://doi.org/10.1080/10810730.2025.2462679

<a id="ref-chatzioglou-2024"></a> Chatzioglou, G. N., Pinar, Y., & Govsa, F. (2024). Biometric analysis hand parameters in young adults for prosthetic hand and ergonomic product applications. Anatomy & Cell Biology, 57, 172-182. https://doi.org/10.5115/acb.23.310

<a id="ref-choudhury-2025"></a> Choudhury, M. M., Eisenbart, B., & Kuys, B. (2025). Artificial intelligence (AI) in the design process: A review and analysis on generative AI perspectives. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/36E8736EEB55F0B38C2C9AB47EF381FE/S2732527X25100771a.pdf/div-class-title-artificial-intelligence-ai-in-the-design-process-a-review-and-analysis-on-generative-ai-perspectives-div.pdf

<a id="ref-chtioui-2023"></a> Chtioui, N., Gaha, R., & Benamara, A. (2023). Design for additive manufacturing: Review and framework proposal. https://sei.ardascience.com/index.php/journal/article/download/185/169

<a id="ref-clarkson-2010"></a> Clarkson, J., & Coleman, R. (2010). Inclusive design. Design Studies. https://doi.org/10.1080/09544821003693689

<a id="ref-cole-2011"></a> Cole, E. (2011). Patient-centered design: Interface personalization for individuals with brain injury.

<a id="ref-colombo-2015"></a> Colombo, G., Facoetti, G., Rizzi, C., & Vitali, A. (2015). Low cost hand-tracking devices to design customized medical devices. Interacción. https://doi.org/10.1007/978-3-319-21067-436

<a id="ref-cordella-2016"></a> Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users.

<a id="ref-costabile-2007"></a> Costabile, M. F., Fogli, D., Lanzilotti, R., Marcante, A., Mussio, P., Provenza, L. P., & Piccinno, A. (2007). Meta-design to face co-evolution and communication gaps between users and designers.

<a id="ref-cross-1982"></a> Cross, N. (1982). Designerly ways of knowing. Design Studies, 3(4), 221-227. https://doi.org/10.1016/0142-694X(82)90040-0

<a id="ref-cklacandr-2022"></a> Çıklaçandır, S., Yılmaz, M., Özmert, O. S., Şahin, A. M., & Mihçin, S. (2022). Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design. In 2022 Medical Technologies Congress (TIPTEKNO) (pp. 1-4). IEEE. https://doi.org/10.1109/TIPTEKNO56568.2022.9960218

<a id="ref-da-silveira-romero-2025"></a> da Silveira Romero, R. C., Costa, K. A., Reis, P. H. R. G., & Vimieiro, C. B. S. (2025). Development of parametric prostheses for different levels of human hand amputations manufactured through additive manufacturing. Applied Sciences, 15, 4467. https://doi.org/10.3390/app15084467

<a id="ref-daprice-flexy-beast"></a> daprice. (n.d.). Flexy Beast [README file]. GitHub. Retrieved July 13, 2026, from https://github.com/daprice/Flexy-Beast/blob/master/README.md

<a id="ref-dechev-2023"></a> Dechev, N., Penner, A., Barlow, I., Vukovic, G., & Lalji, M. (2023). Accessible prosthetic arms: Victoria Hand Project and the impact of 3D printing.

<a id="ref-design-council-2020"></a> Design Council. (2020). Framework for innovation. https://www.designcouncil.org.uk/our-resources/framework-for-innovation/

<a id="ref-dexter-2013"></a> Dexter, M., Crooks, E., Davies, P., & Simm, W. (2013). Open design and cystic fibrosis: Enabling participation in the design process.

<a id="ref-diment-2018"></a> Diment, L. E., Thompson, M. S., & Bergmann, J. H. M. (2018). Three-dimensional printed upper-limb prostheses lack randomised controlled trials: A systematic review. Prosthetics and Orthotics International, 42(1), 7-13. https://doi.org/10.1177/0309364617704803

<a id="ref-dominguez-ruiz-2023"></a> Domínguez-Ruiz, M., Ráez-Ballesteros, E., & Castillo-Castañeda, E. (2023). Low limb prostheses and complex human prosthetic interaction: A systematic literature review.

<a id="ref-elbreki-2022"></a> Elbreki, A. M., Alshari, K., Ramdan, S., & Rajab, Z. (2022). Practical design of an upper prosthetic limb using three dimensional printer with an artificial intelligence based controller. In 2022 International Conference on Engineering & MIS (ICEMIS). IEEE. https://doi.org/10.1109/ICEMIS56295.2022.9914291

<a id="ref-elhadad-2026"></a> ELhadad, N., Aboulhassan, A., & Hassan, Y. M. I. (2026). LLM-based 3D model generation of MHE for OpenSCAD. Procedia Computer Science.

<a id="ref-engdahl-2024"></a> Engdahl, S., Gonzalez, M. A., Lee, C., & Gates, D. H. (2024). Perspectives on the comparative benefits of body-powered and myoelectric upper limb prostheses. https://jneuroengrehab.biomedcentral.com/counter/pdf/10.1186/s12984-024-01436-4

<a id="ref-figoli-2022"></a> Figoli, F. A., Mattioli, F., & Rampino, L. (2022). AI in design idea development: A workshop on creativity and human-AI collaboration. https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=2915&context=drs-conference-papers

<a id="ref-fink-2023"></a> Fink, C., & Diamond, Y. (2023). Prosthesis options and management in upper extremity amputation. Operative Techniques in Orthopaedics, 33(3), 101061. https://doi.org/10.1016/j.oto.2023.101061

<a id="ref-fischer-2017"></a> Fischer, G., Fogli, D., & Piccinno, A. (2017). Revisiting and broadening the meta-design framework for end-user development.

<a id="ref-fischer-2004"></a> Fischer, G., Giaccardi, E., Ye, Y., Sutcliffe, A. G., & Mehandjiev, N. (2004). Meta-design.

<a id="ref-fisher-2020"></a> Fisher, M., & Johansen, E. (2020). Human-centered design for medical devices and diagnostics in global health. Global Health Innovation, 3(1), 1-15. https://doi.org/10.15641/ghi.v3i1.762

<a id="ref-frangos-2016"></a> Frangos, P., Mierdel, S., & Koirala, S. (2016). Democratising design in scientific innovation: Application of an open value network to open source hardware design.

<a id="ref-franke-2003"></a> Franke, N., & von Hippel, E. (2003). Satisfying heterogeneous user needs via innovation toolkits: The case of Apache security software. *Research Policy, 32*(7), 1199–1215. https://doi.org/10.1016/S0048-7333(03)00049-0

<a id="ref-frayling-1994"></a> Frayling, C. (1994). Research in art and design (Royal College of Art Research Papers, Vol. 1, No. 1, 1993/4). Royal College of Art.

<a id="ref-ghali-2008"></a> Ghali, S. (2008). Constructive solid geometry. In Introduction to geometric computing.

<a id="ref-ghillebert-2019"></a> Ghillebert, J., Schoukens, J., & Vanderborght, B. (2019). Guidelines and recommendations to investigate the efficacy of a lower-limb prosthetic device: A systematic review.

<a id="ref-gonzalez-avila-2024"></a> Gonzalez Avila, J. F., Pietrzak, T., Girouard, A., & Casiez, G. (2024). Understanding the challenges of OpenSCAD users for 3D printing. In Proceedings of the CHI Conference on Human Factors in Computing Systems. ACM. https://arxiv.org/abs/2408.01796

<a id="ref-gordon-2015"></a> Gordon, C. C., Blackwell, C. L., Bradtmiller, B., Parham, J. L., Barrientos, P., Paquette, S. P., Corner, B. D., Carson, J. M., Venezia, J. C., Rockwell, B. M., Mucher, M., & Kristensen, S. (2015). 2012 anthropometric survey of U.S. Army personnel: Methods and summary statistics (Report No. NATICK/TR-15/007). U.S. Army Natick Soldier Research, Development and Engineering Center.

<a id="ref-gordon-1989"></a> Gordon, C. C., Churchill, T., Clauser, C. E., Bradtmiller, B., McConville, J. T., Tebbetts, I., & Walker, R. A. (1989). Anthropometric survey of U.S. Army personnel: Methods and summary statistics 1988 (Technical Report NATICK/TR-89/044). U.S. Army Natick Research, Development and Engineering Center.

<a id="ref-gorski-2022"></a> Górski, F., Zawadzki, P., Wichniarek, R., Kuczko, W., Słupińska, S., & Żukowska, M. (2022). Automated design and rapid manufacturing of low-cost customized upper limb prostheses. Journal of Physics: Conference Series, 2198, 012040. https://doi.org/10.1088/1742-6596/2198/1/012040

<a id="ref-govender-2020"></a> Govender, R., Abrahmsén-Alami, S., Larsson, A., Borde, A., Liljeblad, A., & Folestad, S. (2020). Independent tailoring of dose and drug release via a modularized product design concept for mass customization. Pharmaceutics.

<a id="ref-gu-2024"></a> Gu, Y., He, L., Zeng, H., Li, J., Zhang, N., Zhang, X., & Liu, T. (2024). A data-driven design framework for structural optimization to enhance wearing adaptability of prosthetic hands. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 32. https://doi.org/10.1109/TNSRE.2024.3430070

<a id="ref-guo-2025"></a> Guo, M. (2025). Human-centered design strategies for prosthetics based on user needs. Interdisciplinary Humanities and Communication Studies, 1(1), 39-48.

<a id="ref-hafner-2016"></a> Hafner, B. J., & Sawers, A. B. (2016). Issues affecting the level of prosthetics research evidence: Secondary analysis of a systematic review.

<a id="ref-henao-2025"></a> Henao, J. C., Phillips, S. T., Brooks, T. L., Pienta, K. J., Brantley, J. S., & Carey, S. L. (2025). Upper-limb prosthetic requirements from the healthcare providers, end-users and relatives' perspectives. Journal of Hand Therapy. Advance online publication. https://doi.org/10.1016/j.jht.2025.01.004

<a id="ref-herbst-2021"></a> Herbst, Y., Georgopoulou, A., Dettwyler, M., Fernandez, A., Bacher, M., & Paik, J. (2021). Scan-driven fully-automated pipeline for a personalized, 3D printed low-cost prosthetic hand. In 2021 IEEE 17th International Conference on Automation Science and Engineering (CASE) (pp. 1188-1194). IEEE. https://doi.org/10.1109/CASE49439.2021.9551649

<a id="ref-herneth-2024"></a> Herneth, T., Hiesl, A., Stief, F., & Farago, D. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1-8). IEEE. https://doi.org/10.1109/IROS58592.2024.10801868

<a id="ref-hippel-2002"></a> von Hippel, E., & Katz, R. (2002). Shifting innovation to users via toolkits. *Management Science, 48*(7), 821–833. https://doi.org/10.1287/mnsc.48.7.821.2817

<a id="ref-hofmann-2016"></a> Hofmann, M. H., Griffiths, D., & Margetts, E. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858346

<a id="ref-howard-2022"></a> Howard, D., Davies, L., Dwyer, A., & Williams, J. (2022). Assessing the use of co-design to produce bespoke assistive technology solutions within a current healthcare service: A service evaluation.

<a id="ref-hsueh-2021"></a> Hsueh, M.-H., Lai, C.-J., Wang, S.-H., Zeng, Y.-S., Hsieh, C.-H., Pan, C.-Y., & Huang, W.-C. (2021). Effect of printing parameters on the thermal and mechanical properties of 3D-printed PLA and PETG, using fused deposition modeling. *Polymers, 13*(11), 1758. https://doi.org/10.3390/polym13111758

<a id="ref-hu-2007"></a> Hu, H., Li, Z., Yan, J., Wang, X., Xiao, H., Duan, J., & Zheng, L. (2007). Anthropometric measurement of the Chinese elderly living in the Beijing area. International Journal of Industrial Ergonomics, 37(4), 303-311. https://doi.org/10.1016/j.ergon.2006.11.006

<a id="ref-hussaini-2023"></a> Hussaini, A., Kyberd, P., Mulindwa, B., Ssekitoleko, R., Keeble, W., Kenney, L., & Howard, D. (2023). 3D printing in LMICs: Functional design for upper limb prosthetics in Uganda.

<a id="ref-ibiwari-2025"></a> Ibiwari, B. W., Osemeke, B. E., Progress, V. D., Khadija, A., & Chikere, O. P. (2025). Hand anthropometric measurement and grip strength for basketball and volleyball players in higher institutions in Port Harcourt metropolis. International Journal of Science Academic Research, 6(8), 10513-10517.

<a id="ref-ibrahim-2024"></a> Ibrahim, M. T., Azman, H., Adzahar, N. S. I. A., Ismail, M. A., & Shaharuddin, S. (2024). Techniques for measuring the fluctuation of residual lower limb volume in clinical practices: A systematic review of the past four decades. Applied Sciences, 14(6), 2594. https://www.mdpi.com/2076-3417/14/6/2594/pdf?version=1710932396

<a id="ref-idris-2024"></a> Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, N. (2024). Exploring the integration of artificial intelligence in co-design framework for designer. https://ebpj.e-iph.co.uk/index.php/EBProceedings/article/download/6348/3640

<a id="ref-jones-2023"></a> Jones, H., Chadwell, A., & Dyson, M. (2023). Evidencing the effectiveness of upper limb prostheses: A multi-stakeholder perspective on study requirements. *Frontiers in Health Services, 3*, Article 1213752. https://doi.org/10.3389/frhs.2023.1213752

<a id="ref-kadenhe-2025"></a> Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI co-design and co-creation: A review of emerging approaches, challenges, and future directions. Proceedings of the AAAI Symposium Series, 6(1), 265-270. https://doi.org/10.1609/aaaiss.v6i1.36061

<a id="ref-kandikjan-2022"></a> Kandikjan, T., Djokikj, J., Mircheski, I., & Angeleska, E. (2022). Integrating parametric design and additive manufacturing knowledge in industrial design education. Materials Today: Proceedings, 70, 687-693. https://doi.org/10.1016/j.matpr.2022.10.124

<a id="ref-kannenberg-2024"></a> Kannenberg, A., Buis, A. W. P., Sengeh, D. M., & Worsley, P. R. (2024). Insights into the spectrum of transtibial prosthetic socket design from expert clinicians and their digital records. Frontiers in Rehabilitation Sciences, 5. https://doi.org/10.3389/fresc.2024.1354069

<a id="ref-kaygan-2025"></a> Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. https://doi.org/10.1080/14606925.2024.2420152

<a id="ref-kellam-2019"></a> Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

<a id="ref-kerr-2024"></a> Kerr, A., Del Din, S., Clarkson, P. J., & Rochester, L. (2024). A participatory model for cocreating accessible rehabilitation technology for stroke survivors: User-centered design approach.

<a id="ref-khanolkar-2023"></a> Khanolkar, P. M., Vrolijk, A., & Olechowski, A. (2023). Mapping artificial intelligence-based methods to engineering design stages: A focused literature review. Artificial Intelligence for Engineering Design, Analysis and Manufacturing, 37, e25. https://doi.org/10.1017/S0890060423000203

<a id="ref-krahe-2020"></a> Krahe, C., Bräunche, A., Jacob, A., Stricker, N., & Lanza, G. (2020). Deep learning for automated product design. Procedia CIRP, 91, 3-8. https://doi.org/10.1016/j.procir.2020.01.135

<a id="ref-kuhl-2020"></a> Kuhl, M., Lutz, J., Krause, D., & Vielhaber, M. (2020). Design of personalized devices: The tradeoff between individual value and personalization workload. Applied Sciences.

<a id="ref-lei-2016"></a> Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. https://dr.ntu.edu.sg/bitstream/10356/83735/1/An%20additive%20manufacturing%20process%20model%20for%20product%20family%20design.pdf

<a id="ref-li-aflatoony-2025"></a> Li, M., & Aflatoony, L. (2025). Parametric design and three-dimensional printing: Enabling occupational therapists to develop custom hand grips. Disability and Rehabilitation: Assistive Technology, 20(6), 1829-1837. https://doi.org/10.1080/17483107.2025.2483953

<a id="ref-li-2021"></a> Li, X., Demirel, H., Goldstein, M., & Sha, Z. (2021). Exploring generative design thinking for engineering design and design education. https://peer.asee.org/38349.pdf

<a id="ref-lim-2018"></a> Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. https://doi.org/10.1115/DETC2018-85645

<a id="ref-lindell-2021"></a> Lindell, E., Tingsvik, H., Guo, L., & Peterson, J. (2021). 3D body scan as anthropometric tool for individualized prosthetic socks. https://sciendo.com/pdf/10.2478/aut-2021-0007

<a id="ref-machado-2019"></a> Machado, F., Malpica, N., & Borromeo, S. (2019). Parametric CAD modeling for open source scientific hardware: Comparing OpenSCAD and FreeCAD Python scripts. PLOS ONE, 14(12), e0225795. https://doi.org/10.1371/journal.pone.0225795

<a id="ref-manero-2019"></a> Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

<a id="ref-manz-2022"></a> Manz, S., Valette, R., Damonte, F., Avanci Gaudio, L., Gonzalez-Vargas, J., Sartori, M., Dosen, S., & Rietman, J. (2022). A review of user needs to drive the development of lower limb prostheses. *Journal of NeuroEngineering and Rehabilitation, 19*, Article 119. https://doi.org/10.1186/s12984-022-01097-1

<a id="ref-marinelli-2022"></a> Marinelli, M., Putrino, D., Stella, F., & Guglielmelli, E. (2022). Active upper limb prostheses: A review on current state and upcoming breakthroughs.

<a id="ref-martins-2024"></a> Martins, R. F., Branco, R., Martins, M., Macek, W., Marciniak, Z., Silva, R., Trindade, D., Moura, C., Franco, M., & Malça, C. (2024). Mechanical properties of additively manufactured polymeric materials—PLA and PETG—for biomechanical applications. *Polymers, 16*(13), 1868. https://doi.org/10.3390/polym16131868

<a id="ref-menaka-2025"></a> Menaka, S., Raja, W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s). https://ijamjournal.org/ijam/publication/index.php/ijam/article/download/341/311

<a id="ref-mikoajewski-2023"></a> Mikołajewski, D., Rojek, I., Kotlarz, P., Dorożyński, J., & Kopowski, J. (2023). Personalization of the 3D-printed upper limb exoskeleton design: Mechanical and IT aspects. Applied Sciences.

<a id="ref-millet-2018"></a> Millet, A., Abi Akle, A., & Legardeur, J. (2018, July 5-6). Human centred criteria for healthcare design [Conference paper]. 25e colloque des Sciences de la conception et de l’innovation (CONFERE 2018), Budapest, Hungary. https://hal.science/hal-01938985

<a id="ref-mistarihi-2020"></a> Mistarihi, M. Z. (2020). A data set on anthropometric measurements and degree of discomfort of physically disabled workers for ergonomic requirements in work space design. Data in Brief, 30, 105420. https://doi.org/10.1016/j.dib.2020.105420

<a id="ref-molenbroek-1998"></a> Molenbroek, J. F. M. (1998). Geron study on Dutch elderly anthropometry. DINED database. Delft University of Technology. https://dined.io.tudelft.nl

<a id="ref-molenbroek-2003"></a> Molenbroek, J. F. M., Kroon-Ramaekers, Y. M. T., & Snijders, C. J. (2003). Revision of the Dutch standard for furniture in schools. Ergonomics, 46(5), 491-498. https://doi.org/10.1080/0014013031000085635

<a id="ref-moreo-2016"></a> Moreo, A. M. (2016). Parametric design of a 3D printable hand prosthesis for children in developing countries [Master's thesis, Delft University of Technology].

<a id="ref-nag-2003"></a> Nag, A., Nag, P. K., & Desai, H. (2003). Hand anthropometry of Indian women. Indian Journal of Medical Research, 117, 260-269.

<a id="ref-nilsiam-2017"></a> Nilsiam, Y., & Pearce, J. M. (2017). Free and open source 3-D model customizer for websites to democratize design with OpenSCAD. Designs, 1(1), 5. https://doi.org/10.3390/designs1010005

<a id="ref-nini-2024"></a> Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. https://doi.org/10.1109/BioRob60516.2024.10719909

<a id="ref-oldfrey-2024"></a> Oldfrey, B. M., Morgado Ramirez, D. Z., Miodownik, M., Wassall, M., Ramstrand, N., Wong, M. S., Danemayer, J., Dickinson, A., Kenney, L., Nester, C., Lemaire, E., Gholizadeth, H., Diment, L. E., Donovan-Hall, M. K., & Holloway, C. (2024). A scoping review of digital fabrication techniques applied to prosthetics and orthotics: Part 1 of 2—Prosthetics. *Prosthetics and Orthotics International, 48*(5), 574–589. https://doi.org/10.1097/PXR.0000000000000351

<a id="ref-ostlie-2012"></a> Østlie, K., Lesjø, I. M., Franklin, R. J., Garfelt, B., Skjeldal, O. H., & Magnus, P. (2012). Prosthesis rejection in acquired major upper-limb amputees: A population-based survey. *Disability and Rehabilitation: Assistive Technology, 7*(4), 294–303. https://doi.org/10.3109/17483107.2011.635405

<a id="ref-openscad-community-nd"></a> OpenSCAD Community. (n.d.). OpenSCAD User Manual/Using OpenSCAD in a command line environment. Wikibooks. Retrieved July 7, 2026, from https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment

<a id="ref-openscad-project-nd-a"></a> OpenSCAD Project. (n.d.-a). OpenSCAD: The programmers solid 3D CAD modeller. Retrieved July 7, 2026, from https://openscad.org/

<a id="ref-openscad-project-nd-b"></a> OpenSCAD Project. (n.d.-b). OpenSCAD source repository [Computer software]. GitHub. Retrieved July 7, 2026, from https://github.com/openscad/openscad

<a id="ref-ozdemir-2022"></a> Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0F2B66A61E2CE6410F9D1F335244EB9C/S2053470122000038a.pdf/div-class-title-design-methodology-for-mass-personalisation-enabled-by-digital-manufacturing-div.pdf

<a id="ref-panchal-2019"></a> Panchal, J. H., Fuge, M., Liu, Y., Missoum, S., & Tucker, C. S. (2019). Special issue: Machine learning for engineering design. Journal of Mechanical Design, 141(11), 110301. https://doi.org/10.1115/1.4044690

<a id="ref-parlamento-europeu-2017"></a> Parlamento Europeu, & Conselho da União Europeia. (2017). Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical devices. https://eur-lex.europa.eu/eli/reg/2017/745/oj

<a id="ref-peerdeman-2011"></a> Peerdeman, B., Boere, D., Witteveen, H., Huis in 't Veld, R., Hermens, H., Stramigioli, S., Rietman, H., Veltink, P., & Misra, S. (2011). Myoelectric forearm prostheses: State of the art from a user-centered perspective. Journal of Rehabilitation Research and Development, 48(6), 719-738. https://doi.org/10.1682/JRRD.2010.08.0161

<a id="ref-peixoto-2025"></a> Peixoto, S., Martins, N., Miranda, D., Matos, D., & Carvalho, V. (2025). The design process in the development of an online platform for personalizing wearable prostheses: A preliminary approach. Designs, 9(2), 39. https://doi.org/10.3390/designs9020039

<a id="ref-peters-2023"></a> Peters, C., & Richter, P. (2023). Individualizing patient pathways through modularization: Design and evaluation of healthcare-specific modularization parameters.

<a id="ref-quintero-2018"></a> Quintero, D., Reznick, E., Lambert, D. J., Rezazadeh, S., Gray, L., & Gregg, R. D. (2018). Intuitive clinician control interface for a powered knee-ankle prosthesis: A case study. IEEE Journal of Translational Engineering in Health and Medicine, 6, 2600209. https://doi.org/10.1109/JTEHM.2018.2880199

<a id="ref-ramnath-2019"></a> Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J. J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. In Volume 1: 39th Computers and Information in Engineering Conference (Article V001T02A006). ASME. https://doi.org/10.1115/DETC2019-97378

<a id="ref-resnik-2010"></a> Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. JPO: Journal of Prosthetics and Orthotics, 22(2), 121-126. https://doi.org/10.1097/JPO.0b013e3181d427b7

<a id="ref-rezwana-2022"></a> Rezwana, J., & Maher, M. (2022). Understanding user perceptions, collaborative experience, and user engagement in different human-AI interaction designs for co-creative systems. https://arxiv.org/pdf/2204.13217

<a id="ref-richardson-2017"></a> Richardson, C., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review.

<a id="ref-rodriguez-vega-2024"></a> Rodríguez-Vega, G., & Rodríguez-Vega, D. A. (2024). Normative data for the anthropometric hand dimensions of the Mexican population. European Public & Social Innovation Review, 9, 1-15. https://doi.org/10.31637/epsir-2024-932

<a id="ref-romani-levi-2020"></a> Romani, A., & Levi, M. (2020). Parametric design for online user customization of 3D printed assistive technology for rheumatic diseases. In International Conference on Augmented and Virtual Reality.

<a id="ref-romero-2025"></a> Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475

<a id="ref-saeidnia-2024"></a> Saeidnia, H. R., & Ausloos, M. (2024). Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework. InfoScience Trends, 1(2), 1-9. https://doi.org/10.61186/ist.202401.01.09

<a id="ref-saldarriaga-2024"></a> Saldarriaga, A. M., Romero, E., Abarca, V. E., & Elias, D. A. (2024). A parametric design approach for affordable customized 3D socket for transradial upper limb prostheses. In 2024 10th International Conference on Control, Decision and Information Technologies (CoDIT). https://doi.org/10.1109/CoDIT62066.2024.10708382

<a id="ref-samuelsson-2012"></a> Samuelsson, K. A. M., Töytäri, O., Salminen, A.-L., & Brandt, Å. (2012). Effects of lower limb prosthesis on activity, participation, and quality of life: A systematic review.

<a id="ref-schofer-seibel-2025"></a> Schöfer, F., & Seibel, A. (2025). Augmented design automation: Leveraging parametric designs using large language models. Proceedings of the Design Society.

<a id="ref-segura-2024"></a> Segura, D., Romero, E., Abarca, V. E., & Elías, D. A. (2024). Upper limb prostheses by the level of amputation: A systematic review. Prosthesis, 6(2), 22. https://doi.org/10.3390/prosthesis6020022

<a id="ref-seregni-2021"></a> Seregni, F., Arlati, S., Colombo, V., Spoladore, D., Greci, L., Pedroli, E., Serino, S., Cipresso, P., Goulene, K., Stroulia, E., Rizzo, A., & Sacco, M. (2021). Virtual coaching for rehabilitation: The participatory design experience of the vCare Project.

<a id="ref-shah-2006"></a> Shah, S. G. S., & Robinson, I. (2006). User involvement in healthcare technology development and assessment: Structured literature review. International Journal of Health Care Quality Assurance, 19(6), 500-515. https://doi.org/10.1108/09526860610687619

<a id="ref-silva-alcara-2018"></a> Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

<a id="ref-silva-2024"></a> Silva, R., Silva, B., Fernandes, C., Morouco, P., Alves, N., & Veloso, A. (2024). A review on 3D scanners studies for producing customized orthoses. Sensors, 24(5), 1373. https://pmc.ncbi.nlm.nih.gov/articles/PMC10935386/pdf/sensors-24-01373.pdf

<a id="ref-sims-2017"></a> Sims, T., Cranny, A., Metcalf, C., Chappell, P., & Donovan-Hall, M. (2017). Participatory design of pediatric upper limb prostheses: Qualitative methods and prototyping.

<a id="ref-smail-2021"></a> Smail, L. C., Neal, C., Wilkins, C., & Packham, T. L. (2021). Comfort and function remain key factors in upper limb prosthetic abandonment: Findings of a scoping review. Disability and Rehabilitation: Assistive Technology, 16(8), 821-830. https://doi.org/10.1080/17483107.2020.1738567

<a id="ref-soyer-2016"></a> Soyer, K., Unver, B., Tamer, S., & Ulger, O. (2016). The importance of rehabilitation concerning upper extremity amputees: A systematic review. https://pjms.com.pk/index.php/pjms/article/view/9922/4660

<a id="ref-squibb-2024"></a> Squibb, C., Madigan, M. L., & Philen, M. K. (2024). A high precision laser scanning system for measuring shape and volume of transtibial amputee residual limbs: Design and validation. PLOS ONE, 19(5). https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0301619&type=printable

<a id="ref-steenbekkers-1998"></a> Steenbekkers, L. P. A., & van Beijsterveldt, C. E. M. (Eds.). (1998). Design-relevant characteristics of ageing users. Delft University Press.

<a id="ref-story-2006"></a> Story, M. F. (2006). Applying the principles of universal design to medical devices. In J. M. Winters & M. F. Story (Eds.), Medical instrumentation: Accessibility and usability considerations (pp. 83-92). CRC Press. https://doi.org/10.1201/9781420006223-6

<a id="ref-stralen-2018"></a> van Stralen, M. (2018). Mass customization: A critical perspective on parametric design, digital fabrication and design democratization. In Proceedings of the 22nd Congress of the Iberoamerican Society of Digital Graphics (pp. 142-149). Blucher. https://doi.org/10.5151/sigradi2018-1770

<a id="ref-sunderland-2024"></a> Sunderland, F., Willerth, S., Silver-Thorn, B., & Dickinson, A. (2024). OpenLimbTT, a transtibial residual limb shape model for prosthetics simulation and design: Creating a statistical anatomic model using sparse data. medRxiv. https://www.medrxiv.org/content/medrxiv/early/2024/11/30/2024.11.27.24317622.full.pdf

<a id="ref-ten-kate-2017"></a> ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

<a id="ref-thorsen-2023"></a> Thorsen, R., Hansen, A. H., & Nilsen, E. R. (2023). From patient to maker: A workflow including people with cerebral palsy in co-creating assistive devices using 3D printing technologies.

<a id="ref-trautmann-2021"></a> Trautmann, L. (2021). Product customization and generative design. Multidiszciplináris Tudományok.

<a id="ref-verganti-2020"></a> Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). Innovation and design in the age of artificial intelligence. https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jpim.12523

<a id="ref-viros-i-martin-2021"></a> Virós-i-Martin, A., & Selva, D. (2021). A framework to study human-AI collaborative design space exploration. In Volume 6: 33rd International Conference on Design Theory and Methodology (Article V006T06A052). ASME. https://doi.org/10.1115/DETC2021-67619

<a id="ref-walker-2019"></a> Walker, M., Paras, A., Boonstra, N., & Murrup-Stewart, C. (2019). Towards including end-users in the design of prosthetic hands: Ethical analysis of a survey of Australians with upper-limb difference.

<a id="ref-walters-2025"></a> Walters, S., Seminati, E., Metcalfe, B., Bailey, N. Y., & Pegg, E. C. (2025). Demystifying upper limb hybrid prostheses: A scoping review. Frontiers in Rehabilitation Sciences, 6, 1610336. https://doi.org/10.3389/fresc.2025.1610336

<a id="ref-wang-2024"></a> Wang, X., & Hu, B. (2024). Machine learning algorithms for improved product design user experience. IEEE Access, 12, 112810-112821. https://doi.org/10.1109/ACCESS.2024.3442085

<a id="ref-wendo-2022"></a> Wendo, K., Barbier, O., Bollen, X., Schubert, T., Lejeune, T., Raucent, B., & Olszewski, R. (2022). Open-source 3D printing in the prosthetic field: The case of upper limb prostheses: A review. Machines, 10(6), 413. https://doi.org/10.3390/machines10060413

<a id="ref-white-2022"></a> White, J., & Mosca, E. I. (2022). Developing innovative solutions for universal design in healthcare and other sectors. Studies in Health Technology and Informatics, 297, 340-347. https://doi.org/10.3233/SHTI220858

<a id="ref-wiberg-2019"></a> Wiberg, A., Persson, J., & Ölvander, J. (2019). Design for additive manufacturing: A review of available design methods and software. Rapid Prototyping Journal, 25(6), 1080-1094. https://doi.org/10.1108/RPJ-10-2018-0262

<a id="ref-wilke-2020"></a> Wilke, H., Badke-Schaub, P., & Thoring, K. (2020). The healthcare design dilemma: Perils of a technology-driven design process for medical products. Proceedings of the Design Society: DESIGN Conference, 1, 2217-2226. https://doi.org/10.1017/dsd.2020.133

<a id="ref-windrich-2016"></a> Windrich, M., Grimmer, M., Christ, O., Rinderknecht, S., & Beckerle, P. (2016). Active lower limb prosthetics: A systematic review of design issues and solutions.

<a id="ref-xu-qin-2022"></a> Xu, K., & Qin, S.-F. (2022). 3D printing, limb prosthetics and generative design: A scoping review. In *2022 27th International Conference on Automation and Computing (ICAC)* (pp. 1–6). IEEE. https://doi.org/10.1109/ICAC55051.2022.9911138

<a id="ref-yao-2016"></a> Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive manufactured variable platforms in product families. Journal of Mechanical Design, 138(4), 041701. https://doi.org/10.1115/1.4032504

<a id="ref-young-2023"></a> Young, P. R., Hebert, J. S., Marasco, P., Carey, J., & Schofield, J. S. (2023). Advances in the measurement of prosthetic socket interface mechanics: A review of technology, techniques, and a 20-year update. https://www.tandfonline.com/doi/pdf/10.1080/17434440.2023.2244418?needAccess=true&role=button

<a id="ref-yu-2013"></a> Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

<a id="ref-yuksel-2023"></a> Yüksel, N., Börklü, H. R., Sezer, H. K., & Canyurt, O. (2023). Review of artificial intelligence applications in engineering design perspective. Engineering Applications of Artificial Intelligence, 118, 105697. https://doi.org/10.1016/j.engappai.2022.105697

<a id="ref-zhu-2022"></a> Zhu, Z., & Zhong, R. Y. (2022). A digital twin enabled wearable device for customized healthcare.

<a id="ref-zimmerman-2007"></a> Zimmerman, J., Forlizzi, J., & Evenson, S. (2007). Research through design as a method for interaction design research in HCI. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 493-502). ACM. https://doi.org/10.1145/1240624.1240704

<a id="ref-zuniga-2015"></a> Zuniga, J., Katsavelis, D., Peck, J., Stollberg, J., Petrykowski, M., Carson, A., & Fernandez, C. (2015). Cyborg beast: A low-cost 3D-printed prosthetic hand for children with upper-limb differences. BMC Research Notes, 8, 10. https://doi.org/10.1186/s13104-015-0971-9

## Anexo A — Metodologia de extração e codificação de dados antropométricos

### A.1 Contexto e Objectivo

O desenvolvimento de um gerador paramétrico de próteses de membro superior requer dados antropométricos da mão humana que sejam suficientemente variados para cobrir diferentes populações, sexos e grupos etários. O objectivo deste processo foi construir uma base de dados estruturada em formato CSV que servisse de entrada directa ao modelo paramétrico, reunindo medições reais retiradas de literatura científica publicada e de relatórios técnicos de antropometria militar.

Foram produzidos três conjuntos de dados complementares em formato CSV:

- conjunto ANSUR completo — 2.726 linhas de dados, 47 dimensões corporais do estudo ANSUR 1988 (Gordon et al., 1989), população militar norte-americana

- subconjunto ANSUR mão–braço — 696 linhas de dados, restrito às medições da mão, antebraço e braço

- conjunto de dados da mão proveniente de várias populações — 1.790 linhas, provenientes de fontes e subconjuntos populacionais de nove países

### A.2 Estratégia de Pesquisa Bibliográfica

### A.2.1 Pesquisa bibliográfica orientada

A pesquisa de literatura recorreu a consultas bibliográficas orientadas por questões, complementadas por ferramentas de apoio à revisão e triagem, com o objectivo de identificar estudos de antropometria da mão com dados primários tabelados. As questões-chave incluíam variações de:

> "*hand anthropometry normative data population study percentiles*" "*hand dimensions measurement ergonomics working population*" "*anthropometric survey finger length breadth caliper*"

As listas de referências resultantes foram guardadas localmente em pastas organizadas por capítulo da tese. Os ficheiros de trabalho, citações e listas bibliográficas foram cruzados com a coleção local de PDFs para identificar lacunas.

### A.2.2 Base ANSUR 1988

O relatório ANSUR 1988 (Gordon et al., 1989) apresenta 9.068 participantes no levantamento geral. Os ficheiros gerados neste projecto codificam as tabelas estatísticas detalhadas do anexo para os grupos nelas identificados: 2.208 mulheres e 1.774 homens, num total analítico de 3.982 participantes. O total geral do levantamento e os grupos das tabelas codificadas têm âmbitos distintos e não devem ser somados nem usados como se descrevessem a mesma amostra. As tabelas fornecem, para cada dimensão e por sexo, média, desvio-padrão, percentis do P1 ao P99, mínimo e máximo.

### A.3 Critérios de Inclusão e Exclusão de Estudos

Para cada estudo identificado, a decisão de incluir ou excluir os seus dados na base CSV seguiu critérios explícitos.

### A.3.1 Critérios de inclusão

Um estudo foi incluído se satisfazia simultaneamente as seguintes condições:

1. Dados primários — o estudo apresenta medições recolhidas pelos seus próprios autores sobre participantes reais, não reutilizando tabelas de terceiros sem transformação.

2. Dimensões da mão ou do membro superior — pelo menos uma medição refere-se à mão, dedos, palma, antebraço ou punho.

3. Estatística descritiva legível — a tabela do artigo fornece, no mínimo, a média. A presença de desvio-padrão e/ou percentis constituía um critério de preferência.

4. Identificação clara da população — o artigo especifica país, sexo, dimensão amostral e método de medição.

### A.3.2 Critérios de exclusão

Um estudo foi excluído nas seguintes situações:

- Dados secundários sem valor acrescentado — por exemplo, o trabalho de Moreo (2016) apresenta valores percentílicos de comprimento de dedo extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas), sem recolha própria. A Tabela 6.1 desse trabalho serve apenas para validar as escolhas de *design* do protótipo, não constituindo uma fonte primária codificável de forma independente.

- Artigos de engenharia sem tabelas antropométricas — estudos centrados em materiais, análise de elementos finitos ou fabrico aditivo que referenciam dimensões da mão apenas de forma incidental e sem estatística descritiva.

- Dimensões não da mão em estudos mistos — medições de outras regiões corporais presentes no mesmo artigo foram excluídas se não existia uma razão directa para a prótese de mão (excepção: comprimento cotovelo-ponta dos dedos, incluído por ser relevante para o encaixe do *socket*).

### A.4 Processo de Extracção de Dados

### A.4.1 Leitura dos PDFs e localização das tabelas

Cada artigo foi lido integralmente, com foco nas secções de *Methods* (para identificar o instrumento de medição, a mão medida, e a posição do participante) e *Results* (para localizar as tabelas com estatística descritiva). A página exacta de cada tabela foi registada no campo sourcepage do CSV.

Quando um artigo reportava medições em mais do que uma tabela (por exemplo, comprimentos numa tabela e larguras noutra), cada tabela foi processada separadamente.

### A.4.2 Identificação das unidades e conversão

Os artigos consultados reportam medições em milímetros (mm), centímetros (cm) ou, no caso do ANSUR, em polegadas (in). O CSV armazena sempre os três sistemas em simultâneo (valuemm, valuecm, valuein), calculados a partir de uma única unidade-fonte:

- Se o artigo reporta em mm: valuecm = valuemm / 10; valuein = valuecm / 2.54

- Se o artigo reporta em cm: valuemm = valuecm × 10; valuein = valuecm / 2.54

- Se o artigo reporta em in: valuecm = valuein × 2,54; valuemm = valuein × 25,4

Esta redundância elimina conversões em tempo de execução por parte do modelo paramétrico.

### A.4.3 Decomposição em linhas atómicas

Cada célula de uma tabela estatística origina uma linha independente no CSV. Assim, para uma dada dimensão, população e sexo, existem tantas linhas quantos os indicadores estatísticos disponíveis: por exemplo, se um artigo reporta média, desvio-padrão, P5, P50 e P95, são criadas cinco linhas — cada uma com o campo stattype definido como mean, stddev ou percentile, e o campo percentile preenchido apenas nas linhas de tipo percentile.

Esta estrutura longa (*long format*) permite filtrar e agregar por qualquer combinação de variáveis sem necessidade de transformação prévia.

### A.4.4 Registo fiel do contexto da medição

O campo measurementmethodnote regista, para cada estudo, informações sobre:

- O instrumento utilizado (e.g., "paquímetro digital Vernier 200 mm, resolução 0,01 mm")

- A mão medida (direita/esquerda/dominante)

- A posição da mão durante a medição (estendida e plana, em posição de repouso, sentado)

- O ponto de referência do comprimento (e.g., "da prega palmar proximal à ponta do dedo")

Esta informação é crítica porque estudos diferentes definem as mesmas dimensões com protocolos diferentes: por exemplo, "comprimento da mão" pode ser medido desde a prega do pulso até à ponta do dedo médio (Rodríguez-Vega et al., 2024) ou desde o processo estilóide até à mesma ponta (Anacleto Filho et al., 2023), produzindo valores não directamente comparáveis.

### A.5 Decisões por Estudo

### A.5.1 ANSUR 1988 — EUA, militares (Gordon et al., 1989)

Fonte: tabelas detalhadas do relatório técnico do U.S. Army Natick Research Center (março de 1989), com 47 dimensões corporais codificadas e grupos separados por sexo (n=2.208 mulheres; n=1.774 homens). O relatório apresenta 9.068 participantes no levantamento geral, enquanto os grupos usados nas tabelas codificadas totalizam 3.982. As dimensões da mão e do membro superior incluem comprimento e largura da mão, comprimentos dos dedos, circunferência do pulso e comprimento do antebraço.

Decisão: inclusão das 47 tabelas legíveis codificadas no *script*. A dimensão amostral, a amplitude dos indicadores estatísticos e a descrição do levantamento tornam esta fonte uma referência central da base de dados, sem a converter em norma universal para outras populações.

Notas: a auditoria ao código e ao documento de origem identificou oito células anómalas, classificadas como seis normalizações ou correcções e dois valores preservados com advertência. Esta enumeração substitui a formulação imprecisa de «sete correcções». Cinco valores em centímetros foram corrigidos com apoio na coluna em polegadas ou na sequência estatística: página 8, percentil 40 feminino, 74,93 para 71,93 cm; página 37, percentil 1 feminino, 35,55 para 53,55 cm; página 42, percentil 65 masculino, 507,19 para 207,19 cm; página 44, percentil 95 feminino, 1143,33 para 114,33 cm; e página 45, percentil 2 masculino, 35,31 para 25,31 cm. Na página 25, a impressão «59397» na coluna em polegadas foi normalizada para 59,97 in apenas para apresentação, porque o valor de 152,32 cm já estava correcto. Na página 40, o mínimo feminino de 11,70 cm foi mantido e assinalado como provável erro; na página 46, o desvio-padrão masculino de 0,52 cm foi igualmente mantido e marcado como incerto, pois a coluna em polegadas indica cerca de 3,53 cm. Cada caso fica descrito no campo `dataqualitynote`, permitindo distinguir alterações efectuadas de valores apenas sinalizados.

### A.5.2 Turquia — jovens adultos (Chatzioglou et al., 2024)

Fonte: Anatomy & Cell Biology, 57:172–182. n=51 (32F, 19M), idade 18–30, Izmir e Istanbul. Método foto-antropométrico com ImageJ (pixel → mm via factor de calibração 0,08618 ×). Comprimentos dos cinco dedos da mão direita, por sexo e amostra total, Tabela 1.

Decisão: inclusão. Primeiro estudo de foto-antropometria da mão na base de dados; o método dispõe de documentação rigorosa e o artigo foi publicado em revista indexada com revisão por pares. Os valores mínimo e máximo, sem percentis, foram codificados como `stattype = min` e `max`.

### A.5.3 México — população geral (Rodríguez-Vega & Rodríguez-Vega, 2024)

Fonte: European Public & Social Innovation Review, 9:1–15. n=2.837 (2.275M, 562F), Noroeste do México, idade 15–59. Quatro dimensões: comprimento da mão (HL), comprimento da palma (PL), largura da mão (HB) e diâmetro de preensão (HGD). Tabela 3 (amostra geral) e Tabela 4 (oito grupos etários: 15–19, 20–24, …, 50–54).

Decisão: inclusão, com marcação de qualidade nos subgrupos de pequena dimensão. A desagregação por grupo etário é única na base de dados e relevante para modelação por faixa etária. Foram detectados dois casos problemáticos na Tabela 4: o subgrupo feminino 50-54 tem n=3 (`SD = 0,00` reportado para `HB`, provavelmente por arredondamento); o subgrupo feminino 45-49 tem n=10. Ambos foram incluídos e marcados no campo `dataqualitynote`.

### A.5.4 Índia — mulheres trabalhadoras (Nag et al., 2003)

Fonte: Indian Journal of Medical Research, 117:260–269. n=95 mulheres, trabalhadores informais (indústria de bidis, agarbattis e vestuário), Ahmedabad. 51 dimensões da mão direita em cinco tabelas (comprimentos, larguras, circunferências, profundidades, extensões e folgas), com P5, P50 e P95 reportados.

Decisão: inclusão total. É o estudo com maior detalhe de dimensões da mão na base de dados e o único com dados de profundidade e circunferência por articulação. A restrição a mulheres e a uma população laboral informal específica é documentada na coluna `population`.

### A.5.5 Portugal — trabalhadores industriais (Anacleto Filho et al., 2023)

Fonte: International Journal of Industrial Ergonomics, 97:103473. n=343 (169M, 174F),

trabalhadores industriais do Norte de Portugal, 2021. De um conjunto de 27 dimensões corporais, apenas duas são da mão: comprimento da mão e largura da mão (metacarpal II–V). Tabela 3, P5, P50, P95 por sexo.

Decisão: inclusão. Embora sejam disponibilizadas duas dimensões da mão, trata-se da única fonte de dados antropométricos da mão para população portuguesa adulta identificada na literatura, o que justifica a sua inclusão na contextualização nacional da dissertação.

Nota metodológica: O estudo mediu o lado esquerdo por limitação de instalações; este facto é registado em measurementmethodnote.

### A.5.6 Nigéria — atletas universitários (Ibiwari et al., 2025)

Fonte: International Journal of Science Academic Research, 6(8):10513–10517. n=80: basquetebol (n=41: 21M, 20F) e voleibol (n=39: 20M, 19F), Universidade de Port Harcourt, idade 19–30. Quatro dimensões da mão direita por desporto e sexo: comprimento da mão, largura da mão, comprimento palmar e comprimento do 3.º dígito. Tabelas 3 e 4.

Decisão: inclusão com marcação de subgrupo desportivo. Dois subgrupos apresentam desvio-padrão atipicamente elevado, como o comprimento da mão no voleibol masculino (`SD = 37,49 mm`), sugerindo a presença de valores atípicos na amostra original. Estes casos foram marcados com nota de qualidade; os valores foram preservados por provirem de tabelas publicadas.

Nota: A população de atletas não é representativa da população geral; os valores reflectem uma selecção fisicamente activa e potencialmente com mãos de dimensões superiores à média.

### A.5.7 Jordânia — trabalhadores com deficiência (Mistarihi, 2020)

Fonte: Data in Brief, 30:105420. n=40 trabalhadores com deficiência física, governorate de Irbid, Jordânia, idade 20–40. Sexos combinados (sem desagregação por sexo em Tabela 4). Comprimento da mão (mm) e comprimento cotovelo-ponta dos dedos (cm) com P5 e P95 na Tabela 4; largura da mão (cm, média apenas) a partir da Figura 2.

Decisão: Inclusão parcial. A dimensão amostral reduzida (n=40) e a ausência de desagregação por sexo limitam a utilidade directa dos dados. No entanto, é o único estudo com dados de uma população do Médio Oriente e com uma população com deficiência, o que justifica a inclusão para representatividade demográfica. A largura da mão (apenas média, sem SD, retirada de um diagrama de figura e não de uma tabela) foi incluída com marcação explícita de qualidade.

### A.5.8 EUA — dedo indicador (Lim et al., 2018)

Fonte: Trabalho académico UC Berkeley. n=50 adultos, idade 18–30. Apenas duas dimensões do dedo indicador (D2): comprimento MCP-ponta (média=90,9 mm) e largura na articulação PIP (média=16,9 mm). Apenas médias reportadas, sem SD ou percentis.

Decisão: inclusão limitada. A ausência de desvio-padrão e percentis reduz significativamente a utilidade estatística. O estudo foi incluído por se orientar especificamente para a personalização de próteses de dedo e fornecer valores de referência para o *design* de um dedo indicador protésico, directamente relevantes para o objectivo desta dissertação. O coeficiente de determinação `R² = 0,18` entre comprimento e largura do dedo é registado como indicador de correlação fraca.

### A.5.9 Estudo excluído: Moreo (2016)

O trabalho de Moreo (2016), dissertação de mestrado sobre *design* paramétrico de prótese de mão para crianças, foi lido na íntegra (55 páginas). A Tabela 6.1 apresenta valores percentílicos de comprimento de dedo por grupo etário, mas estes valores são extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas), sem recolha primária por parte da autora. A inclusão duplicaria uma fonte secundária sem ligação directa ao estudo DINED original. Decisão: excluído.

### A.5.10 EUA — militares ANSUR II (Gordon et al., 2015)

Fonte: Relatório técnico NATICK/TR-15/007, U.S. Army Natick Soldier Research, Development and Engineering Center. n=6.068 militares activos (4.082M, 1.986F), idade 17–58, grande diversidade étnica. Os dados brutos individuais foram disponibilizados em acesso público em 2017 (licença CC BY 4.0). As estatísticas foram calculadas a partir dos CSV individuais, usando Python sem dependências externas, para permitir a regeneração exacta pelo mesmo procedimento.

Decisão: Inclusão total. É o maior conjunto de dados individuais de antropometria da mão disponível publicamente. A disponibilidade de dados brutos individuais (em vez de apenas tabelas sumárias) permitiu calcular o conjunto completo de 11 indicadores por dimensão (média, SD, mínimo, máximo, P5, P10, P25, P50, P75, P90, P95). Sete medições codificadas: comprimento da mão, largura da mão (metacarpal), circunferência da mão, comprimento da palma, circunferência do pulso, comprimento antebraço-ponta do dedo médio e comprimento antebraço-centro de preensão.

Nota: A medição wristheight foi excluída — corresponde à distância do chão ao pulso em posição de pé, uma dimensão postural e não uma medição da mão.

### A.5.11 Países Baixos — DINED (TU Delft, 1993–2004)

Fonte: Base de dados antropométrica do Delft Institute for Ergonomics and Design, acessível via conta institucional em dined.io.tudelft.nl. Três sub-datasets distintos, com dados de mão disponíveis:

- kima1993: crianças neerlandesas, idades 2–12 (grupos por ano), por sexo e combinado; 8 medições da mão por grupo etário.

- geron1998: idosos neerlandeses, idades 50–80+ (bandas de 5 anos), por sexo e combinado; 5 medições da mão.

- dined2004: adultos neerlandeses, grupos etários 20–30, 31–60, 60+, por sexo e combinado; 6–7 medições da mão.

Os dados foram extraídos a partir do HTML da interface *web* (padrões id="mean{col}{row}" / id="sd{col}{row}"), mapeando índices de coluna para combinações (*sub-dataset*, sexo, grupo etário) e índices de linha para nomes de medição.

Decisão: Inclusão total (três *sub-datasets*). Apenas média e desvio-padrão estão disponíveis; percentis não são fornecidos pela interface DINED. O grupo combinado 20–60 do dined2004 foi excluído por ser redundante relativamente aos grupos 20–30 e 31–60. Primeiro *dataset* pediátrico e o *dataset* de idosos mais granular da base de dados.

### A.5.12 China — idosos de Pequim (Hu et al., 2007)

Fonte: International Journal of Industrial Ergonomics, 37(4):303–311. DOI: 10.1016/j.ergon.2006.11.006. n=108 (58F, 50M), idade 65–85, residentes na área de Pequim, recrutados por conveniência entre reformados. Medições com paquímetro deslizante e paquímetro de pontas, segundo a norma chinesa GB/T 5703-1999 (equivalente à ISO 7250:1996). Tabela 1 (média e desvio-padrão) e Tabela 2 (P1, P5, P50, P95, P99).

Decisão: Inclusão parcial (cinco medições de mão/antebraço: largura da mão no metacarpal, largura máxima da mão, comprimento da mão, comprimento do dedo, comprimento antebraço-ponta dos dedos). P5, P50 e P95 codificados a partir da Tabela 2. A medição "*Finger length*" usa a designação do padrão GB/T 5703 sem especificar o dígito; assume-se o dedo médio, documentado em dataqualitynote.

Nota de cobertura: Primeira fonte de dados de idosos chineses e, simultaneamente, a única fonte da Ásia Oriental na base de dados (após a verificação de que uma referência alternativa inicialmente identificada não era verificável).

### A.5.13 Estudo excluído: reconstrução corporal 3D a partir de fotografias ortogonais

Fonte: artigo metodológico sobre reconstrução de modelos corporais 3D a partir de fotografias ortogonais, publicado no International Journal of Industrial Ergonomics, usando deformação de forma livre (FFD).

Decisão: excluído. O artigo não é um estudo de antropometria populacional: apresenta um método de modelação e valida-o sobre um único sujeito. A figura de validação do artigo compara valores do modelo com valores do participante real para 22 dimensões — não constituindo estatística descritiva de uma amostra. Não há média, desvio-padrão nem percentis de uma população. Incluir o valor de comprimento de mão do sujeito de validação (17 cm, lido do gráfico) seria metodologicamente incorreto.

### A.6 Estrutura do CSV e esquema de dados

### A.6.1 Campos

| Campo | Tipo | Descrição |

| --- | --- | --- |

| sourcedocument | *string* | Título abreviado do artigo ou relatório fonte |

| sourcepage | *int* | Página da tabela de origem no documento |

| sourcecitation | *string* | Citação completa em estilo APA |

| measurementname | *string* | Nome da dimensão, incluindo especificações de método quando relevante |

| bodyregion | *string* | Região corporal (*hand, forearm, upperarm, lowerlimb, torso, head*) |

| measurementmethodnote | *string* | Instrumento, mão medida, posição e protocolo de medição |

| population | *string* | Descrição da população (e.g., "*Young adults (age 18-30)*") |

| country | *string* | País de recolha dos dados |

| sex | *string* | *male, female ou combined* |

| agegroup | *string* | Intervalo etário da (sub)amostra |

| samplesize | *int* | Número de participantes na (sub)amostra |

| stattype | *string* | Tipo de estatística: *mean, stddev, percentile, min, max* |

| percentile | *string* | Valor do percentil (5, 10, 25, 50, 75, 90, 95) — vazio se não aplicável |

| valuecm | *float* | Valor em centímetros |

| valuemm | *float* | Valor em milímetros |

| valuein | *float* | Valor em polegadas (calculado automaticamente) |

| dataqualitynote | *string* | Notas sobre limitações, artefactos ou incertezas do valor |

### A.6.2 Formato longo (*long format*)

A opção pelo formato longo — uma linha por estatística, e não uma linha por dimensão com colunas mean, sd, p5, etc. — permite:

- Filtrar facilmente por tipo de estatística sem tratamento especial de colunas opcionais

- Incluir estudos que reportam apenas subconjuntos de estatísticas (e.g., apenas média, sem percentis) sem introduzir células vazias em colunas estruturais

- Acrescentar novos tipos de estatística, por exemplo intervalos de confiança, sem alterar o esquema de dados

O custo é a repetição dos campos de identificação (país, sexo, dimensão) em cada linha — aceitável dado o volume total de dados (< 5 MB).

### A.7 Controlo de Qualidade dos Dados

### A.7.1 Marcação *inline* de limitações

O campo dataqualitynote é preenchido sempre que existe uma das seguintes situações:

- Valor extraído de uma figura (diagrama ou gráfico) em vez de uma tabela

- Subgrupo com n ≤ 10

- Desvio-padrão ausente ou atipicamente elevado

- Valor estimado a partir de estatísticas adjacentes por ilegibilidade da tabela

- Correlação fraca entre variáveis reportada pelo próprio estudo

- Inconsistência tipográfica no documento original, corrigida com nota

### A.7.2 Verificação de unidades

Todos os valores foram verificados pela coerência de ordem de grandeza. Por exemplo, um comprimento de mão adulta reportado em cm deve situar-se entre 15 e 22 cm; qualquer valor fora deste intervalo foi relido no artigo original antes de ser codificado.

### A.7.3 Ligação à fonte

Cada linha do CSV contém a citação completa (sourcecitation) e o número de página exacto (sourcepage), permitindo que qualquer valor seja verificado directamente na fonte primária sem necessidade de metadados externos.

### A.8 Escrita do Código de Geração

Os dados foram codificados por dois procedimentos Python independentes:

- procedimento ANSUR — gera o conjunto completo e o subconjunto mão–braço a partir de dicionários Python incorporados, um por tabela do relatório ANSUR

- procedimento de integração dos dados — gera o conjunto de dados da mão a partir de secções correspondentes às fontes e aos subconjuntos incluídos

A incorporação dos dados no código serve três propósitos: manter cada valor junto da citação e da nota de método; permitir que a execução do *script* regenere o CSV pelo mesmo procedimento; e tornar as alterações visíveis no histórico de versões com o contexto da fonte modificada.

O *script* aplica automaticamente as conversões de unidade, calcula valuein a partir de valuecm, e valida que nenhuma linha é emitida sem pelo menos uma das colunas valuemm ou valuecm preenchida.

### A.8.1 Correspondência entre os CSV e os parâmetros da plataforma

Os CSV não são enviados directamente ao modelo OpenSCAD nem constituem registos individuais. O importador agrega as linhas estatísticas por população, sexo, grupo etário e tipo de estatística, guarda os perfis normalizados na base local da aplicação e organiza as medidas numa árvore `measurements`. A correspondência posterior é executada pelo serviço determinístico de correspondência de perfis, no estado da plataforma usado nos ensaios principais. Este serviço é partilhado pela aplicação da configuração de referência e pela construção do contexto antropométrico enviado à IA.

O mapeamento canónico liga apenas medidas com correspondência anatómica explícita: `palm.width_mm` a `palm_breadth_mm`; `palm.length_mm` a `palm_length_mm`; `palm.thickness_mm` a `palm_thickness_mm`; os comprimentos totais de `digits.index`, `middle`, `ring`, `pinky` e `thumb` aos cinco parâmetros `*_finger_length_mm`; os comprimentos proximais dos mesmos dedos aos parâmetros `*_base_length_mm`; e `wrist.circumference_mm` a `wrist_circumference_mm`. Um valor só é aplicado quando o parâmetro existe no modelo activo, é numérico, pertence a este mapa e contém uma medida finita e positiva. O valor é arredondado a uma casa decimal e limitado pelo mínimo e pelo máximo declarados no catálogo de modelos; parâmetros em falta permanecem por configurar e parâmetros mecânicos, de visualização ou de lateralidade não são alterados por esta operação.

Quando a entrada é uma descrição textual, a selecção da referência populacional usa uma pontuação determinística. O algoritmo pondera correspondência de sexo, categoria e proximidade etária, menção explícita do país e qualidade do subconjunto, aceitando apenas resultados acima do limiar codificado. Se o país descrito não estiver presente na base, não é atribuído qualquer ponto de correspondência nacional; o sistema pode seleccionar um grupo com base nos restantes campos, mas essa escolha deve ser apresentada como referência populacional aproximada. As médias seleccionadas orientam a configuração inicial e o contexto da IA, sem substituir medidas directas da pessoa nem demonstrar ajuste anatómico individual.

Este encadeamento separa quatro unidades que não devem ser confundidas: a linha estatística do CSV, o perfil populacional agregado na base de dados, o conjunto de parâmetros compatíveis com o modelo activo e a geometria gerada após confirmação humana. O percurso pode, assim, ser reconstruído desde a fonte e a página registadas no CSV até ao caminho antropométrico, ao nome do parâmetro e ao limite aplicado pelo modelo.

### A.9 Resultado Final

| Conjunto de dados | Linhas | Países | Fontes ou subconjuntos | Dimensões distintas |

| --- | --- | --- | --- | --- |

| ANSUR completo | 2.726 | 1 (EUA) | 1 | 47 |

| ANSUR mão–braço | 696 | 1 (EUA) | 1 | 17 |

| Base de dados da mão com dados de várias populações | 1.790 | 9 | 12 | cerca de 85 |

Estes totais foram confirmados pela regeneração dos três conjuntos de dados. A contagem de 12 corresponde a documentos-fonte ou subconjuntos identificados pelo procedimento de geração e não implica 12 estudos primários independentes.

A base de dados da mão reúne informação proveniente de nove países (EUA, Países Baixos, Turquia, México, Índia, Portugal, Nigéria, Jordânia e China), ambos os sexos e grupos combinados, grupos etários desde os 2 até aos 80 ou mais anos, e populações como crianças em idade escolar, idosos, atletas universitários, trabalhadores industriais, trabalhadoras informais e militares.

Na inspecção final da base local da aplicação, a tabela antropométrica continha 100 perfis agregados: 97 com origem `csv_bulk`, dois com origem `csv` e um criado manualmente. Este total representa perfis processados pela aplicação e não linhas dos três CSV; cada perfil pode reunir várias estatísticas e medidas da mesma população.

### A.10 Cobertura Global da Base de Dados e Lacunas

### A.10.1 O que está coberto

A base de dados da mão foi construída para reunir dados de várias populações e representar a diversidade antropométrica da mão em termos geográficos, demográficos, etários e estatísticos. A tabela seguinte sintetiza a cobertura actual.

### A.10.1.1 Cobertura geográfica

| Região | Países representados | Fonte(s) |

| --- | --- | --- |

| Europa Ocidental | Portugal, Países Baixos | Anacleto Filho et al. (2023); DINED kima1993, geron1998, dined2004 |

| América do Norte | EUA | ANSUR 1988, ANSUR II 2012, Lim et al. (2018) |

| América Latina | México | Rodríguez-Vega et al. (2024) |

| Médio Oriente | Jordânia | Mistarihi (2020) |

| África | Nigéria | Ibiwari et al. (2025) |

| Sul da Ásia | Índia | Nag et al. (2003) |

| Ásia Oriental | China (Pequim) | Hu et al. (2007) |

| Europa do Sul / Ásia Menor | Turquia | Chatzioglou et al. (2024) |

Nove países estão representados, distribuídos por sete regiões do mundo. A cobertura é particularmente densa nos EUA (três fontes independentes) e nos Países Baixos (três *sub-datasets* DINED).

### A.10.1.2 Cobertura etária

| Faixa etária | Cobertura | Fonte(s) |

| --- | --- | --- |

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

### A.10.1.3 Cobertura estatística

A profundidade estatística varia consideravelmente entre fontes:

| Nível de detalhe | Estudos |

| --- | --- |

| Média, SD, min, max, P5–P95 (11 indicadores) | ANSUR 1988, ANSUR II 2012 |

| Média e SD (2 indicadores) | DINED (3 subconjuntos) |

| Média, SD, P5, P50, P95 (5 indicadores) | Hu et al. (2007) |

| P5, P50, P95 (3 indicadores) | Nag et al. (2003), Anacleto Filho et al. (2023), Rodríguez-Vega et al. (2024) |

| Média, SD, min, max (4 indicadores) | Chatzioglou et al. (2024), Ibiwari et al. (2025) |

| Média apenas | Mistarihi (2020) — largura da mão; Lim et al. (2018) |

A maioria das fontes não-americanas fornece apenas subconjuntos de estatísticas. Percentis intermédios (P10, P25, P75, P90) estão disponíveis exclusivamente nos *datasets* ANSUR. Esta assimetria é uma limitação real: para populações não-americanas, o modelo paramétrico pode interpolar entre P5 e P95, mas não dispõe de percentis de granularidade fina.

### A.10.2 Onde a cobertura falha

### A.10.2.1 Lacunas geográficas

As regiões mais populosas do mundo estão sub-representadas ou ausentes:

- Ásia Oriental — China tem uma única fonte (n=108, apenas idosos de Pequim). Japão e Coreia do Sul estão completamente ausentes, apesar de serem países com literatura ergonómica activa. O conjunto ANSUR é amplamente usado como *proxy* para populações ocidentais, mas os valores diferem sistematicamente das populações do leste asiático (mãos tendencialmente mais pequenas nos estudos disponíveis).

- Ásia do Sudeste — Nenhum país representado (Indonésia, Filipinas, Vietname, Tailândia, etc.), apesar de concentrarem uma fração significativa da população mundial e de apresentarem diferenças antropométricas documentadas relativamente às populações sul-asiáticas.

- África Subsaariana — Apenas a Nigéria, com uma amostra de atletas universitários (n=80) que não é representativa da população geral. Angola, Moçambique, e outros países de língua portuguesa estão ausentes, o que é particularmente relevante numa tese desenvolvida em Portugal.

- América do Sul — Completamente ausente. Brasil, Colômbia e Argentina têm literatura ergonómica publicada mas não foram identificadas fontes acessíveis com dados de mão codificáveis.

- Europa Central e de Leste — Ausente. Os Países Baixos e Portugal representam a Europa, mas existem diferenças antropométricas documentadas entre populações do norte, sul e leste do continente.

### A.10.2.2 Lacunas demográficas

- Adolescentes (13–17 anos) — a transição da mão infantil para a adulta não está coberta por nenhum estudo dedicado. O kima1993 chega aos 12 anos e o ANSUR começa aos 17.

- Amputados — a mão de referência para uma prótese unilateral é a mão contralateral intacta do próprio utilizador. Não foi identificado nenhum estudo com estatística descritiva da mão intacta de utilizadores de próteses. Esta é a lacuna de maior impacto directo para o objectivo desta tese: sem estes dados, a personalização paramétrica baseia-se em populações saudáveis como aproximação.

- Pessoas com deficiência física — apenas o estudo de Mistarihi (2020) cobre esta população (n=40, sexos combinados, Jordânia). A dimensão amostral é insuficiente para ser estatisticamente representativa.

- Idosos fora da Europa e China — a prevalência de amputação de membro superior é mais elevada em contextos de baixo rendimento (causas traumáticas, diabetes, doença vascular), mas os dados de idosos disponíveis limitam-se a populações europeias e chinesas.

### A.10.2.3 Limitações qualitativas dos dados existentes

Para além das lacunas por ausência, existem limitações nos dados já presentes:

- Heterogeneidade de protocolos — "comprimento da mão" é medido desde pontos de referência distintos consoante o estudo (prega distal do pulso, processo estilóide do rádio, articulação metacarpo-falângica). Os valores não são directamente comparáveis entre fontes sem ajuste, o que limita a integração directa para inferência de valores fora da base de dados.

- Amostras de conveniência — a maioria dos estudos não é probabilística: Chatzioglou et al. (2024) recrutou estudantes universitários de Izmir e Istanbul; Ibiwari et al. (2025) recrutou atletas universitários; Hu et al. (2007) recrutou reformados da área de Pequim. A representatividade nacional é, em todos estes casos, questionável.

- Desequilíbrio de dimensões — o comprimento da mão e a largura da mão (metacarpal) estão presentes em quase todas as fontes; comprimentos por falange individual, profundidade da palma, e ângulos de abdução dos dedos estão ausentes exceto no ANSUR.

- Mão medida — a maioria dos estudos mede a mão dominante ou a mão direita; o estudo português mede a mão esquerda por limitação de instalações. Esta inconsistência é registada nos metadados mas não pode ser corrigida post-hoc.

### A.10.3 Frentes identificadas para expansão futura

A expansão futura da base de dados deverá priorizar três frentes: dados pediátricos e adolescentes fora do contexto europeu, fontes nacionais de antropometria da mão em regiões ainda ausentes, e conjuntos de dados com maior granularidade anatómica dos dedos, falanges, punho e antebraço distal.

### A.10.3.1 Prioridade alta

- Dados pediátricos e adolescentes da Ásia Oriental, capazes de preencher a lacuna entre os 13 e os 17 anos e de reduzir a dependência de fontes neerlandesas para perfis infantis.

- Dados industriais ou ergonómicos do Médio Oriente com maior dimensão amostral e separação por sexo, de modo a complementar a fonte jordana já incluída.

- Bases públicas nacionais com dados de mão para populações asiáticas, quando disponibilizarem metadados claros e condições de reutilização compatíveis com investigação académica.

### A.10.3.2 Prioridade média

- Relatórios técnicos com medições granulares da mão, incluindo comprimentos por falange, profundidades articulares e ângulos de preensão.

- Estudos baseados em digitalização 3D com amostras adultas amplas, desde que disponibilizem estatísticas por dimensão para além de exemplos individuais.

### A.10.3.3 Pertinência directa para o tema da tese

A lacuna de maior impacto continua a ser a ausência de dados de pessoas amputadas, sobretudo medições da mão contralateral intacta. Para o *design* de próteses de mão personalizadas, a referência mais adequada é a mão intacta do próprio utilizador, e não a média de uma população saudável. Uma recolha primária de dados, mesmo com dimensão reduzida, poderia ser metodologicamente mais valiosa do que acrescentar novas populações saudáveis sem relação clínica directa com o problema da personalização protésica.

# Anexo B — Avaliação do processo paramétrico e da interface da plataforma HandFab

**Índice de tabelas do Anexo B**

| Identificação | Descrição | Página |
| --- | --- | --- |
| Tabela B.1 | Resultados da repetição da mesma configuração por modelo | 150 |
| Tabela B.2 | Resultados do percurso examinado em três navegadores | 150 |
| Tabela B.3 | Comportamento observado perante limites, entradas inválidas e falhas previstas | 151 |
| Tabela B.4 | Categorias de problemas de acessibilidade digital detectadas automaticamente | 153 |
| Tabela B.5 | Resultados da verificação manual complementar de acessibilidade | 153 |

**Data das séries de ensaios:** 2, 13 e 14 de julho de 2026

**Estado avaliado:** HandFab durante a série complementar

**Plataforma pública:** <https://handfab.pedrocandeias.net/>

**Estado da avaliação:** executada, com resultados parciais nas verificações automáticas e manuais

## B.1 Finalidade

Este anexo documenta a avaliação complementar da plataforma HandFab a partir de questões relevantes para o *Design* Industrial. O objectivo não foi certificar o programa informático, mas examinar se o processo de configuração apresenta um comportamento suficientemente previsível para apoiar a actividade de projecto, se preserva o trabalho realizado quando surgem entradas ou falhas problemáticas e se a interface apresenta problemas detectáveis por regras automáticas de acessibilidade digital.

A avaliação foi organizada em três dimensões:

1. **consistência da geração**, entendida como a capacidade de uma configuração fixa produzir a mesma geometria nas execuções concluídas;
2. **recuperação e controlo**, entendidos como a capacidade de limitar, rejeitar ou explicar valores problemáticos sem destruir a configuração válida;
3. **verificação automática e manual de regras seleccionadas de acessibilidade digital**, entendida como a identificação de barreiras nos estados examinados, sem a confundir com usabilidade, acessibilidade percebida por participantes ou conformidade global com as WCAG.

## B.2 Âmbito e limites

Os ensaios locais decorreram numa cópia isolada da plataforma e usaram exclusivamente perfis de ensaio. A plataforma pública foi examinada apenas na página de entrada, sem autenticação ou alteração de dados. Não participaram utilizadores, pessoas com diferença de membro, profissionais clínicos ou técnicos de prótese.

Por conseguinte, este anexo não avalia conforto, ajuste anatómico individual, eficácia protésica, segurança, durabilidade, aprendizagem, satisfação ou uso quotidiano. Também não constitui declaração de conformidade com as *Web Content Accessibility Guidelines* (WCAG) 2.2.

## B.3 Procedimento

Foram fixadas configurações de referência para o Flexy Beast, o Paraglider Hand e a UnLimbited Phoenix. Cada configuração deveria ser gerada e exportada dez vezes. Os ficheiros concluídos foram comparados quanto à identidade do conteúdo e às principais características geométricas.

Uma configuração da UnLimbited Phoenix foi ainda executada em três navegadores. Esta comparação procurou verificar se o percurso produzia a mesma geometria em ambientes de visualização distintos; não corresponde a uma reprodução por outra equipa ou noutro sistema de fabrico.

Os cenários de controlo abrangeram valores nos limites, abaixo deles e acima deles; campos obrigatórios ausentes; texto num campo numérico; contradição entre idade e descrição; país sem correspondência directa na base; e perfil inferior ao limite de um modelo. Abrangeram também indisponibilidade da sugestão de IA, resposta inválida, falha de geração e tentativa de exportação sem geometria.

A acessibilidade foi examinada automaticamente em oito estados do percurso local: autenticação, painel principal, perfil inicial, perfil com erro, parâmetros, sugestão antes e depois da resposta e geometria apresentada. A página pública de entrada foi examinada separadamente. A verificação manual complementar foi realizada em 2 de julho de 2026, às 16:02, em Linux e Firefox 152.0.6 (64-bit), na instância local em `localhost:3000` e na plataforma pública `handfab.pedrocandeias.net`. O percurso com leitor de ecrã usou o Orca; a reformulação do conteúdo foi examinada com ampliação a 400% e largura equivalente a 320 píxeis CSS.

## B.4 Resultados de consistência da geração

### B.4.1 Repetição da mesma configuração

Tabela B.1 — Resultados da repetição da mesma configuração por modelo

| Modelo | Execuções previstas | Execuções concluídas | Ficheiros distintos entre as conclusões | Resultado |
|---|---:|---:|---:|---|
| Flexy Beast | 10 | 7 | 1 | Consistente nas conclusões; critério integral não atingido |
| Paraglider Hand | 10 | 5 | 1 | Consistente nas conclusões; critério integral não atingido |
| UnLimbited Phoenix | 10 | 5 | 1 | Consistente nas conclusões; critério integral não atingido |

Dentro de cada modelo, todas as execuções concluídas produziram um único ficheiro distinto: o conteúdo binário, as dimensões, o número de faces e as restantes métricas registadas permaneceram iguais. Algumas execuções foram interrompidas por bloqueios e tempos-limite no ambiente de ensaio. Como não foram obtidas as dez conclusões previstas por modelo, o resultado global é classificado como **parcial** e não como confirmação integral da consistência entre repetições.

Este resultado também não demonstra qualidade geométrica. O Flexy Beast apresentou arestas não conformes com a condição de sólido múltiplo; o Paraglider continha faces degeneradas e superfície aberta; e a UnLimbited Phoenix apresentou faces degeneradas, arestas não conformes e superfície aberta. A repetição confirmou que a mesma geometria era produzida, incluindo os seus limites.

### B.4.2 Comparação entre navegadores

Tabela B.2 — Resultados do percurso examinado em três navegadores

| Navegador | Percurso concluído | Comparação da geometria | Interpretação |
|---|---|---|---|
| Chromium | Sim | Referência | Percurso concluído |
| Firefox | Sim | Ficheiro idêntico ao Chromium | Resultado equivalente no caso examinado |
| WebKit | Não | Não aplicável | Percurso interrompido na autenticação; resultado inconclusivo |

Uma primeira tentativa com WebKit foi anulada porque o próprio instrumento de ensaio aplicou ao navegador uma opção destinada ao Chromium. Após a correcção, o WebKit iniciou, mas o formulário de autenticação permaneceu oculto e o percurso não chegou à geometria. Não foi, por isso, demonstrada nem uma incompatibilidade da plataforma nem a sua compatibilidade com WebKit.

## B.5 Resultados de recuperação e controlo

Tabela B.3 — Comportamento observado perante limites, entradas inválidas e falhas previstas

| Situação examinada | Comportamento observado | Leitura para o processo de *design* |
|---|---|---|
| Valores mínimo e máximo | Aceites e gerados | Os limites declarados integram o espaço de configuração |
| Valores abaixo ou acima dos limites | Rejeitados no pedido directo | Evita guardar silenciosamente valores fora da gama nesse percurso |
| Campo obrigatório ausente | Rejeitado com indicação do problema | A configuração incompleta não foi criada |
| Perfil abaixo do limite Phoenix | Elevado ao mínimo com registo da alteração | O limite do modelo actuou de forma explícita |
| País sem cobertura directa | Seleccionado um grupo substituto identificável | A ausência de correspondência nacional não foi apresentada como correspondência directa |
| Serviço de IA indisponível | Configuração anterior preservada | O trabalho realizado não foi destruído |
| Resposta de IA inválida | Resposta não aplicada; nova tentativa concluída | A recuperação foi possível |
| Falha de geração | Interface manteve-se disponível e aceitou nova tentativa | O percurso não ficou bloqueado de forma permanente |
| Exportação sem geometria | Operação impedida com mensagem | Não foi criado um ficheiro sem conteúdo válido |
| Texto num campo numérico | Rejeitado pela interface, mas aceite pelo pedido directo | As regras não são ainda coerentes em todas as etapas |
| Sugestão simulada acima do limite | Detectada pelo esquema, mas aplicada ao valor interno | A detecção não impediu a aplicação e exige correcção |

Os resultados mostram que a maioria das situações previstas preservou o estado válido ou permitiu recuperação. As duas últimas situações são, contudo, fragilidades relevantes: uma salvaguarda visual não basta se o mesmo valor puder entrar por outra etapa, e um limite apenas detectado não protege a geometria se a sugestão continuar a ser aplicada. A decisão de projecto resultante é concentrar a verificação antes de qualquer valor ser guardado ou enviado ao modelo paramétrico.

Os ensaios relativos à IA recorreram a respostas simuladas e controladas. Confirmam o comportamento da interface perante respostas previstas, mas não medem estabilidade, dispersão ou qualidade de um modelo de linguagem real. Não foi executada uma série extensa de repetições com chamadas reais ao fornecedor de IA.

## B.6 Resultados da verificação de acessibilidade digital

### B.6.1 Percurso local autenticado

Foram examinados oito estados da interface. O total de treze ocorrências corresponde à soma das regras assinaladas em cada estado, e não a treze tipos diferentes de barreira. Foram identificadas quatro categorias:

Tabela B.4 — Categorias de problemas de acessibilidade digital detectadas automaticamente

| Categoria | Gravidade indicada pelo instrumento | Estados afectados | Consequência de *design* |
|---|---|---:|---|
| Contraste de cor insuficiente | Grave | 8 | Texto e controlos podem perder legibilidade para pessoas com baixa visão ou em condições visuais desfavoráveis |
| Rótulo não associado ao controlo | Crítica | 3 | O significado de campos e cursores pode não ser comunicado por tecnologias de apoio |
| Elementos interactivos aninhados | Grave | 1 | Pode originar foco e activação ambíguos |
| Elemento de selecção sem nome acessível | Crítica | 1 | A função do controlo pode não ser identificável fora da apresentação visual |

As ocorrências envolveram 47 elementos para contraste, 21 para associação de rótulos, quatro elementos interactivos aninhados e um elemento de selecção sem nome. Alguns elementos aparecem em mais do que um estado, pelo que estas contagens não representam necessariamente componentes únicos.

### B.6.2 Superfície pública

Na página pública não autenticada não foram detectadas violações automáticas entre os elementos examinados; oito verificações foram classificadas como aprovadas e uma ficou incompleta. Este resultado limita-se à página de entrada e não pode ser generalizado ao painel autenticado ou ao percurso de configuração.

### B.6.3 Verificação manual complementar

A grelha manual compreendeu doze verificações. Sete foram classificadas como conformes e cinco como não conformes. O protocolo preenchido e a sua representação editável são conservados no Suplemento 2 — Avaliação técnica da plataforma, como evidências `ANNEX-B-014` e `ANNEX-B-015`.

Tabela B.5 — Resultados da verificação manual complementar de acessibilidade

| Verificação | Resultado | Observação |
|---|---|---|
| Navegação por teclado (2.1.1 e 2.1.2) | Conforme | O percurso essencial foi executado apenas com o teclado, sem bloqueio do foco. |
| Visibilidade do foco (2.4.7 e 2.4.11) | Conforme | O indicador de foco permaneceu visível e não oculto nos estados examinados. |
| Ordem do foco (2.4.3) | Não conforme | Com o Orca, a ordenação dos campos não foi sempre suficientemente clara para orientar a sequência de interacção. |
| Nome, função e valor (4.1.2 e 1.3.1) | Não conforme | Com o Orca, algumas descrições de campos necessitavam de maior especificidade e clareza. |
| Identificação e sugestão de correcção de erros (3.3.1 e 3.3.3) | Conforme | Os erros examinados foram apresentados por texto e acompanhados por indicação de correcção. |
| Mensagens de estado (4.1.3) | Conforme | As mensagens dinâmicas examinadas foram anunciadas sem deslocação indevida do foco. |
| Contraste e utilização da cor (1.4.3 e 1.4.1) | Conforme na observação manual | A classificação manual não elimina as 47 ocorrências de contraste insuficiente detectadas automaticamente em oito estados. |
| Reformulação e ampliação (1.4.10 e 1.4.4) | Não conforme | A 400% e com largura equivalente a 320 píxeis CSS, a interface permaneceu apenas parcialmente utilizável. |
| Dimensão mínima dos alvos (2.5.8) | Conforme | Os elementos interactivos examinados apresentaram dimensão ou espaçamento suficiente. |
| Autenticação acessível (3.3.8) | Conforme | A autenticação permitiu colar a palavra-passe e usar um gestor de palavras-passe. |
| Alternativa ao visualizador tridimensional (1.1.1 e 1.3.1) | Não conforme | Com o Orca, o visualizador não foi identificado como imagem nem foi anunciada uma alternativa textual. |
| Percurso com leitor de ecrã | Não conforme | O percurso com o Orca revelou limitações na ordenação e na clareza das descrições dos campos. |

A classificação manual do contraste como conforme descreve apenas a observação efectuada nessa sessão e não substitui a medição automática, que identificou 47 elementos com contraste insuficiente. Como a versão, o ramo e o identificador da revisão da sessão manual não foram registados, os dois resultados são apresentados lado a lado e o contraste permanece uma prioridade de correcção. A avaliação manual complementa a verificação automática, mas não permite emitir uma declaração global de conformidade com as WCAG 2.2 nem substitui avaliação com participantes.

## B.7 Aprendizagens para o *Design* Industrial

1. **A consistência deve ser demonstrada na cadeia completa.** A igualdade entre ficheiros concluídos é útil, mas deve ser acompanhada pela taxa de conclusão e pela qualidade da geometria produzida.
2. **Os limites devem ser visíveis e actuar em todas as etapas.** Não basta limitar um cursor se o valor puder ser aceite ou aplicado por outro percurso.
3. **A recuperação protege a continuidade do trabalho de projecto.** Preservar a última configuração válida, explicar a falha e permitir nova tentativa reduz a perda de trabalho durante a exploração de alternativas.
4. **A acessibilidade é uma qualidade concreta da interface.** Contraste, rótulos, foco, nomes acessíveis e alternativas à visualização tridimensional devem ser tratados como requisitos verificáveis.
5. **A compatibilidade não deve ser presumida.** A conclusão em dois navegadores não permite generalizar para todos os ambientes; o percurso incompleto em WebKit deve permanecer como questão aberta.
6. **A IA necessita de limites anteriores à aplicação.** As sugestões podem apoiar a exploração inicial, mas a geometria só deve receber valores já verificados pelas regras determinísticas do modelo.

## B.8 Conclusão

As séries de ensaios fornecem evidência parcial de que o núcleo paramétrico produz resultados consistentes nas execuções concluídas e de que vários estados de erro preservam o trabalho anterior ou permitem recuperação. Também revelam fragilidades concretas na aplicação uniforme dos limites, na aceitação de tipos de dados e na acessibilidade da interface. A verificação manual classificou sete de doze critérios como conformes e cinco como não conformes, acrescentando problemas de ordem e descrição dos campos, reformulação em ampliação elevada e ausência de alternativa textual ao visualizador tridimensional.

O resultado não autoriza afirmar que a plataforma é robusta, acessível ou compatível com todos os navegadores em termos gerais. Autoriza uma formulação mais delimitada: **nos casos examinados, o processo apresentou consistência das geometrias concluídas, recuperou de várias falhas previstas e permitiu identificar prioridades objectivas de revisão da interface e das salvaguardas paramétricas**.

## B.9 Referências normativas

- World Wide Web Consortium. (2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- World Wide Web Consortium. (2014). *Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0*. https://www.w3.org/TR/WCAG-EM/

# Anexo C — Adaptação paramétrica dos modelos de mão protésica

**Índice de tabelas do Anexo C**

| Identificação | Descrição | Página |
| --- | --- | --- |
| Tabela C.1 | Correspondência entre medidas normalizadas e parâmetros dos modelos | 159 |
| Tabela C.2 | Parâmetros numéricos do Flexy Beast com efeito dimensional | 161 |
| Tabela C.3 | Relações dimensionais do Paraglider Hand | 167 |
| Tabela C.4 | Comparação das adaptações e excepções de escala | 172 |
## C.1 Objectivo e âmbito

Este anexo documenta como quatro modelos de mão protésica de origem aberta foram adaptados à estrutura paramétrica da plataforma HandFab: Flexy Beast, Cyborg Beast, Paraglider Hand e UnLimbited Phoenix Hand. O objectivo é tornar explícita a passagem entre medidas antropométricas, parâmetros configuráveis, relações geométricas e malhas destinadas à preparação para fabrico.

O anexo descreve o que está efectivamente implementado nos ficheiros de configuração e nos modelos OpenSCAD. Não apresenta as relações como regras anatómicas universais. Os intervalos declarados delimitam o espaço de configuração do protótipo e não constituem limites clínicos. Do mesmo modo, a geração de uma geometria coerente ou imprimível não demonstra ajuste individual, conforto, função, segurança ou eficácia protésica.

O estado final examinado corresponde a 14 de Julho de 2026. Uma revisão imediatamente anterior integrou a braçadeira revista do Flexy Beast e alterou o dicionário usado nos ensaios principais: os antigos parâmetros de largura, comprimento e parede da braçadeira foram substituídos por circunferência do punho, inclinação, multiplicador de comprimento e furos de correia. O estado final examinado uniformizou a organização dos grupos e os nomes dos controlos equivalentes, sem modificar as relações geométricas descritas neste anexo.

## C.2 Princípio comum de adaptação

Os modelos herdados não partilhavam nomes de parâmetros, mecanismos de escala ou formas equivalentes de preservar interfaces mecânicas. A adaptação não consistiu, portanto, em aplicar uma única fórmula a todas as mãos. Consistiu em criar uma gramática comum de entrada e, depois, manter uma transformação específica para cada arquitectura.

O percurso comum compreende cinco etapas:

1. uma medida individual, uma referência populacional ou um valor introduzido manualmente é expresso em milímetros;
2. o nome anatómico é associado a um campo canónico reconhecido pela plataforma;
3. o campo só é aplicado quando existe no modelo seleccionado e contém um valor numérico positivo;
4. o valor é limitado ao intervalo declarado na configuração quando provém do mapeamento de perfis;
5. o ficheiro OpenSCAD transforma os valores aceites segundo as relações próprias do modelo e gera a geometria.

![Fluxo de adaptação paramétrica dos modelos](figuras/figura_c1_fluxo_adaptacao_parametrica.png)

Figura C.1 — Fluxo entre dados de entrada, mapa comum, regras específicas dos modelos e geometria exportável. Produção própria.

### C.2.1 Campos antropométricos comuns

O serviço `profileMapping.js` estabelece as correspondências apresentadas na Tabela C.1. A origem é a árvore normalizada `profile.measurements`; o vector `geometry_parameters` produzido pelo importador não é utilizado nesta passagem porque foi concebido para outra organização geométrica e não partilha os nomes dos modelos activos.

Tabela C.1 — Correspondência entre medidas normalizadas e parâmetros dos modelos

| Parâmetro da plataforma | Medida de origem | Aplicação |
| --- | --- | --- |
| `palm_breadth_mm` | `palm.width_mm` | Largura metacarpal usada na escala da palma ou da mão |
| `palm_length_mm` | `palm.length_mm` | Comprimento da palma; só tem efeito geométrico quando o modelo o utiliza |
| `palm_thickness_mm` | `palm.thickness_mm` | Espessura da palma; só tem efeito geométrico quando o modelo o utiliza |
| `index_finger_length_mm` | `digits.index.total_length_mm` | Comprimento total do indicador |
| `middle_finger_length_mm` | `digits.middle.total_length_mm` | Comprimento total do dedo médio |
| `ring_finger_length_mm` | `digits.ring.total_length_mm` | Comprimento total do anelar |
| `pinky_finger_length_mm` | `digits.pinky.total_length_mm` | Comprimento total do mindinho |
| `thumb_length_mm` | `digits.thumb.total_length_mm` | Comprimento total do polegar |
| `*_base_length_mm` | `digits.*.proximal_length_mm` | Comprimento do segmento proximal quando o modelo expõe esta divisão |
| `wrist_circumference_mm` | `wrist.circumference_mm` | Dimensionamento da braçadeira nos modelos que aceitam esta medida |

Uma medida em falta não é interpolada automaticamente: o campo é omitido e conserva o valor corrente ou fica disponível para introdução manual. Os valores válidos são arredondados a uma casa decimal. O mapeamento limita-os ao mínimo e máximo declarados no catálogo de modelos e regista as limitações aplicadas. Os parâmetros mecânicos, as cores, a visibilidade e a lateralidade não são preenchidos a partir das medidas corporais.

Quando a entrada é uma descrição livre, a plataforma pode seleccionar uma referência populacional com base numa pontuação baseada em sexo, categoria etária, proximidade da idade, país e qualidade descritiva do grupo. O perfil só é seleccionado quando a pontuação atinge três. Esta regra escolhe um ponto de partida; não mede proximidade anatómica entre populações e não substitui uma medida individual.

### C.2.2 Tipos de parâmetros

Para efeitos de projecto, os parâmetros foram organizados em quatro classes:

- **directos:** medidas ou decisões introduzidas no modelo, como largura metacarpal, comprimento de um dedo ou diâmetro de um pino;
- **derivados:** resultados calculados a partir de entradas, como factores de escala, proporções entre dedos ou deslocamentos de segmentos;
- **fixos:** constantes herdadas ou calibradas que preservam a geometria-base e as interfaces mecânicas;
- **contextuais:** campos presentes na plataforma, mas sem transformação geométrica activa no modelo em causa.

Esta separação é necessária porque o nome de um campo não garante, por si só, que a dimensão final da malha coincida numericamente com o valor introduzido. A transformação depende da geometria-base, da ordem das escalas e das restrições herdadas.

### C.2.3 Coerência dos controlos no estado final examinado

O estado final examinado aplicou aos quatro modelos a mesma sequência de grupos quando estes existem: componente, antropometria, divisão de segmentos, componentes mecânicos, braçadeira, opções, visibilidade, cores e braço. Esta organização não acrescenta parâmetros nem demonstra melhoria de utilização; reduz diferenças de apresentação entre modelos e torna mais previsível a localização de decisões equivalentes.

Foram igualmente uniformizados dois nomes. O Phoenix passou de `LeftRight` para o campo booleano `mirrored`, já usado pelos restantes modelos. No Paraglider, `show_assembled` passou a `print_layout`, invertendo a formulação para coincidir com o controlo usado no Cyborg e no Phoenix: `true` corresponde à disposição plana destinada à exportação. Estas alterações incidem na correspondência entre os campos da configuração e os controlos da interface; não alteram a escala da palma, os comprimentos digitais ou as interfaces mecânicas.

## C.3 Flexy Beast

### C.3.1 Origem e estratégia de adaptação

O Flexy Beast deriva do trabalho de `daprice`, que combina o Parametric Cyborg Beast com o Flexy Hand. O ficheiro-fonte local indica licença CC BY-SA 4.0. O modelo usa uma palma da linhagem Cyborg Beast e segmentos digitais ligados por conectores flexíveis. A adaptação procurou separar três dimensões: escala da mão, comprimentos relativos dos dedos e braçadeira do antebraço.

### C.3.2 Entradas, limites e relações

Tabela C.2 — Parâmetros numéricos do Flexy Beast com efeito dimensional

| Família | Parâmetros e unidade | Valor inicial | Intervalo declarado | Relação implementada |
| --- | --- | ---: | --- | --- |
| Palma | `palm_breadth_mm` (mm) | 83 | 55–110 | `xScaleFactor = (palm_breadth_mm + 5) / 55`; os três eixos da mão usam o mesmo factor |
| Dedos | `middle_finger_length_mm` (mm) | 72 | 40–120 | `fingerLength = middle_finger_length_mm / (37 × xScaleFactor)` |
| Dedos | indicador e anelar (mm) | 68; 68 | 40–120 | proporção local = comprimento do dedo / comprimento do médio |
| Dedos | mindinho e polegar (mm) | 55; 65 | 30–100; 35–100 | proporção local = comprimento do dedo / comprimento do médio |
| Juntas | `joint_dia`; `joint_thick` (mm) | 7; 4 | 4–10; 1–6 | diâmetro do furo e espessura da ranhura do conector flexível |
| Braçadeira | `wrist_circumference_mm` (mm) | 160 | 110–260 | profundidade da braçadeira derivada de circunferência/π mais 6 mm |
| Braçadeira | `gauntlet_tilt` (graus) | 0 | −10–40 | rotação da braçadeira em torno do eixo do pino do punho |
| Braçadeira | `gauntlet_length_scale` (razão) | 0,7 | 0,7–1,5 | multiplicador do comprimento nativo reconstruído |
| Braçadeira | `gauntlet_rim_hole_d` (mm) | 2,5 | 1,5–6 | diâmetro dos furos de correia no rebordo |
| Punho | `wrist_pin_dia`; `wrist_pin_clearance` (mm) | 7; 0,35 | 4–10; 0,10–0,80 | furo da braçadeira = diâmetro do pino + 2 × folga |

O alcance de referência dos segmentos digitais é 37 mm à escala unitária, formado pelos valores nativos de 20 mm para a base e 17 mm para a ponta. O comprimento do dedo médio define o multiplicador mestre; os restantes dedos recebem uma proporção face ao médio. Esta transformação permite variar os comprimentos digitais sem obrigar a largura da palma a aumentar na mesma proporção.

Os conectores flexíveis são derivados das interfaces mecânicas: a parede em torno do furo é fixada em 1,2 mm; o raio do lóbulo é `joint_dia / 2 + 1,2`; a espessura da ponte corresponde a `joint_thick`; o comprimento ao longo do pino é `9,5 × xScaleFactor`; e a distância entre centros dos lóbulos é `8 × xScaleFactor`. Estes valores descrevem a geometria codificada e não resultam de um ensaio material nesta investigação. As juntas flexíveis não foram produzidas nos protótipos físicos.

### C.3.3 Braçadeira e interfaces confirmáveis

O estado final reutiliza uma braçadeira reconstruída a partir da geometria de referência da braçadeira normal com tensionador. A forma orgânica principal está incorporada como malha poligonal reduzida; os furos mecânicos são novamente abertos de forma paramétrica. A largura nativa medida é 49,88 mm e os centros dos furos das abas situam-se em `X = ±22,6`, `Y = −58,3` e `Z = −9,8` mm no referencial da peça.

As relações principais são:

```text
g_hinge = (26,6 − 2,6) / 22,6
g_depth = (wrist_circumference_mm / π + 6) / (49,88 × xScaleFactor)
g_pin_bore = wrist_pin_dia + 2 × wrist_pin_clearance
```

O factor `g_depth` inclui a divisão por `xScaleFactor` porque a braçadeira volta a ser envolvida pela escala da mão na montagem. Desta forma, a profundidade impressa procura permanecer dependente da circunferência do punho e não da largura da palma. A posição é recalculada para fazer coincidir os furos das abas com o eixo do pino da palma, identificado no código por `Y = −27` e `Z = 5,5` mm.

O código confirma espessuras locais de 3,2 mm na zona dos furos médios e 5 mm nas zonas dos furos do pino e do rebordo. Não confirma uma espessura uniforme da casca orgânica nem uma tolerância de fabrico validada para toda a braçadeira. A folga de 0,35 mm é um valor configurável de projecto; não foi estabelecida por ensaio sistemático de montagem.

### C.3.4 Exemplo de propagação já preservado

O percurso numérico do perfil de ensaio de oito anos — valores aplicados, factores derivados e métricas de três malhas — encontra-se preservado no Suplemento 3 — Parametrização e percurso numérico. Para evitar duplicação, este anexo não repete a Tabela 4.10 nem os 42 registos do dicionário histórico. Acrescenta apenas a alteração posterior da braçadeira e os casos que expõem dependências ainda não descritas nesse suplemento.

O resultado central desse percurso continua a ser pertinente: `palm_breadth_mm` alimenta uma fórmula herdada e não define directamente a extensão transversal da malha. O caso documenta a propagação do valor; não demonstra correspondência anatómica.

### C.3.5 Limitações específicas

- a palma continua a usar escala uniforme;
- os comprimentos digitais controlam relações de alcance, mas não definem independentemente largura ou espessura dos dedos;
- a espessura integral da braçadeira não é um parâmetro no estado final examinado;
- os conectores flexíveis e a folga do punho carecem de ensaios materiais e de montagem;
- a configuração não contém afirmações `assert()` suficientes para impedir todas as combinações inválidas quando os valores são introduzidos fora da interface.

## C.4 Cyborg Beast

### C.4.1 Origem e estratégia de adaptação

O Cyborg Beast local preserva a palma e os segmentos digitais da linhagem MakerBlock/e-NABLE e acrescenta uma camada antropométrica, divisão proximal–distal, braçadeira dimensionada pelo punho, revestimento termoformável e disposição das peças para impressão. A licença não está explicitada no pacote local examinado; esta ausência documental deve permanecer indicada até ser confirmada na fonte original.

### C.4.2 Entradas e escala da mão

Os seis parâmetros principais de palma e dedos usam os mesmos valores iniciais e intervalos do Flexy Beast. A escala global é:

```text
overall_scale = (palm_breadth_mm + 5) / 55
```

Ao contrário do Flexy Beast, o comprimento de cada dedo é obtido através da inversão de curvas de alcance calibradas sobre a geometria original. A curva total usa 60,85 mm como alcance de referência local e duas inclinações: 1,584 para valores positivos da alavanca `len` e 1,328 para valores negativos. A alavanca é limitada ao intervalo interno de −22 a 50 para evitar extensões que o modelo classifica como inseguras para a geometria.

### C.4.3 Divisão proximal–distal

Os valores iniciais dos segmentos proximais são 22, 24, 22 e 16 mm para indicador, médio, anelar e mindinho; os intervalos são 12–60 mm nos três primeiros e 10–55 mm no mindinho. O polegar inicia em 27 mm, com intervalo 12–45 mm.

Para os quatro dedos, a transformação é:

```text
alcance_proximal_local(lp) = 23 + (2/3) × lp
lp = limitar((((base_mm / overall_scale) − 23) / (2/3)), −22, 50)
alcance_distal_de_referência = 60,85 − 23 = 37,85
ld = inversão da curva distal para preencher total_mm − base_mm
```

O segmento distal preenche o comprimento que resta depois do proximal, usando a inclinação correspondente ao sinal da alavanca. O posicionamento da ponta é igualmente deslocado para manter o eixo PIP coincidente.

No polegar, a relação foi ajustada por renderização sobre uma grelha de valores:

```text
alcance_local = 55,84 + 0,6185 × lp + 0,77 × ld
deslocamento da junção = −(23,667 + lp/3 + ld/3)
```

O código declara um resíduo máximo de 0,74 mm para este ajuste. Trata-se de uma calibração geométrica da implementação, não de um modelo anatómico do polegar.

### C.4.4 Braçadeira, folgas e parâmetros fixos

A braçadeira partilha a lógica descrita para o Flexy Beast. Recebe `wrist_circumference_mm` entre 110 e 260 mm, inclinação entre −10° e 40°, multiplicador de comprimento entre 0,7 e 1,5, diâmetro de pino entre 4 e 10 mm, folga entre 0,10 e 0,80 mm e furos de correia entre 1,5 e 6 mm. O furo resultante usa `wrist_pin_dia + 2 × wrist_pin_clearance`.

As constantes de referência da palma incluem raio de nó de 4,85 mm, altura do punho de 10 mm, altura da palma de 20 mm, largura-base de 64 unidades e espessura `th = 3`. Estes valores são herdados ou calibrados no modelo e não estão expostos como medidas antropométricas.

### C.4.5 Exemplo de propagação

Com largura da palma de 83 mm, comprimento do dedo médio de 72 mm e segmento proximal de 24 mm:

```text
overall_scale = (83 + 5) / 55 = 1,6
lp = ((24 / 1,6) − 23) / (2/3) = −12
alcance proximal impresso = 1,6 × [23 + (2/3) × (−12)] = 24 mm
ld ≈ −11,86996
alcance distal impresso = 48 mm
comprimento total calculado = 24 + 48 = 72 mm
```

O exemplo confirma a coerência interna das equações para esta configuração. A correspondência entre o alcance calculado e uma medição corporal teria de ser verificada num protocolo dimensional próprio.

### C.4.6 Limitações específicas

- as curvas dos dedos foram calibradas sobre a geometria original e não sobre uma amostra de mãos;
- o limite interno das alavancas pode impedir que combinações extremas atinjam exactamente o comprimento pedido;
- a calibração do polegar apresenta erro residual declarado;
- o revestimento termoformável é uma possibilidade construtiva, não uma interface corporal avaliada;
- o Cyborg Beast não integrou a comparação dimensional, os projectos de preparação ou as séries físicas descritas no estudo principal.

## C.5 Paraglider Hand

### C.5.1 Origem e estratégia de adaptação

O Paraglider Hand, também identificado como Flexible Flyer, deriva do trabalho de Marcus Mendenhall e encontra-se localmente associado à licença CC BY-SA 4.0. O conjunto integra ainda dependências das linhagens Reborn Hand e UnLimbited Arm com licenças próprias. A adaptação teve de conciliar duas exigências: permitir variação digital por dedo e manter a palma sob escala uniforme para não deformar os furos dos pinos.

### C.5.2 Relações implementadas

Tabela C.3 — Relações dimensionais do Paraglider Hand

| Entrada | Inicial; intervalo | Transformação ou estado |
| --- | --- | --- |
| `palm_breadth_mm` | 83; 55–110 mm | `overall_scale = palm_breadth_mm / 66,4` |
| `palm_length_mm` | 95; 60–140 mm | campo contextual; não deforma a palma de modo independente |
| `palm_thickness_mm` | 32; 18–50 mm | campo contextual; não deforma a palma de modo independente |
| `middle_finger_length_mm` | 72; 40–120 mm | `global_scale = valor / 57,6` |
| indicador e anelar | 68; 40–120 mm | escala própria = valor / 57,6 |
| mindinho | 55; 30–100 mm | escala própria = valor / 57,6 |
| `thumb_length_mm` | 65; 35–100 mm | campo disponível, mas o polegar usa actualmente `global_scale` |
| `string_channel_scale` | 0,9; 0,5–1,0 | razão aplicada ao canal de tracção |
| `elastic_channel_scale` | 0,9; 0,5–1,5 | razão aplicada ao canal de retorno |

A palma Reborn continha internamente `overall_scale = 1,25`. Como o módulo é carregado por `use`, esse valor permanecia no âmbito do ficheiro de origem e ignorava a escala calculada no modelo principal. A correcção foi aplicada no ponto de chamada:

```text
scale(overall_scale / 1,25) × scaled_palm()
```

O módulo continua a aplicar internamente 1,25; o efeito líquido passa a ser `palm_breadth_mm / 66,4`. A variante UnLimbited V3 não exigiu a mesma correcção porque é carregada por `include` e recebe a escala do ficheiro principal.

Os dedos indicador, anelar e mindinho recebem uma razão própria em relação a `global_scale`. O médio define a escala-base dos módulos `fingerator`. No estado examinado, o polegar também usa essa escala-base; `thumb_length_mm` é apresentado e pode ser preenchido pelo perfil, mas não controla autonomamente a geometria do polegar. Esta discrepância deve ser corrigida no modelo ou explicitada na especificação dos parâmetros.

### C.5.3 *Hardware* e limites confirmáveis

O selector `pin_index` escolhe entre quatro famílias de pino. Os diâmetros nominais usados no código são 3,1 mm para parafuso de 3 mm, 1,5875 mm para pino de 1/16", aproximadamente 2,413 mm para prego de calibre 13 e 1,5875 mm para pino de 1/16" sem chumaceira. O código define ainda folga nominal de 0,5 mm para a aba, profundidade de bolso de chumaceira de 0,4 mm e acréscimos locais de 0,25 ou 0,3 mm em algumas interfaces.

Estes valores são constantes ou opções de *hardware*. Não foram comparados com medições sistemáticas das peças impressas. A activação dos canais de cordão e de elástico acrescenta operações geométricas demoradas; a pré-visualização mantém esses canais desligados por omissão. Uma malha sem canais não representa, por isso, uma peça funcionalmente completa.

Os parâmetros `ARM_HandLen`, `ARM_ForearmLen`, `ARM_BicepCircum`, `ARM_CuffLength` e `ARM_PinHoleDia` pertencem à extensão opcional do braço. Não participaram na comparação da mão isolada e não devem ser apresentados como dados testados nos ensaios principais.

### C.5.4 Exemplo de propagação

Com largura da palma de 64 mm, dedo médio de 60 mm, indicador e anelar de 57 mm, mindinho de 46 mm e polegar declarado com 50 mm:

```text
overall_scale = 64 / 66,4 = 0,963855
correcção no ponto de chamada Reborn = 0,963855 / 1,25 = 0,771084
efeito líquido da palma = 1,25 × 0,771084 = 0,963855
global_scale do médio = 60 / 57,6 = 1,041667
escala do indicador = 57 / 57,6 = 0,989583
escala do anelar = 57 / 57,6 = 0,989583
escala do mindinho = 46 / 57,6 = 0,798611
escala actualmente aplicada ao polegar = 1,041667
```

O último valor mostra que os 50 mm declarados para o polegar não são propagados como escala própria. O exemplo deve ser tratado como diagnóstico de uma limitação, não como prova de correspondência individual.

### C.5.5 Limitações específicas

- a palma é escalada uniformemente por decisão mecânica;
- comprimento e espessura da palma são contextuais;
- o parâmetro de comprimento do polegar não tem transformação geométrica independente;
- a geometria completa dos canais pode exigir tempos de cálculo superiores e deve ser activada na exportação funcional;
- a extensão de braço contém parâmetros fora do âmbito dos ensaios da mão;
- as malhas avaliadas revelaram corpos abertos ou faces degeneradas em algumas peças, pelo que a aceitação pelo programa de preparação não equivale a sólido geometricamente válido.

## C.6 UnLimbited Phoenix Hand

### C.6.1 Origem e estratégia de adaptação

O UnLimbited Phoenix Hand local deriva da equipa UnLimbited/e-NABLE e indica licença CC BY-NC-SA 4.0 no ficheiro-fonte. A geometria herdada é composta sobretudo por malhas e poliedros de dimensão fixa. A adaptação preservou essas zonas e acrescentou duas formas de variação: uma escala uniforme para o conjunto e um alongamento localizado dos segmentos digitais em faixas sem furos.

### C.6.2 Escala global e limite dimensional mínimo

A largura de referência da palma é 82 mm. A percentagem de escala é:

```text
se HandPerc_override > 0:
    HandPerc = limitar(HandPerc_override, 100, 160)
caso contrário:
    HandPerc = limitar((palm_breadth_mm / 82) × 100, 100, 160)
```

`palm_breadth_mm` é declarado entre 82 e 131 mm. O parâmetro manual `HandPerc_override` aceita zero como instrução para derivar a escala; valores positivos ficam sujeitos ao mesmo limite mínimo de 100% e ao limite máximo de 160%. Um perfil com palma inferior a 82 mm produz o tamanho mínimo do modelo, não a medida pedida. A configuração deve ser rejeitada ou acompanhada por um aviso de cobertura, em vez de ser descrita como adaptação individual.

### C.6.3 Comprimentos digitais e preservação dos furos

Os quatro dedos iniciam com 72 mm de comprimento total e 31 mm de segmento proximal. Os comprimentos totais variam entre 55 e 115 mm e os proximais entre 18 e 55 mm. O polegar também parte de 72 e 31 mm, com intervalos respectivos de 45–80 e 18–50 mm.

O modelo usa as referências locais de 31 mm para o proximal e 41 mm para o distal:

```text
bd = base_length_mm − 31
td = (finger_length_mm − base_length_mm) − 41
```

A função `stretch_shaft()` divide a malha em três zonas. A zona da dobradiça mantém-se fixa, uma faixa sem furos é alongada ou encurtada, e a extremidade oposta é deslocada pelo mesmo valor. No proximal, a faixa usada situa-se entre Y = 20 e Y = 42; no distal, entre Y = −48 e Y = −14. Assim, as zonas dos furos não recebem escala não uniforme e conservam a secção circular.

### C.6.4 Dependência entre comprimento digital e escala global

Depois do alongamento local, toda a montagem é envolvida por `scale(HandPerc/100)`. Consequentemente, os parâmetros digitais não correspondem necessariamente ao comprimento final impresso quando `HandPerc` é diferente de 100%. O resultado depende de duas operações sucessivas: alteração local do segmento e escala uniforme do conjunto.

Esta ordem é relevante para a interpretação dos nomes `*_finger_length_mm`. A documentação interna que descreve uma alteração de 1:1 só é confirmável à escala de 100%. Para outras larguras de palma, deve ser medida a malha resultante ou reformulada a transformação para compensar a escala global.

### C.6.5 Exemplo de propagação

Para um dedo médio de 100 mm, segmento proximal de 40 mm e palma de 82 mm:

```text
HandPerc = 100%
bd = 40 − 31 = 9 mm
td = (100 − 40) − 41 = 19 mm
comprimento local nominal = 72 + 9 + 19 = 100 mm
```

Se se mantiverem os mesmos valores digitais e a largura da palma passar a 100 mm:

```text
HandPerc = (100 / 82) × 100 = 121,951%
comprimento local nominal antes da escala = 100 mm
comprimento nominal após a escala global ≈ 121,951 mm
```

O segundo cálculo não substitui uma medição da caixa envolvente ou do trajecto MCP–ponta, mas demonstra que o valor digital é novamente afectado pela escala global.

### C.6.6 Componentes fixos e tolerâncias confirmáveis

Os pinos, o bloco tensor e os pinos do tensor foram reconstruídos a partir de medições do ficheiro STEP e permanecem como componentes fixos. Os ficheiros contêm raios e posições medidos para cada corpo, mas não existe um parâmetro global de folga nem um ensaio dimensional consolidado que permita declarar tolerâncias de montagem. A escala uniforme da montagem também afecta estes componentes.

A reconstrução mantém a circularidade dos furos durante o alongamento local dos dedos. Esta propriedade geométrica não demonstra que a folga final entre pino e furo seja adequada depois da impressão, do material e da escala escolhida.

### C.6.7 Limitações específicas

- a palma não desce abaixo do tamanho de referência de 82 mm;
- os comprimentos digitais são afectados pela escala global;
- as zonas dos furos são preservadas, mas a folga física não foi medida de forma sistemática;
- os componentes de *hardware* permanecem associados à arquitectura original e são escalados com o conjunto;
- algumas malhas originais apresentaram descontinuidades; a reparação ou aceitação pelo programa de preparação deve ser distinguida da validade geométrica do sólido.

## C.7 Síntese comparativa das estratégias

Tabela C.4 — Comparação das adaptações e excepções de escala

| Modelo | Escala da palma | Variação dos dedos | Interface preservada | Limitação principal |
| --- | --- | --- | --- | --- |
| Flexy Beast | uniforme, pela fórmula Cyborg Beast | proporções próprias face ao médio | furos e ranhuras dos conectores; eixo do punho | campo de largura da palma não coincide directamente com a extensão da malha |
| Cyborg Beast | uniforme, pela fórmula Cyborg Beast | curvas calibradas e divisão proximal–distal | eixos MCP/PIP; abas e pino da braçadeira | curvas internas e limites de alavanca não são relações anatómicas universais |
| Paraglider Hand | uniforme para preservar furos | escalas próprias para quatro dedos; polegar ainda dependente do médio | furos cilíndricos dos pinos | comprimento do polegar e dimensões independentes da palma não estão plenamente propagados |
| UnLimbited Phoenix | uniforme, 100%–160% | alongamento de faixas sem furos | zonas de dobradiça e furos | comprimentos digitais voltam a ser afectados pela escala global |

A crítica ao escalonamento uniforme continua válida quando este é usado como substituto de todas as diferenças antropométricas. Nos modelos estudados, porém, a escala uniforme foi mantida localmente sempre que a arquitectura herdada dependia de furos circulares, espaçamentos ou componentes montados como conjunto. A decisão de projecto não foi eliminar toda a escala uniforme, mas limitar o seu alcance e acrescentar parâmetros locais onde a geometria o permitia.

Esta solução produz níveis diferentes de adaptação. O Flexy Beast e o Cyborg Beast separam largura da mão, comprimentos digitais e braçadeira; o Paraglider separa a escala da palma de parte dos comprimentos digitais; o Phoenix preserva a escala global e introduz alongamentos localizados. Os quatro modelos não são, por isso, intercambiáveis nem oferecem o mesmo grau de configuração.

## C.8 Critérios de aceitação, limitação e rejeição

Uma configuração pode avançar para geração quando os campos necessários existem, os valores são numéricos positivos e permanecem nos intervalos declarados. Deve ser marcada como limitada quando uma entrada é fixada no limite mínimo do modelo, quando um campo é apenas contextual ou quando a transformação não produz uma correspondência directa entre valor e dimensão final.

Devem impedir a passagem directa para fabrico, ou exigir revisão técnica, as seguintes situações:

- perfil fora da gama dimensional do modelo;
- comprimento proximal igual ou superior ao comprimento total do dedo;
- alteração que faça um valor interno atingir os limites de uma alavanca calibrada;
- ausência de componentes necessários à função, como juntas flexíveis ou canais de tracção;
- malha aberta, não estanque ou com faces degeneradas sem justificação construtiva;
- folga ou espessura sem confirmação para a combinação de material, impressora e orientação;
- valor que chega ao modelo fora do intervalo declarado por contornar a interface.

O estado actual não aplica todas estas condições como bloqueios automáticos dentro de cada ficheiro OpenSCAD. Algumas estão representadas por limites da interface, outras por funções `min`/`max`, e outras permanecem como critérios de revisão. A distinção deve ser mantida no texto da dissertação.

## C.9 Relação com o Suplemento 3

O Suplemento 3 — Parametrização e percurso numérico preserva um estado histórico útil: contém 42 parâmetros numéricos dos três modelos comparados e um percurso do perfil de ensaio até a três malhas do Flexy Beast. Deve, contudo, ser identificado como fotografia do estado usado nesses ensaios.

Depois desse estado, a estrutura paramétrica da braçadeira do Flexy Beast foi alterada. Por esse motivo, `gauntlet_width_mm`, `gauntlet_length_mm`, `gauntlet_wall_mm`, `gauntlet_pos_adjust` e `strap_splay_adjust` não descrevem o estado final examinado. Foram substituídos, no essencial, por `wrist_circumference_mm`, `gauntlet_tilt`, `gauntlet_length_scale`, `gauntlet_rim_hole_d` e uma colocação automática sobre o eixo do pino. O presente anexo acompanha esse estado histórico com esta nota de evolução.

## C.10 Limite de interpretação

As adaptações mostram como modelos abertos e heterogéneos podem ser reorganizados em torno de um conjunto comum de medidas e controlos. O contributo é técnico e de projecto: explicita decisões, dependências, excepções e fragilidades que ficam ocultas quando uma prótese é tratada apenas como um ficheiro STL escalável.

Não se conclui que as geometrias sejam anatomicamente adequadas a uma pessoa, que os intervalos sejam clinicamente seguros ou que as folgas assegurem montagem e funcionamento. Essas conclusões exigem medidas individuais, calibração dimensional, ensaios de fabrico, avaliação funcional e participação de profissionais e utilizadores.

## C.11 Fontes técnicas consultadas

- relatório técnico de adaptação antropométrica da plataforma;
- catálogo de configuração dos modelos;
- serviços de correspondência e importação de perfis antropométricos;
- implementações OpenSCAD activas das famílias Flexy Beast, Cyborg Beast,
  Paraglider Hand e UnLimbited Phoenix, incluindo as dependências de montagem;
- dicionário integral de parâmetros e percurso numérico do perfil de ensaio,
  conservados no Suplemento 3 — Parametrização e percurso numérico;
- Capítulo 4 do manuscrito consolidado;
- relatório integral de revisão académica.

## C.12 Verificações executadas

- comparação dos quatro modelos registados com os parâmetros do catálogo;
- leitura das fórmulas e constantes nos ficheiros OpenSCAD activos;
- confronto entre o Suplemento 3 e o estado final examinado;
- confirmação do mapa entre medidas normalizadas e nomes dos parâmetros;
- recálculo independente dos exemplos numéricos apresentados nas secções C.3 a C.6;
- verificação dos valores inicial, mínimo, máximo e incremento declarados;
- pesquisa de parâmetros contextuais sem efeito geométrico confirmado;
- identificação das relações que permanecem sem calibração dimensional ou ensaio físico.

# Anexo D — Preparação para fabrico e verificação dos protótipos

**Índice de tabelas do Anexo D**

| Identificação | Descrição | Página |
| --- | --- | --- |
| Tabela D.1 | Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada | 179 |
| Tabela D.2 | Estimativas de preparação para impressão na condição digital comum | 180 |
| Tabela D.3 | Comparação dimensional da palma no eixo X em PLA e PETG | 182 |

## D.1 Finalidade

Este anexo reúne evidência verificável sobre a **preparação para impressão** das
mãos protésicas paramétricas geradas pela plataforma HandFab, no contexto de uma
dissertação de ***Design*** **e Desenvolvimento de Produto**. O objectivo não é
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
- **A verificação de malha é geométrica, não mecânica.** «Estanque/*manifold*» e
  «faces degeneradas» descrevem a integridade do ficheiro 3D; não são medida da
  robustez do objecto impresso.
- **As estimativas dependem da versão e do perfil.** Trocar de versão do programa,
  de perfil de processo ou de *firmware* altera os números.

As estimativas de tempo, material, volume e custo devem, pois, ser lidas como
**indicadores comparativos de exigência de preparação**, e não como propriedades
físicas do produto final. Esta restrição não abrange os valores dimensionais da
Secção D.4.4, que correspondem a medições das palmas impressas.

## D.3 Variáveis, controlos e materiais

Foram conduzidas duas séries de ensaios complementares. Os projectos, as condições
de preparação e os resultados completos encontram-se no Suplemento 4 — Preparação
para impressão e protótipos.

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
**não** representa uma impressão física nem confirma que o modelo possa ser impresso com sucesso.

Na análise geométrica, `n_corpos` designa o número de objectos de malha encontrados
no recipiente 3MF, e não uma contagem de componentes topológicos desligados. Uma
face foi classificada como degenerada quando a sua área era inferior a 10⁻⁹ mm².
A estanquidade foi examinada pela correspondência das arestas orientadas, sem
fusão prévia de vértices coincidentes. Estes resultados descrevem, portanto, a
codificação geométrica dos ficheiros e devem ser interpretados em conjunto com o
resultado da preparação para impressão.

## D.4 Resultados

Os resultados quantitativos completos e os registos geométricos encontram-se no
Suplemento 4 — Preparação para impressão e protótipos.

### D.4.1 Série A

Tabela D.1 — Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada

| Modelo e perfil | Material | Equipamento | Configuração | Tempo estimado | Material e custo estimados |
|---|---|---|---|---:|---:|
| Flexy Beast — `teen_15` | PLA | Bambu Lab A1; bico 0,4 mm | Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica | 2 h 21 min 50 s | 18 645,87 mm; 56,51 g; 2,05 € |
| UnLimbited Phoenix — `teen_15` | PLA | Bambu Lab A1; bico 0,4 mm | Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica | 5 h 12 min 44 s | 40 756,68 mm; 123,52 g; 4,48 € |
| UnLimbited Phoenix — `teen_15` | PETG | Bambu Lab A1; bico 0,4 mm | Camada 0,24 mm; enchimento 15%, grelha; suportes em árvore orgânica | 5 h 51 min 52 s | 39 094,09 mm; 117,54 g; 4,27 € |
| Paraglider Hand — `teen_15` | PLA | Prusa MINI; bico 0,4 mm | Camada 0,20 mm; enchimento 15%, grelha; sem suportes | 2 h 32 min 11 s | 12 727,61 mm; 37,96 g; 1,38 € |

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

| Modelo | Perfil | Tempo estimado | Filamento estimado | Massa estimada | Custo estimado | Placas A1 |
|---|---|---:|---:|---:|---:|---:|
| Flexy Beast | `child_8` | 6 h 39 min 34 s | 27 387,6 mm | 83,00 g | 3,01 € | 1 |
| Flexy Beast | `teen_15` | 9 h 51 min 52 s | 43 180,9 mm | 130,87 g | 4,75 € | 1 |
| Flexy Beast | `adult_28` | 12 h 34 min 14 s | 55 811,9 mm | 169,15 g | 6,14 € | 2 |
| Flexy Beast | `elderly_70` | 10 h 52 min 57 s | 47 602,0 mm | 144,27 g | 5,24 € | 2 |
| Paraglider Hand | `child_8` | 4 h 22 min 47 s | 16 522,2 mm | 50,07 g | 1,82 € | 1 |
| Paraglider Hand | `teen_15` | 6 h 45 min 18 s | 27 695,5 mm | 83,94 g | 3,05 € | 1 |
| Paraglider Hand | `adult_28` | 8 h 55 min 41 s | 38 449,4 mm | 116,53 g | 4,23 € | 1 |
| Paraglider Hand | `elderly_70` | 7 h 09 min 05 s | 29 627,5 mm | 89,79 g | 3,26 € | 1 |
| UnLimbited Phoenix | `child_8` | 7 h 29 min 44 s | 30 673,7 mm | 92,96 g | 3,37 € | 2 |
| UnLimbited Phoenix | `teen_15` | 8 h 30 min 45 s | 36 335,2 mm | 110,12 g | 4,00 € | 2 |
| UnLimbited Phoenix | `adult_28` | 8 h 56 min 20 s | 38 179,8 mm | 115,71 g | 4,20 € | 2 |
| UnLimbited Phoenix | `elderly_70` | 7 h 49 min 09 s | 32 412,0 mm | 98,23 g | 3,56 € | 2 |

Os tempos estimados variaram entre 4 h 22 min (Paraglider, `child_8`) e 12 h
34 min (Flexy Beast, `adult_28`). Nos 12 casos, o programa gerou trajectórias e
estimativas. Contudo, assinalou regiões suspensas nos quatro casos Flexy Beast e
no Paraglider `elderly_70`, uma consequência relevante da política comum sem
suportes. Não foram emitidos avisos nos quatro casos Phoenix. A conclusão do
processamento não demonstra, por si só, que a impressão física possa ser realizada
sem rever a orientação ou activar suportes. Os dados completos — tempo, filamento,
camadas, ocupação por placa e avisos — constam do ficheiro
`resultados_serie_b.csv` do Suplemento 4.

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
confundidas; os valores completos constam do ficheiro
`resultados_geometria.csv` do Suplemento 4:

- **Montagem sólida (mão estendida):** a caixa envolvente do corpo único do modelo
  montado, com dedos e punho estendidos. É o *vão anatómico*.
- **Palma (peça):** a caixa envolvente da palma isolada.
- **Placa disposta:** a área ocupada pelas peças efectivamente colocadas na placa.

Achado central: **na orientação analisada, uma dimensão da caixa envolvente do
modelo montado ultrapassa a dimensão nominal da placa.** O corpo único do Flexy
atinge 259 mm (*teen*), 296 mm (*adult*) e 273 mm (*elderly*), enquanto os conjuntos
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

A Tabela D.3 resume o eixo X; o ficheiro
`comparacao_dimensional_72_medicoes.csv` do Suplemento 4 conserva as 72 linhas
correspondentes aos três eixos. Em todas as medições, a
dimensão física ficou abaixo da extensão da malha. Em PLA, os desvios percentuais
variaram entre −0,321% e −0,274%; em PETG, variaram entre −0,425% e −0,369%.
Estes intervalos descrevem os exemplares medidos e não demonstram uma taxa geral
de contracção dos materiais.

Nos casos Paraglider, os valores `palm_length_mm` e `palm_thickness_mm` são
conservados como contexto do perfil, mas não controlam isoladamente as extensões Y
e Z; no Flexy Beast e no Phoenix não existe, nestas configurações, um parâmetro de
entrada correspondente a esses dois eixos. Esta diferença encontra-se identificada
no campo `estado_parametro` do mesmo ficheiro.

As colunas «Entrada» e «Malha» não representam, em todos os modelos, o mesmo
limite geométrico. No Flexy Beast e no Paraglider, a medida antropométrica alimenta
uma regra de escala aplicada a uma geometria-base cuja extensão total inclui abas,
interfaces e margens para montagem. No Phoenix, a largura de referência coincide
aproximadamente com a extensão X da palma-base, pelo que os valores são próximos.
Assim, a diferença entre entrada e malha descreve a transformação resultante do projecto e não
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

As Figuras 8.1 a 8.3 do manuscrito reúnem o registo fotográfico das peças produzidas: componentes separados e em montagem parcial, séries dimensionais de segmentos Paraglider Hand e Flexy Beast, e sete vistas de uma UnLimbited Phoenix montada para o perfil de ensaio de 15 anos. Os 19 originais encontram-se na subpasta `fotografias_originais/` do Suplemento 4; os painéis apresentados foram compostos sem alteração do conteúdo visual. Três fotografias das séries dimensionais foram apenas rodadas 90° para permitir a leitura correcta da orientação e das identificações manuscritas.

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
limites destas comparações constam do ficheiro `compatibilidade_dimensionamento.md`
do Suplemento 4. Os resultados mostram
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
- **Verificação de montagem e articulação:** a folha contém uma observação da
  UnLimbited Phoenix, correspondente ao perfil de ensaio de 15 anos e produzida
  em PLA. A montagem foi concluída, os pinos foram colocados sem dano ou
  correcção, os cinco dedos apresentaram movimento livre e foram observados o
  fecho por cabo e o retorno. Depois de ensaios repetidos, os elásticos das
  articulações alargaram e tiveram de ser substituídos. Não ficaram registados o
  número exacto de ciclos nem os ensaios com cilindros; por isso, o resultado
  permanece parcial.
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
- Que, num espécime UnLimbited Phoenix correspondente ao perfil de ensaio de 15
  anos e produzido em PLA, a montagem foi concluída e foram observados o movimento
  livre dos cinco dedos, o fecho por cabo e o retorno; os elásticos das articulações
  alargaram durante os ensaios repetidos e tiveram de ser substituídos.

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

![Segmentos de dedos do Flexy Beast na placa da Bambu Lab A1](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-3d-dedos-flexy-beast.jpg)
*Figura D.1 — Segmentos de dedos (falanges) do Flexy Beast dispostos na placa da Bambu Lab A1, no fim da impressão.*

![Falanges sobre a placa texturada da A1](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-09201343.jpg)
*Figura D.2 — Falanges (base e ponta) sobre a placa texturada da A1, antes da remoção.*

![Conjunto de dedos na placa da A1](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-09201338.jpg)
*Figura D.3 — Conjunto de dedos ainda na placa da A1.*

![Conjunto de dedos na placa da A1, tomada alternativa](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-09201340.jpg)
*Figura D.4 — O mesmo conjunto, tomada alternativa.*

### D.9.2 Série dimensional física — o mesmo componente aos quatro perfis

Estas imagens são a contraparte física do escalonamento antropométrico discutido
em D.4.2: o mesmo dedo, impresso aos quatro perfis (8, 15, 28 e 70 anos),
cresce proporcionalmente com a dimensão de entrada.

![Dedos articulados do Flexy Beast aos quatro perfis](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-dedos-flexy-beast-v1.jpg)
*Figura D.5 — Dedos articulados do Flexy Beast impressos aos quatro perfis (8, 15, 28 e 70 anos).*

![Dedos do Flexy Beast aos quatro perfis, tomada alternativa](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-dedos-flexy-beast-v2.jpg)
*Figura D.6 — O mesmo conjunto, tomada alternativa.*

![Dedos do Paraglider Hand aos quatro perfis](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-dedos-paraglider-hand-v1.jpg)
*Figura D.7 — Dedos do Paraglider Hand impressos aos quatro perfis.*

![Falanges distais aos quatro perfis, rotuladas por idade](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-12185320.jpg)
*Figura D.8 — Falanges distais aos quatro perfis, rotuladas por idade.*

![Dedos articulados base+ponta aos quatro perfis](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-12185529.jpg)
*Figura D.9 — Dedos articulados (base + ponta) aos quatro perfis, mostrando o crescimento proporcional.*

![Dedos articulados aos quatro perfis, tomada alternativa](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-12185532.jpg)
*Figura D.10 — O mesmo conjunto, tomada alternativa.*

### D.9.3 Componentes soltos

![Palma impressa, vista dorsal, com padrão de enchimento visível](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-08214912.jpg)
*Figura D.11 — Palma impressa (vista dorsal): visíveis os canais dos dedos e o padrão de enchimento — o mesmo tipo de parâmetro (paredes/enchimento) cuja leitura estrutural qualitativa se discute em D.4.3.*

![Componentes do antebraço/punho impressos](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-08214702.jpg)
*Figura D.12 — Componentes do antebraço/punho (gauntlet), em três exemplares.*

### D.9.4 Mão UnLimbited Phoenix montada (perfil de 15 anos)

![Mão Phoenix montada](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15-anos-13221108.jpg)
*Figura D.13 — Mão UnLimbited Phoenix montada (perfil de 15 anos): palma, dedos, polegar e punho articulados.*

![Mão Phoenix montada, segunda vista](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15-anos-13221111.jpg)
*Figura D.14 — A mesma mão, segunda vista.*

![Mão Phoenix montada com polegar em oposição](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15-anos-13221117.jpg)
*Figura D.15 — A mesma mão, com o polegar em oposição.*

![Mão Phoenix, vista do punho/antebraço](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15-anos-13221145.jpg)
*Figura D.16 — A mesma mão, vista do lado do punho/antebraço.*

![Mão Phoenix montada, vista dorsal segura na mão](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15anos-0008.jpg)
*Figura D.17 — Mão Phoenix montada, vista dorsal.*

![Pormenor da articulação do polegar e charneira dos dedos](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15anos-0010.jpg)
*Figura D.18 — Pormenor da articulação do polegar e da charneira dos dedos.*

![Vista palmar da mão Phoenix com enchimento visível através da palma](sources/manuscript/annexes/testes_preparacao_impressao/figuras/teste-impressao-phoenix-15anos-0012.jpg)
*Figura D.19 — Vista palmar: o padrão de enchimento é visível através da palma, ilustrando o parâmetro de enchimento usado.*

> **Nota sobre orientação das figuras.** As imagens foram integradas na orientação
> em que os seus pixéis se apresentam (todas verticais/corretas na revisão feita).
> Qualquer correcção posterior de orientação deve ser aplicada ao original
> conservado na subpasta `fotografias_originais/` do Suplemento 4, sem alterar a
> referência da figura.
