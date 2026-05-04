# Changelog

## 2026-05-04

- Added `scripts/md_to_docx.py`, a dependency-free local CLI that exports Markdown files to `.docx` with support for headings, paragraphs, bullet lists, block quotes, code blocks, and simple pipe tables.
- Updated `README.md` with usage notes for the new Markdown-to-DOCX exporter.

## 2026-05-04

- Added `scripts/grammarly_api.py`, a local CLI wrapper for Grammarly's official `AI Detection API (Beta)` and `Plagiarism Detection API (Beta)` using OAuth 2.0 client credentials, score request creation, file upload, polling, and result retrieval.
- Added [docs/grammarly-api.md](/home/pec/dev/mestrado/docs/grammarly-api.md:1) with setup requirements, environment variables, usage examples, and current API constraints from Grammarly's developer documentation.

## 0.2.41 - 2026-05-04

- Created a new timestamped backup of `Projecto completo.md` before normalizing GitHub image paths.
- Rewrote the manuscript image links from `figuras/...` to `./figuras/...` to improve GitHub Markdown rendering consistency.
- Bumped the manuscript version to `0.2.41`.

## 2026-05-04

- Updated `material/extract_suggested_assets.py` so extracted figure and table assets are now written to the root-level `figuras/` and `tabelas/` directories instead of the old `material/` subfolders.

## 0.2.40 - 2026-05-04

- Created a new timestamped backup of `Projecto completo.md` before updating asset paths.
- Moved the extracted asset folders from `material/figuras` and `material/tabelas` to the repository root as `figuras/` and `tabelas/`.
- Updated the image paths in `Projecto completo.md` to point to the new root-level `figuras/` directory and bumped the manuscript version to `0.2.40`.

## 0.2.39 - 2026-05-04

- Created a new timestamped backup of `Projecto completo.md` before revising the newly added figure and table captions.
- Replaced the abbreviated source notes under the recently inserted figures and tables with explicit APA 7 reference lines.
- Corrected several caption source attributions to match the original documents used for extraction, including the figures from the Manero et al., Yu et al., and Menaka et al. sources.
- Added the newly cited source entries to the bibliography at the end of `Projecto completo.md` and bumped the manuscript version to `0.2.39`.

## 0.2.38 - 2026-05-04

- Created a new timestamped backup of `Projecto completo.md` before integrating selected figures and tables from `material/figures_tables_suggestions.md`.
- Reviewed the extracted assets in `material/figuras/` and `material/tabelas/` and integrated only the items with the strongest direct fit to the manuscript argument.
- Added new figure and table integrations to sections `2.1`, `2.2`, `2.3`, `2.4`, `2.5`, `2.6`, `2.7`, `3.4`, and `4.2`, including explicit captions and short connective prose in European Portuguese.
- Bumped the manuscript version to `0.2.38`.

## 2026-05-03

- Reconciled `projecto_completo_bibliografia/pdfs_em_falta.md` against the PDFs now present in `material/` and cleared the remaining unresolved entries after confirming local matches for `DiaFit`, `Meta-design`, `Satisfying heterogeneous user needs via innovation toolkits`, `Independent tailoring of dose and drug release via a modularized product design concept for mass customization`, `A digital twin enabled wearable device for customized healthcare`, and `Designerly ways of knowing`.
- Corrected `projecto_completo_bibliografia/pdfs_em_falta.md` to remove `Design Council (2020). Framework for innovation` from the missing-PDF list, since that reference is a webpage/image resource rather than a PDF-tracked document.
- Reworked `README.md` to reflect the current repository structure, the local Elicit workflow, the bibliography cache, the utility scripts stored in `material/`, and the newly added `mendeley-downloader/`, reusing the guidance from `material/README.md`.
- Updated `origin` to the repository's new GitHub location, switched this clone back to `main`, set `origin/HEAD` to `main`, removed the remote branch `MDDP---IPCA-2026` after confirming that `main` already contained it, and deleted the local branch `MDDP---IPCA-2026`.
- Located and downloaded local PDFs for `Akasaka et al. (2022)`, `Colombo et al. (2015)`, `Machado et al. (2019)`, `von Hippel & Katz (2002)`, and `Seregni et al. (2021)` into `projecto_completo_bibliografia/`.
- Copied those five PDFs into the most appropriate thematic subfolders under `material/` to keep the local library aligned with the manuscript bibliography cache.
- Attempted to download `Govender et al. (2020)` but the available endpoints returned HTML instead of a valid PDF; removed the invalid file.
- Updated `projecto_completo_bibliografia/pdfs_em_falta.md` to reduce the unresolved list from 11 items to 6.

