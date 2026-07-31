# Elicit Manuscript Crosswalk

Map the existing Elicit searches, reports, and systematic review work to the
current structure of
`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md`.

## By manuscript section

| Manuscript section | Elicit assets already created | Primary purpose | Secondary reuse |
|---|---|---|---|
| `Capítulo 2 — Enquadramento teórico e estado da arte` | `material/investigacao/elicit/capitulo-2/` | Historical searches, reports, synthesis documents, and the structured report for section `2.5`. | Supports the chapter-level literature review; claims still require verification against the primary sources. |
| `6.1 Papel da IA no sistema proposto` | `material/investigacao/elicit/capitulo-6/6.1/searches/search-01.md` | Broad framing of AI roles in upper-limb prosthetic customization systems with explicit parametric CAD and clinician input. | Supports the opening framing for `6.2` by distinguishing AI support from autonomous generation. |
| `6.1 Papel da IA no sistema proposto` | `material/investigacao/elicit/capitulo-6/6.1/searches/search-02.md` | Human-in-the-loop and assistive AI framing for prosthetic or orthotic customization workflows. | Reusable in `6.3` for supervision, accountability, and override logic. |
| `6.1 Papel da IA no sistema proposto` | `material/investigacao/elicit/capitulo-6/6.1/searches/search-03.md` | Anthropometric input, parameter mapping, AI in digital prosthetic design, and additive manufacturing. | Strong bridge into `6.2` because it is closest to anthropometric-to-parameter translation. |
| `6.1 Papel da IA no sistema proposto` | `material/investigacao/elicit/capitulo-6/6.1/reports/5aaf1fab-74a5-4a0b-a871-eadf2ec0e219/` | Main Elicit report for the AI subsection. Grounds the claim that the literature is fragmented and lacks fully integrated workflows combining anthropometry, parametric CAD, AI suggestion, clinician oversight, and 3D printing. | Explicitly reusable in `6.2 IA na parametrização, personalização e apoio à decisão` and `6.3 Ajuste, validação e limitações éticas e técnicas`. |
| `7.1 Estratégia de interação e decisões de UI/UX` | `material/investigacao/elicit/capitulo-7/7.1/reports/5ae68d08-b402-450c-a052-028d7953596c/` | Main report for interface strategy, interaction sequencing, 3D preview, human-in-the-loop mediation, and clinician oversight in parametric prosthetic customization. | Feeds `7.2 Experiência do designer e do utilizador final` and `7.3 Mediação do processo de design e reflexão crítica`. |
| `7.1 Estratégia de interação e decisões de UI/UX` | `material/investigacao/elicit/systematic-reviews/capitulo-7/uiux-parametric-prosthetics/` | Systematic review protocol pack focused on interface, interaction, and human-in-the-loop configuration in digital prosthetic customization platforms. | Designed from the start for continuity into `7.2` and `7.3`. |

## By asset type

### Searches

| Asset | Linked manuscript section | Notes |
|---|---|---|
| `material/investigacao/elicit/capitulo-6/6.1/searches/search-01.md` | `6.1` | Broad AI-in-prosthetics framing; useful for context but noisier than later searches. |
| `material/investigacao/elicit/capitulo-6/6.1/searches/search-02.md` | `6.1` | Strongest conceptual support for assistive AI and human-in-the-loop logic. |
| `material/investigacao/elicit/capitulo-6/6.1/searches/search-03.md` | `6.1` | Best search for anthropometric translation, design workflow logic, and additive manufacturing links. |

### Reports

| Asset | Linked manuscript section | Notes |
|---|---|---|
| `material/investigacao/elicit/capitulo-6/6.1/reports/5aaf1fab-74a5-4a0b-a871-eadf2ec0e219/` | `6.1` | Main evidence base for the role of AI in the proposed system; also supports `6.2` and `6.3`. |
| `material/investigacao/elicit/capitulo-7/7.1/reports/5ae68d08-b402-450c-a052-028d7953596c/` | `7.1` | Main evidence base for interface strategy and interaction design in the platform chapter; also supports `7.2` and `7.3`. |

### Systematic reviews

| Asset | Linked manuscript section | Notes |
|---|---|---|
| `material/investigacao/elicit/systematic-reviews/capitulo-7/uiux-parametric-prosthetics/` | `7.1` primary; `7.2` and `7.3` secondary | Local protocol pack already prepared; this is not a Chapter 6 review. |

### Legacy Chapter 2 exports

| Asset | Linked manuscript section | Notes |
|---|---|---|
| `material/investigacao/elicit/capitulo-2/legacy-exports/` | `Capítulo 2` | Historical CSV, DOCX, PDF, and XLSX exports retained as raw research records. |
| `material/investigacao/elicit/capitulo-2/supporting-docx/` | `Capítulo 2` | Supporting Elicit syntheses in editable DOCX format. |
| `material/investigacao/elicit/capitulo-2/2.3/reports/legacy/parametric_design_additive_manufacturing.md` | `2.3` | Legacy report on parametric design, additive manufacturing, and product customization. |
| `material/investigacao/elicit/capitulo-2/2.4/reports/legacy/open_source_upper_limb_prostheses.md` | `2.4` | Legacy report on open-source, 3D-printable upper-limb prostheses and the available evidence base. |
| `material/investigacao/elicit/capitulo-2/2.5/reports/5a13094d-fe10-4caa-a182-6db2611bdf48/` | `2.5` | Structured report package with query, notes, JSON, Markdown, DOCX, and PDF. |
| `material/investigacao/elicit/capitulo-4/4.3/reports/legacy/openscad_web_ai_industrial_design.md` | `4.3` primary; `5.3` and `6.1` secondary | Legacy report on OpenSCAD for web-based parametric generation and AI-supported industrial design. |

## Coverage gaps in the canonical manuscript

No Elicit searches, reports, or systematic review packs are currently linked to:

- `Capítulo 1`
- `Capítulo 3`
- `Capítulo 4`
- `Capítulo 5`
- any `6.x` section outside the current `6.1` package
- any `7.x` section outside the current `7.1` package and its planned continuity into `7.2` and `7.3`

## Practical writing order

1. Reuse the `6.1` package first when drafting or revising `6.1`, then carry the strongest findings into `6.2` and `6.3`.
2. Use the `7.1` report before opening the full Chapter 7 systematic review workflow.
3. Treat the Chapter 7 systematic review as evidence-deepening for `7.1`, with controlled spillover into `7.2` and `7.3`.
