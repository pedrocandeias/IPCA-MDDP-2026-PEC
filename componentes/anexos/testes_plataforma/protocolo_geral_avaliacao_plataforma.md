# Protocolo geral de avaliação técnica da plataforma HandFab

**Estado do documento:** protocolo anterior à execução.

**Versão do protocolo:** 0.1.

**Data:** 13 de julho de 2026.

## 1. Objectivo

O protocolo estabelece uma cadeia verificável para avaliar três propriedades da plataforma HandFab:

1. repetibilidade e reprodutibilidade do percurso digital;
2. robustez técnica perante variação, limites e falhas previsíveis;
3. acessibilidade técnica da interface relativamente aos critérios WCAG 2.2 de nível AA aplicáveis.

O objecto de análise é o protótipo técnico e os artefactos digitais que este produz. Não são unidades de análise a pessoa utilizadora, a adequação clínica da prótese ou o desempenho funcional do dispositivo.

## 2. Questões de avaliação

- Q1. Em que medida uma configuração aceite produz resultados equivalentes quando o percurso determinístico é repetido nas mesmas condições?
- Q2. Em que medida os resultados determinísticos se mantêm equivalentes nos navegadores e ambientes incluídos no ensaio?
- Q3. Que variabilidade apresentam as sugestões de IA quando a entrada e as definições declaradas permanecem constantes?
- Q4. Como responde a plataforma a valores-limite, entradas inválidas, incompatibilidades entre perfil e modelo e falhas previsíveis de serviços?
- Q5. Que critérios WCAG 2.2 de nível AA aplicáveis são satisfeitos ou violados nos percursos e estados avaliados?

## 3. Definições operacionais

### 3.1 Funcionamento técnico

Conclusão das operações previstas num caso de ensaio, no ambiente declarado, sem erro não tratado e com produção do resultado esperado. O funcionamento observado não equivale a robustez, usabilidade ou prontidão clínica.

### 3.2 Repetibilidade

Grau de concordância entre execuções realizadas com a mesma versão, ambiente, entrada e procedimento. Para a componente determinística, a concordância é avaliada por ficheiros, `checksums`, dimensões, topologia e métricas geométricas. Para a IA, são avaliadas conformidade do esquema, respeito pelos limites e dispersão dos valores sugeridos.

### 3.3 Reprodutibilidade

Grau em que o percurso pode ser reconstruído em ambientes declaradamente diferentes a partir dos mesmos dados, versões, parâmetros e procedimentos. Neste estudo, a comparação pode abranger navegadores distintos e, se disponível, mais do que um sistema operativo.

### 3.4 Robustez técnica

Capacidade do sistema para concluir casos válidos, preservar restrições e produzir respostas controladas perante valores-limite, entradas inválidas, incompatibilidades e falhas previsíveis. Uma mensagem explícita de rejeição pode constituir o resultado correcto; o simples encerramento inesperado da aplicação não constitui comportamento robusto.

### 3.5 Acessibilidade técnica

Conformidade observada dos conteúdos, controlos, estados e percursos avaliados com os critérios WCAG 2.2 de nível AA aplicáveis. Esta definição não inclui usabilidade percebida, facilidade de aprendizagem, acessibilidade económica ou experiência de pessoas com deficiência.

## 4. Proposições técnicas

- PT1. Depois de aceites os parâmetros, o percurso determinístico preserva resultados geometricamente equivalentes em execuções repetidas nas mesmas condições.
- PT2. A plataforma mantém as restrições codificadas e responde de forma controlada aos casos-limite e às entradas inválidas previstos no protocolo.
- PT3. As sugestões de IA apresentam variabilidade mensurável, mas os valores aplicados à configuração permanecem sujeitos ao esquema, aos limites e à validação determinística.
- PT4. A interface satisfaz parte dos critérios WCAG 2.2 de nível AA aplicáveis, sendo as conformidades, violações e verificações inconclusivas registadas por percurso e estado.

As proposições devem ser confirmadas, parcialmente confirmadas ou não confirmadas apenas depois da execução.

## 5. Ambiente e configuração a registar

Antes de cada campanha devem ser registados:

- data, hora e fuso horário;
- responsável pela execução;
- repositório, branch, commit e estado da árvore de trabalho;
- versão declarada no `package.json`;
- sistema operativo e arquitectura;
- versão do Node.js e do gestor de pacotes;
- versões do Playwright e dos navegadores;
- versão do OpenSCAD/WebAssembly;
- URL e ambiente exactos: local em `http://localhost:3000/dashboard` ou público em `https://handfab.pedrocandeias.net/`;
- fornecedor e identificador exacto do modelo de IA;
- parâmetros de amostragem, prompt, esquema e pós-processamento;
- ficheiros de configuração e modelos OpenSCAD usados;
- comandos de inicialização e de ensaio;
- limitações ou desvios ao protocolo.

Não devem ser guardadas chaves de API, credenciais, tokens, cookies de sessão ou dados pessoais.

Os ensaios locais e públicos constituem campanhas distintas. A injecção de falhas, alteração de estado, criação de dados e repetição intensiva devem decorrer localmente. No ambiente público apenas são permitidas verificações não destrutivas e previamente delimitadas, salvo autorização específica para utilizar uma conta e dados de teste.

## 6. Famílias de ensaio

### 6.1 Percurso determinístico

Para cada modelo e perfil seleccionado, a mesma configuração aceite deve ser executada pelo menos dez vezes no mesmo ambiente. Devem ser preservados os artefactos exportados e comparados:

