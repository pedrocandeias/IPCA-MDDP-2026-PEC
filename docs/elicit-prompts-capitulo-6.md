# Prompts Elicit — Capítulo 6

Estes prompts foram escritos para o projeto [`ai-parametric-prosthetic-hand-generator`](https://github.com/pedrocandeias/ai-parametric-prosthetic-hand-generator), cujo sistema usa dados antropométricos, IA para sugerir parâmetros, OpenSCAD para modelação paramétrica e exportação STL para fabrico.

## Objetivo

Recolher literatura e relatórios do Elicit para sustentar:

- `6.1 Papel da IA no sistema proposto`
- `6.2 IA na parametrização, personalização e apoio à decisão`
- `6.3 Ajuste, validação e limitações éticas e técnicas`

## Prompt principal do capítulo

Use este prompt em `report` para um levantamento mais abrangente:

```text
How is artificial intelligence being integrated into parametric customization systems for upper-limb prosthetics, especially for anthropometric input processing, parameter suggestion, decision support, and validation of personalized 3D-printable devices?
```

## Prompts por subsecção

### 6.1 Papel da IA no sistema proposto

```text
What roles can artificial intelligence play in a web-based parametric prosthetic customization system where clinicians enter anthropometric data and the system suggests 3D-printing parameters for upper-limb prosthetic devices?
```

```text
How is AI used as an assistive layer rather than a fully autonomous design system in digital workflows for prosthetic or orthotic customization?
```

```text
What evidence exists on AI as decision support in prosthetic design workflows that still rely on explicit parametric models, clinician oversight, and human validation?
```

### 6.2 IA na parametrização, personalização e apoio à decisão

```text
How can AI support parameter selection and personalization in parametric CAD or computational design systems for prosthetic and assistive devices?
```

```text
What methods are used to translate anthropometric measurements into personalized geometric parameters for prosthetic design, and where does AI improve this process?
```

```text
How is machine learning or generative AI used to recommend design parameters, fit adjustments, or fabrication settings in personalized prosthetic and orthotic systems?
```

```text
What are the benefits and risks of using AI for decision support in anthropometric-driven customization of upper-limb prostheses?
```

### 6.3 Ajuste, validação e limitações éticas e técnicas

```text
How are AI-assisted prosthetic customization systems validated in terms of fit, comfort, manufacturability, and clinician trust?
```

```text
What technical limitations affect AI-generated parameter suggestions in personalized prosthetic or orthotic design systems?
```

```text
What ethical issues arise when AI is used to process anthropometric data and recommend personalized prosthetic configurations?
```

```text
What frameworks or best practices exist for human oversight, transparency, data minimization, and accountability in AI-supported medical or assistive device customization?
```

## Prompts focados no teu sistema

Estes são mais próximos da arquitetura concreta do repositório.

```text
What literature is most relevant to an AI-assisted prosthetic hand generator where a clinician enters patient anthropometric data, an LLM suggests OpenSCAD-compatible design parameters, the model is previewed in-browser, and the result is exported for 3D printing?
```

```text
What evidence supports the use of secure server-side AI proxies and human-in-the-loop validation in prosthetic customization platforms that combine web interfaces, parametric CAD, and AI-generated parameter suggestions?
```

```text
How should a system that uses Claude or GPT-4 to suggest prosthetic design parameters be evaluated for reliability, explainability, and safety before those suggestions are accepted by clinicians or technicians?
```

## Prompts curtos para `search`

Use estes em `search` quando quiseres recolha rápida de artigos.

```text
AI decision support in prosthetic customization
```

```text
anthropometric data parameter recommendation prosthetic design
```

```text
parametric CAD personalization upper limb prosthetics AI
```

```text
human in the loop AI prosthetic design validation
```

```text
ethical issues AI anthropometric data medical device personalization
```

## Filtros recomendados no Elicit

Para melhorar a relevância:

- `minYear`: `2018`
- `type`: `Review`, `Systematic Review`, `Meta-Analysis`, `RCT` quando aplicável
- `pubmedOnly`: `true` para tópicos mais clínicos
- `maxResults`: `20` a `50` em pesquisa exploratória

## Sequência recomendada

1. Executar o `prompt principal do capítulo`
2. Executar um relatório separado para cada subsecção 6.1, 6.2 e 6.3
3. Usar os `prompts curtos para search` para preencher lacunas
4. Comparar resultados clínicos, técnicos e éticos
5. Integrar no texto apenas o que for diretamente aplicável ao sistema descrito no repositório
