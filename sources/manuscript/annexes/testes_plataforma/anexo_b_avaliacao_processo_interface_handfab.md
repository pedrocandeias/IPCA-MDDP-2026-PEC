# Anexo B — Avaliação do processo paramétrico e da interface da plataforma HandFab

**Data das séries de ensaios:** 13 e 14 de Julho de 2026

**Versão avaliada:** HandFab 14.69.0

**Plataforma pública:** <https://handfab.pedrocandeias.net/>

**Estado da avaliação:** executada, com resultados parciais e verificações manuais ainda por realizar

## B.1 Finalidade

Este anexo documenta a avaliação complementar da plataforma HandFab a partir de questões relevantes para o Design Industrial. O objectivo não foi certificar o programa informático, mas examinar se o processo de configuração apresenta um comportamento suficientemente previsível para apoiar a actividade projectual, se preserva o trabalho realizado quando surgem entradas ou falhas problemáticas e se a interface apresenta problemas detectáveis por regras automáticas de acessibilidade digital.

A avaliação foi organizada em três dimensões:

1. **previsibilidade**, entendida como a capacidade de uma configuração fixa produzir a mesma geometria nas execuções concluídas;
2. **recuperação e controlo**, entendidos como a capacidade de limitar, rejeitar ou explicar valores problemáticos sem destruir a configuração válida;
3. **verificação automática de regras seleccionadas de acessibilidade digital**, entendida como a identificação de barreiras detectáveis nos estados examinados, sem a confundir com usabilidade, acessibilidade percebida por participantes ou conformidade global com as WCAG.

## B.2 Âmbito e limites

Os ensaios locais decorreram numa cópia isolada da plataforma e usaram exclusivamente perfis de ensaio. A plataforma pública foi examinada apenas na página de entrada, sem autenticação ou alteração de dados. Não participaram utilizadores, pessoas com diferença de membro, profissionais clínicos ou técnicos de prótese.

Por conseguinte, este anexo não avalia conforto, ajuste anatómico individual, eficácia protésica, segurança, durabilidade, aprendizagem, satisfação ou uso quotidiano. Também não constitui declaração de conformidade com as Web Content Accessibility Guidelines (WCAG) 2.2.

## B.3 Procedimento

Foram fixadas configurações de referência para o Flexy Beast, o Paraglider Hand e a UnLimbited Phoenix. Cada configuração deveria ser gerada e exportada dez vezes. Os ficheiros concluídos foram comparados quanto à identidade do conteúdo e às principais características geométricas.

Uma configuração da UnLimbited Phoenix foi ainda executada em três navegadores. Esta comparação procurou verificar se o percurso produzia a mesma geometria em ambientes de visualização distintos; não corresponde a uma reprodução por outra equipa ou noutro sistema de fabrico.

Os cenários de controlo abrangeram valores nos limites, valores abaixo e acima dos limites, campos obrigatórios ausentes, texto num campo numérico, contradição entre idade e descrição, país sem correspondência directa na base, perfil inferior ao limite de um modelo, indisponibilidade da sugestão de IA, resposta inválida, falha de geração e tentativa de exportação sem geometria.

A acessibilidade foi examinada automaticamente em oito estados do percurso local: autenticação, painel principal, perfil inicial, perfil com erro, parâmetros, sugestão antes e depois da resposta e geometria apresentada. A página pública de entrada foi examinada separadamente. Foi preparada uma lista de verificações manuais, mas essa etapa não foi executada.

## B.4 Resultados de previsibilidade

### B.4.1 Repetição da mesma configuração

Tabela B.1 — Resultados da repetição da mesma configuração por modelo

| Modelo | Execuções previstas | Execuções concluídas | Ficheiros distintos entre as conclusões | Resultado |
|---|---:|---:|---:|---|
| Flexy Beast | 10 | 7 | 1 | Consistente nas conclusões; critério integral não atingido |
| Paraglider Hand | 10 | 5 | 1 | Consistente nas conclusões; critério integral não atingido |
| UnLimbited Phoenix | 10 | 5 | 1 | Consistente nas conclusões; critério integral não atingido |

Dentro de cada modelo, todas as execuções concluídas produziram um único ficheiro distinto: o conteúdo binário, as dimensões, o número de faces e as restantes métricas registadas permaneceram iguais. Algumas execuções foram interrompidas por bloqueios e tempos-limite no ambiente de ensaio. Como não foram obtidas as dez conclusões previstas por modelo, o resultado global é classificado como **parcial** e não como confirmação integral da repetibilidade.

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

| Situação examinada | Comportamento observado | Leitura para o processo de design |
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

Os resultados mostram que a maioria das situações previstas preservou o estado válido ou permitiu recuperação. As duas últimas situações são, contudo, fragilidades relevantes: uma salvaguarda visual não basta se o mesmo valor puder entrar por outra etapa, e um limite apenas detectado não protege a geometria se a sugestão continuar a ser aplicada. A decisão projectual resultante é concentrar a verificação antes de qualquer valor ser guardado ou enviado ao modelo paramétrico.

Os ensaios relativos à IA recorreram a respostas simuladas e controladas. Confirmam o comportamento da interface perante respostas previstas, mas não medem estabilidade, dispersão ou qualidade de um modelo de linguagem real. Não foi executada uma série extensa de repetições com chamadas reais ao fornecedor de IA.

## B.6 Resultados da verificação automática de acessibilidade digital

### B.6.1 Percurso local autenticado

