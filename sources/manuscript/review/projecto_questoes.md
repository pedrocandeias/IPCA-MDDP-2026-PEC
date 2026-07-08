# Questões e respostas a partir do texto actual do projecto

Fonte analisada: `projecto-completo.md`, versão 0.4.1.

Data da leitura: 2026-06-13.

Nota: o pedido refere `projecto_completo`; no repositório, o manuscrito activo encontra-se como `projecto-completo.md`.

## Síntese geral

O texto actual responde às seis questões, mas com graus diferentes de maturidade. As questões 1 a 5 estão respondidas de forma clara no enquadramento, na metodologia e nos capítulos técnicos. A questão 6 está respondida de modo mais parcial: há avaliação técnica, análise crítica e validação preliminar da cadeia paramétrica/plataforma/IA, mas a prototipagem física e a validação em uso real ainda não aparecem documentadas com o mesmo nível de evidência.

| Questão | Grau de resposta no manuscrito | Secções mais relevantes |
| --- | --- | --- |
| 1. Papel do Design Industrial | Forte | 1.1, 1.3.2, 2.2, 2.7, 3.1, 3.2, 7.3 |
| 2. Requisitos protésicos personalizados | Forte | 2.1, 2.3, 2.4, 4.1, 4.2 |
| 3. Modelo paramétrico antropométrico | Forte, com limites assumidos | 2.3, 2.4, 4.2, 4.3, 4.4 |
| 4. Plataforma digital por perfis | Forte | 5.1-5.5, 7.1-7.3 |
| 5. IA assistiva, supervisão e rastreabilidade | Forte, preliminar na validação | 2.5, 5.4, 6.1-6.4, 8.1-8.3 |
| 6. Avaliação por prototipagem e reflexão crítica | Parcial | 3.5, 4.4, 8.1-8.3 |

## 1. Analisar criticamente o papel do Design Industrial na mediação entre tecnologia, corpo e experiência de uso em próteses de membro superior.

**Resposta:** Sim. O manuscrito responde de forma forte a esta questão.

O texto posiciona o Design Industrial como mediador entre tecnologia e experiência humana logo na introdução, ao associar a perda de membro superior a impactos funcionais, sociais e simbólicos e ao afirmar que as soluções protésicas devem articular desempenho mecânico, conforto ergonómico, aceitação estética e viabilidade económica. Esta ideia é retomada no objectivo geral e nos objectivos específicos, onde o Design Industrial surge como prática capaz de articular Design Inclusivo, fabricação aditiva, parametrização e IA.

No Capítulo 2, a resposta torna-se mais crítica. A secção 2.2 não trata o design como mera configuração formal ou estética; apresenta-o como disciplina que traduz necessidades clínicas em soluções tangíveis, articula requisitos regulatórios e experiência de uso, e intervém em equipas multidisciplinares. O texto também reconhece limitações do campo, nomeadamente a predominância de abordagens de engenharia em dispositivos médicos e a participação ainda limitada de profissionais de design centrado no uso.

No Capítulo 3, o Design Industrial é enquadrado como prática investigativa através de Research Through Design. O manuscrito defende que o artefacto, o modelo paramétrico e a plataforma não são apenas resultados técnicos, mas instrumentos para revelar decisões, compromissos e relações entre corpo, tecnologia e uso. No Capítulo 7, esta mediação é aprofundada através da interface: a plataforma é descrita como uma camada que distribui agência, torna o processo mais inteligível e mantém a necessidade de julgamento humano.

**Como responde:** responde articulando três planos: o plano corporal, pela atenção à antropometria, conforto, interface corpo-dispositivo e incorporação; o plano tecnológico, pela parametrização, impressão 3D, OpenSCAD, WebAssembly e IA; e o plano experiencial, pela discussão de aceitação, participação, inteligibilidade, confiança, estética e responsabilidade decisional.

**Limite actual:** a análise crítica é forte no corpo do texto, mas as conclusões do Capítulo 9 ainda estão apenas estruturadas por títulos. A resposta ficaria mais fechada se o capítulo final sintetizasse explicitamente o contributo do Design Industrial como mediação entre sistema técnico, corpo vivido e plataforma digital.

