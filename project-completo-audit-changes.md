# Comparação das alterações — projecto-completo-audit

Comparação entre `projecto-completo.md` e `projecto-completo-audit.md`, gerada em 2026-06-06.

## Resumo quantitativo

| Métrica | Original | Versão auditada | Diferença |
| --- | ---: | ---: | ---: |
| Linhas | 1435 | 1243 | -192 |
| Palavras | 33703 | 21395 | -12308 |
| Caracteres | 252647 | 164502 | -88145 |
| Títulos Markdown | 100 | 84 | -16 |

Redução aproximada: 12308 palavras (36.5% do texto original).

## Critério editorial usado

A versão auditada não altera `projecto-completo.md`. O objetivo foi produzir uma proposta alternativa com menor redundância, preservando a bibliografia e a maioria das referências já existentes. O corte concentrou-se em repetições funcionais: passagens em que o mesmo argumento era reintroduzido em vários capítulos como enquadramento completo.

## Padrões de repetição identificados

| Padrão | Onde aparecia | Tratamento na versão auditada |
| --- | --- | --- |
| Personalização, parametrização e IA como resposta central | 1.1-1.3, 2.3, 2.5, 3.1-3.3, 5.1, 6.1, 7.3 | Mantida na introdução e no enquadramento; capítulos posteriores passam a aplicar a ideia em vez de a reexplicar. |
| Antropometria como base da personalização | 2.4, 3.4, 4.2, 6.3 | Capítulo 2 ficou conceptual; detalhe da base local e normalização permanece no Capítulo 4. |
| IA como apoio, não substituição | 2.5, 5.4, 6.1-6.4, 7.3 | Capítulo 2 define o princípio; Capítulo 6 descreve a implementação e os limites. |
| Plataforma como mediação sociotécnica | 2.6, 5.1, 7.1-7.3 | Capítulo 2 apresenta fundamentos; Capítulos 5 e 7 descrevem arquitetura e experiência sem repetir a teoria. |
| Limitações e validação | 2.7, 3.5, 6.4, 8 | Limitações metodológicas ficam em 3.5; limites da IA em 6.4; avaliação em 8. |

## Alterações por capítulo

| Capítulo | Alterações principais |
| --- | --- |
| 1 | Reescrito para reduzir repetição inicial, corrigir o salto de numeração com nova secção `1.4 Questões de investigação`, separar objetivos de perguntas de investigação e clarificar a tese central. |
| 2.1 | Removidos comentários visíveis de revisão; subsecções internas convertidas para nível hierárquico inferior; linguagem ajustada para português europeu. |
| 2.4 | Reduzido e reenquadrado: mantém conceito, métodos e limitações; desloca o detalhe operacional da base antropométrica para o Capítulo 4. |
| 2.5 | Reduzido para enquadramento conceptual da IA; evita repetir o Capítulo 6. |
| 2.6 | Reduzido para fundamentos de plataformas configuráveis; evita repetir arquitetura, perfis e UI/UX dos Capítulos 5 e 7. |
| 2.7 | Corrigido o artefacto `![Shape][image1]` no título e uniformizada a capitalização da lista final. |
| 3 | Reescrito de forma mais sintética, mantendo RTD, Double Diamond, fases, métodos, critérios e limitações. |
| 4.1 | Reescrito como operacionalização das lacunas, evitando reabrir todo o enquadramento teórico sobre abandono e requisitos. |
| 4.2 | Mantido maioritariamente, porque é o local mais adequado para a descrição técnica da base antropométrica. |
| 4.3-4.4 | Mantidas, com correção da numeração da tabela `4.3.1` para `4.7`. |
| 5 | Reescrito para reduzir repetição entre mediação, arquitetura, WASM, IA e gestão de modelos; preserva os elementos técnicos essenciais. |
| 6 | Reescrito para focar o papel da IA no sistema, a separação entre vetor numérico e contexto semântico, validação interna e limites éticos/técnicos. |
| 7 | Reescrito para distinguir UI/UX, perfis de uso e mediação crítica sem repetir capítulos 5 e 6. |
| 8 | Substituídos títulos vazios por uma estrutura sugerida de avaliação sem inventar resultados. |
| 9 | Substituídos títulos vazios por conclusões sugeridas e limitações, formuladas como síntese metodológica e não como validação clínica. |
| Bibliografia | Mantida, com os IDs bibliográficos duplicados `ref-romero-2025` e `ref-menaka-2025` restaurados onde existiam no original; as ligações internas sem alvo foram verificadas e corrigidas quando necessário. |

## Correções editoriais adicionais

- Restauradas as marcas de notas/comentários de revisão `[^1]` a `[^13]` e os respetivos comentários finais como artefactos editoriais preservados.
- Corrigidas ocorrências selecionadas de português brasileiro para português europeu em texto revisto, como `controle` -> `controlo`, `fabricação` -> `fabrico`, `contato` -> `contacto` e `sinônimo` -> `sinónimo`; também foram corrigidos erros mecânicos gerados pela normalização anterior, como `assumnum`, `expõnum` e `permitnuma`.
- Mantida a cautela metodológica nos capítulos 8 e 9: a versão auditada não afirma resultados clínicos, conforto real ou eficácia terapêutica, porque esses dados não constam do manuscrito original.
- Mantida a maioria das figuras e tabelas existentes; as secções reduzidas conservam as figuras que ajudam a evitar explicação textual repetida.
- Corrigidas citações internas semanticamente ambíguas, por exemplo `Romero et al. (2025)` para `da Silveira Romero et al. (2025)` quando o alvo é `ref-da-silveira-romero-2025`.

## Questões ainda por resolver antes de aplicar ao manuscrito principal

1. Rever a bibliografia de forma dedicada antes de aplicar ao manuscrito principal, decidindo se os IDs duplicados devem ser preservados como estado de trabalho ou resolvidos numa etapa final de publicação.
2. Uniformizar todas as citações remanescentes para o mesmo formato autor-ano com ligações internas.
3. Confirmar se os capítulos 8 e 9 devem permanecer como estrutura metodológica ou aguardar resultados reais antes de serem incorporados.
4. Fazer uma revisão fina de português europeu no texto mantido sem reescrita, sobretudo nas secções técnicas longas do Capítulo 4.
