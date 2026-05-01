# Repository Guidelines

## Project Structure & Module Organization
This repository is organized as a thesis workspace rather than an application codebase. Keep the consolidated manuscript in the root as `Projecto completo.md`. Chapter drafts live in `chapters/text/`, HTML exports in `chapters/html/`, general supporting `.docx` files in `sources/docx/`, Elicit research workflows in `sources/elicit/`, and the local library of papers and reference material in `material/`. Keep new material close to the chapter or topic it supports and avoid mixing raw library content with polished manuscript files.

## Build, Test, and Development Commands
No build system, package manager, or automated test runner was detected in this workspace. Use lightweight validation commands when editing:

```bash
rg --files .
find chapters sources material -maxdepth 2 -type f
```

Use these to confirm file placement and naming. For Markdown or HTML edits, preview locally in your editor before committing. When exporting revised chapter assets, keep the editable source alongside the exported format. When adding or reorganizing papers, verify they land under `material/` in the appropriate topical folder rather than under manuscript or export directories.

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
Do not overwrite raw research exports or original library files in `material/`. Keep original source files intact and create edited derivatives with chapter-specific names. Prefer updating existing manuscript files over creating parallel copies.
Before each substantive writing pass on the main manuscript, create a timestamped copy of the file at the moment writing starts. Use the date and time in the filename so each writing version is recoverable and ordered chronologically.
Maintain a root `CHANGELOG.md` and update it after every repository change, with a short dated note describing what changed. Add new changelog entries at the top of the file so the newest version appears first.
Keep an explicit version line at the top of `Projecto completo.md` and bump that version after every manuscript change. Reflect the same manuscript version bump in `CHANGELOG.md`.
All text written or revised in `Projecto completo.md` must use European Portuguese (`português de Portugal`) consistently.
When adding literature to the manuscript, always uniformize citation style within the edited section and, when feasible, across adjacent sections. Do not mix title-only references with author-year citations in running text when the source metadata is available.
Whenever a new citation is added to the manuscript, add the corresponding full bibliographic entry to the bibliography at the end of the document using APA 7 format.

## Research Workflow
When using Elicit or similar literature tools, work sequentially and keep continuity between related sections instead of researching isolated fragments with no shared framing. For each substantial section, use both targeted searches and broader reports when useful, and treat the suggested bibliography as a primary research output rather than relying only on summaries. If the intended scope of a research task is ambiguous, confirm it before proceeding instead of assuming the focus.
Download completed Elicit reports and organize them into project folders instead of leaving them only in the web interface. Keep report outputs grouped in a predictable directory structure so that the report file, exported assets, and related notes remain traceable and reusable during writing.
Use the folder structure `sources/elicit/<chapter>/<subsection>/`. Inside each subsection folder, keep `queries.md`, `searches/`, `reports/`, and section-specific working notes together. Inside each individual report folder, store the report metadata, downloaded assets, working notes, and the exact query together.
For Elicit agent sessions, use `sources/elicit/agent-sessions/<chapter>/<subsection>/<session-slug>/` and map each session to a specific manuscript section before saving anything locally. Treat the local session folder as the authoritative record of that session rather than leaving reusable material only in the Elicit web interface.
Inside each agent-session folder, keep the session identity explicit with section-numbered filenames such as `<section>_<session-slug>_session_title.md` and `<section>_<session-slug>_prose.md`.
When possible, paste the generated Elicit prose into the local prose file rather than relying only on exported artifacts, because the pasted prose often preserves the synthesis text and footnote markers more reliably.
Add the source list for the prose in structured form, preferably as `<section>_<session-slug>_sources.csv`, and also keep `APA Sources.txt` when Elicit provides it.
When available, keep generated artifacts, chat or transcript exports, and APA/citation files together in the same session folder. Prefer `DOCX`, `PDF`, `CSV`, and `XLSX` exports and rename them with the same section-and-slug prefix to avoid filename collisions across sessions.
If an Elicit agent-session export omits inline citations or bibliography but those are visible in the browser DOM, save the copied HTML snippet locally and keep it with the session files so citation anchors can be extracted into the local session folder.
If the Elicit UI allows copying the generated prose with Markdown footnotes and footnote definitions, prefer saving that prose locally as `.md` or `.txt`, since it preserves both the readable synthesis and the citation-to-bibliography mapping more directly than the plain exported artifact.
After adding or updating session files locally, run the extraction workflow so the session folder also contains extracted readable text, a manifest, local notes, and recovered citation/bibliography outputs. Preserve prose, citations, bibliography, tables, and transcripts before doing any later synthesis into the manuscript.
If a session is relevant to multiple nearby subsections, place it in the best-fit primary subsection and note the broader relevance in the local session `README.md` instead of duplicating the same session across multiple folders.
Create a short notes file for each report covering the query objective, why it matters for the target section, the most useful findings, key limitations, and the most relevant bibliography.
Treat `search` as exploratory mapping and `report` as deeper synthesis. Use both deliberately rather than interchangeably.
When a section is likely to require a more rigorous literature workflow, use the sequence `report -> systematic review` rather than starting directly with a systematic review. Use the report to refine scope, terminology, and likely anchor papers first, then carry that framing into the systematic review protocol.
Do not move claims from Elicit outputs into the manuscript without checking the underlying primary sources when those claims are used as factual support.
Prioritize high-value sources such as systematic reviews, meta-analyses, guidelines, validation studies, and papers directly related to prosthetics, orthotics, parametrization, and decision support.
Clearly distinguish literature evidence from project-specific interpretation or inference in notes and draft writing.
Link every Elicit search or report to a specific manuscript section so research outputs do not become detached from writing goals.
Avoid duplicating reports when an existing report already covers the same question closely enough; complement it with targeted searches instead.
Integrate research incrementally. After each meaningful search or report cycle, update the relevant draft notes or manuscript section instead of stockpiling unread outputs.
Treat Elicit report workflows as a scarce resource. Use targeted searches first to refine scope, reduce noise, and identify likely anchor papers before launching a report. Do not create a new report until the expected value is clear and the question is sufficiently focused to justify consuming a workflow.
When preparing a systematic review, create and maintain a local protocol pack that records the research question, eligibility criteria, search strategy, screening rules, extraction fields, and PRISMA-style decision log, even if the review itself is carried out in the Elicit web interface.
Treat the local systematic review folder as the authoritative operational record for the review. Mirror protocol decisions, UI workflow choices, exports, and status updates there so the review remains reproducible outside the Elicit interface.