## 2026-05-02

- Consolidated the bibliography-missing-PDF tracking into `projecto_completo_bibliografia/pdfs_em_falta.md` and removed the duplicate `projecto_completo_bibliografia/unmatched_references.txt`.
- Updated `AGENTS.md` to require refreshing `projecto_completo_bibliografia/pdfs_em_falta.md` whenever citations or bibliography entries are added or changed in `Projecto completo.md`.

## 0.2.32 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before a directed bibliographic revision of sections `7.1` and `7.2`.
- Strengthened the bibliographic alignment of `7.1` and `7.2` with the locally saved chapter 7 notes, without changing the general argument of either section.
- Added `Colombo et al. (2015)` to support the discussion of 3D visualisation and natural interaction in `7.1`.
- Reinforced `7.2` with more explicit framing of direct upper-limb evidence versus transferable adjacent evidence, and added bibliographic support where appropriate.
- Added bibliography entries for `Colombo et al. (2015)` and `Oldfrey et al. (2024)`.
- Bumped the manuscript version to `0.2.32`.

## 0.2.31 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.5`.
- Reworked section `2.5` in European Portuguese as a clearer introductory framing of artificial intelligence for non-specialist readers, restructuring the section around definition, basic functioning, relevant forms of AI, integration across the design process, and the role of human supervision.
- Consolidated the section's argument using the locally saved research notes while keeping the manuscript free of explicit references to Elicit.
- Bumped the manuscript version to `0.2.31`.

## 2026-05-02

- Updated `AGENTS.md` to clarify the Elicit writing rule: the manuscript must not mention Elicit explicitly, but locally saved Elicit notes and syntheses may be used as drafting support so long as the final prose is written as regular academic text grounded in cited literature.
- Downloaded Elicit report `5a13094d-fe10-4caa-a182-6db2611bdf48` for section `2.5` into `sources/elicit/capitulo-2/2.5/reports/5a13094d-fe10-4caa-a182-6db2611bdf48/`.
- Added local working files `report.md`, `notes.md`, and `query.md` for the report, keeping the full report body in Markdown alongside `report.json`, `report.pdf`, and `report.docx`.

## 0.2.30 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising the transition between sections `4.2` and `4.3`.
- Refined the closing of section `4.2` and the opening of section `4.3` to make the passage from anthropometric data organization to OpenSCAD-based parametric modeling more explicit and fluent.
- Bumped the manuscript version to `0.2.30`.

## 0.2.29 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before integrating a new subsection into section `4.2`.
- Rewrote and integrated the contents of `data_extraction_explained.md` into section `4.2`, adding a new subsection on the collection, normalization, and use of anthropometric data in the parametric model.
- Updated earlier manuscript passages to align the description of the local anthropometric datasets with the current consolidated workflow and corrected the local path to `material/antropometria/dados antropométricos/`.
- Added the APA 7 bibliography entry for Gordon et al. (1989) and copied the corresponding local PDF into `project_completo_bibliografia/`.
- Bumped the manuscript version to `0.2.29`.

## 0.2.28 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before replacing the anglicized label `clinician-dominant`.
- Replaced `clinician-dominant` with `predomínio clínico` in section `7.2`, improving consistency with European Portuguese academic phrasing.
- Bumped the manuscript version to `0.2.28`.

## 0.2.27 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before replacing the expression `painéis e controlos`.
- Replaced `painéis e controlos` with `módulos de interação` in section `7.1`, improving lexical consistency in European Portuguese.
- Bumped the manuscript version to `0.2.27`.

## 0.2.26 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before a second pass of stylistic cleanup on repeated words within nearby sentences and paragraphs.
- Refined selected passages in sections `7.2` and `7.3`, reducing repeated uses of words such as `experiência`, `beneficia`, `processo`, and related terms through lighter reformulation while preserving the argument.
- Bumped the manuscript version to `0.2.26`.

## 0.2.25 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising repeated words across consecutive sentences.
- Revised selected passages in European Portuguese to reduce immediate lexical repetition in the manuscript body, replacing repeated nouns with simpler and more natural alternatives such as `ferramentas`, `pessoa`, `uso`, `adaptação`, `variáveis`, and equivalent reformulations.
- Bumped the manuscript version to `0.2.25`.

