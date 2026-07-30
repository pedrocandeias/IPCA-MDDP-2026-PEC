# Prompt para Claude Code — implementação dos testes da dissertação

## Utilização

Executar este pedido no repositório:

`/home/pec/dev/ai-parametric-prosthetic-hand-generator`

Antes de executar, confirmar que as alterações locais e os ficheiros não versionados existentes pertencem ao utilizador e não devem ser removidos, revertidos ou incluídos inadvertidamente.

## Prompt

Trabalha no repositório `/home/pec/dev/ai-parametric-prosthetic-hand-generator` para implementar a infraestrutura de testes que produzirá evidência para uma dissertação de mestrado em Design e Desenvolvimento de Produto.

Lê integralmente `CLAUDE.md` antes de alterar qualquer ficheiro e cumpre todas as suas regras, incluindo a actualização coordenada de `CHANGELOG.md` e da versão em `package.json` quando houver alterações ao repositório. Preserva todas as alterações existentes e todos os ficheiros não versionados do utilizador. Não faças deploy, não alteres dados de produção e não imprimas nem guardes chaves de API, credenciais, tokens ou cookies.

Os documentos metodológicos autoritativos estão em:

- `/home/pec/dev/mestrado/anexos/testes_plataforma/protocolo_geral_avaliacao_plataforma.md`
- `/home/pec/dev/mestrado/anexos/testes_plataforma/matriz_casos_teste.csv`
- `/home/pec/dev/mestrado/anexos/testes_plataforma/modelo_metadados_execucao.json`
- `/home/pec/dev/mestrado/anexos/testes_plataforma/manifesto_evidencias.csv`

Ambientes:

- local: `http://localhost:3000/dashboard`
- público: `https://handfab.pedrocandeias.net/`

O ambiente local usa HTTP deliberadamente. Não o substituas por HTTPS e não mistures resultados locais com resultados de produção. Usa o ambiente local para testes funcionais, repetição, valores-limite e injecção controlada de falhas. No ambiente público limita-te a verificações não destrutivas e a auditorias de acessibilidade que não criem, alterem ou eliminem dados. Não executes percursos autenticados em produção sem uma conta de teste explicitamente fornecida.

### Objectivo

Criar testes automatizados e comandos reproduzíveis para três famílias:

1. repetibilidade e reprodutibilidade do percurso digital;
2. robustez técnica perante limites, entradas inválidas e falhas previsíveis;
3. acessibilidade segundo os critérios WCAG 2.2 de nível AA aplicáveis.

### Requisitos gerais

1. Inspecciona primeiro a arquitectura, os testes existentes, o `playwright.config.js`, os modelos, os ficheiros de configuração, os fluxos de autenticação e os endpoints. Resume o que encontraste antes de implementar.
2. Não alteres o comportamento funcional da plataforma apenas para fazer um teste passar. Se encontrares um defeito, regista-o; não o corrijas nesta tarefa sem autorização separada.
3. Mantém separados os testes que usam mocks dos testes que chamam serviços reais. Um resultado com mock nunca pode ser apresentado como repetição real da IA.
4. Qualquer teste que possa consumir uma API paga deve estar desactivado por omissão e exigir uma variável explícita, por exemplo `RUN_LIVE_AI_TESTS=1`.
5. Usa uma base de dados local isolada e dados sintéticos. Não uses perfis, credenciais ou dados pessoais reais.
6. Não incluas segredos em capturas, HTML, traces, vídeos, relatórios ou ficheiros JSON.
7. Produz resultados legíveis por máquina e por humanos. Preserva também as falhas; não elimines testes falhados dos relatórios.
8. Regista o commit, a versão, o estado da árvore de trabalho, Node.js, Playwright, navegadores, data, fuso horário, URL testado e comandos.
9. Calcula SHA-256 dos artefactos produzidos e actualiza um manifesto compatível com `manifesto_evidencias.csv`.
10. Não executes `git commit`, `git push` ou deploy.

### Estrutura pretendida

