# Relatório de avaliação técnica de acessibilidade — WCAG 2.2

**Estado:** avaliação automática executada; avaliação manual pendente; síntese revista no Anexo B.

> Nota: este ficheiro conserva o modelo técnico original. Os resultados interpretados e as formulações autorizadas para a dissertação encontram-se em `anexo_b_avaliacao_processo_interface_handfab.md`; os valores brutos estão nas pastas `evidencias/2026-07-14_00-03-19_a11y-local/` e `evidencias/2026-07-14_00-06-48_a11y-public/`.

**Nível-alvo:** WCAG 2.2 AA.

**Campanha:** [identificador]

**Data:** [AAAA-MM-DD]

## 1. Objectivo e limite

Avaliar os critérios WCAG 2.2 de nível A e AA aplicáveis aos percursos críticos e estados seleccionados da plataforma HandFab.

O relatório não constitui, antes da execução completa e da revisão manual, uma declaração de conformidade. Também não substitui ensaios de usabilidade, participação de pessoas com deficiência ou avaliação de acessibilidade económica e organizacional.

## 2. Escopo

| Campo | Valor |
|---|---|
| Aplicação | HandFab |
| Repositório | `/home/pec/dev/ai-parametric-prosthetic-hand-generator` |
| URL local | `http://localhost:3000/dashboard` |
| URL pública | `https://handfab.pedrocandeias.net/` |
| Ambiente avaliado | local / público — seleccionar um por campanha |
| Protocolo local | HTTP, sem TLS |
| Branch/commit | [preencher] |
| Versão | [preencher] |
| Navegadores | [preencher] |
| Tecnologias assistivas | [preencher] |
| Ferramenta automática | [preencher] |
| Norma | WCAG 2.2, níveis A e AA |
| Responsável | [preencher] |

O uso de HTTP limita a campanha ao ambiente local. Critérios ou comportamentos dependentes de contexto seguro, instalação, cookies, cabeçalhos, domínio ou transporte devem ser avaliados numa campanha separada no ambiente HTTPS de produção. Os resultados dos dois ambientes não devem ser agregados sem identificar a sua origem.

## 3. Percursos e estados incluídos

| Identificador | Percurso/estado | Autenticado | Incluído | Observações |
|---|---|---|---|---|
| ACC-P01 | Entrada e autenticação | não/sim | sim | [preencher] |
| ACC-P02 | Dashboard | sim | sim | [preencher] |
| ACC-P03 | Gestão de perfil | sim | sim | [preencher] |
| ACC-P04 | Selecção e configuração de modelo | sim | sim | [preencher] |
| ACC-P05 | Sugestão de IA e confirmação | sim | sim | [preencher] |
| ACC-P06 | Visualização e renderização 3D | sim | sim | [preencher] |
| ACC-P07 | Exportação | sim | sim | [preencher] |
| ACC-P08 | Erros, espera e indisponibilidade | variável | sim | [preencher] |

## 4. Método

### 4.1 Avaliação automática

Executar a ferramenta integrada no Playwright em cada percurso e estado relevante, preservando o resultado estruturado, a captura e o HTML necessário para reproduzir a ocorrência.

### 4.2 Avaliação manual

Verificar, pelo menos:

- sequência completa apenas com teclado;
- foco visível e não obstruído;
- ordem de foco coerente;
- nomes, funções e estados acessíveis;
- associação entre rótulos, instruções, controlos e erros;
- estrutura de títulos e regiões;
- contraste e uso não exclusivo da cor;
- ampliação e reformulação do conteúdo;
- alvos de interacção;
- autenticação acessível;
- anúncios de actualizações dinâmicas;
- alternativa textual e funcional ao visualizador 3D;
- comportamento exploratório com leitor de ecrã.

## 5. Resultados automáticos

| Percurso | Página/estado | Violações críticas | Graves | Moderadas | Menores | Verificações manuais | Evidência |
|---|---|---:|---:|---:|---:|---:|---|
| [não executado] | — | 0 | 0 | 0 | 0 | 0 | — |

## 6. Resultados por critério WCAG

| Critério | Nível | Aplicável | Resultado | Percursos afectados | Evidência | Observação |
|---|---|---|---|---|---|---|
| [não executado] | — | — | não avaliado | — | — | — |

Resultados permitidos: `passa`, `falha`, `não aplicável` e `inconclusivo`.

## 7. Avaliação manual

| Verificação | Percurso | Resultado esperado | Resultado observado | Estado | Evidência |
|---|---|---|---|---|---|
| Navegação apenas por teclado | todos os percursos críticos | todas as operações essenciais são alcançáveis e accionáveis | não executado | não avaliado | — |
| Foco visível | todos | foco perceptível e não obstruído | não executado | não avaliado | — |
| Leitor de ecrã | amostra representativa | nomes, funções, estados e alterações são anunciados | não executado | não avaliado | — |
| Ampliação/reformulação | todos | ausência de perda de conteúdo ou funcionalidade no nível testado | não executado | não avaliado | — |
| Visualizador 3D | configuração/renderização | alternativa suficiente para informação e operações essenciais | não executado | não avaliado | — |

## 8. Barreiras identificadas e correcções

| Identificador | Critério | Barreira | Impacto | Correcção | Versão | Regressão | Estado |
|---|---|---|---|---|---|---|---|
| [não executado] | — | — | — | — | — | — | — |

## 9. Síntese

| Estado | Número de critérios aplicáveis |
|---|---:|
| Passa | 0 |
| Falha | 0 |
| Inconclusivo | 0 |
| Não aplicável | 0 |

## 10. Discussão

### 10.1 Conformidades observadas

[Preencher.]

### 10.2 Barreiras técnicas

[Preencher.]

### 10.3 Aspectos que exigem utilizadores ou especialistas

[Preencher.]

## 11. Conclusão

**Estado da proposição PT4:** não avaliada.

**Declaração de conformidade:** não emitida.

**Formulação autorizada para a dissertação:** [preencher depois da execução].

## 12. Evidências associadas

| Identificador | Caminho | SHA-256 | Descrição |
|---|---|---|---|
| [não executado] | — | — | — |

## 13. Referências normativas

- World Wide Web Consortium. (2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- World Wide Web Consortium. (2014). *Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0*. https://www.w3.org/TR/WCAG-EM/
- World Wide Web Consortium. (s.d.). *Selecting Web Accessibility Evaluation Tools*. https://www.w3.org/WAI/test-evaluate/tools/selecting/