- sucesso da renderização e da exportação;
- formato e tamanho do ficheiro;
- SHA-256, quando o formato for binariamente estável;
- número de vértices e faces;
- dimensões da caixa envolvente;
- volume, quando calculável;
- estanquidade, condição *manifold* e faces degeneradas;
- mensagens, avisos, tempos e falhas.

Se o `checksum` variar apesar de a geometria ser equivalente, a comparação deve usar métricas normalizadas e uma tolerância previamente declarada. A tolerância não pode ser escolhida depois de observados os resultados.

### 6.2 Comparação entre ambientes

Os casos determinísticos seleccionados devem ser repetidos, quando tecnicamente suportado, em Chromium, Firefox e WebKit. Qualquer diferença deve ser classificada como:

- diferença de serialização sem alteração geométrica;
- diferença geométrica dentro da tolerância;
- diferença geométrica fora da tolerância;
- incompatibilidade de execução;
- falha do ambiente.

### 6.3 Sugestões de IA

Cada cenário congelado deve ser repetido pelo menos dez vezes com o mesmo fornecedor, modelo, prompt, esquema e definições. Devem ser registados:

- resposta bruta e resposta após processamento;
- validade sintáctica e conformidade com o esquema;
- campos omissos, adicionais ou inválidos;
- respeito pelos intervalos;
- correspondência da lateralidade e da população de referência;
- valores aceites, corrigidos ou rejeitados;
- dispersão por parâmetro;
- erros, novas tentativas e tempos.

As execuções de IA medem repetibilidade e variabilidade, não identidade determinística.

### 6.4 Robustez e recuperação

Devem ser ensaiados casos normais, valores mínimo/máximo, valores fora da gama, campos omissos, contradições, idiomas diferentes, perfis não cobertos, incompatibilidades entre perfil e modelo, respostas inválidas da IA, indisponibilidade de serviço e falhas de renderização/exportação.

Para cada caso deve ser definido antes da execução se o comportamento correcto é concluir, limitar, rejeitar, pedir confirmação ou apresentar uma mensagem de erro.

### 6.5 Acessibilidade

A avaliação deve abranger os percursos críticos e estados transitórios da aplicação. A componente automática deve ser executada nas páginas autenticadas e não autenticadas com uma ferramenta integrável no Playwright. A componente manual deve incluir, pelo menos:

- navegação apenas por teclado;
- ordem, visibilidade e não obstrução do foco;
- nomes acessíveis e associação de rótulos;
- estrutura semântica e hierarquia de títulos;
- mensagens de erro e instruções;
- contraste e dependência exclusiva da cor;
- ampliação, reformulação e orientação;
- tamanho e activação dos alvos;
- autenticação acessível;
- alternativas ao visualizador tridimensional e aos estados exclusivamente visuais;
- verificação exploratória com leitor de ecrã.

O resultado deve ser registado por critério como `passa`, `falha`, `não aplicável` ou `inconclusivo`. Uma auditoria automática sem falhas não autoriza, por si só, uma declaração de conformidade global.

## 7. Critérios comuns de aceitação

- Todos os casos válidos devem terminar sem erro não tratado.
- Todos os casos inválidos devem ser rejeitados ou corrigidos de acordo com uma regra previamente declarada.
- Nenhuma execução pode expor credenciais, chaves, tokens ou dados pessoais nos relatórios.
- As diferenças entre execuções devem ser preservadas e explicadas, não eliminadas da amostra.
- Uma correcção implementada após uma falha exige um novo identificador de versão e um teste de regressão separado.
- Resultados obtidos antes e depois da correcção não podem ser agregados como se pertencessem à mesma versão.

## 8. Produção e preservação de evidência

Cada execução deve produzir, conforme aplicável:

- metadados da campanha;
- log do comando;
- relatório Playwright;
- resultados estruturados em JSON ou CSV;
- capturas de ecrã;
- respostas de IA sem segredos;
- configurações e parâmetros;
- geometrias exportadas;
- métricas de malha;
- registo de falhas e correcções;
- `checksum` SHA-256 dos artefactos.

O uso de Claude Code ou de outro assistente pode apoiar a escrita e a revisão do código de ensaio. A evidência científica reside, porém, no protocolo congelado, no código versionado, nos comandos, nos resultados brutos e na revisão do investigador.

## 9. Estratégia de análise

Os resultados quantitativos devem incluir contagens, proporções, intervalos, mínimos, máximos e medidas de dispersão adequadas. Os resultados qualitativos devem distinguir claramente:

1. observação;
2. diagnóstico técnico;
3. alteração efectuada;
4. teste de regressão;
5. conhecimento projectual extraído;
6. limite da interpretação.

## 10. Integração na dissertação

- Capítulo 3: síntese do protocolo, unidades de análise, instrumentos e critérios.
- Capítulos 5–7: referência aos requisitos e decisões efectivamente implementados.
- Capítulo 8: resultados, falhas, regressões e discussão.
- Capítulo 9: resposta delimitada às perguntas e proposições.
- Apêndices: protocolo completo, matriz de casos, relatórios e manifesto de evidências.

## 11. Referências normativas

- World Wide Web Consortium. (2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- World Wide Web Consortium. (2014). *Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0*. https://www.w3.org/TR/WCAG-EM/
- World Wide Web Consortium. (s.d.). *Selecting Web Accessibility Evaluation Tools*. https://www.w3.org/WAI/test-evaluate/tools/selecting/