Foram examinados oito estados da interface. O total de treze ocorrências corresponde à soma das regras assinaladas em cada estado, e não a treze tipos diferentes de barreira. Foram identificadas quatro categorias:

Tabela B.4 — Categorias de problemas de acessibilidade digital detectadas automaticamente

| Categoria | Gravidade indicada pelo instrumento | Estados afectados | Consequência de design |
|---|---|---:|---|
| Contraste de cor insuficiente | Grave | 8 | Texto e controlos podem perder legibilidade para pessoas com baixa visão ou em condições visuais desfavoráveis |
| Rótulo não associado ao controlo | Crítica | 3 | O significado de campos e cursores pode não ser comunicado por tecnologias de apoio |
| Elementos interactivos aninhados | Grave | 1 | Pode originar foco e activação ambíguos |
| Elemento de selecção sem nome acessível | Crítica | 1 | A função do controlo pode não ser identificável fora da apresentação visual |

As ocorrências envolveram 47 elementos para contraste, 21 para associação de rótulos, quatro elementos interactivos aninhados e um elemento de selecção sem nome. Alguns elementos aparecem em mais do que um estado, pelo que estas contagens não representam necessariamente componentes únicos.

### B.6.2 Superfície pública

Na página pública não autenticada não foram detectadas violações automáticas entre os elementos examinados; oito verificações foram classificadas como aprovadas e uma ficou incompleta. Este resultado limita-se à página de entrada e não pode ser generalizado ao painel autenticado ou ao percurso de configuração.

### B.6.3 Verificação manual pendente

Permanecem por avaliar manualmente a navegação por teclado, a visibilidade e ordem do foco, a associação de nomes e erros, os anúncios de alterações, a ampliação e reformulação do conteúdo, o tamanho dos alvos, a autenticação, a alternativa ao visualizador tridimensional e o comportamento com leitor de ecrã. Sem estes ensaios não é emitida qualquer declaração de conformidade com as WCAG 2.2.

## B.7 Aprendizagens para o Design Industrial

1. **A previsibilidade deve ser demonstrada na cadeia completa.** A igualdade entre ficheiros concluídos é útil, mas deve ser acompanhada pela taxa de conclusão e pela qualidade da geometria produzida.
2. **Os limites devem ser visíveis e actuar em todas as etapas.** Não basta limitar um cursor se o valor puder ser aceite ou aplicado por outro percurso.
3. **A recuperação protege a continuidade do trabalho projectual.** Preservar a última configuração válida, explicar a falha e permitir nova tentativa reduz a perda de trabalho durante a exploração de alternativas.
4. **A acessibilidade é uma qualidade concreta da interface.** Contraste, rótulos, foco, nomes acessíveis e alternativas à visualização tridimensional devem ser tratados como requisitos verificáveis.
5. **A compatibilidade não deve ser presumida.** A conclusão em dois navegadores não permite generalizar para todos os ambientes; o percurso incompleto em WebKit deve permanecer como questão aberta.
6. **A IA necessita de limites anteriores à aplicação.** As sugestões podem apoiar a exploração inicial, mas a geometria só deve receber valores já verificados pelas regras determinísticas do modelo.

## B.8 Conclusão

As séries de ensaios fornecem evidência parcial de que o núcleo paramétrico produz resultados consistentes nas execuções concluídas e de que vários estados de erro preservam o trabalho anterior ou permitem recuperação. Também revelam fragilidades concretas na aplicação uniforme dos limites, na aceitação de tipos de dados e na acessibilidade da interface.

O resultado não autoriza afirmar que a plataforma é robusta, acessível ou compatível com todos os navegadores em termos gerais. Autoriza uma formulação mais delimitada: **nos casos examinados, o processo apresentou consistência das geometrias concluídas, recuperou de várias falhas previstas e permitiu identificar prioridades objectivas de revisão da interface e das salvaguardas paramétricas**.

## B.9 Ficha técnica e proveniência das evidências

Esta secção conserva apenas a informação necessária para identificar as séries de ensaios. Os pormenores de implementação dos testes não integram o argumento principal da dissertação.

Tabela B.5 — Identificação das séries complementares de avaliação da plataforma

| Série de ensaios | Ambiente | Instrumentos | Evidência principal |
|---|---|---|---|
| `2026-07-13_23-22-21_repetition` | Instância local isolada, perfis de ensaio | Playwright 1.59.1; análise de STL | Resultados por modelo, ficheiros exportados e comparação entre navegadores |
| `2026-07-14_00-02-40_robustness` | Instância local isolada, perfis de ensaio | Playwright 1.59.1 | Casos nominais, limites, entradas inválidas e recuperação |
| `2026-07-14_00-03-19_a11y-local` | Percurso local autenticado | axe-core 4.12.1 integrado no Playwright | Resultados por estado e lista de verificação manual |
| `2026-07-14_00-06-48_a11y-public` | Página pública não autenticada | axe-core 4.12.1 integrado no Playwright | Resultado automático da página de entrada |

As séries de ensaios correspondem ao estado técnico documentado nos respectivos metadados. O código de ensaio, os resultados estruturados e os registos necessários à interpretação das execuções foram conservados no Suplemento 2 — Avaliação técnica da plataforma.

Os resultados estruturados seleccionados integram o Suplemento 2, organizados pelos identificadores técnicos originais de cada série. Os agregados internos e os estados intermédios redundantes não integram o pacote de entrega.

## B.10 Referências normativas

- World Wide Web Consortium. (2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- World Wide Web Consortium. (2014). *Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0*. https://www.w3.org/TR/WCAG-EM/
