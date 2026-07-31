# Elicit Queries — Capítulo 6.1

## Scope
Papel da IA no sistema proposto.

Project constraints to keep in mind:
- clinicians or prosthetists enter anthropometric data
- the system uses explicit parametric OpenSCAD models rather than black-box geometry generation
- AI suggests parameter values; it does not directly replace the parametric model
- rendering is client-side via WebAssembly, while AI calls are proxied securely through the server
- saved configurations, RBAC, and human review are part of the workflow
- some anthropometric profiles are population-level reference datasets, not necessarily individual patient records

## Search Queries

### Search 1 — papel da IA em sistemas configuráveis com modelo paramétrico explícito

```text
What roles can artificial intelligence play in a web-based upper-limb prosthetic customization system where clinicians enter anthropometric data, explicit parametric CAD models generate the geometry, and AI suggests design or fabrication parameters rather than directly generating the prosthetic form?
```

Suggested filters:
- `minYear`: `2018`
- `maxResults`: `10`
- `type`: `Review`

### Search 2 — IA como camada assistiva e human-in-the-loop

```text
How is AI used as an assistive human-in-the-loop layer rather than a fully autonomous design system in digital workflows for prosthetic or orthotic customization?
```

Suggested filters:
- `minYear`: `2018`
- `maxResults`: `10`
- `type`: `Systematic Review`

### Search 3 — apoio à decisão com supervisão clínica e técnica

```text
What evidence exists on AI as decision support in prosthetic design workflows that still rely on explicit parametric models, clinician or prosthetist oversight, and human validation before fabrication?
```

Suggested filters:
- `minYear`: `2018`
- `maxResults`: `15`
- `pubmedOnly`: `true`

### Search 4 — dados antropométricos e tradução para parâmetros

```text
How are anthropometric measurements or reference anthropometric profiles translated into prosthetic design parameters, and what role does AI play in improving or accelerating that mapping?
```

Suggested filters:
- `minYear`: `2018`
- `maxResults`: `15`
- `type`: `Review`

## Report Queries

### Report 1 — enquadramento principal de 6.1

```text
How is artificial intelligence being integrated into upper-limb prosthetic customization systems that combine anthropometric input, explicit parametric CAD models, AI-based parameter suggestion, clinician oversight, and 3D-printing workflows?
```

Suggested settings:
- `maxSearchPapers`: `50`
- `maxExtractPapers`: `10`

### Report 2 — report alinhado com o sistema do repositório

```text
What literature is most relevant to an AI-assisted prosthetic hand generator where a clinician or prosthetist enters anthropometric data, an LLM suggests OpenSCAD-compatible design parameters, the model is previewed in-browser via WebAssembly, and the result is exported as an STL for 3D printing?
```

Suggested settings:
- `maxSearchPapers`: `50`
- `maxExtractPapers`: `10`

### Report 3 — foco em arquitetura sociotécnica do sistema

```text
What research is most relevant to systems where AI supports prosthetic customization through secure server-side inference, explicit parametric design models, user-role-controlled workflows, saved configurations, and human review before manufacturing?
```

Suggested settings:
- `maxSearchPapers`: `50`
- `maxExtractPapers`: `10`

## Continuity Notes

- `6.1` deve estabelecer a IA como camada de apoio ao sistema, não como substituição do modelo paramétrico, da modelação OpenSCAD ou da decisão clínica/técnica.
- A bibliografia recolhida aqui deve abrir caminho para `6.2`, sobretudo em temas de parameter suggestion, anthropometric translation, personalization logic, and decision support.
- Em `6.3`, reutilizar a bibliografia de `6.1` que discuta human oversight, validation, trust, safety, data governance, or accountability.