## 2. Identificar requisitos anatómicos, funcionais, ergonómicos, estéticos e produtivos relevantes para sistemas protésicos personalizados.

**Resposta:** Sim. O manuscrito responde de forma forte e bastante explícita.

O Capítulo 4, especialmente a secção 4.1, identifica directamente as principais categorias de requisitos. O texto descreve o problema de design como multiobjectivo e enumera requisitos funcionais, ergonómicos, técnicos, produtivos, estéticos e psicossociais. Entre os requisitos funcionais surgem padrões de preensão, graus de liberdade, amplitude de movimento, força, velocidade e capacidade de realizar actividades da vida diária. Nos requisitos ergonómicos aparecem conforto, baixo peso, usabilidade, facilidade de colocação e remoção e adequação ao uso prolongado. Nos requisitos produtivos aparecem modularidade, reparabilidade, custo controlado, compatibilidade com fabrico digital/aditivo, tolerâncias, orientação de impressão e limites materiais.

O requisito anatómico é desenvolvido sobretudo na secção 2.4 e depois operacionalizado na secção 4.2. O texto explica que a adequação geométrica ao corpo condiciona conforto, segurança, desempenho e aceitação, distinguindo medições lineares, captura de forma, digitalização 3D, fotogrametria, imagiologia médica e métricas complementares de interface. A tabela de parâmetros antropométricos da mão e do membro superior traduz essa discussão em medidas relevantes: comprimento e largura da mão, comprimento da palma, comprimentos digitais, proporções falângicas, dimensões do polegar, punho, antebraço e membro residual.

Os requisitos estéticos e psicossociais também estão presentes. O texto associa aparência, identidade, aceitação social, incorporação corporal e dignidade à adopção da prótese. Esta resposta é importante porque evita reduzir a prótese a uma peça funcional: o manuscrito reconhece que aceitação e abandono dependem também da relação simbólica e social com o dispositivo.

**Como responde:** responde primeiro por revisão crítica da literatura, depois por categorização dos requisitos e finalmente por tradução parcial desses requisitos em parâmetros de projecto.

**Limite actual:** muitos requisitos ainda aparecem como categorias ou critérios, não como especificações quantitativas fechadas. O texto identifica que conforto, torque, pressão, peso, tolerâncias e resistência devem ser traduzidos em métricas, mas nem sempre fixa valores-alvo mensuráveis para cada um desses requisitos no sistema desenvolvido.

## 3. Estruturar um modelo paramétrico capaz de traduzir dados antropométricos em geometrias configuráveis e fabricáveis por impressão 3D.

**Resposta:** Sim. O manuscrito responde de forma forte, embora assuma que a validação final do ajuste físico permanece por realizar.

O Capítulo 4 é a resposta principal a esta questão. A secção 4.2 estabelece a passagem dos dados antropométricos para a estrutura do modelo. O texto rejeita o escalonamento uniforme como solução suficiente e defende parâmetros independentes para comprimentos, larguras, proporções falângicas, palma, punho e membro residual. Também apresenta conjuntos mínimos de parâmetros por nível de amputação, distinguindo amputação transradial, desarticulação do punho, amputação parcial da mão, amputação de dedos e mão completa.

O manuscrito descreve uma base local consolidada de dados antropométricos com 1.790 registos, cobrindo nove países e várias fontes populacionais. Esta base serve para definir intervalos plausíveis, identificar entradas mínimas recorrentes e testar coerência geométrica entre perfis. O texto é claro ao afirmar que esta base não substitui a medição individual, mas funciona como infraestrutura intermédia e auditável para parametrização.

Na secção 4.3, a estrutura conceptual passa para OpenSCAD. O modelo é descrito em camadas: entrada antropométrica, derivação geométrica, comportamento funcional e restrições produtivas. A escolha do OpenSCAD é justificada pela transparência, reprodutibilidade, modularidade e capacidade de expor parâmetros numa plataforma web. A secção 4.4 reforça que o desenvolvimento ocorreu por iterações, com correcção de intersecções, espessuras insuficientes, folgas, desalinhamentos e combinações paramétricas instáveis.