## 0.2.24 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising English-influenced uses of `reportado/reportar`.
- Revised the manuscript wording in European Portuguese, replacing `reportado/reportar` with more natural academic alternatives such as `indicado`, `assinalado`, `identificado`, `descrito`, `registado`, and `assinaladas`, depending on context.
- Bumped the manuscript version to `0.2.24`.

## 0.2.23 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before removing explicit references to Elicit reports from sections `7.2` and `7.3`.
- Replaced mentions of `Elicit` and `report` in the manuscript body with neutral references to the reviewed literature, to keep the academic argument grounded only in citeable literature.
- Bumped the manuscript version to `0.2.23`.

## 0.2.22 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `7.3`.
- Revised section `7.3` in European Portuguese, strengthening the analysis of the platform as a mediator of the design process through permissions, visibility control, constraint-setting, algorithmic starting points, and redistributed agency.
- Reused and consolidated the Elicit-derived bridge from section `7.2` to `7.3`, and bumped the manuscript version to `0.2.22`.

## 0.2.21 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `7.2`.
- Revised section `7.2` in European Portuguese, strengthening the distinction between professional and end-user experience, clarifying domain-specific distributions of agency, and aligning the discussion with the Elicit synthesis on asymmetric collaboration and mediated participation.
- Reused and consolidated the Elicit-derived literature framing for section `7.2`, and bumped the manuscript version to `0.2.21`.

## 2026-05-02

- Created `sources/elicit/capitulo-7/7.2/` with `queries.md`, `notes.md`, and local `searches/` and `reports/` placeholders to support the Elicit workflow for section `7.2`.
- Updated `sources/elicit/capitulo-7/7.2/notes.md` with consolidated Elicit findings on direct versus transferable evidence, the main literature gaps, and writing implications for section `7.2`.
- Downloaded Elicit report `5aeb15f6-71b8-4ac4-8fe1-912a29d46898` into `sources/elicit/capitulo-7/7.2/reports/5aeb15f6-71b8-4ac4-8fe1-912a29d46898/` and aligned file naming with the existing `sources/elicit` pattern, keeping `report.docx`, `report.json`, `report.pdf`, and `notes.md` for local working notes and pasted Elicit chat answers.
- Integrated the Elicit chat answers from report `5aeb15f6-71b8-4ac4-8fe1-912a29d46898` into the local synthesis for `sources/elicit/capitulo-7/7.2/notes.md`, sharpening the role distinction between socket design, control customization, aesthetic customization, and the bridge from section `7.2` to `7.3`.

## 0.2.19 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `7.1`.
- Revised section `7.1` in European Portuguese, strengthening the discussion of interaction strategy, task-oriented interface structure, controlled exposure of the parametric space, and the methodological role of UI/UX mediation.
- Reused existing in-text citations for section `7.1`, and bumped the manuscript version to `0.2.19`.

## 0.2.18 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising Chapter `6`.
- Revised sections `6.1` to `6.3` in European Portuguese, clarifying the assistive role of AI in the proposed system, its relation to parametric modeling, and its technical and ethical validation limits.
- Reused and consolidated existing in-text citations for Chapter `6`, and bumped the manuscript version to `0.2.18`.

## 0.2.16 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `5.5`.
- Revised section `5.5` in European Portuguese, strengthening the discussion of parameter formalization, practical version management through saved configurations, and the platform's real scalability constraints.
- Added in-text citations to section `5.5` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.16`.

## 0.2.15 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `5.4`.
- Revised section `5.4` in European Portuguese, reorganizing the platform discussion around its functional modules and the interaction flow between model selection, parameter editing, visualization, AI support, configuration management, and administration.
- Added in-text citations to section `5.4` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.15`.

## 0.2.14 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `5.3`.
- Revised section `5.3` in European Portuguese, clarifying the OpenSCAD-via-WebAssembly integration flow, its methodological implications, and its technical tradeoffs in browser-based local rendering.
- Added in-text citations to section `5.3` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.14`.

## 0.2.13 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `5.2`.
- Revised section `5.2` in European Portuguese, consolidating the layered system architecture around client-server separation, persistence, local rendering, and security responsibilities.
- Added in-text citations to section `5.2` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.13`.