Adapta a estrutura às convenções existentes, mas procura disponibilizar comandos equivalentes a:

```text
npm run test:thesis:repetition
npm run test:thesis:robustness
npm run test:thesis:a11y:local
npm run test:thesis:a11y:public
npm run test:thesis
```

O comando agregado deve excluir, por omissão, chamadas pagas de IA e testes destrutivos ou autenticados em produção.

### Repetibilidade e reprodutibilidade

Implementa os casos `REP-*` da matriz. Para o percurso determinístico:

- usa configurações congeladas e identificadas;
- executa pelo menos dez repetições por caso;
- preserva STL/3MF quando produzidos;
- calcula `checksum`, tamanho, métricas dimensionais e, quando as ferramentas locais o permitirem, vértices, faces, volume, estanquidade, condição *manifold* e faces degeneradas;
- distingue diferença binária sem alteração geométrica de diferença geométrica real;
- permite comparação entre Chromium, Firefox e WebKit quando suportados.

Para a IA:

- cria uma suite simulada para esquema, limites, erros e recuperação;
- cria separadamente uma suite opcional de execuções reais repetidas;
- na suite real regista fornecedor, identificador exacto do modelo, prompt, esquema, definições, resposta bruta, resposta processada, erros, novas tentativas e tempos;
- calcula contagens e dispersão por parâmetro;
- nunca classifica variabilidade probabilística como falha apenas por as respostas não serem idênticas.

### Robustez

Implementa os casos `ROB-*` da matriz, incluindo:

- mínimo, máximo, abaixo do mínimo e acima do máximo;
- campo omisso, tipo inválido e campos contraditórios;
- país sem cobertura antropométrica directa;
- perfil incompatível com o limite mínimo de um modelo;
- resposta de IA inválida ou indisponível;
- falha de renderização;
- tentativa de exportação sem geometria válida;
- preservação do estado e possibilidade de recuperação.

Classifica o resultado como `passa`, `falha controlada`, `falha não controlada` ou `inconclusivo`, de acordo com o protocolo. Não introduzas falhas reais no ambiente público.

### Acessibilidade

Implementa os casos `ACC-*` da matriz. Integra uma ferramenta de auditoria compatível com Playwright, preferencialmente `@axe-core/playwright`, registando a versão exacta. Avalia WCAG 2.2 A e AA nos percursos e estados disponíveis:

- autenticação;
- dashboard;
- perfil;
- selecção e configuração do modelo;
- sugestão de IA;
- renderização/visualizador 3D;
- exportação;
- espera, sucesso e erro.

Para cada violação preserva regra, impacto, elemento afectado, selector, ajuda e captura quando possível. Gera também uma lista explícita de verificações manuais que a automação não resolve: teclado, foco, leitor de ecrã, ampliação/reformulação, mensagens dinâmicas e alternativa ao visualizador 3D.

Não declares conformidade global apenas porque a ferramenta automática não encontrou violações.

### Evidências e saída

Guarda cada campanha sem sobrescrever campanhas anteriores, preferencialmente em:

`test-results/thesis-evaluation/AAAA-MM-DD_HH-MM-SS_<campanha>/`

Inclui:

- `metadados.json`;
- logs;
- JSON/CSV de resultados;
- relatório HTML do Playwright quando aplicável;
- capturas, vídeos ou traces necessários;
- configurações congeladas;
- artefactos exportados e métricas;
- manifesto com SHA-256.

Não copies automaticamente grandes artefactos para o repositório da dissertação. No final, indica quais devem ser preservados e copiados para o pacote de anexos.

### Validação final

No final:

1. executa os testes locais que não exigem segredos nem serviços pagos;
2. apresenta os comandos exactos, contagens de testes, aprovações, falhas e exclusões;
3. identifica dependências ou navegadores em falta;
4. lista os ficheiros criados ou alterados;
5. explica qualquer desvio ao protocolo;
6. não ocultes falhas existentes;
7. não afirmes que os testes com utilizadores, a adequação clínica ou a eficácia protésica foram avaliados.
