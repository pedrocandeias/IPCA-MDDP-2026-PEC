# Elicit Systematic Review Runbook

This runbook supports systematic reviews that are executed in the Elicit web interface but documented locally in this repository.

## Rule

Use:

1. `report`
2. `systematic review`

Do not start a systematic review until the preceding report has clarified:

- scope
- vocabulary
- likely anchor papers
- likely exclusion traps

## Local system

For each review, create or reuse:

`material/investigacao/elicit/systematic-reviews/<chapter>/<review-name>/`

Minimum files:

- `protocol.md`
- `eligibility-criteria.md`
- `search-strategy.md`
- `screening-log.md`
- `extraction-schema.md`
- `notes.md`
- `report-link.md`
- `ui-checklist.md`
- `status.md`

Recommended subfolders:

- `exports/`
- `screening/`
- `extraction/`

## Execution checklist in Elicit

### 1. Protocol

- enter the research question
- paste the eligibility framing from `protocol.md`
- configure review stages
- note any stage toggles locally

### 2. Gather

- run semantic searches first
- add keyword / Boolean searches if recall is weak
- record each query variant in `search-strategy.md`
- note why queries were kept, merged, or discarded

### 3. Screening

- apply title/abstract screening
- log ambiguous cases locally
- record exclusion reasons consistently

### 4. Full-text screening

- enable only if needed
- note activation date and rationale in `status.md`

### 5. Extraction

- map Elicit extraction columns to `extraction-schema.md`
- preserve the final extraction field list locally

### 6. Report

- export outputs
- store them in `exports/`
- update `notes.md` with findings, limitations, and chapter relevance

## Status discipline

After each meaningful review session, update:

- `status.md`
- `screening-log.md`
- `notes.md`

This prevents the Elicit UI from becoming the only place where review decisions exist.