**Como responde:** responde ao estruturar uma cadeia de tradução: dados antropométricos -> parâmetros de entrada -> parâmetros derivados -> módulos geométricos -> restrições de fabricabilidade -> geração em OpenSCAD -> exportação/preparação para impressão 3D.

**Limite actual:** a resposta é sólida enquanto estrutura paramétrica e metodológica. Ainda assim, o próprio texto reconhece que a robustez não se esgota na geração da geometria: requer verificação em slicer, controlo dimensional, eventual simulação estrutural, prototipagem física e observação do comportamento da peça. A adequação de sockets ou superfícies anatómicas complexas também é limitada pela natureza do OpenSCAD e pela ausência de digitalização individual.

## 4. Desenvolver uma plataforma digital que torne o modelo paramétrico operável por perfis de utilizador diferenciados.

**Resposta:** Sim. O manuscrito responde de forma forte.

O Capítulo 5 descreve directamente a plataforma web e a sua integração digital. A plataforma é apresentada como camada de mediação entre modelo paramétrico, dados do utilizador e configuração da prótese, evitando que o utilizador tenha de manipular directamente o código OpenSCAD ou dominar software CAD avançado.

A secção 5.1 define três perfis principais: administrador, técnico e utilizador. O administrador gere contas, permissões e supervisão geral. O técnico, que pode corresponder a protésico, clínico, designer ou operador especializado, cria, edita e acompanha configurações. O utilizador final consulta as suas configurações, acompanha o processo e participa dentro de limites definidos. Esta segmentação responde directamente à questão dos perfis diferenciados.

As secções 5.2 a 5.5 explicam a arquitectura: cliente web, servidor Node.js/Express, base de dados SQLite, autenticação com JWT, tokens em cookies HttpOnly, configurações guardadas em JSON, renderização local em OpenSCAD via WebAssembly e Web Worker, gestão de modelos e parâmetros, exportação STL, persistência de configurações e escalabilidade por ficheiros de configuração. O Capítulo 7 complementa esta descrição ao discutir a experiência de designer/técnico/clínico e utilizador final, defendendo uma colaboração assimétrica: certos parâmetros críticos permanecem sob supervisão técnica, enquanto outras dimensões podem ser tornadas mais visíveis e participativas.

**Como responde:** responde através de uma arquitectura multiutilizador, permissões diferenciadas, interface paramétrica, pré-visualização 3D, armazenamento de configurações e exposição controlada de parâmetros.

**Limite actual:** a plataforma está bem descrita como protótipo funcional e sistema metodológico. Falta ainda evidência empírica de usabilidade com os perfis reais a que se destina. O próprio texto reconhece que SQLite e WASM são adequados ao protótipo, mas podem exigir revisão em cenários de maior escala, auditoria ou concorrência.

## 5. Explorar a inteligência artificial como camada assistiva para sugestão, validação preliminar e interpretação de parâmetros, mantendo supervisão humana e rastreabilidade.

**Resposta:** Sim. O manuscrito responde de forma forte e explícita.

O Capítulo 2 enquadra a IA como instrumento assistivo e não como substituto do designer. O texto distingue IA, aprendizagem automática, aprendizagem profunda e IA generativa, e sublinha riscos de enviesamento, opacidade, erro, dependência excessiva e falsa autoridade técnica. A supervisão humana é apresentada como condição necessária em domínios sensíveis.

No Capítulo 5, a IA é integrada funcionalmente na plataforma. A partir de uma descrição livre ou de medidas parciais, a interface constrói um pedido com o esquema vivo do modelo seleccionado, incluindo nomes dos parâmetros, legendas, tipos, limites mínimos e máximos e valores correntes. A resposta esperada é JSON simples com pares parâmetro-valor. A aplicação aceita apenas chaves existentes, descarta parâmetros desconhecidos e aplica valores aos controlos antes de renderizar novamente o modelo.