## 0.2.12 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `5.1`.
- Revised section `5.1` in European Portuguese, strengthening the conceptual framing of the web platform as a sociotechnical mediation layer and clarifying the rationale for differentiated user roles.
- Added in-text citations to section `5.1` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.12`.

## 0.2.11 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `4.4`.
- Revised section `4.4` in European Portuguese, cleaning the heading markup and consolidating the discussion around iteration, parametric refinement, modularization, robustness testing, and fabrication constraints.
- Added in-text citations to section `4.4` using bibliography entries already present in the manuscript, and bumped the manuscript version to `0.2.11`.

## 0.2.10 - 2026-05-02

- Added `projecto_completo_bibliografia/pdfs_em_falta.md` to list the bibliography entries that still do not have an automatically matched local PDF.

## 0.2.9 - 2026-05-02

- Created `projecto_completo_bibliografia/` and copied the locally available PDF files matched against the current bibliography of `Projecto completo.md`.
- Added `projecto_completo_bibliografia/README.md`, `copied_matches.json`, and `unmatched_references.txt` to document automatic matches and references without a local PDF match.

## 0.2.8 - 2026-05-02

- Updated `AGENTS.md` to require copying available local PDF files for sources cited in `Projecto completo.md` into `project_completo_bibliografia/` after bibliography additions.

## 0.2.7 - 2026-05-02

- Created a new timestamped backup of `Projecto completo.md` before revising section `4.3`.
- Rewrote section `4.3` in European Portuguese, restoring the section boundary, removing misplaced draft residue, and consolidating the OpenSCAD discussion around technical structure, parameter logic, fabrication constraints, and a focused critical analysis.
- Added in-text citations and the corresponding APA 7 bibliography entries for the new `4.3` script-based parametric modeling references, and bumped the manuscript version to `0.2.7`.

## 0.2.6 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `4.2`.
- Revised section `4.2` in European Portuguese, tightening its scope around anthropometric parameter selection, minimum measurement sets, collection methods, dataset normalization, and mapping into the model structure.
- Added in-text citations and the corresponding APA 7 bibliography entries for the new `4.2` anthropometry and parametric-workflow references, and bumped the manuscript version to `0.2.6`.

## 0.2.5 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `4.1`.
- Revised section `4.1` in European Portuguese, replacing provisional references with a literature-based framing of the prosthetic design problem, requirement categories, user-need translation, and early constraint formalization.
- Added in-text citations and the corresponding APA 7 bibliography entries for the new `4.1` literature references, and bumped the manuscript version to `0.2.5`.

## 0.2.4 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising Chapter 3.
- Revised sections `3.1` to `3.5` in European Portuguese, strengthening the methodological framing of RTD, the investigative role of industrial design, the relation to the Double Diamond structure, and the interpretation of evaluation criteria and limitations.
- Added in-text citations and the corresponding APA 7 bibliography entries for the Chapter 3 methodology references, and bumped the manuscript version to `0.2.4`.

## 0.2.3 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before refining the anthropometric dataset summary table presentation.
- Reformatted the `2.4` dataset summary as an academic-style table with an explicit caption and source note in European Portuguese.
- Bumped the manuscript version to `0.2.3`.

## 0.2.2 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before adding the anthropometric dataset summary table.
- Expanded section `2.4` in European Portuguese with a summary table describing the composition of `material/antropometria/Dados antopométricos/multi_population_hand.csv` by country, study, sample, measurement coverage, and row count.
- Refined the methodological description in section `3.4` to clarify which metadata dimensions are preserved in the consolidated anthropometric dataset, and bumped the manuscript version to `0.2.2`.

## 0.2.1 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before adding the anthropometric dataset references.
- Revised sections `2.4`, `3.3`, and `3.4` in European Portuguese to document the local hand anthropometry dataset in `material/antropometria/Dados antopométricos/multi_population_hand.csv` and its methodological role in the project.
- Added in-text citations and the corresponding APA 7 bibliography entries for the five source papers used to build the consolidated anthropometric table, and bumped the manuscript version to `0.2.1`.

## 0.1.10 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.7`.
- Revised section `2.7` in European Portuguese, grounding the critical synthesis in review literature on evidence quality, personalization, control, access, and user involvement.
- Added in-text citations and the corresponding bibliography entries for the new `2.7` literature references, and bumped the manuscript version to `0.1.10`.

## 0.1.9 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.6`.
- Revised section `2.6` in European Portuguese, strengthening the framing of configurable systems, meta-design, modularity, parametric personalization, remote participation, and healthcare/prosthetics applications.
- Added in-text citations and the corresponding bibliography entries for the new `2.6` literature references, and bumped the manuscript version to `0.1.9`.

