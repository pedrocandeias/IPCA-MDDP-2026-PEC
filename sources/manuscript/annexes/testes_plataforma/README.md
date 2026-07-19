# Pacote de avaliação técnica da plataforma HandFab

**Estado:** campanhas executadas; resultados consolidados no Anexo B, incluindo a verificação manual de acessibilidade com sete resultados conformes e cinco não conformes.

**Data de criação:** 13 de julho de 2026.

**Secções da dissertação associadas:** 3.5, 5.1–5.3, 6.3, 7.1–7.4, 8.1–8.4 e 9.1–9.3.

## Finalidade

Este directório reúne os protocolos, modelos de relatório, resultados e instrumentos de registo verificável destinados à avaliação técnica da plataforma HandFab. A síntese orientada ao Design Industrial encontra-se em `anexo_b_avaliacao_processo_interface_handfab.md`. Os modelos técnicos separados são conservados como instrumentos de trabalho e devem ser lidos em conjunto com o anexo consolidado e com os resultados estruturados.

A selecção mínima destinada à entrega encontra-se em `suplementos/02_avaliacao_plataforma/`. Essa cópia exclui modelos por preencher, agregados redundantes e estados intermédios, conservando os metadados, comandos, identificadores e resultados necessários para sustentar o manuscrito.

Não são registados resultados presumidos. Os casos não concluídos ou não executados permanecem explicitamente identificados como parciais, inconclusivos ou pendentes.

## Sistema em avaliação

- Repositório local: `/home/pec/dev/ai-parametric-prosthetic-hand-generator`
- Aplicação local: `http://localhost:3000/dashboard`
- Aplicação pública: `https://handfab.pedrocandeias.net/`
- Protocolo de transporte local: HTTP, sem TLS
- Branch observada na preparação do protocolo: `staging`
- Versão observada na preparação do protocolo: `14.68.0`
- Commit observado na preparação do protocolo: `7e604558b337d02fff979169f057d6cbd0c80c0a`

Estes dados constituem apenas a referência inicial. Cada campanha de ensaio deve registar novamente a versão, o commit, o estado da árvore de trabalho, o ambiente e as dependências efectivamente utilizados.

Os resultados obtidos localmente e em produção devem permanecer separados. O ambiente local é a referência para testes funcionais, injecção controlada de falhas e repetição; o ambiente público deve limitar-se a verificações não destrutivas, auditorias de acessibilidade autorizadas e confirmação das diferenças introduzidas por HTTPS, domínio, cabeçalhos e configuração de deployment.

## Conteúdo

- `protocolo_geral_avaliacao_plataforma.md` — âmbito, conceitos operacionais, critérios e procedimento comum.
- `relatorio_repetibilidade_reprodutibilidade.md` — modelo de relatório para o percurso determinístico, comparação entre ambientes e variabilidade da IA.
- `relatorio_robustez_tecnica.md` — modelo de relatório para valores-limite, entradas inválidas, falhas previsíveis e recuperação.
- `relatorio_acessibilidade_wcag_2_2.md` — modelo de relatório de acessibilidade técnica segundo WCAG 2.2, nível AA.
- `matriz_casos_teste.csv` — inventário inicial dos casos, resultados esperados e evidências necessárias.
- `manifesto_evidencias.csv` — índice dos ficheiros produzidos durante cada execução.
- `modelo_metadados_execucao.json` — estrutura mínima para registar uma campanha de ensaio.
- `prompt_claude_code_implementar_testes.md` — instrução auditável para o Claude Code implementar a infraestrutura de ensaio.
- `anexo_b_avaliacao_processo_interface_handfab.md` — síntese dos métodos, resultados, limites e aprendizagens para o Design Industrial.
- `evidencias/` — cópia dos resultados estruturados e dos metadados essenciais das campanhas.

## Organização futura das evidências

As evidências devem ser guardadas sem sobrescrever campanhas anteriores, segundo a estrutura:

```text
evidencias/
  AAAA-MM-DD_HH-MM-SS_<campanha>/
    metadados.json
    logs/
    resultados/
    capturas/
    artefactos/
```

Cada ficheiro deve ser inscrito em `manifesto_evidencias.csv` com o caso de teste, o caminho, o tipo de evidência e o `checksum` SHA-256.

## Fluxo de trabalho

1. Fixar a versão da plataforma e preencher os metadados da campanha.
2. Rever a matriz e congelar os casos, critérios e tolerâncias antes da execução.
3. Implementar os testes automatizados, podendo usar Claude Code como apoio ao desenvolvimento.
4. Rever o código dos testes e executar os comandos numa sessão registada.
5. Preservar resultados brutos, logs, capturas e artefactos, incluindo falhas.
6. Preencher os três relatórios sem eliminar resultados discordantes.
7. Distinguir observação, interpretação e limitação em cada conclusão.
8. Só depois integrar a síntese nos capítulos 3, 8 e 9 e converter os relatórios em apêndices.

## Limite de interpretação

Os ensaios avaliam propriedades técnicas do protótipo e do fluxo digital. Não demonstram adequação clínica, conforto, eficácia protésica, usabilidade observada, aceitação ou acessibilidade percebida por pessoas com deficiência. A conformidade automatizada com critérios de acessibilidade também não substitui avaliação manual especializada nem participação de utilizadores.