O Capítulo 6 aprofunda a lógica de uso. A IA não gera autonomamente a prótese; sugere pontos de partida, interpreta informação incompleta, organiza alternativas e apoia a decisão dentro de uma estrutura paramétrica explícita. A validação antropométrica assistida por IA é definida como validação interna de plausibilidade, não como validação clínica. Os critérios incluem conformidade com o esquema, respeito por limites, proporcionalidade dos dedos, plausibilidade adulta, adequação etária e lateralidade.

O Capítulo 8 confirma resultados preliminares: nos ensaios com perfis sintéticos, a IA produziu valores dentro dos intervalos definidos, manteve proporções anatómicas plausíveis, preservou medições fornecidas e estimou campos em falta. A rastreabilidade é reforçada porque cada sugestão pode ser comparada com um parâmetro existente, o seu intervalo e a consequência visual no modelo.

**Como responde:** responde tratando a IA como camada human-in-the-loop: entrada semântica -> sugestão paramétrica JSON -> filtragem por esquema -> aplicação aos controlos -> visualização -> revisão humana.

**Limite actual:** a validação ainda é preliminar. O texto reconhece variabilidade estocástica, ausência de referência clínica directa, necessidade de regra explícita para espelhamento/lateralidade, validação JSON estrita no servidor, regressão permanente e comparação com medições reais. A IA é útil para reduzir a barreira inicial de parametrização, mas não valida conforto, segurança, função nem prescrição clínica.

## 6. Avaliar a abordagem através de prototipagem, análise técnica e reflexão crítica sobre o processo de design.

**Resposta:** Parcialmente. O manuscrito responde bem à análise técnica e à reflexão crítica, mas ainda responde de forma limitada à prototipagem física.

A metodologia, no Capítulo 3, declara que a fase empírica inclui modelos paramétricos testados com perfis antropométricos e protótipos físicos produzidos por impressão 3D. A secção 3.5 define critérios de avaliação: personalização paramétrica, consistência dimensional, viabilidade de fabrico, robustez estrutural, clareza de configuração, acessibilidade e replicabilidade. Também explicita limitações: ausência de testes com utilizadores reais, uso de dados antropométricos secundários e impossibilidade de validação clínica.

O Capítulo 4 oferece uma reflexão crítica forte sobre o processo de modelação. A secção 4.4 descreve iterações, refinamento, modularização, redução de parâmetros excessivos, correcção de intersecções, espessuras insuficientes, folgas inadequadas, desalinhamentos e conflitos entre personalização e fabricabilidade. Esta parte responde bem à dimensão de Research Through Design, porque mostra como o processo de fazer revelou limites e reconfigurou decisões.

O Capítulo 8 avalia a abordagem em três níveis: coerência técnica do modelo paramétrico, funcionamento da plataforma digital e plausibilidade das sugestões assistidas por IA. A avaliação mostra que a plataforma expõe parâmetros activos, recebe sugestões JSON, rejeita chaves desconhecidas, aplica valores válidos e reduz a barreira inicial para utilizadores com baixa literacia antropométrica.

**Como responde:** responde por avaliação interna do sistema, análise técnica da cadeia modelo-plataforma-IA e reflexão crítica sobre o processo iterativo de design.

**Limite actual:** a componente de prototipagem física ainda não está suficientemente demonstrada no texto actual. Faltam evidências como descrição de protótipos impressos, parâmetros de impressão, fotografias, resultados de montagem, verificação dimensional, ensaios mecânicos simples, testes de encaixe não clínicos ou comparação entre variantes fabricadas. O próprio Capítulo 8 afirma que os critérios usados não avaliam conforto, desempenho funcional nem segurança clínica. Assim, a questão 6 está respondida como avaliação preliminar e metodológica, mas não ainda como validação prototípica completa.

## Conclusão de leitura

O manuscrito actual já cobre o núcleo conceptual e técnico das seis questões. A sua resposta é particularmente forte quando discute mediação pelo Design Industrial, requisitos, estrutura paramétrica, plataforma e IA assistiva. O ponto que mais precisa de consolidação é a avaliação material: para a questão 6 ficar tão robusta como as restantes, o texto deveria documentar de forma mais directa a prototipagem física, os ensaios técnicos realizados e a leitura crítica desses resultados face aos objectivos iniciais.
