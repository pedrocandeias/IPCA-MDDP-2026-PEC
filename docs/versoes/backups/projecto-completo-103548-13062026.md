Projecto completo

Versão do documento:0.4.1

## Capítulo 1 — Introdução

### 1.1 Enquadramento geral, contexto e motivação

A perda de membros superiores provoca impactos funcionais (limitação nas tarefas quotidianas), sociais (alterações na interação e na inclusão) e simbólicos (mudanças na identidade e na percepção), o que requer soluções técnicas e projetuais que aliem desempenho mecânico, conforto ergonómico, aceitação estética e viabilidade económica. Apesar dos avanços em dispositivos médicos e na fabricação aditiva, persistem obstáculos relacionados ao custo, à personalização anatómica e à dependência de técnicos especializados para a adaptação e manutenção das próteses.

Nos últimos anos, a impressão 3D e as plataformas *open source* ampliaram o acesso a dispositivos protésicos, especialmente em contextos economicamente desfavorecidos. No entanto, muitos desses modelos dependem de geometrias fixas, isto é, formas pré-definidas sem adaptação automática, ou de ajustes manuais pouco padronizados, o que resulta em alterações sem um protocolo uniforme e dificulta a escalabilidade, a reprodutibilidade e a integração robusta de dados antropométricos, ou seja, medidas corporais específicas do utilizador.

O Design Industrial é o mediador entre a tecnologia e a experiência humana. A parametrização e a inteligência artificial podem estruturar sistemas configuráveis adequados a requisitos anatómicos, funcionais e simbólicos, promovendo próteses personalizadas, acessíveis e ajustáveis. Este trabalho explora criticamente essas ferramentas no contexto de Research Through Design.

### 1.2 Problema de investigação

Apesar da democratização parcial da produção de próteses por meio da fabricação aditiva, persiste uma lacuna na integração entre a personalização anatómica, a precisão funcional e as metodologias centradas no utilizador. Os processos atuais mostram dificuldades em se adaptar a diferentes perfis antropométricos, dependência de ajustes empíricos e ausência de plataformas configuráveis que aliem parametrização, dados antropométricos e apoio algorítmico à decisão projetual.

O problema central é compreender como o design de produto, através de sistemas paramétricos (soluções ajustáveis com base em dados) e inteligência artificial (algoritmos que auxiliam a tomada de decisões), pode viabilizar a personalização de próteses de membros superiores de modo acessível, reprodutível e robusto, mantendo a qualidade funcional e o controlo do projeto.

### 1.3 Objetivos da investigação

### 1.3.1 Objetivo geral

O objetivo geral é gerar conhecimento por meio da prática do Design, criando e avaliando um sistema de Design paramétrico (modelo ajustável por parâmetros definidos) assistido por inteligência artificial (algoritmos inteligentes) para próteses personalizadas de membros superiores. O sistema articula Design Industrial (criação de produtos), Design Inclusivo (acessibilidade para todos) e Design para Fabricação Aditiva.

### 1.3.2 Objetivos específicos

Pretende-se analisar criticamente o papel do Design Industrial como mediador entre a tecnologia e a experiência humana. O sistema paramétrico é um modelo ajustável, apoiado por uma plataforma digital, que permite configurar próteses com base em dados antropométricos (medidas físicas do utilizador) e em preferências individuais. Validar-se-á a abordagem por meio de prototipagem e de experimentação por impressão 3D, avaliando aspectos funcionais, ergonómicos e formais, bem como a viabilidade de fabricação.

A investigação busca responder: como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controle projetual? Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a reprodutibilidade de próteses impressas em 3D? Como o Design Industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?

### 1.5 Abordagem metodológica geral

O projeto adota uma metodologia aplicada, baseada em Research Through Design, que reconhece o ato de projetar como uma forma de gerar conhecimento. Estrutura-se em fases conceptual, metodológica e empírica, articuladas pelo modelo Double Diamond, que promove ciclos iterativos de exploração, definição, desenvolvimento e validação.

A fase conceptual realiza uma revisão crítica da literatura e das plataformas, consolidando o quadro teórico e os requisitos técnicos. A fase metodológica estabelece a arquitetura do sistema paramétrico assistido por inteligência artificial, integrando dados antropométricos e princípios de design para fabricação aditiva. A fase empírica operacionaliza a modelação paramétrica, a produção de protótipos por impressão 3D e a avaliação técnica e funcional, sem utilizar dados pessoais de utilizadores.

### 1.6 Estrutura da dissertação

A dissertação organiza-se em nove capítulos principais. O Capítulo 1 apresenta o enquadramento, o problema, os objetivos, as questões de investigação e a abordagem metodológica geral. O Capítulo 2 desenvolve o enquadramento teórico e o estado da arte. O Capítulo 3 explicita a metodologia de investigação. O Capítulo 4 descreve o desenvolvimento do modelo paramétrico. O Capítulo 5 aborda a plataforma web e a integração digital. O Capítulo 6 trata da integração da inteligência artificial. O Capítulo 7 discute a interface, a interação e a experiência de utilização. O Capítulo 8 reúne a avaliação e a discussão dos resultados. Por fim, o Capítulo 9 sintetiza as conclusões e os trabalhos futuros.

## Capítulo 2 — Enquadramento Teórico e Estado da Arte

### 2.1 Prótese de membro superior e dispositivos médicos

