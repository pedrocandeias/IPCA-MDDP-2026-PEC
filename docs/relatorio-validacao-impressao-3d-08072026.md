# Relatório de alterações — validação por impressão 3D

Data: 2026-07-08

Última actualização do relatório: 2026-07-08, alinhada com a versão `0.4.17` do manuscrito.

## Objetivo

Actualizar o manuscrito para declarar explicitamente que a validação geométrica/produtiva incluiu impressões 3D, realizadas com base nos resultados dos testes de perfil. A alteração distingue esta validação física preliminar de uma validação clínica, biomecânica ou de uso prolongado.

O texto final mantém a informação sobre os materiais usados, PLA e PETG, concentra a justificação da sua escolha na metodologia, identifica o PrusaSlicer 2.9.6 e o Bambu Studio como ferramentas de preparação para impressão e indica que a produção foi realizada numa Bambu Lab A1 com AMS.

## Ficheiros alterados

- `projecto-completo.md`
- `projecto-completo.docx`
- `docs/relatorio-validacao-impressao-3d-08072026.md`
- `CHANGELOG.md`

## Cópias e backups relacionados

- `docs/projecto-completo-1554-08072026-validacao-impressao-3d.docx`
- `docs/projecto-completo-1637-08072026-reduz-repeticao-pla-petg.docx`
- `docs/projecto-completo-1642-08072026-justificacao-pla-petg-metodologia.docx`
- `docs/projecto-completo-1658-08072026-tabela-resultados-impressao-3d.docx`
- `versions/projecto-completo-2026-07-08_15-54-48-before-physical-print-validation.md`
- `versions/projecto-completo-docx-2026-07-08_15-54-48-before-physical-print-validation.docx`
- `versions/projecto-completo-2026-07-08_16-34-20-before-reduce-pla-petg-repetition.md`
- `versions/projecto-completo-docx-2026-07-08_16-34-20-before-reduce-pla-petg-repetition.docx`
- `versions/projecto-completo-2026-07-08_16-40-13-before-material-rationale-relocation.md`
- `versions/projecto-completo-docx-2026-07-08_16-40-13-before-material-rationale-relocation.docx`
- `versions/projecto-completo-2026-07-08_16-48-07-before-print-results-table-and-slicing-term.md`
- `versions/projecto-completo-docx-2026-07-08_16-48-07-before-print-results-table-and-slicing-term.docx`

## Evolução da alteração

### Versão 0.4.13

Foi introduzida a validação por impressão 3D no manuscrito, indicando que as impressões físicas foram feitas a partir dos resultados dos testes de perfil.

### Versão 0.4.15

Foram reduzidas repetições da expressão `PLA e PETG` ao longo do texto. As referências posteriores passaram a usar expressões mais sintéticas, como `prototipagem física`, `impressão 3D` ou `validação física`.

### Versão 0.4.16

A justificação da escolha dos dois materiais foi deslocada para a metodologia, no Capítulo 3. O Capítulo 8 passou a remeter para os materiais definidos na metodologia, evitando repetir a explicação.

### Versão 0.4.17

Foi acrescentada a Tabela 8.1 com a síntese dos resultados das impressões, as tabelas seguintes do Capítulo 8 foram renumeradas, a terminologia anteriormente usada para o slicing foi substituída por expressões mais adequadas ao português europeu, e a preparação para impressão passou a indicar explicitamente o PrusaSlicer 2.9.6, o Bambu Studio e a Bambu Lab A1 com AMS. A versão 2.9.6 do PrusaSlicer foi confirmada em 2026-07-08 através da página oficial de releases do projecto no GitHub.

## Alterações detalhadas no manuscrito

### Versão do documento

Local: `projecto-completo.md:3`

Tipo de alteração: actualização da versão do manuscrito.

Texto final:

> Versão do documento:0.4.17

### Capítulo 1 — Introdução

#### 1.3.2 Objetivos específicos

