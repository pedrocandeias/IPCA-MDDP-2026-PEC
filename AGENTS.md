# Repository Guidelines

## Project Structure & Module Organization
This repository is organized as a thesis workspace rather than an application codebase. Keep the consolidated manuscript in the root as `Projecto completo.md`. Chapter drafts live in `chapters/text/`, HTML exports in `chapters/html/`, general supporting `.docx` files in `sources/docx/`, and chapter 2 research exports in `sources/capitulo2/`. Keep new material close to the chapter it supports and avoid mixing raw exports with polished manuscript files.

## Build, Test, and Development Commands
No build system, package manager, or automated test runner was detected in this workspace. Use lightweight validation commands when editing:

```bash
rg --files .
find chapters sources -maxdepth 2 -type f
```

Use these to confirm file placement and naming. For Markdown or HTML edits, preview locally in your editor before committing. When exporting revised chapter assets, keep the editable source alongside the exported format.

## Coding Style & Naming Conventions
Preserve the existing document-first style. Use clear section headings, short paragraphs, and consistent academic Portuguese where a file already uses it. Follow existing filename patterns such as `cap_2_5.txt` or `capitulo_4_3_1.html`. Prefer lowercase names with underscores, and keep chapter-related files grouped by chapter number. Avoid creating duplicate variants like `final`, `final2`, or `new`.

## Testing Guidelines
Quality control here is manual. After changes, verify:

- chapter numbering and headings remain consistent
- links between draft, export, and source files are still accurate
- tabular research files open correctly and preserve encoding

If you add derived outputs, note the source file and generation method in the same directory.

## Commit & Pull Request Guidelines
Git history is not available in this workspace, so no repository-specific commit convention could be inferred. Use short imperative commit messages, for example: `Update chapter 2 literature review sources`. Keep each commit scoped to one chapter or dataset change. Pull requests should include a short summary, affected paths, and screenshots only when layout-sensitive HTML output changed.

## Document Handling Tips
Do not overwrite raw research exports. Keep original source files intact and create edited derivatives with chapter-specific names. Prefer updating existing manuscript files over creating parallel copies.
Before each substantive writing pass on the main manuscript, create a timestamped copy of the file at the moment writing starts. Use the date and time in the filename so each writing version is recoverable and ordered chronologically.
When adding literature to the manuscript, always uniformize citation style within the edited section and, when feasible, across adjacent sections. Do not mix title-only references with author-year citations in running text when the source metadata is available.
Whenever a new citation is added to the manuscript, add the corresponding full bibliographic entry to the bibliography at the end of the document using APA 7 format.

## Research Workflow
When using Elicit or similar literature tools, work sequentially and keep continuity between related sections instead of researching isolated fragments with no shared framing. For each substantial section, use both targeted searches and broader reports when useful, and treat the suggested bibliography as a primary research output rather than relying only on summaries. If the intended scope of a research task is ambiguous, confirm it before proceeding instead of assuming the focus.
Download completed Elicit reports and organize them into project folders instead of leaving them only in the web interface. Keep report outputs grouped in a predictable directory structure so that the report file, exported assets, and related notes remain traceable and reusable during writing.
Use the folder structure `sources/elicit/<chapter>/<subsection>/`. Inside each subsection folder, keep `queries.md`, `searches/`, `reports/`, and section-specific working notes together. Inside each individual report folder, store the report metadata, downloaded assets, working notes, and the exact query together.
Create a short notes file for each report covering the query objective, why it matters for the target section, the most useful findings, key limitations, and the most relevant bibliography.
Treat `search` as exploratory mapping and `report` as deeper synthesis. Use both deliberately rather than interchangeably.
Do not move claims from Elicit outputs into the manuscript without checking the underlying primary sources when those claims are used as factual support.
Prioritize high-value sources such as systematic reviews, meta-analyses, guidelines, validation studies, and papers directly related to prosthetics, orthotics, parametrization, and decision support.
Clearly distinguish literature evidence from project-specific interpretation or inference in notes and draft writing.
Link every Elicit search or report to a specific manuscript section so research outputs do not become detached from writing goals.
Avoid duplicating reports when an existing report already covers the same question closely enough; complement it with targeted searches instead.
Integrate research incrementally. After each meaningful search or report cycle, update the relevant draft notes or manuscript section instead of stockpiling unread outputs.
Treat Elicit report workflows as a scarce resource. Use targeted searches first to refine scope, reduce noise, and identify likely anchor papers before launching a report. Do not create a new report until the expected value is clear and the question is sufficiently focused to justify consuming a workflow.