Prótese de membro superior é um dispositivo médico externo que substitui um segmento ausente devido à amputação ou a uma deficiência  congénita. Vai além da restituição formal: recupera funções, facilita atividades diárias, melhora a autonomia e reduz o impacto psicossocial da perda ([Fink & Diamond, 2023](#ref-fink-2023); [Segura et al., 2024](#ref-segura-2024)).

A perda total ou parcial de um membro superior provoca consequências físicas, funcionais, sociais e emocionais profundas. "Perda total" refere-se à ausência completa do membro, enquanto "perda parcial" indica ausência apenas de parte dele. A mão humana incorpora capacidades motoras e sensoriais complexas, abrangendo o alcance (movimento do membro para tocar ou agarrar objetos), a preensão (ato de segurar objetos), a manipulação fina (habilidade para movimentos precisos), a estabilização (manter objetos ou posições), a coordenação bimanual (uso de ambas as mãos em colaboração) e a exploração tátil (detecção de propriedades dos objetos pelo contato). Replicar artificialmente estas funções continua a ser um desafio significativo nos dispositivos médicos e na reabilitação. O desenvolvimento e a prescrição de próteses envolvem compromissos permanentes entre funcionalidade, peso, robustez, conforto, controle intuitivo, manutenção e custo.

> [!Qual sector?]
> Nas últimas décadas, o setor evoluiu de soluções maioritariamente cosméticas e mecânicas para sistemas com maior sofisticação eletromecânica, integração eletrônica aprimorada e potencial de personalização ampliado. Ainda assim, o avanço tecnológico não resolveu desafios estruturais como desconforto, dificuldade de controle, ausência de feedback sensorial e alta taxa de abandono. Esta tensão entre o potencial técnico e os resultados práticos é fundamental para compreender o estado atual das próteses de membro superior como dispositivos médicos.

### Tipologias de próteses de membro superior

> [!Quem diz que são 4?]
> As próteses de membro superior podem ser classificadas de acordo com a fonte de energia e o mecanismo de controlo. Distinguem-se quatro categorias principais: passivas (cosméticas), mecânicas acionadas pelo corpo, mioelétricas (externamente alimentadas) e híbridas. Cada tipo possui vantagens e limitações, o que reflete diferentes equilíbrios entre desempenho funcional, conforto, durabilidade e custo.

Próteses passivas destinam-se à aparência e ao apoio estático em tarefas simples, sem preensão ativa. Variam entre dispositivos rígidos e versões ajustáveis, nas quais os dedos ou os terminais podem ser movidos manualmente. São leves, simples, silenciosas e requerem pouca manutenção. Oferecem utilidade funcional limitada e são preferidas quando a estética é prioritária ou quando o utilizador procura um dispositivo discreto ([Fink & Diamond, 2023](#ref-fink-2023); [Segura et al., 2024](#ref-segura-2024)).

### Próteses mecânicas acionadas pelo corpo (*body-powered*)
As próteses mecânicas utilizam sistemas de arnês e cabos para converter movimentos do ombro, do tronco ou da cintura escapular em ação no dispositivo terminal, tipicamente um gancho ou uma mão mecânica. São soluções tradicionalmente valorizadas pela robustez, fiabilidade, menor custo e relativa facilidade de manutenção. Um atributo particularmente relevante é o feedback [^1]proprioceptivo indireto proporcionado pela tensão transmitida pelo sistema de cabos, que pode contribuir para um controlo funcional mais previsível em determinadas tarefas. Contudo, estas próteses apresentam limitações expressivas: o arnês pode ser desconfortável e restritivo, os padrões de preensão tendem a ser mais limitados e a sua utilização exige esforço físico contínuo e aprendizagem motora específica ([Engdahl et al., 2024](#ref-engdahl-2024); [Fink & Diamond, 2023](#ref-fink-2023)).

### Próteses mioelétricas
As próteses mioelétricas são dispositivos eletricamente alimentados que utilizam sinais eletromiográficos (EMG) captados por meio de elétrodos de superfície aplicados no membro residual. Esses sinais são processados eletronicamente e ativam os motores responsáveis pelo movimento da mão, do punho ou do cotovelo. Em comparação com as soluções mecânicas, apresentam habitualmente maior integração estética, ausência de arnês e potencial para padrões de movimento mais sofisticados. Em alguns casos, a sua utilização tem sido associada à redução da dor fantasma e a uma experiência de uso mais aceitável em contextos sociais. As suas limitações incluem maior peso, custo mais elevado, dependência de baterias, maior sensibilidade à humidade e a interferências, necessidade de calibração e ausência de feedback sensorial direto ([Bates et al., 2020](#ref-bates-2020); [Engdahl et al., 2024](#ref-engdahl-2024)).

### Sistemas híbridos
Combinam mecanismos mecânicos e elétricos no mesmo dispositivo. São particularmente frequentes em amputações proximais, como amputações transumerais ou desarticulações do ombro, podendo associar, por exemplo, controlo mecânico do cotovelo e controlo mioelétrico do terminal. Esta configuração procura tirar partido das vantagens específicas de cada sistema, distribuindo o peso, as exigências funcionais e a complexidade de controlo. Em contrapartida, a aprendizagem, a adaptação e a manutenção podem tornar-se mais exigentes ([Segura et al., 2024](#ref-segura-2024); [Walters et al., 2025](#ref-walters-2025)).

Uma representação visual útil desta diversidade tipológica é apresentada na Figura 2.1, que reúne exemplos de próteses impressas em 3D com soluções morfológicas e mecânicas distintas, ajudando a perceber como diferentes opções de configuração materializam compromissos distintos entre simplicidade, função e custo.

![](./figuras/ch23dprintedupperlimbprosthesesafigure2p5.png)

Figura 2.1 — Exemplos de próteses de membro superior impressas em 3D, ilustrando diversidade tipológica e construtiva.

Fonte original: ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

### Considerações clínicas e funcionais

A prescrição de uma prótese de membro superior constitui um processo clínico complexo, centrado no utilizador e conduzido por uma equipa multidisciplinar composta por médicos, protesistas, terapeutas e pelo próprio utilizador/paciente na escolha do dispositivo terminal, mas envolve uma avaliação integrada de fatores físicos, funcionais, ocupacionais e psicossociais ([Fink & Diamond, 2023](#ref-fink-2023); [Soyer et al., 2016](#ref-soyer-2016)).

Entre os fatores físicos incluem-se o nível de amputação, o comprimento e a condição do coto residual, a integridade cutânea, a amplitude articular e a força muscular. Amputações de nível mais proximal implicam desafios acrescidos em termos de controlo e do peso do sistema protésico.

Os fatores individuais, como idade, comorbilidades, dominância manual, literacia técnica, contexto profissional e atividades recreativas, influenciam significativamente a escolha da tipologia protésica. A título de exemplo, utilizadores envolvidos em trabalho manual intensivo ou em ambientes mais exigentes podem beneficiar de soluções mecânicas mais robustas, enquanto contextos profissionais e sociais em que a integração estética e a diversidade funcional são mais valorizadas podem favorecer dispositivos mioelétricos.

Os fatores psicossociais, incluindo motivação, expectativas, imagem corporal, suporte social e capacidade cognitiva, são igualmente determinantes. Expectativas irrealistas relativamente às capacidades do dispositivo podem levar à insatisfação, ao uso intermitente e ao eventual abandono.

A reabilitação protésica desenvolve-se em fases — cuidados perioperatórios, preparação pré-protésica, treino com prótese definitiva e acompanhamento a longo prazo. O treino funcional é particularmente relevante em sistemas mioelétricos, exigindo fortalecimento muscular específico, aprendizagem da geração de sinais consistentes e integração progressiva do dispositivo em tarefas reais. De modo recorrente, a literatura sublinha a importância do seguimento continuado, da educação do utilizador e do ajustamento iterativo do dispositivo ao longo do tempo ([Bates et al., 2020](#ref-bates-2020); [Soyer et al., 2016](#ref-soyer-2016)).

### Medição de resultados e abandono protésico

A avaliação objetiva do sucesso protésico continua a ser um desafio. Persistem a escassez de instrumentos padronizados e a heterogeneidade de métricas, o que dificulta a comparação entre estudos, dispositivos e estratégias de reabilitação. São utilizadas ferramentas de avaliação registadas pelo utilizador, centradas na funcionalidade percebida, na satisfação e na qualidade de vida, bem como testes baseados em desempenho, orientados para a destreza, a velocidade de execução e o controlo funcional em tarefas estruturadas ([Segura et al., 2024](#ref-segura-2024); [Soyer et al., 2016](#ref-soyer-2016)).

Apesar da evolução tecnológica, as taxas de abandono permanecem elevadas. A literatura associa, de forma recorrente, a rejeição protésica a problemas de conforto, peso, funcionalidade insuficiente, manutenção exigente e controlo pouco intuitivo. Esta persistência indica que a melhoria tecnológica isolada não garante adoção sustentada. Ainda assim, quando o dispositivo está adequadamente prescrito, ajustado e acompanhado, a utilização continuada de prótese tende a associar-se a maior independência funcional e a melhores indicadores de participação e de qualidade de vida do que a não utilização ([Fink & Diamond, 2023](#ref-fink-2023); [Smail et al., 2020](#ref-smail-2020)).

Esta persistência do abandono é sintetizada de forma clara na Figura 2.2, que relaciona uso, rejeição primária e rejeição secundária, reforçando que o problema não é marginal, mas estrutural no campo das próteses de membro superior.

![](./figuras/ch2prosthesisrejectioninacquiredmafigure1p4.png)

Figura 2.2 — Utilização, rejeição primária e rejeição secundária de próteses do membro superior adquiridas.

Fonte original (APA 7): Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive Technology, 2(6), 346-357. https://doi.org/10.1080/17483100701714733

### Enquadramento regulatório enquanto dispositivo médico

As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pela Regulamento ([^2]EU) 2017/745 (MDR) - https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng*, que classifica os dispositivos nas Classes I, IIa, IIb e III. Dispositivos terapêuticos ativos, incluindo próteses mioelétricas, enquadram-se geralmente nas classes intermédias ou superiores, o que exige avaliação por um organismo notificado para efeitos de marcação CE[^3] ([Parlamento Europeu e Conselho da União Europeia, 2017](#ref-parlamento-europeu-2017)).

Nos Estados Unidos, a regulação é assegurada pela Food and Drug Administration (FDA) por meio de um sistema de classificação de risco. A maioria dos componentes protésicos convencionais enquadra-se nas classes de risco mais baixas, enquanto sistemas mais complexos, como próteses mioelétricas avançadas, podem exigir controles , documentação técnica mais extensa e, em certos casos, evidência clínica adicional ([Resnik et al., 2010](#ref-resnik-2010)).

A demonstração de segurança e desempenho implica avaliação clínica sistemática, testes de biocompatibilidade, avaliação da segurança mecânica e elétrica, validação de software e consideração explícita de fatores humanos e de usabilidade. Normas desenvolvidas no âmbito do comité técnico ISO/TC 168[^4] contribuem para a padronização de requisitos aplicáveis a próteses e ortóteses. Adicionalmente, os fabricantes devem implementar sistemas de vigilância pós-comercialização, recolhendo dados de uso real ao longo do ciclo de vida do dispositivo, o que reforça a natureza regulada, iterativa e evidencial deste domínio ([Parlamento Europeu & Conselho da União Europeia, 2017](#ref-parlamento-europeu-2017); [Resnik et al., 2010](#ref-resnik-2010)).

### 2.2 Design Industrial, Design Inclusivo e Design Centrado no Utilizador

O design industrial, no contexto da saúde e das tecnologias de apoio, é reconhecido progressivamente como uma disciplina mediadora entre as necessidades humanas, os contextos de utilização e os sistemas técnicos regulados. A literatura evidencia que o design não se limita à configuração formal de produtos, mas também desempenha um papel estruturante na promoção da inclusão, da autonomia e da participação social, ao modelar a relação entre indivíduos e ambientes por meio de artefactos e sistemas. Em particular, nas tecnologias de apoio, o design é descrito como um elemento que medeia a interação entre os utilizadores e o seu meio envolvente, contribuindo para reduzir barreiras funcionais e sociais e, consequentemente, para melhorar os resultados de participação e a qualidade de vida ([Clarkson & Coleman, 2010](#ref-clarkson-2010); [Shah & Robinson, 2006](#ref-shah-2006)).

Paralelamente, o design inclusivo é apresentado como um imperativo contemporâneo que visa minimizar a exclusão evitável decorrente de decisões projetuais que não consideram a diversidade populacional e a variabilidade de capacidades ao longo do tempo. Esta perspetiva alinha-se com a responsabilidade dos sistemas de saúde de responder a utilizadores heterogéneos, com diferentes condições físicas, cognitivas e contextuais ([Clarkson & Coleman, 2010](#ref-clarkson-2010)).

### Design industrial em dispositivos médicos

No domínio dos dispositivos médicos, o design industrial surge tanto como prática metodológica centrada no utilizador como também com um papel colaborativo integrado em equipas multidisciplinares de desenvolvimento. A literatura identifica, contudo, uma lacuna estrutural: muitos dispositivos médicos continuam a ser desenvolvidos predominantemente com base em abordagens de engenharia e em requisitos regulatórios, com participação limitada de profissionais com formação específica em metodologias de design centrado no uso. Esta assimetria contribui para soluções tecnicamente robustas, mas nem sempre otimizadas em termos de ergonomia, usabilidade ou integração na vida quotidiana ([Fisher & Johansen, 2020](#ref-fisher-2020); [Wilke et al., 2020](#ref-wilke-2020)).

Neste contexto, o design industrial assume relevância não apenas na fase de conceptualização, mas também na definição de requisitos de utilização, na tradução de necessidades clínicas em soluções tangíveis e na articulação entre requisitos regulatórios e experiência do utilizador ([Fisher & Johansen, 2020](#ref-fisher-2020); [Shah & Robinson, 2006](#ref-shah-2006)).

Esta posição intermédia do design torna-se mais clara quando se observa a multiplicidade de papéis que os profissionais de saúde podem assumir nos processos de desenvolvimento. Em vez de contribuírem apenas como validadores de soluções, estes agentes podem ser intervenientes do seu setor, utilizadores peritos, mediadores entre domínios e profissionais clínicos ou investigadores, como sintetiza a Tabela 2.1.

Tabela 2.1 — Papéis dos profissionais de saúde no desenvolvimento de dispositivos médicos

| Intervenientes do setor                 | Identificam oportunidades, especificações e condicionantes regulatórias | Mercado, estratégia e processos de certificação            |
| --------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| Utilizadores peritos                    | Fornecem experiência clínica situada e problemas de uso                 | Experiência do utilizador e adequação funcional            |
| Mediadores                              | Traduzem linguagem, necessidades e constrangimentos entre equipas       | Problemas técnicos, terminologia e entendimento partilhado |
| Profissionais clínicos e investigadores | Enquadram cuidados, testes e validação empírica                         | Resultados clínicos, ensaios e usabilidade                 |

Fonte adaptada. Referência original (APA 7): Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. https://doi.org/10.1080/14606925.2024.2420152

### Design Inclusivo e Design Universal

O design inclusivo representa uma mudança conceptual significativa ao deslocar o foco da deficiência enquanto atributo individual para a compreensão da deficiência como resultado de desajustes entre capacidades humanas e ambientes projetados ([Clarkson & Coleman, 2010](#ref-clarkson-2010)).

Esta perspetiva aproxima-se dos modelos sociais e relacionais da deficiência, enfatizando que a exclusão pode ser produzida por decisões de projeto que não contemplam a diversidade de utilizadores ([Clarkson & Coleman, 2010](#ref-clarkson-2010)).

Enquanto campo de prática e investigação, o design inclusivo desenvolveu ferramentas e orientações destinadas a apoiar equipas de projeto na consideração sistemática da diversidade populacional. Estas incluem estratégias de segmentação, análise de capacidades e critérios de acessibilidade aplicáveis a produtos e sistemas, incluindo tecnologias digitais em saúde ([Clarkson & Coleman, 2010](#ref-clarkson-2010)).

O design universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente aplicada no design industrial, tendo como princípio orientador a conceção de produtos e ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações ou de design especializado. Os Sete Princípios do Design Universal, propostos por Ron Mace[^5], são amplamente citados como um quadro normativo para avaliar equidade, flexibilidade, simplicidade, tolerância ao erro e redução do esforço físico ([Story, 2006](#ref-story-2006)).

Na área da saúde, o design universal é associado a abordagens centradas no paciente e avaliado por meio de critérios orientados a resultados, como a participação, a inclusão e a igualdade de acesso. A convergência entre design inclusivo e design universal revela-se particularmente evidente na ênfase comum na redução de barreiras ambientais e na ampliação do conceito de usabilidade para uma população mais ampla ([Story, 2006](#ref-story-2006); [White & Mosca, 2022](#ref-white-2022)).

### Design Centrado no Utilizador e Design Centrado no Humano

O design centrado no utilizador (User-Centred Design – UCD) é descrito como uma abordagem que envolve os utilizadores finais ao longo de todo o processo de desenvolvimento, com o objetivo de assegurar que o produto seja funcionalmente adequado, compreensível e valorizado. Esta abordagem mobiliza métodos como entrevistas, personas, protocolos de think-aloud, prototipagem iterativa e grupos focais, promovendo ciclos sucessivos de recolha de requisitos e de validação ([Fisher & Johansen, 2020](#ref-fisher-2020); [Shah & Robinson, 2006](#ref-shah-2006)).

O design centrado no humano (Human-Centred Design – HCD) amplia esta perspetiva ao integrar dimensões culturais, contextuais e sistémicas. No desenvolvimento de dispositivos médicos, o HCD é associado a práticas como etnografia, design participativo, mapeamento de jornadas (journey maps), mapeamento de stakeholders e avaliação de fatores humanos. A norma ISO 62366 estabelece requisitos específicos para a aplicação de engenharia de usabilidade em dispositivos médicos, reforçando a integração formal de testes formativos e sumativos no processo regulado ([Fisher & Johansen, 2020](#ref-fisher-2020); [Millet et al., 2018](#ref-millet-2018)).

A incorporação de fatores humanos é igualmente reforçada por diretivas e normas que exigem a redução dos riscos de uso inadequado, articulando segurança, ergonomia e usabilidade como dimensões indissociáveis do desenvolvimento de dispositivos médicos ([Millet et al., 2018](#ref-millet-2018)).

### Design Participativo e Co-design

O design participativo e o co-design representam um aprofundamento das abordagens centradas no utilizador, enfatizando a participação ativa e o empoderamento dos utilizadores no processo de projeto. Nestes modelos, os utilizadores não são apenas fontes de dados, mas também colaboradores na definição de problemas, na geração de soluções e na avaliação de protótipos ([Chapman et al., 2025](#ref-chapman-2025)).

Revisões sistemáticas apontam para a necessidade de maior transparência e rigor na descrição dos processos de co-design, de modo a fortalecer a sua validade metodológica e eficácia prática. Nas tecnologias de apoio, observa-se uma evolução discursiva dos modelos centrados no utilizador para paradigmas de cocriação, nos quais as experiências dos utilizadores assumem um estatuto central na tomada de decisão ([Chapman et al., 2025](#ref-chapman-2025)). Persistem tensões entre ideais participativos e contextos regulatórios altamente estruturados, nos quais a autoridade decisional permanece frequentemente concentrada em profissionais clínicos e em equipas técnicas ([Chapman et al., 2025](#ref-chapman-2025); [Wilke et al., 2020](#ref-wilke-2020)).

### Metodologias, instrumentos e avaliação

A literatura evidencia que as abordagens inclusivas e centradas no utilizador recorrem a repertórios metodológicos diversificados, incluindo personas, simulação de limitações, prototipagem iterativa, oficinas participativas e análise de ecossistemas de stakeholders ([Fisher & Johansen, 2020](#ref-fisher-2020); [Shah & Robinson, 2006](#ref-shah-2006)).

No domínio hospitalar e dos serviços de saúde, ferramentas de avaliação baseadas em critérios de design universal e de design para todos (Design for All) introduzem sistemas de análise multicritério e listas de verificação estruturadas para aferir os níveis de inclusão ([White & Mosca, 2022](#ref-white-2022)).

Em contextos de tecnologias de apoio, modelos como o Matching Person and Technology (MPT)[^6] e quadros conceptuais baseados na Classificação Internacional de Funcionalidade (ICF) são utilizados para apoiar decisões de seleção e de adequação tecnológica, promovendo o alinhamento entre as características do utilizador, do ambiente e do dispositivo ([White & Mosca, 2022](#ref-white-2022)).

A avaliação da evidência tem sido igualmente reforçada por meio do uso de protocolos sistemáticos, como o PRISMA, e de instrumentos de avaliação crítica, o que reflete uma crescente preocupação em fundamentar decisões de design com base empírica robusta ([Chapman et al., 2025](#ref-chapman-2025)).
### Desafios e lacunas

Entre os principais desafios identificados destacam-se: – a articulação entre padronização e personalização, particularmente relevante em dispositivos médicos sujeitos a regulamentação rigorosa; – a discrepância entre modelos teóricos de UCD ensinados academicamente e as restrições institucionais à prática em saúde; – a dificuldade de tradução de processos participativos para contextos de implementação e de escalabilidade; – e a necessidade de integrar dimensões interseccionais (como género e fatores socioculturais) na investigação e no desenvolvimento.

Estas lacunas evidenciam que o design industrial em dispositivos médicos não pode ser compreendido apenas como uma prática formal ou estética, mas como uma disciplina estratégica que articula inclusão, regulação, implementação e experiência do utilizador.

### 2.3 Fabricação Aditiva e parametrização no design de produto

A convergência entre modelação paramétrica e fabricação aditiva (FdA) tem sido amplamente reconhecida como um dos principais vetores de transformação no design contemporâneo, particularmente em contextos que exigem personalização, adaptação morfológica e produção de variantes em pequena escala. A literatura posiciona estas duas abordagens como complementares: a modelação paramétrica permite gerar múltiplas variações controladas a partir de um modelo-base, enquanto a fabricação aditiva viabiliza a materialização de geometrias complexas sem necessidade de moldes ou ferramentas dedicadas ([Lei et al., 2016](#ref-lei-2016); [Ozdemir et al., 2022](#ref-ozdemir-2022); [Stralen, 2018](#ref-stralen-2018)).

Esta articulação é representada com clareza na Figura 2.3, que resume o encadeamento entre aquisição digital, modelação/retificação e fabrico, evidenciando que a personalização depende menos de um único software ou de uma etapa isolada e mais de um workflow integrado.

![](./figuras/ch2ascopingreviewofdigitalfabricafigure1p2.png)

Figura 2.3 — Fluxo digital entre aquisição, CAD/CAM e fabricação aditiva em próteses e ortóteses.

Fonte original (APA 7): Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517

Neste enquadramento, a personalização deixa de ser entendida como exceção e passa a constituir uma estratégia estruturada, operacionalizada por meio de “seed designs”[^7] ou modelos-base parametrizados. Estes modelos preservam uma arquitetura estável, expondo simultaneamente um conjunto limitado de variáveis ajustáveis, frequentemente acessíveis por meio de interfaces digitais ou de configuradores destinados a utilizadores não especialistas ([Ozdemir et al., 2022](#ref-ozdemir-2022); [Stralen, 2018](#ref-stralen-2018)).

### Modelação Paramétrica e Espaços de Variação

Os modelos paramétricos desempenham duas funções centrais. Em primeiro lugar, codificam a lógica geométrica do produto — relações, restrições e regras —, assegurando que alterações nos valores dos parâmetros gerem novas variantes sem comprometer a integridade estrutural nem a coerência funcional. Em segundo lugar, permitem explorar espaços de variação extensos, frequentemente descritos como quase contínuos, o que possibilita a criação de famílias de produtos ajustáveis por meio da modificação de variáveis dimensionais ou funcionais ([Lei et al., 2016](#ref-lei-2016); [Ozdemir et al., 2022](#ref-ozdemir-2022)).

No contexto da adaptação ao utilizador, a literatura destaca que a parametrização torna-se particularmente eficaz quando associada a dados mensuráveis, como a antropometria ou as digitalizações tridimensionais. Em vez de um escalonamento uniforme, que pode introduzir desvios significativos, a definição de parâmetros independentes (por exemplo, comprimento e largura) permite ajustes mais precisos e controlo dimensional dentro de margens reduzidas. Em aplicações protésicas, esta abordagem revelou maior proximidade às cinemáticas naturais e melhor adequação morfológica face a modelos simplesmente [^8]escalados ([Lim et al., 2018](#ref-lim-2018)).
### Integração com Fabricação Aditiva e Design for Additive Manufacturing

A eficácia da personalização depende da integração precoce dos constrangimentos do processo de fabricação aditiva no processo de projeto. A literatura sobre Design for Additive Manufacturing (DfAM) sublinha que a incorporação antecipada de limitações de processo — tolerâncias, resistência mecânica, espessuras mínimas, orientação de impressão — reduz falhas de fabrico e encurta os ciclos iterativos ([Chtioui et al., 2023](#ref-chtioui-2023); [Wiberg et al., 2019](#ref-wiberg-2019)).

Estudos aplicados demonstram que, ao determinar experimentalmente constrangimentos do processo e incorporá-los ao modelo paramétrico, é possível gerar milhares de variantes únicas com elevada taxa de sucesso funcional, minimizando as reimpressões ([Wiberg et al., 2019](#ref-wiberg-2019)). [^9]

Esta evidência reforça a necessidade de uma ligação sistemática entre as fases de design e manufatura, contrariando abordagens que tratam a fabricação como etapa posterior e corretiva ([Chtioui et al., 2023](#ref-chtioui-2023); [Wiberg et al., 2019](#ref-wiberg-2019)).

As tecnologias de FA utilizadas incluem FDM/FFF (extrusão de termoplásticos), SLS (fusão seletiva a laser), SLA (estereolitografia) e processos industriais metálicos, o que reflete a diversidade de rotas produtivas para componentes personalizados. Cada tecnologia implica requisitos específicos de projeto, reforçando a importância de integrar critérios técnicos no modelo paramétrico desde o início ([Chtioui et al., 2023](#ref-chtioui-2023); [Wiberg et al., 2019](#ref-wiberg-2019)).[^10]

### Configuradores e Cocriação Digital

A articulação entre modelação paramétrica e interfaces digitais possibilita novos modelos de cocriação e de produção distribuída. Configuradores web ou interfaces baseadas em CAD expõem um conjunto delimitado de parâmetros, permitindo ao utilizador ajustar dimensões ou características dentro de intervalos válidos, frequentemente com feedback em tempo real sobre viabilidade ([Ozdemir et al., 2022](#ref-ozdemir-2022); [Stralen, 2018](#ref-stralen-2018)).

A Figura 2.4 mostra um exemplo especialmente relevante desta lógica: a personalização mediada por interface, em que o utilizador atua sobre atributos visuais e formais dentro de um espaço de variação previamente estruturado. Este tipo de configurador ajuda a compreender como a cocriação digital pode ser operacionalizada sem exigir domínio direto de ferramentas CAD complexas.

![](./figuras/ch2implementationof3dprintingtechnfigure5p8.png)

Figura 2.4 — Exemplo de configurador digital para personalização de uma prótese impressa em 3D.

Fonte original (APA 7): Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

Este modelo “file-to-factory” viabiliza fluxos digitais em que o ficheiro parametrizado é convertido diretamente em instruções de fabrico, seja localmente (impressão 3D descentralizada) ou através de uma encomenda online[^11]. A literatura associa esta lógica à democratização do design e à expansão de estratégias de *mass customization* e *mass personalization*, reduzindo custos marginais ao eliminar a utilização de moldes e dispositivos específicos de [^12]fabrico ([Lei et al., 2016](#ref-lei-2016); [Stralen, 2018](#ref-stralen-2018)).

Contudo, enfatiza-se que configuradores eficazes devem limitar o número de parâmetros expostos e fornecer orientação clara sobre os limites válidos, evitando complexidade excessiva ou escolhas superficiais ([Ozdemir et al., 2022](#ref-ozdemir-2022)).

### Otimização, Geração e Avaliação de Desempenho

A parametrização é frequentemente combinada com métodos de otimização topológica, de geração de estruturas reticuladas e de abordagens multiobjetivo. Estas estratégias permitem gerir compromissos entre peso, resistência, custo e tempo de fabrico, explorando fronteiras de Pareto para selecionar soluções alinhadas com objetivos específicos ([Lei et al., 2016](#ref-lei-2016); [Yao et al., 2016](#ref-yao-2016)).

Em contextos médicos e assistivos, estudos demonstram a integração de modelos paramétricos com análises de elementos finitos (FEM) para validar o desempenho estrutural, bem como de algoritmos generativos que adaptam padrões e estruturas superficiais a geometrias individualizadas ([Lei et al., 2016](#ref-lei-2016); [Lim et al., 2018](#ref-lim-2018)).

Este cruzamento entre parametrização, simulação e FA evidencia um ecossistema digital integrado que sustenta personalização técnica com base quantitativa ([Lei et al., 2016](#ref-lei-2016); [Yao et al., 2016](#ref-yao-2016)).

### Implicações para o Design Industrial

A literatura converge para a ideia de que a robustez do modelo paramétrico é uma condição crítica para a personalização em escala. Modelos mal estruturados ou com dependências inconsistentes podem comprometer a simulação, a otimização e a configuração de famílias de produto ([Lei et al., 2016](#ref-lei-2016); [Wiberg et al., 2019](#ref-wiberg-2019)).

Assim, a qualidade da definição paramétrica desempenha um papel estratégico para a viabilidade de sistemas adaptáveis ([Ozdemir et al., 2022](#ref-ozdemir-2022)).

Em termos económicos, a Fabricação Aditiva permite reduzir [^13]penalizações tradicionais associadas à variação de produto, sustentando modelos de personalização acessíveis. Estudos orientados para famílias de produto indicam que a integração de modelos paramétricos com análises de custo e desempenho pode manter os custos relativamente estáveis mesmo com elevada diversidade geométrica ([Lei et al., 2016](#ref-lei-2016); [Yao et al., 2016](#ref-yao-2016)).

No plano educativo e profissional, recomenda-se a integração de DfAM nos currículos de design industrial, promovendo competências que articulem a conceção, a simulação e a fabricação digital em fluxo contínuo ([Kandikjan et al., 2022](#ref-kandikjan-2022)).

### 2.4 Antropometria aplicada ao design protésico

A antropometria constitui um fundamento técnico e metodológico central no design protésico, na medida em que a adequação geométrica do dispositivo ao corpo do utilizador condiciona diretamente o conforto, a segurança, o desempenho funcional e a aceitação. Em próteses e tecnologias de apoio, a literatura recente evidencia uma transição progressiva de medições manuais baseadas em marcos anatómicos para processos digitais de captura de superfície (digitalização 3D e fotogrametria), integrados com fluxos CAD/CAM e com fabricação aditiva. Esta evolução é frequentemente descrita como uma cadeia “aquisição anatómica → modelação/retificação em CAD → fabrico aditivo → pós-processamento”, embora também se reconheça que muitos estudos permanecem em fases de prova de conceito e carecem de validação longitudinal e em larga escala ([Chainando et al., 2025](#ref-chainando-2025)).

### Da dimensão linear à “forma” como dado de projeto

Historicamente, a antropometria aplicada ao design baseou-se em medidas escalares (comprimentos, larguras, perímetros), obtidas com instrumentos como paquímetros, compassos antropométricos e fitas métricas, muitas vezes segundo procedimentos normalizados (por exemplo, a norma ISO 7250). Contudo, no design protésico — particularmente em interfaces corpo–dispositivo, como o encaixe (socket) — a literatura sublinha que a “forma” (shape) desempenha um papel determinante, pois pequenas variações volumétricas e distribuições de pressão podem gerar desconforto, lesões cutâneas e abandono do dispositivo. Estudos e revisões referem que o ajuste protésico pode exigir tolerâncias muito reduzidas e que a complexidade anatómica, bem como trajetórias de carga e zonas de alívio, não é devidamente capturada por um conjunto limitado de medidas lineares ([Albin & Molenbroek, 2023](#ref-albin-2023); [Young et al., 2023](#ref-young-2023)).

Assim, observa-se uma valorização crescente de métodos capazes de capturar geometria tridimensional de alta resolução e de traduzir essa informação em modelos CAD passíveis de retificação, parametrização e fabrico ([Squibb et al., 2024](#ref-squibb-2024)).

Mesmo assim, a medição linear continua a ser indispensável para estruturar o modelo paramétrico, sobretudo quando se pretende definir um conjunto mínimo de entradas robustas e replicáveis. A Figura 2.5 ilustra precisamente este nível basal: os marcos anatómicos e os comprimentos de referência que sustentam medições comparáveis da mão.

![](./figuras/ch22dand3danatomicalanalysesofhafigure1p3.png)

Figura 2.5 — Marcos anatómicos e medidas de referência da mão para fins de personalização.

Fonte original (APA 7): Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

### Métodos de recolha antropométrica em próteses e tecnologias de apoio

A literatura organiza os métodos de recolha em famílias, cada uma com potencialidades e limitações específicas para o design protésico:

1. A antropometria manual inclui medições em posturas normalizadas, com instrumentos clínicos e de ergonomia. Mantém relevância em contextos de acessibilidade clínica e de monitorização simples (por exemplo, circunferências para inferir variações do coto). Contudo, assinala-se que as medidas de circunferência podem ser um proxy frágil para alterações reais de volume, dependendo da geometria e da distribuição dos tecidos, o que limita a sua fiabilidade para decisões de ajuste fino ([Ibrahim et al., 2024](#ref-ibrahim-2024)).

2. Digitalização 3D (scanning óptico)capta a superfície corporal em nuvens de pontos ou malhas, que são posteriormente limpas e convertidas em modelos utilizáveis (frequentemente em STL) para CAD e fabrico. É descrita como facilitadora de fluxos de personalização e pode ser combinada com a automatização (por exemplo, correspondência de características anatómicas) para reduzir o trabalho manual. A consistência pode variar conforme a complexidade da forma, e desafios de repetibilidade são relatados quando a geometria é irregular, como em cotos complexos ([Squibb et al., 2024](#ref-squibb-2024)).

3. Fotogrametria reconstrói modelos 3D a partir de fotografias 2D, incluindo soluções baseadas em smartphones.É apresentada como um método promissor pela rapidez na captura e pelo potencial de democratização, embora possa exigir mais tempo de processamento e cuidados com a iluminação e a cobertura da imagem. Em síntese, as ortóteses constituem uma das abordagens mais adequadas para a aquisição da geometria 3D do corpo em fluxos personalizados ([Silva et al., 2024](#ref-silva-2024)).

4. Imagens médicas (CT/MRI) permitem obter geometria externa e, em alguns casos, informação interna (por exemplo, estruturas ósseas), o que sustenta modelos mais ricos e abordagens como a modelação estatística de forma. Contudo, envolve maior custo e menor acessibilidade e, no caso do CT, implica considerações associadas à exposição à radiação e à dependência do contexto hospitalar.

5. Medições complementares da interface (pressão, termografia, bioimpedância) A literatura enfatiza que, em próteses, a adequação não é apenas geométrica: depende do comportamento da interface durante o uso. Por isso, surgem métodos adjuntos que quantificam sinais de ajuste, como a distribuição de pressão e de cisalhamento, “hot spots” térmicos e flutuações de volume do coto. Estes métodos ajudam a ligar decisões de forma/retificação a desfechos de conforto e segurança, embora, em muitos casos, sejam descritos como ainda experimentais e com barreiras à adoção clínica ([Ibrahim et al., 2024](#ref-ibrahim-2024); [Young et al., 2023](#ref-young-2023)).

### Interpretação e aplicação de dados antropométricos no projeto

A passagem de dados antropométricos para critérios de projeto ocorre por diferentes vias analíticas:

– Dimensionamento estatístico por percentis e avaliação de incompatibilidades dimensionais: método típico no design ergonómico para definir dimensões que acomodam uma percentagem da população; aplicado sobretudo a produtos de uso “externo” (por exemplo, cadeiras de rodas e interfaces). – Métodos multivariados e aprendizagem estatística: usados quando se trabalha com dados de alta dimensionalidade (malhas, secções, nuvens de pontos), permitindo extrair padrões de retificação ou modos de variação. – Modelos preditivos e modelação estatística de forma (SSM): aplicados para reconstruir a geometria a partir de medições reduzidas e inferir relações entre a superfície e a anatomia interna, com PCA e regressões como ferramentas frequentes, embora limitados por tamanhos amostrais reduzidos em vários estudos ([Sunderland et al., 2024](#ref-sunderland-2024)).

Em design protésico, a aplicação mais crítica recai sobre o encaixe e as zonas de contacto, onde a geometria capturada é submetida a processos de retificação (diferenças propositadas entre o corpo e o dispositivo) e, depois, validada por critérios de conforto e de interface. A literatura é explícita ao considerar a captura dimensional/geométrica do coto como etapa decisiva para a qualidade do encaixe ([Kannenberg et al., 2024](#ref-kannenberg-2024); [Young et al., 2023](#ref-young-2023)).

### Evidência por tipo de dispositivo

Embora os princípios sejam transversais, a literatura evidencia diferenças por tipo de dispositivo:

– Encaixes protésicos e ortóteses: forte ênfase na digitalização 3D, na análise quantitativa de malhas e na validação por meio de métricas de interface e/ou de simulação (FEA). Em workflows digitais de fabrico, verificam-se diferenças geométricas relevantes entre soluções manuais e digitais, reforçando que “digitalizar” não se limita a mudar de formato, mas também a alterar o resultado do ajuste final ([Kannenberg et al., 2024](#ref-kannenberg-2024); [Silva et al., 2024](#ref-silva-2024)). – Próteses de membro superior: coexistência de CT, scanners comerciais e fotogrametria como métodos de captura; estudos comparativos indicam que medições obtidas por 3D scanning podem ser fiáveis e repetíveis face a métodos tradicionais quando bem implementadas. Há também destaque para pipelines automatizados que adaptam modelos CAD inteligentes a dados de digitalização, encurtando o intervalo entre a captura e a obtenção de um modelo pronto para fabricação ([Chainando et al., 2025](#ref-chainando-2025); [Çıklaçandır et al., 2022](#ref-cklacandr-2022)). – Produtos de assistência definidos por zonas de alcance funcional (ex.: cadeiras de rodas e acessórios): a antropometria é frequentemente operacionalizada como critério de posicionamento e de acessibilidade, com mapeamentos de alcance e critérios percentílicos.

### Limitações, lacunas e recomendações

Apesar do avanço metodológico, a literatura identifica limitações consistentes: amostras pequenas em estudos aplicados, inconsistência no registo das etapas de retificação e de pós-processamento e falta de validação em contexto real e de longo prazo.

Um problema estrutural particularmente relevante para o design inclusivo é a escassez de bases de dados antropométricas normalizadas para pessoas com deficiência, o que dificulta estimativas de acomodação e pode perpetuar desajustes de design em populações sub-representadas ([Bradtmiller, 2022](#ref-bradtmiller-2022)).

Como orientação prática, emergem recomendações claras: selecionar o método de medição em função da questão de design (captura de forma, monitorização de volume, validação de interface), garantir a repetibilidade através de posturas e de uma marcação consistente dos pontos de referência anatómicos, e utilizar bases de dados antropométricas alinhadas com a população-alvo quando se pretende definir critérios de acomodação e ajuste ([ASTM International, 2024](#ref-astm-international-2024); [Ibrahim et al., 2024](#ref-ibrahim-2024)).

Acresce a recomendação de distinguir o ajuste estático (em posturas padronizadas) do ajuste dinâmico (durante a amplitude de movimento funcional), reconhecendo que ajuste e conforto são conceitos relacionados, mas não equivalentes ([ASTM International, 2024](#ref-astm-international-2024)).

### Estruturação de dados

A antropometria aplicada ao design protésico evoluiu para um paradigma digital centrado na captura e na interpretação tridimensionais, complementado por métricas de interface que aproximam a medição do desempenho real de uso. Esta abordagem permite maior precisão na personalização, na integração com CAD, na parametrização e no fabrico aditivo, abrindo caminho para fluxos de adaptação parcialmente automatizados. Contudo, a consolidação destas práticas exige procedimentos mais padronizados, amostras mais amplas e bases de dados antropométricas representativas, para que a personalização não dependa apenas da capacidade tecnológica, mas também de evidências robustas, rastreáveis e acessíveis ([Bradtmiller, 2022](#ref-bradtmiller-2022); [Sunderland et al., 2024](#ref-sunderland-2024)).

No contexto desta investigação, esta necessidade foi operacionalizada através da construção de uma base local consolidada de medidas da mão e do membro superior distal. A descrição detalhada da seleção das fontes, da extração dos valores, da normalização dos dados e da sua tradução para parâmetros de projeto é retomada no Capítulo 4, onde esses dados deixam de funcionar apenas como enquadramento teórico e passam a integrar a metodologia de desenvolvimento do modelo paramétrico.

### 2.5 Inteligência Artificial no processo de design

A integração de Inteligência Artificial (IA) no design tornou-se um tema central não apenas pelo surgimento de novas ferramentas, mas também por ter alterado a forma como se concebe a relação entre criatividade, análise, decisão e automatização. Contudo, a rápida disseminação do termo “IA” também gerou alguma imprecisão conceptual. Em muitos contextos, a mesma designação é usada para sistemas de previsão, algoritmos de otimização, modelos generativos e interfaces conversacionais, apesar desses mecanismos terem funções e modos de operação distintos. Numa dissertação de Design Industrial, importa por isso começar por uma clarificação introdutória: o objetivo desta secção é explicar, de forma acessível, o que é a IA, como funciona em termos gerais, que formas assume no design e porque razão deve ser entendida como instrumento assistivo, e não como substituto autónomo do designer ([Choudhury et al., 2025](#ref-choudhury-2025); [Saeidnia & Ausloos, 2024](#ref-saeidnia-2024); [Yüksel et al., 2023](#ref-yuksel-2023)).

Para efeitos de enquadramento, a Figura 2.6 é útil porque mostra a IA não como um bloco monolítico, mas como uma camada integrada num fluxo CAD mais amplo, em que a recolha de dados, a modelação, a otimização e a avaliação permanecem articuladas com a decisão projetual.

![](./figuras/ch2aidrivencomputeraideddesigncadfigure1p6.png)

Figura 2.6 — Enquadramento de um fluxo de CAD assistido por IA para desenvolvimento de produto.

Fonte original (APA 7): Menaka, S., Raja, A. W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s).

### O que é a Inteligência Artificial

De forma ampla, a IA pode ser entendida como um conjunto de métodos computacionais orientados a executar tarefas que requerem aprendizagem, reconhecimento de padrões, inferência ou geração de respostas com base em dados. Esta definição é útil porque evita tratar a IA como uma entidade única ou um sinônimo de inteligência humana generalizada. O que caracteriza a maioria dos sistemas atuais não é uma capacidade abstrata de “pensar” em qualquer domínio, mas a aptidão para operar sobre tipos específicos de problemas a partir de exemplos, regularidades e relações estatísticas aprendidas durante o treino ([Choudhury et al., 2025](#ref-choudhury-2025); [Yüksel et al., 2023](#ref-yuksel-2023)).

Dentro deste campo, a aprendizagem automática designa as abordagens em que o sistema aprende a partir de dados, em vez de depender exclusivamente de regras explicitamente escritas. A aprendizagem profunda corresponde a um subconjunto desta família e baseia-se em redes neuronais artificiais com múltiplas camadas, particularmente adequadas para tratar dados complexos, como imagens, texto ou som. Já a IA generativa refere-se a modelos capazes de produzir novos conteúdos — por exemplo, texto, imagens, composições formais ou variantes de projeto — com base nos padrões que aprenderam. Esta distinção é particularmente importante para o design, pois diferentes tipos de IA apoiam diferentes tipos de tarefas: algumas ajudam a analisar, outras a prever, outras a otimizar e outras ainda a gerar alternativas ([Khanolkar et al., 2023](#ref-khanolkar-2023); [Krahe et al., 2020](#ref-krahe-2020); [Li et al., 2021](#ref-li-2021)).

### Como funciona: dados, treino, inferência e geração

O funcionamento básico da maioria dos sistemas atuais de IA pode ser explicado em quatro etapas: dados, treino, inferência e, em certos casos, geração. Em primeiro lugar, o sistema necessita de dados de entrada, isto é, exemplos a partir dos quais possa aprender padrões. Em segundo lugar, durante o treino, o modelo ajusta os seus parâmetros internos para captar padrões recorrentes nos dados. Em terceiro lugar, após o treinamento, o modelo passa a realizar inferência, produzindo previsões, classificações, recomendações ou respostas a novos casos. Em modelos generativos, há ainda um quarto momento: a produção de novos conteúdos compatíveis com os padrões aprendidos, em vez de simples classificação ou previsão ([Ao et al., 2025](#ref-ao-2025); [Menaka et al., 2025](#ref-menaka-2025); [Panchal et al., 2019](#ref-panchal-2019)).

Esta lógica distingue a IA contemporânea dos sistemas puramente baseados em regras. Num sistema baseado em regras, o comportamento é prescrito antecipadamente: se ocorrer determinada condição, executa-se determinada ação. Num sistema treinado com dados, pelo contrário, o comportamento emerge da exposição a exemplos. Esta diferença ajuda a explicar, simultaneamente, a sua força e a sua fragilidade. A força reside na capacidade de lidar com grande complexidade, variabilidade e volume de informação. A fragilidade reside no facto do sistema depender dos dados com que foi treinado, podendo reproduzir enviesamentos, simplificações e erros já presentes nesses dados ([Panchal et al., 2019](#ref-panchal-2019); [Yüksel et al., 2023](#ref-yuksel-2023)).

Nos modelos generativos, este processo torna-se particularmente visível. O sistema aprende distribuições de forma, linguagem, composição ou estilo e, a partir daí, produz novas saídas em resposta a condições ou prompts. Isto permite criar imagens, textos ou alternativas formais que não existiam previamente naquela forma exata, mas também significa que o resultado pode ser apenas plausível, e não necessariamente adequado, original ou tecnicamente robusto. Para o design, esta distinção é decisiva: gerar muitas alternativas não equivale a resolver bem o problema de projeto ([Burnap et al., 2019](#ref-burnap-2019); [Choudhury et al., 2025](#ref-choudhury-2025); [Li et al., 2021](#ref-li-2021)).

### Formas de IA mais relevantes para o design

A literatura identifica várias famílias de aplicações da IA com relevância direta para o design. Uma primeira família é a do apoio à decisão, na qual sistemas analíticos ajudam a interpretar grandes volumes de informação, a comparar alternativas e a reduzir a carga cognitiva em problemas multivariados. Uma segunda é a otimização, particularmente importante na engenharia de produto, na parametrização e no fabrico, na qual algoritmos exploram combinações possíveis e sugerem soluções com melhor desempenho estrutural, funcional ou produtivo. Uma terceira é a visão por computador, usada quando o sistema precisa interpretar imagens, formas ou padrões visuais. Uma quarta é o processamento de linguagem natural, que permite interagir com sistemas complexos por meio de descrições semânticas, em vez de comandos técnicos rígidos. Finalmente, a quinta família, hoje mais visível, corresponde aos sistemas generativos capazes de produzir texto, imagem, forma ou variantes de projeto em resposta a condições de entrada ([Ao et al., 2025](#ref-ao-2025); [Khanolkar et al., 2023](#ref-khanolkar-2023); [Wang & Hu, 2024](#ref-wang-2024)).

Para o Design Industrial, estas famílias não têm exatamente o mesmo peso. A IA generativa tornou-se especialmente relevante na ideação, na comunicação visual e na rápida exploração de alternativas. A otimização e os modelos preditivos assumem maior importância quando o problema envolve desempenho, simulação, restrições de fabrico ou espaços paramétricos amplos. Já o processamento de linguagem natural ganha interesse crescente enquanto camada de acesso a sistemas mais complexos, sobretudo quando se pretende que utilizadores menos especializados consigam formular intenções ou restrições sem depender de software CAD avançado ou de uma sintaxe demasiado técnica ([Ao et al., 2025](#ref-ao-2025); [Menaka et al., 2025](#ref-menaka-2025); [Wang & Hu, 2024](#ref-wang-2024)).

### IA ao longo do processo de design

Uma das conclusões mais consistentes da literatura é que a IA não atua apenas numa fase isolada do processo projetual. Nas fases iniciais, pode apoiar a pesquisa, a síntese de informação e o enquadramento do problema, ajudando a identificar padrões nas necessidades dos utilizadores, tendências, dados de mercado ou requisitos de contexto. Na ideação, pode ampliar o espaço de procura, reduzir fixação prematura e produzir rapidamente múltiplas alternativas de partida. No desenvolvimento, pode acelerar a iteração, gerar variantes paramétricas e articular a exploração formal às restrições técnicas. Em fases posteriores, pode apoiar a prototipagem, a simulação, a previsão de desempenho e a comparação entre opções concorrentes. Também pode reforçar a comunicação e a documentação, produzindo representações mais rápidas de cenários, conceitos e soluções ([Khanolkar et al., 2023](#ref-khanolkar-2023); [Saeidnia & Ausloos, 2024](#ref-saeidnia-2024); [Verganti et al., 2020](#ref-verganti-2020)).

Isto não significa, porém, que a IA seja igualmente eficaz em todas as etapas. A literatura sugere que seu valor tende a ser maior em tarefas de exploração divergente, análise extensiva e automatização parcial, enquanto as etapas de convergência, enquadramento contextual, decisão ética e validação final continuam a depender fortemente do julgamento humano. A IA pode ampliar o que é possível explorar e tornar mais rápida a comparação entre alternativas, mas não elimina a necessidade de decidir o que faz sentido desenvolver, para quem, em que contexto e com que consequências ([Ao et al., 2025](#ref-ao-2025); [Choudhury et al., 2025](#ref-choudhury-2025); [Virós-i-Martin & Selva, 2021](#ref-viros-i-martin-2021)).

### Papel do designer, riscos e necessidade de supervisão humana

Neste quadro, a questão central deixa de ser se a IA substitui o designer e passa a ser como ela redistribui a agência no processo de projeto. A literatura descreve uma deslocação do designer, enquanto gerador exclusivo de forma, para um papel mais híbrido de orientador, curador, intérprete e decisor estratégico. Em vez de desaparecer, o papel humano torna-se mais exigente em tarefas como a formulação do problema, a definição de critérios, a leitura contextual, a seleção entre alternativas e a justificação das decisões. Esta transformação é particularmente relevante em domínios sensíveis, onde a adequação ao utilizador, a responsabilidade técnica e a aceitabilidade ética não podem ser delegadas a um sistema treinado apenas com dados passados ([Figoli et al., 2022](#ref-figoli-2022); [Kadenhe et al., 2025](#ref-kadenhe-2025); [Virós-i-Martin & Selva, 2021](#ref-viros-i-martin-2021)).

É também neste ponto que emergem os principais riscos. Um primeiro risco é o enviesamento, já que modelos treinados com dados históricos ou desequilibrados podem reproduzir exclusões, preferências dominantes e padrões culturais pouco representativos. Um segundo risco é a opacidade: muitos sistemas produzem resultados eficazes, mas são difíceis de explicar em termos do seu raciocínio interno, o que dificulta a confiança e a responsabilização. Um terceiro risco é o erro, incluindo respostas plausíveis, mas incorretas, simplificações abusivas e sugestões sem robustez técnica suficiente. A estes somam-se riscos de dependência excessiva, homogeneização formal, enfraquecimento de competências críticas e incerteza quanto à autoria e originalidade dos resultados produzidos com assistência algorítmica ([Burnap et al., 2019](#ref-burnap-2019); [Panchal et al., 2019](#ref-panchal-2019); [Yüksel et al., 2023](#ref-yuksel-2023)).

Por estas razões, a literatura converge para a defesa de modelos com supervisão humana explícita. A integração mais robusta da IA não assenta em autonomia plena, mas em ciclos assistidos, em que o sistema acelera a análise, a geração ou a previsão e o humano mantém autoridade sobre critérios, validação e consequências da decisão. Em termos práticos, isto implica preservar mecanismos de controlo, a comparação entre alternativas, a explicitação de limites, a verificação técnica e a capacidade de recusar ou reformular sugestões produzidas pela máquina. Em design, a supervisão humana não é um complemento opcional; é a condição que transforma a IA em instrumento projetual e não em fonte acrítica de soluções aparentes ([Ao et al., 2025](#ref-ao-2025); [Kadenhe et al., 2025](#ref-kadenhe-2025); [Verganti et al., 2020](#ref-verganti-2020)).

### Síntese

Em síntese, a IA pode ser compreendida como um conjunto de métodos computacionais baseados em dados, capazes de aprender padrões, apoiar a inferência, gerar conteúdo e acelerar tarefas distribuídas ao longo de várias fases do processo de design. A sua relevância para o Design Industrial decorre menos de uma promessa de substituir a criatividade humana do que da sua capacidade de ampliar a exploração, apoiar a avaliação e tornar operáveis espaços de decisão mais complexos. O seu valor depende, contudo, do enquadramento: quanto mais o sistema exige interpretação contextual, sensibilidade humana, responsabilidade ética ou validação técnica, mais importante se torna o papel do designer como agente de mediação e controlo ([Choudhury et al., 2025](#ref-choudhury-2025); [Saeidnia & Ausloos, 2024](#ref-saeidnia-2024); [Verganti et al., 2020](#ref-verganti-2020)).

No âmbito desta investigação, esta leitura é decisiva porque legitima a integração da IA como camada assistiva à parametrização, e não como instância autónoma de projeto. Para sistemas orientados à personalização, à adaptação anatómica e ao apoio à decisão, a IA é mais útil quando ajuda a organizar alternativas, interpretar relações complexas e apoiar escolhas em espaços paramétricos amplos, preservando sempre a validação técnica, a rastreabilidade e a supervisão humana ao longo do processo ([Ao et al., 2025](#ref-ao-2025); [Menaka et al., 2025](#ref-menaka-2025); [Wang & Hu, 2024](#ref-wang-2024)).

### 2.6 Plataformas digitais e sistemas configuráveis

A evolução recente do desenvolvimento de produto, particularmente em contextos de saúde e de tecnologias de apoio, tem sido acompanhada de um crescimento de plataformas digitais configuráveis e de sistemas participativos orientados à personalização. A literatura caracteriza estes sistemas como infraestruturas sociotécnicas que articulam enquadramentos conceptuais que legitimam e estruturam a participação, mecanismos técnicos de configurabilidade, como configuradores, parametrização e modularidade, e workflows participativos que traduzem experiência vivida em requisitos, protótipos e iterações de projeto ([Fischer et al., 2004](#ref-fischer-2004); [Hippel & Katz, 2002](#ref-hippel-2002); [Howard et al., 2022](#ref-howard-2022)).

Em domínios como a reabilitação e as tecnologias assistivas, a personalização é frequentemente descrita como uma necessidade funcional, e não apenas como uma diferenciação de mercado. Isso significa que a adequação do produto ao utilizador pode ser determinante para a segurança, a usabilidade e a adoção sustentada, deslocando o foco do design de uma solução “média” para sistemas capazes de acomodar a variabilidade individual de forma controlada ([Fischer et al., 2017](#ref-fischer-2017); [Kerr et al., 2024](#ref-kerr-2024); [Zhu & Zhong, 2022](#ref-zhu-2022)).

### Fundamentos conceptuais: toolkits, meta-design e end-user development.

Uma linha teórica relevante é a dos “toolkits for user innovation”, que entende os sistemas configuráveis como ferramentas coordenadas e acessíveis que transferem parte do trabalho de design relacionado com as necessidades dos utilizadores, enquanto fabricantes e especialistas retêm tarefas de resolução e de produção. A distinção entre configuradores, centrados em selecionar opções, e toolkits, centrados em desenhar dentro de um espaço de projeto delimitado, é central: a participação pode variar entre escolher alternativas pré-definidas e efetivamente criar configurações em um ambiente com regras e feedback ([Franke & Hippel, 2002](#ref-franke-2002); [Hippel & Katz, 2002](#ref-hippel-2002)).

O meta-design aprofunda esta lógica ao defender a participação “em uso”, estabelecendo condições técnicas e sociais para que os utilizadores se tornem co-designers e o sistema evolua ao longo do tempo. O modelo Seeding, Evolutionary Growth, and Reseeding formaliza este processo como alternância entre “sementes” iniciais, criadas por especialistas, evolução por meio do desenvolvimento do utilizador e reestruturações periódicas que consolidam as aprendizagens e reorganizam o sistema ([Costabile et al., 2007](#ref-costabile-2007); [Fischer et al., 2004](#ref-fischer-2004)).

Para enquadrar estes fundamentos de forma mais operacional, a Figura 2.7 mostra um modelo de configuração da participação em living labs, útil porque desloca a discussão da participação como princípio abstrato para a participação como estrutura desenhável.

![](./figuras/ch2aframeworkforconfiguringparticifigure1p4.png)

Figura 2.7 — Modelo de processo para configurar participação em ecossistemas de inovação e cocriação.

Fonte original (APA 7): Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488

A literatura identifica, contudo, riscos como a participation overload, isto é, a transferência excessiva de carga de trabalho e de decisão para os utilizadores, o que requer mecanismos de apoio, curadoria e reutilização para tornar a participação sustentável ([Fischer et al., 2017](#ref-fischer-2017)).

Em paralelo, o conceito de Software Shaping Workshop operacionaliza o meta-design como um “workshop virtual” composto por ferramentas familiares adaptadas à cultura e às competências de uma comunidade. Em contextos de reabilitação e assistência, este paradigma manifesta-se em sistemas que fornecem a cuidadores e terapeutas interfaces do tipo editor, permitindo adaptar scripts, exercícios e conteúdos sem necessidade de programação, respondendo de forma pragmática às necessidades de personalização ([Costabile et al., 2007](#ref-costabile-2007); [Fischer et al., 2017](#ref-fischer-2017)).

Esta transição entre princípio e operação pode ser resumida pelos elementos nucleares apresentados na Tabela 2.2, que sistematiza dimensões recorrentes no desenho de participação mediada: quando participar, quem participa, por quais canais, através de quais pontos de contacto e com que mecanismos de motivação.

Tabela 2.2 — Elementos centrais na configuração da participação em sistemas configuráveis

| Fase e propósito    | Em que momento participa o utilizador e com que objetivo            |
| ------------------- | ------------------------------------------------------------------- |
| Participantes       | Que perfis participam, em que número e com que papel                |
| Formato             | Que canais, espaços e métodos suportam a colaboração                |
| Contacto            | Como se recrutam participantes e como se mantém a relação           |
| Gestão da motivação | Que fatores promovem adesão e que barreiras dificultam continuidade |

Fonte adaptada. Referência original (APA 7): Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488

### Mecanismos de personalização: modularidade, parametrização e tailoring

A literatura sintetiza a personalização por meio de mecanismos recorrentes que diferem quanto a “quem configura”, “o que é configurável” e “quando se configura”. Três mecanismos destacam-se pela relevância para sistemas protésicos e dispositivos médicos personalizados:

1. Seleção modular de componentes: a personalização é obtida por meio da combinação de módulos interoperáveis, permitindo adaptar a funcionalidade por meio de combinações e substituições. A modularidade surge como estratégia para conciliar personalização, reutilização e escalabilidade em ecossistemas de produto ([Dechev et al., 2023](#ref-dechev-2023); [Peters & Richter, 2023](#ref-peters-2023)).

2. Configuração paramétrica: o utilizador, ou um intermediário clínico, fornece entradas num espaço de parâmetros e o sistema gera automaticamente artefactos de design, como ficheiros CAD, com base nesses valores. Este mecanismo é mais adequado quando a personalização depende de atributos mensuráveis, ligando diretamente dados antropométricos e cinemáticos a variáveis de projeto ([Kuhl et al., 2020](#ref-kuhl-2020); [Zhu & Zhong, 2022](#ref-zhu-2022)).

3. Tailoring por toolkit/editor: a personalização ocorre em tempo de uso, permitindo editar conteúdos, instruções, rotinas de treino ou componentes informacionais associados ao produto ou serviço. Em saúde, este mecanismo é particularmente relevante em plataformas de reabilitação e de telereabilitação, nas quais a adaptação de exercícios e de objetivos faz parte do cuidado contínuo ([Cole, 2011](#ref-cole-2011); [Fischer et al., 2017](#ref-fischer-2017)).

A seleção do mecanismo mais adequado depende do locus de conhecimento: modularidade funciona quando as necessidades podem ser expressas como combinações de módulos conhecidos; parametrização é mais eficaz quando há dados mensuráveis que podem ser mapeados para variáveis de design; e toolkits são indicados quando a adaptação contínua em contexto é crítica e quando o utilizador ou intermediário tem conhecimento situado para ajustar o sistema ([Hippel & Katz, 2002](#ref-hippel-2002); [Peters & Richter, 2023](#ref-peters-2023); [Zhu & Zhong, 2022](#ref-zhu-2022)).

### Workflows participativos e infraestruturas remotas

Uma característica transversal é o recurso crescente à participação remota e aos workflows digitalmente mediados. A literatura documenta sessões de co-design por videoconferência, workshops online e processos de co-manufactura à distância, em que o ciclo “definir → prototipar → fabricar → testar” ocorre com envio de protótipos para experimentação no contexto real do utilizador. Estes modelos são particularmente relevantes em tecnologias assistivas, nas quais a avaliação em contexto e a adaptação iterativa são determinantes para a adequação funcional e a aceitação ([Dexter et al., 2013](#ref-dexter-2013); [Thorsen et al., 2023](#ref-thorsen-2023)).

No entanto, as fontes sublinham que a tecnologia não é suficiente. A eficácia destes sistemas depende de governance, isto é, de quem decide o quê e quando, de mediação por clínicos, designers ou técnicos, e de mecanismos de gestão da carga de trabalho e da comunicação. Em modelos abertos e distribuídos, surgem riscos de quebra de compromissos e de atrasos decorrentes da falta de accountability, o que exige o desenho explícito de regras, expectativas e responsabilidades ([Frangos et al., 2016](#ref-frangos-2016); [Hussaini et al., 2023](#ref-hussaini-2023); [Kerr et al., 2024](#ref-kerr-2024)).

### Aplicações em saúde, reabilitação e próteses

Em saúde, plataformas baseadas em digital twins são descritas como sistemas de serviço personalizados que conectam participantes por meio da nuvem, integrando sensores, parâmetros de movimento e métricas de desempenho. Embora apresentem correlações elevadas em cenários controlados, a literatura assinala degradação de desempenho em contextos mais complexos, revelando limites entre modelos e a variabilidade real do movimento humano. Estes sistemas mostram o potencial de integrar personalização, fabrico digital e monitorização remota, mas também deixam claro que a robustez do modelo depende da qualidade dos dados e da diversidade dos cenários de uso ([Mikołajewski et al., 2023](#ref-mikoajewski-2023); [Zhu & Zhong, 2022](#ref-zhu-2022)).

Na reabilitação, plataformas de virtual coaching, serious games configuráveis e modelos de cocriação tecnológica são apresentados como formas de personalizar os tratamentos com base no estado clínico, nos objetivos terapêuticos e no feedback do utilizador. As avaliações indicam boa usabilidade e experiência do utilizador quando a participação é integrada no ciclo de desenvolvimento e mostram que a personalização não se limita à interface, estendendo-se à seleção de exercícios, ao ritmo do programa e à mediação por profissionais de saúde ([Cole, 2011](#ref-cole-2011); [Kerr et al., 2024](#ref-kerr-2024); [Seregni et al., 2021](#ref-seregni-2021)).

No contexto protésico e assistivo, evidencia-se a relevância dos ecossistemas modulares e das cadeias de aprendizagem distribuída. Estudos sobre próteses pediátricas, serviços de reabilitação assistiva e modelos como o Victoria Hand Project mostram que a personalização pode combinar prototipagem iterativa, módulos intercambiáveis, criação digital de encaixes e circulação de feedback entre locais clínicos e equipas centrais de desenvolvimento. Neste enquadramento, a plataforma deixa de ser apenas uma interface de configuração e passa a funcionar como infraestrutura organizacional de aprendizagem e de atualização contínua ([Dechev et al., 2023](#ref-dechev-2023); [Howard et al., 2022](#ref-howard-2022); [Sims et al., 2017](#ref-sims-2017)).

Em contextos de baixos recursos, a literatura reforça que a impressão 3D pode ser um facilitador importante, mas só produz benefícios quando integrada a infraestruturas de apoio, confiança, manutenção e capacitação técnica. A simples disponibilização de tecnologia de fabrico não garante soluções adequadas nem adoção sustentada, pelo que os modelos participativos e a mediação local assumem um papel determinante na tradução do potencial técnico em valor real para os utilizadores ([Hussaini et al., 2023](#ref-hussaini-2023); [Thorsen et al., 2023](#ref-thorsen-2023)).

### Limitações e lacunas: sustentabilidade, adoção e equilíbrio entre standardização e improviso

Apesar do potencial, a evidência empírica frequentemente baseia-se em amostras pequenas e em estudos de caso, o que limita a generalização. Para além disso, surgem três tensões estruturais ([Frangos et al., 2016](#ref-frangos-2016); [Howard et al., 2022](#ref-howard-2022); [Thorsen et al., 2023](#ref-thorsen-2023)):

– Sustentabilidade da participação: risco de sobrecarga de participação e de desistência; necessidade de mecanismos de apoio, curadoria e redistribuição da carga entre utilizadores e especialistas ([Fischer et al., 2017](#ref-fischer-2017)).

– Standardização vs personalização: em domínios regulados, a personalização deve manter rastreabilidade, segurança e qualidade, o que pode colidir com improvisos locais necessários para responder a necessidades idiossincráticas ([Costabile et al., 2007](#ref-costabile-2007); [Fischer et al., 2004](#ref-fischer-2004)).

– Adoção e valor realizado: a literatura sobre personalização em massa regista falhas frequentes na conversão e na adoção de configuradores; por analogia, em saúde e tecnologias assistivas, a configurabilidade não garante aceitação sem alinhamento com expectativas, confiança e integração nos serviços ([Akasaka et al., 2022](#ref-akasaka-2022); [Frangos et al., 2016](#ref-frangos-2016)).

### 2.7 Análise crítica do estado da arte e lacunas identificadas![Shape][image1]

A transição entre o entusiasmo técnico e a maturidade efetiva do campo torna-se particularmente visível ao se observarem os níveis de prontidão tecnológica na literatura. A Figura 2.8 antecipa esta leitura ao mostrar a distribuição dos estudos por technology readiness level (TRL), reforçando que muitos contributos permanecem concentrados em fases ainda distantes de adoção ampla e sustentada.

![](./figuras/ch2ascopingreviewofdigitalfabricafigure10p9.png)

Figura 2.8 — Distribuição dos estudos por nível de prontidão tecnológica (TRL) em próteses e ortóteses com fabrico digital.

Fonte original (APA 7): Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517

A síntese das secções anteriores evidencia um panorama marcado por avanços técnicos significativos, mas também por limitações estruturais persistentes na investigação e no desenvolvimento de próteses e de tecnologias assistivas. Um tema transversal é o desfasamento entre inovação tecnológica e evidência robusta: muitos desenvolvimentos permanecem em fase de protótipo, testados em amostras reduzidas e por períodos curtos, com escassa validação por meio de ensaios clínicos, estudos longitudinais e avaliações em contextos reais ([Chadwell et al., 2020](#ref-chadwell-2020); [Samuelsson et al., 2012](#ref-samuelsson-2012); [Windrich et al., 2016](#ref-windrich-2016)).

Este padrão enfraquece a capacidade de comparar soluções, generalizar conclusões e traduzir melhorias laboratoriais em benefícios consistentes na vida quotidiana ([Hafner & Sawers, 2016](#ref-hafner-2016); [Samuelsson et al., 2012](#ref-samuelsson-2012)).

### Lacuna 1 — Evidência insuficiente e fraca tradução para o mundo real

A revisão de literatura aponta repetidamente a ausência de estudos comparativos robustos e de ensaios clínicos que confrontem dispositivos avançados com prescrições convencionais, particularmente em sistemas ativos e externamente alimentados. Em vários subdomínios, observa-se dependência de protótipos e de pequenas amostras, o que limita as inferências sobre eficácia, segurança e valor clínico. Em paralelo, verifica-se predominância de avaliações em laboratório e de tarefas pouco representativas, que não captam adequadamente o desempenho em ambientes naturais, com variabilidade de contextos, objetos e exigências funcionais ([Ghillebert et al., 2019](#ref-ghillebert-2019); [Samuelsson et al., 2012](#ref-samuelsson-2012); [Windrich et al., 2016](#ref-windrich-2016)).

Esta lacuna é particularmente relevante porque a adaptação, a aprendizagem e o abandono de próteses ocorrem ao longo do tempo e em ecossistemas reais, como o trabalho, a casa e o espaço público. Quando a evidência se baseia em janelas de observação curtas, torna-se difícil compreender trajetórias de adoção, padrões de uso e emergências de problemas de conforto ou de manutenção ([Chadwell et al., 2020](#ref-chadwell-2020); [Samuelsson et al., 2012](#ref-samuelsson-2012)).

### Lacuna 2 — Desalinhamento entre necessidades identificadas, métricas objetivas, e qualidade de vida

Um problema recorrente é a ligação frágil entre aquilo que os utilizadores referem como necessidades — como conforto, controlo intuitivo, aparência e participação social —, os indicadores objetivos habitualmente medidos — como desempenho em testes funcionais, parâmetros biomecânicos e contagens de atividade  —, e os resultados finais desejáveis — como autonomia e qualidade de vida. Revisões salientam que as necessidades são contextuais e interdependentes e que as medições laboratoriais podem não refletir tarefas relevantes do quotidiano, contribuindo para contradições entre resultados subjetivos e objetivos ([Cordella et al., 2016](#ref-cordella-2016); [Manz et al., 2022](#ref-manz-2022)).

Esta desconexão tem implicações diretas no design: sem métricas ecologicamente válidas e sensíveis às prioridades do utilizador, torna-se difícil orientar decisões de projeto para benefícios significativos e sustentados, podendo ocorrer “melhorias técnicas” que não se traduzem em aceitação ou uso continuado ([Manz et al., 2022](#ref-manz-2022); [Samuelsson et al., 2012](#ref-samuelsson-2012)).

### Lacuna 3 — Persistência de problemas na interface corpo–dispositivo e na personalização

Apesar do progresso em componentes e controlo, a literatura converge para a identificação da interface corpo–dispositivo como um ponto crítico ainda não resolvido. Problemas de ajuste, desconforto, irritação cutânea e dificuldades de adaptação persistem como fatores determinantes de insatisfação e de abandono. Nas revisões, a personalização é frequentemente descrita como insuficiente ou metodologicamente frágil, com evidência difícil de sintetizar devido à variabilidade das intervenções e ao registo incompleto ([Alluhydan et al., 2023](#ref-alluhydan-2023); [Baldock et al., 2023](#ref-baldock-2023); [Richardson & Dillon, 2017](#ref-richardson-2017)).

Um aspeto estruturante desta lacuna é a falta de pipelines “medição → decisão de design → validação” consistentes e acessíveis, com dados objetivos suficientes para orientar ajustes individualizados. Mesmo quando se propõem soluções baseadas em sensores e na monitorização do uso, emergem barreiras práticas, como o custo, a autonomia da bateria, a disponibilidade e a formação, o que limita a adoção como prática clínica padrão ([Chadwell et al., 2020](#ref-chadwell-2020); [Richardson & Dillon, 2017](#ref-richardson-2017)).

### Lacuna 4 — Estagnação e fragilidade metodológica em controlo e interação humano–prótese

No caso das próteses de membro superior, algumas revisões caracterizam uma estagnação relativa nas estratégias de controlo em aplicações comerciais, com evolução lenta desde as primeiras abordagens do século XX. Persistem dificuldades de robustez e de transferibilidade entre cenários laboratoriais e o uso real, bem como desafios associados ao esforço cognitivo, ao tempo de aprendizagem e à inconsistência de desempenho em situações quotidianas ([Cordella et al., 2016](#ref-cordella-2016); [Marinelli et al., 2022](#ref-marinelli-2022)).

Esta lacuna não é apenas técnica: reflete também uma conceptualização insuficiente da interação humano–prótese como um sistema integrado, em que controlo, feedback, treino e contexto de uso devem ser co-otimizados ([Domínguez-Ruiz et al., 2023](#ref-dominguez-ruiz-2023); [Marinelli et al., 2022](#ref-marinelli-2022)).

### Lacuna 5 — Acesso, custo, manutenção e inequidades sistémicas

A acessibilidade surge como um constrangimento central e persistente, tanto em contextos de baixos recursos quanto em sistemas de saúde mais robustos. Revisões identificam barreiras associadas a custos elevados, à necessidade de formação especializada, a atrasos na prestação de cuidados e a pressões sistémicas que levam os utilizadores a negociar intensivamente para obter soluções adequadas. Em contextos de baixos e médios rendimentos, enfatizam-se ainda problemas de durabilidade e de manutenção, com trade-offs claros: soluções biomecanicamente mais sofisticadas podem ser mais frágeis e difíceis de manter, comprometendo a sustentabilidade do uso ([Alluhydan et al., 2023](#ref-alluhydan-2023); [Andrysek, 2010](#ref-andrysek-2010); [Baumann & Maria, 2023](#ref-baumann-2023)).

Assim, a inovação pode agravar as inequidades ao introduzir dependências de infraestrutura, de apoio técnico e de cadeias de fornecimento indisponíveis para uma parcela significativa da população ([Andrysek, 2010](#ref-andrysek-2010); [Segura et al., 2024](#ref-segura-2024)).

### Lacuna 6 — Envolvimento do utilizador e registo metodológico insuficiente

O envolvimento do utilizador é descrito como um problema metodológico e ético ainda não resolvido. Revisões relacionam explicitamente processos pouco patient-tailored ao abandono e à incapacidade de responder às necessidades relevantes. Em várias áreas, identifica-se a ausência de métodos qualitativos sistemáticos para captar a experiência e a aceitabilidade, mesmo em componentes centrados no conforto, como liners, o que limita a compreensão profunda dos fatores de uso e de rejeição ([Marinelli et al., 2022](#ref-marinelli-2022); [Richardson & Dillon, 2017](#ref-richardson-2017); [Walker et al., 2019](#ref-walker-2019)).

Adicionalmente, a heterogeneidade de métodos e a falta de critérios comuns de avaliação, como escalas partilhadas de utilidade e satisfação, dificultam a síntese e as meta-análises, mantendo o campo fragmentado e com baixa comparabilidade ([Cordella et al., 2016](#ref-cordella-2016); [Hafner & Sawers, 2016](#ref-hafner-2016); [Richardson & Dillon, 2017](#ref-richardson-2017)).

### Implicações para esta investigação

Em conjunto, estas lacunas apontam para a necessidade de abordagens que:

1. reforcem a ligação entre personalização e evidência, com pipelines integrados de aquisição de dados, geração de variantes e validação;

2. privilegiem avaliação ecologicamente válida e longitudinal, aproximando métricas de resultados de participação e qualidade de vida;

3. tratem a interface corpo–dispositivo e o conforto como requisitos estruturantes, não como otimizações posteriores;

4. incorporem envolvimento do utilizador como elemento contínuo e reportável, articulando métodos qualitativos e quantitativos;

5. Considerem a acessibilidade, a manutenção e o contexto de serviço como parte do problema de design ([Anderson et al., 2024](#ref-anderson-2024); [Baumann & Maria, 2023](#ref-baumann-2023); [Chadwell et al., 2020](#ref-chadwell-2020)).

## Capítulo 3 — Metodologia de Investigação

### 3.1 Enquadramento metodológico e abordagem Research Through Design

A presente investigação inscreve-se numa metodologia de natureza aplicada, estruturada no enquadramento do Research Through Design (RTD). Esta abordagem reconhece o design não apenas como prática projetual, mas também como meio de produção de conhecimento, no qual conceber, experimentar, prototipar e refletir constituem simultaneamente atos de criação e de investigação ([Frayling, 1994](#ref-frayling-1994); [Zimmerman et al., 2007](#ref-zimmerman-2007)).

O objetivo principal do projeto é gerar conhecimento por meio da prática do design industrial, articulando o processo criativo, o desenvolvimento técnico e a reflexão crítica sobre o papel do design como mediador entre a tecnologia e a experiência humana. Neste contexto, propõe-se o desenvolvimento de um sistema de design paramétrico assistido por inteligência artificial para a criação de próteses personalizadas de membros superiores, explorando a interligação entre design industrial, design para a fabricação aditiva (DfAM) e metodologias de design inclusivo.

A pertinência da abordagem RTD justifica-se pela natureza exploratória e iterativa do problema em estudo. A personalização de próteses envolve variáveis anatómicas, funcionais, simbólicas e técnicas que dificilmente podem ser plenamente compreendidas apenas por via teórica. A produção de protótipos, a modelação paramétrica e a integração de algoritmos de apoio ao design constituem, neste projeto, instrumentos epistemológicos que permitem testar hipóteses, revelar constrangimentos e reformular decisões projetuais. Neste sentido, o artefacto não é entendido apenas como resultado final, mas como um veículo de investigação, tornando visíveis decisões, compromissos e relações entre requisitos que dificilmente emergiriam num modelo exclusivamente descritivo ou analítico ([Zimmerman et al., 2007](#ref-zimmerman-2007)).

A investigação é igualmente estruturada segundo a lógica processual do modelo Double Diamond, articulando momentos de divergência e de convergência nas fases de descoberta, definição, desenvolvimento e entrega. Esta estrutura não é aplicada de forma linear, mas como orientação para ciclos iterativos de exploração, síntese e validação, coerentes com a combinação entre pesquisa, formulação do problema, geração de alternativas, prototipagem e teste que caracteriza a prática do design contemporâneo ([Design Council, 2020](#ref-design-council-2020)).

### 3.2 O design industrial como prática investigativa

O projeto parte do entendimento do design industrial como disciplina projetual, técnica e social, capaz de mediar entre a inovação tecnológica e a experiência humana. No domínio das próteses de membros superiores, esta mediação assume particular relevância, dado que o objeto projetado intervém diretamente na corporeidade, na autonomia e na identidade do utilizador. Esta perspetiva aproxima-se da ideia de designerly ways of knowing, segundo a qual o design possui modos próprios de formular problemas, produzir conhecimento e articular exigências funcionais, formais e humanas ([Cross, 1982](#ref-cross-1982)).

A produção contemporânea de próteses personalizadas continua a enfrentar desafios significativos, nomeadamente custos elevados, processos de adaptação pouco flexíveis, dependência de técnicos especializados e dificuldades de escalabilidade. Embora a impressão 3D tenha contribuído para a democratização parcial do fabrico de dispositivos de apoio, persistem limitações na personalização anatómica rigorosa, na reprodutibilidade dos processos e na integração sistemática de critérios ergonómicos e simbólicos.

Neste enquadramento, o design industrial é entendido como uma prática investigativa capaz de estruturar soluções que conciliem requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos. A investigação assume que o desenvolvimento de um sistema paramétrico assistido por inteligência artificial pode contribuir para superar abordagens baseadas em modelos estáticos e em ajustes empíricos, promovendo processos mais configuráveis, reprodutíveis e acessíveis. A dimensão investigativa não reside apenas na resolução do problema projetual, mas também na explicitação dos critérios, das relações paramétricas e dos mecanismos de decisão que tornam o processo analisável, criticável e transferível para outros contextos de desenvolvimento.

A hipótese principal sustenta que a integração de design paramétrico e de ferramentas de inteligência artificial permite desenvolver próteses mais adequadas às necessidades anatómicas e funcionais dos utilizadores, tornando o processo de personalização mais acessível e escalável, especialmente em contextos economicamente desfavorecidos. As hipóteses secundárias aprofundam esta perspetiva, sugerindo que a combinação de princípios de design inclusivo, DfAM e processos participativos pode melhorar a usabilidade, o conforto e a aceitação, ao mesmo tempo que reduz a dependência de especialistas.

### 3.3 Estrutura metodológica do projeto

A metodologia organiza-se em três fases interligadas — conceptual, metodológica e empírica — que se desenvolvem de forma sequencial, mantendo, contudo, a natureza iterativa própria do processo de design. Esta estrutura funciona como adaptação do enquadramento RTD a um problema de design de produto com forte componente digital e prototípica, preservando a alternância entre abertura exploratória e convergência decisional característica do Double Diamond ([Design Council, 2020](#ref-design-council-2020); [Zimmerman et al., 2007](#ref-zimmerman-2007)).

A fase conceptual corresponde ao momento de enquadramento teórico e de problematização. Neste estágio, procede-se à revisão crítica da literatura nas áreas de design paramétrico, fabrico aditivo, design inclusivo, antropometria aplicada e integração de inteligência artificial no processo de design. Paralelamente, realiza-se uma análise comparativa de soluções open-source existentes no domínio das próteses impressas em 3D, identificando abordagens formais, estruturais e tecnológicas, bem como limitações quanto à personalização e à reprodutibilidade. Foi também nesta fase que se estruturou uma base local consolidada de dados antropométricos da mão, a partir de medições publicadas e de bases de dados antropométricas, de modo a apoiar a definição dos parâmetros iniciais do sistema e a comparação entre perfis populacionais. O resultado desta fase é a consolidação de um quadro conceptual alinhado com as questões de investigação e com a hipótese central.

A fase metodológica corresponde à definição e implementação do sistema paramétrico assistido por IA. Nesta etapa especifica-se a arquitetura da plataforma digital, integrando módulos de configuração paramétrica, bases de dados antropométricas e algoritmos de apoio à interpretação de medidas e à otimização geométrica. Desenvolvem-se protótipos digitais iterativos, testando relações formais e funcionais e avaliando a viabilidade de fabrico segundo os princípios de DfAM. É nesta fase que a investigação se aproxima mais claramente de uma lógica de research by making, em que as decisões de modelação, parametrização e iteração constituem simultaneamente desenvolvimento técnico e produção de conhecimento metodológico.

A fase empírica materializa a operacionalização do conhecimento gerado. Os modelos paramétricos são testados com diferentes perfis antropométricos provenientes de bases de dados públicas, e protótipos físicos são produzidos por meio de impressão 3D. Esta fase permite avaliar a integridade estrutural, a montagem, a ajustabilidade e a coerência formal, bem como verificar a consistência do sistema perante variações dimensionais.

### 3.4 Métodos de recolha e análise de dados

A investigação recorre a métodos qualitativos e experimentais, coerentes com a natureza prática do RTD. A recolha de dados realiza-se em diferentes níveis, combinando análise documental, comparação de precedentes, construção paramétrica, prototipagem iterativa e reflexão crítica sobre os resultados de cada ciclo.

Num primeiro nível, procede-se à análise documental e à revisão da literatura, o que permite identificar lacunas, requisitos técnicos e critérios de avaliação. Num segundo nível, realiza-se a análise comparativa de projetos existentes, com foco nas suas soluções construtivas, nos sistemas de ajuste e nas estratégias de personalização.

Durante o desenvolvimento do sistema paramétrico, os dados assumem natureza técnica e projetual, incluindo parâmetros geométricos, relações dimensionais, tempos de fabrico, consumo de material e desempenho estrutural dos protótipos. Estes dados são analisados de forma iterativa, permitindo reformular o modelo paramétrico e otimizar o seu desempenho.

Na fase de prototipagem, a análise incide sobre os critérios de exequibilidade de fabrico, robustez estrutural, coerência dimensional e facilidade de montagem. Não são recolhidos dados pessoais ou biométricos de utilizadores reais; utilizam-se exclusivamente conjuntos de dados antropométricos públicos, o que delimita o âmbito empírico ao domínio técnico e projetual. Entre estes, destaca-se a base local consolidada de medidas da mão e do membro superior distal, usada como infraestrutura intermédia para a seleção, comparação e normalização de medidas relevantes para a parametrização geométrica. A organização dos dados preserva informação sobre país, amostra, tipo de medida, estatística, fonte documental e granularidade dos subconjuntos analisados, tornando explícitas a cobertura e as limitações de cada fonte antes da sua tradução em parâmetros de projeto.

Embora o presente estudo não utilize participantes reais, a literatura metodológica da área ajuda a esclarecer como medições lineares e procedimentos de ajuste são normalmente operacionalizados em contextos aplicados. A Figura 3.1 ilustra esse tipo de recolha dimensional orientada para fabrico, servindo aqui como precedente metodológico para a tradução de medidas em parâmetros de projeto.

![](./figuras/ch3anundergraduateengineeringservicfigure1p4.png)

Figura 3.1 — Exemplo de recolha dimensional para ajuste de prótese impressa em 3D.

Fonte original (APA 7): Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

### 3.5 Critérios de avaliação e limitações metodológicas

A avaliação do sistema desenvolvido baseia-se em critérios técnicos, funcionais e metodológicos. Entre os principais critérios consideram-se a capacidade de personalização paramétrica, a consistência dimensional perante diferentes perfis antropométricos, a viabilidade de fabrico por impressão 3D, a robustez estrutural e a clareza do processo de configuração. Estes critérios visam avaliar não só o desempenho do artefacto, mas também a qualidade do próprio processo de design enquanto dispositivo de investigação, nomeadamente a sua capacidade de tornar explícitas as decisões, testar alternativas e produzir aprendizagem transferível ([Zimmerman et al., 2007](#ref-zimmerman-2007)).

Adicionalmente, são considerados critérios relacionados com a acessibilidade e a replicabilidade, avaliando-se em que medida o sistema pode ser utilizado por técnicos não especializados ou por comunidades locais com recursos limitados. A dimensão ética é igualmente ponderada, particularmente no que se refere à promoção da autonomia e da dignidade do utilizador.

Importa, contudo, reconhecer limitações metodológicas. A ausência de testes com utilizadores reais impede a validação clínica e a avaliação aprofundada da experiência de uso subjetiva. A utilização de dados antropométricos secundários limita a verificação empírica da adaptação individual. Por fim, a integração de inteligência artificial é circunscrita a funções de apoio à configuração e otimização geométricas, não abrangendo sistemas clínicos ou biomédicos avançados. Acresce que a própria estrutura iterativa adotada, embora adequada à exploração projetual, não produz, por si só, evidência clínica ou generalização estatística, exigindo que os resultados sejam lidos como contributo metodológico e prototípico, e não como validação final de eficácia em contexto de uso.

Estas limitações são assumidas como enquadramento do estudo, que se posiciona prioritariamente no domínio do design de produto e da investigação metodológica, contribuindo para a reflexão sobre o papel do design paramétrico e da inteligência artificial na personalização de dispositivos assistivos.

---

## Capítulo 4 — Desenvolvimento do Modelo Paramétrico

### 4.1 Definição do problema de design e requisitos

A definição do problema de design no desenvolvimento de próteses de membro superior é enquadrada na literatura como um desafio multiobjetivo situado na interseção entre o desempenho biomecânico, a integração humano-dispositivo e a experiência vivida do utilizador ([Cordella et al., 2016](#ref-cordella-2016); [Guo, 2025](#ref-guo-2025); [Peerdeman et al., 2011](#ref-peerdeman-2011)). O problema não pode, por isso, ser reduzido à mera replicação formal da mão ou do membro perdido. Em vez disso, trata-se de conceber dispositivos que conciliem funcionalidade, conforto, leveza, fiabilidade, controlo inteligível, aceitabilidade estética e viabilidade económica, num contexto em que continuam a registar-se taxas elevadas de rejeição e de abandono. A literatura associa estas taxas, de forma recorrente, a desconforto no encaixe, peso excessivo, limitações funcionais, baixa robustez e estratégias de controlo pouco intuitivas, revelando uma lacuna persistente entre a capacidade tecnológica e as necessidades reais de uso ([Biddiss et al., 2007](#ref-biddiss-2007); [Cordella et al., 2016](#ref-cordella-2016); [Peerdeman et al., 2011](#ref-peerdeman-2011)).

No que respeita aos tipos de requisitos considerados, a conceção protésica integra múltiplas categorias interdependentes. Os requisitos funcionais incluem padrões de preensão, graus de liberdade, amplitude de movimento, força, velocidade e capacidade de realizar atividades da vida diária. Os requisitos ergonómicos assumem particular centralidade, destacando-se o conforto, o baixo peso, a usabilidade, a facilidade de colocação e de remoção e a adequação prolongada ao uso quotidiano. Ao nível técnico, definem-se parâmetros relativos a atuadores, sistemas de transmissão, sensores, estratégias de controlo, fontes de energia e seleção de materiais com propriedades mecânicas e biocompatíveis adequadas. Em termos de fabrico, emergem exigências de modularidade, reparabilidade, custo controlado e compatibilidade com fluxos de fabrico digital e aditivo. Acrescem ainda requisitos estéticos e psicossociais, relacionados com a identidade, a aceitação social e a incorporação corporal, cuja relevância é reiterada tanto por utilizadores como por clínicos e familiares ([Biddiss et al., 2007](#ref-biddiss-2007); [Brack & Amalu, 2021](#ref-brack-2021); [Henao et al., 2025](#ref-henao-2025); [Walker et al., 2019](#ref-walker-2019)).

A tradução destas necessidades em parâmetros mensuráveis e programáveis constitui um ponto crítico no desenvolvimento de dispositivos médicos personalizados. Tal tradução implica converter necessidades qualitativas, como conforto, segurança ou facilidade de controlo, em especificações técnicas quantificáveis, como limites de peso, distribuição admissível de pressões, torque necessário nas articulações, número de graus de liberdade, autonomia energética ou tolerâncias dimensionais. A literatura sobre requisitos em próteses de membro superior mostra que este passo é decisivo, pois as prioridades dos utilizadores nem sempre coincidem com os indicadores habitualmente privilegiados pela engenharia, o que exige uma explicitação rigorosa das correspondências entre a necessidade, o critério de avaliação e a decisão projetual ([Cordella et al., 2016](#ref-cordella-2016); [Hofmann et al., 2016](#ref-hofmann-2016); [Jones et al., 2023](#ref-jones-2023)). Em contextos paramétricos, esta operacionalização materializa-se na definição de variáveis geométricas, mecânicas e construtivas controladas por parâmetros, permitindo a geração de geometrias adaptadas a dados antropométricos e a requisitos funcionais específicos.

Diversos enquadramentos metodológicos sustentam a especificação de requisitos em sistemas protéticos paramétricos ou fabricados digitalmente. Para além dos modelos clássicos de engenharia sistemática, observa-se uma transição clara para abordagens centradas no utilizador, como o User-Centered Design, o Human-Centered Design e metodologias participativas e de co-criação. Estas abordagens promovem ciclos iterativos de prototipagem e avaliação com envolvimento ativo de utilizadores, clínicos e, em alguns casos, familiares, reconhecendo que a definição do problema de design depende tanto da performance mecânica como da experiência concreta de uso ([Henao et al., 2025](#ref-henao-2025); [Peerdeman et al., 2011](#ref-peerdeman-2011); [Walker et al., 2019](#ref-walker-2019)). No domínio digital, a integração de modelação paramétrica, digitalização 3D e simulação, nomeadamente análise por elementos finitos e modelação cinemática, estrutura um fluxo de desenvolvimento em que os requisitos podem ser incorporados diretamente em modelos computacionais ajustáveis e verificados antes da produção física.

A formalização de constrangimentos nas fases iniciais do design desempenha igualmente um papel estruturante. Constrangimentos materiais são definidos em termos de resistência, rigidez, durabilidade e compatibilidade biológica. Constrangimentos mecânicos incluem limites de torque, deformação admissível, integridade estrutural sob carga e capacidades cinemáticas mínimas para tarefas quotidianas. Constrangimentos anatómicos são integrados com base em dados antropométricos e, quando possível, na digitalização do membro residual, o que condiciona as geometrias, as interfaces e os volumes internos. Finalmente, os constrangimentos produtivos relacionam-se com as capacidades e limitações do fabrico aditivo, as tolerâncias, a orientação de impressão, o tempo de fabrico, o custo e a escalabilidade. A formalização destes limites desde as fases conceptuais permite enquadrar o processo como um exercício de otimização sob múltiplas restrições, estruturando as decisões projetuais de forma explícita e verificável ([Brack & Amalu, 2021](#ref-brack-2021); [Herneth et al., 2024](#ref-herneth-2024); [Jones et al., 2023](#ref-jones-2023)).

### 4.2 Parâmetros antropométricos e estrutura do modelo

A definição e operacionalização de parâmetros antropométricos constituem um elemento central no desenvolvimento de sistemas protésicos personalizados, funcionando como a principal interface entre o corpo do utilizador e a configuração geométrica e funcional do modelo paramétrico. No contexto das próteses de membro superior, estes parâmetros não se limitam a medições isoladas, mas integram um sistema estruturado de variáveis que descrevem a morfologia da mão, dos dedos, do punho e, quando aplicável, do antebraço ou do membro residual. A literatura recente converge em dois pontos: a personalização eficaz depende de medidas anatomicamente relevantes e não de escalonamentos genéricos; e essas medidas devem ser organizadas de forma a alimentar diretamente a lógica do modelo digital ([Chatzioglou et al., 2024](#ref-chatzioglou-2024); [Moreo, 2016](#ref-moreo-2016); [Rodríguez-Vega & Rodríguez-Vega, 2024](#ref-rodriguez-vega-2024)).

Esta exigência de organizar as medições em parâmetros operáveis é particularmente evidente nos modelos digitais do dedo e da mão. A Figura 4.1 mostra um exemplo de decomposição paramétrica em comprimentos, larguras e secções articulares, o que clarifica o tipo de estrutura dimensional que sustenta a transição da antropometria para a geometria configurável.

![](./figuras/ch4parametric3dmodelingofacustomifigure3p2.png)

Figura 4.1 — Parâmetros antropométricos utilizados na modelação paramétrica de dedos protésicos.

Fonte original (APA 7): Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. https://doi.org/10.1109/BioRob60516.2024.10719909

Os parâmetros antropométricos mais relevantes concentram-se, em primeiro lugar, na definição da estrutura dimensional base da mão. Medidas como o comprimento da mão, a largura da mão e o comprimento da palma constituem descritores dimensionais primários, permitindo estabelecer a escala do modelo e definir a sua organização geral. Para além destas, incluem-se parâmetros relativos aos dedos, como comprimentos segmentares e proporções entre falanges, bem como as dimensões do polegar e do punho, essenciais para a funcionalidade e a integração do dispositivo ([Chatzioglou et al., 2024](#ref-chatzioglou-2024); [Nag et al., 2003](#ref-nag-2003)).

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

A definição de um conjunto mínimo de parâmetros antropométricos depende diretamente do nível de amputação, uma vez que diferentes configurações protésicas exigem graus distintos de detalhe. Em termos práticos, reduzir o número de medições necessárias é importante para viabilizar processos de personalização mais escaláveis, sobretudo quando a recolha de dados ocorre fora de contextos clínicos altamente especializados ([Moreo, 2016](#ref-moreo-2016); [Romero et al., 2025](#ref-da-silveira-romero-2025)).

Tabela 4.2 — Conjuntos mínimos de parâmetros por nível de amputação

| Transradial (abaixo do cotovelo) | Comprimento do membro residual, circunferência do antebraço, largura do punho |
| --- | --- |
| Desarticulação do punho | Largura e profundidade do punho, comprimento da mão |
| Parcial da mão | Comprimento da palma, dimensões dos dedos remanescentes |
| Dedos (parcial) | Comprimento e largura do dedo, proporções falângicas |
| Mão completa (cosmética/funcional) | Comprimento da mão, largura da palma, comprimento dos dedos |

Esta abordagem permite estruturar o sistema paramétrico com base em entradas (inputs) essenciais, reduzindo a complexidade sem comprometer a funcionalidade. Importa, contudo, distinguir entre parâmetros mínimos de configuração e parâmetros de refinamento: os primeiros permitem gerar uma instância funcional do modelo; os segundos melhoram o ajuste, a coerência proporcional ou o desempenho cinemático quando há dados adicionais disponíveis.

### Limitações do escalonamento uniforme

Uma limitação recorrente em abordagens simplificadas de modelação é o uso de escalonamento uniforme (uniform scaling), no qual um modelo base é dimensionado proporcionalmente em todas as direções. Esta abordagem revela-se inadequada no contexto antropométrico, uma vez que as dimensões da mão apresentam correlações imperfeitas entre si e variam de forma desigual entre populações, sexos e grupos etários. Em consequência, indivíduos com largura de mão semelhante podem apresentar comprimentos digitais, proporções falângicas ou dimensões do polegar significativamente diferentes. A modelação paramétrica exige, por isso, a definição de parâmetros independentes e a possibilidade de derivar proporções locais sem pressupor homotetia global do modelo ([Lim et al., 2018](#ref-lim-2018); [Nag et al., 2003](#ref-nag-2003); [Rodríguez-Vega & Rodríguez-Vega, 2024](#ref-rodriguez-vega-2024)).

Esta limitação torna-se visualmente evidente na Figura 4.2, que compara um modelo uniformemente escalado com outro parametrizado a partir de variáveis independentes. A diferença é relevante porque mostra que a personalização não depende apenas de “aumentar ou reduzir” um modelo-base, mas também de reorganizar as relações geométricas internas.

![](./figuras/ch4customizationofa3dprintedprostfigure8p7.png)

Figura 4.2 — Comparação entre o escalonamento uniforme e a modelação paramétrica de dedo protésico.

Fonte original: Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. https://doi.org/10.1115/DETC2018-85645

### Métodos de recolha de dados antropométricos

A recolha de dados pode ser realizada por diferentes métodos, com implicações diretas na precisão e na aplicabilidade dos modelos. A escolha do método depende do objetivo da medição: parametrização dimensional básica, reconstrução geométrica fina, desenho do encaixe ou obtenção de relações internas entre superfícies e estruturas ósseas. Em termos práticos, a literatura mostra que não há um método universalmente superior; há, sim, uma adequação diferencial entre método, custo, acessibilidade e tipo de dado necessário ([Çıklaçandır et al., 2022](#ref-cklacandr-2022); [Herbst et al., 2021](#ref-herbst-2021)).

Tabela 4.3 — Métodos de recolha de dados antropométricos e suas características

| Medição manual | Dimensões lineares | Simplicidade, baixo custo | Representação geométrica limitada | Parametrização básica |
| --- | --- | --- | --- | --- |
| Digitalização 3D | Geometria superficial | Elevada precisão, rapidez | Equipamento e processamento necessários | Encaixe e forma |
| Imagiologia médica | Estrutura interna e externa | Dados anatómicos detalhados | Alto custo e menor acessibilidade | Modelação biomecânica |
| Fotogrametria | Geometria aproximada | Acessível, potencial remoto | Precisão variável | Aquisição preliminar |

### Bases de dados antropométricas, extração e normalização

A definição de parâmetros pode apoiar-se em bases de dados antropométricas de referência e em normas de medição corporal, que ajudam a estabilizar a nomenclatura, os pontos anatómicos e os intervalos esperados de variação. No presente projeto, esse apoio foi operacionalizado através da consolidação local de dados provenientes de estudos populacionais e de bases de referência. O conjunto reunido contém 1.790 registos em formato longo, cobre nove países — China, Estados Unidos da América, Índia, Jordânia, México, Nigéria, Países Baixos, Portugal e Turquia — e combina dados de estudos publicados, relatórios técnicos e sub-bases DINED disponibilizadas pela TU Delft.

O objetivo desta consolidação não foi criar uma nova norma antropométrica, nem substituir a medição individual do utilizador. O objetivo foi construir uma infraestrutura intermédia, verificável e comparável, capaz de apoiar três decisões de projeto: definir intervalos plausíveis para os parâmetros expostos no modelo; identificar quais dimensões são suficientemente recorrentes na literatura para servirem como entradas mínimas; e testar a coerência geométrica de configurações geradas a partir de diferentes perfis populacionais. Esta distinção é importante porque os dados populacionais descrevem tendências e dispersões, enquanto uma prótese personalizada continua a exigir medições diretas ou digitalização específica quando o ajuste final ao corpo está em causa.

A seleção das fontes seguiu critérios explícitos. Foram incluídas fontes que apresentavam dados primários ou bases de dados reconhecidas, pelo menos uma dimensão relevante para a mão, dedos, palma, punho ou antebraço, identificação da população ou subgrupo e estatística descritiva legível. Foram excluídos estudos que apenas reutilizavam dados secundários sem acesso claro à fonte original, artigos de engenharia que mencionavam dimensões de forma incidental, exemplos baseados num único sujeito e fontes sem informação suficiente sobre população, método ou unidade. Esta decisão explica, por exemplo, a exclusão dos valores percentílicos reproduzidos por Moreo (2016) a partir da base DINED: apesar de o trabalho ser relevante para a lógica de parametrização, a tabela não constitui recolha primária autónoma e seria metodologicamente redundante quando a fonte DINED podia ser tratada diretamente ([Moreo, 2016](#ref-moreo-2016)).

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

A opção pelo formato longo foi deliberada. Em vez de criar uma linha por dimensão com colunas fixas para média, desvio-padrão e percentis, cada estatística foi registada como uma linha própria. Assim, uma mesma dimensão pode originar várias linhas para média, desvio-padrão, P5, P50, P95, mínimo ou máximo. Este formato facilita a integração de fontes incompletas, porque nem todos os estudos reportam o mesmo conjunto de estatísticas. Na base atual, existem 612 médias, 609 desvios-padrão, 513 percentis, 28 mínimos e 28 máximos. Esta assimetria é metodologicamente relevante: os datasets ANSUR e algumas fontes DINED permitem uma leitura estatística mais ampla, enquanto estudos como Mistarihi (2020) ou Lim et al. (2018) só oferecem valores parciais, úteis como referência contextual mas insuficientes para inferência populacional robusta ([Gordon et al., 2015](#ref-gordon-2015); [Lim et al., 2018](#ref-lim-2018); [Mistarihi, 2020](#ref-mistarihi-2020)).

As principais dificuldades encontradas dizem respeito à heterogeneidade dos protocolos. A expressão “comprimento da mão”, por exemplo, nem sempre corresponde ao mesmo trajeto anatómico: alguns estudos usam a prega do punho, outros o processo estilóide, e outros definem o comprimento a partir de marcos funcionais da palma. Do mesmo modo, há estudos que medem a mão direita, outros a mão dominante, e o estudo português mede a mão esquerda por constrangimentos de recolha ([Anacleto Filho et al., 2023](#ref-anacleto-filho-2023)). Estas diferenças impedem tratar todas as entradas como equivalentes diretas e justificam o registo explícito do protocolo de medição. A base não apaga a heterogeneidade; torna-a explícita para que o modelo paramétrico possa usar os dados de forma informada.

Houve também dificuldades de granularidade e representatividade. Algumas fontes são estatisticamente fortes, mas pouco específicas para a mão; outras são ricas em medidas da mão, mas limitadas a uma população muito particular. Nag et al. (2003), por exemplo, fornece uma cobertura dimensional muito detalhada, mas apenas para mulheres indianas trabalhadoras. Rodríguez-Vega e Rodríguez-Vega (2024) oferecem uma amostra mexicana numerosa e grupos etários úteis, mas concentram-se em quatro dimensões principais. Ibiwari et al. (2025) acrescenta dados africanos, mas a amostra é composta por atletas universitários, não por população geral. Mistarihi (2020) é relevante por incluir trabalhadores com deficiência física, mas apresenta poucos registos, sem desagregação suficiente por sexo. Estes casos foram mantidos porque aumentam a diversidade de referência, mas as suas limitações foram registadas nos metadados da população, da dimensão amostral e da qualidade do dado.

Em sentido inverso, algumas fontes facilitaram a extração. As tabelas com percentis claros, unidades explícitas e separação por sexo ou idade permitiram codificação direta e maior confiança. A estrutura HTML da DINED facilitou a recuperação sistemática de médias e desvios-padrão por sub-base, sexo e grupo etário, embora não disponibilize percentis na mesma interface. O ANSUR II também foi particularmente útil por disponibilizar estatísticas amplas e uma grande amostra militar, permitindo trabalhar com medições da mão, punho e antebraço em escala populacional ([Gordon et al., 2015](#ref-gordon-2015); [Molenbroek, 1998](#ref-molenbroek-1998); [Molenbroek et al., 2003](#ref-molenbroek-2003); [Steenbekkers & van Beijsterveldt, 1998](#ref-steenbekkers-1998)). Ainda assim, estas fontes não resolvem o problema da personalização clínica: militares, crianças neerlandesas ou idosos chineses não representam automaticamente utilizadores com amputação de membro superior.

As decisões de normalização seguiram quatro princípios. Primeiro, todas as unidades foram convertidas para milímetros, centímetros e polegadas, mantendo uma unidade-fonte única para evitar conversões ambíguas no momento de utilização. Segundo, valores provenientes de subgrupos muito pequenos, figuras em vez de tabelas, desvios-padrão atípicos ou definições anatómicas incertas foram preservados, mas assinalados em notas de qualidade, em vez de serem eliminados sem rasto. Terceiro, as medidas foram agrupadas por região corporal, para distinguir dimensões diretamente ligadas à geometria da mão de dimensões úteis apenas para a interface com o punho ou antebraço. Quarto, os dados foram tratados como referências paramétricas e não como prescrições dimensionais finais.

Esta base faz sentido para o projeto porque responde a uma necessidade específica do modelo desenvolvido: transformar uma discussão genérica sobre personalização em intervalos, relações e restrições utilizáveis. O modelo precisa de saber que medidas são recorrentes na literatura, que variações são plausíveis entre populações, que dimensões podem servir como entradas mínimas e onde o escalonamento uniforme se torna arriscado. A base local permite comparar comprimento da mão, largura da palma, comprimentos digitais, dimensões do punho e relações com o antebraço de forma rastreável. Por isso, ela sustenta a passagem entre o enquadramento antropométrico e a modelação em OpenSCAD: os dados não geram a prótese por si só, mas delimitam o espaço de variação no qual o modelo pode operar com maior coerência.

Permanece, contudo, uma limitação central. A maior parte dos dados disponíveis provém de populações sem amputação e não descreve a morfologia do membro residual, nem a interação dinâmica entre tecido, carga e encaixe. Para uma prótese definitiva, a referência mais adequada seria a medição direta do utilizador, idealmente complementada por digitalização tridimensional e validação de interface. Nesta investigação, os dados antropométricos públicos são usados para estruturar o sistema, testar coerência dimensional e fundamentar decisões de parametrização; não são apresentados como substituto de avaliação clínica, prova de conforto ou validação individual.

### Estrutura paramétrica e mapeamento de parâmetros

A estrutura do modelo paramétrico organiza os parâmetros segundo uma lógica hierárquica e relacional, distinguindo entre parâmetros primários, derivados, funcionais e construtivos. Esta distinção é metodologicamente importante porque impede que o modelo seja tratado como um conjunto plano de medidas independentes. Em vez disso, estabelece-se uma cadeia de transformação em que algumas variáveis funcionam como entradas principais do utilizador e outras como consequências geométricas, cinemáticas ou produtivas dessas entradas ([Moreo, 2016](#ref-moreo-2016); [Romero et al., 2025](#ref-da-silveira-romero-2025)).

Tabela 4.5 — Estrutura hierárquica dos parâmetros no modelo paramétrico

| Primários | Comprimento da mão, largura da palma | Input direto | Independentes |
| --- | --- | --- | --- |
| Derivados | Proporções das falanges | Construção geométrica | Dependentes |
| Funcionais | Amplitude de movimento, posição articular | Desempenho | Ligação cinemática |
| Construtivos | Espessuras, folgas, tolerâncias | Fabrico | Ajuste técnico |

A tradução destes parâmetros em geometria é realizada por meio de relações explícitas entre medições e componentes do modelo.

Tabela 4.6 — Mapeamento entre parâmetros antropométricos e elementos do modelo

| Comprimento da mão | Escala geral e comprimento dos dedos |
| --- | --- |
| Largura da palma | Volume da palma e espaçamento entre dedos |
| Comprimento dos dedos | Geometria das falanges |
| Circunferência do antebraço | Geometria do encaixe |
| Largura do punho | Interface palma-punho |
| Proporções falângicas | Relações cinemáticas dos mecanismos digitais |

Este mapeamento constitui a base da modelação paramétrica, permitindo converter dados antropométricos em configurações geométricas e funcionais. Em termos práticos, a passagem de medição para geometria não deve ser entendida como uma transposição linear, mas como a definição de relações controladas: certos parâmetros regulam a escala geral, outros definem proporções locais e outros ainda atuam como restrições de consistência ou de fabricabilidade. Antes de qualquer implementação em código, torna-se necessário estabilizar três níveis: os dados de entrada, as relações entre parâmetros e os limites técnicos que condicionam a sua transformação em forma.

No contexto desta investigação, o papel da secção 4.2 é, portanto, delimitado com clareza: identificar quais são os parâmetros antropométricos relevantes, como são recolhidos ou inferidos, e de que modo se organizam antes de entrarem na estrutura computacional do modelo. A secção seguinte retoma precisamente esta base para mostrar como esse sistema de entradas, dependências e restrições é formalizado em OpenSCAD como um modelo executável, modular e regenerável.

### 4.3 Modelação paramétrica em OpenSCAD

A modelação paramétrica em OpenSCAD corresponde, nesta investigação, ao momento em que a estrutura definida na secção anterior passa de um quadro conceptual a um sistema operativo. Os parâmetros antropométricos selecionados, as relações hierárquicas entre variáveis e os limites de configuração deixam de funcionar apenas como critérios de organização e passam a ser inscritos em código, de modo a gerar geometria de forma consistente e repetível. Assim, a transição para OpenSCAD não representa uma mudança de tema, mas a continuação lógica do mesmo problema: como transformar dados corporais e regras de projeto num modelo configurável que preserve coerência formal, funcional e produtiva.

A modelação paramétrica em OpenSCAD é, por isso, aqui entendida como uma abordagem em que a geometria resulta de regras explícitas, parâmetros definidos em código e relações de dependência entre componentes, em vez de edição manual isolada de formas. Para o desenvolvimento de próteses personalizadas de membro superior, esta lógica é particularmente relevante, pois permite tratar a prótese como uma família configurável de soluções, regenerável com base em novos dados antropométricos, requisitos funcionais e limites de fabrico. A literatura sobre modelação paramétrica aplicada a próteses e sobre CAD baseado em código converge precisamente nesta direção, associando este tipo de abordagem a maior rastreabilidade, repetibilidade e capacidade de automatização em fluxos de personalização digital ([Machado et al., 2019](#ref-machado-2019); [Moreo, 2016](#ref-moreo-2016); [Romero et al., 2025](#ref-da-silveira-romero-2025)).

Ao contrário de ambientes centrados na manipulação gráfica direta, o OpenSCAD opera como uma especificação computacional do objeto. Essa característica é metodologicamente relevante para a presente investigação porque torna o modelo não apenas um resultado geométrico, mas também um artefacto explícito de projeto: um sistema em que se registam as relações entre entradas antropométricas, módulos geométricos, restrições construtivas e decisões formais. Neste sentido, a modelação baseada em código articula-se bem com uma perspetiva de Research Through Design, na medida em que o próprio modelo pode ser lido, revisto, testado e documentado como uma estrutura de conhecimento técnico.

### 4.3.1 Estrutura técnica, parâmetros e restrições

A estrutura técnica de um modelo paramétrico baseado em OpenSCAD pode ser compreendida como uma arquitetura em camadas. Numa primeira camada situam-se os dados de entrada, provenientes de medições lineares, de dados consolidados de referência ou de digitalização tridimensional. Numa segunda camada, esses dados são transformados em parâmetros geométricos derivados, responsáveis por estabelecer proporções, espessuras, posições articulares e relações entre subcomponentes. Segue-se uma camada funcional, na qual se definem exigências de mobilidade, montagem ou integração mecânica, e uma camada de restrições produtivas, na qual se enquadram espessuras mínimas, folgas, tolerâncias e limites de fabricabilidade. Esta organização permite controlar a personalização sem comprometer a coerência interna do sistema ([Moreo, 2016](#ref-moreo-2016); [Nini et al., 2024](#ref-nini-2024); [Saldarriaga et al., 2024](#ref-saldarriaga-2024)).

Tabela 4.3.1 — Estrutura técnica em camadas de um modelo paramétrico em OpenSCAD para próteses personalizadas

| Entrada | Dados antropométricos e/ou dados de digitalização | Individualizar o modelo | Largura da palma, comprimentos digitais, perímetro do coto |
| --- | --- | --- | --- |
| Derivação geométrica | Parâmetros calculados a partir das entradas | Traduzir medidas em relações formais | Comprimentos segmentares, espessuras, offsets |
| Comportamento funcional | Parâmetros ligados ao uso e ao mecanismo | Regular movimento, montagem e desempenho | Amplitude articular, espaço para tendões, eixos |
| Restrições produtivas | Limites de fabrico e consistência | Garantir fabricabilidade e robustez | Espessura mínima, folgas, raios mínimos |

Em OpenSCAD, esta arquitetura tende a materializar-se através de módulos relativamente autónomos. Em vez de concentrar toda a definição geométrica num único bloco de código, o modelo pode ser distribuído em módulos correspondentes à palma, aos dedos, às articulações, às interfaces de fixação ou de encaixe. A modularidade tem aqui duas vantagens diretas: reduz a opacidade do sistema e facilita a regeneração controlada de variantes. Num contexto protésico, isto permite que alterações nos parâmetros de entrada não se propaguem de forma arbitrária a todo o modelo, mas sim segundo relações previamente explícitas e localizáveis ([Machado et al., 2019](#ref-machado-2019); [Romero et al., 2025](#ref-da-silveira-romero-2025)).

Outro aspeto central é a integração de restrições diretamente na lógica paramétrica. Em vez de tratar a verificação de fabricabilidade como etapa exclusivamente posterior, o modelo pode incorporar, desde o início, limites mínimos de espessura, folgas entre elementos móveis, margens de tolerância e verificações condicionais para evitar combinações inválidas. Este princípio é particularmente relevante em próteses produzidas por fabrico aditivo, nas quais pequenas alterações dimensionais podem comprometer a montagem, a resistência ou a imprimibilidade. Estudos sobre modelação paramétrica de dedos protésicos e sockets personalizados mostram, precisamente, que a robustez do sistema depende da articulação entre parâmetros antropométricos e restrições construtivas, e não apenas da liberdade de variação geométrica ([Nini et al., 2024](#ref-nini-2024); [Saldarriaga et al., 2024](#ref-saldarriaga-2024)).

Finalmente, a modelação em OpenSCAD pode ser articulada a fluxos de dados mais complexos, incluindo a digitalização tridimensional e a automatização parcial do desenho. Trabalhos como os de [Herbst et al. (2021)](#ref-herbst-2021) e [Saldarriaga et al. (2024)](#ref-saldarriaga-2024) mostram que a personalização contemporânea tende a aproximar a medição, a parametrização e o fabrico, reduzindo o intervalo entre a captura anatómica e a geração de modelos prontos para produção. No caso desta investigação, essa articulação não significa abandonar a lógica explícita do código, mas, antes, usá-la como núcleo organizador sobre o qual dados, restrições e interfaces de configuração podem ser integrados de modo consistente e repetível.

### 4.3.2 Análise crítica da abordagem

A adoção do OpenSCAD apresenta vantagens metodológicas claras para este projeto. A primeira é a transparência. Como o modelo é definido por código, as relações entre variáveis, dependências e restrições ficam mais explícitas do que em muitos fluxos CAD baseados apenas em operações gráficas. Esta condição favorece a rastreabilidade, a revisão crítica e a reprodutibilidade, qualidades particularmente importantes num trabalho académico em que o modelo paramétrico não é apenas um instrumento de produção formal, mas também um objeto de análise ([Machado et al., 2019](#ref-machado-2019)).

Uma segunda vantagem reside na afinidade entre a modelação baseada em código, a automação e a partilha aberta. A literatura mostra que sistemas como o OpenSCAD articulam-se bem com lógicas de configuração web, de geração repetida de variantes e de circulação de ficheiros-fonte em comunidades distribuídas. O facto de um modelo poder ser exposto por meio de parâmetros, ligado a interfaces HTML e convertido em resultados fabricáveis, sem exigir edição direta do código a cada iteração, constitui um argumento forte para a sua utilização em contextos de personalização acessível ([Nilsiam & Pearce, 2017](#ref-nilsiam-2017)). Para um projeto que pretende aproximar parametrização, interface e apoio computacional, esta característica é especialmente relevante.

Contudo, a abordagem apresenta limitações importantes. A primeira é a barreira cognitiva associada à programação. Mesmo quando o modelo é modular e bem estruturado, a edição direta em OpenSCAD exige raciocínio abstrato sobre transformações geométricas, dependências paramétricas e operações booleanas. Por essa razão, a utilidade do OpenSCAD aumenta quando o sistema é mediado por camadas intermediárias de interface ou por procedimentos que exponham apenas os parâmetros realmente necessários à configuração. A segunda limitação é geométrica: a lógica de Constructive Solid Geometry favorece peças mecânicas, modulares e relativamente discretas, mas tende a ser menos fluida para superfícies orgânicas complexas ou interfaces anatómicas altamente irregulares, sobretudo quando comparada com ferramentas mais orientadas para superfícies livres.

Há ainda uma limitação na interoperabilidade. A literatura comparativa sobre OpenSCAD sublinha que o ecossistema está fortemente orientado para formatos tesselados e para fluxos de fabrico baseados em malhas, o que pode dificultar a integração com certos circuitos CAD industriais ou com ambientes que exijam preservação completa da informação paramétrica em formatos normalizados ([Machado et al., 2019](#ref-machado-2019)). Isto não invalida a adequação do OpenSCAD ao presente projeto, mas significa que a sua adoção deve ser vista como uma escolha situada: muito eficaz para estruturar um núcleo paramétrico explícito, menos adequada quando o objetivo depende de plena continuidade com certos fluxos proprietários de engenharia.

Por fim, importa reconhecer que a robustez da abordagem não se esgota na geração da geometria. Mesmo quando a lógica paramétrica é clara e as restrições estão integradas, a validação continua a depender da verificação no slicer, do controlo dimensional, de eventual simulação estrutural e da observação do comportamento da peça em protótipo. Em consequência, o valor do OpenSCAD nesta investigação não reside numa promessa de automatização total, mas na capacidade de fornecer uma infraestrutura técnica clara para ligar a personalização antropométrica, a modularidade, as restrições de fabrico e a documentação do processo. É precisamente essa combinação entre explicitação, reexecução e criticabilidade que justifica a sua escolha como base para a modelação paramétrica aqui desenvolvida.

### 4.4 Iterações, refinamento e discussão intermédia

O desenvolvimento do modelo paramétrico não ocorreu, desde o início, como uma sequência linear orientada para uma solução estável e definitiva. Pelo contrário, evoluiu através de ciclos sucessivos de formulação, teste, correção e reconfiguração, em coerência com a perspetiva de Research Through Design, segundo a qual o próprio processo projetual constitui um meio de produção de conhecimento (Zimmerman, Forlizzi, & Evenson, 2007). Neste enquadramento, cada versão do modelo funcionou simultaneamente como protótipo operativo e como dispositivo crítico, permitindo tornar visíveis as limitações, reformular os critérios e aprofundar a compreensão das relações entre dados antropométricos, organização geométrica, requisitos funcionais e constrangimentos de fabrico.

A necessidade de iteração tornou-se particularmente evidente porque a modelação paramétrica, apesar da sua aparência sistemática, depende de um equilíbrio delicado entre abstração e concretização. Numa fase inicial, a estrutura do sistema assentou na definição de um conjunto de parâmetros julgados essenciais e numa primeira hierarquia entre variáveis de entrada, valores derivados e restrições. No entanto, à medida que o modelo foi sendo testado em diferentes cenários, verificou-se que a mera disponibilidade de muitos parâmetros não aumentava, por si só, a capacidade de personalização. Pelo contrário, a exposição excessiva de variáveis tendia a tornar o sistema mais opaco, menos previsível e mais vulnerável a incoerências geométricas, confirmando a importância de limitar e estruturar cuidadosamente o espaço configurável (Ozdemir, Verlinden, & Cascini, 2022; Lei, Yao, Moon, & Bi, 2016).

Uma parte decisiva do refinamento incidiu, por isso, na reorganização da arquitetura paramétrica. O objetivo deixou de ser apenas permitir a variação e passou a consistir em garantir uma variação controlada. Isto implicou reduzir redundâncias, clarificar as dependências internas e distinguir com maior rigor os parâmetros estruturantes dos ajustamentos secundários. Em vez de um sistema monolítico e pouco legível, procurou-se construir uma lógica hierárquica em que as relações críticas permanecessem explícitas e rastreáveis. Esta passagem foi importante não apenas para a manutenção do código, mas também para a robustez do próprio modelo, dado que a literatura sublinha que a qualidade das relações paramétricas é determinante para a viabilidade de famílias de produto adaptáveis e tecnicamente consistentes ([Lei et al., 2016](#ref-lei-2016); Wiberg, Persson, & Ölvander, 2019).

À medida que a estrutura geral se consolidou, o trabalho iterativo deslocou-se para a decomposição do sistema em módulos relativamente autónomos. Esta modularização permitiu isolar problemas, testar componentes localmente e introduzir alterações sem comprometer integralmente o comportamento global do modelo. No contexto do presente projeto, esta estratégia revelou-se especialmente útil na articulação entre elementos estruturais, zonas de contacto, interfaces mecânicas e componentes de ligação. Mais do que uma escolha organizativa do código, a modularização funcionou como uma clarificação progressiva da lógica do objeto, aproximando o modelo de uma estrutura configurável, mais disciplinada e compatível com futuros contextos de interface ou de configuração assistida ([Nilsiam & Pearce, 2017](#ref-nilsiam-2017)).

As iterações também mostraram que a robustez de um modelo paramétrico só se torna legível quando confrontado com situações-limite. Um sistema pode parecer estável dentro de uma faixa reduzida de variação e, ainda assim, revelar fragilidades relevantes quando submetido a combinações menos previsíveis de parâmetros. Foi precisamente nesse tipo de ensaio que surgiram problemas como interseções indevidas entre componentes, espessuras insuficientes em zonas críticas, desalinhamentos de interfaces, incompatibilidades entre dimensões derivadas e perdas localizadas de coerência proporcional. O refinamento consistiu, assim, menos na correção pontual de erros isolados e mais na identificação de padrões recorrentes de instabilidade, o que levou à introdução progressiva de verificações condicionais, limites paramétricos e ajustes automáticos.

Outro eixo central do processo prendeu-se à relação entre personalização e fabricabilidade. Nem toda a variação admissível do ponto de vista formal mostrou-se viável do ponto de vista produtivo. Certas configurações geravam geometrias demasiado finas, folgas inadequadas, transições abruptas ou zonas vulneráveis no contexto da impressão 3D. Neste sentido, a evolução do modelo confirmou a relevância de integrar critérios de Design for Additive Manufacturing à própria lógica paramétrica, em vez de tratá-los como uma verificação externa e posterior. A literatura sobre DfAM aponta precisamente para a necessidade de incorporar tolerâncias, espessuras mínimas, orientações de fabrico e limites materiais desde a fase de conceção, reduzindo falhas e encurtando os ciclos de reimpressão e de correção (Chtioui, Gaha, & Benamara, 2023; [Wiberg et al., 2019](#ref-wiberg-2019)).

A dimensão funcional introduziu um nível adicional de exigência. Em sistemas configuráveis para próteses, a coerência geométrica e a imprimibilidade não bastam para assegurar a adequação ao uso. A articulação entre segmentos, o posicionamento relativo dos mecanismos, a distribuição de massa, as zonas de esforço e a amplitude de movimento influenciam diretamente o desempenho esperado do objeto. Por essa razão, várias revisões do modelo implicaram reajustes que não se limitavam a problemas formais, mas também à necessidade de manter um equilíbrio plausível entre adaptação dimensional, comportamento funcional e viabilidade material. O refinamento correspondeu, assim, a uma negociação contínua entre a simplificação paramétrica e a exigência prototípica.

Do ponto de vista metodológico, importa sublinhar que este percurso não deve ser lido como uma simples sucessão de tentativas e erros. Cada iteração reconfigurou a compreensão do problema e tornou mais explícitos aspetos que não eram plenamente antecipáveis na formulação inicial. Entre eles, destacam-se a dificuldade de traduzir certas qualidades anatómicas em relações paramétricas simples, a tendência de modelos demasiado abertos a perderem consistência e a necessidade de explicitar restrições para preservar a coerência perante a variação. Neste sentido, o conhecimento produzido não reside apenas no estado final do modelo, mas também no próprio processo de convergência crítica que permitiu delimitar o que pode e o que não pode ser razoavelmente parametrizado neste contexto ([Zimmerman et al., 2007](#ref-zimmerman-2007)).

A discussão intermédia decorrente destas iterações permite tirar algumas conclusões provisórias. Em primeiro lugar, confirma-se que a modelação paramétrica baseada em código constitui um enquadramento adequado para estruturar sistemas configuráveis, desde que a arquitetura seja disciplinada e os parâmetros expostos sejam criteriosamente selecionados. Em segundo lugar, verifica-se que a robustez do sistema depende menos da quantidade de variáveis disponíveis do que da qualidade das relações estabelecidas entre elas. Em terceiro lugar, torna-se claro que a personalização eficaz exige integração simultânea de critérios antropométricos, funcionais e produtivos, não podendo ser reduzida a mera transformação geométrica. Por fim, a iteração evidencia-se como mecanismo indispensável de convergência: não encerra definitivamente o sistema, mas estabiliza uma versão suficientemente consistente para sustentar as fases seguintes de plataforma, integração digital e exploração assistida.

---

## Capítulo 5 — Plataforma Web e Integração Digital

### 5.1 Enquadramento conceptual e perfis de utilizador

A plataforma web desenvolvida no âmbito deste projeto constitui a camada de mediação entre o modelo paramétrico, os dados do utilizador e os processos de configuração digital da prótese. O seu enquadramento conceptual assenta na ideia de que a personalização não deve depender da manipulação direta do código nem de competências avançadas de modelação tridimensional, mas de uma interface capaz de traduzir dados antropométricos, decisões de configuração e critérios de fabrico em parâmetros operacionais inteligíveis. Nesta perspetiva, a plataforma não é apenas um visualizador técnico do modelo, mas também um dispositivo de mediação que reorganiza a relação entre o sistema paramétrico, o utilizador, o processo de decisão e a preparação para o fabrico. Esta leitura é coerente com a literatura sobre personalização digital e mass personalisation, que descreve os configuradores como infraestruturas que expõem uma parte controlada do espaço de variação, permitindo adaptar produtos sem comprometer a coerência interna do modelo-base (Ozdemir, Verlinden, & Cascini, 2022; [Stralen, 2018](#ref-stralen-2018)).

Do ponto de vista funcional, a plataforma foi concebida para suportar um processo de personalização progressiva, no qual a definição geométrica da prótese resulta da articulação entre a recolha de dados, a seleção do modelo, o ajustamento de parâmetros, a visualização do resultado e a eventual exportação para prototipagem. Esta organização procura reduzir a distância entre o domínio técnico da modelação paramétrica e o contexto aplicado de utilização clínica, projetual ou experimental. Em vez de exigir que cada interveniente compreenda a estrutura interna do ficheiro OpenSCAD, o sistema disponibiliza uma camada de interação mais acessível, baseada em controlos paramétricos, pré-visualização tridimensional e gestão de configurações. Tal opção aproxima-se de abordagens recentes em plataformas de personalização protésica, nas quais a interface funciona como meio de tornar observável, configurável e progressivamente verificável um processo que, de outro modo, permaneceria dependente de software especializado ou de mediação exclusivamente técnica ([Peixoto et al., 2025](#ref-peixoto-2025)).

Neste sentido, a plataforma deve ser entendida como um sistema sociotécnico, e não apenas como um artefacto de software. A personalização deixa de ser concebida como um ato individual e isolado e passa a ser enquadrada como um processo distribuído, no qual diferentes agentes intervêm com graus distintos de responsabilidade e de controlo. Num contexto de próteses personalizadas, o resultado final pode depender da articulação entre o utilizador final, o designer, o técnico ou o clínico, bem como de condicionantes produtivas e de critérios de validação. A plataforma procura, assim, oferecer uma infraestrutura digital que acomode essa pluralidade de agentes sem comprometer a consistência técnica da configuração paramétrica nem deslocar indevidamente a responsabilidade para o utilizador menos especializado (Bai, Yuan, Liu, Huang, & Feng, 2024; [Quintero et al., 2018](#ref-quintero-2018)).

A definição dos perfis de utilizador corresponde, por isso, a uma opção conceptual central. O sistema organiza-se em três perfis principais: administrador, técnico e utilizador. O perfil de administrador assegura a gestão global da plataforma, incluindo a criação de contas, a definição de permissões e a supervisão do ecossistema de configurações. O perfil técnico, pensado para profissionais intermédios, como protésicos, clínicos ou operadores especializados, permite criar, editar e acompanhar configurações próprias e, quando aplicável, aceder às configurações dos utilizadores sob sua responsabilidade. O perfil de utilizador corresponde ao nível mais restrito, centrado na consulta das suas configurações, no acompanhamento do processo e em interações delimitadas pelo sistema. Esta segmentação traduz uma lógica de controlo de acesso baseada em papéis, procurando equilibrar autonomia, segurança, inteligibilidade e responsabilidade distribuída.

Importa sublinhar que esta diferenciação não se limita a uma decisão administrativa. Ela participa diretamente na forma como a plataforma enquadra a personalização. Ao reservar certos parâmetros, decisões ou operações a perfis técnicos, o sistema reconhece que nem todos os aspetos da configuração devem ser apresentados ao utilizador final como escolhas livres. Em domínios sensíveis, como o das próteses, a experiência de uso beneficia quando a interface torna visível o processo, mas também quando delimita o campo de ação de forma coerente com critérios de supervisão, segurança e adequação funcional. A literatura sobre interfaces clínicas e interação em próteses inteligentes aponta precisamente para a necessidade de distinguir entre participação informada do utilizador e controlo técnico supervisionado, evitando tanto a opacidade excessiva como a transferência imprudente de responsabilidade para agentes não especializados ([Bai et al., 2024](#ref-bai-2024); [Quintero et al., 2018](#ref-quintero-2018)).

Deste modo, o enquadramento conceptual da plataforma articula três objetivos complementares: tornar a lógica paramétrica operável em ambiente web, estruturar a personalização como um processo progressivo e inteligível e distribuir o acesso às operações de acordo com papéis diferenciados. O valor da plataforma, nesta fase, não reside apenas em permitir editar parâmetros à distância, mas também em reconfigurar o próprio processo de personalização como uma sequência assistida, rastreável e criticável. É nessa articulação entre configurabilidade, mediação da interface e organização por perfis que a secção seguinte, dedicada à arquitetura geral do sistema, encontra a sua base conceptual.

### 5.2 Arquitetura geral do sistema

A arquitetura geral do sistema foi concebida como uma estrutura em camadas, organizada para separar a interface, a lógica de aplicação, a persistência de dados e os serviços complementares de apoio à configuração. Esta opção procura responder a um problema central do projeto: tornar operável um modelo paramétrico tecnicamente exigente num ambiente web sem concentrar, no mesmo ponto, responsabilidades de interação, cálculo geométrico, armazenamento e controlo de acesso. Em termos conceptuais, esta separação prolonga a lógica já discutida nas secções anteriores: a personalização digital exige sistemas suficientemente configuráveis para acomodar a variação, mas também suficientemente disciplinados para preservar a coerência, a rastreabilidade e a capacidade de manutenção ([Ozdemir et al., 2022](#ref-ozdemir-2022); [Lei et al., 2016](#ref-lei-2016)).

No lado do cliente, a aplicação funciona no navegador e integra os componentes responsáveis pela interface, pela recolha e edição de parâmetros, pela gestão do estado da sessão e pela visualização local dos modelos. No lado do servidor, um serviço desenvolvido em Node.js com Express assegura o fornecimento de ficheiros estáticos, o processamento de pedidos à API, a autenticação de utilizadores, a aplicação de permissões e a comunicação com a camada de persistência. Esta distribuição de responsabilidades evita que a interface dependa de processamento remoto contínuo para todas as operações e, simultaneamente, impede que tarefas sensíveis, como a gestão de utilizadores, o controlo de acessos e a comunicação com serviços externos, fiquem expostas diretamente no cliente. A arquitetura não corresponde, portanto, a uma simples divisão técnica entre “frente” e “retaguarda”, mas sim a uma estratégia de contenção da complexidade e de delimitação explícita de responsabilidades.

A camada de persistência assenta numa base de dados SQLite, utilizada para armazenar contas de utilizador, configurações guardadas, relações de atribuição técnica e tokens de autenticação. A escolha desta solução responde ao caráter prototípico e funcional do sistema nesta fase da investigação, privilegiando a leveza de implementação, a portabilidade e a facilidade de manutenção. As configurações paramétricas são armazenadas como estruturas JSON associadas a um modelo e a um utilizador, permitindo preservar diferentes instâncias de personalização, recuperá-las em momentos posteriores e compará-las como estados distintos do processo projetual. Deste modo, a base de dados não funciona apenas como repositório administrativo, mas também como infraestrutura que sustenta a continuidade, o versionamento prático e a rastreabilidade das variantes produzidas.

Um dos aspetos mais relevantes da arquitetura é que a renderização geométrica não é executada no servidor. Em vez disso, o cálculo e a geração da geometria tridimensional ocorrem localmente no navegador, por meio de um processo baseado em OpenSCAD, compilado para WebAssembly e executado em um Web Worker. Esta decisão reduz a carga computacional do backend, diminui a dependência de um serviço remoto de renderização e favorece uma interação mais imediata durante a edição paramétrica. Ao mesmo tempo, preserva-se uma fronteira clara: o servidor mantém-se responsável pela autenticação, armazenamento, gestão de configurações e intermediação de chamadas a serviços de inteligência artificial, enquanto o cliente assume a computação geométrica intensiva. A arquitetura resultante é, assim, híbrida: centraliza funções de controlo e persistência, mas distribui localmente a geração formal do modelo.

No plano da segurança e do controlo de acesso, a arquitetura incorpora autenticação baseada em JWT, utilização de tokens de atualização em cookies HttpOnly, validação de dados, limitação de pedidos e bloqueio explícito de ficheiros sensíveis. Estes mecanismos não devem ser entendidos como adições periféricas, mas como parte integrante do desenho do sistema, sobretudo num contexto em que múltiplos perfis de utilizador operam sobre configurações potencialmente sensíveis e em que a plataforma articula a autonomia de uso com a supervisão técnica. A literatura sobre interfaces de configuração em contexto protésico sublinha, precisamente, a importância de equilibrar a participação, a diferenciação de permissões e o enquadramento seguro das operações críticas ([Quintero et al., 2018](#ref-quintero-2018); [Bai et al., 2024](#ref-bai-2024)). Neste sentido, a arquitetura traduz uma opção por robustez e extensibilidade controlada: não procura apenas “ligar” componentes, mas estruturar um ecossistema técnico coerente com os requisitos de personalização assistida, gestão multiutilizador e futura evolução da plataforma.

### 5.3 Integração OpenSCAD via WebAssembly (WASM)

A integração do OpenSCAD por meio de WebAssembly constitui um dos elementos técnicos mais relevantes da plataforma, pois permite executar localmente, no navegador, um modelo paramétrico baseado em código, sem depender de um serviço externo de renderização contínua. O OpenSCAD funciona como linguagem e ambiente de modelação em que a geometria é definida por instruções escritas, parâmetros numéricos e relações explícitas entre componentes, em vez de resultar exclusivamente de manipulação gráfica direta. O WebAssembly (WASM), por sua vez, possibilita a execução de aplicações compiladas com desempenho próximo ao nativo no contexto da web. A articulação entre ambos torna viável um cenário particularmente pertinente para esta investigação: preservar a lógica algorítmica do modelo e, ao mesmo tempo, disponibilizá-la num ambiente de utilização mais acessível, orientado por uma interface ([Machado et al., 2019](#ref-machado-2019); [Nilsiam & Pearce, 2017](#ref-nilsiam-2017)).

Em termos operacionais, o processo organiza-se em uma cadeia relativamente clara. Os ficheiros .scad, que contêm a definição algorítmica do modelo, e os conjuntos de parâmetros produzidos pela interface são carregados no frontend. Esses elementos são depois encaminhados para um Web Worker, isto é, um processo separado da interface principal, capaz de executar tarefas pesadas em segundo plano. Nesse worker, a versão compilada do OpenSCAD em WASM interpreta o código, aplica os parâmetros recebidos e gera a geometria tridimensional correspondente. O resultado é então devolvido ao ambiente de visualização no navegador, onde o utilizador pode observar os efeitos das alterações introduzidas sem sair da plataforma nem recorrer a software CAD instalado localmente. Esta cadeia de parâmetros -> worker -> OpenSCAD em WASM -> geometria visível é central para o funcionamento do sistema, pois liga a edição, o cálculo e o feedback formal numa sequência rastreável.

Do ponto de vista metodológico, esta solução tem implicações importantes. Em primeiro lugar, preserva o estatuto do modelo paramétrico como especificação explícita e não como caixa negra geométrica. A plataforma não substitui o OpenSCAD por uma representação simplificada desligada do código; antes, torna o próprio núcleo algorítmico operável em ambiente web. Em segundo lugar, esta integração reduz a distância entre modelação e interação, permitindo que a exploração formal decorra num contexto mais observável e iterativo. O utilizador não necessita de dominar a sintaxe do OpenSCAD para beneficiar da estrutura paramétrica do modelo, mas essa estrutura continua a ser a base efetiva da geometria apresentada. Neste sentido, a plataforma atua como uma camada intermédia entre a disciplina técnica do código e a experiência configurável descrita na literatura sobre configuradores e sistemas de personalização digital ([Nilsiam & Pearce, 2017](#ref-nilsiam-2017); [Ozdemir et al., 2022](#ref-ozdemir-2022)).

Do ponto de vista técnico, o uso de Web Workers é especialmente relevante porque impede que a renderização bloqueie a interface principal. Em modelos geometricamente mais exigentes, o cálculo pode ser intensivo; se fosse executado diretamente na thread principal do navegador, comprometeria a fluidez da interação. Ao mover esse trabalho para um processo separado, a plataforma mantém uma experiência mais estável, mesmo quando a geração não é instantânea. A renderização permanece integralmente no lado do cliente, o que reforça a autonomia local do sistema e reduz o tráfego e a carga associados ao backend. Esta decisão complementa a arquitetura híbrida descrita na secção anterior: o servidor conserva funções de autenticação, persistência e mediação com serviços externos, enquanto o navegador assume a computação geométrica diretamente relacionada com a exploração paramétrica.

Esta integração tem ainda valor estratégico no contexto da investigação, pois aproxima a lógica da modelação baseada em código à acessibilidade operacional exigida por uma plataforma web. A literatura sobre OpenSCAD tem sublinhado precisamente a sua afinidade com fluxos repetíveis, configuradores digitais e a partilha de modelos paramétricos em ambientes abertos, ainda que, muitas vezes, fora de contextos protésicos especificamente clínicos ([Machado et al., 2019](#ref-machado-2019); [Nilsiam & Pearce, 2017](#ref-nilsiam-2017)). No presente projeto, a adoção de WASM não representa apenas uma decisão de engenharia para “correr código no browser”; representa a tentativa de integrar, numa mesma infraestrutura, a transparência do modelo paramétrico, a observabilidade da interação e a capacidade de atualização iterativa da geometria.

Não obstante as vantagens, esta solução introduz limitações que importa reconhecer. O desempenho da renderização depende da complexidade do modelo, dos valores paramétricos escolhidos e dos recursos do dispositivo do utilizador, podendo resultar em tempos de espera mais longos para geometrias mais exigentes. Acresce que o carregamento inicial do módulo WASM, a serialização de dados entre a interface e o worker e a própria conversão da saída geométrica para formatos visualizáveis introduzem sobrecarga que não existe da mesma forma em ambientes CAD locais dedicados. Assim, a integração de OpenSCAD via WebAssembly deve ser entendida como um compromisso tecnicamente situado: amplia a acessibilidade e a autonomia local, mas o faz dentro dos limites computacionais e operacionais do navegador. O valor da solução reside, por isso, menos numa promessa de desempenho absoluto e mais na capacidade de tornar executável, em ambiente web, um núcleo paramétrico explícito e criticável.

### 5.4 Estrutura funcional da plataforma

A estrutura funcional da plataforma organiza-se em um conjunto de módulos interligados que suportam o ciclo completo de configuração paramétrica: seleção do modelo, introdução e edição de parâmetros, visualização tridimensional, sugestões assistidas por IA, gestão de configurações e administração multiutilizador. Esta organização modular não serve apenas para distribuir funcionalidades; também torna o processo de personalização legível e sequencial. Em vez de expor o utilizador a um ambiente indiferenciado de opções, a plataforma reparte o trabalho por etapas e componentes com funções distintas, o que está de acordo com a literatura sobre configuradores digitais, segundo a qual a eficácia da personalização depende, em grande medida, da clareza com que o sistema delimita o espaço de ação disponível e articula feedback com decisão ([Ozdemir et al., 2022](#ref-ozdemir-2022); [Peixoto et al., 2025](#ref-peixoto-2025)).

O ponto de entrada do sistema é o módulo de seleção de modelos. Cada modelo é descrito por um ficheiro de configuração que inclui o identificador, a descrição, o ficheiro OpenSCAD associado e a lista de parâmetros editáveis. A partir dessa estrutura, a interface consegue gerar dinamicamente os controlos de edição necessários, como sliders, campos numéricos, caixas de seleção ou campos de texto. Esta opção reduz a rigidez do sistema e permite acomodar famílias distintas de modelos paramétricos sem exigir reprogramação manual de cada ecrã. Em termos funcionais, este módulo atua como mediador entre a biblioteca de modelos e a interface, convertendo uma estrutura técnica de ficheiros e parâmetros num ponto de entrada compreensível para a configuração.

O núcleo operativo da plataforma situa-se, depois, na articulação entre o módulo de edição paramétrica e o de visualização 3D. Quando os parâmetros são alterados, o sistema recompõe o código, aciona a renderização local e devolve ao utilizador a geometria atualizada. Esta ligação direta entre edição e pré-visualização é decisiva do ponto de vista funcional, pois transforma a manipulação de variáveis abstratas em observação imediata das suas consequências formais. Funções de reposição de valores por defeito, atualização incremental e exportação de ficheiros STL alargam esta utilidade para além da mera experimentação visual, aproximando a plataforma de um ambiente de prototipagem e de preparação para fabrico. A literatura sobre interfaces para configuração assistida em contexto protésico sugere precisamente que a legibilidade do processo melhora quando o utilizador consegue relacionar a ação, a consequência geométrica e a possibilidade de validação num mesmo circuito de interação ([Peixoto et al., 2025](#ref-peixoto-2025); [Quintero et al., 2018](#ref-quintero-2018)).

Sobre esta base opera o módulo de apoio por inteligência artificial, que introduz uma camada adicional de mediação sem substituir a lógica principal da configuração. A partir de uma descrição livre do utilizador, ou de medidas antropométricas parciais, a interface constrói dinamicamente um pedido que inclui o esquema atual do modelo selecionado: nomes dos parâmetros, legendas, tipos, limites mínimos e máximos e valores correntes. Esse pedido é enviado ao servidor por uma rota autenticada, que atua como intermediário entre a plataforma e o serviço externo de IA. A resposta esperada é um objeto JSON simples, composto apenas por pares parâmetro-valor. A aplicação aceita apenas chaves existentes no esquema, descarta parâmetros desconhecidos e aplica os valores resultantes aos controlos antes de acionar uma nova renderização em OpenSCAD/WebAssembly.

Esta arquitetura corrige uma fragilidade identificada numa versão anterior do sistema, em que o pedido à IA permanecia demasiado associado a um modelo já removido e podia induzir sugestões com nomes de parâmetros inexistentes. Ao ancorar a sugestão no esquema vivo do modelo ativo, a IA passa a operar sobre a mesma gramática paramétrica que a interface, os perfis antropométricos importados e o modelo OpenSCAD. O papel funcional deste módulo não é gerar autonomamente a prótese, mas sim ampliar a capacidade exploratória do sistema, sugerindo pontos de partida plausíveis e ajudando a reduzir a carga inicial de parametrização. Nesta perspetiva, o módulo de IA integra-se no fluxo como suporte à decisão, e não como instância soberana de configuração, o que mantém coerência com a lógica human-in-the-loop assumida no projeto.

Outro componente central é o módulo de gestão de configurações. A possibilidade de nomear, guardar, recuperar, atualizar e eliminar instâncias de personalização é particularmente relevante num processo iterativo, em que diferentes variantes podem corresponder a hipóteses sucessivas de trabalho e não apenas a estados finais. Funcionalmente, este módulo transforma a configuração de um ato momentâneo numa sequência acumulativa e rastreável, permitindo retomar versões anteriores, comparar alternativas e sustentar processos de revisão progressiva. Deste modo, a gestão de configurações não é uma simples conveniência de interface: é parte integrante da estrutura funcional que torna a personalização verificável e acumulável ao longo do tempo.

Por fim, a plataforma inclui um módulo administrativo e de controlo de acesso que suporta a organização multiutilizador. Este módulo assegura a criação de contas, a diferenciação de permissões, a atribuição de utilizadores a técnicos e a delimitação das ações acessíveis a cada perfil. A sua presença confirma que a estrutura funcional da plataforma não se esgota na manipulação de parâmetros e na visualização de formas; inclui também a gestão das relações entre agentes, das responsabilidades e dos níveis de intervenção. Neste sentido, a aplicação obtém sugestões paramétricas através do servidor, que se comunica com serviços externos por intermédio de um proxy seguro¹, mas enquadra essa capacidade dentro de uma estrutura funcional mais ampla, em que configuração, supervisão e persistência coexistem como partes de um mesmo sistema operativo.

¹ Entende-se por proxy seguro uma camada intermédia de comunicação que permite ao servidor gerir os pedidos enviados a serviços externos, protegendo credenciais sensíveis, controlando o acesso e reduzindo a exposição direta da aplicação a sistemas externos.

A biblioteca de modelos integrada na plataforma confirma esta lógica modular. Em vez de tratar a prótese como um único ficheiro estático, o sistema organiza diferentes famílias de mãos protésicas como modelos registados, cada uma com parâmetros, dependências, limites e modos de visualização próprios. Esta decisão permitiu comparar estratégias distintas de integração: modelos reconstruídos integralmente em OpenSCAD, modelos provenientes de geometrias existentes e modelos open source já paramétricos, mas não alinhados com a nomenclatura antropométrica da plataforma. A integração não consistiu, portanto, apenas em “carregar” ficheiros tridimensionais; consistiu em traduzir cada modelo para uma interface comum de parâmetros, mantendo as suas restrições mecânicas específicas.

No caso do Paraglider Hand, também conhecido como Flexible Flyer, a integração partiu de uma mão mecânica acionada pelo corpo, derivada da linhagem Phoenix e UnLimbited. O desafio principal não foi reconstruir a geometria dos dedos, já definida em OpenSCAD, mas alinhar a lógica original do modelo com os nomes canónicos usados pelo sistema. A palma passou a ser controlada pela largura metacarpal, enquanto os dedos foram associados a comprimentos digitais independentes. Esta separação foi importante porque a largura da palma e o comprimento dos dedos não variam necessariamente de forma proporcional. Ao mesmo tempo, a palma teve de manter escalonamento uniforme, uma vez que os furos cilíndricos para pinos metálicos não podem ser deformados em elipses sem comprometer a montagem. Assim, certas medidas, como o comprimento e a espessura da palma, foram mantidas como informação contextual para a IA e para o perfil antropométrico, mas não foram usadas como transformações geométricas ativas nesse modelo.

A integração do Paraglider também revelou limitações práticas da execução de OpenSCAD em WebAssembly. Alguns ficheiros originais usavam construções sintáticas não suportadas pela versão compilada para navegador, o que impediu a definição de módulos durante a renderização. A solução foi manter cópias corrigidas dos ficheiros necessários, preservar a origem do modelo e controlar explicitamente as dependências carregadas para o sistema virtual de ficheiros do navegador. Esta etapa teve relevância metodológica porque mostrou que a compatibilidade web não depende apenas da qualidade geométrica do modelo, mas também da forma como bibliotecas, ficheiros importados e variantes de sintaxe são organizados no fluxo digital.

O trabalho realizado sobre modelos do tipo Cyborg Beast/Flexy Hand teve uma função complementar. Estes modelos foram usados como base exploratória para testar uma reparametrização mais ampla, em que a geometria original foi reorganizada em torno de medidas antropométricas da palma, dos dedos, do punho e do membro residual. A versão antropométrica resultante não foi tratada como simples escala global: incorporou comprimentos digitais, espessuras estruturais, canais internos, parâmetros de hardware e dimensões de encaixe derivadas de medidas do antebraço. Essa experiência foi útil para clarificar a diferença entre adaptar um modelo existente por multiplicadores gerais e reconstruir a sua lógica dimensional em torno de uma estrutura antropométrica coerente. Mesmo quando determinados modelos permaneceram como material de desenvolvimento e comparação, contribuíram para estabilizar a taxonomia de parâmetros que a plataforma passou a exigir aos modelos ativos.

Em conjunto, estes casos mostram que a escalabilidade da plataforma depende menos da quantidade de modelos disponíveis e mais da existência de uma gramática comum de integração. Cada nova mão exige três operações: identificar quais parâmetros antropométricos são relevantes, decidir que parâmetros podem alterar a geometria sem quebrar interfaces mecânicas e declarar essas relações de forma compreensível para a interface, para o renderizador e para a camada de IA. A biblioteca de modelos torna-se, assim, um campo de validação técnica da própria arquitetura: quanto mais heterogéneos forem os modelos integrados, mais clara se torna a necessidade de separar dados antropométricos, regras geométricas, restrições de fabrico e sugestões assistidas.

### 5.5 Gestão de parâmetros, versões e escalabilidade

A gestão de parâmetros constitui uma das condições centrais para transformar um modelo paramétrico em um sistema utilizável e persistente. No caso da plataforma desenvolvida, essa gestão é operacionalizada através de ficheiros de configuração que descrevem cada parâmetro segundo atributos como nome, tipo, valor inicial, limites, incrementos e agrupamento temático. Esta estrutura não cumpre apenas uma função técnica de leitura na interface; formaliza a relação entre o código OpenSCAD, o espaço de variação permitido e os mecanismos de controlo disponibilizados ao utilizador. Em termos metodológicos, esta opção aproxima-se da lógica descrita na literatura sobre configuradores e personalização digital, segundo a qual a eficácia do sistema depende da capacidade de expor apenas parâmetros relevantes, dentro de limites inteligíveis e controlados, preservando a coerência interna do modelo-base ([Ozdemir et al., 2022](#ref-ozdemir-2022); [Lei et al., 2016](#ref-lei-2016)).

Ao descrever os parâmetros em estruturas independentes do código geométrico principal, a plataforma obtém duas vantagens. A primeira é a rastreabilidade: torna-se possível saber quais variáveis são editáveis, quais são os seus intervalos válidos e como se articulam com a interface. A segunda é a reconfigurabilidade do próprio sistema: a adição, remoção ou ajuste de parâmetros pode ser realizada sem reescrever integralmente a lógica de interação. Assim, a gestão de parâmetros funciona como uma camada intermédia entre a definição geométrica e a experiência de uso, permitindo que o modelo permaneça tecnicamente explícito sem exigir que o utilizador interaja diretamente com a sua sintaxe interna.

A gestão de versões manifesta-se, neste estágio do projeto, sobretudo por meio do armazenamento de configurações salvas. A plataforma permite conservar diferentes conjuntos de parâmetros associados ao mesmo modelo, atribuindo-lhes identificação própria, notas descritivas e associação a um utilizador específico. Embora esta solução ainda não corresponda a um sistema de versionamento completo nos moldes tradicionais do desenvolvimento de software, já suporta uma função projetualmente relevante: acompanhar o processo iterativo de configuração, preservar variantes e permitir a comparação entre estados sucessivos do mesmo artefacto. Cada configuração registada pode, assim, ser entendida como uma instância rastreável do processo de personalização, e não apenas como um ficheiro transitório. Esta capacidade é particularmente importante num contexto em que a personalização não é um ato único, mas uma sequência de aproximações, testes e revisões.

Do ponto de vista funcional, a persistência dessas configurações em estruturas JSON associadas a modelos e utilizadores reforça a continuidade entre interação, revisão e reutilização. O sistema deixa de operar apenas em tempo real e passa a acumular histórico operativo, possibilitando retomar soluções anteriores, documentar alternativas exploradas e preparar comparações futuras entre versões. Esta forma de versionamento prático é coerente com o caráter prototípico da plataforma: ainda não pretende substituir mecanismos mais sofisticados de gestão de revisões, mas fornece uma base suficiente para sustentar o acompanhamento iterativo do desenvolvimento e a análise reflexiva do processo.

Quanto à escalabilidade, a plataforma beneficia de uma arquitetura modular e orientada para configuração. A separação entre modelos, parâmetros, interface, autenticação e persistência permite acrescentar novos modelos em OpenSCAD, novos tipos de parâmetros ou novas rotinas de apoio sem reestruturar integralmente a aplicação. Na prática, a introdução de um novo modelo exige sobretudo a adição do ficheiro .scad correspondente e o respetivo registo em models-config.json, o que evidencia uma forma de escalabilidade baseada menos na duplicação de código e mais na extensão configurável. Esta característica é consistente com a literatura sobre sistemas paramétricos e famílias de produto, que associa robustez e expansão sustentável à qualidade das estruturas relacionais, e não ao aumento indiscriminado de opções ou de módulos independentes ([Lei et al., 2016](#ref-lei-2016); [Ozdemir et al., 2022](#ref-ozdemir-2022)).

Todavia, esta escalabilidade deve ser analisada criticamente. O recurso ao SQLite é adequado a um protótipo funcional com baixa ou média concorrência, mas poderá revelar limitações em cenários de utilização mais intensiva, com múltiplos utilizadores simultâneos, maior volume de configurações ou necessidades mais exigentes de auditoria e sincronização. De forma semelhante, a renderização local via WASM, embora eficaz em muitos contextos, depende do desempenho do dispositivo do utilizador, o que introduz variabilidade na experiência e impõe limites ao crescimento indiscriminado da complexidade geométrica. Assim, a escalabilidade da plataforma não pode ser reduzida à possibilidade de adicionar funcionalidades ou modelos; envolve também a capacidade de sustentar esse crescimento sem perder legibilidade, desempenho, segurança e manutenibilidade.

Neste sentido, a secção confirma uma conclusão importante para o projeto: a gestão de parâmetros, de configurações e de expansão futura deve ser entendida como parte integrante da própria lógica de design da plataforma. Não se trata apenas de resolver problemas infraestruturais posteriores, mas de reconhecer que a configurabilidade, a persistência e o crescimento controlado são condições para que a personalização paramétrica permaneça tecnicamente viável e metodologicamente rastreável ao longo do desenvolvimento.

---

## Capítulo 6 — Integração da Inteligência Artificial

### 6.1 Papel da IA no sistema proposto

A integração da inteligência artificial no sistema proposto deve ser enquadrada com precisão. A literatura recente mostra que a IA já ocupa um lugar relevante no domínio das próteses, mas esse lugar permanece concentrado sobretudo em tarefas de controlo, interpretação de biosinais, reconhecimento de gestos e adaptação funcional, e menos na estruturação integral de fluxos de personalização paramétrica. Revisões sobre próteses de membro superior e sobre próteses e ortóteses indicam que a aprendizagem automática é aplicada principalmente à classificação de sinais EMG, à inferência de intenção motora e à melhoria do desempenho operativo do dispositivo (Choo e Chang, 2023; Terrazas-Rodas e Carrión-Pérez, 2022; Hachoumi, Laabidi e Eddabbah, 2026; Batista, Vieira e Gaspar, 2025). Em contrapartida, continuam pouco consolidadas as abordagens que articulam, no mesmo sistema, a entrada antropométrica, o modelo paramétrico explícito, a sugestão assistida de parâmetros e a supervisão técnica. Esta lacuna é central para a presente investigação, pois permite situar a proposta não como repetição do estado da arte, mas como tentativa de ligação entre componentes que a literatura tende a desenvolver de forma fragmentada.

Neste enquadramento, o papel da IA não consiste em substituir o processo de projeto, a lógica geométrica nem a validação técnica. A sua função é a de uma camada complementar de apoio à configuração, operando sobre uma base paramétrica já definida. A literatura sobre modelação paramétrica aplicada a próteses personalizadas e sobre fabrico aditivo mostra que há um fundamento técnico robusto para construir geometrias configuráveis com base em regras explícitas, parâmetros dimensionais e relações geométricas controladas. Estudos sobre próteses paramétricas para diferentes níveis de amputação da mão, sobre customização de dedos protésicos por modelação paramétrica e sobre sockets personalizados para próteses transradiais demonstram que a personalização pode ser estruturada por meio de modelos explícitos e fluxos CAD/CAM ajustáveis ([da Silveira Romero et al., 2025](#ref-da-silveira-romero-2025); [Lim et al., 2018](#ref-lim-2018); [Saldarriaga et al., 2024](#ref-saldarriaga-2024)). O sistema aqui proposto parte precisamente desta premissa: a geometria não é gerada de forma opaca por um modelo autónomo, mas sim por um modelo paramétrico explícito, definido em OpenSCAD e manipulável por meio de parâmetros rastreáveis.

É neste ponto que a IA assume uma função específica. Em vez de atuar como gerador integral da forma, atua como um mecanismo de mediação entre os dados de entrada e a exploração inicial do espaço paramétrico. O seu papel é apoiar a tradução de informação antropométrica, de preferências funcionais e de critérios de fabrico em sugestões paramétricas plausíveis, reduzindo a complexidade associada à definição manual de valores iniciais e à navegação em sistemas com múltiplas dependências internas. Esta posição aproxima-se de abordagens data-driven orientadas a melhorar a adaptação, o conforto e a adequação estrutural, sem eliminar a necessidade de interpretação humana ([Gu et al., 2024](#ref-gu-2024)). Em termos projetuais, a IA funciona como instrumento de apoio à decisão e à iteração: propõe pontos de partida, ajuda a comparar cenários e acelera os ciclos de teste, sem substituir a estrutura técnica do sistema. Entre os antecedentes mais próximos desta lógica encontram-se trabalhos que combinam personalização anatómica, modelação paramétrica, fabrico aditivo e componentes inteligentes, como o estudo de [Romero et al. (2025)](#ref-da-silveira-romero-2025), bem como quadros de otimização estrutural orientados por dados anatómicos e constrangimentos de adaptação, como o proposto por [Gu et al. (2024)](#ref-gu-2024).

Esta leitura é coerente com a arquitetura da plataforma descrita no capítulo anterior. O sistema separa a camada de interface, a lógica paramétrica, a renderização local em WebAssembly e a comunicação controlada com serviços externos de IA. Tal organização é metodologicamente relevante porque preserva a rastreabilidade entre a entrada, a sugestão e o resultado geométrico. Em vez de encerrar o processo num modelo generativo pouco transparente, o sistema mantém a IA numa posição assistiva e supervisionada: sugere, mas não determina autonomamente; apoia, mas não valida; acelera, mas não substitui o julgamento técnico. Esta opção é particularmente importante, considerando que a supervisão clínica ou técnica permanece limitada em vários estudos que já articulam modelação digital, CAD, IA, co-design assistido ou impressão 3D ([Romero et al., 2025](#ref-da-silveira-romero-2025); [Elbreki et al., 2022](#ref-elbreki-2022); [Idris et al., 2024](#ref-idris-2024)). O valor da IA reside, assim, menos na promessa de automatização total e mais na sua capacidade de reforçar um processo de personalização já estruturado por lógica paramétrica explícita, por requisitos de fabrico e por responsabilidade humana.

### 6.2 IA na parametrização, personalização e apoio à decisão

No domínio da parametrização, a inteligência artificial torna-se mais relevante quando opera sobre uma estrutura geométrica previamente formalizada, em vez de tentar substituí-la. Em sistemas como o aqui proposto, isso significa receber dados antropométricos, requisitos funcionais e restrições de fabrico e convertê-los em sugestões iniciais para os parâmetros já definidos no modelo. A literatura sobre próteses paramétricas e personalização anatómica mostra que a customização eficaz depende de relações explícitas entre medidas, proporções e componentes geométricos, e não apenas da introdução isolada de valores numéricos ([Saldarriaga et al., 2024](#ref-saldarriaga-2024); [da Silveira Romero et al., 2025](#ref-da-silveira-romero-2025)). Neste enquadramento, a IA não elimina a lógica determinística do modelo paramétrico; antes, aumenta a sua operabilidade, ajudando a propor intervalos plausíveis, combinações coerentes entre variáveis e pontos de partida mais ajustados ao caso específico.

No plano da personalização, esta mediação é importante porque a adaptação de uma prótese não se reduz ao escalonamento uniforme da forma. A literatura indica que diferentes parâmetros podem ter de ser controlados de forma independente para respeitar as proporções anatómicas, o conforto, a mobilidade e os requisitos de montagem. O estudo de [Lim et al. (2018)](#ref-lim-2018), por exemplo, demonstra que o comprimento e a largura de um dedo protésico não devem ser ajustados como se fossem variáveis que variam de forma linear e proporcional, reforçando a necessidade de parametrizações mais finas do que simples operações de escala. De forma convergente, [Gu et al. (2024)](#ref-gu-2024) mostram que abordagens data-driven podem apoiar a adaptação estrutural e a melhoria da vestibilidade, sugerindo que métodos inteligentes podem ser úteis para antecipar as relações entre geometria, desempenho e conforto. Para o sistema proposto, isto significa que a IA pode funcionar como uma camada de inferência preliminar sobre um espaço paramétrico já estruturado, e não como um gerador autónomo de soluções.

A operacionalização desta lógica ocorre em dois objetos distintos. O primeiro é um vetor numérico de parâmetros geométricos, consumido diretamente pela interface e pelos modelos OpenSCAD. O segundo é um contexto semântico para a IA, que descreve a origem das medições, campos em falta, incerteza, valores atípicos, tolerâncias, hardware selecionado e notas sobre parâmetros derivados. Esta separação é importante porque impede confundir cálculo geométrico com raciocínio assistido: os parâmetros numéricos alimentam o modelo; o contexto semântico ajuda a IA a explicar, ponderar ou sugerir ajustes, mas não substitui as regras determinísticas que geram a geometria.

O apoio à decisão emerge precisamente desta capacidade de transformar dados de entrada em cenários comparáveis. Em vez de produzir uma única configuração apresentada como “ótima”, a integração da IA revela maior utilidade quando ajuda a explicitar compromissos entre robustez, leveza, amplitude de ajuste, rapidez de fabrico, facilidade de montagem e adequação anatómica. Esta lógica está alinhada com exemplos recentes de integração entre digitalização, modelação paramétrica, fabrico aditivo e sistemas inteligentes, como o trabalho de [Romero et al. (2025)](#ref-da-silveira-romero-2025), ainda que aí a componente de IA esteja mais ligada ao controlo mioelétrico do que à sugestão paramétrica em ambiente web. A pertinência desse precedente reside menos na equivalência técnica direta e mais no facto de mostrar que a personalização digital e a camada inteligente podem coexistir no mesmo fluxo, desde que cada componente mantenha uma função claramente delimitada.

É por isso que, nesta investigação, a personalização assistida por IA deve ser entendida como uma prática de human-in-the-loop. O sistema não procura substituir o protésico, o designer ou o utilizador informado, mas sim ampliar a sua capacidade de análise e de exploração. A IA pode sugerir configurações iniciais, organizar alternativas, sinalizar dependências entre parâmetros e tornar mais legíveis certas consequências projetuais; a aceitação final, porém, continua dependente de verificação técnica e de julgamento contextual. Deste modo, a parametrização assistida por IA não corresponde a uma automatização cega da personalização, mas a um mecanismo de apoio à decisão que atua sobre uma base geométrica explícita, rastreável e tecnicamente verificável.

### 6.3 Validação antropométrica assistida por IA no sistema

A validação antropométrica assistida por IA realizada no sistema deve ser entendida como validação interna de plausibilidade e de coerência paramétrica, não como validação clínica da prótese final. O objetivo foi verificar se uma pessoa sem conhecimento técnico de medições da mão poderia descrever um caso em linguagem comum e obter, como ponto de partida, um conjunto de parâmetros anatómica e tecnicamente plausível para o modelo Flexy Beast. Esta distinção é metodologicamente essencial: a plataforma consegue testar conformidade com o esquema, intervalos declarados, proporcionalidade digital e coerência de lateralidade, mas não consegue, por si só, provar conforto, segurança, desempenho funcional ou adequação terapêutica.

O ensaio foi estruturado a partir da cadeia funcional implementada na plataforma: descrição livre do caso, construção do pedido no frontend com injeção do esquema vivo do modelo, chamada autenticada à rota de sugestão por IA, resposta JSON com valores paramétricos, filtragem de chaves desconhecidas e aplicação dos valores válidos aos controlos do modelo. Esta arquitetura tem uma consequência importante: a IA não trabalha sobre uma lista genérica de medidas, mas sobre os parâmetros efetivamente disponíveis no modelo ativo, incluindo nomes exatos, legendas, limites e valores correntes. Assim, a validação não incidiu apenas sobre os números sugeridos, mas também sobre a capacidade do fluxo de manter continuidade entre linguagem natural, estrutura antropométrica, interface e geração geométrica.

Foram definidos cinco critérios de verificação. O primeiro foi a conformidade com o esquema: a saída deveria ser JSON válido, conter apenas nomes de parâmetros existentes e respeitar os limites mínimos e máximos declarados. O segundo foi a proporcionalidade dos dedos, exigindo uma ordenação anatómica plausível, com o dedo médio como referência mais longa, o dedo mínimo como mais curto e o polegar abaixo do comprimento do dedo médio. O terceiro foi a plausibilidade adulta, usando como referência os intervalos antropométricos canónicos já adotados no sistema. O quarto foi a adequação etária, sobretudo em perfis infantis ou adolescentes. O quinto foi a lateralidade em casos de amputação unilateral, verificando se o parâmetro de espelhamento produzia a mão do lado amputado e não uma cópia do lado medido.

O primeiro conjunto experimental usou cinco perfis sintéticos descritos apenas por indicadores populacionais indiretos, como idade, sexo, altura, peso, país, envergadura ou constituição física, sem qualquer medição direta da mão. Este cenário é relevante porque corresponde ao caso de menor literacia técnica: o utilizador não sabe medir a mão com rigor, mas consegue fornecer informação demográfica geral. Nas cinco situações, a IA produziu valores dentro dos limites do modelo, manteve a ordem anatómica dos dedos e gerou dimensões compatíveis com a idade e a constituição descritas. A redução espontânea de parâmetros de hardware num perfil infantil também mostrou que o modelo de linguagem usou as legendas do esquema, e não apenas os nomes técnicos dos parâmetros.

O segundo conjunto experimental avaliou três níveis de riqueza de entrada em cenários de amputação unilateral. Num caso com medições completas da mão intacta, os valores fornecidos foram preservados de forma literal e o sistema sugeriu a mão oposta. Num caso parcial, com apenas a largura da palma e dados demográficos, a medida fornecida foi mantida e as dimensões em falta foram estimadas de modo proporcional. Num caso apenas demográfico, a IA gerou um conjunto completo de medidas plausíveis. Nos três casos, a lateralidade sugerida foi correta. Este resultado é relevante porque mostra que a IA consegue degradar o comportamento de forma gradual: usa medições diretas quando existem, ancora estimativas em dados parciais e recorre a normas populacionais quando só há descrição geral.

Os resultados devem, contudo, ser lidos com cautela. A execução documentada corresponde a uma amostra representativa, não a uma caracterização estatística completa da distribuição de saídas. A repetição do mesmo perfil produziu variações pequenas, na ordem de poucos milímetros, preservando os invariantes anatómicos e os limites do modelo; ainda assim, essa variabilidade confirma que a componente de IA é estocástica. Também se observou uma forma de variabilidade estrutural: em algumas execuções, certos parâmetros de hardware foram emitidos explicitamente; noutras, foram omitidos, deixando o valor corrente do modelo. Ambas as respostas são aceitáveis no contrato atual, mas reforçam a necessidade de avaliar propriedades invariantes, e não valores exatos isolados.

A principal fragilidade identificada prende-se com a lateralidade. Embora os ensaios tenham produzido o lado correto, a regra de espelhamento foi inferida pelo modelo a partir da linguagem natural, e não imposta explicitamente no pedido. Esta situação é aceitável como evidência preliminar de capacidade inferencial, mas é insuficiente como salvaguarda de um parâmetro crítico: uma prótese gerada para o lado errado é inutilizável e o erro pode não ser imediatamente evidente para um utilizador não especializado. Por isso, a evolução do sistema deve incluir uma instrução explícita sobre mão intacta, lado amputado e espelhamento, bem como validação no servidor por esquema JSON e reenvio automático do pedido quando a saída não cumprir o contrato esperado.

A principal conclusão desta validação é que a IA pode cumprir uma função útil de acessibilidade paramétrica: transformar descrições incompletas e não técnicas em pontos de partida editáveis, coerentes e auditáveis. No entanto, a sua utilidade depende da arquitetura que a contém. A sugestão só é metodologicamente defensável porque está ancorada no esquema do modelo, limitada por intervalos, filtrada pela interface e sujeita a revisão humana. Deste modo, a validação antropométrica assistida por IA contribui para reduzir a barreira inicial de configuração e para tornar a parametrização mais acessível, mas não substitui medição direta, avaliação técnica, prototipagem física nem validação clínica.

### 6.4 Ajuste, validação e limitações éticas e técnicas

A introdução de IA num sistema deste tipo exige distinguir claramente entre sugestão paramétrica, ajuste efetivo e validação final. Uma recomendação produzida por um modelo de IA pode ser útil como ponto de partida, mas não equivale a uma prova de adequação funcional, de conforto ergonómico ou de segurança estrutural. O ajuste real de uma prótese depende sempre de confirmação em contexto técnico e, idealmente, de iterações de teste, observação e refinamento. Por essa razão, as saídas da IA devem ser entendidas como hipóteses operativas sujeitas a validação posterior, e não como prescrições definitivas.

Do ponto de vista técnico, subsistem limitações significativas. A IA pode produzir sugestões plausíveis, mas inadequadas para casos extremos, perfis antropométricos pouco representados ou combinações paramétricas fora da distribuição esperada. Pode também introduzir inconsistências difíceis de detetar se a sua saída não for confrontada com restrições geométricas, limites de fabrico e critérios funcionais explícitos. Assim, a integração robusta da IA depende da existência de salvaguardas no próprio sistema: limites paramétricos, validação de intervalos, verificação de coerência entre módulos, comparação entre alternativas e supervisão humana capaz de identificar quando uma sugestão é tecnicamente infundada ou insuficientemente justificada. Esta necessidade de enquadramento crítico é coerente com a literatura sobre explicabilidade e responsabilidade no design assistido por IA, que sublinha a importância de não tratar o modelo algorítmico como uma caixa-preta autojustificada ([Panchal et al., 2019](#ref-panchal-2019); [Yüksel et al., 2023](#ref-yuksel-2023)).

As limitações éticas são igualmente centrais. Num domínio associado a dispositivos personalizados e potencialmente sensíveis, importa evitar a recolha excessiva de dados, a exposição desnecessária de informação pessoal e a falsa perceção de objetividade algorítmica. Mesmo quando o sistema trabalha com dados antropométricos não clínicos ou em cenários experimentais, a sua arquitetura deve assumir princípios de minimização de dados, controlo de acesso e transparência quanto ao papel efetivo da IA. O utilizador deve compreender que está perante um sistema de apoio à decisão e não perante uma autoridade clínica autónoma. Esta clareza é essencial para evitar deslocamentos indevidos de responsabilidade e definir corretamente o escopo da ferramenta.

Por fim, subsiste uma limitação metodológica mais ampla: a qualidade da IA depende da qualidade das estruturas em que se insere. Sem modelos paramétricos bem definidos, sem critérios de validação claros e sem dados suficientemente representativos, a IA tende a amplificar incerteza em vez de a reduzir. Neste sentido, a sua integração só se torna relevante quando articulada com uma base projetual explícita, com procedimentos de verificação e com uma compreensão crítica das suas margens de erro. A principal contribuição da IA para o sistema proposto não reside, portanto, numa promessa de automatização total, mas na possibilidade de reforçar processos de personalização e decisão, desde que permaneça enquadrada por regras, validação e responsabilidade humanas.

---

## Capítulo 7 — Interface, Interação e Experiência de Utilização

### 7.1 Estratégia de interação e decisões de UI/UX

A estratégia de interação da plataforma foi definida a partir de um problema central: tornar utilizável um sistema de modelação paramétrica baseado em código sem expor o utilizador à complexidade direta do OpenSCAD. Em vez de apresentar a lógica algorítmica do modelo como interface principal, a aplicação organiza a interação em torno de ações reconhecíveis e progressivas, como selecionar um modelo, introduzir dados antropométricos, ajustar parâmetros, observar o resultado e guardar versões. Esta opção traduz uma decisão de UI/UX deliberada: a interface não procura ocultar a natureza técnica do sistema, mas reconfigurá-la em operações compreensíveis, sequenciais e verificáveis, em linha com abordagens que privilegiam a clareza do onboarding, a navegação guiada e a redução da carga interpretativa em plataformas de personalização protésica ([Colombo et al., 2015](#ref-colombo-2015); [Peixoto et al., 2025](#ref-peixoto-2025)).

Do ponto de vista estrutural, a interface assenta numa lógica de composição modular e orientada por tarefa. O utilizador não enfrenta um ambiente tridimensional aberto nem um editor de código, mas sim um conjunto de módulos de interação cuja organização corresponde a etapas reconhecíveis do processo de configuração. A seleção do modelo funciona como ponto de entrada; os parâmetros surgem depois como elementos editáveis com correspondência direta a propriedades geométricas; a visualização tridimensional atua como mecanismo de feedback contínuo; e as ações de guardar, recuperar ou exportar prolongam o processo para além do momento de configuração imediata. Esta organização procura reduzir carga cognitiva, evitar navegação errática e manter uma relação legível entre intenção, ação e consequência formal. A literatura revisada sugere precisamente que sistemas de configuração mais eficazes tendem a separar a visualização, o ajuste e a validação em camadas de interação mais inteligíveis, quer em plataformas web orientadas ao utilizador final, quer em interfaces destinadas a profissionais de ajuste protésico ([Peixoto et al., 2025](#ref-peixoto-2025); [Quintero et al., 2018](#ref-quintero-2018)).

Uma decisão particularmente relevante reside na forma como a interface traduz a lógica paramétrica em linguagem operacional. Cada controlo não representa apenas um valor numérico isolado, mas também um ponto de acesso a relações geométricas que permanecem definidas no modelo. Em termos de UI/UX, isto significa que a plataforma deve tornar editável apenas o que pode ser interpretado, observado e, idealmente, revisto de forma responsável. A estratégia de interação não consiste, portanto, em maximizar liberdade aparente, mas em expor uma parte controlada do espaço de variação. Esta contenção é importante porque, em sistemas configuráveis aplicados a próteses, excesso de liberdade pode gerar combinações pouco inteligíveis, tecnicamente frágeis ou difíceis de validar. A interface atua como filtro e mediadora: aumenta a acessibilidade sem comprometer a coerência interna do modelo paramétrico.

Outra decisão relevante diz respeito à articulação entre a edição paramétrica e a pré-visualização. A renderização local via WebAssembly permite que a resposta visual decorra da própria lógica geométrica do sistema, e não de imagens estáticas ou de simplificações visuais desconexas do modelo. Em termos de experiência, isto reforça a sensação de continuidade entre o controlo paramétrico e a forma observada. Ao mesmo tempo, o uso de Web Workers protege a interface de bloqueios excessivos durante operações mais pesadas, contribuindo para uma interação mais estável e previsível. A experiência não é instantânea em todos os casos, mas a arquitetura foi concebida para que os tempos de espera sejam compreendidos como parte do processamento geométrico real, e não como uma falha arbitrária da interface. A importância deste feedback iterativo, da visualização em tempo real e de formas de manipulação mais naturais é coerente com trabalhos que articulam configuração assistida, visualização e ajuste progressivo em contextos protésicos, ainda que, muitas vezes, fora de plataformas web puras (Abbas Alili et al., 2023; [Colombo et al., 2015](#ref-colombo-2015); [Peixoto et al., 2025](#ref-peixoto-2025)).

Em termos de linguagem visual e de uso, a plataforma privilegia a clareza funcional em relação à exuberância formal. Isto é coerente com o contexto do projeto: trata-se de uma ferramenta de configuração protésica, não de um configurador lúdico ou promocional. Assim, as decisões de UI/UX visam favorecer a legibilidade, a consistência entre os controlos, a previsibilidade das ações e a rastreabilidade das alterações. O valor da interface não reside apenas na aparência, mas na sua capacidade de mediar, com o mínimo de ambiguidade possível, a passagem entre os dados do utilizador, as regras paramétricas, a assistência algorítmica e o resultado tridimensional. Essa necessidade de clareza torna-se ainda mais evidente quando a literatura sobre próteses inteligentes sublinha a importância de equilibrar a autonomia do utilizador, os mecanismos de supervisão e a diferenciação de permissões entre utilizadores e profissionais ([Bai et al., 2024](#ref-bai-2024); [Quintero et al., 2018](#ref-quintero-2018)).

Deste modo, a estratégia de interação adotada não deve ser lida apenas como um conjunto de escolhas de interface, mas como uma decisão metodológica sobre a forma de tornar o processo de personalização observável, configurável e criticável. A UI/UX participa diretamente na construção do sistema, atuando como infraestrutura de mediação entre o conhecimento técnico, os dados individuais e a decisão projetual. O seu objetivo não é simplificar artificialmente o problema, mas organizar a complexidade de forma inteligível, preservando continuidade com a lógica paramétrica do modelo e com o enquadramento assistivo da IA discutido no capítulo anterior.

### 7.2 Experiência do designer e do utilizador final

A experiência do designer, técnico ou clínico que utiliza a plataforma distingue-se estruturalmente da do utilizador final, embora ambas se desenvolvam sobre a mesma infraestrutura digital. A literatura analisada sugere que esta diferença não decorre apenas de níveis distintos de literacia técnica, mas também do próprio tipo de decisão que cada agente é chamado a tomar. Em sistemas de personalização protésica, diferentes domínios de configuração exigem distribuições distintas de autoridade. Quando estão em causa parâmetros ligados à geometria do encaixe, à biomecânica, à tolerância dos tecidos ou à viabilidade de fabrico, o papel do profissional tende a ser dominante, pois envolve interpretação especializada, validação contextual e responsabilidade técnica. Em contrapartida, quando a configuração incide sobre preferências de controlo, inteligibilidade do sistema ou aspetos estéticos mais diretamente experienciados pelo utilizador, a participação deste torna-se mais substantiva. O contraste entre estes domínios é central para compreender a diferenciação entre perfis de uso, ainda que a literatura direta sobre plataformas paramétricas para o membro superior permaneça escassa e muitas conclusões tenham de ser complementadas por evidência transferível de contextos adjacentes ([Cordella et al., 2016](#ref-cordella-2016); [Saldarriaga et al., 2024](#ref-saldarriaga-2024)).

Para o designer, protésico ou clínico, a plataforma funciona sobretudo como um ambiente de trabalho orientado à configuração, ao teste, à comparação de alternativas e à supervisão do processo. O interesse principal deste perfil não está apenas em “ver” a prótese, mas em compreender como os parâmetros se relacionam, quais dependências estruturais existem entre dimensões e quais efeitos pequenas alterações podem produzir na geometria final ou no comportamento do sistema. A evidência transferível proveniente de plataformas de configuração e afinação em contexto protésico indica que profissionais valorizam interfaces que reduzam tempo de ajuste, tornem o espaço paramétrico mais interpretável e mantenham uma continuidade suficiente com o raciocínio clínico ou técnico habitual, incluindo ambientes em que conhecimento especializado é codificado em regras, sugestões iniciais ou ferramentas de comparação ([Colombo et al., 2015](#ref-colombo-2015); [Quintero et al., 2018](#ref-quintero-2018); [Bai et al., 2024](#ref-bai-2024)). Contudo, essa mesma literatura mostra também que a digitalização não aumenta automaticamente a confiança profissional: quando o sistema elimina pistas tácteis, empíricas ou processuais importantes, pode igualmente restringir certas formas de saber prático, como sugere a literatura sobre retificação digital e workflows CAD/CAM.

Para o utilizador final, por outro lado, a experiência tende a ser mais centrada na compreensibilidade, na confiança e na perceção de participação. Mesmo quando a pessoa não manipula diretamente todos os parâmetros, a possibilidade de visualizar o modelo, reconhecer alterações e acompanhar o processo de personalização torna a configuração menos opaca. A interface ajuda, assim, a transformar essa adaptação de uma decisão técnica distante em um processo parcialmente observável e inteligível. Este aspeto é particularmente relevante num domínio em que a aceitação de uma prótese não depende apenas do desempenho funcional, mas também da perceção de adequação, de participação e de controlo sobre o resultado. A literatura revisada sugere, de forma consistente, que a inteligibilidade da lógica do sistema influencia a experiência de uso: quando o sistema torna mais visíveis os efeitos das ações, os limites das escolhas ou a relação entre input e comportamento, tende a aumentar tanto a capacidade de uso quanto a confiança subjetiva. Plataformas de personalização estética e sistemas com uma visualização mais explícita do espaço de decisão sugerem, precisamente, que a agência do utilizador cresce quando o domínio editável é legível e de baixo risco ([Peixoto et al., 2025](#ref-peixoto-2025)).

Esta diferenciação torna-se mais clara quando se distinguem três domínios de personalização que a literatura tende a tratar de forma distinta. No primeiro, correspondente à geometria do encaixe e ao ajustamento biomecânico, predomina uma lógica clínica: a pessoa fornece feedback sobre conforto, tolerância ou preferência, mas a decisão permanece concentrada em quem detém competência técnica e responsabilidade pela validação. No segundo, correspondente à personalização do controlo e à afinação de sistemas interativos, a autoridade do utilizador tende a aumentar, porque só ele pode avaliar de forma imediata a sensação de controlo, a carga cognitiva ou a adequação do comportamento do sistema em uso. No terceiro, ligado à personalização estética e identitária, a literatura sugere que a autonomia dessa participação pode ser mais ampla, precisamente porque o risco clínico e biomecânico é menor e o critério de adequação é mais diretamente experienciado pelo próprio. Esta distinção é importante porque impede tratar a “participação do utilizador” como uma categoria homogénea.

A coexistência destes perfis e domínios justifica a adoção de permissões diferenciadas e de uma experiência graduada por papéis. O sistema não distribui o mesmo poder de edição a todos os agentes, pois isso reduziria a segurança, a coerência e a legibilidade do processo. Em vez disso, estrutura diferentes níveis de acesso, permitindo que determinadas ações sejam reservadas a perfis técnicos, enquanto outras se mantêm acessíveis ao utilizador que acompanha a sua configuração. Esta diferenciação não deve ser entendida como uma limitação arbitrária, mas como uma decisão de desenho que procura equilibrar autonomia, segurança e responsabilidade. A literatura recente sobre próteses inteligentes e interfaces configuráveis aponta no mesmo sentido, defendendo modelos de controlo em que parâmetros críticos permanecem sob supervisão profissional, enquanto ajustes mais circunscritos podem tornar-se acessíveis ao utilizador final ([Bai et al., 2024](#ref-bai-2024); [Quintero et al., 2018](#ref-quintero-2018)).

Do ponto de vista da experiência global, a plataforma revela-se mais forte quando entendida como um espaço de colaboração assimétrica. O designer ou técnico dispõe de uma ferramenta que acelera iterações, estrutura a exploração paramétrica e apoia decisões de maior responsabilidade; o utilizador final ganha maior transparência, inteligibilidade e possibilidade de acompanhamento; e o sistema, no seu conjunto, passa a oferecer uma cadeia de interação mais clara entre o conhecimento especializado e a necessidade individual. A utilização da plataforma não se resume, por isso, à ergonomia dos ecrãs, mas à forma como distribui a agência entre diferentes participantes no processo de personalização. Esta leitura é consistente com abordagens human-in-the-loop, nas quais as preferências do utilizador, o ajustamento algorítmico e a supervisão profissional coexistem de forma hierárquica e não mutuamente exclusiva, ao mesmo tempo que a literatura mais ampla sobre fabrico digital em próteses continua a assinalar lacunas de formação, validação longitudinal e comparação sistemática entre workflows ([Alili et al., 2023](#ref-alili-2023); [Oldfrey et al., 2024](#ref-oldfrey-2024)). É precisamente essa distribuição desigual, mas intencional, de acesso, interpretação e decisão que prepara a questão seguinte: não apenas quem usa a plataforma, mas também de que modo ela própria medeia o processo de design.

### 7.3 Mediação do processo de design e reflexão crítica

O contributo mais relevante da interface não reside apenas em permitir editar parâmetros, mas também em mediar o próprio processo de design. A plataforma introduz uma camada intermédia entre o modelo algorítmico, a decisão técnica e a interpretação do utilizador, reorganizando o desenvolvimento da prótese como uma sequência de interações assistidas. Esta mediação é importante porque reduz a dependência de manipulação direta do código, mas também porque explicita que a personalização não é um ato instantâneo: trata-se de uma dinâmica iterativa de leitura de dados, proposta de configuração, avaliação visual, revisão crítica e eventual exportação para fabrico. A literatura revisada reforça que esta dimensão processual não constitui mero efeito secundário da interface, mas sim parte central do modo como sistemas digitais desta natureza distribuem trabalho, autoridade e visibilidade entre diferentes agentes. Em vez de apenas executar decisões previamente tomadas, a plataforma ajuda a estruturar quando, como e por quem essas decisões se tornam possíveis.

Neste sentido, a interface funciona como um dispositivo epistemológico, e não apenas operacional. Ela condiciona a forma como o problema é visto, como as alternativas são exploradas e como as decisões são justificadas. Ao disponibilizar parâmetros editáveis, visualização tridimensional, sugestões assistidas por IA e gestão de versões, a plataforma torna o trabalho projetual mais estruturado e rastreável. Contudo, essa mesma estrutura também estabelece limites: o utilizador explora o espaço de soluções que o modelo e a interface permitem. A mediação digital aumenta a capacidade de ação, mas também enquadra e delimita o campo do possível. A literatura revisada sugere precisamente que as plataformas mais relevantes neste domínio operam por mecanismos concretos de mediação: controlo diferenciado de permissões, exposição seletiva de variáveis, pontos de partida algorítmicos, visualização orientada por problema e formas de supervisão embutidas na própria interface. Tal tensão entre a ampliação da capacidade e o enquadramento do campo de decisão torna-se particularmente visível em sistemas que diferenciam deliberadamente entre parâmetros acessíveis ao utilizador e parâmetros reservados a profissionais ou a rotinas automáticas de afinação ([Bai et al., 2024](#ref-bai-2024); [Alili et al., 2023](#ref-alili-2023)).

Uma implicação decisiva desta leitura é que a plataforma não medeia apenas “quem usa”, mas também “o que pode ser visto”. A visualização tridimensional, os indicadores de estado, os limites paramétricos e os mecanismos de feedback não são elementos neutros de apresentação; organizam a inteligibilidade do problema. Ao tornar certas relações mais visíveis e outras menos acessíveis, a interface produz uma forma específica de legibilidade do processo de personalização. O mesmo se aplica aos mecanismos de comparação e revisão: quando o sistema oferece variantes, propõe valores iniciais ou assinala incongruências, está a intervir na forma como as alternativas são construídas antes mesmo de serem escolhidas. Nesta perspetiva, a mediação digital não é mera facilitação; é também uma tecnologia de enquadramento do juízo projetual.

Esta observação conduz a uma importante reflexão crítica. Uma interface bem desenhada pode criar a sensação de evidência ou de neutralidade em decisões que continuam contingentes e projetuais. O facto de um parâmetro ser apresentado como controlo disponível, ou de uma sugestão surgir com aparência de plausibilidade técnica, não significa que a solução esteja validada ou que represente a melhor opção em todos os contextos. A mediação da interface deve, por isso, ser avaliada não apenas pela sua eficiência, mas também pela forma como torna visíveis as dependências, as incertezas e as responsabilidades envolvidas no processo. A literatura analisada reforça esta cautela: resultados positivos de usabilidade ou de rapidez de afinação não eliminam a necessidade de definir quem decide, quais parâmetros podem ser alterados, quais decisões ficam pré-estruturadas pelo sistema e sob quais condições essas alterações são consideradas seguras ou adequadas ([Peixoto et al., 2025](#ref-peixoto-2025); [Quintero et al., 2018](#ref-quintero-2018); [Bai et al., 2024](#ref-bai-2024)).

Deste ponto de vista, o sistema proposto assume uma posição produtiva: utiliza a interface para ampliar a acessibilidade, a inteligibilidade e a capacidade iterativa, sem dissolver a necessidade de julgamento humano. A mediação do processo de design não elimina a autoria projetual nem substitui a validação técnica; reorganiza-as num ambiente digital mais controlado e explícito. A plataforma redistribui a agência, mas não o faz de forma uniforme: concentra certas decisões em agentes tecnicamente qualificados, abre outras à participação informada do utilizador e deixa outras sob enquadramento assistido por lógica algorítmica. É precisamente nessa articulação entre interface, lógica paramétrica, sugestão assistida, visibilidade seletiva e responsabilidade crítica que reside o valor metodológico deste sistema enquanto contributo para o design de próteses personalizadas.

---

## Capítulo 8 — Avaliação e Discussão

### 8.1 Estratégia e critérios de avaliação

A avaliação do sistema foi organizada em torno de três níveis complementares: coerência técnica do modelo paramétrico, funcionamento da plataforma digital e plausibilidade das sugestões assistidas por IA. Esta separação é necessária porque o projeto combina componentes de natureza distinta. Um modelo OpenSCAD pode ser parametricamente consistente e, ainda assim, a interface pode não tornar essa consistência compreensível; do mesmo modo, uma sugestão de IA pode ser plausível como ponto de partida e continuar insuficiente como validação final da prótese. Assim, os critérios usados procuram avaliar o encadeamento entre dados, parâmetros, renderização e revisão humana, em vez de tratar qualquer componente como solução autónoma.

No plano antropométrico, a avaliação concentrou-se em invariantes: conformidade com o esquema de parâmetros, respeito pelos limites mínimos e máximos, proporcionalidade entre dedos, adequação etária, coerência com intervalos adultos e lateralidade correta em casos de amputação unilateral. Estes critérios foram escolhidos porque são verificáveis dentro do sistema e correspondem a riscos diretamente relacionados com a personalização inicial. Não avaliam conforto, desempenho funcional nem segurança clínica, mas permitem identificar se a cadeia descrição livre, sugestão paramétrica e modelo renderizado preserva condições mínimas de plausibilidade antes de qualquer prototipagem.

### 8.2 Avaliação técnica e experiencial do sistema

Do ponto de vista técnico, a integração entre interface, esquema paramétrico e renderização local mostrou-se funcional para o modelo Flexy Beast. A plataforma conseguiu expor os parâmetros ativos, receber sugestões em JSON, rejeitar chaves desconhecidas e aplicar os valores válidos aos controlos do modelo. A correção de uma fragilidade anterior, em que o pedido à IA permanecia alinhado com um modelo removido, foi particularmente relevante: ao usar o esquema vivo do modelo, o sistema reduziu a possibilidade de receber parâmetros sem correspondência geométrica. Esta alteração reforça a rastreabilidade, porque cada sugestão pode ser comparada com um parâmetro existente, com o seu intervalo e com a sua consequência visual.

Nos ensaios com perfis sintéticos, a IA produziu valores dentro dos intervalos definidos e manteve proporções anatómicas plausíveis em todos os casos observados. Os perfis sem medições diretas demonstraram a utilidade do sistema para utilizadores com baixa literacia antropométrica, enquanto os perfis com dados parciais mostraram que o mecanismo preserva medidas fornecidas e estima os campos em falta de forma proporcional. A experiência resultante deve ser entendida como uma redução da barreira inicial de configuração: o utilizador ou técnico deixa de começar perante um conjunto vazio de parâmetros e passa a trabalhar a partir de uma proposta editável, visualizável e criticável.

### 8.3 Discussão dos resultados face aos objetivos

Face aos objetivos da investigação, os resultados reforçam a pertinência de articular design paramétrico, dados antropométricos e IA numa plataforma única, desde que a IA permaneça enquadrada por regras explícitas e revisão humana. A contribuição não está em automatizar a conceção de uma prótese final, mas em estruturar um fluxo no qual informação incompleta pode ser convertida num ponto de partida dimensionalmente plausível. Esta capacidade responde diretamente ao problema de acessibilidade identificado no projeto: muitos utilizadores conseguem descrever idade, altura, constituição física ou lado amputado, mas não dominam a nomenclatura nem os procedimentos de medição necessários para parametrizar uma mão protésica.

A avaliação também delimita com clareza os limites do sistema. A variabilidade estocástica da IA impede tratar uma saída isolada como prescrição fixa; a ausência de uma referência clínica direta impede afirmar precisão individual; e a lateralidade, embora correta nos ensaios, requer uma regra explícita de espelhamento para deixar de depender de inferência linguística. Consequentemente, os resultados são promissores enquanto validação de coerência interna e de acessibilidade paramétrica, mas permanecem preliminares enquanto validação protésica. A continuidade do trabalho deverá incluir amostragem repetida por perfil, validação JSON estrita no servidor, conjunto permanente de regressão e comparação com medições reais ou bases antropométricas com referência individual.

---

## Capítulo 9 — Conclusões e Trabalhos Futuros

### 9.1 Síntese dos principais contributos

### 9.2 Contributos para o Design Industrial

### 9.3 Limitações e perspetivas de desenvolvimento futuro

## Bibliografia

<a id="ref-alili-2023"></a>
Alili, A., Nalam, V., Li, M., Liu, M., Feng, J., Si, J., & Huang, H. (2023). A novel framework to facilitate user preferred tuning for a robotic knee prosthesis. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31, 895-903. https://doi.org/10.1109/TNSRE.2023.3236217

<a id="ref-albin-2023"></a>
Albin, T., & Molenbroek, J. F. M. (2023). Introduction to the special issue, anthropometry in design. https://repository.tudelft.nl/file/Fileda5bfdc9-98bc-41d3-a402-553d5f0d0a63

<a id="ref-astm-international-2024"></a>
ASTM International. (2024). Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers. https://www.astm.org/f3661-24.html

<a id="ref-bai-2024"></a>
Bai, X., Yuan, J., Liu, M., Huang, H., & Feng, J. (2024). Human factors considerations of interaction between wearers and intelligent lower-limb prostheses: A prospective discussion. Journal of NeuroEngineering and Rehabilitation, 21, 187. https://doi.org/10.1186/s12984-024-01475-x

<a id="ref-bates-2020"></a>
Bates, T., Fergason, J., & Pierrie, S. N. (2020). Technological advances in prosthesis design and rehabilitation following upper extremity limb loss. https://www.semanticscholar.org/paper/905056ffa9fa963e8df8b974d90b94c05a5f7e29

<a id="ref-bradtmiller-2022"></a>
Bradtmiller, B. (2022). Design for all, design for disabled: How important is anthropometry? https://researchonline.jcu.edu.au/76898/

<a id="ref-chainando-2025"></a>
Chainando, N., Faephu, C., Suwaphong, N., Bureerat, S., Limphirat, W., Thammajaruk, P., & Syafrudin, M. (2025). Applying 3D scanning and printing techniques to produce upper limb prostheses: Bibliometric analysis and scoping review. Prosthesis, 7(2), 26. https://www.mdpi.com/2673-1592/7/2/26/pdf?version=1740996517

<a id="ref-kaygan-2025"></a>
Kaygan, H., & Kaygan, P. (2025). Clients and carers: Healthcare professionals’ roles in medical device development processes in SMEs. The Design Journal, 28(2), 213-231. https://doi.org/10.1080/14606925.2024.2420152

<a id="ref-kellam-2019"></a>
Kellam, S. M., Boleneus, G. J., Stewart, J., Richter, D. C., Michaelis, B. M., & Gerlick, R. E. (2019). An undergraduate engineering service learning project involving 3D-printed prosthetic hands for children. In American Society for Engineering Education Annual Conference & Exposition Proceedings.

<a id="ref-colombo-2015"></a>
Colombo, G., Facoetti, G., Rizzi, C., & Vitali, A. (2015). Low cost hand-tracking devices to design customized medical devices. Interacción. https://doi.org/10.1007/978-3-319-21067-436

<a id="ref-da-silveira-romero-2025"></a>
da Silveira Romero, R. C., Costa, K. A., Reis, P. H. R. G., & Vimieiro, C. B. S. (2025). Development of parametric prostheses for different levels of human hand amputations manufactured through additive manufacturing. Applied Sciences, 15, 4467. https://doi.org/10.3390/app15084467

<a id="ref-gu-2024"></a>
Gu, Y., He, L., Zeng, H., Li, J., Zhang, N., Zhang, X., & Liu, T. (2024). A data-driven design framework for structural optimization to enhance wearing adaptability of prosthetic hands. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 32. https://doi.org/10.1109/TNSRE.2024.3430070

<a id="ref-engdahl-2024"></a>
Engdahl, S., Gonzalez, M. A., Lee, C., & Gates, D. H. (2024). Perspectives on the comparative benefits of body-powered and myoelectric upper limb prostheses. https://jneuroengrehab.biomedcentral.com/counter/pdf/10.1186/s12984-024-01436-4

<a id="ref-elbreki-2022"></a>
Elbreki, A. M., Alshari, K., Ramdan, S., & Rajab, Z. (2022). Practical design of an upper prosthetic limb using three dimensional printer with an artificial intelligence based controller. In 2022 International Conference on Engineering & MIS (ICEMIS). IEEE. https://doi.org/10.1109/ICEMIS56295.2022.9914291

<a id="ref-fink-2023"></a>
Fink, C., & Diamond, Y. (2023). Prosthesis options and management in upper extremity amputation. https://www.semanticscholar.org/paper/3532a770446eb6144ef25a6b0162d1f98b61e0ff

<a id="ref-ibrahim-2024"></a>
Ibrahim, M. T., Azman, H., Adzahar, N. S. I. A., Ismail, M. A., & Shaharuddin, S. (2024). Techniques for measuring the fluctuation of residual lower limb volume in clinical practices: A systematic review of the past four decades. Applied Sciences, 14(6), 2594. https://www.mdpi.com/2076-3417/14/6/2594/pdf?version=1710932396

<a id="ref-kandikjan-2022"></a>
Kandikjan, T., Djokikj, J., Mircheski, I., & Angeleska, E. (2022). Integrating parametric design and additive manufacturing knowledge in industrial design education. https://www.semanticscholar.org/paper/7d28a8c124ef0a3599dd937791a3f3e093775ac0

<a id="ref-kannenberg-2024"></a>
Kannenberg, A., Buis, A. W. P., Sengeh, D. M., & Worsley, P. R. (2024). Insights into the spectrum of transtibial prosthetic socket design from expert clinicians and their digital records. Frontiers in Rehabilitation Sciences, 5. https://doi.org/10.3389/fresc.2024.1354069

<a id="ref-lei-2016"></a>
Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. https://dr.ntu.edu.sg/bitstream/10356/83735/1/An%20additive%20manufacturing%20process%20model%20for%20product%20family%20design.pdf

<a id="ref-lindell-2021"></a>
Lindell, E., Tingsvik, H., Guo, L., & Peterson, J. (2021). 3D body scan as anthropometric tool for individualized prosthetic socks. https://sciendo.com/pdf/10.2478/aut-2021-0007

<a id="ref-lim-d-georgiou-t-bhardwaj"></a>
Lim, D., Georgiou, T., Bhardwaj, A., O'Connell, G. D., & Agogino, A. M. (2018, August 26). Customization of a 3D printed prosthetic finger using parametric modeling. In Proceedings of the ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. https://doi.org/10.1115/DETC2018-85645

<a id="ref-ozdemir-2022"></a>
Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0F2B66A61E2CE6410F9D1F335244EB9C/S2053470122000038a.pdf/div-class-title-design-methodology-for-mass-personalisation-enabled-by-digital-manufacturing-div.pdf

<a id="ref-peixoto-2025"></a>
Peixoto, S., Martins, N., Miranda, D., Matos, D., & Carvalho, V. (2025). The design process in the development of an online platform for personalizing wearable prostheses: A preliminary approach. Designs, 9(2), 39. https://doi.org/10.3390/designs9020039

<a id="ref-parlamento-europeu-2017"></a>
Parlamento Europeu, & Conselho da União Europeia. (2017). Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical devices. https://eur-lex.europa.eu/eli/reg/2017/745/oj

<a id="ref-chapman-2025"></a>
Chapman, K., Allen, C., & Kendall, E. (2025). Methods for co-designing health communication initiatives with people with disability: A scoping review. Health Communication. https://doi.org/10.1080/10810730.2025.2462679

<a id="ref-clarkson-2010"></a>
Clarkson, J., & Coleman, R. (2010). Inclusive design. Design Studies. https://doi.org/10.1080/09544821003693689

<a id="ref-chtioui-2023"></a>
Chtioui, N., Gaha, R., & Benamara, A. (2023). Design for additive manufacturing: Review and framework proposal. https://sei.ardascience.com/index.php/journal/article/download/185/169

<a id="ref-fisher-2020"></a>
Fisher, M., & Johansen, E. (2020). Human-centered design for medical devices and diagnostics in global health. https://www.semanticscholar.org/paper/89c3c6bd56f4d0b54f5da3e3c96f18e815d9f5d4

<a id="ref-millet-2018"></a>
Millet, A., Akle, A. A., & Legardeur, J. (2018). Human centred criteria for healthcare design. https://www.semanticscholar.org/paper/267b655f123f4f167f1f9e7e6c8a1f17f73a73d0

<a id="ref-oldfrey-2024"></a>
Oldfrey, B., Ramirez, D. Z. M., Miodownik, M., et al. (2024). A scoping review of digital fabrication techniques applied to prosthetics and orthotics: Part 1 of 2—Prosthetics. Prosthetics and Orthotics International. https://doi.org/10.1097/PXR.0000000000000351

<a id="ref-quintero-2018"></a>
Quintero, D., Reznick, E., Lambert, D. J., Rezazadeh, S., Gray, L., & Gregg, R. D. (2018). Intuitive clinician control interface for a powered knee-ankle prosthesis: A case study. IEEE Journal of Translational Engineering in Health and Medicine, 6, 2600209. https://doi.org/10.1109/JTEHM.2018.2880199

<a id="ref-resnik-2010"></a>
Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. https://www.semanticscholar.org/paper/71e1fef52dde69cbcea4f62c709f7c6689f9463d

<a id="ref-romero-2025"></a>
Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475

<a id="ref-segura-2024"></a>
Segura, D., Romero, E., Abarca, V. E., & Elías, D. A. (2024). Upper limb prostheses by the level of amputation: A systematic review. Prosthesis, 6(2), 22. https://www.mdpi.com/2673-1592/6/2/22/pdf?version=1710818539

<a id="ref-smail-2020"></a>
Smail, L. C., Neal, C., Wilkins, C., & Packham, T. (2020). Comfort and function remain key factors in upper limb prosthetic abandonment: Findings of a scoping review. https://www.semanticscholar.org/paper/b5eb3fd2414ebedaa5d2283451268fafa2db0a81

<a id="ref-soyer-2016"></a>
Soyer, K., Unver, B., Tamer, S., & Ulger, O. (2016). The importance of rehabilitation concerning upper extremity amputees: A systematic review. https://pjms.com.pk/index.php/pjms/article/view/9922/4660

<a id="ref-saldarriaga-2024"></a>
Saldarriaga, A. M., Romero, E., Abarca, V. E., & Elias, D. A. (2024). A parametric design approach for affordable customized 3D socket for transradial upper limb prostheses. In 2024 10th International Conference on Control, Decision and Information Technologies (CoDIT). https://doi.org/10.1109/CoDIT62066.2024.10708382

<a id="ref-shah-2006"></a>
Shah, S., & Robinson, I. (2006). User involvement in healthcare technology development and assessment: Structured literature review. https://www.semanticscholar.org/paper/299d5b2c1d65791cc4c9f2db76edf20f479adcbc

<a id="ref-silva-2024"></a>
Silva, R., Silva, B., Fernandes, C., Morouco, P., Alves, N., & Veloso, A. (2024). A review on 3D scanners studies for producing customized orthoses. Sensors, 24(5), 1373. https://pmc.ncbi.nlm.nih.gov/articles/PMC10935386/pdf/sensors-24-01373.pdf

<a id="ref-story-2006"></a>
Story, M. (2006). Applying the principles of universal design to medical devices. https://www.semanticscholar.org/paper/d0d84425d517331607c9120290ed26d1bf2e1862

<a id="ref-stralen-2018"></a>
Stralen, M. V. (2018). Mass customization: A critical perspective on parametric design, digital fabrication and design democratization. https://www.semanticscholar.org/paper/a18f2c4d248e791d2a9b84f3cab268d5a377cc10

<a id="ref-squibb-2024"></a>
Squibb, C., Madigan, M. L., & Philen, M. K. (2024). A high precision laser scanning system for measuring shape and volume of transtibial amputee residual limbs: Design and validation. PLOS ONE, 19(5). https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0301619&type=printable

<a id="ref-sunderland-2024"></a>
Sunderland, F., Willerth, S., Silver-Thorn, B., & Dickinson, A. (2024). OpenLimbTT, a transtibial residual limb shape model for prosthetics simulation and design: Creating a statistical anatomic model using sparse data. medRxiv. https://www.medrxiv.org/content/medrxiv/early/2024/11/30/2024.11.27.24317622.full.pdf

<a id="ref-cklacandr-2022"></a>
Çıklaçandır, S., Yilmaz, M., Ozmert, O. S., Şahin, A. M., & Mihçin, S. (2022). Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design. https://www.semanticscholar.org/paper/a24aab5d4434a01eeeda73c8a62f921580ceba54

<a id="ref-white-2022"></a>
White, J., & Mosca, E. I. (2022). Developing innovative solutions for universal design in healthcare and other sectors. https://www.semanticscholar.org/paper/df2bb0d53af547bd89b2c716933c2a544bf422b1

<a id="ref-wiberg-2019"></a>
Wiberg, A., Persson, J., & Ölvander, J. (2019). Design for additive manufacturing: A review of available design methods and software. https://www.semanticscholar.org/paper/e03bf769f344512519f1005baa1d6b83fe4fc8ed

<a id="ref-wilke-2020"></a>
Wilke, H., Badke-Schaub, P., & Thoring, K. (2020). The healthcare design dilemma: Perils of a technology-driven design process for medical products. https://www.semanticscholar.org/paper/078781d9389d4618fc1b5db9347ab68ca7ef46d9

<a id="ref-walters-2025"></a>
Walters, S., Seminati, E., Metcalfe, B., Bailey, N. Y., & Pegg, E. C. (2025). Demystifying upper limb hybrid prostheses: A scoping review. https://www.semanticscholar.org/paper/d659aff9bb182a3c92377571973e6e077a3b1838

<a id="ref-yao-2016"></a>
Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive manufactured variable platforms in product families. https://www.semanticscholar.org/paper/f7bc9dc2a80714c18ac068f45b99408b0f4fe65e

<a id="ref-young-2023"></a>
Young, P. R., Hebert, J. S., Marasco, P., Carey, J., & Schofield, J. S. (2023). Advances in the measurement of prosthetic socket interface mechanics: A review of technology, techniques, and a 20-year update. https://www.tandfonline.com/doi/pdf/10.1080/17434440.2023.2244418?needAccess=true&role=button

<a id="ref-ao-2025"></a>
Ao, Y., Li, S., & Duan, H. (2025). Artificial intelligence-aided design (AIAD) for structures and engineering: A state-of-the-art review and future perspectives. Archives of Computational Methods in Engineering. https://link.springer.com/content/pdf/10.1007/s11831-025-10264-1.pdf

<a id="ref-burnap-2019"></a>
Burnap, A., Hauser, J., & Timoshenko, A. (2019). Design and evaluation of product aesthetics: A human-machine hybrid approach. https://www.semanticscholar.org/paper/7a7994f2de74a61cbdeb3c230d1ee343a0d5e783

<a id="ref-choudhury-2025"></a>
Choudhury, M. M., Eisenbart, B., & Kuys, B. (2025). Artificial intelligence (AI) in the design process: A review and analysis on generative AI perspectives. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/36E8736EEB55F0B38C2C9AB47EF381FE/S2732527X25100771a.pdf/div-class-title-artificial-intelligence-ai-in-the-design-process-a-review-and-analysis-on-generative-ai-perspectives-div.pdf

<a id="ref-figoli-2022"></a>
Figoli, F. A., Mattioli, F., & Rampino, L. (2022). AI in design idea development: A workshop on creativity and human-AI collaboration. https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=2915&context=drs-conference-papers

<a id="ref-idris-2024"></a>
Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, N. (2024). Exploring the integration of artificial intelligence in co-design framework for designer. https://ebpj.e-iph.co.uk/index.php/EBProceedings/article/download/6348/3640

<a id="ref-kadenhe-2025"></a>
Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI co-design and co-creation: A review of emerging approaches, challenges, and future directions. https://www.semanticscholar.org/paper/61c04706b7af0be5be4b0d15f595d4ab41874d12

<a id="ref-khanolkar-2023"></a>
Khanolkar, P., Vrolijk, A., & Olechowski, A. (2023). Mapping artificial intelligence-based methods to engineering design stages: A focused literature review. https://www.semanticscholar.org/paper/4d63443d45e1a7156c5972ef009ed07bb0650117

<a id="ref-krahe-2020"></a>
Krahe, C., Bräunche, A., Jacob, A., Stricker, N., & Lanza, G. (2020). Deep learning for automated product design. https://www.semanticscholar.org/paper/a5b9b4f63805f2b1773bc8214b29e38dbac27975

<a id="ref-li-2021"></a>
Li, X., Demirel, H., Goldstein, M., & Sha, Z. (2021). Exploring generative design thinking for engineering design and design education. https://peer.asee.org/38349.pdf

<a id="ref-menaka-2025"></a>
Menaka, S., Raja, W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. https://ijamjournal.org/ijam/publication/index.php/ijam/article/download/341/311

<a id="ref-panchal-2019"></a>
Panchal, J. H., Fuge, M., Liu, Y., Missoum, S., & Tucker, C. S. (2019). Special issue: Machine learning for engineering design. Journal of Mechanical Design. https://www.semanticscholar.org/paper/2c4f7ca9381db7debefe61d04da51f9e8e63d09d

<a id="ref-ramnath-2019"></a>
Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. https://www.semanticscholar.org/paper/40a0b51e5b01234cec3e807158b26a284ea77e0f

<a id="ref-rezwana-2022"></a>
Rezwana, J., & Maher, M. (2022). Understanding user perceptions, collaborative experience, and user engagement in different human-AI interaction designs for co-creative systems. https://arxiv.org/pdf/2204.13217

<a id="ref-saeidnia-2024"></a>
Saeidnia, H. R., & Ausloos, M. (2024). Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework. https://www.semanticscholar.org/paper/e2b8a10036428046443e24dc33ec5306876afdbb

<a id="ref-verganti-2020"></a>
Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). Innovation and design in the age of artificial intelligence. https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jpim.12523

<a id="ref-viros-i-martin-2021"></a>
Virós-i-Martin, A., & Selva, D. (2021). A framework to study human-AI collaborative design space exploration. https://www.semanticscholar.org/paper/716be148371af443169531b0856ae07dfe400869

<a id="ref-wang-2024"></a>
Wang, X., & Hu, B. (2024). Machine learning algorithms for improved product design user experience. https://www.semanticscholar.org/paper/717e7ad25dcafec12f01b6732773bdf9c5a49661

<a id="ref-yuksel-2023"></a>
Yüksel, N., Börklü, H. R., Sezer, H. K., & Canyurt, O. (2023). Review of artificial intelligence applications in engineering design perspective. https://www.semanticscholar.org/paper/cd38b58edf6690459767097aca745a3806824236

<a id="ref-akasaka-2022"></a>
Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs. https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488

<a id="ref-akyol-2021"></a>
Akyol, P., Barker, T., Hall, R., Morrissey, K., McCarthy, J., & Mackley, K. L. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. https://www.semanticscholar.org/paper/ea18361f7564fb19db367899adb6295a07bfa05c

<a id="ref-cole-2011"></a>
Cole, E. (2011). Patient-centered design: Interface personalization for individuals with brain injury.

<a id="ref-costabile-2007"></a>
Costabile, M. F., Fogli, D., Lanzilotti, R., Marcante, A., Mussio, P., Provenza, L. P., & Piccinno, A. (2007). Meta-design to face co-evolution and communication gaps between users and designers.

<a id="ref-dechev-2023"></a>
Dechev, N., Penner, A., Barlow, I., Vukovic, G., & Lalji, M. (2023). Accessible prosthetic arms: Victoria Hand Project and the impact of 3D printing.

<a id="ref-dexter-2013"></a>
Dexter, M., Crooks, E., Davies, P., & Simm, W. (2013). Open design and cystic fibrosis: Enabling participation in the design process.

<a id="ref-fischer-2004"></a>
Fischer, G., Giaccardi, E., Ye, Y., Sutcliffe, A. G., & Mehandjiev, N. (2004). Meta-design.

<a id="ref-fischer-2017"></a>
Fischer, G., Fogli, D., & Piccinno, A. (2017). Revisiting and broadening the meta-design framework for end-user development.

<a id="ref-frangos-2016"></a>
Frangos, P., Mierdel, S., & Koirala, S. (2016). Democratising design in scientific innovation: Application of an open value network to open source hardware design.

<a id="ref-franke-2002"></a>
Franke, N., & von Hippel, E. (2002). Satisfying heterogeneous user needs via innovation toolkits: The case of Apache security software.

<a id="ref-govender-2020"></a>
Govender, R., Abrahmsén-Alami, S., Larsson, A., Borde, A., Liljeblad, A., & Folestad, S. (2020). Independent tailoring of dose and drug release via a modularized product design concept for mass customization. Pharmaceutics.

<a id="ref-howard-2022"></a>
Howard, D., Davies, L., Dwyer, A., & Williams, J. (2022). Assessing the use of co-design to produce bespoke assistive technology solutions within a current healthcare service: A service evaluation.

<a id="ref-hippel-2002"></a>
Hippel, E. von, & Katz, R. (2002). Shifting innovation to users via toolkits. Management Science, 48(7).

<a id="ref-hussaini-2023"></a>
Hussaini, A., Kyberd, P., Mulindwa, B., Ssekitoleko, R., Keeble, W., Kenney, L., & Howard, D. (2023). 3D printing in LMICs: Functional design for upper limb prosthetics in Uganda.

<a id="ref-kerr-2024"></a>
Kerr, A., Del Din, S., Clarkson, P. J., & Rochester, L. (2024). A participatory model for cocreating accessible rehabilitation technology for stroke survivors: User-centered design approach.

<a id="ref-kuhl-2020"></a>
Kuhl, M., Lutz, J., Krause, D., & Vielhaber, M. (2020). Design of personalized devices: The tradeoff between individual value and personalization workload. Applied Sciences.

<a id="ref-mikoajewski-2023"></a>
Mikołajewski, D., Rojek, I., Kotlarz, P., Dorożyński, J., & Kopowski, J. (2023). Personalization of the 3D-printed upper limb exoskeleton design: Mechanical and IT aspects. Applied Sciences.

<a id="ref-peters-2023"></a>
Peters, C., & Richter, P. (2023). Individualizing patient pathways through modularization: Design and evaluation of healthcare-specific modularization parameters.

<a id="ref-seregni-2021"></a>
Seregni, F., Arlati, S., Colombo, V., Spoladore, D., Greci, L., Pedroli, E., Serino, S., Cipresso, P., Goulene, K., Stroulia, E., Rizzo, A., & Sacco, M. (2021). Virtual coaching for rehabilitation: The participatory design experience of the vCare Project.

<a id="ref-sims-2017"></a>
Sims, T., Cranny, A., Metcalf, C., Chappell, P., & Donovan-Hall, M. (2017). Participatory design of pediatric upper limb prostheses: Qualitative methods and prototyping.

<a id="ref-thorsen-2023"></a>
Thorsen, R., Hansen, A. H., & Nilsen, E. R. (2023). From patient to maker: A workflow including people with cerebral palsy in co-creating assistive devices using 3D printing technologies.

<a id="ref-zhu-2022"></a>
Zhu, Z., & Zhong, R. Y. (2022). A digital twin enabled wearable device for customized healthcare.

<a id="ref-alluhydan-2023"></a>
Alluhydan, A., Alsaadi, S., Almutairi, A., & Alharbi, A. (2023). Functionality and comfort design of lower-limb prosthetics: A review.

<a id="ref-anderson-2024"></a>
Anderson, C. B., Stephens, A. R., Scully, A., Pasquina, P. F., & Highsmith, M. J. (2024). A narrative review of prosthesis design decision making after lower-limb amputation for developing shared decision-making resources.

<a id="ref-andrysek-2010"></a>
Andrysek, J. (2010). Lower-limb prosthetic technologies in the developing world: A review of literature from 1994-2010.

<a id="ref-baldock-2023"></a>
Baldock, C., Greaves, M., Chockalingam, N., & Kark, L. (2023). Adjustable prosthetic sockets: A systematic review of industrial and research design characteristics and their justifications.

<a id="ref-baumann-2023"></a>
Baumann, C., & Maria, P. (2023). Improving access to prosthetic limbs in Germany: An explorative review.

<a id="ref-chadwell-2020"></a>
Chadwell, A., Kenney, L., Thies, S., Galpin, A., & Head, J. (2020). Technology for monitoring everyday prosthesis use: A systematic review.

<a id="ref-cordella-2016"></a>
Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users.

<a id="ref-dominguez-ruiz-2023"></a>
Domínguez-Ruiz, M., Ráez-Ballesteros, E., & Castillo-Castañeda, E. (2023). Low limb prostheses and complex human prosthetic interaction: A systematic literature review.

<a id="ref-ghillebert-2019"></a>
Ghillebert, J., Schoukens, J., & Vanderborght, B. (2019). Guidelines and recommendations to investigate the efficacy of a lower-limb prosthetic device: A systematic review.

<a id="ref-hafner-2016"></a>
Hafner, B. J., & Sawers, A. B. (2016). Issues affecting the level of prosthetics research evidence: Secondary analysis of a systematic review.

<a id="ref-manz-2022"></a>
Manz, S. M., Menges, M. M., Schaffernicht, E., Mattes, K., & Kannenberg, A. (2022). A review of user needs to inform the development of lower-limb prostheses.

<a id="ref-marinelli-2022"></a>
Marinelli, M., Putrino, D., Stella, F., & Guglielmelli, E. (2022). Active upper limb prostheses: A review on current state and upcoming breakthroughs.

<a id="ref-richardson-2017"></a>
Richardson, C., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review.

<a id="ref-samuelsson-2012"></a>
Samuelsson, K. A. M., Töytäri, O., Salminen, A.-L., & Brandt, Å. (2012). Effects of lower limb prosthesis on activity, participation, and quality of life: A systematic review.

<a id="ref-walker-2019"></a>
Walker, M., Paras, A., Boonstra, N., & Murrup-Stewart, C. (2019). Towards including end-users in the design of prosthetic hands: Ethical analysis of a survey of Australians with upper-limb difference.

<a id="ref-windrich-2016"></a>
Windrich, M., Grimmer, M., Christ, O., Rinderknecht, S., & Beckerle, P. (2016). Active lower limb prosthetics: A systematic review of design issues and solutions.

<a id="ref-anacleto-filho-2023"></a>
Anacleto Filho, P. C., da Silva, L., Mattos, D., Pombeiro, A., Castellucci, H. I., Colim, A., Carneiro, P., & Arezes, P. (2023). Establishing an anthropometric database: A case for the Portuguese working population. International Journal of Industrial Ergonomics, 97, 103473. https://doi.org/10.1016/j.ergon.2023.103473

<a id="ref-chatzioglou-2024"></a>
Chatzioglou, G. N., Pinar, Y., & Govsa, F. (2024). Biometric analysis hand parameters in young adults for prosthetic hand and ergonomic product applications. Anatomy & Cell Biology, 57, 172-182. https://doi.org/10.5115/acb.23.310

<a id="ref-gordon-1989"></a>
Gordon, C. C., Churchill, T., Clauser, C. E., Bradtmiller, B., McConville, J. T., Tebbetts, I., & Walker, R. A. (1989). Anthropometric survey of U.S. Army personnel: Methods and summary statistics 1988 (Technical Report NATICK/TR-89/044). U.S. Army Natick Research, Development and Engineering Center.

<a id="ref-ibiwari-2025"></a>
Ibiwari, B. W., Osemeke, B. E., Progress, V. D., Khadija, A., & Chikere, O. P. (2025). Hand anthropometric measurement and grip strength for basketball and volleyball players in higher institutions in Port Harcourt metropolis. International Journal of Science Academic Research, 6(8), 10513-10517.

<a id="ref-nag-2003"></a>
Nag, A., Nag, P. K., & Desai, H. (2003). Hand anthropometry of Indian women. Indian Journal of Medical Research, 117, 260-269.

<a id="ref-rodriguez-vega-2024"></a>
Rodríguez-Vega, G., & Rodríguez-Vega, D. A. (2024). Normative data for the anthropometric hand dimensions of the Mexican population. European Public & Social Innovation Review, 9, 1-15. https://doi.org/10.31637/epsir-2024-932

<a id="ref-gordon-2015"></a>
Gordon, C. C., Blackwell, C. L., Bradtmiller, B., Parham, J. L., Barrientos, P., Paquette, S. P., Corner, B. D., Carson, J. M., Venezia, J. C., Rockwell, B. M., Mucher, M., & Kristensen, S. (2015). 2012 anthropometric survey of U.S. Army personnel: Methods and summary statistics (Report No. NATICK/TR-15/007). U.S. Army Natick Soldier Research, Development and Engineering Center.

<a id="ref-hu-2007"></a>
Hu, H., Li, Z., Yan, J., Wang, X., Xiao, H., Duan, J., & Zheng, L. (2007). Anthropometric measurement of the Chinese elderly living in the Beijing area. International Journal of Industrial Ergonomics, 37(4), 303-311. https://doi.org/10.1016/j.ergon.2006.11.006

<a id="ref-mistarihi-2020"></a>
Mistarihi, M. Z. (2020). A data set on anthropometric measurements and degree of discomfort of physically disabled workers for ergonomic requirements in work space design. Data in Brief, 30, 105420. https://doi.org/10.1016/j.dib.2020.105420

<a id="ref-molenbroek-1998"></a>
Molenbroek, J. F. M. (1998). Geron study on Dutch elderly anthropometry. DINED database. Delft University of Technology. https://dined.io.tudelft.nl

<a id="ref-molenbroek-2003"></a>
Molenbroek, J. F. M., Kroon-Ramaekers, Y. M. T., & Snijders, C. J. (2003). Revision of the Dutch standard for furniture in schools. Ergonomics, 46(5), 491-498. https://doi.org/10.1080/0014013031000085635

<a id="ref-steenbekkers-1998"></a>
Steenbekkers, L. P. A., & van Beijsterveldt, C. E. M. (Eds.). (1998). Design-relevant characteristics of ageing users. Delft University Press.

<a id="ref-cross-1982"></a>
Cross, N. (1982). Designerly ways of knowing. Design Studies, 3(4), 221-227. https://doi.org/10.1016/0142-694X(82)90040-0

<a id="ref-design-council-2020"></a>
Design Council. (2020). Framework for innovation. https://www.designcouncil.org.uk/our-resources/framework-for-innovation/

<a id="ref-frayling-1994"></a>
Frayling, C. (1994). Research in art and design (Royal College of Art Research Papers, Vol. 1, No. 1, 1993/4). Royal College of Art.

<a id="ref-zimmerman-2007"></a>
Zimmerman, J., Forlizzi, J., & Evenson, S. (2007). Research through design as a method for interaction design research in HCI. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 493-502). ACM. https://doi.org/10.1145/1240624.1240704

<a id="ref-biddiss-2007"></a>
Biddiss, E., Beaton, D., & Chau, T. (2007). Consumer design priorities for upper limb prosthetics. Disability and Rehabilitation: Assistive Technology, 2(6), 346-357. https://doi.org/10.1080/17483100701714733

<a id="ref-brack-2021"></a>
Brack, T., & Amalu, E. H. (2021). A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. Journal of Orthopaedics, 24, 88-96. https://doi.org/10.1016/j.jor.2021.03.011

<a id="ref-guo-2025"></a>
Guo, M. (2025). Human-centered design strategies for prosthetics based on user needs. Interdisciplinary Humanities and Communication Studies, 1(1), 39-48.

<a id="ref-henao-2025"></a>
Henao, J. C., Phillips, S. T., Brooks, T. L., Pienta, K. J., Brantley, J. S., & Carey, S. L. (2025). Upper-limb prosthetic requirements from the healthcare providers, end-users and relatives' perspectives. Journal of Hand Therapy. Advance online publication. https://doi.org/10.1016/j.jht.2025.01.004

<a id="ref-herneth-2024"></a>
Herneth, T., Hiesl, A., Stief, F., & Farago, D. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1-8). IEEE. https://doi.org/10.1109/IROS58592.2024.10801868

<a id="ref-hofmann-2016"></a>
Hofmann, M. H., Griffiths, D., & Margetts, E. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858346

<a id="ref-jones-2023"></a>
Jones, M. L. H., Vrieling, A. H., Steadman, J., & Kyberd, P. J. (2023). Evidencing the effectiveness of upper limb prostheses: A multi-stakeholder perspective on study requirements. Frontiers in Health Services, 3, 1123682. https://doi.org/10.3389/frhs.2023.1123682

<a id="ref-peerdeman-2011"></a>
Peerdeman, B., Boere, D., Witteveen, H., Huis in 't Veld, R., Hermens, H., Stramigioli, S., Rietman, H., Veltink, P., & Misra, S. (2011). Myoelectric forearm prostheses: State of the art from a user-centered perspective. Journal of Rehabilitation Research and Development, 48(6), 719-738. https://doi.org/10.1682/JRRD.2010.08.0161

<a id="ref-baron-2020"></a>
Baron, A., Gatzweiler, C., Geislinger, A., Huber, C., & Aszmann, O. C. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 274-287. https://doi.org/10.3390/prosthesis2040021

<a id="ref-cabibihan-2018"></a>
Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2831907

<a id="ref-herbst-2021"></a>
Herbst, Y., Georgopoulou, A., Dettwyler, M., Fernandez, A., Bacher, M., & Paik, J. (2021). Scan-driven fully-automated pipeline for a personalized, 3D printed low-cost prosthetic hand. In 2021 IEEE 17th International Conference on Automation Science and Engineering (CASE) (pp. 1188-1194). IEEE. https://doi.org/10.1109/CASE49439.2021.9551649

<a id="ref-lim-2018"></a>
Lim, S. H., Bae, M., & Kim, S. H. (2018). Customization of a 3D printed prosthetic finger using parametric modeling. In ASME 2018 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference. ASME. https://doi.org/10.1115/DETC2018-86211

<a id="ref-moreo-2016"></a>
Moreo, A. M. (2016). Parametric design of a 3D printable hand prosthesis for children in developing countries [Master's thesis, Delft University of Technology].

<a id="ref-romero-2025"></a>
Romero, M., Sánchez, J., & Álvarez, H. (2025). Development of parametric prostheses for different levels of human hand amputations manufactured through additive manufacturing. Applied Sciences, 15(3), 1124. https://doi.org/10.3390/app15031124

<a id="ref-machado-2019"></a>
Machado, F., Malpica, N., & Borromeo, S. (2019). Parametric CAD modeling for open source scientific hardware: Comparing OpenSCAD and FreeCAD Python scripts. PLOS ONE, 14(12), e0225795. https://doi.org/10.1371/journal.pone.0225795

<a id="ref-manero-2019"></a>
Manero, A., Smith, P., Sparkman, J., Dombrowski, M., Courbin, D., Kester, A., Womack, I., & Chi, A. (2019). Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. International Journal of Environmental Research and Public Health, 16, 1641. https://doi.org/10.3390/ijerph16091641

<a id="ref-menaka-2025"></a>
Menaka, S., Raja A, W., Ramakrishnan, S., Karthikeswaran, D., Sridar, K., & Sivaranjani, T. (2025). AI-driven computer-aided design (CAD) systems: Leveraging neural networks for optimized engineering product development. International Journal of Applied Mathematics, 38(5s).

<a id="ref-nilsiam-2017"></a>
Nilsiam, Y., & Pearce, J. M. (2017). Free and open source 3-D model customizer for websites to democratize design with OpenSCAD. Designs, 1(1), 5. https://doi.org/10.3390/designs1010005

<a id="ref-nini-2024"></a>
Nini, L., Ceccarelli, A., Tagliamonte, N., Zollo, L., & Taffoni, F. (2024). Parametric 3D modeling of a customized prosthetic hand finger for additive manufacturing. In 2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob). IEEE. https://doi.org/10.1109/BioRob60516.2024.10719909

<a id="ref-ten-kate-2017"></a>
ten Kate, J., Smit, G., & Breedveld, P. (2017). 3D-printed upper limb prostheses: A review. Disability and Rehabilitation: Assistive Technology, 12(3), 300-314. https://doi.org/10.1080/17483107.2016.1253117

<a id="ref-yu-2013"></a>
Yu, A., Yick, K. L., Ng, S. P., & Yip, J. (2013). 2D and 3D anatomical analyses of hand dimensions for custom-made gloves. Applied Ergonomics, 44, 381-392.

<a id="ref-base-local-antropometrica-2026"></a>
Base local consolidada de dados antropométricos da mão e do membro superior distal. (2026). [Conjunto de dados]. Material de apoio da investigação, `material/antropometria/dados antropométricos/multi_population_hand.csv`.

<a id="ref-1-definir-o-que-e-propriocep"></a>
[^1]: definir o que é proprioceptivo

<a id="ref-2-meter-este-link-na-bibliog"></a>
[^2]: Meter este link na bibliografia

<a id="ref-3-nao-e-bem-marcacao-ne-te"></a>
[^3]: não é bem marcação, né. Tem que ser outra palavra

<a id="ref-4-cool-mas-se-calhar-so-se"></a>
[^4]: Cool, mas se calhar, só se calhar, linkar isto tb né?

<a id="ref-5-vamos-adicionar-a-citacao"></a>
[^5]: vamos adicionar a citação e bibliografia. faz sentido uma tabela?

<a id="ref-6-explicar-oque-sao-todos-es"></a>
[^6]: explicar oque são todos estes modelos.

<a id="ref-7-definir-seed-design"></a>
[^7]: definir seed design

<a id="ref-8-escalonados-amplicados-e"></a>
[^8]: escalonados? amplicados e reduzidos? Que palavra utilizar?

<a id="ref-9-toda-esta-frase-podia-ser"></a>
[^9]: toda esta frase podia ser melhorada

<a id="ref-10-posso-igualmente-aumentar"></a>
[^10]: Posso igualmente aumentar este secção um pouco. Está tudo super comprimido

<a id="ref-11-nao-me-soa-super-bem"></a>
[^11]: não me soa super bem.

<a id="ref-12-estou-a-bater-mal-ou-ja-e"></a>
[^12]: Estou a bater mal ou já escrevi isto?

<a id="ref-13-penalizacoes-e-um-pouco-f"></a>
[^13]: penalizações é um pouco forte
