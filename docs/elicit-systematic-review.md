# Elicit Systematic Review Workflow

This project uses a two-step workflow for higher-rigor literature work:

1. `report`
2. `systematic review`

The `report` is used first to refine scope, terminology, anchor papers, and likely gaps. The `systematic review` is then used to run a more reproducible workflow with explicit screening and extraction.

## Why this order

- Reports are faster for early synthesis.
- Reports help reduce ambiguity before consuming a full systematic review workflow.
- Systematic reviews are better when a chapter or subsection needs stronger control over inclusion, exclusion, and extraction.

## Current limitation

The local CLI in `scripts/elicit_api.py` supports `search` and `report`, but this repository does not yet assume public API support for creating Elicit Systematic Reviews programmatically. Until that is confirmed, systematic reviews should be run through the Elicit web interface, with all protocol materials mirrored locally.

## Local folder convention

Use:

`sources/elicit/systematic-reviews/<chapter>/<review-name>/`

Recommended files:

- `protocol.md`
- `search-strategy.md`
- `eligibility-criteria.md`
- `screening-log.md`
- `extraction-schema.md`
- `notes.md`
- `report-link.md`

Recommended subfolders:

- `exports/`
- `screening/`
- `extraction/`

## Minimum protocol contents

### `protocol.md`

- research question
- rationale
- target manuscript section
- relationship to the preceding Elicit report

### `eligibility-criteria.md`

- inclusion criteria
- exclusion criteria
- population / device / workflow scope
- study design constraints

### `search-strategy.md`

- semantic search prompts
- keyword / Boolean searches
- date or source restrictions
- notes on query iterations

### `screening-log.md`

- screened in
- screened out
- reasons for exclusion
- unresolved borderline cases

### `extraction-schema.md`

- citation
- study type
- prosthetic scope
- personalization method
- interface / interaction findings
- AI role
- validation notes
- relevance to manuscript

## Recommended usage for Chapter 7

For `7.1`, use the current report first, then open a systematic review focused on:

- interaction design
- user interface strategy
- human-in-the-loop configuration
- digital prosthetic customization workflows
- anthropometric input and 3D preview
- clinician or designer oversight

## Sources

- Elicit Systematic Reviews: https://support.elicit.com/en/articles/7927169
- Workflow FAQ: https://support.elicit.com/en/articles/8863489
- Getting started with Elicit workflows: https://support.elicit.com/en/articles/1418881