## 0.1.8 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.5`.
- Revised section `2.5` in European Portuguese, clarifying AI roles in generative design, surrogate evaluation, adaptive optimization, human-AI collaboration, and explainability.
- Added in-text citations and the corresponding bibliography entries for the new `2.5` literature references, and bumped the manuscript version to `0.1.8`.

## 0.1.7 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.4`.
- Revised section `2.4` in European Portuguese, tightening the discussion of anthropometry, digital capture methods, interface measurement, and prosthetic fit.
- Added in-text citations and the corresponding bibliography entries for the new `2.4` literature references, and bumped the manuscript version to `0.1.7`.

## 0.1.6 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.3`.
- Added in-text citations to section `2.3` of `Projecto completo.md`, covering parametric variation, seed-design logic, DfAM integration, configurators, cost-performance tradeoffs, and educational implications.
- Added the corresponding bibliography entries for the new `2.3` literature references and bumped the manuscript version to `0.1.6`.

## 0.1.5 - 2026-05-01

- Updated `AGENTS.md` to require that new `CHANGELOG.md` entries are added at the top of the file so the newest version always appears first.

## 0.1.4 - 2026-05-01

- Reordered `CHANGELOG.md` so the newest version entries appear at the top of the file.

## 0.1.3 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before revising section `2.2`.
- Revised section `2.2` in European Portuguese, tightening the framing of industrial design, inclusive design, universal design, UCD/HCD, co-design, and healthcare implementation challenges.
- Added in-text citations and the corresponding bibliography entries for the new `2.2` literature references, and bumped the manuscript version to `0.1.3`.

## 0.1.2 - 2026-05-01

- Created a new timestamped backup of `Projecto completo.md` before the next writing pass.
- Added in-text citations to section `2.1` of `Projecto completo.md`, covering prosthesis definition, typologies, rehabilitation, abandonment, and regulatory framing.
- Added the corresponding bibliography entries for the new `2.1` citations and bumped the manuscript version to `0.1.2`.

## 0.1.0 - 2026-05-01

- Added document version tracking to `Projecto completo.md`.
- Added repository instructions to update `CHANGELOG.md` after every change and bump the manuscript version after every manuscript edit.
- Created the initial changelog entry for the versioning workflow.
- Gathered additional Elicit materials into `elicit_reports_systematic_reviews/`, including Chapter 2 local systematic review exports and the Chapter 4.3 completed report download.
- Added chapter-matched local metadata records for older Elicit review and systematic-review links whose downloadable assets are not exposed through the currently available API.
- Normalized Elicit filenames to include chapter and subsection prefixes, consolidated the duplicate Chapter 4 report placement into the canonical `4.3` folder, and labeled the broad Chapter 2 personalization review set as spanning `2.3-2.7`.
- Added chapter-matched folders and an index for the listed Elicit agent sessions under `sources/elicit/agent-sessions/` to support later ingestion of exported artifacts, chats, and bibliography.
- Added `session_title.md` files inside each created Elicit agent-session folder so the full original session name is visible locally without relying on the slug alone.
- Added support in the local Elicit agent-session ingest workflow for pasted HTML snippets from the browser console, so inline citation anchors can be extracted into `inline_citations.txt` alongside the session artifacts.
- Added support in the local Elicit agent-session ingest workflow for pasted prose with Markdown footnotes, allowing inline citation markers and bibliography lines to be extracted from `.md` or `.txt` session captures.
- Added a `prose.md` placeholder to each created Elicit agent-session folder so copied prose can be pasted directly into the correct chapter-matched location.
- Renamed agent-session helper files so their filenames also include the section number, reducing ambiguity when files are viewed outside their folder paths.
- Renamed agent-session files again so they include both the section number and the session slug, preventing filename collisions between different session folders that share the same section number.
- Extended the local agent-session extraction script with in-place extraction commands and ran it across `sources/elicit/agent-sessions/`, generating `extracted/` outputs, `manifest.json`, `README.md`, `bibliography_apa.txt`, and `inline_citations.txt` files for the current session folders.
- Updated `AGENTS.md` to require that all text written or revised in `Projecto completo.md` uses European Portuguese (`português de Portugal`) consistently.
- Expanded `AGENTS.md` with the full Elicit agent-session workflow, including section-mapped foldering, prose and source capture, export naming, local extraction, and cross-section handling guidance.
- Revised section `2.1` of `Projecto completo.md` in European Portuguese, strengthening the framing of upper-limb prostheses as medical devices, clarifying typologies, clinical considerations, abandonment factors, and the regulatory context while preserving the existing chapter structure.