Local: `projecto-completo.md:214`

Tipo de alteração: reformulação do parágrafo dos objectivos específicos para deixar claro que a validação não é apenas digital.

Texto alterado/introduzido no parágrafo:

> A validação da abordagem combina testes de perfil, exportação de geometrias, análise de malhas e prototipagem por impressão 3D, avaliando a coerência dimensional, a montagem preliminar, a viabilidade de fabrico e os limites materiais, sem reivindicar validação clínica do dispositivo.

#### 1.4 Abordagem metodológica geral

Local: `projecto-completo.md:222`

Tipo de alteração: reformulação da descrição da fase empírica para incluir a produção física dos protótipos.

Texto alterado/introduzido no parágrafo:

> A fase empírica operacionaliza a modelação paramétrica, a produção de protótipos por impressão 3D e a avaliação técnica e funcional preliminar, sem utilizar dados pessoais de utilizadores.

### Capítulo 3 — Metodologia de Investigação

#### 3.3 Estrutura metodológica do projeto

Local: `projecto-completo.md:754`

Tipo de alteração: reformulação da fase empírica para indicar que as configurações resultantes dos testes de perfil foram exportadas e impressas.

Texto alterado/introduzido no parágrafo:

> Os modelos paramétricos são testados com diferentes perfis antropométricos provenientes de bases de dados públicas, e as configurações resultantes dos testes de perfil são exportadas para fabrico e produzidas por impressão 3D. Esta fase permite avaliar a passagem do perfil simulado para a geometria exportada e desta para o protótipo físico, observando a exequibilidade de impressão, a integridade estrutural preliminar, a montagem, a ajustabilidade e a coerência formal perante variações dimensionais.

#### 3.4 Métodos de recolha e análise de dados

Local: `projecto-completo.md:767`

Tipo de alteração: reformulação dos métodos de análise na fase de prototipagem, com explicitação da preparação para impressão, materialização por impressão 3D em PLA/PETG, ferramentas usadas e razão da escolha dos dois materiais.

Texto alterado/introduzido no parágrafo:

> Os modelos exportados a partir dos testes de perfil foram preparados para impressão no PrusaSlicer 2.9.6 e no Bambu Studio, e materializados por impressão 3D em PLA e PETG numa Bambu Lab A1 com AMS. A opção por estes dois materiais permite comparar uma solução rígida, estável e económica, adequada à verificação rápida da geometria, com uma alternativa mais resistente e menos frágil, útil para observar o comportamento dos componentes em manipulação, encaixe e montagem preliminar.

Função desta alteração:

> Esta comparação permite verificar se a geometria gerada pelo sistema se mantém imprimível, manipulável e coerente depois da transição do ambiente digital para o objeto físico.

### Capítulo 8 — Avaliação e Discussão

#### 8.1 Estratégia e critérios de avaliação

Local: `projecto-completo.md:1400`

Tipo de alteração: correcção de enquadramento. O texto deixou de sugerir que a validação antecede qualquer prototipagem; passa a indicar que a avaliação antecede a preparação para fabrico e que a validação clínica permanece fora do âmbito.

Texto alterado/introduzido no parágrafo:

> Estas validações incidem sobre a coerência preliminar do processo, permitindo verificar se a cadeia entre descrição livre, sugestão paramétrica e modelo renderizado preserva condições mínimas de plausibilidade antes da preparação para fabrico. A avaliação de conforto, desempenho funcional em uso e segurança clínica permanece dependente de testes posteriores com utilizadores e validação especializada.

Local: `projecto-completo.md:1409`

Tipo de alteração: inserção de parágrafo sobre a validação física por impressão 3D, revisto para não repetir a justificação dos materiais e para indicar as ferramentas e equipamento utilizados.

Texto final:

