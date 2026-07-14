# Relatório de robustez técnica da plataforma

**Estado:** campanha executada; síntese revista no Anexo B.

> Nota: este ficheiro conserva o modelo técnico original. Os resultados interpretados e as formulações autorizadas para a dissertação encontram-se em `anexo_b_avaliacao_processo_interface_handfab.md`; os valores brutos estão em `evidencias/2026-07-14_00-02-40_robustness/`.

**Campanha:** [identificador]

**Data:** [AAAA-MM-DD]

## 1. Objectivo

Avaliar o comportamento da plataforma perante casos válidos, valores-limite, entradas inválidas, incompatibilidades e falhas previsíveis, distinguindo funcionamento nominal de resposta robusta.

## 2. Configuração da campanha

| Campo | Valor |
|---|---|
| Repositório | `/home/pec/dev/ai-parametric-prosthetic-hand-generator` |
| Ambiente | local — a robustez com injecção de falhas não deve ser ensaiada em produção |
| URL local | `http://localhost:3000/dashboard` |
| URL pública de referência | `https://handfab.pedrocandeias.net/` |
| Branch/commit | [preencher] |
| Versão | [preencher] |
| Sistema e navegador | [preencher] |
| Modelos OpenSCAD | [preencher] |
| Ficheiros de configuração | [preencher] |
| Serviço/modelo de IA | [preencher] |
| Responsável | [preencher] |

## 3. Critérios de classificação

- **Passa:** conclui, limita, rejeita ou pede confirmação exactamente como definido no caso.
- **Falha controlada:** não conclui a operação, mas preserva o estado, apresenta mensagem compreensível e permite recuperação.
- **Falha não controlada:** erro não tratado, bloqueio, perda de estado, resultado silenciosamente incorrecto ou exposição de informação sensível.
- **Inconclusivo:** a evidência não permite determinar o comportamento.

## 4. Resultados por categoria

### 4.1 Casos nominais

| Caso | Pré-condição | Resultado esperado | Resultado observado | Estado | Evidência |
|---|---|---|---|---|---|
| [não executado] | — | — | — | não executado | — |

### 4.2 Valores-limite

| Caso | Parâmetro | Limite | Valor ensaiado | Comportamento esperado | Comportamento observado | Estado |
|---|---|---:|---:|---|---|---|
| [não executado] | — | — | — | — | — | não executado |

### 4.3 Entradas inválidas ou incompletas

| Caso | Entrada | Regra aplicável | Resposta esperada | Resposta observada | Estado |
|---|---|---|---|---|---|
| [não executado] | — | — | — | — | não executado |

### 4.4 Incompatibilidades entre perfil e modelo

| Caso | Perfil | Modelo | Incompatibilidade esperada | Salvaguarda esperada | Resultado | Estado |
|---|---|---|---|---|---|---|
| [não executado] | — | — | — | — | — | não executado |

### 4.5 Falhas de serviço e recuperação

| Caso | Falha induzida | Estado anterior preservado | Mensagem apresentada | Recuperação possível | Estado |
|---|---|---|---|---|---|
| [não executado] | — | — | — | — | não executado |

## 5. Síntese quantitativa

| Categoria | Casos | Passa | Falha controlada | Falha não controlada | Inconclusivo |
|---|---:|---:|---:|---:|---:|
| Nominais | 0 | 0 | 0 | 0 | 0 |
| Limites | 0 | 0 | 0 | 0 | 0 |
| Inválidos/incompletos | 0 | 0 | 0 | 0 | 0 |
| Incompatibilidades | 0 | 0 | 0 | 0 | 0 |
| Serviços/recuperação | 0 | 0 | 0 | 0 | 0 |

## 6. Falhas, alterações e regressão

| Identificador | Observação | Diagnóstico | Alteração | Versão | Teste de regressão | Resultado | Conhecimento projectual |
|---|---|---|---|---|---|---|---|
| [não executado] | — | — | — | — | — | — | — |

## 7. Discussão

### 7.1 Funcionamento nominal observado

[Preencher.]

### 7.2 Robustez sustentada pelos ensaios

[Preencher sem generalizar para casos não testados.]

### 7.3 Fragilidades e comportamento residual

[Preencher.]

## 8. Limitações

- Os casos cobrem apenas falhas previsíveis incluídas na matriz.
- Robustez de software não demonstra resistência mecânica, durabilidade ou segurança do dispositivo físico.
- A ausência de erro numa amostra não demonstra ausência de erro em todas as configurações.
- Outras limitações: [preencher].

## 9. Conclusão

**Estado da proposição PT2:** não avaliada.

**Formulação autorizada para a dissertação:** [preencher depois da execução].

## 10. Evidências associadas

| Identificador | Caminho | SHA-256 | Descrição |
|---|---|---|---|
| [não executado] | — | — | — |
