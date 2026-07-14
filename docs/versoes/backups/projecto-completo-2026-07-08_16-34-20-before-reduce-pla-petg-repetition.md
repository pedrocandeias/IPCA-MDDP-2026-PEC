Projecto completo

Versão do documento:0.4.14

## INTEGRAÇÃO DO DESIGN E DA INTELIGÊNCIA ARTIFICIAL EM PROCESSOS PARAMÉTRICOS PARA O DESENVOLVIMENTO DE PRÓTESES DE MEMBROS SUPERIORES EM IMPRESSÃO 3D.

## Lista de acrónimos

| Acrónimo | Designação/explicação |

| --- | --- |

| 2D | Bidimensional. |

| 3D | Tridimensional. |

| 3DP | 3D Printing; impressão 3D. |

| 3MF | 3D Manufacturing Format; formato de ficheiro para fabrico aditivo. |

| ANSUR | Anthropometric Survey of U.S. Army Personnel; inquérito antropométrico do Exército dos Estados Unidos. |

| API | Application Programming Interface; interface de programação de aplicações. |

| ASTM | American Society for Testing and Materials; organismo internacional de normalização. |

| CAD | Computer-Aided Design; desenho ou projeto assistido por computador. |

| CAM | Computer-Aided Manufacturing; fabrico assistido por computador. |

| CE | Conformité Européenne; marcação europeia de conformidade. |

| CSG | Constructive Solid Geometry; geometria sólida construtiva. |

| CSV | Comma-Separated Values; formato de valores separados por vírgulas. |

| CT | Computed Tomography; tomografia computorizada. |

| DfAM | Design for Additive Manufacturing; design para fabricação aditiva. |

| DINED | Delft Institute of Ergonomics and Design; base de dados antropométrica da TU Delft. |

| DOI | Digital Object Identifier; identificador digital de objeto. |

| EMG | Eletromiografia; registo da atividade elétrica muscular. |

| EU | European Union; União Europeia. |

| EUA | Estados Unidos da América. |

| FA/FdA | Fabricação aditiva. |

| FDA | Food and Drug Administration; agência reguladora dos Estados Unidos para alimentos, medicamentos e dispositivos médicos. |

| FDM | Fused Deposition Modelling; modelação por deposição fundida. |

| FEA | Finite Element Analysis; análise por elementos finitos. |

| FEM | Finite Element Method; método dos elementos finitos. |

| FFF | Fused Filament Fabrication; fabricação por filamento fundido. |

| FFD | Free-Form Deformation; deformação de forma livre. |

| GB/T | Norma nacional recomendada chinesa. |

| HB | Hand Breadth; largura da mão. |

| HCD | Human-Centred Design; design centrado no humano. |

| HGD | Hand Grip Diameter; diâmetro de preensão da mão. |

| HL | Hand Length; comprimento da mão. |

| HTML | HyperText Markup Language; linguagem de marcação de hipertexto. |

| IA | Inteligência Artificial. |

| ICF | International Classification of Functioning, Disability and Health; Classificação Internacional de Funcionalidade, Incapacidade e Saúde. |

| IEEE | Institute of Electrical and Electronics Engineers; associação técnico-científica e entidade editorial/de normalização. |

| ISO | International Organization for Standardization; Organização Internacional de Normalização. |

| JSON | JavaScript Object Notation; formato leve de intercâmbio de dados. |

| JWT | JSON Web Token; token web em formato JSON para autenticação e autorização. |

| LL | Lower Limb; membro inferior. |

| MCP | Metacarpophalangeal; articulação metacarpofalângica. |

| MDR | Medical Device Regulation; Regulamento Europeu dos Dispositivos Médicos. |

| MPT | Matching Person and Technology; modelo de adequação entre pessoa e tecnologia. |

| MRI | Magnetic Resonance Imaging; ressonância magnética. |

| PCA | Principal Component Analysis; análise de componentes principais. |

| PDF | Portable Document Format; formato portátil de documento. |

| PIP | Proximal Interphalangeal; articulação interfalângica proximal. |

| PL | Palm Length; comprimento da palma. |

| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses; diretrizes para reporte de revisões sistemáticas e meta-análises. |

| RTD | Research Through Design; investigação através do design. |

| SD | Standard Deviation; desvio-padrão. |

| SLA | Stereolithography; estereolitografia. |

| SLS | Selective Laser Sintering; sinterização seletiva a laser. |

| SSM | Statistical Shape Modelling; modelação estatística da forma. |

| SQLite | Motor leve de base de dados relacional baseado em SQL, autónomo e incorporável na aplicação. |

| STL | Stereolithography; formato de ficheiro de malha tridimensional usado em impressão 3D. |

| TC | Technical Committee; comité técnico. |

| TRL | Technology Readiness Level; nível de prontidão tecnológica. |

| UCD | User-Centred Design; design centrado no utilizador. |

| UI | User Interface; interface do utilizador. |

| UL | Upper Limb; membro superior. |

| UX | User Experience; experiência do utilizador. |

| WASM | WebAssembly; tecnologia para execução de código compilado no navegador. |

| XAI | Explainable Artificial Intelligence; inteligência artificial explicável. |

## Lista de tabelas

| Identificação | Descrição | Página |
| --- | --- | --- |
| Tabela 2.1 | Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos | 14 |
| Tabela 2.2 | Elementos centrais na configuração da participação em sistemas configuráveis | 34 |
| Tabela 4.1 | Principais parâmetros antropométricos da mão e do membro superior relevantes para modelação paramétrica | 53 |
| Tabela 4.2 | Conjuntos mínimos de parâmetros por nível de amputação | 53 |
| Tabela 4.3 | Métodos de recolha de dados antropométricos e suas características | 55 |
| Tabela 4.4 | Fontes integradas na base local de dados antropométricos | 57 |
| Tabela 4.5 | Estrutura hierárquica dos parâmetros no modelo paramétrico | 61 |
| Tabela 4.6 | Mapeamento entre parâmetros antropométricos e elementos do modelo | 63 |
| Tabela 4.7 | Estrutura técnica em camadas de um modelo paramétrico em OpenSCAD para próteses personalizadas | 65 |
| Tabela 8.1 | Entradas/prompt utilizadas para criação dos perfis de validação antropométrica por IA | 99 |
| Tabela 8.2 | Síntese da validação antropométrica assistida por IA | 102 |
| Tabela 8.3 | Modelos e mecanismos de escala avaliados | 103 |
| Tabela 8.4 | Rácio adimensional da maior dimensão da palma exportada face ao baseline | 103 |

## Lista de figuras

| Identificação | Descrição | Página |
| --- | --- | --- |
| Figura 1.1 | Exemplos de próteses e dispositivos associados à fabricação aditiva em contexto protésico. | 5 |
| Figura 2.1 | Exemplos de próteses de membro superior impressas em 3D, ilustrando diversidade tipológica e construtiva. | 10 |
| Figura 2.2 | Utilização, rejeição primária e rejeição secundária de próteses do membro superior adquiridas. | 12 |
| Figura 2.3 | Fluxo digital entre aquisição, CAD/CAM e fabricação aditiva em próteses e ortóteses. | 17 |
| Figura 2.4 | Exemplo de configurador digital para personalização de uma prótese impressa em 3D. | 20 |
| Figura 2.5 | Marcos anatómicos e medidas de referência da mão para fins de personalização. | 25 |
| Figura 2.6 | Enquadramento de um fluxo de CAD assistido por IA para desenvolvimento de produto. | 29 |
| Figura 2.7 | Modelo de processo para configurar participação em ecossistemas de inovação e cocriação. | 34 |
| Figura 2.8 | Distribuição dos estudos por nível de prontidão tecnológica (TRL) e categoria de aplicação. O gráfico distingue estudos sobre próteses em geral, próteses de membro inferior produzidas por impressão 3D (LL 3DP), próteses de membro inferior desenvolvidas com recurso a CAD/CAM (LL CAD/CAM), outras abordagens aplicadas ao membro inferior (LL other), próteses de membro superior produzidas por impressão 3D (UL 3DP) e outros casos não enquadrados nas categorias anteriores. | 39 |
| Figura 3.1 | Processo interdisciplinar de desenvolvimento de uma prótese de membro superior impressa em 3D. | 44 |
| Figura 3.2 | Exemplo de recolha dimensional para ajuste de prótese impressa em 3D. | 47 |
| Figura 4.1 | Parâmetros antropométricos utilizados na modelação paramétrica de dedos protésicos. | 51 |
| Figura 4.2 | Comparação entre o escalonamento uniforme e a modelação paramétrica de dedo protésico. | 55 |
| Figura 4.3 | Relação entre modelo paramétrico digital, prototipagem e verificação de um dedo protésico. | 65 |
| Figura 5.1 | Fluxo geral de produção personalizada de próteses a partir de plataforma web – Hand Fab | 71 |
| Figura 5.2 | Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo. | 73 |
| Figura 5.3 | Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso. | 77 |
| Figura 6.1 | Relação entre desafios de explicabilidade e princípios de IA responsável. | 89 |
| Figura 7.1 | Teste de uma prótese impressa em 3D com utilizador em contexto aplicado. | 94 |
| Figura 8.1 | Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior. | 98 |

## Capítulo 1 — Introdução

### 1.1 Enquadramento geral, contexto e motivação

A perda de membros superiores provoca impactos funcionais (limitação nas tarefas quotidianas), sociais (alterações na interação e na inclusão) e simbólicos (mudanças na identidade e na percepção), o que requer soluções técnicas e projetuais que aliem desempenho mecânico, conforto ergonómico, aceitação estética e viabilidade económica. Apesar dos avanços em dispositivos médicos e na fabricação aditiva, persistem obstáculos relacionados ao custo, à personalização anatómica e à dependência de técnicos especializados para a adaptação e manutenção das próteses.

Nos últimos anos, a impressão 3D e as plataformas open source ampliaram o acesso a dispositivos protésicos, especialmente em contextos economicamente desfavorecidos. No entanto, muitos desses modelos dependem de geometrias fixas, isto é, formas pré-definidas sem adaptação automática, ou de ajustes manuais pouco padronizados, o que resulta em alterações sem um protocolo uniforme e dificulta a expansã, a reprodutibilidade e a integração robusta de dados antropométricos, ou seja, medidas corporais específicas do utilizador.

A Figura 1.1 introduz visualmente este contexto, mostrando como a fabricação aditiva tem sido associada a soluções protésicas abertas, acessíveis e adaptáveis. Esta leitura ajuda a enquadrar a motivação inicial do projeto: a impressão 3D amplia o campo de possibilidades, mas a personalização robusta continua a exigir modelos configuráveis, critérios de ajuste e mediação projetual.

![](projecto-completo_media/image01.png)

Figura 1.1 — Exemplos de próteses e dispositivos associados à fabricação aditiva em contexto protésico.

Fonte original: Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

O Design Industrial é o mediador entre a tecnologia e a experiência humana. A parametrização e a inteligência artificial podem estruturar sistemas configuráveis adequados a requisitos anatómicos, funcionais e simbólicos, promovendo próteses personalizadas, acessíveis e ajustáveis. Este trabalho explora criticamente essas ferramentas no contexto de Research Through Design.

### 1.2 Problema de investigação

Apesar da democratização parcial da produção de próteses por meio da fabricação aditiva, persiste uma lacuna na integração entre a personalização anatómica, a precisão funcional e as metodologias centradas no utilizador. Os processos atuais mostram dificuldades em se adaptar a diferentes perfis antropométricos, dependência de ajustes empíricos e ausência de plataformas configuráveis que aliem parametrização, dados antropométricos e apoio algorítmico à decisão projetual.

O problema central é compreender como o design de produto, através de sistemas paramétricos (soluções ajustáveis com base em dados) e inteligência artificial (algoritmos que auxiliam a tomada de decisões), pode viabilizar a personalização de próteses de membros superiores de modo acessível, reprodutível e robusto, mantendo a qualidade funcional e o controlo do projeto.

### 1.3 Objetivos da investigação

### 1.3.1 Objetivo geral

O objetivo geral é gerar conhecimento por meio da prática do Design, criando e avaliando um sistema de Design paramétrico (modelo ajustável por parâmetros definidos) assistido por inteligência artificial (algoritmos inteligentes) para próteses personalizadas de membros superiores. O sistema articula Design Industrial (criação de produtos), Design Inclusivo (acessibilidade para todos) e Design para Fabricação Aditiva.

### 1.3.2 Objetivos específicos

Pretende-se analisar criticamente o papel do Design Industrial como mediador entre a tecnologia e a experiência humana. O sistema paramétrico é um modelo ajustável, apoiado por uma plataforma digital, que permite configurar próteses com base em dados antropométricos (medidas físicas do utilizador) e em preferências individuais. A validação da abordagem combina testes de perfil, exportação de geometrias, análise de malhas e prototipagem por impressão 3D em PLA e PETG, avaliando a coerência dimensional, a montagem preliminar, a viabilidade de fabrico e os limites materiais, sem reivindicar validação clínica do dispositivo.

A investigação busca responder: como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controle projetual? Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a reprodutibilidade de próteses impressas em 3D? Como o Design Industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?

### 1.4 Abordagem metodológica geral

O projeto adota uma metodologia aplicada, baseada em Research Through Design, que reconhece o ato de projetar como uma forma de gerar conhecimento. Estrutura-se em fases conceptual, metodológica e empírica, articuladas pelo modelo Double Diamond, que promove ciclos iterativos de exploração, definição, desenvolvimento e validação.

A fase conceptual realiza uma revisão crítica da literatura e das plataformas, consolidando o quadro teórico e os requisitos técnicos. A fase metodológica estabelece a arquitetura do sistema paramétrico assistido por inteligência artificial, integrando dados antropométricos e princípios de design para fabricação aditiva. A fase empírica operacionaliza a modelação paramétrica, a produção de protótipos por impressão 3D em PLA e PETG e a avaliação técnica e funcional preliminar, sem utilizar dados pessoais de utilizadores.

### 1.5 Estrutura da dissertação

A dissertação organiza-se em nove capítulos principais. O Capítulo 1 apresenta o enquadramento, o problema, os objetivos, as questões de investigação e a abordagem metodológica geral. O Capítulo 2 desenvolve o enquadramento teórico e o estado da arte. O Capítulo 3 explicita a metodologia de investigação. O Capítulo 4 descreve o desenvolvimento do modelo paramétrico. O Capítulo 5 aborda a plataforma web e a integração digital. O Capítulo 6 trata da integração da inteligência artificial. O Capítulo 7 discute a interface, a interação e a experiência de utilização. O Capítulo 8 reúne a avaliação e a discussão dos resultados. Por fim, o Capítulo 9 sintetiza as conclusões e os trabalhos futuros.

## Capítulo 2 — Enquadramento Teórico e Estado da Arte

### 2.1 Prótese de membro superior e dispositivos médicos

Prótese de membro superior é um dispositivo médico externo que substitui um segmento ausente devido à amputação ou a uma deficiência  congénita. Vai além da restituição formal: recupera funções, facilita atividades diárias, melhora a autonomia e reduz o impacto psicossocial da perda (Fink & Diamond, 2023 (#ref-fink-2023); Segura et al., 2024 (#ref-segura-2024)).

A perda total ou parcial de um membro superior provoca consequências físicas, funcionais, sociais e emocionais profundas. "Perda total" refere-se à ausência completa do membro, enquanto "perda parcial" indica ausência apenas de parte dele. A mão humana incorpora capacidades motoras e sensoriais complexas, abrangendo o alcance (movimento do membro para tocar ou agarrar objetos), a preensão (ato de segurar objetos), a manipulação fina (habilidade para movimentos precisos), a estabilização (manter objetos ou posições), a coordenação bimanual (uso de ambas as mãos em colaboração) e a exploração tátil (detecção de propriedades dos objetos pelo contato). Replicar artificialmente estas funções continua a ser um desafio significativo nos dispositivos médicos e na reabilitação. O desenvolvimento e a prescrição de próteses envolvem compromissos permanentes entre funcionalidade, peso, robustez, conforto, controle intuitivo, manutenção e custo.

Nas últimas décadas, o setor evoluiu de soluções maioritariamente cosméticas e mecânicas para sistemas com maior sofisticação eletromecânica, integração eletrônica aprimorada e potencial de personalização ampliado. Ainda assim, o avanço tecnológico não resolveu desafios estruturais como desconforto, dificuldade de controle, ausência de feedback sensorial e alta taxa de abandono. Esta tensão entre o potencial técnico e os resultados práticos é fundamental para compreender o estado atual das próteses de membro superior como dispositivos médicos.

### Tipologias de próteses de membro superior

As próteses de membro superior podem ser classificadas de acordo com a fonte de energia e o mecanismo de controlo. Distinguem-se quatro categorias principais: passivas (cosméticas), mecânicas acionadas pelo corpo, mioelétricas (externamente alimentadas) e híbridas. Cada tipo possui vantagens e limitações, o que reflete diferentes equilíbrios entre desempenho funcional, conforto, durabilidade e custo   (Brack & Amalu, 2021).

.

Próteses passivas destinam-se à aparência e ao apoio estático em tarefas simples, sem preensão ativa. Variam entre dispositivos rígidos e versões ajustáveis, nas quais os dedos ou os terminais podem ser movidos manualmente. São leves, simples, silenciosas e requerem pouca manutenção. Oferecem utilidade funcional limitada e são preferidas quando a estética é prioritária ou quando o utilizador procura um dispositivo discreto (Fink & Diamond, 2023 (#ref-fink-2023); Segura et al., 2024 (#ref-segura-2024)).

### Próteses mecânicas acionadas pelo corpo (body-powered)

As próteses mecânicas utilizam um sistema de arnês e cabos que converte movimentos do ombro, do tronco ou da cintura escapular em ação no dispositivo terminal, tipicamente um gancho ou uma mão mecânica. São soluções tradicionalmente valorizadas pela robustez, pela previsibilidade mecânica, pelo menor custo e pela relativa facilidade de manutenção.

Um atributo particularmente relevante é o feedback proprioceptivo indireto proporcionado pela tensão transmitida pelo sistema de cabos, que pode contribuir para um controlo funcional mais previsível em determinadas tarefas. Contudo, estas próteses apresentam limitações expressivas: o arnês pode ser desconfortável e restritivo, os padrões de preensão tendem a ser mais limitados e a sua utilização exige esforço físico contínuo e aprendizagem motora específica (Engdahl et al., 2024 (#ref-engdahl-2024); Fink & Diamond, 2023 (#ref-fink-2023)).

### Próteses mioelétricas

As próteses mioelétricas são dispositivos eletricamente alimentados que utilizam sinais eletromiográficos (EMG) captados por meio de elétrodos de superfície aplicados no membro residual. Esses sinais são processados eletronicamente e ativam os motores responsáveis pelo movimento da mão, do punho ou do cotovelo. Em comparação com as soluções mecânicas, apresentam habitualmente maior integração estética, ausência de arnês e potencial para padrões de movimento mais sofisticados. Em alguns casos, a sua utilização tem sido associada à redução da dor fantasma e a uma experiência de uso mais aceitável em contextos sociais. As suas limitações incluem maior peso, custo mais elevado, dependência de baterias, maior sensibilidade à humidade e a interferências, necessidade de calibração e ausência de feedback sensorial direto (Bates et al., 2020 (#ref-bates-2020); Engdahl et al., 2024 (#ref-engdahl-2024)).

### Sistemas híbridos

Combinam mecanismos mecânicos e elétricos no mesmo dispositivo. São particularmente frequentes em amputações proximais, como amputações transumerais ou desarticulações do ombro, podendo associar, por exemplo, controlo mecânico do cotovelo e controlo mioelétrico do terminal. Esta configuração procura tirar partido das vantagens específicas de cada sistema, distribuindo o peso, as exigências funcionais e a complexidade de controlo. Em contrapartida, a aprendizagem, a adaptação e a manutenção podem tornar-se mais exigentes (Segura et al., 2024 (#ref-segura-2024); Walters et al., 2025 (#ref-walters-2025)).

Uma representação visual útil desta diversidade tipológica é apresentada na Figura 2.1, que reúne exemplos de próteses impressas em 3D com soluções morfológicas e mecânicas distintas, ajudando a perceber como diferentes opções de configuração materializam compromissos distintos entre simplicidade, função e custo.

![](projecto-completo_media/image02.png)

Figura 2.1 — Exemplos de próteses de membro superior impressas em 3D, ilustrando diversidade tipológica e construtiva.

Fonte original: ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

### Considerações clínicas e funcionais

A prescrição de uma prótese de membro superior constitui um processo clínico complexo, centrado no utilizador e conduzido por uma equipa multidisciplinar composta por médicos, protesistas, terapeutas e pelo próprio utilizador/paciente na escolha do dispositivo terminal, mas envolve uma avaliação integrada de fatores físicos, funcionais, ocupacionais e psicossociais (Fink & Diamond, 2023 (#ref-fink-2023); Soyer et al., 2016 (#ref-soyer-2016)).

Entre os fatores físicos incluem-se o nível de amputação, o comprimento e a condição do membro residual, a integridade cutânea, a amplitude articular e a força muscular. Amputações de nível mais proximal implicam desafios acrescidos em termos de controlo e do peso do sistema protésico.

Os fatores individuais, como idade, comorbilidades, dominância manual, literacia técnica, contexto profissional e atividades recreativas, influenciam significativamente a escolha da tipologia protésica. A título de exemplo, utilizadores envolvidos em trabalho manual intensivo ou em ambientes mais exigentes podem beneficiar de soluções mecânicas mais robustas, enquanto contextos profissionais e sociais em que a integração estética e a diversidade funcional são mais valorizadas podem favorecer dispositivos mioelétricos.

Os fatores psicossociais, incluindo motivação, expectativas, imagem corporal, suporte social e capacidade cognitiva, são igualmente determinantes. Expectativas irrealistas relativamente às capacidades do dispositivo podem levar à insatisfação, ao uso intermitente e ao eventual abandono.

A reabilitação protésica desenvolve-se em fases — cuidados perioperatórios, preparação pré-protésica, treino com prótese definitiva e acompanhamento a longo prazo. O treino funcional é particularmente relevante em sistemas mioelétricos, exigindo fortalecimento muscular específico, aprendizagem da geração de sinais consistentes e integração progressiva do dispositivo em tarefas reais. De modo recorrente, a literatura sublinha a importância do seguimento continuado, da educação do utilizador e do ajustamento iterativo do dispositivo ao longo do tempo (Bates et al., 2020 (#ref-bates-2020); Soyer et al., 2016 (#ref-soyer-2016)).

### Medição de resultados e abandono protésico

A avaliação objetiva do sucesso protésico continua a ser um desafio. Persistem a escassez de instrumentos padronizados e a heterogeneidade de métricas, o que dificulta a comparação entre estudos, dispositivos e estratégias de reabilitação. São utilizadas ferramentas de avaliação registadas pelo utilizador, centradas na funcionalidade percebida, na satisfação e na qualidade de vida, bem como testes baseados em desempenho, orientados para a destreza, a velocidade de execução e o controlo funcional em tarefas estruturadas (Segura et al., 2024 (#ref-segura-2024); Soyer et al., 2016 (#ref-soyer-2016)).

Apesar da evolução tecnológica, as taxas de abandono permanecem elevadas. A literatura associa, de forma recorrente, a rejeição protésica a problemas de conforto, peso, funcionalidade insuficiente, manutenção exigente e controlo pouco intuitivo. Esta persistência indica que a melhoria tecnológica isolada não garante adoção sustentada. Ainda assim, quando o dispositivo está adequadamente prescrito, ajustado e acompanhado, a utilização continuada de prótese tende a associar-se a maior independência funcional e a melhores indicadores de participação e de qualidade de vida do que a não utilização (Fink & Diamond, 2023 (#ref-fink-2023); Smail et al., 2020 (#ref-smail-2020)).

Esta persistência do abandono é sintetizada de forma clara na Figura 2.2, que relaciona uso, rejeição primária e rejeição secundária, reforçando que o problema não é marginal, mas estrutural no campo das próteses de membro superior.

![](projecto-completo_media/image03.png)

Figura 2.2 — Utilização, rejeição primária e rejeição secundária de próteses do membro superior adquiridas.

Fonte original: Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive Technology, 2(6), 346-357. [https://doi.org/10.1080/17483100701714733](https://doi.org/10.1080/17483100701714733)

### Enquadramento regulatório enquanto dispositivo médico

As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pela Regulamento ([^2]EU) 2017/745 (MDR) - https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng, que classifica os dispositivos nas Classes I, IIa, IIb e III. Dispositivos terapêuticos ativos, incluindo próteses mioelétricas, enquadram-se geralmente nas classes intermédias ou superiores, o que exige avaliação por um organismo notificado para efeitos de marcação CE[^3] (Parlamento Europeu e Conselho da União Europeia, 2017 (#ref-parlamento-europeu-2017)).

Nos Estados Unidos, a regulação é assegurada pela Food and Drug Administration (FDA) por meio de um sistema de classificação de risco. A maioria dos componentes protésicos convencionais enquadra-se nas classes de risco mais baixas, enquanto sistemas mais complexos, como próteses mioelétricas avançadas, podem exigir controles , documentação técnica mais extensa e, em certos casos, evidência clínica adicional (Resnik et al., 2010 (#ref-resnik-2010)).

A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de software e consideração explícita de fatores humanos e de usabilidade. Normas desenvolvidas no âmbito do comité técnico ISO/TC 168[^4] contribuem para a padronização de requisitos aplicáveis a próteses e ortóteses. Adicionalmente, os fabricantes devem implementar sistemas de vigilância pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o que reforça a natureza regulada, iterativa e evidencial deste domínio (Parlamento Europeu & Conselho da União Europeia, 2017 (#ref-parlamento-europeu-2017); Resnik et al., 2010 (#ref-resnik-2010)).

### 2.2 Design Industrial, Design Inclusivo e Design Centrado no Utilizador

O design industrial, no contexto da saúde e das tecnologias de apoio, é reconhecido progressivamente como uma disciplina mediadora entre as necessidades humanas, os contextos de utilização e os sistemas técnicos regulados.

A literatura revista evidencia que o design desempenha um papel estruturante na promoção da inclusão, da autonomia e da participação social, ao articular a configuração formal dos produtos com a modelação da relação entre indivíduos, ambientes, artefactos e sistemas.

Em particular, nas tecnologias de apoio, o design é descrito como um elemento que medeia a interação entre os utilizadores e o seu meio envolvente, contribuindo para reduzir barreiras funcionais e sociais e, consequentemente, para melhorar os resultados de participação e a qualidade de vida (Clarkson & Coleman, 2010 (#ref-clarkson-2010); Shah & Robinson, 2006 (#ref-shah-2006)).

Paralelamente, o design inclusivo é apresentado como um imperativo contemporâneo que visa minimizar a exclusão evitável decorrente de decisões projetuais que não consideram a diversidade populacional e a variabilidade de capacidades ao longo do tempo. Esta perspetiva alinha-se com a responsabilidade dos sistemas de saúde de responder a utilizadores heterogéneos, com diferentes condições físicas, cognitivas e contextuais (Clarkson & Coleman, 2010 (#ref-clarkson-2010)).

### Design industrial em dispositivos médicos

No domínio dos dispositivos médicos, o design industrial surge tanto como prática metodológica centrada no utilizador como também com um papel colaborativo integrado em equipas multidisciplinares de desenvolvimento. A literatura identifica, contudo, uma lacuna estrutural: muitos dispositivos médicos continuam a ser desenvolvidos predominantemente com base em abordagens de engenharia e em requisitos regulatórios, com participação limitada de profissionais com formação específica em metodologias de design centrado no uso. Esta assimetria contribui para soluções tecnicamente robustas, mas nem sempre otimizadas em termos de ergonomia, usabilidade ou integração na vida quotidiana (Fisher & Johansen, 2020 (#ref-fisher-2020); Wilke et al., 2020 (#ref-wilke-2020)).

Neste contexto, o design industrial assume relevância não apenas na fase de conceptualização, mas também na definição de requisitos de utilização, na tradução de necessidades clínicas em soluções tangíveis e na articulação entre requisitos regulatórios e experiência do utilizador (Fisher & Johansen, 2020 (#ref-fisher-2020); Shah & Robinson, 2006 (#ref-shah-2006)).

Esta posição intermédia do design torna-se mais clara quando se observa a multiplicidade de papéis que os profissionais de saúde podem assumir nos processos de desenvolvimento. Em vez de contribuírem apenas como validadores de soluções, estes agentes podem ser intervenientes do seu setor, utilizadores peritos, mediadores entre domínios e profissionais clínicos ou investigadores, como sintetiza a Tabela 2.1.

Tabela 2.1 — Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos

| Intervenientes do setor | Identificam oportunidades, especificações e condicionantes regulatórias | Mercado, estratégia e processos de certificação |

| --- | --- | --- |

| Utilizadores peritos | Fornecem experiência clínica situada e problemas de uso | Experiência do utilizador e adequação funcional |

| Mediadores | Traduzem linguagem, necessidades e constrangimentos entre equipas | Problemas técnicos, terminologia e entendimento partilhado |

| Profissionais clínicos e investigadores | Enquadram cuidados, testes e validação empírica | Resultados clínicos, ensaios e usabilidade |

Fonte adaptada. Referência original: Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. [https://doi.org/10.1080/14606925.2024.2420152](https://doi.org/10.1080/14606925.2024.2420152)

### Design Inclusivo e Design Universal

O design inclusivo representa uma mudança conceptual significativa ao deslocar o foco da deficiência enquanto atributo individual para a compreensão da deficiência como resultado de desajustes entre capacidades humanas e ambientes projetados (Clarkson & Coleman, 2010 (#ref-clarkson-2010)).

Esta perspetiva aproxima-se dos modelos sociais e relacionais da deficiência, enfatizando que a exclusão pode ser produzida por decisões de projeto que não contemplam a diversidade de utilizadores (Clarkson & Coleman, 2010 (#ref-clarkson-2010)).

Enquanto campo de prática e investigação, o design inclusivo desenvolveu ferramentas e orientações destinadas a apoiar equipas de projeto na consideração sistemática da diversidade populacional. Estas incluem estratégias de segmentação, análise de capacidades e critérios de acessibilidade aplicáveis a produtos e sistemas, incluindo tecnologias digitais em saúde (Clarkson & Coleman, 2010 (#ref-clarkson-2010)).

O design universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente aplicada no design industrial, tendo como princípio orientador a conceção de produtos e ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações ou de design especializado. Os Sete Princípios do Design Universal, propostos por Ron Mace[^5], são amplamente citados como um quadro normativo para avaliar equidade, flexibilidade, simplicidade, tolerância ao erro e redução do esforço físico (Story, 2006 (#ref-story-2006)).

Na área da saúde, o design universal é associado a abordagens centradas no paciente e avaliado por meio de critérios orientados a resultados, como a participação, a inclusão e a igualdade de acesso. A convergência entre design inclusivo e design universal revela-se particularmente evidente na ênfase comum na redução de barreiras ambientais e na ampliação do conceito de usabilidade para uma população mais ampla (Story, 2006 (#ref-story-2006); White & Mosca, 2022 (#ref-white-2022)).

### Design Centrado no Utilizador e Design Centrado no Humano

O design centrado no utilizador (User-Centred Design – UCD) é descrito como uma abordagem que envolve os utilizadores finais ao longo de todo o processo de desenvolvimento, com o objetivo de assegurar que o produto seja funcionalmente adequado, compreensível e valorizado. Esta abordagem mobiliza métodos como entrevistas, personas, protocolos de think-aloud, prototipagem iterativa e grupos focais, promovendo ciclos sucessivos de recolha de requisitos e de validação (Fisher & Johansen, 2020 (#ref-fisher-2020); Shah & Robinson, 2006 (#ref-shah-2006)).

O design centrado no humano (Human-Centred Design – HCD) amplia esta perspetiva ao integrar dimensões culturais, contextuais e sistémicas. No desenvolvimento de dispositivos médicos, o HCD é associado a práticas como etnografia, design participativo, mapeamento de jornadas (journey maps), mapeamento de stakeholders e avaliação de fatores humanos. A norma ISO 62366 define requisitos específicos para a aplicação da engenharia de usabilidade a dispositivos médicos, reforçando a integração formal de avaliações formativas e sumativas no processo regulado de desenvolvimento. (Fisher & Johansen, 2020 (#ref-fisher-2020); Millet et al., 2018 (#ref-millet-2018)).

A incorporação de fatores humanos é igualmente reforçada por diretivas e normas que exigem a redução dos riscos de uso inadequado, articulando segurança, ergonomia e usabilidade como dimensões indissociáveis do desenvolvimento de dispositivos médicos (Millet et al., 2018 (#ref-millet-2018)).

### Design Participativo e Co-design

O design participativo e o co-design representam um aprofundamento das abordagens centradas no utilizador, enfatizando a participação ativa e o empoderamento dos utilizadores no processo de projeto. Nestes modelos, os utilizadores não são apenas fontes de dados, mas também colaboradores na definição de problemas, na geração de soluções e na avaliação de protótipos (Chapman et al., 2025 (#ref-chapman-2025)).

Revisões sistemáticas apontam para a necessidade de maior transparência e rigor na descrição dos processos de co-design, de modo a fortalecer a sua validade metodológica e eficácia prática. Nas tecnologias de apoio, observa-se uma evolução discursiva dos modelos centrados no utilizador para paradigmas de cocriação, nos quais as experiências dos utilizadores assumem um estatuto central na tomada de decisão (Chapman et al., 2025 (#ref-chapman-2025)). Persistem tensões entre ideais participativos e contextos regulatórios altamente estruturados, nos quais a autoridade decisional permanece frequentemente concentrada em profissionais clínicos e em equipas técnicas (Chapman et al., 2025 (#ref-chapman-2025); Wilke et al., 2020 (#ref-wilke-2020)).

### Metodologias, instrumentos e avaliação

A literatura evidencia que as abordagens inclusivas e centradas no utilizador recorrem a repertórios metodológicos diversificados, incluindo personas, simulação de limitações, prototipagem iterativa, oficinas participativas e análise de ecossistemas de stakeholders (Fisher & Johansen, 2020 (#ref-fisher-2020); Shah & Robinson, 2006 (#ref-shah-2006)).

No domínio hospitalar e dos serviços de saúde, ferramentas de avaliação baseadas em critérios de design universal e de design para todos (Design for All) introduzem sistemas de análise multicritério e listas de verificação estruturadas para aferir os níveis de inclusão (White & Mosca, 2022 (#ref-white-2022)).

Em contextos de tecnologias de apoio, modelos como o Matching Person and Technology (MPT) e quadros conceptuais baseados na Classificação Internacional de Funcionalidade (ICF) são utilizados para apoiar decisões de seleção e de adequação tecnológica, promovendo o alinhamento entre as características do utilizador, do ambiente e do dispositivo (White & Mosca, 2022 (#ref-white-2022)).

A avaliação da evidência tem sido igualmente reforçada através do uso de protocolos sistemáticos, como o PRISMA, que orienta a identificação, seleção e apresentação transparente dos estudos analisados, bem como de instrumentos de avaliação crítica. Esta evolução reflete uma preocupação crescente em fundamentar decisões de design numa base empírica robusta. (Chapman et al., 2025 (#ref-chapman-2025)).

### Desafios e lacunas

Entre os principais desafios identificados destacam-se: – a articulação entre padronização e personalização, particularmente relevante em dispositivos médicos sujeitos a regulamentação rigorosa; – a discrepância entre modelos teóricos de UCD ensinados academicamente e as restrições institucionais à prática em saúde; – a dificuldade de tradução de processos participativos para contextos de implementação e de expansão; – e a necessidade de integrar dimensões interseccionais (como género e fatores socioculturais) na investigação e no desenvolvimento (Privitera, 2017;  Oldfrey et al 2024;   Mc Guinness et al, 2025).

Estas lacunas evidenciam que o design industrial em dispositivos médicos não pode ser compreendido apenas como uma prática formal ou estética, mas como uma disciplina estratégica que articula inclusão, regulação, implementação e experiência do utilizador.

### 2.3 Fabricação Aditiva e parametrização no design de produto

A convergência entre modelação paramétrica e fabricação aditiva (FdA) tem sido amplamente reconhecida como um dos principais vetores de transformação no design contemporâneo, particularmente em contextos que exigem personalização, adaptação morfológica e produção de variantes em pequena escala. A literatura posiciona estas duas abordagens como complementares: a modelação paramétrica permite gerar múltiplas variações controladas a partir de um modelo-base, enquanto a fabricação aditiva viabiliza a materialização de geometrias complexas sem necessidade de moldes ou ferramentas dedicadas (Lei et al., 2016 (#ref-lei-2016); Ozdemir et al., 2022 (#ref-ozdemir-2022); Stralen, 2018 (#ref-stralen-2018)).

Esta articulação é representada com clareza na Figura 2.3, que resume o encadeamento entre aquisição digital, modelação/retificação e fabrico, evidenciando que a personalização depende menos de um único software ou de uma etapa isolada e mais de um workflow integrado.

![](projecto-completo_media/image04.png)

Figura 2.3 — Fluxo digital entre aquisição, CAD/CAM e fabricação aditiva em próteses e ortóteses.

Fonte original: Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. [https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517](https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517)

Neste enquadramento, a personalização deixa de ser entendida como exceção e passa a constituir uma estratégia estruturada, operacionalizada por meio de “seed designs” ou modelos-base parametrizados. Estes modelos preservam uma arquitetura estável, expondo simultaneamente um conjunto limitado de variáveis ajustáveis, frequentemente acessíveis por meio de interfaces digitais ou de configuradores destinados a utilizadores não especialistas (Ozdemir et al., 2022 (#ref-ozdemir-2022); Stralen, 2018 (#ref-stralen-2018)).

### Modelação Paramétrica e Espaços de Variação

Os modelos paramétricos desempenham duas funções centrais. Em primeiro lugar, codificam a lógica geométrica do produto — relações, restrições e regras —, assegurando que alterações nos valores dos parâmetros gerem novas variantes sem comprometer a integridade estrutural nem a coerência funcional. Em segundo lugar, permitem explorar espaços de variação extensos, frequentemente descritos como quase contínuos, o que possibilita a criação de famílias de produtos ajustáveis por meio da modificação de variáveis dimensionais ou funcionais (Lei et al., 2016 (#ref-lei-2016); Ozdemir et al., 2022 (#ref-ozdemir-2022)).

No contexto da adaptação ao utilizador, a literatura destaca que a parametrização torna-se particularmente eficaz quando associada a dados mensuráveis, como a antropometria ou as digitalizações tridimensionais.

Em vez de recorrer a um escalonamento uniforme, que pode introduzir desvios significativos, a definição de parâmetros independentes, como comprimento e largura, permite ajustes mais precisos e maior controlo dimensional dentro de margens reduzidas. Em aplicações protésicas, esta abordagem revelou maior proximidade às cinemáticas naturais e melhor adequação morfológica face a modelos ajustados apenas por escala global. (Lim et al., 2018 (#ref-lim-2018)).

### Integração com Fabricação Aditiva e Design for Additive Manufacturing

A eficácia da personalização depende da integração precoce dos constrangimentos do processo de fabricação aditiva no processo de projeto. A literatura sobre Design for Additive Manufacturing (DfAM) sublinha que a incorporação antecipada de limitações de processo — tolerâncias, resistência mecânica, espessuras mínimas, orientação de impressão — reduz falhas de fabrico e encurta os ciclos iterativos (Chtioui et al., 2023 (#ref-chtioui-2023); Wiberg et al., 2019 (#ref-wiberg-2019)).

Estudos aplicados demonstram que, ao determinar experimentalmente constrangimentos do processo e incorporá-los ao modelo paramétrico, é possível gerar milhares de variantes únicas com elevada taxa de sucesso funcional, minimizando as reimpressões (Wiberg et al., 2019 (#ref-wiberg-2019)). [^9]

Esta evidência reforça a necessidade de uma ligação sistemática entre as fases de design e manufatura, contrariando abordagens que tratam a fabricação como etapa posterior e corretiva (Chtioui et al., 2023 (#ref-chtioui-2023); Wiberg et al., 2019 (#ref-wiberg-2019)).

As tecnologias de fabricação aditiva (FA) utilizadas incluem FDM/FFF (extrusão de termoplásticos), SLS (fusão seletiva a laser), SLA (estereolitografia) e processos industriais metálicos, o que reflete a diversidade de rotas produtivas para componentes personalizados. Cada tecnologia implica requisitos específicos de projeto, reforçando a importância de integrar critérios técnicos no modelo paramétrico desde o início (Chtioui et al., 2023 (#ref-chtioui-2023); Wiberg et al., 2019 (#ref-wiberg-2019)).[^10]

### Configuradores e Cocriação Digital

A articulação entre modelação paramétrica e interfaces digitais possibilita novos modelos de cocriação e de produção distribuída. Configuradores web ou interfaces baseadas em CAD expõem um conjunto delimitado de parâmetros, permitindo ao utilizador ajustar dimensões ou características dentro de intervalos válidos, frequentemente com feedback em tempo real sobre viabilidade (Ozdemir et al., 2022 (#ref-ozdemir-2022); Stralen, 2018 (#ref-stralen-2018)).

A Figura 2.4 mostra um exemplo especialmente relevante desta lógica: a personalização mediada por interface, em que o utilizador atua sobre atributos visuais e formais dentro de um espaço de variação previamente estruturado. Este tipo de configurador ajuda a compreender como a cocriação digital pode ser operacionalizada sem exigir domínio direto de ferramentas CAD complexas.

![](projecto-completo_media/image05.png)

Figura 2.4 — Exemplo de configurador digital para personalização de uma prótese impressa em 3D.

Fonte original: Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

Este modelo “file-to-factory” viabiliza fluxos digitais em que o ficheiro parametrizado é convertido diretamente em instruções de fabrico, seja localmente (impressão 3D descentralizada) ou através de uma encomenda online[^11]. A literatura associa esta lógica à democratização do design e à expansão de estratégias de customização em massa (mass customization) e personalização em massa (mass personalization), reduzindo custos marginais ao dispensar moldes e dispositivos específicos de fabrico.[^12] (Lei et al., 2016 (#ref-lei-2016); Stralen, 2018 (#ref-stralen-2018)).

Contudo, enfatiza-se que configuradores eficazes devem limitar o número de parâmetros expostos e fornecer orientação clara sobre os limites válidos, evitando complexidade excessiva ou escolhas superficiais (Ozdemir et al., 2022 (#ref-ozdemir-2022)).

### Otimização, Geração e Avaliação de Desempenho

A parametrização é frequentemente combinada com métodos de otimização topológica, de geração de estruturas reticuladas e de abordagens multiobjetivo. Estas estratégias permitem gerir compromissos entre peso, resistência, custo e tempo de fabrico, explorando fronteiras de Pareto para selecionar soluções alinhadas com objetivos específicos (Lei et al., 2016 (#ref-lei-2016); Yao et al., 2016 (#ref-yao-2016)).

Em contextos médicos e de tecnologias de apoio, estudos demonstram a integração de modelos paramétricos com análises de elementos finitos (FEM) para validar o desempenho estrutural, bem como a utilização de algoritmos generativos capazes de adaptar padrões e estruturas superficiais a geometrias individualizadas. (Lei et al., 2016 (#ref-lei-2016); Lim et al., 2018 (#ref-lim-2018)).

Este cruzamento entre parametrização, simulação e FA evidencia um ecossistema digital integrado que sustenta personalização técnica com base quantitativa (Lei et al., 2016 (#ref-lei-2016); Yao et al., 2016 (#ref-yao-2016)).

### Implicações para o Design Industrial

A literatura converge para a ideia de que a robustez do modelo paramétrico é uma condição crítica para a personalização em escala. Modelos mal estruturados ou com dependências inconsistentes podem comprometer a simulação, a otimização e a configuração de famílias de produto (Lei et al., 2016 (#ref-lei-2016); Wiberg et al., 2019 (#ref-wiberg-2019)).

Assim, a qualidade da definição paramétrica desempenha um papel estratégico para a viabilidade de sistemas adaptáveis (Ozdemir et al., 2022 (#ref-ozdemir-2022)).

Em termos económicos, a Fabricação Aditiva permite reduzir [^13]penalizações tradicionais associadas à variação de produto, sustentando modelos de personalização acessíveis. Estudos orientados para famílias de produto indicam que a integração de modelos paramétricos com análises de custo e desempenho pode manter os custos relativamente estáveis mesmo com elevada diversidade geométrica (Lei et al., 2016 (#ref-lei-2016); Yao et al., 2016 (#ref-yao-2016)).

No plano educativo e profissional, recomenda-se a integração de DfAM nos currículos de design industrial, promovendo competências que articulem a conceção, a simulação e a fabricação digital em fluxo contínuo (Kandikjan et al., 2022 (#ref-kandikjan-2022)).

### 2.4 Próteses open source de membro superior passíveis de impressão 3D

As próteses open source de membro superior passíveis de impressão 3D constituem um caso particularmente relevante para esta investigação, porque tornam visível a articulação entre fabricação aditiva, partilha digital de ficheiros, produção distribuída e adaptação local. Ao contrário dos dispositivos comerciais desenvolvidos em cadeias industriais fechadas, estes modelos circulam frequentemente como ficheiros editáveis ou imprimíveis, acompanhados por instruções de montagem, listas de componentes e documentação comunitária. A sua importância não reside apenas no baixo custo de fabrico, mas também na demonstração de que uma comunidade distribuída pode produzir, adaptar e disseminar soluções protésicas funcionais fora dos canais tradicionais da indústria médica (Manero et al., 2019 (#ref-manero-2019); Wendo et al., 2022 (#ref-wendo-2022)).

O projeto e-NABLE é o exemplo mais influente deste movimento. A comunidade consolidou-se em torno da criação e partilha de dispositivos de assistência para diferenças de membro superior, em especial mãos mecânicas acionadas pelo corpo e braços impressos em 3D para crianças. O seu catálogo reúne modelos de mão, braço, dedos, polegares e dispositivos terminais, organizados de acordo com a anatomia disponível e o tipo de acionamento. Nos modelos de mão acionados pelo punho, a flexão dos dedos depende normalmente da flexão ativa do punho e de uma palma parcialmente preservada; quando essa condição anatómica não existe, a solução tende a deslocar-se para braços ou mecanismos acionados pelo cotovelo (Wendo et al., 2022 (#ref-wendo-2022)).

Este enquadramento é importante porque vários modelos usados ou analisados nesta investigação pertencem diretamente a esta linhagem. O Cyborg Beast, o Raptor Reloaded, a Flexy Hand, o Flexy Beast, o Paraglider Hand/Flexible Flyer, a Phoenix Hand e a Unlimbited Phoenix Hand não devem ser entendidos como objetos isolados, mas como variações de um ecossistema e-NABLE em que cada modelo traduz compromissos diferentes entre simplicidade de impressão, facilidade de montagem, robustez, custo, aparência e adequação anatómica. O Cyborg Beast, por exemplo, foi descrito como uma mão protésica infantil de baixo custo, acionada pelo punho e ajustável por procedimentos remotos de medição e escala (Zuniga et al., 2015 (#ref-zuniga-2015)). Já modelos posteriores, como a Phoenix/Unlimbited Phoenix e derivados como o Paraglider, procuram simplificar a montagem, melhorar a manutenção e estabilizar geometrias recorrentes. Para o presente projeto, isto tem uma consequência direta: a integração de modelos e-NABLE numa plataforma paramétrica não é apenas uma operação técnica de importação de ficheiros, mas uma tentativa de explicitar e controlar regras geométricas que, nos modelos originais, aparecem muitas vezes como escalas globais, limites empíricos ou decisões embebidas no próprio ficheiro.

O Victoria Hand Project representa uma alternativa complementar ao modelo comunitário e maker do e-NABLE. Em vez de depender sobretudo de voluntários dispersos, organiza-se como uma estrutura de prestação de cuidados baseada em parcerias locais, formação técnica, fabrico descentralizado e acompanhamento por profissionais ou clínicas parceiras. A sua relevância está em mostrar que a impressão 3D pode ser integrada num modelo de serviço mais estruturado, no qual a criação digital de componentes, a seleção modular, a adaptação de encaixes e a circulação de feedback entre parceiros locais e equipa central funcionam como infraestrutura de aprendizagem contínua (Dechev et al., 2023 (#ref-dechev-2023)). Assim, enquanto o e-NABLE evidencia o potencial da comunidade aberta e da documentação partilhada, o Victoria Hand Project evidencia a importância da mediação clínica, da formação e da qualidade controlada em contextos de baixo acesso a cuidados protésicos.

A evidência disponível, contudo, obriga a uma leitura cautelosa. As revisões sistemáticas sobre próteses de membro superior impressas em 3D indicam que os resultados são promissores, mas continuam limitados por amostras pequenas, ausência de ensaios controlados, períodos curtos de acompanhamento e heterogeneidade nos instrumentos de avaliação. A literatura existente não demonstra superioridade robusta face a próteses convencionais nem permite concluir sobre efeitos de longo prazo em conforto, durabilidade ou qualidade de vida (Diment et al., 2018 (#ref-diment-2018)). Uma revisão mais recente sobre resultados clínicos de próteses impressas em 3D reforça a mesma cautela: há sinais de melhoria em destreza, satisfação e adequação, mas a qualidade da evidência permanece limitada e pouco comparável entre estudos (Atallah et al., 2025 (#ref-atallah-2025)).

As limitações técnicas também são relevantes para o design. Estudos mecânicos sobre mãos open source mostram que a acessibilidade e o baixo custo coexistem com restrições claras de desempenho, repertório de preensões, resistência, durabilidade e segurança funcional. No caso do Raptor Reloaded, por exemplo, uma mão corporalmente acionada pode ser útil para tarefas simples, mas permanece distante da diversidade de movimentos e preensões de uma mão humana (Cabibihan et al., 2021 (#ref-cabibihan-2021)). Esta constatação não diminui o valor social destes modelos, mas impede que sejam apresentados como substitutos clínicos universais. Pelo contrário, reforça a necessidade de os tratar como plataformas de desenvolvimento, aprendizagem e personalização progressiva.

Para esta investigação, o interesse das próteses open source impressas em 3D está precisamente nessa tensão. Por um lado, modelos como o Flexy Beast, o Paraglider Hand e a Unlimbited Phoenix Hand oferecem bases acessíveis, reproduzíveis e compatíveis com fabrico distribuído. Por outro lado, a sua personalização continua frequentemente dependente de escalonamento, adaptação manual e conhecimento tácito da comunidade. A proposta de um sistema paramétrico assistido por inteligência artificial situa-se nesse intervalo: procura transformar modelos abertos em objetos configuráveis com regras explícitas, limites dimensionais visíveis, apoio à escolha do modelo adequado e ligação mais clara entre dados antropométricos, geometria gerada e critérios de fabrico. Deste modo, o ecossistema e-NABLE e o Victoria Hand Project não são apenas antecedentes históricos, mas referências críticas para compreender o que a plataforma deve preservar, corrigir e tornar mais verificável.

### 2.5 Antropometria aplicada ao design protésico

A antropometria constitui um fundamento técnico e metodológico central no design protésico, na medida em que a adequação geométrica do dispositivo ao corpo do utilizador condiciona diretamente o conforto, a segurança, o desempenho funcional e a aceitação. Em próteses e tecnologias de apoio, a literatura recente evidencia uma transição progressiva de medições manuais baseadas em marcos anatómicos para processos digitais de captura de superfície (digitalização 3D e fotogrametria), integrados com fluxos CAD/CAM e com fabricação aditiva. Esta evolução é frequentemente descrita como uma cadeia “aquisição anatómica → modelação/retificação em CAD → fabrico aditivo → pós-processamento”, embora também se reconheça que muitos estudos permanecem em fases de prova de conceito e carecem de validação longitudinal e em larga escala (Chainando et al., 2025 (#ref-chainando-2025)).

### Da dimensão linear à “forma” como dado de projeto

Historicamente, a antropometria aplicada ao design baseou-se em medidas escalares (comprimentos, larguras, perímetros), obtidas com instrumentos como paquímetros, compassos antropométricos e fitas métricas, muitas vezes segundo procedimentos normalizados (por exemplo, a norma ISO 7250). Contudo, no design protésico — particularmente em interfaces corpo–dispositivo, como o encaixe (socket) — a literatura sublinha que a “forma” (shape) desempenha um papel determinante, pois pequenas variações volumétricas e distribuições de pressão podem gerar desconforto, lesões cutâneas e abandono do dispositivo. Estudos e revisões referem que o ajuste protésico pode exigir tolerâncias muito reduzidas e que a complexidade anatómica, bem como trajetórias de carga e zonas de alívio, não é devidamente capturada por um conjunto limitado de medidas lineares (Albin & Molenbroek, 2023 (#ref-albin-2023); Young et al., 2023 (#ref-young-2023)).

Assim, observa-se uma valorização crescente de métodos capazes de capturar geometria tridimensional de alta resolução e de traduzir essa informação em modelos CAD passíveis de retificação, parametrização e fabrico (Squibb et al., 2024 (#ref-squibb-2024)).

Mesmo assim, a medição linear continua a ser indispensável para estruturar o modelo paramétrico, sobretudo quando se pretende definir um conjunto mínimo de entradas robustas e replicáveis. A Figura 2.5 ilustra precisamente este nível basal: os marcos anatómicos e os comprimentos de referência que sustentam medições comparáveis da mão.

![](projecto-completo_media/image06.png)

Figura 2.5 — Marcos anatómicos e medidas de referência da mão para fins de personalização.

Fonte original: Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

### Métodos de recolha antropométrica em próteses e tecnologias de apoio

A literatura organiza os métodos de recolha em famílias, cada uma com potencialidades e limitações específicas para o design protésico:

A antropometria manual inclui medições em posturas normalizadas, com instrumentos clínicos e de ergonomia. Mantém relevância em contextos de acessibilidade clínica e de monitorização simples, por exemplo através da medição de circunferências para acompanhar variações do membro residual. Contudo, estas medidas podem representar de forma limitada as alterações reais de volume, uma vez que dependem da geometria do segmento e da distribuição dos tecidos, o que reduz a precisão necessária para decisões de ajuste fino. (Ibrahim et al., 2024 (#ref-ibrahim-2024)).

2. A digitalização 3D, através de scanning óptico, permite captar a superfície corporal sob a forma de nuvens de pontos ou malhas, posteriormente limpas e convertidas em modelos utilizáveis em CAD e fabrico, frequentemente no formato STL. Esta tecnologia facilita fluxos de personalização e pode ser combinada com processos de automatização, como a correspondência de características anatómicas, para reduzir o trabalho manual. A consistência dos resultados pode, contudo, variar conforme a complexidade da forma, sobretudo em geometrias irregulares, como segmentos residuais complexos. (Squibb et al., 2024 (#ref-squibb-2024)).

3. Fotogrametria reconstrói modelos 3D a partir de fotografias 2D, incluindo soluções baseadas em smartphones.É apresentada como um método promissor pela rapidez na captura e pelo potencial de democratização, embora possa exigir mais tempo de processamento e cuidados com a iluminação e a cobertura da imagem. (Silva et al., 2024 (#ref-silva-2024)).

4. As imagens médicas, como tomografia computorizada (CT) ou ressonância magnética (MRI: Magnetic Resonance Imaging), permitem obter geometria externa e, em alguns casos, informação interna, por exemplo sobre estruturas ósseas. Esta informação pode sustentar modelos mais ricos e abordagens como a modelação estatística de forma. Contudo, estas técnicas implicam maior custo e menor acessibilidade e, no caso do CT, exigem ainda considerar a exposição à radiação e a dependência de contexto hospitalar.

5. Medições complementares da interface (pressão, termografia, bioimpedância) A literatura enfatiza que, em próteses, a adequação não é apenas geométrica: depende do comportamento da interface durante o uso. Por isso, surgem métodos adjuntos que quantificam sinais de ajuste, como a distribuição de pressão e de cisalhamento, zonas de aquecimento localizado (Thermal hot spots) e flutuações de volume do membro residual. Estes métodos ajudam a ligar decisões de forma/retificação a desfechos de conforto e segurança, embora, em muitos casos, sejam descritos como ainda experimentais e com barreiras à adoção clínica (Ibrahim et al., 2024 (#ref-ibrahim-2024); Young et al., 2023 (#ref-young-2023)).

### Interpretação e aplicação de dados antropométricos no projeto

A passagem de dados antropométricos para critérios de projeto ocorre por diferentes vias analíticas:

– Dimensionamento estatístico por percentis e avaliação de incompatibilidades dimensionais: método típico no design ergonómico para definir dimensões que acomodam uma percentagem da população; aplicado sobretudo a produtos de uso “externo” (por exemplo, cadeiras de rodas e interfaces).

– Métodos multivariados e aprendizagem estatística: usados quando se trabalha com dados de alta dimensionalidade (malhas, secções, nuvens de pontos), permitindo extrair padrões de retificação ou modos de variação.

– Modelos preditivos e modelação estatística de forma (SSM): aplicados para reconstruir a geometria a partir de medições reduzidas e inferir relações entre a superfície e a anatomia interna, com análise de componentes principais (PCA) e regressões como ferramentas frequentes, embora limitados por tamanhos amostrais reduzidos em vários estudos (Sunderland et al., 2024 (#ref-sunderland-2024)).

Em design protésico, a aplicação mais crítica recai sobre o encaixe e as zonas de contacto, onde a geometria capturada é submetida a processos de retificação (diferenças propositadas entre o corpo e o dispositivo) e, depois, validada por critérios de conforto e de interface. A literatura é explícita ao considerar a captura dimensional/geométrica do membro como etapa decisiva para a qualidade do encaixe (Kannenberg et al., 2024 (#ref-kannenberg-2024); Young et al., 2023 (#ref-young-2023)).

### Evidência por tipo de dispositivo

Embora os princípios sejam transversais, a literatura evidencia diferenças por tipo de dispositivo:

– Encaixes protésicos e ortóteses: forte ênfase na digitalização 3D, na análise quantitativa de malhas e na validação através de métricas de interface e/ou de simulação por elementos finitos (FEA). Em fluxos digitais de fabrico, verificam-se diferenças geométricas relevantes entre soluções manuais e digitais, reforçando que a digitalização implica uma transformação do próprio processo de ajuste e pode alterar o resultado final (Kannenberg et al., 2024 (#ref-kannenberg-2024); Silva et al., 2024 (#ref-silva-2024)).

– Próteses de membro superior: coexistência de tomografia computorizada (CT), scanners comerciais e fotogrametria como métodos de captura; estudos comparativos indicam que medições obtidas por digitalização 3D podem ser fiáveis e consistentes face a métodos tradicionais quando bem implementadas. Destacam-se também fluxos automatizados que adaptam modelos CAD inteligentes a dados de digitalização, reduzindo o intervalo entre a captura anatómica e a obtenção de um modelo pronto para fabrico (Chainando et al., 2025 (#ref-chainando-2025); Çıklaçandır et al., 2022 (#ref-cklacandr-2022)).

– Produtos de assistência definidos por zonas de alcance funcional (ex.: cadeiras de rodas e acessórios): a antropometria é frequentemente operacionalizada como critério de posicionamento e de acessibilidade, com mapeamentos de alcance e critérios percentílicos.

### Limitações, lacunas e recomendações

Apesar do avanço metodológico, a literatura identifica limitações consistentes: amostras pequenas em estudos aplicados, inconsistência no registo das etapas de retificação e de pós-processamento e falta de validação em contexto real e de longo prazo.

Um problema estrutural particularmente relevante para o design inclusivo é a escassez de bases de dados antropométricas normalizadas para pessoas com deficiência, o que dificulta estimativas de acomodação e pode perpetuar desajustes de design em populações sub-representadas (Bradtmiller, 2022 (#ref-bradtmiller-2022)).

Como orientação prática, emergem recomendações claras: selecionar o método de medição em função da questão de design — captura de forma, monitorização de volume ou validação de interface —, garantir a consistência da medição através de posturas padronizadas e da marcação coerente dos pontos de referência anatómicos, e utilizar bases de dados antropométricas alinhadas com a população-alvo quando se pretende definir critérios de acomodação e ajuste (ASTM International, 2024 (#ref-astm-international-2024); Ibrahim et al., 2024 (#ref-ibrahim-2024)).

Acresce a recomendação de distinguir o ajuste estático (em posturas padronizadas) do ajuste dinâmico (durante a amplitude de movimento funcional), reconhecendo que ajuste e conforto são conceitos relacionados, mas não equivalentes (ASTM International, 2024 (#ref-astm-international-2024)).

### Estruturação de dados

A antropometria aplicada ao design protésico evoluiu para um paradigma digital centrado na captura e na interpretação tridimensionais, complementado por métricas de interface que aproximam a medição do desempenho real de uso. Esta abordagem permite maior precisão na personalização, na integração com CAD, na parametrização e no fabrico aditivo, abrindo caminho para fluxos de adaptação parcialmente automatizados. Contudo, a consolidação destas práticas exige procedimentos mais padronizados, amostras mais amplas e bases de dados antropométricas representativas, para que a personalização não dependa apenas da capacidade tecnológica, mas também de evidências robustas, rastreáveis e acessíveis (Bradtmiller, 2022 (#ref-bradtmiller-2022); Sunderland et al., 2024 (#ref-sunderland-2024)).

No contexto desta investigação, esta necessidade foi operacionalizada através da construção de uma base local consolidada de medidas da mão e do membro superior distal. A descrição detalhada da seleção das fontes, da extração dos valores, da normalização dos dados e da sua tradução para parâmetros de projeto é retomada no Capítulo 4, onde esses dados deixam de funcionar apenas como enquadramento teórico e passam a integrar a metodologia de desenvolvimento do modelo paramétrico.

### 2.6 Inteligência Artificial no processo de design

A integração de Inteligência Artificial (IA) no design tornou-se um tema central não apenas pelo surgimento de novas ferramentas, mas também por ter alterado a forma como se concebe a relação entre criatividade, análise, decisão e automatização. Contudo, a rápida disseminação do termo “IA” também gerou alguma imprecisão conceptual. Em muitos contextos, a mesma designação é usada para sistemas de previsão, algoritmos de otimização, modelos generativos e interfaces conversacionais, apesar desses mecanismos terem funções e modos de operação distintos. Numa dissertação de Design Industrial, importa por isso começar por uma clarificação introdutória: o objetivo desta secção é explicar, de forma acessível, o que é a IA, como funciona em termos gerais, que formas assume no design e porque razão deve ser entendida como instrumento assistivo, e não como substituto autónomo do designer (Choudhury et al., 2025 (#ref-choudhury-2025); Saeidnia & Ausloos, 2024 (#ref-saeidnia-2024); Yüksel et al., 2023 (#ref-yuksel-2023)).

Para efeitos de enquadramento, a Figura 2.6 é útil porque mostra a IA não como um bloco monolítico, mas como uma camada integrada num fluxo CAD mais amplo, em que a recolha de dados, a modelação, a otimização e a avaliação permanecem articuladas com a decisão projetual.

![](projecto-completo_media/image07.png)

Figura 2.6 — Enquadramento de um fluxo de CAD assistido por IA para desenvolvimento de produto.

Adaptado de Menaka, S., Raja, A. W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s).

### O que é a Inteligência Artificial

De forma ampla, a IA pode ser entendida como um conjunto de métodos computacionais orientados para executar tarefas que requerem aprendizagem, reconhecimento de padrões, inferência ou geração de respostas com base em dados. Neste contexto, inferência designa o processo pelo qual um sistema aplica padrões aprendidos durante o treino a novos dados de entrada, produzindo uma classificação, previsão, recomendação ou resposta plausível. Esta definição é útil porque evita tratar a IA como uma entidade única ou como sinónimo de inteligência humana generalizada. O que caracteriza a maioria dos sistemas atuais não é uma capacidade abstrata de “pensar” em qualquer domínio, mas a aptidão para operar sobre tipos específicos de problemas a partir de exemplos, regularidades e relações estatísticas aprendidas durante o treino. (Choudhury et al., 2025 (#ref-choudhury-2025); Yüksel et al., 2023 (#ref-yuksel-2023)).

Dentro deste campo, a aprendizagem automática designa as abordagens em que o sistema aprende a partir de dados, em vez de depender exclusivamente de regras explicitamente escritas. A aprendizagem profunda corresponde a um subconjunto desta família e baseia-se em redes neuronais artificiais com múltiplas camadas, particularmente adequadas para tratar dados complexos, como imagens, texto ou som. Já a IA generativa refere-se a modelos capazes de produzir novos conteúdos — por exemplo, texto, imagens, composições formais ou variantes de projeto — com base nos padrões que aprenderam. Esta distinção é particularmente importante para o design, pois diferentes tipos de IA apoiam diferentes tipos de tarefas: algumas ajudam a analisar, outras a prever, outras a otimizar e outras ainda a gerar alternativas (Khanolkar et al., 2023 (#ref-khanolkar-2023); Krahe et al., 2020 (#ref-krahe-2020); Li et al., 2021 (#ref-li-2021)).

### Como funciona: dados, treino, inferência e geração

O funcionamento básico da maioria dos sistemas atuais de IA pode ser explicado em quatro etapas: dados, treino, inferência e, em certos casos, geração. Em primeiro lugar, o sistema necessita de dados de entrada, isto é, exemplos a partir dos quais possa aprender padrões. Em segundo lugar, durante o treino, o modelo ajusta os seus parâmetros internos para captar padrões recorrentes nos dados. Em terceiro lugar, após o treinamento, o modelo passa a realizar inferência, produzindo previsões, classificações, recomendações ou respostas a novos casos. Em modelos generativos, há ainda um quarto momento: a produção de novos conteúdos compatíveis com os padrões aprendidos, em vez de simples classificação ou previsão (Ao et al., 2025 (#ref-ao-2025); Menaka et al., 2025 (#ref-menaka-2025); Panchal et al., 2019 (#ref-panchal-2019)).

Esta lógica distingue a IA contemporânea dos sistemas puramente baseados em regras. Num sistema baseado em regras, o comportamento é prescrito antecipadamente: se ocorrer determinada condição, executa-se determinada ação. Num sistema treinado com dados, pelo contrário, o comportamento emerge da exposição a exemplos. Esta diferença ajuda a explicar, simultaneamente, a sua força e a sua fragilidade. A força reside na capacidade de lidar com grande complexidade, variabilidade e volume de informação. A fragilidade reside no facto do sistema depender dos dados com que foi treinado, podendo reproduzir enviesamentos, simplificações e erros já presentes nesses dados (Panchal et al., 2019 (#ref-panchal-2019); Yüksel et al., 2023 (#ref-yuksel-2023)).

Nos modelos generativos, este processo torna-se particularmente visível. O sistema aprende distribuições de forma, linguagem, composição ou estilo e, a partir daí, produz novas saídas em resposta a condições ou prompts. Isto permite criar imagens, textos ou alternativas formais que não existiam previamente naquela forma exata, mas também significa que o resultado pode ser apenas plausível, e não necessariamente adequado, original ou tecnicamente robusto. Para o design, esta distinção é decisiva: gerar muitas alternativas não equivale a resolver bem o problema de projeto (Burnap et al., 2019 (#ref-burnap-2019); Choudhury et al., 2025 (#ref-choudhury-2025); Li et al., 2021 (#ref-li-2021)).

### Formas de IA mais relevantes para o design

A literatura identifica várias famílias de aplicações da IA com relevância direta para o design. Uma primeira família é a do apoio à decisão, na qual sistemas analíticos ajudam a interpretar grandes volumes de informação, a comparar alternativas e a reduzir a carga cognitiva em problemas multivariados. Uma segunda é a otimização, particularmente importante na engenharia de produto, na parametrização e no fabrico, na qual algoritmos exploram combinações possíveis e sugerem soluções com melhor desempenho estrutural, funcional ou produtivo. Uma terceira é a visão por computador, usada quando o sistema precisa interpretar imagens, formas ou padrões visuais. Uma quarta é o processamento de linguagem natural, que permite interagir com sistemas complexos por meio de descrições semânticas, em vez de comandos técnicos rígidos. Finalmente, a quinta família, hoje mais visível, corresponde aos sistemas generativos capazes de produzir texto, imagem, forma ou variantes de projeto em resposta a condições de entrada (Ao et al., 2025 (#ref-ao-2025); Khanolkar et al., 2023 (#ref-khanolkar-2023); Wang & Hu, 2024 (#ref-wang-2024)).

Para o Design Industrial, estas famílias não têm exatamente o mesmo peso. A IA generativa tornou-se especialmente relevante na ideação, na comunicação visual e na rápida exploração de alternativas. A otimização e os modelos preditivos assumem maior importância quando o problema envolve desempenho, simulação, restrições de fabrico ou espaços paramétricos amplos. Já o processamento de linguagem natural ganha interesse crescente enquanto camada de acesso a sistemas mais complexos, sobretudo quando se pretende que utilizadores menos especializados consigam formular intenções ou restrições sem depender de software CAD avançado ou de uma sintaxe demasiado técnica (Ao et al., 2025 (#ref-ao-2025); Menaka et al., 2025 (#ref-menaka-2025); Wang & Hu, 2024 (#ref-wang-2024)).

### IA ao longo do processo de design

Uma das conclusões mais consistentes da literatura é que a IA não atua apenas numa fase isolada do processo projetual. Nas fases iniciais, pode apoiar a pesquisa, a síntese de informação e o enquadramento do problema, ajudando a identificar padrões nas necessidades dos utilizadores, tendências, dados de mercado ou requisitos de contexto. Na ideação, pode ampliar o espaço de procura, reduzir fixação prematura e produzir rapidamente múltiplas alternativas de partida. No desenvolvimento, pode acelerar a iteração, gerar variantes paramétricas e articular a exploração formal às restrições técnicas. Em fases posteriores, pode apoiar a prototipagem, a simulação, a previsão de desempenho e a comparação entre opções concorrentes. Também pode reforçar a comunicação e a documentação, produzindo representações mais rápidas de cenários, conceitos e soluções (Khanolkar et al., 2023 (#ref-khanolkar-2023); Saeidnia & Ausloos, 2024 (#ref-saeidnia-2024); Verganti et al., 2020 (#ref-verganti-2020)).

A eficácia da IA varia consoante a etapa do processo de design. A literatura sugere que o seu valor tende a ser maior em tarefas de exploração divergente, análise extensiva e automatização parcial, enquanto as etapas de convergência, enquadramento contextual, decisão ética e validação final exigem avaliação humana qualificada. A IA pode ampliar o campo de exploração e acelerar a comparação entre alternativas, mas a decisão sobre o que faz sentido desenvolver, para quem, em que contexto e com que consequências permanece uma responsabilidade humana. (Ao et al., 2025 (#ref-ao-2025); Choudhury et al., 2025 (#ref-choudhury-2025); Virós-i-Martin & Selva, 2021 (#ref-viros-i-martin-2021)).

### Papel do designer, riscos e necessidade de supervisão humana

A integração da IA no processo de design exige uma redefinição do papel do designer, sobretudo quando a geração de alternativas, a análise de dados ou a sugestão de soluções passam a ser parcialmente mediadas por sistemas computacionais. Neste contexto, a questão central desloca-se da autoria formal para a capacidade de orientar, interpretar e avaliar criticamente os resultados produzidos. A literatura consultada descreve, assim, uma evolução do designer enquanto gerador exclusivo de forma para um papel mais híbrido, no qual assume funções de orientação, curadoria, interpretação e decisão estratégica. O papel humano torna-se particularmente exigente em tarefas como a formulação do problema, a definição de critérios, a leitura contextual, a seleção entre alternativas e a justificação das decisões. Esta transformação é especialmente relevante em domínios sensíveis, nos quais a adequação ao utilizador, a responsabilidade técnica e a aceitabilidade ética exigem supervisão humana qualificada (Figoli et al., 2022 (#ref-figoli-2022); Kadenhe et al., 2025 (#ref-kadenhe-2025); Virós-i-Martin & Selva, 2021 (#ref-viros-i-martin-2021)).

É também neste ponto que emergem os principais riscos. Um primeiro risco é o enviesamento, já que modelos treinados com dados históricos ou desequilibrados podem reproduzir exclusões, preferências dominantes e padrões culturais pouco representativos. Um segundo risco é a opacidade: muitos sistemas produzem resultados eficazes, mas são difíceis de explicar em termos do seu raciocínio interno, o que dificulta a confiança e a responsabilização. Um terceiro risco é o erro, incluindo respostas plausíveis, mas incorretas, simplificações abusivas e sugestões sem robustez técnica suficiente. A estes somam-se riscos de dependência excessiva, homogeneização formal, enfraquecimento de competências críticas e incerteza quanto à autoria e originalidade dos resultados produzidos com assistência algorítmica (Burnap et al., 2019 (#ref-burnap-2019); Panchal et al., 2019 (#ref-panchal-2019); Yüksel et al., 2023 (#ref-yuksel-2023)).

Por estas razões, a literatura converge para a defesa de modelos com supervisão humana explícita. A integração mais robusta da IA não assenta em autonomia plena, mas em ciclos assistidos, em que o sistema acelera a análise, a geração ou a previsão e o humano mantém autoridade sobre critérios, validação e consequências da decisão. Em termos práticos, isto implica preservar mecanismos de controlo, a comparação entre alternativas, a explicitação de limites, a verificação técnica e a capacidade de recusar ou reformular sugestões produzidas pela máquina. Em design, a supervisão humana não é um complemento opcional; é a condição que transforma a IA em instrumento projetual e não em fonte acrítica de soluções aparentes (Ao et al., 2025 (#ref-ao-2025); Kadenhe et al., 2025 (#ref-kadenhe-2025); Verganti et al., 2020 (#ref-verganti-2020)).

### 2.7 Plataformas digitais e sistemas configuráveis

A evolução recente do desenvolvimento de produto, particularmente em contextos de saúde e de tecnologias de apoio, tem sido acompanhada pelo crescimento de plataformas digitais configuráveis e de sistemas participativos orientados para a personalização. A literatura caracteriza estes sistemas como infraestruturas sociotécnicas que articulam três dimensões principais: enquadramentos conceptuais que legitimam e estruturam a participação dos utilizadores; recursos técnicos de personalização, como parametrização, modularidade e interfaces de configuração;  e fluxos participativos que traduzem a experiência vivida em requisitos, protótipos e iterações de projeto. (Fischer et al., 2004 (#ref-fischer-2004); Hippel & Katz, 2002 (#ref-hippel-2002); Howard et al., 2022 (#ref-howard-2022)).

Em domínios como a reabilitação e as tecnologias de assistência, a personalização é frequentemente descrita como uma necessidade funcional, e não apenas como uma diferenciação de mercado. Isso significa que a adequação do produto ao utilizador pode ser determinante para a segurança, a usabilidade e a adoção sustentada, deslocando o foco do design de uma solução “média” para sistemas capazes de acomodar a variabilidade individual de forma controlada (Fischer et al., 2017 (#ref-fischer-2017); Kerr et al., 2024 (#ref-kerr-2024); Zhu & Zhong, 2022 (#ref-zhu-2022)).

### Fundamentos conceptuais: toolkits, meta-design e end-user development.

Uma linha teórica relevante é a dos “toolkits for user innovation”, que entende os sistemas configuráveis como ferramentas coordenadas e acessíveis que transferem parte do trabalho de design relacionado com as necessidades dos utilizadores, enquanto fabricantes e especialistas retêm tarefas de resolução e de produção. A distinção entre configuradores, centrados em selecionar opções, e toolkits, centrados em desenhar dentro de um espaço de projeto delimitado, é central: a participação pode variar entre escolher alternativas pré-definidas e efetivamente criar configurações em um ambiente com regras e feedback (Franke & Hippel, 2002 (#ref-franke-2002); Hippel & Katz, 2002 (#ref-hippel-2002)).

O meta-design aprofunda esta lógica ao defender a participação “em uso”, estabelecendo condições técnicas e sociais para que os utilizadores se tornem co-designers e o sistema evolua ao longo do tempo. O modelo Seeding, Evolutionary Growth, and Reseeding formaliza este processo como alternância entre “sementes” iniciais, criadas por especialistas, evolução por meio do desenvolvimento do utilizador e reestruturações periódicas que consolidam as aprendizagens e reorganizam o sistema (Costabile et al., 2007 (#ref-costabile-2007); Fischer et al., 2004 (#ref-fischer-2004)).

Para enquadrar estes fundamentos de forma mais operacional, a Figura 2.7 mostra um modelo de configuração da participação em living labs, útil porque desloca a discussão da participação como princípio abstrato para a participação como estrutura desenhável.

![](projecto-completo_media/image08.png)

Figura 2.7 — Modelo de processo para configurar participação em ecossistemas de inovação e cocriação.

Fonte original: Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. [https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488](https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488)

A literatura identifica, contudo, o risco de sobrecarga participativa, entendido como a transferência excessiva de trabalho, responsabilidade e decisão para os utilizadores. Este risco exige mecanismos de apoio, curadoria e reutilização que tornem a participação sustentável (Fischer et al., 2017 (#ref-fischer-2017)).

Em paralelo, o conceito de Software Shaping Workshop operacionaliza o meta-design, entendido como uma abordagem que cria condições técnicas e sociais para que utilizadores finais participem ativamente na adaptação e evolução dos sistemas que utilizam. Neste enquadramento, o Software Shaping Workshop funciona como uma “oficina virtual”: um ambiente digital composto por ferramentas familiares, ajustadas à cultura, às práticas e às competências de uma comunidade específica. Em contextos de reabilitação e assistência, este paradigma manifesta-se em sistemas que fornecem a cuidadores e terapeutas interfaces do tipo editor, permitindo adaptar scripts, exercícios e conteúdos sem necessidade de programação especializada, respondendo de forma pragmática às necessidades de personalização (Costabile et al., 2007 (#ref-costabile-2007); Fischer et al., 2017 (#ref-fischer-2017)).

Esta transição entre princípio e operação pode ser resumida pelos elementos nucleares apresentados na Tabela 2.2, que sistematiza dimensões recorrentes no desenho de participação mediada: quando participar, quem participa, por quais canais, através de quais pontos de contacto e com que mecanismos de motivação.

Tabela 2.2 — Elementos centrais na configuração da participação em sistemas configuráveis

| Fase e propósito | Em que momento participa o utilizador e com que objetivo |

| --- | --- |

| Participantes | Que perfis participam, em que número e com que papel |

| Formato | Que canais, espaços e métodos suportam a colaboração |

| Contacto | Como se recrutam participantes e como se mantém a relação |

| Gestão da motivação | Que fatores promovem adesão e que barreiras dificultam continuidade |

Fonte adaptada. Referência original: Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. [https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488](https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488)

### Mecanismos de personalização: modularidade, parametrização e adaptação individualizada

A literatura sintetiza a personalização por meio de mecanismos recorrentes que diferem quanto a “quem configura”, “o que é configurável” e “quando se configura”. Três mecanismos destacam-se pela relevância para sistemas protésicos e dispositivos médicos personalizados:

1. Seleção modular de componentes: a personalização é obtida por meio da combinação de módulos interoperáveis, permitindo adaptar a funcionalidade por meio de combinações e substituições. A modularidade surge como estratégia para conciliar personalização, reutilização e expansão em ecossistemas de produto (Dechev et al., 2023 (#ref-dechev-2023); Peters & Richter, 2023 (#ref-peters-2023)).

2. Configuração paramétrica: o utilizador, ou um intermediário clínico, fornece entradas num espaço de parâmetros e o sistema gera automaticamente artefactos de design, como ficheiros CAD, com base nesses valores. Este mecanismo é mais adequado quando a personalização depende de atributos mensuráveis, ligando diretamente dados antropométricos e cinemáticos a variáveis de projeto (Kuhl et al., 2020 (#ref-kuhl-2020); Zhu & Zhong, 2022 (#ref-zhu-2022)).

3. Tailoring por toolkit/editor: a personalização ocorre em tempo de uso, permitindo editar conteúdos, instruções, rotinas de treino ou componentes informacionais associados ao produto ou serviço. Em saúde, este mecanismo é particularmente relevante em plataformas de reabilitação e de telereabilitação, nas quais a adaptação de exercícios e de objetivos faz parte do cuidado contínuo (Cole, 2011 (#ref-cole-2011); Fischer et al., 2017 (#ref-fischer-2017)).

A seleção do mecanismo mais adequado depende da forma como o conhecimento relevante se distribui entre utilizadores, designers, profissionais técnicos ou clínicos e sistemas digitais. A modularidade é adequada quando as necessidades podem ser expressas através da combinação de módulos previamente definidos; a parametrização torna-se mais eficaz quando existem dados mensuráveis que podem ser traduzidos em variáveis de projeto; e os kits de ferramentas são particularmente relevantes quando a adaptação contínua em contexto é crítica e quando o utilizador ou um intermediário dispõe de conhecimento situado para ajustar o sistema. (Hippel & Katz, 2002 (#ref-hippel-2002); Peters & Richter, 2023 (#ref-peters-2023); Zhu & Zhong, 2022 (#ref-zhu-2022)).

### Workflows participativos e infraestruturas remotas

Uma característica transversal é o recurso crescente à participação remota e aos workflows digitalmente mediados. A literatura documenta sessões de co-design por videoconferência, workshops online e processos de co-manufactura à distância, em que o ciclo “definir → prototipar → fabricar → testar” ocorre com envio de protótipos para experimentação no contexto real do utilizador. Estes modelos são particularmente relevantes em tecnologias assistivas, nas quais a avaliação em contexto e a adaptação iterativa são determinantes para a adequação funcional e a aceitação (Dexter et al., 2013 (#ref-dexter-2013); Thorsen et al., 2023 (#ref-thorsen-2023)).

No entanto, a literatura sublinha que a tecnologia, por si só, não é suficiente. A eficácia destes sistemas depende de estruturas de governação, isto é, da definição clara de quem decide, o que decide e em que momento do processo. Depende igualmente da mediação exercida por clínicos, designers ou técnicos, bem como de mecanismos que permitam gerir a carga de trabalho, a comunicação e a coordenação entre intervenientes. Em modelos abertos e distribuídos, podem surgir riscos de incumprimento de compromissos e atrasos decorrentes da ausência de responsabilização clara, o que exige a definição explícita de regras, expectativas e responsabilidades. (Frangos et al., 2016 (#ref-frangos-2016); Hussaini et al., 2023 (#ref-hussaini-2023); Kerr et al., 2024 (#ref-kerr-2024)).

### Aplicações em saúde, reabilitação e próteses

Em saúde, plataformas baseadas em digital twins são descritas como sistemas de serviço personalizados que conectam participantes por meio da nuvem, integrando sensores, parâmetros de movimento e métricas de desempenho. Embora apresentem correlações elevadas em cenários controlados, a literatura assinala degradação de desempenho em contextos mais complexos, revelando limites entre modelos e a variabilidade real do movimento humano. Estes sistemas mostram o potencial de integrar personalização, fabrico digital e monitorização remota, mas também deixam claro que a robustez do modelo depende da qualidade dos dados e da diversidade dos cenários de uso (Mikołajewski et al., 2023 (#ref-mikoajewski-2023); Zhu & Zhong, 2022 (#ref-zhu-2022)).

Na reabilitação, plataformas de virtual coaching, serious games configuráveis e modelos de cocriação tecnológica são apresentados como formas de personalizar os tratamentos com base no estado clínico, nos objetivos terapêuticos e no feedback do utilizador. As avaliações indicam boa usabilidade e experiência do utilizador quando a participação é integrada no ciclo de desenvolvimento e mostram que a personalização não se limita à interface, estendendo-se à seleção de exercícios, ao ritmo do programa e à mediação por profissionais de saúde (Cole, 2011 (#ref-cole-2011); Kerr et al., 2024 (#ref-kerr-2024); Seregni et al., 2021 (#ref-seregni-2021)).

No contexto protésico e assistivo, evidencia-se a relevância dos ecossistemas modulares e das cadeias de aprendizagem distribuída. Estudos sobre próteses pediátricas, serviços de reabilitação assistiva e modelos como o Victoria Hand Project mostram que a personalização pode combinar prototipagem iterativa, módulos intercambiáveis, criação digital de encaixes e circulação de feedback entre locais clínicos e equipas centrais de desenvolvimento. Neste enquadramento, a plataforma deixa de ser apenas uma interface de configuração e passa a funcionar como infraestrutura organizacional de aprendizagem e de atualização contínua (Dechev et al., 2023 (#ref-dechev-2023); Howard et al., 2022 (#ref-howard-2022); Sims et al., 2017 (#ref-sims-2017)).

Em contextos de baixos recursos, a literatura reforça que a impressão 3D pode ser um facilitador importante, mas só produz benefícios quando integrada a infraestruturas de apoio, confiança, manutenção e capacitação técnica. A simples disponibilização de tecnologia de fabrico não garante soluções adequadas nem adoção sustentada, pelo que os modelos participativos e a mediação local assumem um papel determinante na tradução do potencial técnico em valor real para os utilizadores (Hussaini et al., 2023 (#ref-hussaini-2023); Thorsen et al., 2023 (#ref-thorsen-2023)).

### Limitações e lacunas: sustentabilidade, adoção e equilíbrio entre normalização e improviso

Apesar do potencial das plataformas configuráveis e dos workflows participativos para apoiar a personalização de dispositivos médicos e tecnologias de apoio, a evidência empírica disponível baseia-se frequentemente em amostras reduzidas e em estudos de caso, o que limita a generalização dos resultados (Frangos et al., 2016 (#ref-frangos-2016); Howard et al., 2022 (#ref-howard-2022); Thorsen et al., 2023 (#ref-thorsen-2023)). Para além disso, a literatura identifica três tensões estruturais relevantes.

A primeira diz respeito à sustentabilidade da participação: processos participativos prolongados ou mal distribuídos podem gerar sobrecarga, fadiga e eventual desistência por parte dos utilizadores, exigindo mecanismos de apoio, curadoria e redistribuição da carga entre utilizadores, especialistas e intermediários técnicos ou clínicos (Fischer et al., 2017 (#ref-fischer-2017)).

A segunda tensão situa-se entre normalização e personalização. Em domínios regulados, a adaptação individualizada deve preservar rastreabilidade, segurança e qualidade, o que pode entrar em conflito com ajustamentos locais necessários para responder a necessidades específicas ou contextuais (Costabile et al., 2007 (#ref-costabile-2007); Fischer et al., 2004 (#ref-fischer-2004)).

A terceira tensão relaciona-se com a adoção e o valor efetivamente realizado. A literatura sobre personalização em massa regista dificuldades recorrentes na conversão e adoção de configuradores; por analogia, em contextos de saúde e de tecnologias de apoio, a configurabilidade não garante aceitação sem alinhamento com expectativas, confiança dos intervenientes e integração nos serviços existentes (Akasaka et al., 2022 (#ref-akasaka-2022); Frangos et al., 2016 (#ref-frangos-2016)).

### 2.8 Análise crítica do estado da arte e lacunas identificadas

A distância entre o potencial técnico destas abordagens e a sua consolidação prática torna-se particularmente visível quando se analisam os níveis de prontidão tecnológica descritos na literatura. A Figura 2.8 apresenta a distribuição dos estudos por nível de prontidão tecnológica, ou Technology Readiness Level (TRL), evidenciando que muitos contributos permanecem concentrados em fases ainda afastadas de uma adoção ampla e sustentada.

![](projecto-completo_media/image09.png)

Figura 2.8 — Distribuição dos estudos por nível de prontidão tecnológica (TRL) e categoria de aplicação. O gráfico distingue estudos sobre próteses em geral, próteses de membro inferior produzidas por impressão 3D (LL 3DP), próteses de membro inferior desenvolvidas com recurso a CAD/CAM (LL CAD/CAM), outras abordagens aplicadas ao membro inferior (LL other), próteses de membro superior produzidas por impressão 3D (UL 3DP) e outros casos não enquadrados nas categorias anteriores.

Fonte original: Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517

A síntese das secções anteriores evidencia um panorama marcado por avanços técnicos significativos, mas também por limitações estruturais persistentes na investigação e no desenvolvimento de próteses e de tecnologias de apoio. Um tema transversal é o desfasamento entre o desenvolvimento tecnológico e a sua validação empírica. Muitos contributos permanecem em fase de protótipo, com testes realizados em amostras reduzidas e por períodos curtos, o que limita a demonstração da sua eficácia, segurança e adequação em contextos reais de utilização. (Chadwell et al., 2020 (#ref-chadwell-2020); Samuelsson et al., 2012 (#ref-samuelsson-2012); Windrich et al., 2016 (#ref-windrich-2016)).

A predominância de estudos com amostras reduzidas, curta duração e validação limitada dificulta a comparação entre soluções, a generalização de conclusões e a tradução de melhorias laboratoriais em benefícios consistentes na vida quotidiana. (Hafner & Sawers, 2016 (#ref-hafner-2016); Samuelsson et al., 2012 (#ref-samuelsson-2012)).

### Lacuna 1 — Validação empírica limitada e fraca transposição para contextos reais de utilização

A revisão da literatura aponta repetidamente para a ausência de estudos comparativos consistentes e de ensaios clínicos que confrontem dispositivos avançados com soluções convencionalmente prescritas, particularmente no caso de próteses ativas e externamente alimentadas. Em vários subdomínios, observa-se uma dependência significativa de protótipos e de amostras reduzidas, o que limita as inferências sobre eficácia, segurança e valor clínico. Em paralelo, verifica-se a predominância de avaliações laboratoriais e de tarefas pouco representativas, que não captam adequadamente o desempenho em contextos reais de utilização, marcados pela variabilidade dos ambientes, dos objetos manipulados e das exigências funcionais (Ghillebert et al., 2019 (#ref-ghillebert-2019); Samuelsson et al., 2012 (#ref-samuelsson-2012); Windrich et al., 2016 (#ref-windrich-2016)).

Esta lacuna é particularmente relevante porque a adaptação, a aprendizagem e o eventual abandono de uma prótese ocorrem ao longo do tempo e em contextos quotidianos, como o trabalho, a habitação e o espaço público. Quando a evidência disponível se baseia em períodos de observação curtos, torna-se difícil compreender trajetórias de adoção, padrões de uso e o surgimento progressivo de problemas relacionados com conforto, manutenção ou integração funcional (Chadwell et al., 2020 (#ref-chadwell-2020); Samuelsson et al., 2012 (#ref-samuelsson-2012)).

### Lacuna 2 — Desalinhamento entre necessidades identificadas, métricas objetivas, e qualidade de vida

A literatura evidencia uma articulação insuficiente entre as necessidades expressas pelos utilizadores, como conforto, controlo intuitivo, aparência e participação social; os indicadores objetivos habitualmente medidos, como desempenho em testes funcionais, parâmetros biomecânicos e métricas instrumentadas de uso da prótese; e os resultados finais desejáveis, como autonomia e qualidade de vida. As revisões salientam que estas necessidades são contextuais e interdependentes, e que as medições laboratoriais nem sempre refletem tarefas relevantes do quotidiano, contribuindo para contradições entre resultados subjetivos e objetivos (Cordella et al., 2016 (#ref-cordella-2016); Manz et al., 2022 (#ref-manz-2022)).

Esta desarticulação tem implicações diretas para o design. A existência de métricas ecologicamente válidas e sensíveis às prioridades do utilizador é essencial para orientar decisões de projeto para benefícios significativos e sustentados. Como consequência, melhorias técnicas isoladas podem produzir ganhos limitados em termos de aceitação, integração funcional ou uso continuado da prótese (Manz et al., 2022 (#ref-manz-2022); Samuelsson et al., 2012 (#ref-samuelsson-2012)).

### Lacuna 3 — Persistência de problemas na interface corpo–prótese e no ajuste individualizado

Apesar dos avanços em componentes técnicos e sistemas de controlo, a literatura continua a identificar a interface corpo–prótese como um ponto crítico ainda insuficientemente resolvido. Problemas de ajuste, desconforto, irritação cutânea e dificuldade de adaptação persistem como fatores determinantes de insatisfação e abandono. Nas revisões analisadas, a personalização é frequentemente descrita como insuficiente ou metodologicamente frágil, sendo a evidência difícil de sintetizar devido à variabilidade das intervenções e ao registo incompleto dos processos e resultados (Alluhydan et al., 2023 (#ref-alluhydan-2023); Baldock et al., 2023 (#ref-baldock-2023); Richardson & Dillon, 2017 (#ref-richardson-2017)).

Um aspeto estruturante desta lacuna é a ausência de fluxos metodológicos consistentes e acessíveis que articulem medição, decisão de projeto e validação. Esta ausência dificulta a utilização de dados objetivos para orientar ajustes individualizados. Mesmo quando são propostas soluções baseadas em sensores e na monitorização do uso, persistem barreiras práticas, como o custo, a autonomia da bateria, a disponibilidade de equipamentos e a necessidade de formação técnica, o que limita a sua adoção como prática clínica regular (Chadwell et al., 2020 (#ref-chadwell-2020); Richardson & Dillon, 2017 (#ref-richardson-2017)).

### Lacuna 4 — Evolução limitada das estratégias de controlo e da interação utilizador–prótese

No caso das próteses de membro superior, algumas revisões apontam para uma evolução limitada das estratégias de controlo em aplicações comerciais, marcada por uma progressão lenta desde as primeiras abordagens desenvolvidas no século XX. Persistem dificuldades relacionadas com a robustez dos sistemas e com a sua transferência entre cenários laboratoriais e contextos reais de utilização, bem como desafios associados ao esforço cognitivo, ao tempo de aprendizagem e à inconsistência do desempenho em situações quotidianas (Cordella et al., 2016 (#ref-cordella-2016); Marinelli et al., 2022 (#ref-marinelli-2022)).

Esta lacuna não é apenas técnica. Reflete também uma conceptualização ainda insuficiente da interação utilizador–prótese enquanto sistema integrado, no qual controlo, informação sensorial, treino e contexto de uso devem ser considerados de forma articulada (Domínguez-Ruiz et al., 2023 (#ref-dominguez-ruiz-2023); Marinelli et al., 2022 (#ref-marinelli-2022)).

### Lacuna 5 — Acesso, custo, manutenção e inequidades sistémicas

A acessibilidade surge como um constrangimento central e persistente, tanto em contextos de baixos recursos quanto em sistemas de saúde mais robustos. Revisões identificam barreiras associadas a custos elevados, à necessidade de formação especializada, a atrasos na prestação de cuidados e a pressões sistémicas que levam os utilizadores a negociar intensivamente para obter soluções adequadas. Em contextos de baixos e médios rendimentos, enfatizam-se ainda problemas de durabilidade e de manutenção, com compromissos claros: soluções biomecanicamente mais sofisticadas podem ser mais frágeis e difíceis de manter, comprometendo a sustentabilidade do uso (Alluhydan et al., 2023 (#ref-alluhydan-2023); Andrysek, 2010 (#ref-andrysek-2010); Baumann & Maria, 2023 (#ref-baumann-2023)).

Assim, a inovação pode agravar as inequidades ao introduzir dependências de infraestrutura, de apoio técnico e de cadeias de fornecimento indisponíveis para uma parcela significativa da população (Andrysek, 2010 (#ref-andrysek-2010); Segura et al., 2024 (#ref-segura-2024)).

### Lacuna 6 — Envolvimento do utilizador e registo metodológico insuficiente

O envolvimento do utilizador permanece uma fragilidade metodológica e ética no desenvolvimento de próteses. As revisões relacionam explicitamente processos pouco ajustados às necessidades individuais dos pacientes com o abandono dos dispositivos e com a dificuldade em responder a prioridades relevantes de uso. Em várias áreas, identifica-se ainda a ausência de métodos qualitativos sistemáticos para captar a experiência, a aceitabilidade e os fatores de rejeição, mesmo em componentes diretamente associados ao conforto, como os liners. Esta limitação reduz a compreensão dos fatores que condicionam a adoção, a continuidade de uso e a adequação da prótese à vida quotidiana (Marinelli et al., 2022 (#ref-marinelli-2022); Richardson & Dillon, 2017 (#ref-richardson-2017); Walker et al., 2019 (#ref-walker-2019)).

Adicionalmente, a heterogeneidade metodológica e a ausência de critérios comuns de avaliação, como escalas partilhadas de utilidade e satisfação, dificultam a síntese dos resultados e a realização de meta-análises, mantendo o campo fragmentado e com baixa comparabilidade entre estudos (Cordella et al., 2016 (#ref-cordella-2016); Hafner & Sawers, 2016 (#ref-hafner-2016); Richardson & Dillon, 2017 (#ref-richardson-2017)).

### Implicações para esta investigação

Em conjunto, estas lacunas apontam para a necessidade de abordagens que:

- reforcem a ligação entre personalização e validação empírica, através de fluxos integrados de aquisição de dados, geração de variantes e avaliação;

- privilegiem avaliações ecologicamente válidas e longitudinais, aproximando as métricas de desempenho dos resultados relacionados com participação, autonomia e qualidade de vida;

- tratem a interface corpo–prótese e o conforto como requisitos estruturantes do processo de projeto, e não como ajustes posteriores;

- incorporem o envolvimento do utilizador como elemento contínuo, documentável e passível de análise, articulando métodos qualitativos e quantitativos;

- considerem a acessibilidade, a manutenção e o contexto de serviço como dimensões constitutivas do problema de design (Anderson et al., 2024 (#ref-anderson-2024); Baumann & Maria, 2023 (#ref-baumann-2023); Chadwell et al., 2020 (#ref-chadwell-2020)).

## Capítulo 3 — Metodologia de Investigação

### 3.1 Enquadramento metodológico e abordagem Research Through Design

A presente investigação inscreve-se numa metodologia de natureza aplicada, estruturada no enquadramento do Research Through Design (RTD). Esta abordagem reconhece o design não apenas como prática projetual, mas também como meio de produção de conhecimento, no qual conceber, experimentar, prototipar e refletir constituem simultaneamente atos de criação e de investigação (Frayling, 1994 (#ref-frayling-1994); Zimmerman et al., 2007 (#ref-zimmerman-2007)).

O objetivo principal do projeto é gerar conhecimento por meio da prática do design industrial, articulando o processo criativo, o desenvolvimento técnico e a reflexão crítica sobre o papel do design como mediador entre a tecnologia e a experiência humana. Neste contexto, propõe-se o desenvolvimento de um sistema de design paramétrico assistido por inteligência artificial para a criação de próteses personalizadas de membros superiores, explorando a interligação entre design industrial, design para a fabricação aditiva (DfAM) e metodologias de design inclusivo.

A pertinência da abordagem RTD justifica-se pela natureza exploratória e iterativa do problema em estudo. A personalização de próteses envolve variáveis anatómicas, funcionais, simbólicas e técnicas que dificilmente podem ser plenamente compreendidas apenas por via teórica. A produção de protótipos, a modelação paramétrica e a integração de algoritmos de apoio ao design constituem, neste projeto, instrumentos epistemológicos que permitem testar hipóteses, revelar constrangimentos e reformular decisões projetuais. Neste sentido, o artefacto não é entendido apenas como resultado final, mas como um veículo de investigação, tornando visíveis decisões, compromissos e relações entre requisitos que dificilmente emergiriam num modelo exclusivamente descritivo ou analítico (Zimmerman et al., 2007 (#ref-zimmerman-2007)).

A investigação é igualmente estruturada segundo a lógica processual do modelo Double Diamond, articulando momentos de divergência e de convergência nas fases de descoberta, definição, desenvolvimento e entrega. Esta estrutura não é aplicada de forma linear, mas como orientação para ciclos iterativos de exploração, síntese e validação, coerentes com a combinação entre pesquisa, formulação do problema, geração de alternativas, prototipagem e teste que caracteriza a prática do design contemporâneo (Design Council, 2020 (#ref-design-council-2020)).

Esta articulação entre investigação, prototipagem e participação encontra um precedente relevante em processos interdisciplinares de desenvolvimento de próteses impressas em 3D. A Figura 3.1 sintetiza um fluxo de desenvolvimento em que avaliação clínica, definição de requisitos, prototipagem e teste com utilizador são tratados como etapas interdependentes, aproximando a metodologia do presente projeto de uma lógica iterativa e situada de Research Through Design (Silva et al., 2018 (#ref-silva-alcara-2018)).

![](projecto-completo_media/image10.png)

Figura 3.1 — Processo interdisciplinar de desenvolvimento de uma prótese de membro superior impressa em 3D.

Fonte original: Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

### 3.2 O design industrial como prática investigativa

O projeto parte do entendimento do design industrial como campo de prática e investigação, de natureza técnica e social, capaz de mediar entre a inovação tecnológica e a experiência humana. No domínio das próteses de membros superiores, esta mediação assume particular relevância, uma vez que o objeto projetado intervém diretamente na corporeidade, na autonomia e na identidade do utilizador. Esta perspetiva relaciona-se com a noção de designerly ways of knowing, formulada por Nigel Cross para reconhecer o design como uma disciplina com modos próprios de conhecer, formular problemas e desenvolver soluções através da prática projetual. Neste sentido, o conhecimento produzido pelo design não resulta apenas da análise externa do problema, mas também da experimentação material, da geração de alternativas, da prototipagem e da articulação entre exigências funcionais, formais, técnicas e humanas (Cross, 1982 (#ref-cross-1982)).

Partindo deste enquadramento, a investigação assume o desenvolvimento de um sistema paramétrico assistido por inteligência artificial como meio para explorar formas mais configuráveis, reprodutíveis e acessíveis de personalização protésica. O contributo de investigação do projeto não reside apenas na obtenção de uma solução funcional, mas também na explicitação dos critérios, das relações paramétricas e dos mecanismos de decisão que estruturam o processo, tornando-o analisável, aberto à revisão crítica e potencialmente transferível para outros contextos de desenvolvimento.

A hipótese principal sustenta que a integração de design paramétrico e de ferramentas de inteligência artificial permite desenvolver próteses mais adequadas às necessidades anatómicas e funcionais dos utilizadores, tornando o processo de personalização mais acessível e escalável, especialmente em contextos economicamente desfavorecidos. As hipóteses secundárias aprofundam esta perspetiva, sugerindo que a combinação de princípios de design inclusivo, DfAM e processos participativos pode melhorar a usabilidade, o conforto e a aceitação, ao mesmo tempo que reduz a dependência de especialistas.

### 3.3 Estrutura metodológica do projeto

A metodologia organiza-se em três fases interligadas — conceptual, metodológica e empírica — que se desenvolvem de forma sequencial, mantendo, contudo, a natureza iterativa própria do processo de design. Esta estrutura funciona como uma adaptação do enquadramento de Research Through Design a um problema de design de produto com forte componente digital e experimental, preservando a alternância entre abertura exploratória e convergência projetual orientada por critérios, característica do modelo Double Diamond. (Design Council, 2020 (#ref-design-council-2020); Zimmerman et al., 2007 (#ref-zimmerman-2007)).

A fase conceptual corresponde ao momento de enquadramento teórico e de problematização. Neste estágio, procede-se à revisão crítica da literatura nas áreas de design paramétrico, fabrico aditivo, design inclusivo, antropometria aplicada e integração de inteligência artificial no processo de design. Paralelamente, realiza-se uma análise comparativa de soluções open-source existentes no domínio das próteses impressas em 3D, identificando abordagens formais, estruturais e tecnológicas, bem como limitações quanto à personalização e à reprodutibilidade. Foi também nesta fase que se estruturou uma base local consolidada de dados antropométricos da mão, a partir de medições publicadas e de bases de dados antropométricas, de modo a apoiar a definição dos parâmetros iniciais do sistema e a comparação entre perfis populacionais. O resultado desta fase é a consolidação de um quadro conceptual alinhado com as questões de investigação e com a hipótese central.

A fase metodológica corresponde à definição e implementação do sistema paramétrico assistido por IA. Nesta etapa especifica-se a arquitetura da plataforma digital, integrando módulos de configuração paramétrica, bases de dados antropométricas e algoritmos de apoio à interpretação de medidas e à otimização geométrica. Desenvolvem-se protótipos digitais iterativos, testando relações formais e funcionais e avaliando a viabilidade de fabrico segundo os princípios de DfAM. É nesta fase que a investigação se aproxima mais claramente de uma lógica de research by making, em que as decisões de modelação, parametrização e iteração constituem simultaneamente desenvolvimento técnico e produção de conhecimento metodológico.

A fase empírica materializa a operacionalização do conhecimento gerado. Os modelos paramétricos são testados com diferentes perfis antropométricos provenientes de bases de dados públicas, e as configurações resultantes dos testes de perfil são exportadas para fabrico e produzidas por impressão 3D em PLA e PETG. Esta fase permite avaliar a passagem do perfil simulado para a geometria exportada e desta para o protótipo físico, observando a exequibilidade de impressão, a integridade estrutural preliminar, a montagem, a ajustabilidade e a coerência formal perante variações dimensionais.

### 3.4 Métodos de recolha e análise de dados

A investigação recorre a métodos qualitativos e experimentais, coerentes com a natureza prática do RTD. A recolha de dados realiza-se em diferentes níveis, combinando análise documental, comparação de precedentes, construção paramétrica, prototipagem iterativa e reflexão crítica sobre os resultados de cada ciclo.

Num primeiro nível, procede-se à análise documental e à revisão da literatura, o que permite identificar lacunas, requisitos técnicos e critérios de avaliação. Num segundo nível, realiza-se a análise comparativa de projetos existentes, com foco nas suas soluções construtivas, nos sistemas de ajuste e nas estratégias de personalização.

Durante o desenvolvimento do sistema paramétrico, os dados assumem natureza técnica e projetual, incluindo parâmetros geométricos, relações dimensionais, tempos de fabrico, consumo de material e desempenho estrutural dos protótipos. Estes dados são analisados de forma iterativa, permitindo reformular o modelo paramétrico e otimizar o seu desempenho.

Na fase de prototipagem, a análise incide sobre os critérios de exequibilidade de fabrico, robustez estrutural preliminar, coerência dimensional, facilidade de montagem e comportamento material inicial. Os modelos exportados a partir dos testes de perfil são preparados para impressão, fatiados e materializados em PLA e PETG, permitindo verificar se a geometria gerada pelo sistema se mantém imprimível, manipulável e coerente depois da transição do ambiente digital para o objeto físico. Não são recolhidos dados pessoais ou biométricos de utilizadores reais; utilizam-se exclusivamente conjuntos de dados antropométricos públicos, o que delimita o âmbito empírico ao domínio técnico e projetual. Entre estes, destaca-se a base local consolidada de medidas da mão e do membro superior distal, usada como infraestrutura intermédia para a seleção, comparação e normalização de medidas relevantes para a parametrização geométrica. A organização dos dados preserva informação sobre país, amostra, tipo de medida, estatística, fonte documental e granularidade dos subconjuntos analisados, tornando explícitas a cobertura e as limitações de cada fonte antes da sua tradução em parâmetros de projeto.

Embora o presente estudo não utilize participantes reais, a literatura metodológica da área ajuda a esclarecer como medições lineares e procedimentos de ajuste são normalmente operacionalizados em contextos aplicados. A Figura 3.2 ilustra esse tipo de recolha dimensional orientada para fabrico, servindo aqui como precedente metodológico para a tradução de medidas em parâmetros de projeto.

![](projecto-completo_media/image11.png)

Figura 3.2 — Exemplo de recolha dimensional para ajuste de prótese impressa em 3D.

Fonte original: Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

### 3.5 Critérios de avaliação e limitações metodológicas

A avaliação do sistema desenvolvido baseia-se em critérios técnicos, funcionais e metodológicos. Entre os principais critérios consideram-se a capacidade de personalização paramétrica, a consistência dimensional perante diferentes perfis antropométricos, a viabilidade de fabrico por impressão 3D, a robustez estrutural e a clareza do processo de configuração. Estes critérios visam avaliar não só o desempenho do artefacto, mas também a qualidade do próprio processo de design enquanto dispositivo de investigação, nomeadamente a sua capacidade de tornar explícitas as decisões, testar alternativas e produzir aprendizagem transferível (Zimmerman et al., 2007 (#ref-zimmerman-2007)).

No caso específico da parametrização assistida por IA, a avaliação foi organizada em dois patamares. O primeiro incidiu sobre a plausibilidade numérica das sugestões, verificando conformidade com o esquema de parâmetros, respeito pelos intervalos mínimos e máximos, proporcionalidade entre dedos, adequação etária e coerência de lateralidade em amputações unilaterais. O segundo prolongou essa verificação até à geometria exportada, testando se os valores sugeridos eram efetivamente aplicados nos modelos OpenSCAD/WebAssembly e se os ficheiros 3MF e STL resultantes apresentavam escalas coerentes com os perfis antropométricos simulados. Esta separação permite distinguir a validade interna do fluxo paramétrico da validação clínica, que permanece fora do âmbito empírico desta investigação.

Adicionalmente, são considerados critérios relacionados com a acessibilidade e a replicabilidade, avaliando-se em que medida o sistema pode ser utilizado por técnicos não especializados ou por comunidades locais com recursos limitados. A dimensão ética é igualmente ponderada, particularmente no que se refere à promoção da autonomia e da dignidade do utilizador.

Importa, contudo, reconhecer limitações metodológicas. A ausência de testes com utilizadores reais impede a validação clínica e a avaliação aprofundada da experiência de uso subjetiva. A utilização de dados antropométricos secundários limita a verificação empírica da adaptação individual. Por fim, a integração de inteligência artificial é circunscrita a funções de apoio à configuração e otimização geométricas, não abrangendo sistemas clínicos ou biomédicos avançados. Acresce que a própria estrutura iterativa adotada, embora adequada à exploração projetual, não produz, por si só, evidência clínica ou generalização estatística, exigindo que os resultados sejam lidos como contributo metodológico assente no desenvolvimento de um protótipo, e não como validação final de eficácia em contexto de uso.

Estas limitações são assumidas como enquadramento do estudo, que se posiciona prioritariamente no domínio do design de produto e da investigação metodológica, contribuindo para a reflexão sobre o papel do design paramétrico e da inteligência artificial na personalização de dispositivos de apoio.

## Capítulo 4 — Desenvolvimento do Modelo Paramétrico

### 4.1 Definição do problema de design e requisitos

Como referido anteriormente, o desenvolvimento de próteses de membro superior é enquadrado na literatura como um problema de elevada complexidade, situado na interseção entre desempenho biomecânico, integração corpo–dispositivo e experiência vivida do utilizador (Cordella et al., 2016 (#ref-cordella-2016); Guo, 2025 (#ref-guo-2025); Peerdeman et al., 2011 (#ref-peerdeman-2011)). Este desafio não pode ser reduzido à mera replicação formal da mão ou do segmento ausente. Implica, pelo contrário, a conceção de dispositivos capazes de conciliar funcionalidade, conforto, leveza, funcionamento consistente, controlo inteligível, aceitabilidade estética e custos compatíveis com a produção, adaptação, manutenção e acesso continuado à prótese, num contexto em que continuam a registar-se taxas elevadas de rejeição e abandono.

A literatura associa estas taxas, de forma recorrente, a desconforto no encaixe, peso excessivo, limitações funcionais, baixa robustez e estratégias de controlo pouco intuitivas, evidenciando uma lacuna persistente entre a capacidade tecnológica dos dispositivos e as necessidades reais de uso (Biddiss et al., 2007 (#ref-biddiss-2007); Cordella et al., 2016 (#ref-cordella-2016); Peerdeman et al., 2011 (#ref-peerdeman-2011)).

Neste contexto, a definição de requisitos não constitui apenas uma etapa técnica de especificação, mas um processo de tradução entre problemas de uso, limitações clínicas, possibilidades tecnológicas e condições concretas de adoção. Assim, os requisitos considerados no projeto de uma prótese de membro superior devem ser entendidos como categorias interdependentes, que procuram responder simultaneamente ao desempenho funcional do dispositivo, à sua adequação ao corpo, à experiência quotidiana do utilizador e à viabilidade do seu desenvolvimento e manutenção.

A partir desta leitura, os requisitos de projeto podem ser organizados em categorias interdependentes. Os requisitos funcionais incluem padrões de preensão, graus de liberdade, amplitude de movimento, força, velocidade e capacidade de realizar atividades da vida diária. Os requisitos ergonómicos assumem particular centralidade, destacando-se o conforto, o baixo peso, a usabilidade, a facilidade de colocação e remoção da prótese e a adequação ao uso quotidiano prolongado. Ao nível técnico, definem-se parâmetros relativos a atuadores, sistemas de transmissão, sensores, estratégias de controlo, fontes de energia e seleção de materiais com propriedades mecânicas adequadas e compatibilidade biológica. Em termos de fabrico, emergem exigências de modularidade, reparabilidade, custo controlado e compatibilidade com fluxos de fabrico digital e aditivo. Acrescem ainda requisitos estéticos e psicossociais, relacionados com a identidade, a aceitação social e a incorporação corporal, cuja relevância é reiterada tanto por utilizadores como por clínicos e familiares (Biddiss et al., 2007 (#ref-biddiss-2007); Brack & Amalu, 2021 (#ref-brack-2021); Henao et al., 2025 (#ref-henao-2025); Walker et al., 2019 (#ref-walker-2019)).

A tradução destas necessidades em parâmetros mensuráveis e programáveis constitui um ponto crítico no desenvolvimento de dispositivos médicos personalizados. Tal tradução implica converter necessidades qualitativas, como conforto, segurança ou facilidade de controlo, em especificações técnicas quantificáveis, como limites de peso, distribuição admissível de pressões, torque necessário nas articulações, número de graus de liberdade, autonomia energética ou tolerâncias dimensionais. A literatura sobre requisitos em próteses de membro superior mostra que este passo é decisivo, pois as prioridades dos utilizadores nem sempre coincidem com os indicadores habitualmente privilegiados pela engenharia, o que exige uma explicitação rigorosa das correspondências entre a necessidade, o critério de avaliação e a decisão de projeto (Cordella et al., 2016 (#ref-cordella-2016); Hofmann et al., 2016 (#ref-hofmann-2016); Jones et al., 2023 (#ref-jones-2023)). No desenvolvimento do sistema paramétrico proposto nesta investigação, esta relação traduz-se na definição de variáveis geométricas, mecânicas e construtivas controladas por parâmetros, permitindo a gerar geometrias adaptadas a dados antropométricos e a requisitos funcionais específicos. Contudo, para que esta tradução entre dados, requisitos e forma não resulte apenas de decisões empíricas ou arbitrárias, torna-se necessário enquadrar a especificação dos requisitos em modelos metodológicos adequados ao desenvolvimento de sistemas protésicos personalizados. Diversos enquadramentos metodológicos sustentam esta especificação em sistemas protésicos paramétricos ou fabricados digitalmente. Para além das abordagens clássicas da engenharia de produto, que estruturam o desenvolvimento através da definição de funções, requisitos técnicos, alternativas de solução e critérios de validação, observa-se uma transição clara para modelos centrados no utilizador , como o User-Centered Design, o Human-Centered Design e metodologias participativas e de co-criação. Estas abordagens promovem ciclos iterativos de prototipagem e avaliação com envolvimento ativo de utilizadores, clínicos e, em alguns casos, familiares, reconhecendo que a definição do problema de design depende tanto da performance mecânica como da experiência concreta de uso (Henao et al., 2025 (#ref-henao-2025); Peerdeman et al., 2011 (#ref-peerdeman-2011); Walker et al., 2019 (#ref-walker-2019)). No domínio digital, a integração de modelação paramétrica, digitalização 3D e simulação, nomeadamente análise por elementos finitos e modelação cinemática, estrutura um fluxo de desenvolvimento em que os requisitos podem ser incorporados diretamente em modelos computacionais ajustáveis e verificados antes da produção física.

A formalização de constrangimentos nas fases iniciais do processo de design desempenha um papel estruturante, permitindo delimitar o espaço de solução antes da geração e avaliação de alternativas. Neste trabalho, estes constrangimentos são organizados em quatro categorias principais: materiais, mecânicos, anatómicos e produtivos. Esta organização permite distinguir os limites relacionados com as propriedades dos materiais, o comportamento estrutural e funcional do dispositivo, a adequação ao corpo do utilizador e as condições de fabrico.

Os constrangimentos materiais são definidos em termos de resistência, rigidez, durabilidade e compatibilidade biológica. Os constrangimentos mecânicos incluem limites de binário, deformação admissível, integridade estrutural sob carga e capacidades cinemáticas mínimas para a realização de tarefas quotidianas. Os constrangimentos anatómicos são integrados com base em dados antropométricos e, quando possível, na digitalização do membro residual, condicionando as geometrias, as zonas de contacto e os volumes internos. Por fim, os constrangimentos produtivos relacionam-se com as capacidades e limitações do fabrico aditivo, incluindo tolerâncias, orientação de impressão, tempo de fabrico, custo e escalonamento.

A explicitação destes limites desde as fases conceptuais permite enquadrar o processo como um exercício de otimização sujeito a múltiplas restrições, estruturando as decisões projetuais de forma clara, verificável e passível de análise crítica (Brack & Amalu, 2021 (#ref-brack-2021); Herneth et al., 2024 (#ref-herneth-2024); Jones et al., 2023 (#ref-jones-2023)).

### 4.2 Parâmetros antropométricos e estrutura do modelo

No desenvolvimento de sistemas protésicos personalizados, as medições corporais funcionam como elemento de ligação entre o corpo do utilizador e a configuração geométrica e funcional do modelo paramétrico. No contexto das próteses de membro superior, estas medições não devem ser tratadas como valores isolados, mas como parte de um sistema estruturado de variáveis capaz de descrever a morfologia da mão, dos dedos, do punho e, quando aplicável, do antebraço ou do membro residual. A literatura recente converge em dois pontos: a personalização eficaz depende de medidas anatomicamente relevantes, e não de escalonamentos genéricos; e essas medidas devem ser organizadas de modo a alimentar diretamente a lógica do modelo digital (Chatzioglou et al., 2024 (#ref-chatzioglou-2024); Moreo, 2016 (#ref-moreo-2016); Rodríguez-Vega & Rodríguez-Vega, 2024 (#ref-rodriguez-vega-2024)).

Esta exigência de organizar as medições em parâmetros operáveis é particularmente evidente nos modelos digitais do dedo e da mão. A Figura 4.1 mostra um exemplo de decomposição paramétrica em comprimentos, larguras e secções articulares, o que clarifica o tipo de estrutura dimensional que sustenta a transição da antropometria para a geometria configurável.

![](projecto-completo_media/image12.png)

Figura 4.1 — Parâmetros antropométricos utilizados na modelação paramétrica de dedos protésicos.

Fonte original: Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. [https://doi.org/10.1109/BioRob60516.2024.10719909](https://doi.org/10.1109/BioRob60516.2024.10719909)

Os parâmetros antropométricos mais relevantes concentram-se, em primeiro lugar, na definição da estrutura dimensional base da mão. Medidas como o comprimento da mão, a largura da mão e o comprimento da palma constituem descritores dimensionais primários, permitindo estabelecer a escala do modelo e definir a sua organização geral. Para além destas, incluem-se parâmetros relativos aos dedos, como comprimentos segmentares e proporções entre falanges, bem como as dimensões do polegar e do punho, essenciais para a funcionalidade e a integraçãoe a integração da mão protésica no uso quotidiano (Chatzioglou et al., 2024 (#ref-chatzioglou-2024); Nag et al., 2003 (#ref-nag-2003)).

Tabela 4.1 — Principais parâmetros antropométricos da mão e do membro superior relevantes para modelação paramétrica

| Mão | Comprimento da mão | Distância do punho à ponta do dedo médio | Escala global do modelo |

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

O conjunto mínimo de parâmetros antropométricos varia em função do nível de amputação, dado que diferentes configurações protésicas exigem níveis distintos de detalhe dimensional. A redução das medições necessárias contribui para processos de personalização mais escaláveis e acessíveis, particularmente quando a recolha de dados é realizada fora de contextos clínicos especializados. (Moreo, 2016 (#ref-moreo-2016); Romero et al., 2025 (#ref-da-silveira-romero-2025)).

Tabela 4.2 — Conjuntos mínimos de parâmetros por nível de amputação

| Transradial (abaixo do cotovelo) | Comprimento do membro residual, circunferência do antebraço, largura do punho |

| --- | --- |

| Desarticulação do punho | Largura e profundidade do punho, comprimento da mão |

| Parcial da mão | Comprimento da palma, dimensões dos dedos remanescentes |

| Dedos (parcial) | Comprimento e largura do dedo, proporções falângicas |

| Mão completa (cosmética/funcional) | Comprimento da mão, largura da palma, comprimento dos dedos |

Esta lógica permite estruturar o sistema paramétrico a partir de entradas essenciais, controlando a complexidade inicial do processo sem inviabilizar a geração de uma solução funcional. Importa, contudo, distinguir entre parâmetros mínimos de configuração e parâmetros de refinamento: os primeiros permitem gerar uma instância funcional do modelo; os segundos aumentam o grau de especificidade da configuração, permitindo afinar a coerência proporcional, a adequação geométrica ou o desempenho cinemático quando existem dados adicionais disponíveis.

### Limitações do redimensionamento proporcional

Uma limitação recorrente em abordagens simplificadas de modelação é o uso de redimensionamento proporcional (uniform scaling), no qual um modelo base é dimensionado proporcionalmente em todas as direções. Esta abordagem revela-se inadequada no contexto antropométrico, uma vez que as dimensões da mão apresentam correlações imperfeitas entre si e variam de forma desigual entre populações, sexos e grupos etários. Em consequência, indivíduos com largura de mão semelhante podem apresentar comprimentos digitais, proporções falângicas ou dimensões do polegar significativamente diferentes. A modelação paramétrica exige, por isso, a definição de parametros independentes que permitem derivar proporções locais sem pressupor uma homotetia global do modelo, isto é, sem assumir que a prótese deve ser redimensionada de forma proporcional como um todo, mantendo invariáveis todas as relações geométricas entre as suas partes. (Lim et al., 2018 (#ref-lim-2018); Nag et al., 2003 (#ref-nag-2003); Rodríguez-Vega & Rodríguez-Vega, 2024 (#ref-rodriguez-vega-2024)).

Esta limitação torna-se visualmente evidente na Figura 4.2, que compara um modelo uniformemente escalado com outro parametrizado a partir de variáveis independentes. A diferença é relevante porque mostra que a personalização não depende apenas de “aumentar ou reduzir” um modelo-base, mas também de reorganizar as relações geométricas internas.

![](projecto-completo_media/image13.png)

Figura 4.2 — Comparação entre o escalonamento uniforme e a modelação paramétrica de dedo protésico.

Adaptado de fonte original: Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. [https://doi.org/10.1115/DETC2018-85645](https://doi.org/10.1115/DETC2018-85645)

### Métodos de recolha de dados antropométricos

A recolha de dados pode ser realizada por diferentes métodos, com implicações diretas na precisão das medições e na sua tradução para parâmetros de projeto. A escolha do método depende do objetivo da medição: parametrização dimensional básica, reconstrução geométrica fina, desenho do encaixe ou obtenção de relações internas entre superfícies e estruturas ósseas. Em termos práticos, a literatura mostra que não há um método universalmente superior; há, sim, uma adequação diferencial entre método, custo, acessibilidade e o tipo de dados necessários (Çıklaçandır et al., 2022 (#ref-cklacandr-2022); Herbst et al., 2021 (#ref-herbst-2021)).

Tabela 4.3 — Métodos de recolha de dados antropométricos e suas características

| Medição manual | Dimensões lineares | Simplicidade, baixo custo | Representação geométrica limitada | Parametrização básica |

| --- | --- | --- | --- | --- |

| Digitalização 3D | Geometria superficial | Elevada precisão, rapidez | Equipamento e processamento necessários | Encaixe e forma |

| Imagiologia médica | Estrutura interna e externa | Dados anatómicos detalhados | Alto custo e menor acessibilidade | Modelação biomecânica |

| Fotogrametria | Geometria aproximada | Acessível, potencial remoto | Precisão variável | Aquisição preliminar |

### Bases de dados antropométricas, extração e normalização

A definição de parâmetros pode apoiar-se em bases de dados antropométricas de referência e em normas de medição corporal, que ajudam a estabilizar a nomenclatura, os pontos anatómicos e os intervalos esperados de variação. No presente projeto, esse apoio foi operacionalizado através da consolidação local de dados provenientes de estudos populacionais e de bases de referência. O conjunto reunido contém 1.790 registos em formato longo, cobre nove países — China, Estados Unidos da América, Índia, Jordânia, México, Nigéria, Países Baixos, Portugal e Turquia — e combina dados de estudos publicados, relatórios técnicos e sub-bases DINED disponibilizadas pela TU Delft.

O objetivo desta consolidação não foi criar uma nova norma antropométrica, nem substituir a medição individual do utilizador. O objetivo foi construir uma infraestrutura intermédia, verificável e comparável, capaz de apoiar três decisões de projeto: definir intervalos plausíveis para os parâmetros expostos no modelo; identificar quais dimensões são suficientemente recorrentes na literatura para servirem como entradas mínimas; e testar a coerência geométrica de configurações geradas a partir de diferentes perfis populacionais. Esta distinção é importante porque os dados populacionais descrevem tendências e dispersões, enquanto uma prótese personalizada continua a exigir medições diretas ou digitalização específica quando o ajuste final ao corpo está em causa.

A seleção das fontes seguiu critérios explícitos. Foram incluídas fontes que apresentavam dados primários ou bases de dados reconhecidas, pelo menos uma dimensão relevante para a mão, dedos, palma, punho ou antebraço, identificação da população ou subgrupo e estatística descritiva claramente reportada, como médias, desvios-padrão, percentis ou intervalos de variação.. Foram excluídos estudos que apenas reutilizavam dados secundários sem acesso claro à fonte original, artigos de engenharia que mencionavam dimensões de forma incidental, exemplos baseados num único sujeito e fontes sem informação suficiente sobre população, método ou unidade. Esta decisão explica, por exemplo, a exclusão dos valores percentílicos reproduzidos por Moreo (2016) a partir da base DINED: apesar de o trabalho ser relevante para a lógica de parametrização, a tabela não constitui recolha primária autónoma e seria metodologicamente redundante quando a fonte DINED podia ser tratada diretamente (Moreo, 2016 (#ref-moreo-2016)).

Tabela 4.4 — Fontes integradas na base local de dados antropométricos

| Fonte | População e cobertura | Dados extraídos | Registos |

| --- | --- | --- | --- |

| DINED kima1993, TU Delft | Crianças neerlandesas, 2–12 anos | Médias e desvios-padrão de medições da mão por idade e sexo | 528 |

| DINED geron1998, TU Delft | Idosos neerlandeses, 50–80+ anos | Médias e desvios-padrão de medições da mão por grupos etários | 210 |

| DINED dined2004, TU Delft | Adultos neerlandeses, 20–60+ anos | Médias e desvios-padrão de medições da mão por sexo e idade | 114 |

| Rodríguez-Vega e Rodríguez-Vega (2024) | População mexicana, 15–59 anos | Comprimento da mão, comprimento da palma, largura da mão e diâmetro de preensão, com valores gerais e por grupos etários | 360 |

| Nag et al. (2003) | Mulheres indianas trabalhadoras | 51 dimensões da mão, incluindo comprimentos, larguras, circunferências, profundidades e aberturas | 255 |

| Gordon et al. (2015) | Militares norte-americanos do ANSUR II | Medições da mão, punho e antebraço extraídas das estatísticas públicas do inquérito | 154 |

| Chatzioglou et al. (2024) | Jovens adultos da Turquia | Comprimentos dos cinco dedos da mão direita, por sexo e combinado | 56 |

| Hu et al. (2007) | Idosos chineses da área de Pequim | Larguras, comprimento da mão, comprimento do dedo e comprimento antebraço-ponta dos dedos | 50 |

| Ibiwari et al. (2025) | Atletas universitários da Nigéria | Comprimento da mão, largura da mão, comprimento palmar e 3.º dedo, por modalidade e sexo | 32 |

| Anacleto Filho et al. (2023) | Trabalhadores industriais portugueses | Comprimento e largura da mão, por sexo | 20 |

| Mistarihi (2020) | Trabalhadores com deficiência física na Jordânia | Comprimento da mão, largura da mão e comprimento cotovelo-ponta dos dedos | 9 |

| Lim et al. (2018) | Adultos jovens nos EUA | Comprimento e largura do dedo indicador para customização de dedo protésico | 2 |

A extração foi realizada a partir das tabelas dos artigos e, quando aplicável, da interface estruturada das bases de dados. Nos artigos científicos, a leitura concentrou-se em duas zonas: a metodologia, para identificar instrumento, postura, mão medida e pontos anatómicos; e os resultados, para localizar as tabelas com médias, desvios-padrão, percentis, mínimos e máximos. Cada valor foi transcrito para uma estrutura comum que preserva a fonte documental, a página, a citação, o nome da medida, a região corporal, o protocolo de medição, a população, o país, o sexo, o grupo etário, a dimensão amostral, o tipo de estatística, as unidades convertidas e uma nota de qualidade quando necessário. A decisão de preservar simultaneamente a fonte, a página, a população e a nota metodológica torna cada valor auditável e permite regressar ao documento original sempre que uma medida pareça incoerente.

A opção pelo formato longo resultou de uma decisão metodológica orientada para a flexibilidade da estrutura de dados. Em vez de criar uma linha por dimensão com colunas fixas para média, desvio-padrão e percentis, cada estatística foi registada como uma linha própria. Assim, uma mesma dimensão pode originar várias linhas relativas à média, ao desvio-padrão, ao P5, P50, P95, mínimo ou máximo.

Este formato facilita a integração de fontes incompletas, porque nem todos os estudos reportam o mesmo conjunto de estatísticas.

Na base atual, existem 612 médias, 609 desvios-padrão, 513 percentis, 28 mínimos e 28 máximos. Esta assimetria é metodologicamente relevante: os conjuntos de dados (Datasets) ANSUR e algumas fontes DINED permitem uma leitura estatística mais ampla, enquanto estudos como Mistarihi (2020) ou Lim et al. (2018) só oferecem valores parciais, úteis como referência contextual mas insuficientes para inferência populacional robusta (Gordon et al., 2015 (#ref-gordon-2015); Lim et al., 2018 (#ref-lim-2018); Mistarihi, 2020 (#ref-mistarihi-2020)).

As principais dificuldades encontradas dizem respeito à heterogeneidade dos protocolos. A expressão “comprimento da mão”, por exemplo, nem sempre corresponde ao mesmo trajeto anatómico: alguns estudos tomam como referência a linha de flexão do punho, outros o processo estilóide, enquanto outros definem o comprimento a partir de marcos funcionais da palma.

Do mesmo modo, verifica-se heterogeneidade no critério de seleção da mão analisada, com estudos que consideram a mão direita, a mão dominante ou, no caso do estudo português, a mão esquerda, em função das condições específicas de recolha de dados. (Anacleto Filho et al., 2023 (#ref-anacleto-filho-2023)). Estas diferenças impedem que todos os dados sejam tratados como diretamente equivalentes e justificam o registo explícito dos respetivos protocolos de medição. A base de dados não elimina a heterogeneidade das fontes; pelo contrário, torna-a visível, permitindo que o modelo paramétrico utilize os valores antropométricos de forma contextualizada e metodologicamente informada.
Foram igualmente identificadas dificuldades relacionadas com a granularidade e a representatividade dos dados. Algumas fontes apresentam amostras robustas, mas oferecem informação limitada sobre dimensões específicas da mão; outras disponibilizam medições detalhadas, mas circunscritas a populações muito particulares. Nag et al. (2003), por exemplo, fornece uma cobertura dimensional extensa, embora limitada a mulheres indianas trabalhadoras. Rodríguez-Vega (2024) apresentam uma amostra mexicana numerosa e grupos etários úteis para comparação, mas concentram-se em quatro dimensões principais. Ibiwari et al. (2025) acrescenta dados relativos a uma população africana, embora a amostra seja composta por atletas universitários, e não por população geral. Mistarihi (2020) é relevante por incluir trabalhadores com deficiência física, mas apresenta um número reduzido de registos e insuficiente desagregação por sexo. Estes casos foram mantidos por ampliarem a diversidade das referências antropométricas, sendo as suas limitações registadas nos metadados relativos à população, à dimensão amostral e à qualidade dos dados.
Em sentido inverso, algumas fontes facilitaram a extração. As tabelas com percentis claros, unidades explícitas e separação por sexo ou idade permitiram uma codificação direta e maior confiança na transcrição dos valores. No caso da DINED, a estrutura HTML da interface facilitou a identificação e extração repetível das médias e dos desvios-padrão, permitindo registar, para cada medida antropométrica, tanto o valor médio observado no grupo como a respetiva variabilidade interna. Esta informação foi recolhida mantendo a separação entre sub-bases, sexo e grupos etários, embora os percentis não estivessem disponíveis na mesma interface.

O ANSUR II também foi particularmente útil por disponibilizar estatísticas amplas e uma grande amostra militar, permitindo trabalhar com medições da mão, punho e antebraço em escala populacional (Gordon et al., 2015 (#ref-gordon-2015); Molenbroek, 1998 (#ref-molenbroek-1998); Molenbroek et al., 2003 (#ref-molenbroek-2003); Steenbekkers & van Beijsterveldt, 1998 (#ref-steenbekkers-1998)). Ainda assim, estas fontes não resolvem o problema da personalização clínica, uma vez que amostras compostas por militares, crianças neerlandesas ou idosos chineses não podem ser diretamente extrapoladas para utilizadores com amputação de membro superior.

As decisões de normalização dos dados seguiram quatro princípios metodológicos. Em primeiro lugar, todas as medidas antropométricas foram convertidas para milímetros, centímetros e polegadas, mantendo-se também a unidade originalmente utilizada em cada fonte. Esta decisão permite comparar valores entre estudos sem perder a referência ao formato de publicação original e reduz o risco de conversões ambíguas no momento de utilização dos dados. Em segundo lugar, valores provenientes de subgrupos com dimensão amostral reduzida, dados extraídos de figuras em vez de tabelas, desvios-padrão discrepantes ou definições anatómicas pouco explícitas foram mantidos na base, mas assinalados através de notas de qualidade. Deste modo, a incerteza associada a cada registo permanece documentada, em vez de ser eliminada sem justificação metodológica. Em terceiro lugar, as medidas foram agrupadas por região corporal, distinguindo dimensões da mão, dedos e palma, diretamente relevantes para a geração da geometria principal, de dimensões do punho e antebraço, mais associadas à interface, à fixação ou à adaptação ao membro residual. Por fim, os valores recolhidos foram tratados como referências paramétricas, e não como prescrições dimensionais finais. A base antropométrica construída responde, assim, a uma necessidade específica do modelo desenvolvido: traduzir o enquadramento antropométrico da personalização protésica em intervalos, relações proporcionais e restrições utilizáveis no processo de modelação. Deste modo, os dados não definem automaticamente a forma da prótese, mas delimitam o espaço de variação dentro do qual o modelo pode operar com maior coerência geométrica e metodológica. Para tal, o sistema necessita de identificar quais as medidas recorrentes na literatura, que variações podem ser consideradas plausíveis entre populações, que dimensões podem funcionar como entradas mínimas de configuração e em que situações o redimensionamento uniforme se torna metodologicamente arriscado.

A base de dados construída permite comparar valores relativos ao comprimento da mão, à largura da palma, aos comprimentos digitais, às dimensões do punho e às relações com o antebraço, mantendo a referência à fonte, à população e ao contexto metodológico de cada registo.

Deste modo, a base de dados sustenta a passagem entre o enquadramento antropométrico e a modelação paramétrica tridimensional, usando OpenSCAD: os dados não geram automaticamente a prótese, mas delimitam o espaço de variação dentro do qual o modelo pode operar com maior coerência geométrica e metodológica.

Permanece, contudo, uma limitação central. A maior parte dos dados disponíveis provém de populações sem amputação e não descreve a morfologia do membro residual, nem a interação dinâmica entre tecido, carga e encaixe. Para uma prótese definitiva, a referência mais adequada seria a medição direta do utilizador, idealmente complementada por digitalização tridimensional e validação de interface. Nesta investigação, os dados antropométricos públicos são usados para estruturar o sistema, testar coerência dimensional e fundamentar decisões de parametrização; não são apresentados como substituto de avaliação clínica, prova de conforto ou validação individual.

### Estrutura paramétrica e mapeamento de parâmetros

A estrutura do modelo paramétrico organiza os parâmetros segundo uma lógica hierárquica e relacional, distinguindo entre parâmetros primários, derivados, funcionais e construtivos. Esta distinção é metodologicamente importante porque impede que o modelo seja tratado como um conjunto plano de medidas independentes. Em vez disso, estabelece-se uma cadeia de transformação em que algumas variáveis funcionam como entradas principais do utilizador e outras como consequências geométricas, cinemáticas ou produtivas dessas entradas (Moreo, 2016 (#ref-moreo-2016); Romero et al., 2025 (#ref-da-silveira-romero-2025)).

Tabela 4.5 — Estrutura hierárquica dos parâmetros no modelo paramétrico

| Primários | Comprimento da mão, largura da palma | Input direto | Independentes |

| --- | --- | --- | --- |

| Derivados | Proporções das falanges | Construção geométrica | Dependentes |

| Funcionais | Amplitude de movimento, posição articular | Desempenho | Ligação cinemática |

| Construtivos | Espessuras, folgas, tolerâncias | Fabrico | Ajuste técnico |

A tradução destes parâmetros em geometria é realizada por meio de relações explícitas entre medições e componentes do modelo.

### OpenSCAD: enquadramento e justificação da escolha

Antes de avançar para a formalização do modelo, importa clarificar o que é o OpenSCAD e por que motivo foi escolhido como ambiente de modelação paramétrica neste projeto. O OpenSCAD é um ambiente livre e open source de CAD tridimensional baseado em ficheiros de script, orientado para a criação de geometria sólida e não para a modelação artística de superfícies. O modelo é descrito num ficheiro .scad, escrito numa linguagem própria, e esse ficheiro é interpretado pelo programa para gerar o sólido correspondente. Do ponto de vista geométrico, o OpenSCAD assenta numa lógica de Constructive Solid Geometry (CSG), na qual primitivas como cubos, cilindros, esferas e extrusões são combinadas por operações booleanas, transformações e relações hierárquicas entre módulos (OpenSCAD Project, n.d.-a (#ref-openscad-project-nd-a); OpenSCAD Project, n.d.-b (#ref-openscad-project-nd-b); Ghali, 2008 (#ref-ghali-2008)).

Esta natureza programável distingue o OpenSCAD dos ambientes CAD convencionais baseados sobretudo em manipulação gráfica direta. Em muitos sistemas CAD, o utilizador constrói uma sequência de operações num histórico visual e parametriza algumas características desse histórico; no OpenSCAD, pelo contrário, a própria descrição textual é o modelo paramétrico. As variáveis, funções e módulos não são uma camada posterior aplicada à geometria, mas a estrutura que a gera. Esta diferença é relevante para a investigação, porque torna as relações entre parâmetros, componentes e restrições mais explícitas, reexecutáveis e documentáveis, embora implique uma curva de aprendizagem maior e dificuldades conhecidas em tarefas de navegação código-vista, validação e criação de formas orgânicas complexas (Trautmann, 2021 (#ref-trautmann-2021); Gonzalez Avila et al., 2024 (#ref-gonzalez-avila-2024)).

A escolha do OpenSCAD resulta, em primeiro lugar, da sua adequação a processos reprodutíveis de design paramétrico. Por ser texto simples, o ficheiro-fonte pode ser versionado, comparado, revisto e reutilizado, o que favorece a rastreabilidade das decisões de modelação e a replicação das variantes geradas. Esta característica é particularmente valorizada em hardware científico e open source, precisamente porque a documentação do processo é tão importante como o ficheiro final exportado. Além disso, o OpenSCAD pode ser executado por linha de comando, receber valores por parâmetros e exportar automaticamente geometrias para formatos de fabrico digital, como STL ou 3MF, tornando-o compatível com fluxos de geração em lote e com configuradores digitais (Machado et al., 2019 (#ref-machado-2019); OpenSCAD Community, n.d. (#ref-openscad-community-nd)).

Em segundo lugar, o OpenSCAD adapta-se bem à arquitetura web proposta nesta dissertação. A separação entre definição geométrica e interface permite que o ficheiro .scad permaneça como núcleo técnico do modelo, enquanto a plataforma apresenta ao utilizador apenas os parâmetros relevantes. Esta lógica já foi explorada em configuradores web baseados em OpenSCAD, nos quais utilizadores sem domínio da linguagem podem gerar variantes imprimíveis a partir de modelos parametrizados por designers. A existência de implementações em WebAssembly, como o OpenSCAD Web, reforça esta escolha, porque demonstra que o motor de geração pode ser executado no navegador, associado a editores, visualizadores 3D e interfaces de customização sem exigir a instalação local de software CAD completo (Nilsiam & Pearce, 2017 (#ref-nilsiam-2017); Brooks, 2026 (#ref-brooks-2026)).

Em terceiro lugar, o OpenSCAD é particularmente compatível com um fluxo de design assistido por inteligência artificial. Como a geometria é expressa em código curto, estruturado e relativamente legível, uma IA pode sugerir valores, explicar relações entre variáveis ou propor alterações ao script sem substituir a lógica paramétrica por uma geometria opaca. Trabalhos recentes sobre geração de modelos 3D a partir de linguagem natural e automação de desenho paramétrico mostram que modelos de linguagem podem atuar sobre scripts CAD, embora continuem a exigir revisão humana, verificação dimensional e validação técnica antes de qualquer aplicação produtiva ou clínica (ELhadad et al., 2026 (#ref-elhadad-2026); Schöfer & Seibel, 2025 (#ref-schofer-seibel-2025); Gonzalez Avila et al., 2024 (#ref-gonzalez-avila-2024)).

No contexto específico das próteses e das tecnologias de apoio, esta escolha é ainda reforçada por estudos que usam modelação paramétrica para adaptar dedos protésicos, mãos mecânicas acionadas pelo corpo e outros dispositivos de apoio às medidas ou necessidades do utilizador.
Estes trabalhos não eliminam a necessidade de ensaios funcionais, avaliação ergonómica ou validação clínica, mas demonstram que a personalização geométrica pode ser estruturada por parâmetros explícitos e por modelos reexecutáveis. Para este projeto, o OpenSCAD é, portanto, adequado não porque resolva sozinho o problema da prótese personalizada, mas porque oferece uma base transparente para ligar medidas antropométricas, regras de modelação, interface web, sugestões de IA, exportação para fabrico aditivo e revisão humana (Lim et al., 2018 (#ref-lim-2018); Bustamante et al., 2018 (#ref-bustamante-2018); Romani & Levi, 2020 (#ref-romani-levi-2020)).

Tabela 4.6 — Mapeamento entre parâmetros antropométricos e elementos do modelo

| Comprimento da mão | Escala geral e comprimento dos dedos |

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

A modelação paramétrica em OpenSCAD corresponde, nesta investigação, ao momento em que a estrutura definida na secção anterior deixa de ser apenas um quadro conceptual e passa a constituir um modelo operacional, capaz de traduzir parâmetros, relações e restrições em geometrias configuráveis. Os parâmetros antropométricos selecionados, as relações hierárquicas entre variáveis e os limites de configuração deixam de funcionar apenas como critérios de organização e passam a ser inscritos em código, de modo a gerar geometria de forma consistente e repetível. Assim, a transição para OpenSCAD não representa uma mudança de tema, mas a continuação lógica do mesmo problema: como transformar dados corporais e regras de projeto num modelo configurável que preserve coerência formal, funcional e produtiva.

A modelação paramétrica em OpenSCAD é, por isso, aqui entendida como uma abordagem em que a geometria resulta de regras explícitas, parâmetros definidos em código e relações de dependência entre componentes, em vez de edição manual isolada de formas. No desenvolvimento de próteses personalizadas de membro superior, esta lógica é particularmente relevante, pois permite compreender a prótese não como um objeto único e fixo, mas como um conjunto configurável de variantes, passível de ser regenerado a partir de novos dados antropométricos, requisitos funcionais e limites associados ao fabrico. Os estudos revistos sobre modelação paramétrica aplicada a próteses e sobre modelação CAD programável reforçam esta perspetiva, ao associarem estas abordagens a maior rastreabilidade das decisões, consistência entre variantes e capacidade de automatização em fluxos de personalização digital. (Machado et al., 2019 (#ref-machado-2019); Moreo, 2016 (#ref-moreo-2016); Romero et al., 2025 (#ref-da-silveira-romero-2025)).

Ao contrário de ambientes centrados na manipulação gráfica direta, o OpenSCAD opera como uma especificação computacional do objeto. Esta característica é metodologicamente relevante para a presente investigação, porque permite compreender o modelo não apenas como um resultado geométrico, mas também como uma estrutura explícita de projeto, na qual ficam registadas as relações entre entradas antropométricas, módulos geométricos, restrições construtivas e decisões formais. Neste sentido, a modelação baseada em código articula-se com uma perspetiva de Research Through Design, na medida em que o próprio modelo pode ser lido, revisto, testado e documentado como uma estrutura de conhecimento técnico-projetual.

A Figura 4.3 reforça esta passagem entre definição paramétrica, modelo virtual e protótipo físico. O seu valor para esta investigação não reside em replicar a solução apresentada, mas em tornar visível a cadeia que liga a decomposição dimensional do dedo, a modelação computacional e a verificação material, isto é, o mesmo tipo de continuidade que o modelo em OpenSCAD procura preservar (Nini et al., 2024 (#ref-nini-2024)).

![](projecto-completo_media/image14.png)

Figura 4.3 — Relação entre modelo paramétrico digital, prototipagem e verificação de um dedo protésico.

Fonte original: Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. [https://doi.org/10.1109/BioRob60516.2024.10719909](https://doi.org/10.1109/BioRob60516.2024.10719909)

### 4.3.1 Estrutura técnica, parâmetros e restrições

Num modelo paramétrico baseado em OpenSCAD, a organização interna pode ser compreendida como uma arquitetura em camadas.

Numa primeira camada situam-se os dados de entrada, provenientes de medições lineares, de dados consolidados de referência ou de digitalização tridimensional. Numa segunda camada, esses dados são transformados em parâmetros geométricos derivados, responsáveis por estabelecer proporções, espessuras, posições articulares e relações entre subcomponentes. Segue-se uma camada funcional, na qual se definem exigências de mobilidade, montagem ou integração mecânica, e uma camada de restrições produtivas, na qual se enquadram espessuras mínimas, folgas, tolerâncias e limites de fabricação. Esta organização permite controlar a personalização sem comprometer a coerência interna do sistema (Moreo, 2016 (#ref-moreo-2016); Nini et al., 2024 (#ref-nini-2024); Saldarriaga et al., 2024 (#ref-saldarriaga-2024)).

Tabela 4.7 — Estrutura técnica em camadas de um modelo paramétrico em OpenSCAD para próteses personalizadas

| Entrada | Dados antropométricos e/ou dados de digitalização | Individualizar o modelo | Largura da palma, comprimentos digitais, perímetro do membro residual |

| --- | --- | --- | --- |

| Derivação geométrica | Parâmetros calculados a partir das entradas | Traduzir medidas em relações formais | Comprimentos segmentares, espessuras, offsets |

| Comportamento funcional | Parâmetros ligados ao uso e ao mecanismo | Regular movimento, montagem e desempenho | Amplitude articular, espaço para tendões, eixos |

| Restrições produtivas | Limites de fabrico e consistência | Garantir fabricação e robustez | Espessura mínima, folgas, raios mínimos |

Quando transposta para o ambiente de modelação em OpenSCAD, esta arquitetura tende a materializar-se através de módulos relativamente autónomos. Em vez de concentrar toda a definição geométrica num único bloco de código, o modelo pode ser distribuído em módulos correspondentes à palma, aos dedos, às articulações, às interfaces de fixação ou ao encaixe. A modularidade apresenta aqui duas vantagens diretas: reduz a opacidade do sistema e facilita a regeneração controlada de variantes. Num contexto protésico, isto permite que alterações nos parâmetros de entrada não se propaguem de forma arbitrária a todo o modelo, mas segundo relações previamente explicitadas e localizáveis. (Machado et al., 2019 (#ref-machado-2019); Romero et al., 2025 (#ref-da-silveira-romero-2025)).

Outro aspeto central é a integração de restrições diretamente na lógica paramétrica. Em vez de tratar a compatibilidade com o fabrico aditivo como uma etapa exclusivamente posterior, o modelo pode incorporar, desde o início, limites mínimos de espessura, folgas entre elementos móveis, margens de tolerância e verificações condicionais para evitar combinações inválidas.

Este princípio é particularmente relevante em próteses produzidas por fabrico aditivo, nas quais pequenas alterações dimensionais podem comprometer a montagem, a resistência ou a viabilidade de impressão. Estudos sobre modelação paramétrica de dedos protésicos e e encaixes protésicos personalizados mostram, precisamente, que a robustez do sistema depende da articulação entre parâmetros antropométricos e restrições construtivas, e não apenas da liberdade de variação geométrica (Nini et al., 2024 (#ref-nini-2024); Saldarriaga et al., 2024 (#ref-saldarriaga-2024)).

A modelação em OpenSCAD pode ser articulada a fluxos de dados mais complexos, incluindo a digitalização tridimensional e a automatização parcial do desenho. Trabalhos como os de Herbst et al. (2021) (#ref-herbst-2021) e Saldarriaga et al. (2024) (#ref-saldarriaga-2024) mostram que a personalização tende a aproximar a medição, a parametrização e o fabrico, reduzindo o intervalo entre a captura anatómica e a geração de modelos prontos para produção. No caso desta investigação, essa articulação não significa abandonar a lógica explícita do código, mas, antes, usá-la como núcleo organizador sobre o qual dados, restrições e interfaces de configuração podem ser integrados de modo consistente e repetível.

### 4.3.2 Análise crítica da abordagem

A adoção do OpenSCAD neste projecto, apresenta vantagens metodológicas relevantes, sobretudo pela forma como torna explícita a construção do modelo paramétrico. Ao ser definido por código, o modelo permite que as relações entre variáveis, dependências e restrições sejam mais facilmente identificadas do que em muitos fluxos CAD baseados apenas em operações gráficas. Esta condição favorece a transparência do processo, a revisão crítica e a possibilidade de reconstituir as decisões de modelação, qualidades particularmente importantes num trabalho académico em que o modelo paramétrico não constitui apenas um instrumento de produção formal, mas também um objeto de análise (Machado et al., 2019 (#ref-machado-2019)).

Uma segunda vantagem reside na afinidade entre a modelação baseada em código, a automação e a partilha aberta. Os estudos analisados indicam que o OpenSCAD é particularmente adequado a fluxos de personalização digital em que o modelo é configurado através de parâmetros e não através da edição manual da geometria. Esta característica permite associar o ficheiro-fonte a interfaces web, gerar múltiplas variantes de forma controlada e disponibilizar modelos reutilizáveis em comunidades distribuídas. Assim, a possibilidade de ajustar o modelo sem editar diretamente o código em cada iteração reforça a sua pertinência em contextos de personalização acessível e fabrico digital (Nilsiam & Pearce, 2017 (#ref-nilsiam-2017)).Para um projeto que pretende aproximar parametrização, interface e apoio computacional, esta característica é especialmente relevante.

Contudo, esta abordagem apresenta limitações importantes. Uma delas prende-se com a exigência técnica e conceptual associada à programação. Mesmo quando o modelo é modular e bem estruturado, a edição direta em OpenSCAD requer capacidade de interpretar transformações geométricas, dependências paramétricas e operações booleanas. Por essa razão, a utilidade do OpenSCAD aumenta quando o sistema é mediado por camadas intermédias de interface ou por procedimentos que exponham apenas os parâmetros necessários à configuração. A segunda limitação é de natureza geométrica. A modelação por combinação de sólidos, habitualmente designada por Constructive Solid Geometry (CSG), favorece a criação de peças mecânicas, modulares e relativamente discretas, mas tende a ser menos adequada à definição de superfícies orgânicas complexas ou de interfaces anatómicas altamente irregulares, sobretudo quando comparada com ferramentas orientadas para superfícies livres.

Há ainda uma limitação relacionada com a interoperabilidade. Os estudos comparativos sobre OpenSCAD sublinham que este ambiente de modelação está fortemente orientado para formatos baseados em malhas, nos quais a geometria é representada por uma aproximação poligonal da superfície, como acontece nos ficheiros STL. Esta orientação favorece fluxos de fabrico digital e impressão 3D, mas pode dificultar a integração com certos circuitos CAD industriais ou com ambientes que exijam a preservação completa da informação paramétrica em formatos normalizados (Machado et al., 2019 (#ref-machado-2019)). Isto não invalida a adequação do OpenSCAD ao presente projeto, mas significa que a sua adoção deve ser vista como uma escolha situada: muito eficaz para estruturar um núcleo paramétrico explícito, menos adequada quando o objetivo depende de plena continuidade com certos fluxos proprietários de engenharia.

Por fim, importa reconhecer que a robustez da abordagem resulta da articulação entre a geração da geometria e as etapas subsequentes de validação. Mesmo quando a lógica paramétrica é clara e as restrições estão integradas, a confirmação do modelo depende da verificação durante a preparação do modelo para impressão 3D, do controlo dimensional, de eventual simulação estrutural e da observação do comportamento da peça em protótipo.

Em consequência, o valor do OpenSCAD nesta investigação não reside numa promessa de automatização total, mas na capacidade de fornecer uma infraestrutura técnica clara para ligar a personalização antropométrica, a modularidade, as restrições de fabrico e a documentação do processo. É precisamente essa combinação entre explicitação, reexecução e possibilidade de revisão crítica que justifica a sua escolha como base para a modelação paramétrica aqui desenvolvida.

### 4.4 Iterações, refinamento e discussão intermédia

O desenvolvimento do modelo paramétrico não ocorreu, desde o início, como uma sequência linear orientada para uma solução estável e definitiva. Pelo contrário, evoluiu através de ciclos sucessivos de formulação, teste, correção e reconfiguração, em coerência com a perspetiva de Research Through Design, segundo a qual o próprio processo projetual constitui um meio de produção de conhecimento (Zimmerman, Forlizzi, & Evenson, 2007). Neste enquadramento, cada versão do modelo funcionou simultaneamente como protótipo operativo e como dispositivo crítico, permitindo tornar visíveis as limitações, reformular os critérios e aprofundar a compreensão das relações entre dados antropométricos, organização geométrica, requisitos funcionais e constrangimentos de fabrico.

A necessidade de iteração tornou-se particularmente evidente porque a modelação paramétrica, apesar da sua aparência sistemática, depende de um equilíbrio delicado entre abstração e concretização. Numa fase inicial, a estrutura do sistema assentou na definição de um conjunto de parâmetros julgados essenciais e numa primeira hierarquia entre variáveis de entrada, valores derivados e restrições. No entanto, à medida que o modelo foi sendo testado em diferentes cenários, verificou-se que a mera disponibilidade de muitos parâmetros não aumentava, por si só, a capacidade de personalização. Pelo contrário, a exposição excessiva de variáveis tendia a tornar o sistema mais opaco, menos previsível e mais vulnerável a incoerências geométricas, confirmando a importância de limitar e estruturar cuidadosamente o espaço configurável (Ozdemir, Verlinden, & Cascini, 2022; Lei, Yao, Moon, & Bi, 2016).

Uma parte decisiva do refinamento incidiu, por isso, na reorganização da arquitetura paramétrica. O objetivo deixou de ser apenas permitir a variação e passou a consistir em garantir uma variação controlada. Isto implicou reduzir redundâncias, clarificar as dependências internas e distinguir com maior rigor os parâmetros estruturantes dos ajustamentos secundários. Em vez de um sistema monolítico e pouco legível, procurou-se construir uma lógica hierárquica em que as relações críticas permanecessem explícitas e rastreáveis. Esta passagem foi importante não apenas para a manutenção do código, mas também para a robustez do próprio modelo, dado que a literatura sublinha que a qualidade das relações paramétricas é determinante para a viabilidade de famílias de produto adaptáveis e tecnicamente consistentes (Lei et al., 2016 (#ref-lei-2016); Wiberg, Persson, & Ölvander, 2019).

À medida que a estrutura geral se consolidou, o trabalho iterativo deslocou-se para a decomposição do sistema em módulos relativamente autónomos. Esta organização modular permitiu isolar problemas, testar componentes de forma localizada e introduzir alterações sem comprometer integralmente o comportamento global do modelo. No contexto do presente projeto, esta estratégia revelou-se especialmente útil na articulação entre elementos estruturais, zonas de contacto, interfaces mecânicas e componentes de ligação. Para além de organizar o código, a divisão do modelo em módulos contribuiu para clarificar progressivamente a lógica do objeto, aproximando-o de uma estrutura configurável, mais sistemática e compatível com futuros contextos de interface ou de configuração assistida (Nilsiam & Pearce, 2017 (#ref-nilsiam-2017)).

As iterações também mostraram que a robustez de um modelo paramétrico só se torna legível quando confrontado com situações-limite. Um sistema pode parecer estável dentro de uma faixa reduzida de variação e, ainda assim, revelar fragilidades relevantes quando submetido a combinações menos previsíveis de parâmetros. Foi precisamente nesse tipo de ensaio que surgiram problemas como interseções indevidas entre componentes, espessuras insuficientes em zonas críticas, desalinhamentos de interfaces, incompatibilidades entre dimensões derivadas e perdas localizadas de coerência proporcional. O refinamento consistiu, assim, menos na correção pontual de erros isolados e mais na identificação de padrões recorrentes de instabilidade, o que levou à introdução progressiva de verificações condicionais, limites paramétricos e ajustes automáticos.

Outro eixo central do processo prendeu-se à relação entre personalização e fabricação. Nem todas as variações formalmente admissíveis se revelaram compatíveis com as exigências do fabrico. Algumas configurações geravam geometrias excessivamente finas, folgas insuficientes ou desproporcionadas, transições abruptas e zonas potencialmente frágeis no contexto da impressão 3D. Neste sentido, a evolução do modelo confirmou a relevância de integrar critérios de Design for Additive Manufacturing à própria lógica paramétrica, em vez de tratá-los como uma verificação externa e posterior. A literatura sobre DfAM aponta precisamente para a necessidade de incorporar tolerâncias, espessuras mínimas, orientações de fabrico e limites materiais desde a fase de conceção, reduzindo falhas e encurtando os ciclos de reimpressão e de correção (Chtioui, Gaha, & Benamara, 2023; Wiberg et al., 2019 (#ref-wiberg-2019)).

Em sistemas configuráveis para próteses, a coerência geométrica e a compatibilidade com o processo de impressão não são suficientes para assegurar a adequação ao uso. A articulação entre segmentos, o posicionamento relativo dos mecanismos, a distribuição de massa, as zonas sujeitas a esforço e a amplitude de movimento influenciam diretamente o desempenho esperado do objeto. Por essa razão, várias revisões do modelo implicaram reajustes que articularam a correção formal da geometria com a necessidade de manter um equilíbrio plausível entre adaptação dimensional, comportamento funcional e viabilidade material.

O refinamento correspondeu, assim, a uma negociação contínua entre a simplificação paramétrica e as exigências funcionais e materiais do protótipo.

Do ponto de vista metodológico, importa sublinhar que este percurso não deve ser lido como uma simples sucessão de tentativas e erros. Cada iteração reconfigurou a compreensão do problema e tornou mais explícitos aspetos que não eram plenamente antecipáveis na formulação inicial. Entre eles, destacam-se a dificuldade de traduzir certas qualidades anatómicas em relações paramétricas simples, a tendência de modelos demasiado abertos a perderem consistência e a necessidade de explicitar restrições para preservar a coerência perante a variação. Neste sentido, o conhecimento produzido não reside apenas no estado final do modelo, mas também no próprio processo de convergência crítica que permitiu delimitar o que pode e o que não pode ser razoavelmente parametrizado neste contexto (Zimmerman et al., 2007 (#ref-zimmerman-2007)).

A discussão intermédia decorrente destas iterações permite tirar algumas conclusões provisórias. Em primeiro lugar, confirma-se que a modelação paramétrica baseada em código constitui um enquadramento adequado para estruturar sistemas configuráveis, desde que a arquitetura seja disciplinada e os parâmetros expostos sejam criteriosamente selecionados. Em segundo lugar, verifica-se que a robustez do sistema depende menos da quantidade de variáveis disponíveis do que da qualidade das relações estabelecidas entre elas. Em terceiro lugar, torna-se claro que a personalização eficaz exige integração simultânea de critérios antropométricos, funcionais e produtivos, não podendo ser reduzida a mera transformação geométrica. Por fim, a iteração evidencia-se como mecanismo indispensável de convergência: não encerra definitivamente o sistema, mas estabiliza uma versão suficientemente consistente para sustentar as fases seguintes de plataforma, integração digital e exploração assistida.

## Capítulo 5 — Plataforma Web e Integração Digital

### 5.1 Enquadramento conceptual e perfis de utilizador

A plataforma web desenvolvida no âmbito deste projeto constitui a camada de mediação entre o modelo paramétrico, os dados do utilizador e os processos de configuração digital da prótese. O seu enquadramento conceptual assenta na ideia de que a personalização não deve depender da manipulação direta do código nem de competências avançadas de modelação tridimensional, mas de uma interface capaz de traduzir dados antropométricos, decisões de configuração e critérios de fabrico em parâmetros operacionais inteligíveis. Nesta perspetiva, a plataforma não é apenas um visualizador técnico do modelo, mas também um dispositivo de mediação que reorganiza a relação entre o sistema paramétrico, o utilizador, o processo de decisão e a preparação para o fabrico. Esta leitura é coerente com os estudos sobre personalização digital e personalização em massa, que descrevem os configuradores como infraestruturas capazes de expor uma parte controlada do espaço de variação, permitindo adaptar produtos sem comprometer a coerência interna do modelo-base (Ozdemir, Verlinden, & Cascini, 2022; Stralen, 2018 (#ref-stralen-2018)).

Do ponto de vista funcional, a plataforma foi concebida para suportar um processo progressivo de personalização, no qual a definição geométrica da prótese resulta da articulação entre a recolha de dados, a seleção do modelo, o ajustamento de parâmetros, a visualização do resultado e a eventual exportação para prototipagem. Esta organização procura reduzir a distância entre o domínio técnico da modelação paramétrica e o contexto aplicado de utilização clínica, experimental ou de projecto.

Em vez de exigir que cada interveniente compreenda a estrutura interna do ficheiro OpenSCAD, o sistema disponibiliza uma camada de interação mais acessível, baseada em controlos paramétricos, pré-visualização tridimensional e gestão de configurações.

Tal opção aproxima-se de abordagens recentes em plataformas de personalização de próteses, nas quais a interface funciona como meio de tornar observável, configurável e progressivamente verificável um processo que, de outro modo, permaneceria dependente de software especializado ou de mediação exclusivamente técnica (Peixoto et al., 2025 (#ref-peixoto-2025)).

![](projecto-completo_media/image15.png)

Figura 5.1 — Fluxo geral de produção personalizada de próteses a partir de plataforma web – Hand Fab

Produção própria

Neste sentido, a plataforma deve ser entendida como uma infraestrutura de mediação entre componentes técnicos, utilizadores e intervenientes especializados, e não apenas como um artefacto de software. A personalização deixa, assim, de corresponder a um ato individual e isolado, passando a ser enquadrada como um processo distribuído, no qual diferentes intervenientes participam com graus distintos de responsabilidade, conhecimento e controlo.

Num contexto de próteses personalizadas, o resultado final pode depender da articulação entre o utilizador final, o designer, o técnico ou o clínico, bem como de condicionantes produtivas e de critérios de validação. A plataforma procura, assim, oferecer uma infraestrutura digital que acomode essa pluralidade de agentes sem comprometer a consistência técnica da configuração paramétrica nem deslocar indevidamente a responsabilidade para o utilizador menos especializado (Bai, Yuan, Liu, Huang, & Feng, 2024; Quintero et al., 2018 (#ref-quintero-2018)).

A definição dos perfis de utilizador constitui, por isso, uma decisão estruturante no desenho da plataforma, uma vez que determina como se distribuem responsabilidades, permissões e formas de intervenção no processo de personalização. O sistema organiza-se em três perfis principais: administrador, técnico e utilizador.

O perfil de administrador assegura a gestão global da plataforma, incluindo a criação de contas, a definição de permissões e a supervisão do ecossistema de configurações, incluindo da base de dados antropométricos. O perfil técnico, pensado para profissionais intermédios, como técnicos de ortoprotesia, clínicos ou operadores especializados, permite criar, editar e acompanhar configurações próprias e, quando aplicável, aceder às configurações dos utilizadores sob sua responsabilidade. O perfil de utilizador corresponde ao nível mais restrito, centrado na consulta das suas configurações, no acompanhamento do processo e em interações delimitadas pelo sistema.

Esta segmentação traduz uma lógica de controlo de acesso baseada em papéis, procurando equilibrar autonomia, segurança e responsabilidade distribuída, ao tornar claros os limites de intervenção de cada perfil. Importa sublinhar que esta diferenciação não se limita a uma decisão administrativa, participando diretamente na forma como a plataforma enquadra a personalização.

Ao reservar certos parâmetros, decisões ou operações a perfis técnicos, o sistema reconhece que nem todos os aspetos da configuração devem ser apresentados ao utilizador final como escolhas livres. Em domínios sensíveis, como o das próteses, a experiência de uso beneficia quando a interface torna visível o processo, mas também quando delimita o campo de ação de forma coerente com critérios de supervisão, segurança e adequação funcional. A literatura sobre interfaces clínicas e interação em próteses inteligentes aponta precisamente para a necessidade de distinguir entre participação informada do utilizador e controlo técnico supervisionado, evitando tanto a opacidade excessiva como a transferência imprudente de responsabilidade para agentes não especializados (Bai et al., 2024 (#ref-bai-2024); Quintero et al., 2018 (#ref-quintero-2018)).

Deste modo, o enquadramento conceptual da plataforma articula três objetivos complementares: tornar a lógica paramétrica operável em ambiente web, estruturar a personalização como um processo progressivo e inteligível e distribuir o acesso às operações de acordo com papéis diferenciados. O valor da plataforma, nesta fase, não reside apenas em permitir editar parâmetros à distância, mas também em reconfigurar o próprio processo de personalização como uma sequência assistida, documentável e passível de revisão crítica. É nessa articulação entre capacidade de configuração, mediação pela interface e organização por perfis que a secção seguinte, dedicada à arquitetura geral do sistema, encontra a sua base conceptual.

### 5.2 Arquitetura geral do sistema

O sistema organiza-se numa estrutura em camadas, concebida para distinguir a interface de utilização, a lógica de configuração, a persistência de dados e os serviços complementares de apoio ao processo de personalização. Esta opção procura responder a um problema central do projeto: tornar operável um modelo paramétrico tecnicamente exigente num ambiente web sem concentrar, no mesmo ponto, responsabilidades de interação, cálculo geométrico, armazenamento e controlo de acesso. Em termos conceptuais, esta separação prolonga a lógica já discutida nas secções anteriores: a personalização digital exige sistemas suficientemente configuráveis para acomodar a variação, mas também suficientemente disciplinados para preservar a coerência, a rastreabilidade e a capacidade de manutenção (Ozdemir et al., 2022 (#ref-ozdemir-2022); Lei et al., 2016 (#ref-lei-2016)).

A Figura 5.2 apresenta um precedente de arquitetura de produção personalizada em que a digitalização, o processamento de dados, a adaptação CAD e o fabrico aditivo são articulados num fluxo de ponta a ponta. A comparação é útil porque mostra que a personalização digital depende da continuidade entre captura, parametrização e produção, ainda que, no presente projeto, essa continuidade seja deslocada para uma plataforma web e para modelos OpenSCAD executados localmente (Górski et al., 2022 (#ref-gorski-2022)).

![](projecto-completo_media/image16.png)

Figura 5.2 — Fluxo geral de produção personalizada de próteses a partir de digitalização, CAD adaptativo e fabrico aditivo.

Fonte original: Górski, F., Zawadzki, P., Wichniarek, R., Kuczko, W., Słupińska, S., & Żukowska, M. (2022). Automated design and rapid manufacturing of low-cost customized upper limb prostheses. Journal of Physics: Conference Series, 2198, 012040. [https://doi.org/10.1088/1742-6596/2198/1/012040](https://doi.org/10.1088/1742-6596/2198/1/012040)

No navegador do utilizador, a aplicação integra os componentes responsáveis pela interface, pela recolha e edição de parâmetros, pela gestão do estado da sessão e pela visualização local dos modelos. No servidor, um serviço desenvolvido em Node.js, com recurso ao framework Express.js, assegura a disponibilização de ficheiros estáticos, o processamento de pedidos à API, a autenticação de utilizadores, a aplicação de permissões e a comunicação com a camada de persistência. Esta distribuição de responsabilidades evita que a interface dependa de processamento remoto contínuo para todas as operações e, simultaneamente, impede que tarefas sensíveis, como a gestão de utilizadores, o controlo de acessos e a comunicação com serviços externos, fiquem expostas diretamente no cliente. A arquitetura não corresponde, portanto, a uma simples divisão técnica entre “frente” (frontend) e “retaguarda” (backend), mas sim a uma estratégia de contenção da complexidade e de delimitação explícita de responsabilidades.

A camada de persistência assenta numa base de dados SQLite, utilizada para armazenar contas de utilizador, configurações guardadas, relações de atribuição técnica e tokens de autenticação. A escolha desta solução responde ao caráter prototípico e funcional do sistema nesta fase da investigação, privilegiando a leveza de implementação, a portabilidade e a facilidade de manutenção. As configurações paramétricas são armazenadas como estruturas JSON associadas a um modelo e a um utilizador, permitindo preservar diferentes instâncias de personalização, recuperá-las em momentos posteriores e compará-las como estados distintos do processo do projeto. Deste modo, a base de dados não funciona apenas como repositório administrativo, mas também como infraestrutura que sustenta a continuidade do processo, a gestão prática de versões e o acompanhamento da evolução das variantes produzidas.

Um dos aspetos mais relevantes da arquitetura é que a renderização geométrica não é executada no servidor. Em vez disso, o cálculo e a geração da geometria tridimensional ocorrem localmente no navegador, através de uma versão do OpenSCAD compilada para WebAssembly, tecnologia que permite executar código de elevado desempenho em ambiente web. Este processo é realizado num Web Worker, isto é, numa tarefa separada da interface principal, evitando que a geração do modelo bloqueie a interação do utilizador com a plataforma. Esta decisão reduz a carga computacional do backend, diminui a dependência de um serviço remoto de renderização e favorece uma interação mais imediata durante a edição paramétrica. Ao mesmo tempo, preserva-se uma fronteira clara: o servidor mantém-se responsável pela autenticação, armazenamento, gestão de configurações e intermediação de chamadas a serviços de inteligência artificial, enquanto o cliente assume a computação geométrica intensiva. A arquitetura resultante é, assim, híbrida: centraliza funções de controlo e persistência, mas distribui localmente a geração formal do modelo.

No plano da segurança e do controlo de acesso, a arquitetura incorpora autenticação baseada em JSON Web Token (JWT), um mecanismo que permite verificar a identidade do utilizador através de credenciais digitais temporárias. A plataforma utiliza ainda tokens de atualização armazenados em cookies HttpOnly, isto é, cookies que não podem ser acedidos diretamente por scripts executados no navegador, reduzindo a exposição a certos tipos de ataque. Estes mecanismos são complementados por validação de dados, limitação de pedidos e bloqueio explícito de ficheiros sensíveis.

Estes mecanismos não devem ser entendidos como adições periféricas, mas como parte integrante do desenho do sistema, sobretudo num contexto em que múltiplos perfis de utilizador operam sobre configurações potencialmente sensíveis e em que a plataforma articula a autonomia de uso com a supervisão técnica. A literatura sobre interfaces de configuração em contexto protésico sublinha, precisamente, a importância de equilibrar a participação, a diferenciação de permissões e o enquadramento seguro das operações críticas (Quintero et al., 2018 (#ref-quintero-2018); Bai et al., 2024 (#ref-bai-2024)). Neste sentido, a arquitetura traduz uma opção por robustez e extensibilidade controlada: não procura apenas “ligar” componentes, mas estruturar um ecossistema técnico coerente com os requisitos de personalização assistida, gestão multiutilizador e futura evolução da plataforma.

### 5.3 Integração OpenSCAD via WebAssembly (WASM)

A integração do OpenSCAD por meio de WebAssembly, como referido anteriormente, constitui um dos elementos técnicos mais relevantes da plataforma, pois permite executar localmente, no navegador, um modelo paramétrico baseado em código, sem depender de um serviço externo de renderização contínua. O OpenSCAD funciona como linguagem e ambiente de modelação em que a geometria é definida por instruções escritas, parâmetros numéricos e relações explícitas entre componentes, em vez de resultar exclusivamente de manipulação gráfica direta. O WebAssembly (WASM), por sua vez, possibilita a execução de aplicações compiladas com desempenho próximo ao nativo no contexto da web. A articulação entre ambos torna viável um cenário particularmente pertinente para esta investigação: preservar a lógica algorítmica do modelo e, ao mesmo tempo, disponibilizá-la num ambiente de utilização mais acessível, orientado por uma interface (Machado et al., 2019 (#ref-machado-2019); Nilsiam & Pearce, 2017 (#ref-nilsiam-2017)).

Operacionalmente, a integração articula três elementos principais: os ficheiros .scad, formato de script utilizado pelo OpenSCAD para definir modelos geométricos por código; os parâmetros introduzidos ou ajustados na interface; e o ambiente de execução em WebAssembly. Quando o utilizador altera uma configuração, a plataforma envia os valores atualizados para um Web Worker, que aplica esses parâmetros ao modelo em OpenSCAD e gera a geometria tridimensional correspondente. O resultado é depois devolvido ao visualizador no navegador, permitindo observar os efeitos das alterações sem recorrer a software CAD instalado localmente. Este fluxo estabelece uma ligação direta entre edição paramétrica, cálculo geométrico e feedback visual, permitindo que o processo seja documentado, verificado e revisto dentro da própria plataforma.

Do ponto de vista metodológico, esta solução tem implicações importantes. Em primeiro lugar, preserva o estatuto do modelo paramétrico como especificação explícita e não como caixa negra geométrica. A plataforma não substitui o OpenSCAD por uma representação simplificada desligada do código; antes, torna o próprio núcleo algorítmico operável em ambiente web. Em segundo lugar, esta integração reduz a distância entre modelação e interação, permitindo que a exploração formal decorra num contexto mais observável e iterativo. O utilizador não necessita de dominar a sintaxe do OpenSCAD para beneficiar da estrutura paramétrica do modelo, mas essa estrutura continua a ser a base efetiva da geometria apresentada. Neste sentido, a plataforma atua como uma camada intermédia entre a disciplina técnica do código e a experiência configurável descrita na literatura sobre configuradores e sistemas de personalização digital (Nilsiam & Pearce, 2017 (#ref-nilsiam-2017); Ozdemir et al., 2022 (#ref-ozdemir-2022)).

Do ponto de vista técnico, o uso de Web Workers é especialmente relevante porque impede que a renderização bloqueie a interface principal. Em modelos geometricamente mais exigentes, o cálculo pode ser intensivo; se fosse executado diretamente na thread principal do navegador, comprometeria a fluidez da interação. Ao mover esse trabalho para um processo separado, a plataforma mantém uma experiência mais estável, mesmo quando a geração não é instantânea. A renderização permanece integralmente no lado do cliente, o que reforça a autonomia local do sistema e reduz o tráfego e a carga associados ao backend. Esta decisão complementa a arquitetura híbrida descrita na secção anterior: o servidor conserva funções de autenticação, persistência e mediação com serviços externos, enquanto o navegador assume a computação geométrica diretamente relacionada com a exploração paramétrica.

Esta integração tem ainda valor estratégico no contexto da investigação, pois aproxima a lógica da modelação baseada em código à acessibilidade operacional exigida por uma plataforma web. A literatura sobre OpenSCAD tem sublinhado precisamente a sua afinidade com fluxos repetíveis, configuradores digitais e a partilha de modelos paramétricos em ambientes abertos, ainda que, muitas vezes, fora de contextos de próteses e especificamente clínicos (Machado et al., 2019 (#ref-machado-2019); Nilsiam & Pearce, 2017 (#ref-nilsiam-2017)). No presente projeto, a adoção de WASM não representa apenas uma decisão de engenharia para “correr código no browser”; representa a tentativa de integrar, numa mesma infraestrutura, a transparência do modelo paramétrico, a observabilidade da interação e a capacidade de atualização iterativa da geometria.

Não obstante as vantagens, esta solução introduz limitações que importa reconhecer: O desempenho da renderização depende da complexidade do modelo, dos valores paramétricos escolhidos e dos recursos do dispositivo do utilizador, podendo resultar em tempos de espera mais longos para geometrias mais exigentes. Acresce que o carregamento inicial do módulo WASM, a serialização de dados entre a interface e o worker e a própria conversão da saída geométrica para formatos visualizáveis introduzem sobrecarga que não existe da mesma forma em ambientes CAD locais dedicados. Assim, a integração de OpenSCAD via WebAssembly deve ser entendida como um compromisso tecnicamente situado: amplia a acessibilidade e a autonomia local, mas apenas dentro dos limites computacionais e operacionais do navegador. O valor da solução reside, por isso, menos numa promessa de desempenho absoluto e mais na capacidade de tornar executável, em ambiente web, um núcleo paramétrico explícito, verificável e sujeito a revisão crítica.

### 5.4 Estrutura funcional da plataforma

A estrutura funcional da plataforma organiza-se num conjunto de módulos interligados que suportam o ciclo completo de configuração paramétrica: seleção do modelo, introdução e edição de parâmetros, visualização tridimensional, sugestões assistidas por IA, gestão de configurações e administração multiutilizador.Esta organização modular permite distribuir as funcionalidades da plataforma, ao mesmo tempo que estrutura o processo de personalização como uma sequência legível de operações.

Em vez de expor o utilizador a um ambiente indiferenciado de opções, a plataforma reparte o trabalho por etapas e componentes com funções distintas, o que está de acordo com a literatura sobre configuradores digitais, segundo a qual a eficácia da personalização depende, em grande medida, da clareza com que o sistema delimita o espaço de ação disponível e articula feedback com decisão (Ozdemir et al., 2022 (#ref-ozdemir-2022); Peixoto et al., 2025 (#ref-peixoto-2025)).

A Figura 5.3 ilustra um precedente particularmente próximo desta lógica: uma ferramenta paramétrica orientada a terapeutas ocupacionais, na qual múltiplas variantes de produto podem ser configuradas a partir de dimensões, materiais e pesos ajustáveis. A sua pertinência para esta dissertação reside em demonstrar que a parametrização ganha valor quando é mediada por uma interface acessível a profissionais que não são necessariamente especialistas em modelação CAD.

(Li & Aflatoony, 2025 (#ref-li-aflatoony-2025)).

![](projecto-completo_media/image17.png)

Figura 5.3 — Ferramenta paramétrica para configuração de ajudas técnicas com variação de dimensões, materiais e peso.

Fonte original: Li, M., & Aflatoony, L. (2025). Parametric design and three-dimensional printing: Enabling occupational therapists to develop custom hand grips. Disability and Rehabilitation: Assistive Technology, 20(6), 1829-1837. [https://doi.org/10.1080/17483107.2025.2483953](https://doi.org/10.1080/17483107.2025.2483953)

O ponto de entrada do sistema é o módulo de seleção de modelos. Cada modelo é descrito por um ficheiro de configuração que inclui o identificador, a descrição, o ficheiro OpenSCAD associado e a lista de parâmetros editáveis. A partir dessa estrutura, a interface gera automaticamente os controlos necessários para editar esses parâmetros, incluindo campos numéricos, seletores de valores dentro de intervalos definidos, caixas de seleção e campos de texto. Esta opção reduz a rigidez do sistema e permite acomodar famílias distintas de modelos paramétricos sem exigir reprogramação manual de cada ecrã. Em termos funcionais, este módulo atua como mediador entre a biblioteca de modelos e a interface, convertendo uma estrutura técnica de ficheiros e parâmetros num ponto de entrada compreensível para a configuração.

O núcleo operativo da plataforma situa-se, depois, na articulação entre o módulo de edição paramétrica e o de visualização 3D. Quando os parâmetros são alterados, o sistema recompõe o código, aciona a renderização local e devolve ao utilizador a geometria atualizada. Esta ligação direta entre edição e pré-visualização é decisiva do ponto de vista funcional, pois transforma a manipulação de variáveis abstratas em observação imediata das suas consequências formais. Funções de reposição de valores por defeito, atualização incremental e exportação de ficheiros STL ou 3MF alargam esta utilidade para além da mera experimentação visual, aproximando a plataforma de um ambiente de prototipagem e de preparação para fabrico. A literatura sobre interfaces para configuração assistida em contexto protésico sugere precisamente que a legibilidade do processo melhora quando o utilizador consegue relacionar a ação, a consequência geométrica e a possibilidade de validação num mesmo circuito de interação (Peixoto et al., 2025 (#ref-peixoto-2025); Quintero et al., 2018 (#ref-quintero-2018)).

Sobre esta base opera o módulo de apoio por inteligência artificial, que introduz uma camada adicional de mediação sem substituir a lógica principal da configuração. A partir de uma descrição livre do utilizador, ou de medidas antropométricas parciais, a interface constrói dinamicamente um pedido que inclui o esquema atual do modelo selecionado: nomes dos parâmetros, legendas, tipos, limites mínimos e máximos e valores correntes. Esse pedido é enviado ao servidor por uma rota autenticada, que atua como intermediário entre a plataforma e o serviço externo de IA. A resposta esperada é um objeto JSON simples, composto apenas por pares parâmetro-valor. A aplicação aceita apenas chaves existentes no esquema, descarta parâmetros desconhecidos e aplica os valores resultantes aos controlos antes de acionar uma nova renderização em OpenSCAD/WebAssembly.

Esta arquitetura corrige uma fragilidade identificada numa versão anterior do sistema, em que o pedido à IA permanecia demasiado associado a um modelo já removido e podia induzir sugestões com nomes de parâmetros inexistentes. Ao ancorar a sugestão no esquema vivo do modelo ativo, a IA passa a operar sobre a mesma gramática paramétrica que a interface, os perfis antropométricos importados e o modelo OpenSCAD. O papel funcional deste módulo não é gerar autonomamente a prótese, mas sim ampliar a capacidade exploratória do sistema, sugerindo pontos de partida plausíveis e ajudando a reduzir a carga inicial de parametrização. Nesta perspetiva, o módulo de IA integra-se no fluxo como suporte à decisão, e não como instância soberana de configuração, o que mantém coerência com a lógica human-in-the-loop assumida no projeto.

A evolução posterior do módulo acrescentou uma ancoragem opcional em dados populacionais. Quando o frontend envia a descrição do paciente e o identificador do modelo, o servidor procura o perfil antropométrico populacional mais próximo, considerando atributos como sexo, idade aproximada e país, e projeta as médias desse perfil sobre os parâmetros disponíveis no modelo ativo. O bloco de referência é então anexado ao pedido enviado à IA como ponto de ancoragem quantitativo, permitindo orientar a sugestão paramétrica sem se sobrepor a medições diretamente fornecidas pelo utilizador. Esta solução reforça a continuidade entre três formas de introdução de dados na plataforma: a seleção manual de um perfil populacional de referência, a importação de perfis antropométricos e a sugestão assistida por IA.

Outro componente central é o módulo de gestão de configurações. A possibilidade de nomear, guardar, recuperar, atualizar e eliminar instâncias de personalização é particularmente relevante num processo iterativo, em que diferentes variantes podem corresponder a hipóteses sucessivas de trabalho e não apenas a estados finais. Funcionalmente, este módulo transforma a configuração de um ato momentâneo numa sequência acumulativa, na qual diferentes estados podem ser guardados, recuperados e comparados ao longo do processo, permitindo retomar versões anteriores, comparar alternativas e sustentar processos de revisão progressiva. Deste modo, a gestão de configurações não é uma simples conveniência de interface: é parte integrante da estrutura funcional que torna a personalização verificável e acumulável ao longo do tempo.

Por fim, a plataforma inclui um módulo administrativo e de controlo de acesso que suporta a organização multi-utilizador. Este módulo assegura a criação de contas, a diferenciação de permissões, a atribuição de utilizadores a técnicos e a delimitação das ações acessíveis a cada perfil.

A sua presença confirma que a estrutura funcional da plataforma abrange a manipulação de parâmetros, a visualização de formas e a gestão das relações entre agentes, responsabilidades e níveis de intervenção. Neste sentido, a aplicação obtém sugestões paramétricas através do servidor, que comunica com serviços externos por intermédio de um proxy seguro, enquadrando essa capacidade numa estrutura funcional mais ampla, em que configuração, supervisão e persistência coexistem como partes de um mesmo sistema operativo.

A biblioteca de modelos integrada na plataforma confirma esta lógica modular. Em vez de tratar a prótese como um único ficheiro estático, o sistema organiza diferentes famílias de próteses como modelos registados, cada uma com parâmetros, dependências, limites e modos de visualização próprios. Esta decisão permitiu comparar estratégias distintas de integração: modelos reconstruídos integralmente em OpenSCAD, modelos provenientes de geometrias existentes e modelos open source já paramétricos, mas não alinhados com a nomenclatura antropométrica da plataforma. A integração não consistiu, portanto, apenas em “carregar” ficheiros tridimensionais; consistiu em traduzir cada modelo para uma interface comum de parâmetros, mantendo as suas restrições mecânicas específicas.

No caso do Paraglider Hand, também conhecido como Flexible Flyer, a integração partiu de uma mão mecânica acionada pelo corpo, derivada da linhagem Phoenix e UnLimbited. O desafio principal não foi reconstruir a geometria dos dedos, já definida em OpenSCAD, mas alinhar a lógica original do modelo com os nomes canónicos usados pelo sistema. A palma passou a ser controlada pela largura metacarpal, enquanto os dedos foram associados a comprimentos digitais independentes. Esta separação foi importante porque a largura da palma e o comprimento dos dedos não variam necessariamente de forma proporcional. Ao mesmo tempo, a palma teve de manter escalonamento uniforme, uma vez que os furos cilíndricos para pinos metálicos não podem ser deformados em elipses sem comprometer a montagem. Assim, certas medidas, como o comprimento e a espessura da palma, foram mantidas como informação contextual para a IA e para o perfil antropométrico, mas não foram usadas como transformações geométricas ativas nesse modelo.

A integração do Paraglider também revelou limitações práticas da execução de OpenSCAD em WebAssembly. Alguns ficheiros originais usavam construções sintáticas não suportadas pela versão compilada para navegador, o que impediu a definição de módulos durante a renderização. A solução foi manter cópias corrigidas dos ficheiros necessários, preservar a origem do modelo e controlar explicitamente as dependências carregadas para o sistema virtual de ficheiros do navegador. Esta etapa teve relevância metodológica porque mostrou que a compatibilidade web não depende apenas da qualidade geométrica do modelo, mas também da forma como bibliotecas, ficheiros importados e variantes de sintaxe são organizados no fluxo digital.

O trabalho realizado sobre modelos do tipo Cyborg Beast/Flexy Hand teve uma função complementar. Estes modelos foram usados como base exploratória para testar uma reparametrização mais ampla, em que a geometria original foi reorganizada em torno de medidas antropométricas da palma, dos dedos, do punho e do membro residual. A versão antropométrica resultante não foi tratada como simples escala global: incorporou comprimentos digitais, espessuras estruturais, canais internos, parâmetros de hardware e dimensões de encaixe derivadas de medidas do antebraço. Essa experiência foi útil para clarificar a diferença entre adaptar um modelo existente por multiplicadores gerais e reconstruir a sua lógica dimensional em torno de uma estrutura antropométrica coerente. Mesmo quando determinados modelos permaneceram como material de desenvolvimento e comparação, contribuíram para estabilizar a taxonomia de parâmetros que a plataforma passou a exigir aos modelos ativos.

Em conjunto, estes casos mostram que a expansão da plataforma depende menos da quantidade de modelos disponíveis e mais da existência de uma gramática comum de integração. Cada nova prótese a integrar no sistema exige três operações: identificar quais parâmetros antropométricos são relevantes, decidir que parâmetros podem alterar a geometria sem quebrar interfaces mecânicas e declarar essas relações de forma compreensível para a interface, para o renderizador e para a camada de IA. A biblioteca de modelos torna-se, assim, um campo de validação técnica da própria arquitetura: quanto mais heterogéneos forem os modelos integrados, mais clara se torna a necessidade de separar dados antropométricos, regras geométricas, restrições de fabrico e sugestões assistidas.

### 5.5 Gestão de parâmetros, versões e expansão

Controlar parâmetros constitui uma das condições centrais para transformar um modelo paramétrico num sistema utilizável e persistente. No caso da plataforma desenvolvida, essa gestão é operacionalizada através de ficheiros de configuração que descrevem cada parâmetro segundo atributos como nome, tipo, valor inicial, limites, incrementos e agrupamento temático. Esta estrutura não cumpre apenas uma função técnica de leitura na interface; formaliza a relação entre o código OpenSCAD, o espaço de variação permitido e os mecanismos de controlo disponibilizados ao utilizador. Em termos metodológicos, esta opção aproxima-se da lógica descrita na literatura sobre configuradores e personalização digital, segundo a qual a eficácia do sistema depende da capacidade de expor apenas parâmetros relevantes, dentro de limites inteligíveis e controlados, preservando a coerência interna do modelo-base (Ozdemir et al., 2022 (#ref-ozdemir-2022); Lei et al., 2016 (#ref-lei-2016)).

Ao descrever os parâmetros em estruturas independentes do código geométrico principal, a plataforma obtém duas vantagens. A primeira é a rastreabilidade: torna-se possível saber quais variáveis são editáveis, quais são os seus intervalos válidos e como se articulam com a interface. A segunda vantagem reside na possibilidade de adaptar a estrutura do próprio sistema: parâmetros podem ser adicionados, removidos ou ajustados sem que seja necessário reescrever integralmente a lógica de interação. Assim, a gestão de parâmetros funciona como uma camada intermédia entre a definição geométrica e a experiência de uso, permitindo que o modelo permaneça tecnicamente explícito sem exigir que o utilizador interaja diretamente com a sua sintaxe interna.

A gestão de versões manifesta-se, neste estágio do projeto, sobretudo por meio do armazenamento de configurações salvas. A plataforma permite conservar diferentes conjuntos de parâmetros associados ao mesmo modelo, atribuindo-lhes identificação própria, notas descritivas e associação a um utilizador específico. Embora esta solução ainda não corresponda a um sistema completo de gestão de versões, como os utilizados no desenvolvimento de software, já suporta uma função relevante para o processo de projeto: acompanhar a configuração ao longo do tempo, preservar variantes e permitir a comparação entre estados sucessivos do mesmo artefacto. Cada configuração registada pode, assim, ser entendida como uma instância documentada do processo de personalização, passível de recuperação, comparação e revisão, e não apenas como um ficheiro transitório. Esta capacidade é particularmente importante num contexto em que a personalização não é um ato único, mas uma sequência de aproximações, testes e revisões.

Do ponto de vista funcional, a persistência dessas configurações em estruturas JSON associadas a modelos e utilizadores reforça a continuidade entre interação, revisão e reutilização. O sistema deixa, assim, de limitar a configuração ao estado temporário da sessão e passa a preservar um registo das configurações realizadas, possibilitando retomar soluções anteriores, documentar alternativas exploradas e preparar comparações futuras entre versões. Esta forma de gestão prática de versões é coerente com o caráter experimental da plataforma: ainda não pretende substituir mecanismos mais sofisticados de gestão de revisões, mas fornece uma base suficiente para sustentar o acompanhamento iterativo do desenvolvimento e a análise reflexiva do processo.

Quanto à capacidade de expansão, a plataforma beneficia de uma arquitetura modular e orientada por ficheiros de configuração. A separação entre modelos, parâmetros, interface, autenticação e persistência permite acrescentar novos modelos em OpenSCAD, novos tipos de parâmetros ou novas rotinas de apoio sem reestruturar integralmente a aplicação. Na prática, a introdução de um novo modelo exige sobretudo a adição do ficheiro .scad correspondente e o seu registo no ficheiro de configuração dos modelos (models-config.json). Esta estrutura evidencia uma lógica de expansão baseada menos na duplicação de código e mais na extensão controlada da plataforma. Esta característica é consistente com a literatura sobre sistemas paramétricos e famílias de produto, que associa robustez e expansão sustentável à qualidade das estruturas relacionais, e não ao aumento indiscriminado de opções ou de módulos independentes (Lei et al., 2016 (#ref-lei-2016); Ozdemir et al., 2022 (#ref-ozdemir-2022)).

Todavia, esta lógica de expansão deve ser analisada criticamente.

O recurso ao SQLite é adequado a um protótipo funcional com um número reduzido ou moderado de acessos simultâneos, mas poderá revelar limitações em cenários de utilização mais intensiva, com maior volume de configurações, operações frequentes de leitura e escrita ou necessidades mais exigentes de auditoria e sincronização.

De forma semelhante, a renderização local via WASM, embora eficaz em muitos contextos, depende do desempenho do dispositivo do utilizador, o que introduz variabilidade na experiência e impõe limites ao crescimento indiscriminado da complexidade geométrica. Para além da integração de novas funcionalidades ou modelos, a expansão da plataforma depende da capacidade de sustentar esse crescimento sem comprometer a clareza da organização interna, o desempenho, a segurança e a facilidade de manutenção do sistema.

Neste sentido, a secção confirma uma conclusão importante para o projeto: a gestão de parâmetros, de configurações e da expansão futura integra a própria lógica de design da plataforma. A capacidade de configuração, a persistência e o crescimento controlado sustentam uma personalização paramétrica tecnicamente viável, documentável e sujeita a revisão ao longo do desenvolvimento.

## Capítulo 6 — Integração da Inteligência Artificial

### 6.1 Papel da IA no sistema proposto

No sistema desenvolvido, a IA assume uma função distinta daquela que surge com maior frequência nos estudos sobre próteses. Enquanto grande parte da investigação consultada se concentra em tarefas de controlo, interpretação de biosinais, reconhecimento de gestos e adaptação funcional, esta investigação explora a IA como camada de apoio à configuração paramétrica, articulada com dados antropométricos, modelos geométricos explícitos e interface web.

Os estudos consultados indicam que, no caso das próteses de membro superior, a aprendizagem automática tem sido aplicada sobretudo à classificação de sinais EMG, à inferência de intenção motora, isto é, à interpretação dos sinais corporais que permitem estimar o movimento que o utilizador pretende realizar, e à melhoria do desempenho operativo do dispositivo (Choo e Chang, 2023; Terrazas-Rodas e Carrión-Pérez, 2022; Hachoumi, Laabidi e Eddabbah, 2026; Batista, Vieira e Gaspar, 2025).

Em contrapartida, continuam pouco consolidadas as abordagens que articulam, no mesmo sistema, a entrada antropométrica, o modelo paramétrico explícito, a sugestão assistida de parâmetros e a supervisão técnica. Esta lacuna é central para a presente investigação, pois permite situar a proposta como uma articulação entre componentes que os estudos consultados tendem a desenvolver de forma fragmentada.

Neste enquadramento, a IA assume a função de camada complementar de apoio à configuração, operando sobre uma base paramétrica já definida e articulando-se com a lógica geométrica do modelo, a decisão de projeto e a validação técnica. A literatura sobre modelação paramétrica aplicada a próteses personalizadas e sobre fabrico aditivo mostra que há um fundamento técnico robusto para construir geometrias configuráveis com base em regras explícitas, parâmetros dimensionais e relações geométricas controladas. Estudos sobre próteses paramétricas para diferentes níveis de amputação de membros superiores, sobre a personalização de dedos protésicos por modelação paramétrica e sobre encaixes protésicos personalizados para próteses transradiais demonstram que a personalização pode ser estruturada através de modelos explícitos e fluxos CAD/CAM ajustáveis. (da Silveira Romero et al., 2025 (#ref-da-silveira-romero-2025); Lim et al., 2018 (#ref-lim-2018); Saldarriaga et al., 2024 (#ref-saldarriaga-2024)). O sistema aqui proposto parte precisamente desta premissa: a geometria não é gerada de forma opaca por um modelo autónomo, mas sim por um modelo paramétrico explícito, definido em OpenSCAD e manipulável por meio de parâmetros rastreáveis.

É neste ponto que a IA assume uma função específica. Em vez de atuar como gerador integral da forma, atua como um mecanismo de mediação entre os dados de entrada e a exploração inicial do espaço paramétrico. O seu papel é apoiar a tradução de informação antropométrica, de preferências funcionais e de critérios de fabrico em sugestões paramétricas plausíveis, reduzindo a complexidade associada à definição manual de valores iniciais e à navegação em sistemas com múltiplas dependências internas. Esta posição aproxima-se de abordagens data-driven orientadas a melhorar a adaptação, o conforto e a adequação estrutural, sem eliminar a necessidade de interpretação humana (Gu et al., 2024 (#ref-gu-2024)).

No processo de desenvolvimento, a IA funciona como uma ferramenta de apoio à decisão e à iteração: propõe pontos de partida, ajuda a comparar cenários, acelera os ciclos de teste e permanece articulada com a estrutura técnica do sistema.

Entre os antecedentes mais próximos desta lógica encontram-se trabalhos que combinam personalização anatómica, modelação paramétrica, fabrico aditivo e componentes inteligentes, como o estudo de Romero et al. (2025) (#ref-da-silveira-romero-2025), bem como modelos de otimização estrutural orientados por dados anatómicos e restrições de adaptação, como o proposto por Gu et al. (2024) (#ref-gu-2024).

Esta leitura é coerente com a arquitetura da plataforma descrita no capítulo anterior. O sistema separa a camada de interface, a lógica paramétrica, a renderização local em WebAssembly e a comunicação controlada com serviços externos de IA. Tal organização é metodologicamente relevante porque preserva uma continuidade verificável entre a entrada inicial, a sugestão produzida pela IA e o resultado geométrico gerado pelo modelo. Em vez de encerrar o processo num modelo generativo pouco transparente, o sistema mantém a IA supervisionado e num estado de apoio: sugere, mas não determina autonomamente; apoia, mas não valida; acelera, mas não substitui o julgamento técnico. Esta opção é importante, considerando que a supervisão clínica ou técnica permanece limitada em vários estudos que já articulam modelação digital, CAD, IA, co-design assistido ou impressão 3D (Romero et al., 2025 (#ref-da-silveira-romero-2025); Elbreki et al., 2022 (#ref-elbreki-2022); Idris et al., 2024 (#ref-idris-2024)). O valor da IA reside na sua capacidade de reforçar um processo de personalização já estruturado por lógica paramétrica explícita, por requisitos de fabrico e por responsabilidade humana e menos na promessa de automatização total.

### 6.2 IA na parametrização, personalização e apoio à decisão

No domínio da parametrização, a inteligência artificial torna-se mais relevante quando opera sobre uma estrutura geométrica previamente formalizada, em vez de tentar substituí-la. Em sistemas como o aqui proposto, isso significa receber dados antropométricos, requisitos funcionais e restrições de fabrico e convertê-los em sugestões iniciais para os parâmetros já definidos no modelo. A literatura sobre próteses paramétricas e personalização anatómica mostra que a customização eficaz depende de relações explícitas entre medidas, proporções e componentes geométricos, e não apenas da introdução isolada de valores numéricos (Saldarriaga et al., 2024 (#ref-saldarriaga-2024); da Silveira Romero et al., 2025 (#ref-da-silveira-romero-2025)). Neste enquadramento, a IA amplia a capacidade de utilização do modelo paramétrico, ajudando a propor intervalos plausíveis, combinações coerentes entre variáveis e pontos de partida mais ajustados ao caso específico.

No plano da personalização, esta mediação é importante porque a adaptação de uma prótese exige o controlo independente de diferentes parâmetros anatómicos, funcionais e construtivos, ultrapassando a simples alteração proporcional da escala do modelo. A literatura indica que diferentes parâmetros podem ter de ser controlados de forma independente para respeitar as proporções anatómicas, o conforto, a mobilidade e os requisitos de montagem. O estudo de Lim et al. (2018) (#ref-lim-2018), por exemplo, demonstra que o comprimento e a largura de um dedo protésico podem exigir ajustamentos independentes, uma vez que não evoluem necessariamente segundo uma relação linear e proporcional. Este resultado reforça a necessidade de parametrizações mais precisas do que simples operações de escala.

De forma convergente, Gu et al. (2024) (#ref-gu-2024) mostram que abordagens orientadas por dados podem apoiar a adaptação estrutural e a qualidade do ajuste ao corpo, sugerindo que métodos inteligentes podem ajudar a antecipar relações entre geometria, desempenho e conforto. No sistema proposto, a IA funciona, assim, como uma camada de inferência preliminar sobre um espaço paramétrico já estruturado, orientando a exploração inicial das configurações.

A operacionalização desta lógica ocorre em dois objetos distintos. O primeiro é um vetor numérico de parâmetros geométricos, consumido diretamente pela interface e pelos modelos OpenSCAD. O segundo é um contexto semântico para a IA, que descreve a origem das medições, campos em falta, incerteza, valores atípicos, tolerâncias, hardware selecionado e notas sobre parâmetros derivados. Esta separação é importante porque impede confundir cálculo geométrico com raciocínio assistido: os parâmetros numéricos alimentam o modelo; o contexto semântico ajuda a IA a explicar, ponderar ou sugerir ajustes, mas não substitui as regras determinísticas que geram a geometria.

No protótipo implementado, esta separação é materializada pela construção dinâmica do pedido enviado ao modelo de linguagem. O pedido inclui a descrição livre do utilizador, o esquema vivo do modelo selecionado, os nomes exatos dos parâmetros, as legendas, os tipos, os limites e os valores correntes. Quando existe correspondência com um perfil populacional importado, inclui também as médias medidas desse grupo como referência explícita. Deste modo, a IA não infere valores num espaço aberto: opera dentro de uma gramática paramétrica previamente declarada, limitada pelo modelo ativo e sujeita a filtragem posterior pela aplicação.

O apoio à decisão emerge precisamente desta capacidade de transformar dados de entrada em cenários comparáveis. Em vez de produzir uma única configuração apresentada como “ótima”, a integração da IA revela maior utilidade quando ajuda a explicitar compromissos entre robustez, leveza, amplitude de ajuste, rapidez de fabrico, facilidade de montagem e adequação anatómica. Esta lógica está alinhada com exemplos recentes de integração entre digitalização, modelação paramétrica, fabrico aditivo e sistemas inteligentes, como o trabalho de Romero et al. (2025) (#ref-da-silveira-romero-2025), ainda que aí a componente de IA esteja mais ligada ao controlo mioelétrico do que à sugestão paramétrica em ambiente web. A pertinência desse precedente reside menos na equivalência técnica direta e mais no facto de mostrar que a personalização digital e a camada inteligente podem coexistir no mesmo fluxo, desde que cada componente mantenha uma função claramente delimitada.

É por isso que, nesta investigação, a personalização assistida por IA deve ser entendida como uma prática de human-in-the-loop.O sistema procura ampliar a capacidade de análise e de exploração do protesista, do designer ou do utilizador informado. A IA pode sugerir configurações iniciais, organizar alternativas, sinalizar dependências entre parâmetros e tornar mais claras certas consequências de projeto, a aceitação final, porém, continua dependente de verificação técnica e de julgamento contextual. Deste modo, a parametrização assistida por IA não corresponde a uma automatização cega da personalização, mas a um mecanismo de apoio à decisão que atua sobre uma base geométrica explícita, documentada e tecnicamente verificável.

### 6.3 Validação antropométrica assistida por IA no sistema

A validação antropométrica assistida por IA realizada no sistema deve ser entendida como validação interna de plausibilidade e de coerência paramétrica, não como validação clínica da prótese final.  O objetivo consistiu em avaliar se uma descrição em linguagem natural, produzida por uma pessoa sem conhecimento especializado sobre medições da mão, poderia ser convertida num conjunto inicial de parâmetros anatómica e tecnicamente plausível. Esta formulação delimita o alcance da validação realizada: a plataforma permite verificar a conformidade com o esquema de parâmetros, os intervalos declarados, a proporcionalidade digital e a coerência de lateralidade, mas a demonstração de conforto, segurança, desempenho funcional ou adequação terapêutica exige avaliação técnica e clínica posterior.

O ensaio foi estruturado a partir da cadeia funcional implementada na plataforma: descrição livre do caso, construção do pedido no frontend com injeção do esquema vivo do modelo, chamada autenticada à rota de sugestão por IA, resposta JSON com valores paramétricos, filtragem de chaves desconhecidas e aplicação dos valores válidos aos controlos do modelo. Esta arquitetura tem uma consequência importante: a IA não trabalha sobre uma lista genérica de medidas, mas sobre os parâmetros efetivamente disponíveis no modelo ativo, incluindo nomes exatos, legendas, limites e valores correntes. Assim, a validação não incidiu apenas sobre os números sugeridos, mas também sobre a capacidade do fluxo de manter continuidade entre linguagem natural, estrutura antropométrica, interface e geração geométrica.

Foram definidos cinco critérios de verificação. O primeiro foi a conformidade com o esquema: a saída deveria ser JSON válido, conter apenas nomes de parâmetros existentes e respeitar os limites mínimos e máximos declarados. O segundo foi a proporcionalidade dos dedos, exigindo uma ordenação anatómica plausível, com o dedo médio como referência mais longa, o dedo mínimo como mais curto e o polegar abaixo do comprimento do dedo médio. O terceiro foi a plausibilidade adulta, usando como referência os intervalos antropométricos canónicos já adotados no sistema. O quarto foi a adequação etária, sobretudo em perfis infantis ou adolescentes. O quinto critério foi a lateralidade em casos de amputação unilateral, verificando se o parâmetro responsável pela inversão lateral gerava a mão correspondente ao lado amputado, e não uma réplica da mão medida.

O primeiro conjunto experimental usou cinco perfis sintéticos descritos apenas por indicadores populacionais indiretos, como idade, sexo, altura, peso, país, envergadura ou constituição física, sem qualquer medição direta da mão. Este cenário corresponde ao caso de menor literacia técnica: o utilizador não sabe medir o membro superior e/ou mão com rigor, mas consegue fornecer informação demográfica geral. Nas cinco situações, a IA produziu valores dentro dos limites do modelo, manteve a ordem anatómica dos dedos e gerou dimensões compatíveis com a idade e a constituição descritas. A redução espontânea dos parâmetros relativos aos componentes mecânicos num perfil infantil também mostrou que o modelo de linguagem utilizou as legendas do esquema, e não apenas os nomes técnicos dos parâmetros.

O segundo conjunto experimental avaliou três graus de detalhe dos dados de entrada em cenários de amputação unilateral. Num caso com medições completas da mão intacta, os valores fornecidos foram preservados e o sistema sugeriu a mão correspondente ao lado amputado.

Num caso parcial, com apenas a largura da palma e dados demográficos, a medida fornecida foi mantida e as dimensões em falta foram estimadas de modo proporcional. Num caso apenas demográfico, a IA gerou um conjunto completo de medidas plausíveis. Nos três casos, a lateralidade sugerida foi correta. Este resultado é relevante porque mostra que a IA consegue ajustar a resposta à informação disponível: usa medições diretas quando existem, estima valores a partir de dados parciais e recorre a referências populacionais quando apenas existe uma descrição geral.

Numa etapa posterior, a validação foi prolongada para além da resposta numérica, acompanhando o percurso completo até à exportação dos modelos nos formatos STL e 3MF, utilizados na preparação de ficheiros para impressão 3D.

Nesta etapa, foram testadas descrições de utilizadores em três mãos ativas na plataforma — Flexy Beast, Paraglider Hand e UnLimbited Phoenix —, utilizando o fluxo real de sugestão por IA. O procedimento incluiu a aplicação dos parâmetros sugeridos, a exportação das geometrias e a medição das malhas resultantes.

O objetivo desta etapa foi confirmar se a coerência paramétrica observada no JSON chegava efetivamente à geometria imprimível e se diferentes modelos respondiam de forma previsível aos mesmos perfis antropométricos.

Os resultados devem, contudo, ser lidos com cautela. A execução documentada corresponde a uma amostra representativa, não a uma caracterização estatística completa da distribuição de saídas.

A repetição do mesmo perfil produziu pequenas variações, na ordem de poucos milímetros, preservando as relações anatómicas essenciais e os limites do modelo. Esta variação confirma a natureza estocástica da componente de IA: mesmo perante o mesmo perfil, o sistema pode produzir respostas ligeiramente diferentes entre execuções sucessivas.

Observou-se também uma forma de variabilidade estrutural: em algumas execuções, certos parâmetros relativos aos componentes mecânicos foram devolvidos explicitamente; noutras, foram omitidos, mantendo-se o valor corrente do modelo. Ambas as respostas são aceitáveis segundo a especificação atual do sistema, mas reforçam a necessidade de avaliar propriedades estáveis, e não valores exatos isolados.

A principal fragilidade identificada nas validações posteriores relaciona-se com a lateralidade da configuração protésica. Nos primeiros testes, baseados em descrições de casos de amputação unilateral, o sistema gerou corretamente a mão correspondente à situação descrita. Contudo, numa verificação posterior centrada no utilizador, com pedidos explícitos para uma mão esquerda, observou-se que a IA tendia a devolver sistematicamente o valor correspondente à mão direita.

Esta fragilidade foi tratada como um risco de configuração com implicações na adequação funcional do modelo. Para a corrigir, a lateralidade passou a ser definida diretamente pela interface como uma condição determinística do sistema. O parâmetro correspondente foi identificado no esquema com a função role: "laterality", retirado do conjunto de valores que a IA pode sugerir e incluído no pedido como informação fixa. Caso a resposta da IA inclua novamente esse parâmetro, o sistema ignora-o durante a validação da resposta. Desta forma, a lateralidade da configuração protésica passa a ser controlada pela plataforma, em vez de depender da interpretação textual realizada pelo modelo de linguagem.A principal conclusão desta validação é que a IA pode facilitar o acesso à configuração paramétrica, ao transformar descrições incompletas e não técnicas em pontos de partida editáveis, coerentes e passíveis de verificação. Esta função só se torna metodologicamente defensável quando a sugestão permanece ancorada no esquema do modelo, limitada por intervalos definidos, filtrada pela interface e sujeita a revisão humana.

Deste modo, a validação antropométrica assistida por IA contribui para reduzir a barreira inicial de configuração e para tornar a parametrização mais acessível, mas não substitui medição direta, avaliação técnica, prototipagem física nem validação clínica.

### 6.4 Ajuste, validação e limitações éticas e técnicas

A introdução de IA num sistema como o proposto exige distinguir claramente entre sugestão paramétrica, ajuste efetivo e validação final. Uma recomendação produzida por um modelo de IA pode ser útil como ponto de partida, mas não equivale a uma prova de adequação funcional, de conforto ergonómico ou de segurança estrutural. O ajuste real de uma prótese depende sempre de confirmação em contexto técnico e, idealmente, de iterações de teste, observação e refinamento. Por essa razão, os valores sugeridos pela IA devem ser entendidos como hipóteses operativas sujeitas a validação posterior, e não como prescrições definitivas.

Do ponto de vista técnico, subsistem limitações significativas. A IA pode produzir sugestões plausíveis, mas inadequadas para casos extremos, perfis antropométricos pouco representados ou combinações paramétricas fora da distribuição esperada. Pode também introduzir inconsistências difíceis de detetar se a sua saída não for confrontada com restrições geométricas, limites de fabrico e critérios funcionais explícitos. Assim, a integração robusta da IA depende da existência de salvaguardas incorporadas no próprio sistema, incluindo limites paramétricos, validação de intervalos, verificação de coerência entre módulos, comparação entre alternativas e supervisão humana capaz de identificar sugestões tecnicamente infundadas ou insuficientemente justificadas. Esta necessidade de enquadramento crítico é coerente com a literatura sobre responsabilidade no design assistido por IA, que sublinha a importância de compreender os dados considerados, os critérios aplicados e os limites das sugestões produzidas pelo modelo.(Panchal et al., 2019 (#ref-panchal-2019); Yüksel et al., 2023 (#ref-yuksel-2023)).

A Figura 6.1 sintetiza esta tensão entre desafios de explicabilidade e princípios de IA responsável. No contexto desta investigação, a figura é útil porque torna explícito que a responsabilidade não depende apenas de desempenho preditivo, mas de condições como transparência, auditabilidade, privacidade, justiça e prestação de contas. Estes princípios reforçam a opção do sistema por uma IA assistiva, limitada por regras e sujeita a revisão humana (Barredo Arrieta et al., 2020 (#ref-arrieta-2020)).

![](projecto-completo_media/image18.png)

Figura 6.1 — Relação entre desafios de explicabilidade e princípios de IA responsável.

Adaptação de Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82-115. [https://doi.org/10.1016/j.inffus.2019.12.012](https://doi.org/10.1016/j.inffus.2019.12.012)

As limitações éticas assumem particular relevância num domínio associado a dispositivos personalizados e potencialmente sensíveis, exigindo atenção à recolha excessiva de dados, à exposição desnecessária de informação pessoal e ao risco de aceitar sugestões algorítmicas como se fossem neutras ou automaticamente válidas.

Mesmo quando a plataforma utiliza apenas dados antropométricos não clínicos ou cenários experimentais, a sua arquitetura deve limitar a recolha ao necessário, controlar quem pode aceder às configurações e explicitar que a IA atua como apoio à configuração, e não como autoridade técnica ou clínica.

A plataforma deve comunicar de forma clara que a IA desempenha uma função de apoio à decisão no processo de configuração, sem assumir autoridade clínica ou validar autonomamente a adequação da prótese. Esta delimitação é essencial para evitar deslocamentos indevidos de responsabilidade e para definir corretamente o âmbito da ferramenta

Por fim, subsiste uma limitação metodológica mais ampla: a qualidade da IA depende da qualidade das estruturas em que se insere. Sem modelos paramétricos bem definidos, sem critérios de validação claros e sem dados suficientemente representativos, a IA tende a amplificar incerteza em vez de a reduzir. Neste sentido, a sua integração só se torna relevante quando articulada com uma base projetual explícita, com procedimentos de verificação e com uma compreensão crítica das suas margens de erro. A principal contribuição da IA para o sistema proposto não reside, portanto, numa promessa de automatização total, mas na possibilidade de reforçar processos de personalização e decisão, desde que permaneça enquadrada por regras, validação e responsabilidade humanas.

## Capítulo 7 — Interface, Interação e Experiência de Utilização

### 7.1 Estratégia de interação e decisões de UI/UX

O ponto de partida desta secção é a necessidade de tornar acessível, através da interface, um sistema de modelação paramétrica baseado em código. A plataforma procura traduzir essa complexidade técnica em operações compreensíveis, permitindo selecionar modelos, introduzir dados antropométricos, ajustar parâmetros, observar resultados e guardar configurações sem exigir contacto direto com a estrutura interna do código.Em vez de exigir contacto direto com a estrutura interna do modelo, a aplicação organiza a interação em torno de ações reconhecíveis e progressivas, como selecionar um modelo, introduzir dados antropométricos, ajustar parâmetros, observar o resultado e guardar configurações.

Esta opção traduz uma decisão deliberada de desenho da interface: a plataforma não procura ocultar a natureza técnica do sistema, mas reorganizá-la em operações compreensíveis, sequenciais e verificáveis. Esta abordagem aproxima-se de modelos que valorizam a orientação inicial do utilizador no contacto com a plataforma, a navegação guiada e a redução da carga interpretativa em processos de personalização protésica (Colombo et al., 2015 (#ref-colombo-2015); Peixoto et al., 2025 (#ref-peixoto-2025)).

Do ponto de vista estrutural, a interface assenta numa lógica de composição modular e orientada por tarefa. O utilizador não enfrenta um ambiente tridimensional aberto nem um editor de código, mas sim um conjunto de módulos de interação cuja organização corresponde a etapas reconhecíveis do processo de configuração. A seleção do modelo funciona como ponto de entrada; os parâmetros surgem depois como elementos editáveis com correspondência direta a propriedades geométricas; a visualização tridimensional atua como mecanismo de feedback contínuo; e as ações de guardar, recuperar ou exportar prolongam o processo para além do momento de configuração imediata. Esta organização procura reduzir carga cognitiva, evitar navegação errática e manter uma relação legível entre intenção, ação e consequência formal. Os estudos analisados sugerem que os sistemas de configuração mais eficazes distinguem visualização, ajuste e validação em camadas de interação claras, tanto em plataformas web orientadas para o utilizador final como em interfaces destinadas a profissionais responsáveis pelo ajuste protésico (Peixoto et al., 2025 (#ref-peixoto-2025); Quintero et al., 2018 (#ref-quintero-2018)).

Uma decisão particularmente relevante reside na forma como a interface traduz a lógica paramétrica em linguagem operacional. Cada controlo não representa apenas um valor numérico isolado, mas também um ponto de acesso a relações geométricas que permanecem definidas no modelo. Em termos de UI/UX, isto significa que a plataforma deve tornar editável apenas o que pode ser interpretado, observado e, idealmente, revisto de forma responsável. A estratégia de interação não consiste, portanto, em maximizar liberdade aparente, mas em expor uma parte controlada do espaço de variação. Esta contenção é importante porque, em sistemas configuráveis aplicados a próteses, excesso de liberdade pode gerar combinações pouco inteligíveis, tecnicamente frágeis ou difíceis de validar. A interface atua como filtro e mediadora: aumenta a acessibilidade sem comprometer a coerência interna do modelo paramétrico.

A articulação entre edição paramétrica e pré-visualização constitui outra decisão relevante, pois a renderização local através de WebAssembly permite que a resposta visual resulte diretamente da geometria gerada pelo sistema, evitando o recurso a imagens estáticas ou a representações simplificadas desligadas do modelo.

Em termos de experiência, isto reforça a sensação de continuidade entre o controlo paramétrico e a forma observada. Ao mesmo tempo, o uso de Web Workers protege a interface de bloqueios excessivos durante operações mais pesadas, contribuindo para uma interação mais estável e previsível. A experiência não é instantânea em todos os casos, mas a arquitetura foi concebida para que os tempos de espera sejam compreendidos como parte do processamento geométrico real, e não como uma falha arbitrária da interface. A importância deste feedback iterativo, da visualização em tempo real e de formas de manipulação mais naturais é coerente com trabalhos que articulam configuração assistida, visualização e ajuste progressivo em contextos protésicos, ainda que, muitas vezes, fora de plataformas web puras (Abbas Alili et al., 2023; Colombo et al., 2015 (#ref-colombo-2015); Peixoto et al., 2025 (#ref-peixoto-2025)).

A interface privilegia a clareza operacional em relação à exuberância formal, em coerência com o contexto do projeto: trata-se de uma ferramenta de configuração protésica, e não de um configurador lúdico ou promocional.

As decisões de desenho da interface procuram, assim, favorecer a clareza operacional, a consistência entre controlos, a previsibilidade das ações e o registo das alterações, mediando a passagem entre os dados do utilizador, as regras paramétricas, a assistência algorítmica e o resultado tridimensional. Esta clareza é particularmente relevante em sistemas protésicos inteligentes, nos quais importa equilibrar autonomia do utilizador, supervisão técnica e diferenciação de permissões entre utilizadores e profissionais (Bai et al., 2024 (#ref-bai-2024); Quintero et al., 2018 (#ref-quintero-2018)).

Deste modo, a estratégia de interação adotada não deve ser lida apenas como um conjunto de escolhas de interface, mas como uma decisão metodológica sobre a forma de tornar o processo de personalização observável, configurável e aberto à revisão crítica ao longo do desenvolvimento.

A UI/UX participa diretamente na construção do sistema, atuando como infraestrutura de mediação entre o conhecimento técnico, os dados individuais e a decisão do projeto. O seu objetivo não é simplificar artificialmente o problema, mas organizar a complexidade de forma inteligível, preservando continuidade com a lógica paramétrica do modelo e com o enquadramento de apoio da IA discutido no capítulo anterior.

### 7.2 Experiência do designer e do utilizador final

A plataforma foi estruturada para acomodar formas distintas de participação no processo de configuração, uma vez que designers, técnicos, clínicos e utilizadores finais não intervêm sobre os mesmos parâmetros nem assumem o mesmo grau de responsabilidade. Os estudos analisados sugerem que esta diferença não resulta apenas de níveis distintos de literacia técnica, mas também do tipo de decisão que cada interveniente é chamado a tomar.

Em sistemas de personalização protésica, diferentes domínios de configuração exigem distribuições distintas de autoridade. Quando estão em causa parâmetros ligados à geometria do encaixe, à biomecânica, à tolerância dos tecidos ou à viabilidade de fabrico, o papel do profissional tende a ser dominante, pois envolve interpretação especializada, validação contextual e responsabilidade técnica. Em contrapartida, quando a configuração incide sobre preferências de controlo, clareza do sistema ou aspetos estéticos que o utilizador consegue avaliar diretamente, a sua participação torna-se mais substantiva.

O contraste entre estes domínios é central para compreender a diferenciação entre perfis de uso, ainda que a literatura direta sobre plataformas paramétricas para o membro superior permaneça escassa e muitas conclusões tenham de ser complementadas por evidência transferível de contextos adjacentes (Cordella et al., 2016 (#ref-cordella-2016); Saldarriaga et al., 2024 (#ref-saldarriaga-2024)).

Para o designer, técnico especialista de próteses e ortóteses. ou clínico, a plataforma funciona sobretudo como um ambiente de trabalho orientado à configuração, ao teste, à comparação de alternativas e à supervisão do processo. O interesse principal deste perfil não está apenas em “ver” a prótese, mas em compreender como os parâmetros se relacionam, quais dependências estruturais existem entre dimensões e quais efeitos pequenas alterações podem produzir na geometria final ou no comportamento do sistema. A evidência transferível proveniente de plataformas de configuração e afinação em contexto protésico indica que profissionais valorizam interfaces que reduzam tempo de ajuste, tornem o espaço paramétrico mais interpretável e mantenham uma continuidade suficiente com o raciocínio clínico ou técnico habitual, incluindo ambientes em que conhecimento especializado é codificado em regras, sugestões iniciais ou ferramentas de comparação (Colombo et al., 2015 (#ref-colombo-2015); Quintero et al., 2018 (#ref-quintero-2018); Bai et al., 2024 (#ref-bai-2024)). Os estudos consultados mostram, contudo, que a digitalização só reforça a confiança profissional quando mantém continuidade com elementos relevantes do processo de ajuste. A redução de indícios tácteis, empíricos ou processuais pode limitar formas de saber prático associadas à experiência clínica e técnica, como sugerem os estudos sobre retificação digital e fluxos CAD/CAM.

No caso do utilizador final, a experiência tende a concentrar-se na compreensão do processo, na construção de confiança e na perceção de participação. Mesmo quando nem todos os parâmetros são diretamente editáveis, a visualização do modelo, o reconhecimento das alterações e o acompanhamento da personalização contribuem para tornar a configuração menos opaca. A interface contribui, assim, para tornar a adaptação menos distante do utilizador, apresentando-a como um processo parcialmente observável, compreensível e passível de acompanhamento.

Quando a aceitação de uma prótese não depende apenas do desempenho funcional, mas também da perceção de adequação, de participação e de controlo sobre o resultado, este aspecto assume relevância. Os estudos analisados sugerem, de forma consistente, que a clareza com que o sistema comunica o seu funcionamento influencia a experiência de utilização.

Quando a plataforma torna mais visíveis os efeitos das ações, os limites das escolhas e a relação entre os dados introduzidos e o comportamento do modelo, reforça a facilidade de utilização e a confiança subjetiva.

As plataformas de personalização estética e os sistemas com visualização explícita do espaço de decisão sugerem que a participação ativa do utilizador aumenta quando as opções editáveis são claras, compreensíveis e associadas a consequências de baixo risco. (Peixoto et al., 2025 (#ref-peixoto-2025)).

A diferença entre estes níveis de participação torna-se mais clara quando se consideram três domínios de personalização que os estudos analisados abordam de forma diferenciada. O primeiro domínio diz respeito à geometria do encaixe e ao ajustamento biomecânico, predominando aqui uma lógica clínica. Neste caso, a pessoa pode fornecer feedback sobre conforto, tolerância ou preferência, mas a decisão permanece centrada no interveniente com competência técnica e responsabilidade pela validação. O segundo domínio corresponde à personalização do controlo e à afinação de sistemas interativos, nos quais a autoridade do utilizador tende a aumentar, uma vez que a sensação de controlo, a carga cognitiva e a adequação do comportamento do sistema em uso dependem da sua avaliação direta. O terceiro domínio relaciona-se com a personalização estética e identitária, em que a autonomia do utilizador pode ser mais ampla, dado que o risco clínico e biomecânico é menor e o critério de adequação depende mais diretamente da sua perceção.

A coexistência destes perfis e domínios justifica a adoção de permissões diferenciadas e de uma experiência graduada por papéis. O sistema não distribui o mesmo poder de edição a todos os agentes, pois isso reduziria a segurança, a coerência e a legibilidade do processo. Em vez disso, estrutura diferentes níveis de acesso, permitindo que determinadas ações sejam reservadas a perfis técnicos, enquanto outras se mantêm acessíveis ao utilizador que acompanha a sua configuração. Esta diferenciação não deve ser entendida como uma limitação arbitrária, mas como uma decisão de desenho que procura equilibrar autonomia, segurança e responsabilidade. Os estudos recentes sobre próteses inteligentes e interfaces configuráveis reforçam esta leitura, ao defenderem modelos de controlo nos quais os parâmetros críticos permanecem sob supervisão profissional, enquanto ajustes mais delimitados podem ser acessíveis ao utilizador final (Bai et al., 2024 (#ref-bai-2024); Quintero et al., 2018 (#ref-quintero-2018)).

A Figura 7.1 evidencia a importância de analisar a utilização concreta do dispositivo, para além da sua configuração digital. A avaliação com utilizadores permite identificar problemas relacionados com o ajuste ao corpo, o modo de ativação, o conforto e a adequação funcional, aspetos que dificilmente são detetados de forma suficiente apenas através do modelo digital. Para esta investigação, a imagem constitui um ponto de referência metodológico: embora a plataforma possa tornar o processo mais claro e configurável, a validação futura continua a depender da observação do uso em contexto real (Silva et al., 2018 (#ref-silva-alcara-2018)).

![](projecto-completo_media/image19.png)

Figura 7.1 — Teste de uma prótese impressa em 3D com utilizador em contexto aplicado.

Fonte original: Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

Do ponto de vista da experiência global, a plataforma deve ser entendida como um espaço de colaboração assimétrica. Neste enquadramento, o designer ou técnico dispõe de uma ferramenta que acelera iterações, estrutura a exploração paramétrica e apoia decisões de maior responsabilidade, enquanto o utilizador final obtém maior transparência, compreensão do processo e possibilidade de acompanhamento. O sistema passa, assim, a articular de forma mais clara o conhecimento especializado e a necessidade individual. A utilização da plataforma deve ser entendida, por isso, como uma forma de organizar a intervenção dos diferentes participantes no processo de personalização, articulando decisões técnicas, acompanhamento pelo utilizador e mediação pela interface. Esta leitura é consistente com abordagens human-in-the-loop, nas quais as preferências do utilizador, o ajustamento algorítmico e a supervisão profissional coexistem de forma hierárquica e não mutuamente exclusiva, ao mesmo tempo que a literatura mais ampla sobre fabrico digital em próteses continua a assinalar lacunas de formação, validação longitudinal e comparação sistemática entre workflows (Alili et al., 2023 (#ref-alili-2023); Oldfrey et al., 2024 (#ref-oldfrey-2024)). A distribuição diferenciada de acesso, interpretação e decisão conduz, assim, à questão seguinte: compreender de que modo a plataforma medeia o processo de design, para além de definir quem participa na sua utilização.

### 7.3 Mediação do processo de design e reflexão crítica

O contributo mais relevante da interface não reside apenas em permitir editar parâmetros, mas também em mediar o próprio processo de design. A plataforma introduz uma camada intermédia entre o modelo algorítmico, a decisão técnica e a interpretação do utilizador, reorganizando o desenvolvimento da prótese como uma sequência de interações assistidas. Esta mediação é importante porque reduz a dependência de manipulação direta do código e porque explicita que a personalização não é um ato instantâneo: trata-se de uma dinâmica iterativa de leitura de dados, proposta de configuração, avaliação visual, revisão crítica e eventual exportação para fabrico. Os estudos analisados reforçam que esta dimensão processual é parte central do modo como sistemas digitais desta natureza distribuem trabalho, autoridade e visibilidade entre diferentes intervenientes. A plataforma atua, assim, como uma infraestrutura de mediação, organizando as condições em que determinadas decisões são formuladas, avaliadas e realizadas no processo de design.

Neste sentido, a interface assume uma dimensão simultaneamente operacional e epistemológica, ao influenciar a forma como o problema é compreendido, como as alternativas são exploradas e como as decisões são justificadas.

Ao disponibilizar parâmetros editáveis, visualização tridimensional, sugestões assistidas por IA e gestão de versões, a plataforma contribui para estruturar o trabalho de projeto e para documentar a evolução das decisões tomadas ao longo do processo. Contudo, essa mesma estrutura também estabelece limites: o utilizador explora o espaço de soluções que o modelo e a interface permitem. A mediação digital amplia a capacidade de ação, mas também define os limites dentro dos quais a personalização pode ocorrer. Os estudos analisados sugerem que as plataformas mais relevantes neste domínio recorrem a mecanismos concretos de mediação, como o controlo diferenciado de permissões, a exposição seletiva de variáveis, os pontos de partida algorítmicos, a visualização orientada pelo problema e a supervisão integrada na própria interface.

A articulação entre maior capacidade de intervenção e delimitação do campo de decisão torna-se particularmente visível em sistemas que distinguem, de forma deliberada, os parâmetros acessíveis ao utilizador daqueles que permanecem reservados a profissionais ou a rotinas automáticas de ajuste. (Bai et al., 2024 (#ref-bai-2024); Alili et al., 2023 (#ref-alili-2023)).

Uma implicação desta leitura é que a plataforma medeia tanto quem utiliza o sistema como aquilo que se torna visível no processo. A visualização tridimensional, os indicadores de estado, os limites paramétricos e os mecanismos de feedback participam ativamente na forma como o problema é compreendido, interpretado e avaliado.

Ao tornar certas relações mais visíveis e outras menos acessíveis, a interface produz uma forma específica de legibilidade do processo de personalização. O mesmo se aplica aos mecanismos de comparação e revisão: quando o sistema oferece variantes, propõe valores iniciais ou assinala incongruências, está a intervir na forma como as alternativas são construídas antes mesmo de serem escolhidas.

Nesta perspetiva, a mediação digital participa na forma como as decisões de projeto são preparadas, avaliadas e justificadas. Esta observação conduz a uma reflexão crítica sobre o papel da plataforma no próprio processo de design.

Uma interface bem desenhada pode criar a sensação de evidência ou de neutralidade em decisões que continuam condicionadas por critérios de projeto, pressupostos técnicos e escolhas interpretativas. O facto de um parâmetro ser apresentado como controlo disponível, ou de uma sugestão surgir com aparência de plausibilidade técnica, não significa que a solução esteja validada ou que represente a melhor opção em todos os contextos. A mediação da interface deve, por isso, ser avaliada não apenas pela sua eficiência, mas também pela forma como torna visíveis as dependências, as incertezas e as responsabilidades envolvidas no processo. A literatura analisada reforça esta cautela: resultados positivos de usabilidade ou de rapidez de afinação não eliminam a necessidade de definir quem decide, quais parâmetros podem ser alterados, quais decisões ficam pré-estruturadas pelo sistema e sob quais condições essas alterações são consideradas seguras ou adequadas (Peixoto et al., 2025 (#ref-peixoto-2025); Quintero et al., 2018 (#ref-quintero-2018); Bai et al., 2024 (#ref-bai-2024)).

Uma interface bem desenhada pode criar a sensação de evidência ou de neutralidade em decisões que continuam condicionadas por critérios de projeto, pressupostos técnicos e escolhas interpretativas.

A mediação do processo de design preserva a responsabilidade pelas decisões de projeto e a necessidade de validação técnica, reorganizando ambas num ambiente digital mais controlado e explícito.

A plataforma distribui a capacidade de intervenção de forma diferenciada: concentra certas decisões em intervenientes tecnicamente qualificados, abre outras à participação informada do utilizador e enquadra outras através de sugestões produzidas por IA.

É precisamente nessa articulação entre interface, lógica paramétrica, sugestão assistida, visibilidade seletiva e responsabilidade crítica que reside o valor metodológico deste sistema enquanto contributo para o design de próteses personalizadas.

## Capítulo 8 — Avaliação e Discussão

### 8.1 Estratégia e critérios de avaliação

A avaliação do sistema foi organizada em torno de três níveis complementares: coerência técnica do modelo paramétrico, funcionamento da plataforma digital e plausibilidade das sugestões assistidas por IA.

Esta separação demonstrou-se necessária pois o projeto combina componentes de natureza distinta.

Um modelo OpenSCAD pode ser parametricamente consistente e, ainda assim, a interface pode não tornar essa consistência compreensível; do mesmo modo, uma sugestão de IA pode ser plausível como ponto de partida e continuar insuficiente como validação final da prótese. Os critérios usados procuram avaliar o encadeamento entre dados, parâmetros, renderização, exportação e revisão humana, em vez de tratar qualquer componente como solução autónoma.

No plano antropométrico, a avaliação concentrou-se em invariantes: conformidade com o esquema de parâmetros, respeito pelos limites mínimos e máximos, proporcionalidade entre dedos, adequação etária, coerência com intervalos adultos e lateralidade correta em casos de amputação unilateral.
Estes critérios foram escolhidos porque são verificáveis dentro do sistema e correspondem a riscos diretamente relacionados com a personalização inicial.

Estas validações incidem sobre a coerência preliminar do processo, permitindo verificar se a cadeia entre descrição livre, sugestão paramétrica e modelo renderizado preserva condições mínimas de plausibilidade antes da preparação para fabrico. A avaliação de conforto, desempenho funcional em uso e segurança clínica permanece dependente de testes posteriores com utilizadores e validação especializada.

A avaliação geométrica prolongou estes critérios até à etapa de exportação do modelo para fabrico. Para isso, foram executados fluxos de ponta a ponta com a interface real, incluindo autenticação, introdução da descrição do paciente, chamada ao serviço de IA, aplicação dos valores sugeridos, renderização por OpenSCAD/WebAssembly, exportação em STL e medição das malhas resultantes.

Esta etapa foi relevante porque a correção dos valores numéricos sugeridos não garante, por si só, que a geometria final responda de forma coerente aos parâmetros aplicados. A medição das peças exportadas permitiu verificar se as relações paramétricas definidas se preservavam desde a sugestão inicial até ao modelo gerado.

A validação foi depois prolongada para prototipagem física. Com base nos resultados dos testes de perfil, foram selecionadas configurações representativas dos cenários avaliados, incluindo perfis de mão pequena, perfil adulto feminino e perfil adulto masculino. Estas geometrias foram exportadas em STL/3MF, preparadas em ambiente de fatiamento e impressas em PLA e PETG. A utilização dos dois materiais teve uma função comparativa: o PLA permitiu uma verificação rápida, estável e económica da geometria, enquanto o PETG permitiu observar a resposta de um material mais resistente e menos frágil em componentes sujeitos a manipulação, encaixe e montagem preliminar.

A validação física seguiu cinco verificações principais: compatibilidade do ficheiro exportado com o fatiamento, ausência de falhas críticas de malha ou escala, conclusão da impressão sem defeitos impeditivos, inspeção visual e dimensional das zonas críticas e, quando aplicável, teste de encaixe ou montagem entre componentes. Esta etapa não teve como objetivo demonstrar eficácia clínica, conforto de uso ou durabilidade prolongada; o seu objetivo foi confirmar que os resultados dos perfis testados podiam atravessar a cadeia completa perfil -> parâmetros -> OpenSCAD/WebAssembly -> STL/3MF -> impressão 3D, mantendo coerência geométrica e viabilidade produtiva.

A Figura 8.1 apresenta um precedente de avaliação funcional baseado em tarefas quotidianas de membro superior. Embora o presente trabalho não realize validação clínica nem testes com utilizadores reais, este tipo de protocolo ajuda a enquadrar o horizonte de avaliação futura: depois da coerência paramétrica e geométrica, será necessário observar desempenho em tarefas, facilidade de uso e adequação funcional em contexto real (Romero et al., 2025 (#ref-romero-2025)).

![](projecto-completo_media/image20.png)

Figura 8.1 — Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior.

Fonte original: Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475

### 8.2 Validação antropométrica das sugestões de IA

O primeiro conjunto experimental incidiu sobre cinco perfis antropométricos simulados, construídos a partir de indicadores populacionais indiretos, incluindo idade, sexo, altura, peso, país, comprimento do braço e constituição física. Como estes perfis não incluíam medições diretas da mão, a avaliação centrou-se na capacidade do sistema para produzir sugestões paramétricas plausíveis a partir de informação contextual.

Este cenário assume especial relevância para a acessibilidade do sistema, uma vez que representa o caso de um utilizador capaz de descrever a pessoa através de informação contextual, sem domínio dos procedimentos específicos de medição antropométrica.

Nas cinco situações, a IA produziu JSON válido, usou apenas parâmetros existentes, respeitou os limites declarados do modelo e manteve a ordenação anatómica esperada entre os dedos.

Tabela 8.1 — Entradas/prompt utilizadas para criação dos perfis de validação antropométrica por IA

| Conjunto experimental | Tipo de perfil criado | Descrição usada como entrada | Finalidade da validação |

| --- | --- | --- | --- |

| Ensaio 1 — indicadores populacionais indiretos | Adulto masculino com dados demográficos e regionais | man, 28 years old, 82 kg, 180 cm height, Brazil, arm length 70 cm | Testar a inferência paramétrica sem medições diretas da mão |

| Ensaio 1 — indicadores populacionais indiretos | Criança do sexo feminino, com estrutura corporal pequena | girl, 10 years old, 32 kg, 138 cm height, Japan, small frame | Verificar o ajuste à idade e a redução das dimensões e dos componentes mecânicos |

| Ensaio 1 — indicadores populacionais indiretos | Mulher idosa com dados demográficos e regionais | woman, 65 years old, 68 kg, 160 cm height, Nigeria, arm length 62 cm | Avaliar a plausibilidade dos parâmetros num perfil adulto feminino e sénior |

| Ensaio 1 — indicadores populacionais indiretos | Adulto masculino com indicação qualitativa de mãos largas | man, 50 years old, 95 kg, 175 cm height, Germany, broad hands, arm length 66 cm | Verificar a resposta do sistema a uma característica anatómica descrita qualitativamente |

| Ensaio 1 — indicadores populacionais indiretos | Adolescente masculino alto e magro | teenage boy, 15 years old, 60 kg, 168 cm height, India, slim build, arm length 67 cm | Testar a fronteira entre perfil pediátrico e dimensões próximas de adulto |

| Ensaio 2 — amputação unilateral | Entrada completa com medições da mão intacta | Medições completas da mão esquerda intacta: palma 84 mm; indicador 72 mm; médio 78 mm; anelar 75 mm; mínimo 58 mm; polegar 64 mm; prótese necessária para a mão direita | Confirmar a preservação dos valores fornecidos e a geração contralateral |

| Ensaio 2 — amputação unilateral | Entrada parcial com dados demográficos e uma medição direta | Homem, 40 anos; mão direita intacta; largura da palma 90 mm; prótese necessária para a mão esquerda | Confirmar a manutenção da medida fornecida e a estimativa proporcional dos campos em falta |

| Ensaio 2 — amputação unilateral | Entrada apenas demográfica | Mulher, 30 anos, asiática oriental, 158 cm; prótese necessária para a mão direita | Verificar a adaptação do sistema quando não existem medições diretas da mão |

Fonte: elaboração própria a partir dos prompts registados no protocolo de validação antropométrica assistida por IA (docs/aianthropometricvalidation.md) e nos metadados de execução dos ensaios (docs/-ai-sim/run-metadata.json). A coluna apresenta a entrada de paciente usada no prompt; o prompt completo incluía ainda o schema vivo do modelo, os intervalos permitidos e a instrução de devolver apenas JSON válido.

A leitura dos resultados mostra uma adaptação coerente ao grau de detalhe da informação disponível. Nos perfis adultos, as dimensões sugeridas permaneceram dentro dos intervalos antropométricos usados como referência no sistema. No perfil infantil, as dimensões foram reduzidas de forma consistente e os parâmetros relativos aos componentes mecânicos das articulações flexíveis foram também ajustados, com base na informação presente nas legendas do esquema.

No perfil adolescente, um critério preliminar de verificação assinalou a dimensão da palma como potencialmente excessiva. Contudo, a análise posterior mostrou que o valor era compatível com um adolescente alto em fase intermédia da adolescência.

A falha, neste caso, estava na regra de teste demasiado rígida, e não na sugestão da IA.

O segundo conjunto experimental avaliou três cenários de amputação unilateral com riqueza variável de dados. No caso com medições completas da mão intacta, os valores fornecidos foram preservados literalmente e o lado sugerido correspondeu à mão amputada. No caso parcial, a largura da palma fornecida foi mantida e os restantes comprimentos foram estimados proporcionalmente. No caso apenas demográfico, a IA gerou um conjunto completo de medidas plausíveis. Estes ensaios iniciais sugeriam lateralidade correta, mas a avaliação UCD posterior revelou que pedidos explícitos de mão esquerda podiam ser sistematicamente convertidos em mão direita. A correção subsequente retirou a lateralidade do espaço de decisão da IA e transferiu-a para um controlo determinístico da interface.

Tabela 8.2 — Síntese da validação antropométrica assistida por IA

| Eixo avaliado | Resultado observado | Interpretação |

| --- | --- | --- |

| Conformidade com o esquema | Respostas interpretáveis, campos previstos e valores dentro dos limites definidos | O esquema de parâmetros reduziu a ocorrência de sugestões inválidas |

| Proporcionalidade digital | Dedo médio mais longo, dedo mínimo mais curto e polegar inferior ao dedo médio | As principais relações anatómicas entre os dedos foram preservadas |

| Entradas completas | Medições fornecidas mantidas sem alteração | A IA preservou os valores diretamente declarados pelo utilizador |

| Entradas parciais | Campos em falta estimados a partir da medida fornecida | O sistema combinou dados explícitos com referências populacionais |

| Entradas apenas demográficas | Conjunto completo e plausível de parâmetros | O fluxo gerou um ponto de partida para utilizadores sem domínio técnico |

| Lateralidade | Correta nos cenários iniciais, mas inconsistente em pedidos explícitos de mão esquerda na avaliação centrada no utilizador | A lateralidade passou a ser controlada pela interface e excluída das sugestões da IA |

A repetição de perfis idênticos evidenciou a natureza estocástica da componente de IA. As diferenças observadas foram pequenas, tipicamente de poucos milímetros, e preservaram os invariantes anatómicos e os limites do modelo. Também se observou variação estrutural aceitável: em algumas execuções, certos parâmetros de hardware foram sugeridos explicitamente; noutras, foram omitidos e permaneceram nos valores correntes. A avaliação UCD alargou este teste a entradas vagas, comparativas, multilingues e sem medidas diretas, confirmando que o sistema manteve valores válidos e anatomicamente ordenados em descrições próximas das que um utilizador leigo poderia escrever. Esta variabilidade confirma que a avaliação deve privilegiar propriedades invariantes, taxas de aprovação e comportamento em cenários de baixo conhecimento, e não valores absolutos isolados.

### 8.3 Validação geométrica entre modelos

A validação geométrica testou se os valores sugeridos chegavam à malha exportada em três modelos ativos da plataforma: Flexy Beast, Paraglider Hand e UnLimbited Phoenix. Para cada modelo foram comparados um baseline por omissão e três perfis antropométricos simulados: criança, mulher adulta e homem adulto. Todas as execuções devolveram sugestões ancoradas em perfis populacionais e valores dentro dos intervalos declarados.

Tabela 8.3 — Modelos e mecanismos de escala avaliados

| Modelo | Entradas antropométricas principais | Mecanismo de escala | Implicação observada |

| --- | --- | --- | --- |

| Flexy Beast | Largura da palma e comprimentos dos cinco dedos | Escalas independentes para palma e dedos | Adequado a crianças e mãos pequenas |

| Paraglider Hand | Palma e dedos, com parâmetros adicionais de contexto | Escala geral da palma e ajustes por dedo | Adequado a adultos e a uma gama ampla de perfis |

| UnLimbited Phoenix | Largura da palma | Escala uniforme limitada por piso mínimo | Fiel ao modelo original, mas inadequado para mãos pequenas |

Nota: os rácios apresentados são adimensionais. Um valor de 1,000 corresponde à dimensão do baseline; valores inferiores indicam redução e valores superiores indicam aumento face ao modelo de referência.

Os resultados mostraram que o Flexy Beast e o Paraglider Hand respondem de forma semelhante aos mesmos perfis, reduzindo ou aumentando as dimensões da palma de modo aproximadamente linear. A criança produziu uma escala de cerca de 0,76 face ao baseline nos modelos escaláveis, a mulher adulta ficou próxima de 0,93 e o homem adulto ficou entre 1,15 e 1,16. No Phoenix, pelo contrário, o piso mínimo de escala impediu a redução abaixo de cerca de 82 mm de largura de palma, fazendo com que perfis pequenos fossem truncados para o tamanho mínimo suportado pelo próprio modelo.

Tabela 8.4 — Rácio adimensional da maior dimensão da palma exportada face ao baseline

| Perfil | Flexy Beast | Paraglider Hand | UnLimbited Phoenix |

| --- | --- | --- | --- |

| Baseline | 1,000 | 1,000 | 1,000 |

| Criança | 0,761 | 0,747 | 0,760 antes da correção; 1,000 após impor o piso |

| Mulher adulta | 0,932 | 0,928 | 1,000 |

| Homem adulto | 1,148 | 1,157 | 1,171 |

Esta validação revelou três fragilidades técnicas que não eram visíveis na análise numérica isolada. A primeira estava no mecanismo de correspondência populacional: a análise inicial de género e idade era demasiado frágil, e certas abreviaturas presentes no texto de entrada podiam ser interpretadas incorretamente, confundindo unidades de medida com indicação de sexo masculino.

A correção passou por uma análise mais robusta do texto de entrada, capaz de reconhecer termos em diferentes línguas, respeitar fronteiras de palavra e classificar de forma mais fiável os grupos etários.

A segunda fragilidade foi identificada no modelo Paraglider. Neste caso, a dimensão da palma da mão protésica não estava a responder corretamente aos valores sugeridos, porque permanecia associada a uma escala interna herdada da biblioteca original. A correção consistiu em aplicar novamente a escala no ponto do código responsável pela geração dessa geometria. A terceira fragilidade surgiu no modelo UnLimbited Phoenix, onde um parâmetro alternativo permitia ultrapassar o limite mínimo de escala definido para o modelo. A correção passou por aplicar esse mesmo limite também a esse percurso alternativo de geração.

Esta etapa confirmou que a validação das sugestões de IA deve prolongar-se para além da resposta em JSON, pois a geometria exportada e a sua materialização por impressão 3D podem revelar dependências internas, limites de escala, problemas de espessura, folgas insuficientes e heranças de código invisíveis na análise numérica. Evidenciou ainda que os modelos integrados não são intercambiáveis, uma vez que cada um responde de forma distinta aos mesmos perfis antropométricos: o Flexy Beast é mais adequado a mãos pequenas, o Paraglider oferece uma escala ampla para perfis adultos e o Phoenix preserva elevada fidelidade ao original, mas apenas dentro de uma gama dimensional mais restrita.

### 8.4 Discussão dos resultados face aos objetivos

Face aos objetivos da investigação, os resultados reforçam a pertinência de articular design paramétrico, dados antropométricos, interface web e IA numa plataforma única, desde que a IA permaneça enquadrada por regras explícitas e revisão humana. A contribuição não está em automatizar a conceção de uma prótese final, mas em estruturar um fluxo no qual informação incompleta pode ser convertida num ponto de partida  de dimensões plausíveis, editável, visualizável e passível de revisão crítica.

Esta capacidade responde diretamente ao problema de acessibilidade identificado no projeto: muitos utilizadores conseguem descrever idade, altura, constituição física ou lado amputado, mas não dominam a nomenclatura nem os procedimentos de medição necessários para parametrizar uma mão protésica.

A avaliação também delimita com clareza os limites do sistema. A variabilidade estocástica da IA impede tratar uma saída isolada como prescrição fixa; a ausência de uma referência clínica direta impede afirmar precisão individual; e a lateralidade revelou-se um parâmetro crítico que não deve ser delegado à inferência do modelo. A correção implementada resolve esse risco ao deslocar a decisão para a interface, mas exige ainda reforço de UX para tornar a escolha do lado suficientemente visível e obrigatória. Do mesmo modo, a validação geométrica e física demonstra que cada modelo transporta constrangimentos próprios: alguns aceitam escalas pequenas, outros impõem pisos mínimos ou preservam proporções globais herdadas do desenho original. A impressão em PLA e PETG confirmou a viabilidade de prototipagem das configurações selecionadas, mas também reforçou que a passagem para o objeto físico deve ser tratada como etapa de verificação material e não como prova clínica. Consequentemente, os resultados são promissores enquanto validação de coerência interna, acessibilidade paramétrica e viabilidade de prototipagem, mas permanecem preliminares enquanto validação protésica.

A principal conclusão metodológica é que a robustez do sistema depende menos da presença isolada da IA do que da qualidade das regras, limites e mecanismos de validação que enquadram a sua atuação. O esquema de parâmetros do modelo, os limites declarados, a filtragem dos campos devolvidos, a ancoragem em dados populacionais, a renderização por OpenSCAD/WebAssembly, a exportação em STL/3MF, a preparação para fatiamento e a impressão em PLA/PETG formam uma cadeia de verificações sucessivas.

Quando essa cadeia é respeitada, a IA contribui para reduzir a barreira inicial de configuração; quando qualquer elo fica implícito, surgem riscos como lateralidade inferida, parâmetros sem correspondência geométrica ou escalas incompatíveis com o modelo físico.

## Capítulo 9 — Conclusões e Trabalhos Futuros

### 9.1 Síntese dos principais contributos

A investigação desenvolveu e avaliou um sistema de design paramétrico assistido por IA para próteses personalizadas de membro superior, articulando modelação em OpenSCAD, renderização em ambiente web, gestão de parâmetros antropométricos, perfis populacionais e sugestões geradas a partir de linguagem natural. O contributo metodológico da investigação reside no desenvolvimento de uma infraestrutura de apoio à configuração protésica, capaz de tornar mais explícita, documentável e acessível a passagem entre dados do utilizador, parâmetros geométricos e geometria exportável, sem reivindicar validação clínica da prótese resultante.

O trabalho confirma que a personalização paramétrica é mais robusta quando assenta numa gramática comum de medidas, limites e relações geométricas. A plataforma permitiu expor essa gramática numa interface utilizável, guardar configurações, renderizar modelos localmente e exportar ficheiros STL e 3MF.

A integração da IA acrescentou uma camada de apoio à decisão, capaz de transformar descrições incompletas em pontos de partida plausíveis, desde que as sugestões sejam enquadradas pelo esquema de parâmetros do modelo, pelos limites definidos e por validação posterior.

A validação realizada mostrou quatro resultados principais. Primeiro, as sugestões numéricas respeitaram os limites do modelo, preservaram proporções anatómicas e adaptaram-se de forma coerente à riqueza variável das entradas. Segundo, as medições diretamente fornecidas foram preservadas e os dados em falta foram estimados proporcionalmente.

Terceiro, a validação geométrica entre modelos demonstrou que a exportação em STL/3MF é indispensável para identificar constrangimentos que a resposta numérica não revela, como limites mínimos de escala, dependências herdadas do código original e diferenças efetivas entre modelos.

Quarto, a prototipagem física em PLA e PETG confirmou que as configurações selecionadas a partir dos testes de perfil podiam ser preparadas, fatiadas e impressas, permitindo verificar escala, integridade formal, zonas críticas e montagem preliminar. Esta etapa validou a viabilidade produtiva do fluxo, mas não constitui validação clínica ou biomecânica completa.

Quinto, a avaliação centrada no utilizador revelou que a acessibilidade paramétrica depende tanto da qualidade da inferência - entendida como o processo através do qual a IA transforma informação incompleta, indireta ou descritiva em sugestões paramétricas plausíveis - como das salvaguardas incorporadas na interface: entradas vagas e formuladas em diferentes línguas foram tratadas com robustez, mas a lateralidade, a adequação do modelo escolhido e a proveniência das estimativas exigem controlos explícitos para evitar confiança excessiva no resultado.

A mesma lógica sugere a possibilidade de extensão da arquitetura a outros segmentos corporais. A plataforma deixa de depender exclusivamente de pressupostos específicos da mão quando propriedades como lateralidade, tipo de membro e orientação antropométrica passam a ser declaradas no ficheiro de configuração do modelo.

Este passo não valida automaticamente a plataforma para dispositivos destinados ao pé, à perna ou ao braço, uma vez que essa extensão exigiria novos conjuntos de dados, novos mapeamentos antropométricos e validação geométrica específica. Ainda assim, demonstra que a estrutura técnica pode evoluir de um configurador de membros superiores e mãos para uma plataforma paramétrica organizada por tipo de membro, desde que cada modelo declare a sua lógica dimensional, os parâmetros relevantes e os respetivos limites de fabrico.

### 9.2 Contributos para o Design Industrial

O contributo principal reside na demonstração de um processo em que o artefacto, a interface e a lógica paramétrica funcionam como instrumentos de investigação. A prótese é aqui entendida como sistema configurável, no qual requisitos anatómicos, funcionais, produtivos e de utilização são traduzidos em parâmetros passíveis de análise crítica.

Esta abordagem reforça o papel do designer como mediador entre dados, tecnologia, fabrico e experiência humana.

A plataforma também contribui para uma leitura mais disciplinada da personalização. Em vez de associar personalização a liberdade ilimitada de escolha, o sistema mostra a importância de definir que parâmetros são editáveis, quais permanecem sob controlo técnico, que intervalos são aceitáveis e que modelos são adequados a diferentes perfis. Esta contenção é particularmente relevante em dispositivos de apoio, nos quais a acessibilidade da configuração deve ser equilibrada com responsabilidade, segurança e coerência funcional.

A integração da IA reforça essa mediação, mas não a substitui. O modelo de linguagem é útil quando reduz a barreira inicial de parametrização e apoia o utilizador não especialista; torna-se frágil quando a sua saída é interpretada como decisão autónoma. A contribuição projetual está, por isso, em enquadrar a IA como componente human-in-the-loop, articulada com regras explícitas, dados antropométricos, visualização, exportação e revisão técnica.

### 9.3 Limitações e perspetivas de desenvolvimento futuro

O alcance das conclusões deve ser entendido a partir do caráter metodológico e técnico da validação realizada. A avaliação incidiu sobre perfis simulados, dados secundários e critérios internos de plausibilidade, deixando para investigação futura os testes com utilizadores reais, as avaliações clínicas, as medições diretas de conforto, os ensaios funcionais prolongados e a validação biomecânica completa. Assim, os resultados sustentam a validação do fluxo de personalização, sem constituírem demonstração de eficácia protésica em contexto de uso.

A componente de IA exige desenvolvimento adicional, mesmo após a correção determinística da lateralidade. A saída deve ser validada por esquema JSON no servidor, prevendo-se a repetição automática do pedido sempre que a resposta se afaste da estrutura definida.

A variabilidade estocástica deve ser quantificada com múltiplas extrações por perfil, reportando médias, dispersão e taxas de aprovação dos invariantes. A comparação com bases de dados antropométricas ou medições reais permitiria passar da plausibilidade para uma estimativa mais rigorosa de erro. Do ponto de vista da experiência de utilização, a plataforma deve também mostrar a proveniência das estimativas, a incerteza associada ao grupo populacional usado e avisos explícitos quando o modelo escolhido não consegue representar a dimensão estimada do utilizador.

Do ponto de vista geométrico e produtivo, a validação física realizada em PLA e PETG deve ser aprofundada através de ensaios mais sistemáticos de montagem, tolerâncias, resistência, desgaste, repetibilidade de impressão e adequação ao uso. Também será necessário clarificar a seleção de modelos segundo faixas dimensionais: modelos como o Flexy Beast são mais adequados a mãos pequenas, enquanto modelos com piso mínimo, como o Phoenix, exigem restrições claras na interface para evitar expectativas incorretas. A plataforma deve, portanto, evoluir de um configurador que aceita parâmetros para um sistema que também orienta a escolha do modelo adequado ao perfil, ao material e ao objetivo de fabrico.

Por fim, a investigação abre espaço para estudos com utilizadores, técnicos e designers, avaliando não apenas a geometria exportada, mas também a inteligibilidade da interface, a confiança nas sugestões, a distribuição de responsabilidade e a utilidade real do fluxo em contextos de prototipagem. A continuidade do projeto deve manter a distinção que estruturou esta dissertação: a IA pode ampliar a acessibilidade e a velocidade de exploração, mas a qualidade de uma prótese personalizada continua a depender da articulação entre design, dados, fabrico, validação técnica e experiência humana.

## Bibliografia

<a id="ref-alili-2023"></a> Alili, A., Nalam, V., Li, M., Liu, M., Feng, J., Si, J., & Huang, H. (2023). A novel framework to facilitate user preferred tuning for a robotic knee prosthesis. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31, 895-903. https://doi.org/10.1109/TNSRE.2023.3236217

<a id="ref-albin-2023"></a> Albin, T., & Molenbroek, J. F. M. (2023). Introduction to the special issue, anthropometry in design. https://repository.tudelft.nl/file/Fileda5bfdc9-98bc-41d3-a402-553d5f0d0a63

<a id="ref-arrieta-2020"></a> Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82-115. https://doi.org/10.1016/j.inffus.2019.12.012

<a id="ref-astm-international-2024"></a> ASTM International. (2024). Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers. https://www.astm.org/f3661-24.html

<a id="ref-bai-2024"></a> Bai, X., Yuan, J., Liu, M., Huang, H., & Feng, J. (2024). Human factors considerations of interaction between wearers and intelligent lower-limb prostheses: A prospective discussion. Journal of NeuroEngineering and Rehabilitation, 21, 187. https://doi.org/10.1186/s12984-024-01475-x

<a id="ref-bates-2020"></a> Bates, T., Fergason, J., & Pierrie, S. N. (2020). Technological advances in prosthesis design and rehabilitation following upper extremity limb loss. https://www.semanticscholar.org/paper/905056ffa9fa963e8df8b974d90b94c05a5f7e29

<a id="ref-bradtmiller-2022"></a> Bradtmiller, B. (2022). Design for all, design for disabled: How important is anthropometry? https://researchonline.jcu.edu.au/76898/

<a id="ref-chainando-2025"></a> Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517

<a id="ref-kaygan-2025"></a> Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. https://doi.org/10.1080/14606925.2024.2420152

<a id="ref-kellam-2019"></a> Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

<a id="ref-colombo-2015"></a> Colombo, G., Facoetti, G., Rizzi, C., & Vitali, A. (2015). Low cost hand-tracking devices to design customized medical devices. Interacción. https://doi.org/10.1007/978-3-319-21067-436

<a id="ref-da-silveira-romero-2025"></a> da Silveira Romero, R. C., Costa, K. A., Reis, P. H. R. G., & Vimieiro, C. B. S. (2025). Development of parametric prostheses for different levels of human hand amputations manufactured through additive manufacturing. Applied Sciences, 15, 4467. https://doi.org/10.3390/app15084467

<a id="ref-gu-2024"></a> Gu, Y., He, L., Zeng, H., Li, J., Zhang, N., Zhang, X., & Liu, T. (2024). A data-driven design framework for structural optimization to enhance wearing adaptability of prosthetic hands. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 32. https://doi.org/10.1109/TNSRE.2024.3430070

<a id="ref-engdahl-2024"></a> Engdahl, S., Gonzalez, M. A., Lee, C., & Gates, D. H. (2024). Perspectives on the comparative benefits of body-powered and myoelectric upper limb prostheses. https://jneuroengrehab.biomedcentral.com/counter/pdf/10.1186/s12984-024-01436-4

<a id="ref-elbreki-2022"></a> Elbreki, A. M., Alshari, K., Ramdan, S., & Rajab, Z. (2022). Practical design of an upper prosthetic limb using three dimensional printer with an artificial intelligence based controller. In 2022 International Conference on Engineering & MIS (ICEMIS). IEEE. https://doi.org/10.1109/ICEMIS56295.2022.9914291

<a id="ref-fink-2023"></a> Fink, C., & Diamond, Y. (2023). Prosthesis options and management in upper extremity amputation. https://www.semanticscholar.org/paper/3532a770446eb6144ef25a6b0162d1f98b61e0ff

<a id="ref-ibrahim-2024"></a> Ibrahim, M. T., Azman, H., Adzahar, N. S. I. A., Ismail, M. A., & Shaharuddin, S. (2024). Techniques for measuring the fluctuation of residual lower limb volume in clinical practices: A systematic review of the past four decades. Applied Sciences, 14(6), 2594. https://www.mdpi.com/2076-3417/14/6/2594/pdf?version=1710932396

<a id="ref-kandikjan-2022"></a> Kandikjan, T., Djokikj, J., Mircheski, I., & Angeleska, E. (2022). Integrating parametric design and additive manufacturing knowledge in industrial design education. https://www.semanticscholar.org/paper/7d28a8c124ef0a3599dd937791a3f3e093775ac0

<a id="ref-kannenberg-2024"></a> Kannenberg, A., Buis, A. W. P., Sengeh, D. M., & Worsley, P. R. (2024). Insights into the spectrum of transtibial prosthetic socket design from expert clinicians and their digital records. Frontiers in Rehabilitation Sciences, 5. https://doi.org/10.3389/fresc.2024.1354069

<a id="ref-lei-2016"></a> Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. https://dr.ntu.edu.sg/bitstream/10356/83735/1/An%20additive%20manufacturing%20process%20model%20for%20product%20family%20design.pdf

<a id="ref-lindell-2021"></a> Lindell, E., Tingsvik, H., Guo, L., & Peterson, J. (2021). 3D body scan as anthropometric tool for individualized prosthetic socks. https://sciendo.com/pdf/10.2478/aut-2021-0007

<a id="ref-lim-d-georgiou-t-bhardwaj"></a> Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. https://doi.org/10.1115/DETC2018-85645

<a id="ref-ozdemir-2022"></a> Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0F2B66A61E2CE6410F9D1F335244EB9C/S2053470122000038a.pdf/div-class-title-design-methodology-for-mass-personalisation-enabled-by-digital-manufacturing-div.pdf

<a id="ref-peixoto-2025"></a> Peixoto, S., Martins, N., Miranda, D., Matos, D., & Carvalho, V. (2025). The design process in the development of an online platform for personalizing wearable prostheses: A preliminary approach. Designs, 9(2), 39. https://doi.org/10.3390/designs9020039

<a id="ref-parlamento-europeu-2017"></a> Parlamento Europeu, & Conselho da União Europeia. (2017). Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical devices. https://eur-lex.europa.eu/eli/reg/2017/745/oj

<a id="ref-chapman-2025"></a> Chapman, K., Allen, C., & Kendall, E. (2025). Methods for co-designing health communication initiatives with people with disability: A scoping review. Health Communication. https://doi.org/10.1080/10810730.2025.2462679

<a id="ref-clarkson-2010"></a> Clarkson, J., & Coleman, R. (2010). Inclusive design. Design Studies. https://doi.org/10.1080/09544821003693689

<a id="ref-chtioui-2023"></a> Chtioui, N., Gaha, R., & Benamara, A. (2023). Design for additive manufacturing: Review and framework proposal. https://sei.ardascience.com/index.php/journal/article/download/185/169

<a id="ref-fisher-2020"></a> Fisher, M., & Johansen, E. (2020). Human-centered design for medical devices and diagnostics in global health. https://www.semanticscholar.org/paper/89c3c6bd56f4d0b54f5da3e3c96f18e815d9f5d4

<a id="ref-millet-2018"></a> Millet, A., Akle, A. A., & Legardeur, J. (2018). Human centred criteria for healthcare design. https://www.semanticscholar.org/paper/267b655f123f4f167f1f9e7e6c8a1f17f73a73d0

<a id="ref-oldfrey-2024"></a> Oldfrey, B., Ramirez, D. Z. M., Miodownik, M., et al. (2024). A scoping review of digital fabrication techniques applied to prosthetics and orthotics: Part 1 of 2—Prosthetics. Prosthetics and Orthotics International. https://doi.org/10.1097/PXR.0000000000000351

<a id="ref-quintero-2018"></a> Quintero, D., Reznick, E., Lambert, D. J., Rezazadeh, S., Gray, L., & Gregg, R. D. (2018). Intuitive clinician control interface for a powered knee-ankle prosthesis: A case study. IEEE Journal of Translational Engineering in Health and Medicine, 6, 2600209. https://doi.org/10.1109/JTEHM.2018.2880199

<a id="ref-resnik-2010"></a> Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. https://www.semanticscholar.org/paper/71e1fef52dde69cbcea4f62c709f7c6689f9463d

<a id="ref-romero-2025"></a> Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475

<a id="ref-segura-2024"></a> Segura, D., Romero, E., Abarca, V. E., & Elías, D. A. (2024). Upper limb prostheses by the level of amputation: A systematic review. Prosthesis, 6(2), 22. https://www.mdpi.com/2673-1592/6/2/22/pdf?version=1710818539

<a id="ref-smail-2020"></a> Smail, L. C., Neal, C., Wilkins, C., & Packham, T. (2020). Comfort and function remain key factors in upper limb prosthetic abandonment: Findings of a scoping review. https://www.semanticscholar.org/paper/b5eb3fd2414ebedaa5d2283451268fafa2db0a81

<a id="ref-soyer-2016"></a> Soyer, K., Unver, B., Tamer, S., & Ulger, O. (2016). The importance of rehabilitation concerning upper extremity amputees: A systematic review. https://pjms.com.pk/index.php/pjms/article/view/9922/4660

<a id="ref-saldarriaga-2024"></a> Saldarriaga, A. M., Romero, E., Abarca, V. E., & Elias, D. A. (2024). A parametric design approach for affordable customized 3D socket for transradial upper limb prostheses. In 2024 10th International Conference on Control, Decision and Information Technologies (CoDIT). https://doi.org/10.1109/CoDIT62066.2024.10708382

<a id="ref-shah-2006"></a> Shah, S., & Robinson, I. (2006). User involvement in healthcare technology development and assessment: Structured literature review. https://www.semanticscholar.org/paper/299d5b2c1d65791cc4c9f2db76edf20f479adcbc

<a id="ref-silva-alcara-2018"></a> Silva, L. A. da, Medola, F. O., Rodrigues, O. V., Rodrigues, A. C. T., & Sandnes, F. E. (2018). Interdisciplinary-based development of user-friendly customized 3D printed upper limb prosthesis. Comunicação em conferência.

<a id="ref-silva-2024"></a> Silva, R., Silva, B., Fernandes, C., Morouco, P., Alves, N., & Veloso, A. (2024). A review on 3D scanners studies for producing customized orthoses. Sensors, 24(5), 1373. https://pmc.ncbi.nlm.nih.gov/articles/PMC10935386/pdf/sensors-24-01373.pdf

<a id="ref-story-2006"></a> Story, M. (2006). Applying the principles of universal design to medical devices. https://www.semanticscholar.org/paper/d0d84425d517331607c9120290ed26d1bf2e1862

<a id="ref-stralen-2018"></a> Stralen, M. V. (2018). Mass customization: A critical perspective on parametric design, digital fabrication and design democratization. https://www.semanticscholar.org/paper/a18f2c4d248e791d2a9b84f3cab268d5a377cc10

<a id="ref-squibb-2024"></a> Squibb, C., Madigan, M. L., & Philen, M. K. (2024). A high precision laser scanning system for measuring shape and volume of transtibial amputee residual limbs: Design and validation. PLOS ONE, 19(5). https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0301619&type=printable

<a id="ref-sunderland-2024"></a> Sunderland, F., Willerth, S., Silver-Thorn, B., & Dickinson, A. (2024). OpenLimbTT, a transtibial residual limb shape model for prosthetics simulation and design: Creating a statistical anatomic model using sparse data. medRxiv. https://www.medrxiv.org/content/medrxiv/early/2024/11/30/2024.11.27.24317622.full.pdf

<a id="ref-cklacandr-2022"></a> Çıklaçandır, S., Yilmaz, M., Ozmert, O. S., Şahin, A. M., & Mihçin, S. (2022). Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design. https://www.semanticscholar.org/paper/a24aab5d4434a01eeeda73c8a62f921580ceba54

<a id="ref-white-2022"></a> White, J., & Mosca, E. I. (2022). Developing innovative solutions for universal design in healthcare and other sectors. https://www.semanticscholar.org/paper/df2bb0d53af547bd89b2c716933c2a544bf422b1

<a id="ref-wiberg-2019"></a> Wiberg, A., Persson, J., & Ölvander, J. (2019). Design for additive manufacturing: A review of available design methods and software. https://www.semanticscholar.org/paper/e03bf769f344512519f1005baa1d6b83fe4fc8ed

<a id="ref-wilke-2020"></a> Wilke, H., Badke-Schaub, P., & Thoring, K. (2020). The healthcare design dilemma: Perils of a technology-driven design process for medical products. https://www.semanticscholar.org/paper/078781d9389d4618fc1b5db9347ab68ca7ef46d9

<a id="ref-walters-2025"></a> Walters, S., Seminati, E., Metcalfe, B., Bailey, N. Y., & Pegg, E. C. (2025). Demystifying upper limb hybrid prostheses: A scoping review. https://www.semanticscholar.org/paper/d659aff9bb182a3c92377571973e6e077a3b1838

<a id="ref-yao-2016"></a> Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive manufactured variable platforms in product families. https://www.semanticscholar.org/paper/f7bc9dc2a80714c18ac068f45b99408b0f4fe65e

<a id="ref-young-2023"></a> Young, P. R., Hebert, J. S., Marasco, P., Carey, J., & Schofield, J. S. (2023). Advances in the measurement of prosthetic socket interface mechanics: A review of technology, techniques, and a 20-year update. https://www.tandfonline.com/doi/pdf/10.1080/17434440.2023.2244418?needAccess=true&role=button

<a id="ref-ao-2025"></a> Ao, Y., Li, S., & Duan, H. (2025). Artificial intelligence-aided design (AIAD) for structures and engineering: A state-of-the-art review and future perspectives. Archives of Computational Methods in Engineering. https://link.springer.com/content/pdf/10.1007/s11831-025-10264-1.pdf

<a id="ref-burnap-2019"></a> Burnap, A., Hauser, J., & Timoshenko, A. (2019). Design and evaluation of product aesthetics: A human-machine hybrid approach. https://www.semanticscholar.org/paper/7a7994f2de74a61cbdeb3c230d1ee343a0d5e783

<a id="ref-choudhury-2025"></a> Choudhury, M. M., Eisenbart, B., & Kuys, B. (2025). Artificial intelligence (AI) in the design process: A review and analysis on generative AI perspectives. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/36E8736EEB55F0B38C2C9AB47EF381FE/S2732527X25100771a.pdf/div-class-title-artificial-intelligence-ai-in-the-design-process-a-review-and-analysis-on-generative-ai-perspectives-div.pdf

<a id="ref-figoli-2022"></a> Figoli, F. A., Mattioli, F., & Rampino, L. (2022). AI in design idea development: A workshop on creativity and human-AI collaboration. https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=2915&context=drs-conference-papers

<a id="ref-idris-2024"></a> Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, N. (2024). Exploring the integration of artificial intelligence in co-design framework for designer. https://ebpj.e-iph.co.uk/index.php/EBProceedings/article/download/6348/3640

<a id="ref-kadenhe-2025"></a> Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI co-design and co-creation: A review of emerging approaches, challenges, and future directions. https://www.semanticscholar.org/paper/61c04706b7af0be5be4b0d15f595d4ab41874d12

<a id="ref-khanolkar-2023"></a> Khanolkar, P., Vrolijk, A., & Olechowski, A. (2023). Mapping artificial intelligence-based methods to engineering design stages: A focused literature review. https://www.semanticscholar.org/paper/4d63443d45e1a7156c5972ef009ed07bb0650117

<a id="ref-krahe-2020"></a> Krahe, C., Bräunche, A., Jacob, A., Stricker, N., & Lanza, G. (2020). Deep learning for automated product design. https://www.semanticscholar.org/paper/a5b9b4f63805f2b1773bc8214b29e38dbac27975

<a id="ref-li-2021"></a> Li, X., Demirel, H., Goldstein, M., & Sha, Z. (2021). Exploring generative design thinking for engineering design and design education. https://peer.asee.org/38349.pdf

<a id="ref-menaka-2025"></a> Menaka, S., Raja, W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. https://ijamjournal.org/ijam/publication/index.php/ijam/article/download/341/311

<a id="ref-panchal-2019"></a> Panchal, J. H., Fuge, M., Liu, Y., Missoum, S., & Tucker, C. S. (2019). Special issue: Machine learning for engineering design. Journal of Mechanical Design. https://www.semanticscholar.org/paper/2c4f7ca9381db7debefe61d04da51f9e8e63d09d

<a id="ref-ramnath-2019"></a> Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. https://www.semanticscholar.org/paper/40a0b51e5b01234cec3e807158b26a284ea77e0f

<a id="ref-rezwana-2022"></a> Rezwana, J., & Maher, M. (2022). Understanding user perceptions, collaborative experience, and user engagement in different human-AI interaction designs for co-creative systems. https://arxiv.org/pdf/2204.13217

<a id="ref-saeidnia-2024"></a> Saeidnia, H. R., & Ausloos, M. (2024). Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework. https://www.semanticscholar.org/paper/e2b8a10036428046443e24dc33ec5306876afdbb

<a id="ref-verganti-2020"></a> Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). Innovation and design in the age of artificial intelligence. https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jpim.12523

<a id="ref-viros-i-martin-2021"></a> Virós-i-Martin, A., & Selva, D. (2021). A framework to study human-AI collaborative design space exploration. https://www.semanticscholar.org/paper/716be148371af443169531b0856ae07dfe400869

<a id="ref-wang-2024"></a> Wang, X., & Hu, B. (2024). Machine learning algorithms for improved product design user experience. https://www.semanticscholar.org/paper/717e7ad25dcafec12f01b6732773bdf9c5a49661

<a id="ref-yuksel-2023"></a> Yüksel, N., Börklü, H. R., Sezer, H. K., & Canyurt, O. (2023). Review of artificial intelligence applications in engineering design perspective. https://www.semanticscholar.org/paper/cd38b58edf6690459767097aca745a3806824236

<a id="ref-akasaka-2022"></a> Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488

<a id="ref-akyol-2021"></a> Akyol, P., Barker, T., Hall, R., Morrissey, K., McCarthy, J., & Mackley, K. L. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. https://www.semanticscholar.org/paper/ea18361f7564fb19db367899adb6295a07bfa05c

<a id="ref-cole-2011"></a> Cole, E. (2011). Patient-centered design: Interface personalization for individuals with brain injury.

<a id="ref-costabile-2007"></a> Costabile, M. F., Fogli, D., Lanzilotti, R., Marcante, A., Mussio, P., Provenza, L. P., & Piccinno, A. (2007). Meta-design to face co-evolution and communication gaps between users and designers.

<a id="ref-dechev-2023"></a> Dechev, N., Penner, A., Barlow, I., Vukovic, G., & Lalji, M. (2023). Accessible prosthetic arms: Victoria Hand Project and the impact of 3D printing.

<a id="ref-dexter-2013"></a> Dexter, M., Crooks, E., Davies, P., & Simm, W. (2013). Open design and cystic fibrosis: Enabling participation in the design process.

<a id="ref-fischer-2004"></a> Fischer, G., Giaccardi, E., Ye, Y., Sutcliffe, A. G., & Mehandjiev, N. (2004). Meta-design.

<a id="ref-fischer-2017"></a> Fischer, G., Fogli, D., & Piccinno, A. (2017). Revisiting and broadening the meta-design framework for end-user development.

<a id="ref-frangos-2016"></a> Frangos, P., Mierdel, S., & Koirala, S. (2016). Democratising design in scientific innovation: Application of an open value network to open source hardware design.

<a id="ref-franke-2002"></a> Franke, N., & von Hippel, E. (2002). Satisfying heterogeneous user needs via innovation toolkits: The case of Apache security software.

<a id="ref-govender-2020"></a> Govender, R., Abrahmsén-Alami, S., Larsson, A., Borde, A., Liljeblad, A., & Folestad, S. (2020). Independent tailoring of dose and drug release via a modularized product design concept for mass customization. Pharmaceutics.

<a id="ref-howard-2022"></a> Howard, D., Davies, L., Dwyer, A., & Williams, J. (2022). Assessing the use of co-design to produce bespoke assistive technology solutions within a current healthcare service: A service evaluation.

<a id="ref-hippel-2002"></a> Hippel, E. von, & Katz, R. (2002). Shifting innovation to users via toolkits. Management Science, 48(7).

<a id="ref-hussaini-2023"></a> Hussaini, A., Kyberd, P., Mulindwa, B., Ssekitoleko, R., Keeble, W., Kenney, L., & Howard, D. (2023). 3D printing in LMICs: Functional design for upper limb prosthetics in Uganda.

<a id="ref-kerr-2024"></a> Kerr, A., Del Din, S., Clarkson, P. J., & Rochester, L. (2024). A participatory model for cocreating accessible rehabilitation technology for stroke survivors: User-centered design approach.

<a id="ref-kuhl-2020"></a> Kuhl, M., Lutz, J., Krause, D., & Vielhaber, M. (2020). Design of personalized devices: The tradeoff between individual value and personalization workload. Applied Sciences.

<a id="ref-mikoajewski-2023"></a> Mikołajewski, D., Rojek, I., Kotlarz, P., Dorożyński, J., & Kopowski, J. (2023). Personalization of the 3D-printed upper limb exoskeleton design: Mechanical and IT aspects. Applied Sciences.

<a id="ref-peters-2023"></a> Peters, C., & Richter, P. (2023). Individualizing patient pathways through modularization: Design and evaluation of healthcare-specific modularization parameters.

<a id="ref-seregni-2021"></a> Seregni, F., Arlati, S., Colombo, V., Spoladore, D., Greci, L., Pedroli, E., Serino, S., Cipresso, P., Goulene, K., Stroulia, E., Rizzo, A., & Sacco, M. (2021). Virtual coaching for rehabilitation: The participatory design experience of the vCare Project.

<a id="ref-sims-2017"></a> Sims, T., Cranny, A., Metcalf, C., Chappell, P., & Donovan-Hall, M. (2017). Participatory design of pediatric upper limb prostheses: Qualitative methods and prototyping.

<a id="ref-thorsen-2023"></a> Thorsen, R., Hansen, A. H., & Nilsen, E. R. (2023). From patient to maker: A workflow including people with cerebral palsy in co-creating assistive devices using 3D printing technologies.

<a id="ref-zhu-2022"></a> Zhu, Z., & Zhong, R. Y. (2022). A digital twin enabled wearable device for customized healthcare.

<a id="ref-alluhydan-2023"></a> Alluhydan, A., Alsaadi, S., Almutairi, A., & Alharbi, A. (2023). Functionality and comfort design of lower-limb prosthetics: A review.

<a id="ref-anderson-2024"></a> Anderson, C. B., Stephens, A. R., Scully, A., Pasquina, P. F., & Highsmith, M. J. (2024). A narrative review of prosthesis design decision making after lower-limb amputation for developing shared decision-making resources.

<a id="ref-andrysek-2010"></a> Andrysek, J. (2010). Lower-limb prosthetic technologies in the developing world: A review of literature from 1994-2010.

<a id="ref-baldock-2023"></a> Baldock, C., Greaves, M., Chockalingam, N., & Kark, L. (2023). Adjustable prosthetic sockets: A systematic review of industrial and research design characteristics and their justifications.

<a id="ref-baumann-2023"></a> Baumann, C., & Maria, P. (2023). Improving access to prosthetic limbs in Germany: An explorative review.

<a id="ref-chadwell-2020"></a> Chadwell, A., Kenney, L., Thies, S., Galpin, A., & Head, J. (2020). Technology for monitoring everyday prosthesis use: A systematic review.

<a id="ref-cordella-2016"></a> Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users.

<a id="ref-dominguez-ruiz-2023"></a> Domínguez-Ruiz, M., Ráez-Ballesteros, E., & Castillo-Castañeda, E. (2023). Low limb prostheses and complex human prosthetic interaction: A systematic literature review.

<a id="ref-ghillebert-2019"></a> Ghillebert, J., Schoukens, J., & Vanderborght, B. (2019). Guidelines and recommendations to investigate the efficacy of a lower-limb prosthetic device: A systematic review.

<a id="ref-hafner-2016"></a> Hafner, B. J., & Sawers, A. B. (2016). Issues affecting the level of prosthetics research evidence: Secondary analysis of a systematic review.

<a id="ref-manz-2022"></a> Manz, S. M., Menges, M. M., Schaffernicht, E., Mattes, K., & Kannenberg, A. (2022). A review of user needs to inform the development of lower-limb prostheses.

<a id="ref-marinelli-2022"></a> Marinelli, M., Putrino, D., Stella, F., & Guglielmelli, E. (2022). Active upper limb prostheses: A review on current state and upcoming breakthroughs.

<a id="ref-richardson-2017"></a> Richardson, C., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review.

<a id="ref-samuelsson-2012"></a> Samuelsson, K. A. M., Töytäri, O., Salminen, A.-L., & Brandt, Å. (2012). Effects of lower limb prosthesis on activity, participation, and quality of life: A systematic review.

<a id="ref-walker-2019"></a> Walker, M., Paras, A., Boonstra, N., & Murrup-Stewart, C. (2019). Towards including end-users in the design of prosthetic hands: Ethical analysis of a survey of Australians with upper-limb difference.

<a id="ref-windrich-2016"></a> Windrich, M., Grimmer, M., Christ, O., Rinderknecht, S., & Beckerle, P. (2016). Active lower limb prosthetics: A systematic review of design issues and solutions.

<a id="ref-anacleto-filho-2023"></a> Anacleto Filho, P. C., da Silva, L., Mattos, D., Pombeiro, A., Castellucci, H. I., Colim, A., Carneiro, P., & Arezes, P. (2023). Establishing an anthropometric database: A case for the Portuguese working population. International Journal of Industrial Ergonomics, 97, 103473. https://doi.org/10.1016/j.ergon.2023.103473

<a id="ref-chatzioglou-2024"></a> Chatzioglou, G. N., Pinar, Y., & Govsa, F. (2024). Biometric analysis hand parameters in young adults for prosthetic hand and ergonomic product applications. Anatomy & Cell Biology, 57, 172-182. https://doi.org/10.5115/acb.23.310

<a id="ref-gordon-1989"></a> Gordon, C. C., Churchill, T., Clauser, C. E., Bradtmiller, B., McConville, J. T., Tebbetts, I., & Walker, R. A. (1989). Anthropometric survey of U.S. Army personnel: Methods and summary statistics 1988 (Technical Report NATICK/TR-89/044). U.S. Army Natick Research, Development and Engineering Center.

<a id="ref-gorski-2022"></a> Górski, F., Zawadzki, P., Wichniarek, R., Kuczko, W., Słupińska, S., & Żukowska, M. (2022). Automated design and rapid manufacturing of low-cost customized upper limb prostheses. Journal of Physics: Conference Series, 2198, 012040. https://doi.org/10.1088/1742-6596/2198/1/012040

<a id="ref-ibiwari-2025"></a> Ibiwari, B. W., Osemeke, B. E., Progress, V. D., Khadija, A., & Chikere, O. P. (2025). Hand anthropometric measurement and grip strength for basketball and volleyball players in higher institutions in Port Harcourt metropolis. International Journal of Science Academic Research, 6(8), 10513-10517.

<a id="ref-nag-2003"></a> Nag, A., Nag, P. K., & Desai, H. (2003). Hand anthropometry of Indian women. Indian Journal of Medical Research, 117, 260-269.

<a id="ref-rodriguez-vega-2024"></a> Rodríguez-Vega, G., & Rodríguez-Vega, D. A. (2024). Normative data for the anthropometric hand dimensions of the Mexican population. European Public & Social Innovation Review, 9, 1-15. https://doi.org/10.31637/epsir-2024-932

<a id="ref-gordon-2015"></a> Gordon, C. C., Blackwell, C. L., Bradtmiller, B., Parham, J. L., Barrientos, P., Paquette, S. P., Corner, B. D., Carson, J. M., Venezia, J. C., Rockwell, B. M., Mucher, M., & Kristensen, S. (2015). 2012 anthropometric survey of U.S. Army personnel: Methods and summary statistics (Report No. NATICK/TR-15/007). U.S. Army Natick Soldier Research, Development and Engineering Center.

<a id="ref-hu-2007"></a> Hu, H., Li, Z., Yan, J., Wang, X., Xiao, H., Duan, J., & Zheng, L. (2007). Anthropometric measurement of the Chinese elderly living in the Beijing area. International Journal of Industrial Ergonomics, 37(4), 303-311. https://doi.org/10.1016/j.ergon.2006.11.006

<a id="ref-mistarihi-2020"></a> Mistarihi, M. Z. (2020). A data set on anthropometric measurements and degree of discomfort of physically disabled workers for ergonomic requirements in work space design. Data in Brief, 30, 105420. https://doi.org/10.1016/j.dib.2020.105420

<a id="ref-molenbroek-1998"></a> Molenbroek, J. F. M. (1998). Geron study on Dutch elderly anthropometry. DINED database. Delft University of Technology. https://dined.io.tudelft.nl

<a id="ref-molenbroek-2003"></a> Molenbroek, J. F. M., Kroon-Ramaekers, Y. M. T., & Snijders, C. J. (2003). Revision of the Dutch standard for furniture in schools. Ergonomics, 46(5), 491-498. https://doi.org/10.1080/0014013031000085635

<a id="ref-steenbekkers-1998"></a> Steenbekkers, L. P. A., & van Beijsterveldt, C. E. M. (Eds.). (1998). Design-relevant characteristics of ageing users. Delft University Press.

<a id="ref-cross-1982"></a> Cross, N. (1982). Designerly ways of knowing. Design Studies, 3(4), 221-227. https://doi.org/10.1016/0142-694X(82)90040-0

<a id="ref-design-council-2020"></a> Design Council. (2020). Framework for innovation. https://www.designcouncil.org.uk/our-resources/framework-for-innovation/

<a id="ref-frayling-1994"></a> Frayling, C. (1994). Research in art and design (Royal College of Art Research Papers, Vol. 1, No. 1, 1993/4). Royal College of Art.

<a id="ref-zimmerman-2007"></a> Zimmerman, J., Forlizzi, J., & Evenson, S. (2007). Research through design as a method for interaction design research in HCI. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 493-502). ACM. https://doi.org/10.1145/1240624.1240704

<a id="ref-biddiss-2007"></a> Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive Technology, 2(6), 346-357. https://doi.org/10.1080/17483100701714733

<a id="ref-brack-2021"></a> Brack, T., & Amalu, E. H. (2021). A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. Journal of Orthopaedics, 24, 88-96. https://doi.org/10.1016/j.jor.2021.03.011

<a id="ref-guo-2025"></a> Guo, M. (2025). Human-centered design strategies for prosthetics based on user needs. Interdisciplinary Humanities and Communication Studies, 1(1), 39-48.

<a id="ref-henao-2025"></a> Henao, J. C., Phillips, S. T., Brooks, T. L., Pienta, K. J., Brantley, J. S., & Carey, S. L. (2025). Upper-limb prosthetic requirements from the healthcare providers, end-users and relatives' perspectives. Journal of Hand Therapy. Advance online publication. https://doi.org/10.1016/j.jht.2025.01.004

<a id="ref-herneth-2024"></a> Herneth, T., Hiesl, A., Stief, F., & Farago, D. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1-8). IEEE. https://doi.org/10.1109/IROS58592.2024.10801868

<a id="ref-hofmann-2016"></a> Hofmann, M. H., Griffiths, D., & Margetts, E. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858346

<a id="ref-jones-2023"></a> Jones, M. L. H., Vrieling, A. H., Steadman, J., & Kyberd, P. J. (2023). Evidencing the effectiveness of upper limb prostheses: A multi-stakeholder perspective on study requirements. Frontiers in Health Services, 3, 1123682. https://doi.org/10.3389/frhs.2023.1123682

<a id="ref-peerdeman-2011"></a> Peerdeman, B., Boere, D., Witteveen, H., Huis in 't Veld, R., Hermens, H., Stramigioli, S., Rietman, H., Veltink, P., & Misra, S. (2011). Myoelectric forearm prostheses: State of the art from a user-centered perspective. Journal of Rehabilitation Research and Development, 48(6), 719-738. https://doi.org/10.1682/JRRD.2010.08.0161

<a id="ref-baron-2020"></a> Baron, A., Gatzweiler, C., Geislinger, A., Huber, C., & Aszmann, O. C. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 274-287. https://doi.org/10.3390/prosthesis2040021

<a id="ref-cabibihan-2018"></a> Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2831907

<a id="ref-herbst-2021"></a> Herbst, Y., Georgopoulou, A., Dettwyler, M., Fernandez, A., Bacher, M., & Paik, J. (2021). Scan-driven fully-automated pipeline for a personalized, 3D printed low-cost prosthetic hand. In 2021 IEEE 17th International Conference on Automation Science and Engineering (CASE) (pp. 1188-1194). IEEE. https://doi.org/10.1109/CASE49439.2021.9551649

<a id="ref-lim-2018"></a> Lim, S. H., Bae, M., & Kim, S. H. (2018). Customization of a 3D printed prosthetic finger using parametric modeling. In ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. ASME. https://doi.org/10.1115/DETC2018-86211

<a id="ref-li-aflatoony-2025"></a> Li, M., & Aflatoony, L. (2025). Parametric design and three-dimensional printing: Enabling occupational therapists to develop custom hand grips. Disability and Rehabilitation: Assistive Technology, 20(6), 1829-1837. https://doi.org/10.1080/17483107.2025.2483953

<a id="ref-moreo-2016"></a> Moreo, A. M. (2016). Parametric design of a 3D printable hand prosthesis for children in developing countries [Master's thesis, Delft University of Technology].

<a id="ref-romero-2025"></a> Romero, M., Sánchez, J., & Álvarez, H. (2025). Development of parametric prostheses for different levels of human hand amputations manufactured through additive manufacturing. Applied Sciences, 15(3), 1124. https://doi.org/10.3390/app15031124

<a id="ref-machado-2019"></a> Machado, F., Malpica, N., & Borromeo, S. (2019). Parametric CAD modeling for open source scientific hardware: Comparing OpenSCAD and FreeCAD Python scripts. PLOS ONE, 14(12), e0225795. https://doi.org/10.1371/journal.pone.0225795

<a id="ref-manero-2019"></a> Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

<a id="ref-menaka-2025"></a> Menaka, S., Raja A, W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s).

<a id="ref-nilsiam-2017"></a> Nilsiam, Y., & Pearce, J. M. (2017). Free and open source 3-D model customizer for websites to democratize design with OpenSCAD. Designs, 1(1), 5. https://doi.org/10.3390/designs1010005

<a id="ref-nini-2024"></a> Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. https://doi.org/10.1109/BioRob60516.2024.10719909

<a id="ref-ten-kate-2017"></a> ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

<a id="ref-yu-2013"></a> Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

<a id="ref-base-local-antropometrica-2026"></a> Base local consolidada de dados antropométricos da mão e do membro superior distal. (2026). [Conjunto de dados]. Material de apoio da investigação, material/antropometria/dados antropométricos/multipopulationhand.csv.

Brack, R., & Amalu, E. H. (2021). A review  of technology, materials and R&D  challenges of upper limb prosthesis for  improved user suitability. Journal of

Orthopaedics, 23, 88–96.  https://doi.org/10.1016/j.jor.2020.12.009

<a id="ref-2-meter-este-link-na-bibliog"></a>

<a id="ref-3-nao-e-bem-marcacao-ne-te"></a>

<a id="ref-4-cool-mas-se-calhar-so-se"></a>

<a id="ref-5-vamos-adicionar-a-citacao"></a>

<a id="ref-6-explicar-oque-sao-todos-es"></a>

<a id="ref-8-escalonados-amplicados-e"></a>

<a id="ref-9-toda-esta-frase-podia-ser"></a>

<a id="ref-10-posso-igualmente-aumentar"></a>

<a id="ref-11-nao-me-soa-super-bem"></a>

<a id="ref-12-estou-a-bater-mal-ou-ja-e"></a>

<a id="ref-13-penalizacoes-e-um-pouco-f"></a>

## Anexo A — Metodologia de extração e codificação de dados antropométricos da mão

### A.1 Contexto e Objetivo

O desenvolvimento de um gerador paramétrico de próteses de mão requer dados antropométricos da mão humana que sejam suficientemente variados para cobrir diferentes populações, sexos e grupos etários. O objetivo deste processo foi construir uma base de dados estruturada em formato CSV que servisse de entrada direta ao modelo paramétrico, contendo medições reais retiradas de literatura científica publicada e de relatórios militares de referência.

Foram produzidos três ficheiros CSV complementares:

- - ansur1988complete.csv — 2.726 linhas, 47 dimensões corporais do estudo ANSUR 1988 (Gordon et al., 1989), população militar norte-americana

- - ansur1988handarm.csv — 696 linhas, subconjunto do ANSUR restrito às medições da mão, antebraço e braço

- - multipopulationhand.csv — 1.790 linhas, dados de onze estudos populacionais independentes de nove países diferentes

### A.2 Estratégia de Pesquisa Bibliográfica

### A.2.1 Pesquisa bibliográfica assistida e revisões sistemáticas

A pesquisa de literatura foi conduzida através de pesquisas bibliográficas orientadas por questões, complementadas por ferramentas de apoio à revisão e triagem, com o objetivo de identificar estudos de antropometria da mão com dados primários tabelados. As questões-chave incluíam variações de:

> "hand anthropometry normative data population study percentiles" "hand dimensions measurement ergonomics working population" "anthropometric survey finger length breadth caliper"

As listas de referências resultantes foram guardadas localmente em pastas organizadas por capítulo da tese. Os ficheiros de trabalho, citações e listas bibliográficas foram cruzados com a coleção local de PDFs para identificar lacunas.

### A.2.2 Base ANSUR 1988

O relatório ANSUR 1988 (Gordon et al., 1989) foi identificado como fonte de referência fundamental por ser um dos estudos antropométricos com maior dimensão amostral disponíveis publicamente (n=9.068 militares norte-americanos). Os dados foram extraídos diretamente das tabelas estatísticas detalhadas do relatório (Appendix B), que fornece, para cada dimensão e por sexo, a média, o desvio-padrão, os percentis P5, P10, P25, P50, P75, P90, P95, o mínimo e o máximo.

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

- - Dados secundários sem valor acrescentado — por exemplo, o trabalho de Moreo (2016) apresenta valores percentílicos de comprimento de dedo extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas), sem recolha própria. A Tabela 6.1 desse trabalho serve apenas para validar as escolhas de design do protótipo, não constituindo uma fonte primária codificável de forma independente.

- - Artigos de engenharia sem tabelas antropométricas — estudos centrados em materiais, análise de elementos finitos ou fabrico aditivo que referenciam dimensões da mão apenas de forma incidental e sem estatística descritiva.

- - Dimensões não da mão em estudos mistos — medições de outras regiões corporais presentes no mesmo artigo foram excluídas se não existia uma razão direta para a prótese de mão (exceção: comprimento cotovelo-ponta dos dedos, incluído por ser relevante para o encaixe do socket).

### A.4 Processo de Extração de Dados

### A.4.1 Leitura dos PDFs e localização das tabelas

Cada artigo foi lido integralmente, com foco nas secções de Methods (para identificar o instrumento de medição, a mão medida, e a posição do participante) e Results (para localizar as tabelas com estatística descritiva). A página exata de cada tabela foi registada no campo sourcepage do CSV.

Quando um artigo reportava medições em mais do que uma tabela (por exemplo, comprimentos numa tabela e larguras noutra), cada tabela foi processada separadamente.

### A.4.2 Identificação das unidades e conversão

Os artigos consultados reportam medições em milímetros (mm), centímetros (cm) ou, no caso do ANSUR, em polegadas (in). O CSV armazena sempre os três sistemas em simultâneo (valuemm, valuecm, valuein), calculados a partir de uma única unidade-fonte:

- - Se o artigo reporta em mm: valuecm = valuemm / 10; valuein = valuecm / 2.54

- - Se o artigo reporta em cm: valuemm = valuecm × 10; valuein = valuecm / 2.54

Esta redundância elimina conversões em tempo de execução por parte do modelo paramétrico.

### A.4.3 Decomposição em linhas atómicas

Cada célula de uma tabela estatística origina uma linha independente no CSV. Assim, para uma dada dimensão, população e sexo, existem tantas linhas quantos os indicadores estatísticos disponíveis: por exemplo, se um artigo reporta média, desvio-padrão, P5, P50 e P95, são criadas cinco linhas — cada uma com o campo stattype definido como mean, stddev ou percentile, e o campo percentile preenchido apenas nas linhas de tipo percentile.

Esta estrutura longa (long format) permite filtrar e agregar por qualquer combinação de variáveis sem necessidade de transformação prévia.

### A.4.4 Registo fiel do contexto da medição

O campo measurementmethodnote regista, para cada estudo, informações sobre:

- - O instrumento utilizado (e.g., "paquímetro digital Vernier 200 mm, resolução 0,01 mm")

- - A mão medida (direita/esquerda/dominante)

- - A posição da mão durante a medição (estendida e plana, em posição de repouso, sentado)

- - O ponto de referência do comprimento (e.g., "da prega palmar proximal à ponta do dedo")

Esta informação é crítica porque estudos diferentes definem as mesmas dimensões com protocolos diferentes: por exemplo, "comprimento da mão" pode ser medido desde a prega do pulso até à ponta do dedo médio (Rodríguez-Vega et al., 2024) ou desde o processo estilóide até à mesma ponta (Anacleto Filho et al., 2023), produzindo valores não diretamente comparáveis.

### A.5 Decisões por Estudo

### A.5.1 ANSUR 1988 — EUA, militares (Gordon et al., 1989)

Fonte: Tabelas de dados detalhados do relatório técnico do U.S. Army Natick Research Center (março de 1989), 47 dimensões corporais, separadas por sexo (n=2.208 mulheres, n=6.682 homens). As dimensões da mão e do membro superior foram codificadas na íntegra: comprimento da mão, largura da mão, comprimentos dos dedos, circunferência do pulso, comprimento do antebraço, entre outras.

Decisão: Incluição total. A dimensão amostral, a abrangência estatística (11 indicadores por dimensão) e a origem militar controlada tornam-no a âncora de referência da base de dados.

Notas: Sete valores no relatório original apresentavam inconsistências tipográficas (e.g., percentil aparentemente invertido ou unidade suspeita); todos foram corrigidos com anotação inline no campo dataqualitynote.

### A.5.2 Turquia — jovens adultos (Chatzioglou et al., 2024)

Fonte: Anatomy & Cell Biology, 57:172–182. n=51 (32F, 19M), idade 18–30, Izmir e Istanbul. Método foto-antropométrico com ImageJ (pixel → mm via fator de calibração 0,08618 ×). Comprimentos dos cinco dedos da mão direita, por sexo e amostra total, Tabela 1.

Decisão: Incluição. Primeiro estudo de foto-antropometria da mão na base de dados; o método é documentado de forma rigorosa e o artigo é publicado em revista indexada com revisão por pares. Os valores mínimo e máximo (mas não percentis) são reportados; foram codificados como stattype = min e max.

### A.5.3 México — população geral (Rodríguez-Vega & Rodríguez-Vega, 2024)

Fonte: European Public & Social Innovation Review, 9:1–15. n=2.837 (2.275M, 562F), Noroeste do México, idade 15–59. Quatro dimensões: comprimento da mão (HL), comprimento da palma (PL), largura da mão (HB) e diâmetro de preensão (HGD). Tabela 3 (amostra geral) e Tabela 4 (oito grupos etários: 15–19, 20–24, …, 50–54).

Decisão: Incluição, com marcação de qualidade nos subgrupos de pequena dimensão. A desagregação por grupo etário é única na base de dados e de grande valor para modelação por faixa etária. Foram detetados dois casos problemáticos na Tabela 4: o subgrupo feminino 50–54 tem n=3 (SD=0,00 reportado para HB, provavelmente artefacto de arredondamento); o subgrupo feminino 45–49 tem n=10. Ambos foram incluídos mas marcados no campo dataqualitynote.

### A.5.4 Índia — mulheres trabalhadoras (Nag et al., 2003)

Fonte: Indian Journal of Medical Research, 117:260–269. n=95 mulheres, trabalhadores informais (indústria de bidis, agarbattis e vestuário), Ahmedabad. 51 dimensões da mão direita em cinco tabelas (comprimentos, larguras, circunferências, profundidades, extensões e folgas), com P5, P50 e P95 reportados.

Decisão: Incluição total. É o estudo com maior granularidade de dimensões da mão na base de dados, e o único com dados de profundidade e circunferência por articulação. A restrição a mulheres e a uma população laboral informal específica é documentada na coluna population.

### A.5.5 Portugal — trabalhadores industriais (Anacleto Filho et al., 2023)

Fonte: International Journal of Industrial Ergonomics, 97:103473. n=343 (169M, 174F),

trabalhadores industriais do Norte de Portugal, 2021. De um conjunto de 27 dimensões corporais, apenas duas são da mão: comprimento da mão e largura da mão (metacarpal II–V). Tabela 3, P5, P50, P95 por sexo.

Decisão: Incluição. Embora apenas duas dimensões da mão sejam disponibilizadas, trata-se da única fonte de dados antropométricos da mão para população portuguesa adulta identificada na literatura, o que a torna indispensável para a contextualização nacional desta tese.

Nota metodológica: O estudo mediu o lado esquerdo por limitação de instalações; este facto é registado em measurementmethodnote.

### A.5.6 Nigéria — atletas universitários (Ibiwari et al., 2025)

Fonte: International Journal of Science Academic Research, 6(8):10513–10517. n=80: basquetebol (n=41: 21M, 20F) e voleibol (n=39: 20M, 19F), Universidade de Port Harcourt, idade 19–30. Quatro dimensões da mão direita por desporto e sexo: comprimento da mão, largura da mão, comprimento palmar e comprimento do 3.º dígito. Tabelas 3 e 4.

Decisão: Incluição com marcação de subgrupo desportivo. Dois subgrupos apresentam desvio-padrão atipicamente elevado (e.g., comprimento da mão no voleibol masculino: SD=37,49 mm), sugerindo a presença de outliers na amostra original. Estes casos foram marcados com nota de qualidade; os valores não foram excluídos porque provêm de tabelas publicadas e revistas.

Nota: A população de atletas não é representativa da população geral; os valores refletem uma seleção fisicamente ativa e potencialmente com mãos de dimensões superiores à média.

### A.5.7 Jordânia — trabalhadores com deficiência (Mistarihi, 2020)

Fonte: Data in Brief, 30:105420. n=40 trabalhadores com deficiência física, governorate de Irbid, Jordânia, idade 20–40. Sexos combinados (sem desagregação por sexo em Tabela 4). Comprimento da mão (mm) e comprimento cotovelo-ponta dos dedos (cm) com P5 e P95 na Tabela 4; largura da mão (cm, média apenas) a partir da Figura 2.

Decisão: Inclusão parcial. A dimensão amostral reduzida (n=40) e a ausência de desagregação por sexo limitam a utilidade direta dos dados. No entanto, é o único estudo com dados de uma população do Médio Oriente e com uma população com deficiência, o que justifica a inclusão para representatividade demográfica. A largura da mão (apenas média, sem SD, retirada de um diagrama de figura e não de uma tabela) foi incluída com marcação explícita de qualidade.

### A.5.8 EUA — dedo indicador (Lim et al., 2018)

Fonte: Trabalho académico UC Berkeley. n=50 adultos, idade 18–30. Apenas duas dimensões do dedo indicador (D2): comprimento MCP-ponta (média=90,9 mm) e largura na articulação PIP (média=16,9 mm). Apenas médias reportadas, sem SD ou percentis.

Decisão: Inclusão limitada. A ausência de desvio-padrão e percentis reduz significativamente a utilidade estatística. No entanto, o estudo foi incluído porque é especificamente orientado para a customização de próteses de dedo e fornece valores de referência para o design de um dedo índice protésico — diretamente relevantes para o objetivo desta tese. O coeficiente de determinação R²=0,18 entre comprimento e largura do dedo é marcado como indicador de correlação fraca.

### A.5.9 Estudo excluído: Moreo (2016)

O trabalho de Moreo (2016), dissertação de mestrado sobre design paramétrico de prótese de mão para crianças, foi lido na íntegra (55 páginas). A Tabela 6.1 apresenta valores percentílicos de comprimento de dedo por grupo etário, mas estes valores são extraídos da base de dados DINED (TU Delft, n=965 crianças neerlandesas) — não constituindo uma recolha primária por parte da autora. Incluir estes valores equivaleria a duplicar uma fonte secundária sem rastreabilidade direta ao estudo DINED original. Decisão: excluído.

### A.5.10 EUA — militares ANSUR II (Gordon et al., 2015)

Fonte: Relatório técnico NATICK/TR-15/007, U.S. Army Natick Soldier Research, Development and Engineering Center. n=6.068 militares ativos (4.082M, 1.986F), idade 17–58, grande diversidade étnica. Os dados brutos individuais foram disponibilizados em acesso público em 2017 (licença CC BY 4.0). As estatísticas foram calculadas a partir dos CSVs individuais (não do relatório impresso), usando Python puro sem dependências externas, por forma a garantir reprodutibilidade exata.

Decisão: Inclusão total. É o maior conjunto de dados individuais de antropometria da mão disponível publicamente. A disponibilidade de dados brutos individuais (em vez de apenas tabelas sumárias) permitiu calcular o conjunto completo de 11 indicadores por dimensão (média, SD, mínimo, máximo, P5, P10, P25, P50, P75, P90, P95). Sete medições codificadas: comprimento da mão, largura da mão (metacarpal), circunferência da mão, comprimento da palma, circunferência do pulso, comprimento antebraço-ponta do dedo médio e comprimento antebraço-centro de preensão.

Nota: A medição wristheight foi excluída — corresponde à distância do chão ao pulso em posição de pé, uma dimensão postural e não uma medição da mão.

### A.5.11 Países Baixos — DINED (TU Delft, 1993–2004)

Fonte: Base de dados antropométrica do Delft Institute for Ergonomics and Design, acessível via conta institucional em dined.io.tudelft.nl. Três sub-datasets distintos, com dados de mão disponíveis:

- - kima1993: crianças neerlandesas, idades 2–12 (grupos por ano), por sexo e combinado; 8 medições da mão por grupo etário.

- - geron1998: idosos neerlandeses, idades 50–80+ (bandas de 5 anos), por sexo e combinado; 5 medições da mão.

- - dined2004: adultos neerlandeses, grupos etários 20–30, 31–60, 60+, por sexo e combinado; 6–7 medições da mão.

Os dados foram extraídos a partir do HTML da interface web (padrões id="mean{col}{row}" / id="sd{col}{row}"), mapeando índices de coluna para combinações (sub-dataset, sexo, grupo etário) e índices de linha para nomes de medição.

Decisão: Inclusão total (três sub-datasets). Apenas média e desvio-padrão estão disponíveis; percentis não são fornecidos pela interface DINED. O grupo combinado 20–60 do dined2004 foi excluído por ser redundante relativamente aos grupos 20–30 e 31–60. Primeiro dataset pediátrico e o dataset de idosos mais granular da base de dados.

### A.5.12 China — idosos de Pequim (Hu et al., 2007)

Fonte: International Journal of Industrial Ergonomics, 37(4):303–311. DOI: 10.1016/j.ergon.2006.11.006. n=108 (58F, 50M), idade 65–85, residentes na área de Pequim, recrutados por conveniência entre reformados. Medições com paquímetro deslizante e paquímetro de pontas, segundo a norma chinesa GB/T 5703-1999 (equivalente à ISO 7250:1996). Tabela 1 (média e desvio-padrão) e Tabela 2 (P1, P5, P50, P95, P99).

Decisão: Inclusão parcial (cinco medições de mão/antebraço: largura da mão no metacarpal, largura máxima da mão, comprimento da mão, comprimento do dedo, comprimento antebraço-ponta dos dedos). P5, P50 e P95 codificados a partir da Tabela 2. A medição "Finger length" usa a designação do padrão GB/T 5703 sem especificar o dígito; assume-se o dedo médio, documentado em dataqualitynote.

Nota de cobertura: Primeira fonte de dados de idosos chineses e, simultaneamente, a única fonte da Ásia Oriental na base de dados (após a verificação de que uma referência alternativa inicialmente identificada não era verificável).

### A.5.13 Estudo excluído: reconstrução corporal 3D a partir de fotografias ortogonais

Fonte: artigo metodológico sobre reconstrução de modelos corporais 3D a partir de fotografias ortogonais, publicado no International Journal of Industrial Ergonomics, usando deformação de forma livre (FFD).

Decisão: excluído. O artigo não é um estudo de antropometria populacional: apresenta um método de modelação e valida-o sobre um único sujeito. A figura de validação do artigo compara valores do modelo com valores do participante real para 22 dimensões — não constituindo estatística descritiva de uma amostra. Não há média, desvio-padrão nem percentis de uma população. Incluir o valor de comprimento de mão do sujeito de validação (17 cm, lido do gráfico) seria metodologicamente incorreto.

### A.6 Estrutura do CSV e Schema

### A.6.1 Campos

| Campo | Tipo | Descrição |

| --- | --- | --- |

| sourcedocument | string | Título abreviado do artigo ou relatório fonte |

| sourcepage | int | Página da tabela de origem no documento |

| sourcecitation | string | Citação completa em estilo APA |

| measurementname | string | Nome da dimensão, incluindo especificações de método quando relevante |

| bodyregion | string | Região corporal (hand, forearm, upperarm, lowerlimb, torso, head) |

| measurementmethodnote | string | Instrumento, mão medida, posição e protocolo de medição |

| population | string | Descrição da população (e.g., "Young adults (age 18-30)") |

| country | string | País de recolha dos dados |

| sex | string | male, female ou combined |

| agegroup | string | Intervalo etário da (sub)amostra |

| samplesize | int | Número de participantes na (sub)amostra |

| stattype | string | Tipo de estatística: mean, stddev, percentile, min, max |

| percentile | string | Valor do percentil (5, 10, 25, 50, 75, 90, 95) — vazio se não aplicável |

| valuecm | float | Valor em centímetros |

| valuemm | float | Valor em milímetros |

| valuein | float | Valor em polegadas (calculado automaticamente) |

| dataqualitynote | string | Notas sobre limitações, artefactos ou incertezas do valor |

### A.6.2 Formato longo (long format)

A opção pelo formato longo — uma linha por estatística, e não uma linha por dimensão com colunas mean, sd, p5, etc. — permite:

- - Filtrar facilmente por tipo de estatística sem tratamento especial de colunas opcionais

- - Incluir estudos que reportam apenas subconjuntos de estatísticas (e.g., apenas média, sem percentis) sem introduzir células vazias em colunas estruturais

- - Acrescentar novos tipos de estatística (e.g., intervalo de confiança) sem alterar o schema

O custo é a repetição dos campos de identificação (país, sexo, dimensão) em cada linha — aceitável dado o volume total de dados (< 5 MB).

### A.7 Controlo de Qualidade dos Dados

### A.7.1 Marcação inline de limitações

O campo dataqualitynote é preenchido sempre que existe uma das seguintes situações:

- - Valor extraído de uma figura (diagrama ou gráfico) em vez de uma tabela

- - Subgrupo com n ≤ 10

- - Desvio-padrão ausente ou atipicamente elevado

- - Valor estimado a partir de estatísticas adjacentes por ilegibilidade da tabela

- - Correlação fraca entre variáveis reportada pelo próprio estudo

- - Inconsistência tipográfica no documento original, corrigida com nota

### A.7.2 Verificação de unidades

Todos os valores foram verificados pela coerência de ordem de grandeza. Por exemplo, um comprimento de mão adulta reportado em cm deve situar-se entre 15 e 22 cm; qualquer valor fora deste intervalo foi relido no artigo original antes de ser codificado.

### A.7.3 Rastreabilidade total

Cada linha do CSV contém a citação completa (sourcecitation) e o número de página exato (sourcepage), permitindo que qualquer valor seja verificado diretamente na fonte primária sem necessidade de metadados externos.

### A.8 Escrita do Código de Geração

Os dados foram codificados em dois scripts Python independentes:

- - generateansurcsv.py — gera ansur1988complete.csv e ansur1988handarm.csv a partir de dicionários Python embutidos no script, um por tabela do relatório ANSUR

- - generatemultipopulationhandcsv.py — gera multipopulationhand.csv a partir de dez secções numeradas, cada uma correspondente a um estudo ou conjunto de datasets

A escolha de embeber os dados diretamente no código (em vez de, por exemplo, folhas de cálculo intermédias) serve três propósitos: (1) rastreabilidade — cada valor está imediatamente adjacente à sua citação e nota de método; (2) reprodutibilidade — executar o script regenera o CSV de forma determinista; (3) controlo de versão — alterações aos dados são visíveis em diff de git, com o contexto de que estudo foi modificado.

O script aplica automaticamente as conversões de unidade, calcula valuein a partir de valuecm, e valida que nenhuma linha é emitida sem pelo menos uma das colunas valuemm ou valuecm preenchida.

### A.9 Resultado Final

| Ficheiro | Linhas (dados) | Países | Estudos | Dimensões distintas |

| --- | --- | --- | --- | --- |

| ansur1988complete.csv | 2.726 | 1 (EUA) | 1 | 47 |

| ansur1988handarm.csv | 696 | 1 (EUA) | 1 | 17 |

| multipopulationhand.csv | 1.790 | 9 | 11 | ~85 |

O ficheiro multipopulationhand.csv cobre nove países (EUA, Países Baixos, Turquia, México, Índia, Portugal, Nigéria, Jordânia, China), ambos os sexos e grupos combinados, grupos etários desde os 2 até aos 80+ anos, e populações tão diversas como crianças em idade escolar, idosos, atletas universitários, trabalhadores industriais, trabalhadoras informais e militares.

### A.10 Cobertura Global da Base de Dados e Lacunas

### A.10.1 O que está coberto

A base de dados multipopulationhand.csv foi construída com o objetivo de representar a variabilidade antropométrica da mão humana em múltiplas dimensões: geográfica, demográfica, etária e estatística. A tabela seguinte sintetiza a cobertura atual.

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

Nove países estão representados, distribuídos por sete regiões do mundo. A cobertura é particularmente densa nos EUA (três fontes independentes) e nos Países Baixos (três sub-datasets DINED).

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

A cobertura pediátrica (2–12 anos) existe apenas para os Países Baixos. A adolescência (13–17 anos) está ausente como grupo dedicado — o subgrupo mexicano 15–19 é o mais próximo, mas cobre uma faixa mais alargada. A idade adulta ativa (20–60) está bem coberta em múltiplos países. Os idosos estão representados nos Países Baixos (50–80+) e na China (65–85), mas não noutras geografias.

### A.10.1.3 Cobertura estatística

A profundidade estatística varia consideravelmente entre fontes:

| Nível de detalhe | Estudos |

| --- | --- |

| Média, SD, min, max, P5–P95 (11 indicadores) | ANSUR 1988, ANSUR II 2012 |

| Média, SD, P5, P50, P95 (5 indicadores) | DINED (3 sub-datasets), Hu et al. (2007) |

| P5, P50, P95 (3 indicadores) | Nag et al. (2003), Anacleto Filho et al. (2023), Rodríguez-Vega et al. (2024) |

| Média, SD, min, max (4 indicadores) | Chatzioglou et al. (2024), Ibiwari et al. (2025) |

| Média apenas | Mistarihi (2020) — largura da mão; Lim et al. (2018) |

A maioria das fontes não-americanas fornece apenas subconjuntos de estatísticas. Percentis intermédios (P10, P25, P75, P90) estão disponíveis exclusivamente nos datasets ANSUR. Esta assimetria é uma limitação real: para populações não-americanas, o modelo paramétrico pode interpolar entre P5 e P95, mas não dispõe de percentis de granularidade fina.

### A.10.2 Onde a cobertura falha

### A.10.2.1 Lacunas geográficas

As regiões mais populosas do mundo estão sub-representadas ou ausentes:

- - Ásia Oriental — China tem uma única fonte (n=108, apenas idosos de Pequim). Japão e Coreia do Sul estão completamente ausentes, apesar de serem países com literatura ergonómica ativa. O conjunto ANSUR é amplamente usado como proxy para populações ocidentais, mas os valores diferem sistematicamente das populações do leste asiático (mãos tendencialmente mais pequenas nos estudos disponíveis).

- - Ásia do Sudeste — Nenhum país representado (Indonésia, Filipinas, Vietname, Tailândia, etc.), apesar de concentrarem uma fração significativa da população mundial e de apresentarem diferenças antropométricas documentadas relativamente às populações sul-asiáticas.

- - África Subsaariana — Apenas a Nigéria, com uma amostra de atletas universitários (n=80) que não é representativa da população geral. Angola, Moçambique, e outros países de língua portuguesa estão ausentes, o que é particularmente relevante numa tese desenvolvida em Portugal.

- - América do Sul — Completamente ausente. Brasil, Colômbia e Argentina têm literatura ergonómica publicada mas não foram identificadas fontes acessíveis com dados de mão codificáveis.

- - Europa Central e de Leste — Ausente. Os Países Baixos e Portugal representam a Europa, mas há variabilidade antropométrica documentada entre populações do norte, sul e leste do continente.

### A.10.2.2 Lacunas demográficas

- - Adolescentes (13–17 anos) — a transição da mão infantil para a adulta não está coberta por nenhum estudo dedicado. O kima1993 chega aos 12 anos e o ANSUR começa aos 17.

- - Amputados — a mão de referência para uma prótese unilateral é a mão contralateral intacta do próprio utilizador. Não foi identificado nenhum estudo com estatística descritiva da mão intacta de utilizadores de próteses. Esta é a lacuna de maior impacto direto para o objetivo desta tese: sem estes dados, a personalização paramétrica baseia-se em populações saudáveis como aproximação.

- - Pessoas com deficiência física — apenas o estudo de Mistarihi (2020) cobre esta população (n=40, sexos combinados, Jordânia). A dimensão amostral é insuficiente para ser estatisticamente representativa.

- - Idosos fora da Europa e China — a prevalência de amputação de membro superior é mais elevada em contextos de baixo rendimento (causas traumáticas, diabetes, doença vascular), mas os dados de idosos disponíveis limitam-se a populações europeias e chinesas.

### A.10.2.3 Limitações qualitativas dos dados existentes

Para além das lacunas por ausência, existem limitações nos dados já presentes:

- - Heterogeneidade de protocolos — "comprimento da mão" é medido desde pontos de referência distintos consoante o estudo (prega distal do pulso, processo estilóide do rádio, articulação metacarpo-falângica). Os valores não são diretamente comparáveis entre fontes sem ajuste, o que limita a integração direta para inferência de valores fora da base de dados.

- - Amostras de conveniência — a maioria dos estudos não é probabilística: Chatzioglou et al. (2024) recrutou estudantes universitários de Izmir e Istanbul; Ibiwari et al. (2025) recrutou atletas universitários; Hu et al. (2007) recrutou reformados da área de Pequim. A representatividade nacional é, em todos estes casos, questionável.

- - Desequilíbrio de dimensões — o comprimento da mão e a largura da mão (metacarpal) estão presentes em quase todas as fontes; comprimentos por falange individual, profundidade da palma, e ângulos de abdução dos dedos estão ausentes exceto no ANSUR.

- - Mão medida — a maioria dos estudos mede a mão dominante ou a mão direita; o estudo português mede a mão esquerda por limitação de instalações. Esta inconsistência é registada nos metadados mas não pode ser corrigida post-hoc.

### A.10.3 Frentes identificadas para expansão futura

A expansão futura da base de dados deverá priorizar três frentes: dados pediátricos e adolescentes fora do contexto europeu, fontes nacionais de antropometria da mão em regiões ainda ausentes, e conjuntos de dados com maior granularidade anatómica dos dedos, falanges, punho e antebraço distal.

### A.10.3.1 Prioridade alta

- - Dados pediátricos e adolescentes da Ásia Oriental, capazes de preencher a lacuna entre os 13 e os 17 anos e de reduzir a dependência de fontes neerlandesas para perfis infantis.

- - Dados industriais ou ergonómicos do Médio Oriente com maior dimensão amostral e separação por sexo, de modo a complementar a fonte jordana já incluída.

- - Bases públicas nacionais com dados de mão para populações asiáticas, quando disponibilizarem metadados claros e condições de reutilização compatíveis com investigação académica.

### A.10.3.2 Prioridade média

- - Relatórios técnicos com medições granulares da mão, incluindo comprimentos por falange, profundidades articulares e ângulos de preensão.

- - Estudos baseados em digitalização 3D com amostras adultas amplas, desde que disponibilizem estatísticas por dimensão e não apenas exemplos individuais.

### A.10.3.3 Pertinência direta para o tema da tese

A lacuna de maior impacto continua a ser a ausência de dados de pessoas amputadas, sobretudo medições da mão contralateral intacta. Para o design de próteses de mão personalizadas, a referência mais adequada é a mão intacta do próprio utilizador, e não a média de uma população saudável. Uma recolha primária de dados, mesmo com dimensão reduzida, poderia ser metodologicamente mais valiosa do que acrescentar novas populações saudáveis sem relação clínica direta com o problema da personalização protésica.