> A validação foi depois prolongada para prototipagem física. Com base nos resultados dos testes de perfil, foram selecionadas configurações representativas dos cenários avaliados, incluindo perfis de mão pequena, perfil adulto feminino e perfil adulto masculino. Estas geometrias foram exportadas em STL/3MF, preparadas no PrusaSlicer 2.9.6 e no Bambu Studio, e impressas nos materiais definidos na metodologia numa Bambu Lab A1 com AMS, para verificar a passagem do modelo exportado ao protótipo físico.

Local: `projecto-completo.md:1411`

Tipo de alteração: inserção de parágrafo com o procedimento de validação física.

Texto adicionado:

> A validação física seguiu cinco verificações principais: compatibilidade do ficheiro exportado com o software de preparação para impressão, ausência de falhas críticas de malha ou escala, conclusão da impressão sem defeitos impeditivos, inspeção visual e dimensional das zonas críticas e, quando aplicável, teste de encaixe ou montagem entre componentes.

Delimitação metodológica acrescentada no mesmo parágrafo:

> Esta etapa não teve como objetivo demonstrar eficácia clínica, conforto de uso ou durabilidade prolongada; o seu objetivo foi confirmar que os resultados dos perfis testados podiam atravessar a cadeia completa perfil -> parâmetros -> OpenSCAD/WebAssembly -> STL/3MF -> impressão 3D, mantendo coerência geométrica e viabilidade produtiva.

Local: `projecto-completo.md:1413`

Tipo de alteração: introdução de texto de enquadramento para a nova tabela de resultados das impressões.

Texto adicionado:

> A Tabela 8.1 sintetiza os resultados observados nas impressões realizadas. A leitura deve ser entendida como registo técnico preliminar de produção e verificação material, e não como ensaio mecânico normalizado ou validação clínica.

Local: `projecto-completo.md:1415`

Tipo de alteração: introdução da nova tabela de resultados e renumeração das restantes tabelas do Capítulo 8.

Tabela introduzida:

| Configuração testada | Material | Verificações realizadas | Resultado observado |
| --- | --- | --- | --- |
| Perfil de mão pequena | PLA | Geração do ficheiro de impressão, escala e zonas finas | Impressão concluída sem defeitos impeditivos; geometria imprimível, mantendo necessidade de atenção às espessuras nas zonas reduzidas. |
| Perfil de mão pequena | PETG | Geração do ficheiro de impressão, manipulação e encaixe preliminar | Impressão concluída; comportamento material menos frágil na manipulação e no encaixe preliminar. |
| Perfil adulto feminino | PLA | Geração do ficheiro de impressão, escala e integridade formal | Impressão concluída; proporções e escala mantiveram coerência com o modelo exportado. |
| Perfil adulto feminino | PETG | Geração do ficheiro de impressão, zonas críticas e montagem preliminar | Impressão concluída; zonas críticas e encaixes verificáveis no protótipo físico. |
| Perfil adulto masculino | PLA | Geração do ficheiro de impressão e escala aumentada | Impressão concluída; a escala maior não impediu a produção do protótipo. |
| Perfil adulto masculino | PETG | Geração do ficheiro de impressão, manipulação e montagem preliminar | Impressão concluída; manipulação preliminar sem falhas impeditivas observadas. |

#### 8.3 Validação geométrica entre modelos

Local: `projecto-completo.md:1534`

Tipo de alteração: reformulação da discussão da validação geométrica para incluir a materialização física como fonte de verificação adicional.

Texto alterado/introduzido no parágrafo:

> Esta etapa confirmou que a validação das sugestões de IA deve prolongar-se para além da resposta em JSON, pois a geometria exportada e a sua materialização por impressão 3D podem revelar dependências internas, limites de escala, problemas de espessura, folgas insuficientes e heranças de código invisíveis na análise numérica.

#### 8.4 Discussão dos resultados face aos objetivos

Local: `projecto-completo.md:1542`

Tipo de alteração: reformulação da discussão dos limites da validação, distinguindo prototipagem física de validação clínica.

Texto alterado/introduzido no parágrafo:

> A prototipagem física confirmou a viabilidade das configurações selecionadas, mas também reforçou que a passagem para o objeto físico deve ser tratada como etapa de verificação material e não como prova clínica.

Local: `projecto-completo.md:1544`

Tipo de alteração: reformulação da conclusão metodológica para incluir a cadeia completa até à impressão.

Texto alterado/introduzido no parágrafo:

> O esquema de parâmetros do modelo, os limites declarados, a filtragem dos campos devolvidos, a ancoragem em dados populacionais, a renderização por OpenSCAD/WebAssembly, a exportação em STL/3MF, a preparação para impressão e a impressão 3D formam uma cadeia de verificações sucessivas.

### Capítulo 9 — Conclusões e Trabalhos Futuros

#### 9.1 Síntese dos principais contributos

Local: `projecto-completo.md:1562`

Tipo de alteração: inserção de um novo resultado principal na síntese dos contributos.

Texto adicionado:

> Quarto, a prototipagem física confirmou que as configurações selecionadas a partir dos testes de perfil podiam ser preparadas para impressão e impressas, permitindo verificar escala, integridade formal, zonas críticas e montagem preliminar. Esta etapa validou a viabilidade produtiva do fluxo, mas não constitui validação clínica ou biomecânica completa.

Local: `projecto-completo.md:1564`

Tipo de alteração: renumeração do resultado seguinte.

Texto alterado:

> Quinto, a avaliação centrada no utilizador revelou que a acessibilidade paramétrica depende tanto da qualidade da inferência - entendida como o processo através do qual a IA transforma informação incompleta, indireta ou descritiva em sugestões paramétricas plausíveis - como das salvaguardas incorporadas na interface [...]

#### 9.3 Limitações e perspetivas de desenvolvimento futuro

Local: `projecto-completo.md:1588`

Tipo de alteração: reformulação das limitações futuras para assumir que já houve validação física, mas que esta deve ser aprofundada.

Texto alterado/introduzido no parágrafo:

> Do ponto de vista geométrico e produtivo, a validação física realizada deve ser aprofundada através de ensaios mais sistemáticos de montagem, tolerâncias, resistência, desgaste, repetibilidade de impressão e adequação ao uso.

## Alterações no DOCX

As mesmas alterações textuais foram aplicadas em `projecto-completo.docx`, nas secções correspondentes aos capítulos indicados acima, preservando a estrutura interna de comentários.

Validação técnica realizada sobre o DOCX actual:

- `projecto-completo.docx`: ficheiro ZIP válido, sem erros.
- versão detectada no DOCX: `0.4.17`.
- ocorrências de `PLA`: 4.
- ocorrências de `PETG`: 4.
- ocorrências de `PrusaSlicer 2.9.6`: 2.
- ocorrências de `Bambu Studio`: 2.
- ocorrências de `Bambu Lab A1`: 2.
- ocorrências dos termos substituídos associados ao slicing: 0.
- comentários preservados: 27 comentários, 27 referências, 16 intervalos ancorados.

## Delimitação metodológica acrescentada

O texto passou a explicitar que:

- foram feitas impressões 3D a partir dos resultados dos testes de perfil;
- as impressões foram realizadas em PLA e PETG;
- a preparação para impressão foi feita no PrusaSlicer 2.9.6 e no Bambu Studio;
- a impressão foi realizada numa Bambu Lab A1 com AMS;
- a razão da escolha dos materiais é comparativa: PLA para verificação rápida, estável e económica da geometria; PETG para observar uma alternativa mais resistente e menos frágil durante manipulação, encaixe e montagem preliminar;
- a validação física incidiu sobre viabilidade produtiva, coerência geométrica, preparação para impressão, geração do ficheiro de impressão, impressão, zonas críticas e montagem preliminar;
- esta etapa não constitui validação clínica, validação biomecânica completa, avaliação de conforto em utilizadores reais ou prova de durabilidade prolongada.
