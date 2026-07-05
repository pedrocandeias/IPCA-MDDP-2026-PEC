# Changelog

## 2026-07-05

- Converted the current root `projecto-completo.docx` into `docs/projecto-completo-0125-05072026-convertido-de-docx.md`, extracting its 19 embedded images into the matching `_media/` folder.
- Updated `tools/docx_to_md.py` so DOCX-to-Markdown exports preserve embedded images and external hyperlinks instead of dropping them during conversion.

## 2026-07-03

- Added `tabelas/tabelas_revisadas.md` as the editable source for a consolidated `tabelas.docx` covering Tables 2.1, 2.2, 4.1-4.7, and 8.1-8.3, and strengthened Table 4.2 with additional support from local PDFs on transradial sockets, parametric fingers, and body-powered hand parametrization.
- Added `tabelas/tabela_4_2_parametros_por_nivel_amputacao.md` and exported `tabelas.docx` with a revised credited version of Table 4.2, separating Romero et al.'s hand-amputation levels from Moreo's anthropometric parameter reduction.
- Created Portuguese `_pt.png` variants for Figures 2.3, 2.6, 2.7, 2.8, 3.1, and 4.1 under `figuras/`, preserving the original figure files and leaving `projecto-completo.docx` unchanged.
- Localized Figure 4.2 labels from English to European Portuguese in `figuras/ch4_customization_of_a_3d_printed_prost_figure8_p7.png`, replacing "Uniformly Scaled" with "Escala uniforme" and "Parametric Modeling" with "Modelação paramétrica".
- Created backups at `versions/figuras-backup-2026-07-03_14-33-29_before-figura-4-2-pt/` and `versions/projecto-completo-docx-2026-07-03_14-33-29-before-figura-4-2-pt.docx`, then refreshed `projecto-completo.docx` and added `docs/projecto-completo-1434-03072026-figura-4-2-pt.docx`.

## 2026-07-02

- Trimmed excessive white top margins from the 19 figures referenced in `projecto-completo.md`, preserving a small top margin and documenting the crop in `docs/figuras-recorte-margem-superior-2026-07-02.md`.
- Created figure backups in `versions/figuras-backup-2026-07-02_18-06-35_before-top-whitespace-trim/` and a pre-change DOCX backup at `versions/projecto-completo-docx-2026-07-02_18-06-35-before-top-whitespace-trim.docx`.
- Added a post-trim backup at `versions/projecto-completo-docx-2026-07-02_19-49-51-after-top-whitespace-trim.docx` before committing the corrected DOCX.
- Added `docs/projecto-completo-1807-02072026-recorte-margem-superior.docx` as the LibreOffice-validated initial trimmed DOCX and `docs/projecto-completo-1951-02072026-recorte-margem-superior-comentarios.docx` as the current timestamped copy matching the root `projecto-completo.docx`, preserving 19 embedded figures and 36 DOCX comments.

## 2026-07-01

- Added `tools/extract_docx_comments.py` to extract DOCX comments, classify likely action types, and map annotated paragraphs back to `projecto-completo.md` line numbers without modifying the manuscript.
- Restored DOCX comments from `docs/projecto-completo-151329-01072026.docx` into the root `projecto-completo.docx`, preserving the 19 embedded figures from the latest export and validating the result with LibreOffice.
- Added `docs/projecto-completo-1844-01072026-com-comentarios-libreoffice.docx` as the timestamped recovered DOCX for the initial 23 restored comments and kept a pre-restore backup at `versions/projecto-completo-docx-1823-01072026-before-comment-restore.docx`.
- Added `docs/projecto-completo-2304-01072026-com-comentarios-libreoffice.docx` as a timestamped copy of the current root `projecto-completo.docx`, preserving its 19 figures and 32 DOCX comments.
- Added `tools/recover_docx_comments.py` to recover DOCX comments after Markdown-based manuscript exports while preserving the target DOCX XML structure for LibreOffice compatibility.
- Bumped `projecto-completo.md` to version `0.4.5` and integrated 8 additional figures across Chapters 1, 3, 4, 5, 6, 7, and 8, bringing the manuscript to 19 referenced figures.
- Exported the updated manuscript to `docs/projecto-completo-1617-01072026.docx` and refreshed the root convenience copy `projecto-completo.docx`.
- Added bibliography entries and local bibliography PDFs for the new figure sources where needed, and updated `projecto_completo_bibliografia/pdfs_em_falta.md`.
- Embedded the 11 manuscript figures referenced in `projecto-completo.md` into `projecto-completo.docx`, created timestamped export `docs/projecto-completo-151329-01072026.docx`, and kept a pre-image DOCX backup in `versions/`.
- Backed up the current `figuras/` folder to `versions/figuras-backup-2026-07-01_10-13-33_before-visual-fixes/` before manual visual crop fixes.
- Corrected manually identified bad figure crops that contained page headers, article text, or incomplete fragments, including the living-lab process, digital fabrication workflow, biometric hand image, anthropometric hand dimensions, D3Frame, XAI/responsible AI, and motion-similarity chart figures.
- Regenerated `docs/figuras-contact-sheets-2026-06-30/` after the visual corrections and added `docs/figuras-correcoes-visuais-2026-07-01.md` documenting the corrected files.

## 2026-06-30

- Added docs/figuras-contact-sheets-2026-06-30/ with all-figure and per-chapter contact sheets for manual visual crop review.
- Backed up the current figure PNGs to `versions/figuras-backup-2026-06-30_before-recrops/` and regenerated all `125` extracted figure PNGs from their source PDFs using bottommost-caption matching, original-caption exclusion, and white margins.
- Corrected the final recrop pass to handle compact `Fig.N.` captions and bottommost caption selection, fixing the blank `figuras/ch4_parametric_3d_modeling_of_a_customi_figure7_p5.png` crop.
- Updated `docs/figuras-imagens-auditoria-2026-06-30.md` with the post-recorte validation and refreshed dimensions in `docs/figuras-auditoria-2026-06-30.md`.
- Added `docs/figuras-imagens-auditoria-2026-06-30.md` auditing PNG crop quality, original-caption presence, white margins, and edge/cut risk for all extracted figures.
- Updated `docs/figuras-auditoria-2026-06-30.md` to include the local source PDF filename for each extracted image.
- Added `docs/figuras-auditoria-2026-06-30.md` auditing the extracted figures against `projecto-completo.md`, including usage counts, duplicate groups, per-chapter status, and integration priorities.

## 0.4.4 - 2026-06-29

- Corrected the root convenience DOCX filename to `projecto-completo.docx` and updated the repository export instruction accordingly.
- Created timestamped backup `versions/projecto-completo-2026-06-29_22-03-07.md` before synchronising the updated AI validation and simulation notes.
- Updated `projecto-completo.md` with the UCD validation results, deterministic laterality correction, model-fit warning/provenance requirements, and universalisation notes for other paired limbs.
- Bumped the manuscript version to `0.4.4`.
- Exported `projecto-completo.md` version `0.4.4` to `docs/projecto-completo-2204-29062026.docx` using `tools/md_to_docx.py`.
- Refreshed root convenience copy `projecto-completo.docx` from the latest DOCX export.

## 0.4.3 - 2026-06-29

- Added an `AGENTS.md` shorthand rule defining `cpd` as `commit, push, deploy`.
- Added an `AGENTS.md` instruction requiring DOCX exports to be saved both as timestamped files under `docs/` and as root `projecto-completo.docx`.
- Created root convenience copy `projecto-completo.docx` from the latest DOCX export.
- Exported `projecto-completo.md` version `0.4.3` to `docs/projecto-completo-1724-29062026.docx` using `tools/md_to_docx.py`.
- Created timestamped backup `versions/projecto-completo-2026-06-29_08-42-08.md` before integrating the AI anthropometric validation document.
- Integrated `docs/ai_anthropometric_validation.md` across `projecto-completo.md`, distributing the methodology, platform grounding, AI prompt architecture, anthropometric validation, inter-model geometric validation, conclusions and future work.
- Bumped the manuscript version to `0.4.3`.

## 2026-06-16

- Added `material/antropometria/antropometria_criancas.md` summarizing local anthropometry sources with child and adolescent data, including direct studies, a cautious mixed-age source, and excluded adult/fetal sources.

## 2026-06-15

- Exported `projecto-completo.md` version 0.4.2 to `docs/projecto-completo-2016-15062026.docx` using `tools/md_to_docx.py`.

## 2026-06-13

- Created timestamped backup `versions/projecto-completo-103548-13062026.md` before structural manuscript corrections.
- Corrected manuscript structure in `projecto-completo.md`: Chapter 1 section numbering, heading hierarchy, table sequence, stale figure paths, and the stray image artefact in section 2.7.
- Bumped the manuscript version to `0.4.2`.
- Added `projecto_questoes.md` mapping the current `projecto-completo.md` version 0.4.1 against the six research questions/objectives, including coverage level, supporting sections, and remaining gaps.

## 0.4.1 - 2026-06-07

- Created a timestamped backup of `projecto-completo.md` before revising the AI and anthropometric validation discussion.
- Updated `projecto-completo.md` with the current AI-assisted anthropometric sizing pipeline, including live model-schema prompting, JSON parameter filtering, validation criteria, observed results, stochastic variation and handedness limitations.
- Expanded Chapter 8 with the evaluation synthesis for technical coherence, anthropometric plausibility and the limits of AI-assisted parameter suggestions.
- Bumped the manuscript version to `0.4.1`.

## 2026-06-06

- Added `projecto-completo-audit.md` with a reduced, non-destructive audit version of the manuscript focused on removing repeated context across chapters.
- Added `project-completo-audit-changes.md` comparing the original manuscript with the audit version, including reduction metrics, repeated-pattern findings, and chapter-level change notes.
- Revised the audit files to preserve the original duplicate bibliography IDs and review-note artefacts, while correcting internal citation targets instead of removing them.
- Validated `projecto-completo-audit.md` after the audit revision: duplicate bibliography IDs are intentionally preserved, review notes `[^1]` to `[^13]` are restored, and internal citation targets resolve without missing references.

## 2026-06-05

- Expanded `projecto-completo.md` with the platform model-integration discussion for Paraglider/Flexible Flyer and Cyborg Beast/Flexy Hand, added the anthropometric AI validation section, and bumped the manuscript version to 0.4.0.
- Updated deploy.sh to reuse an existing local changelog entry when it differs from the latest committed changelog section, generating an automatic entry only when the two match.
- Updated `projecto-completo.md` against `versions/projecto-completo-172559-05062026.md`, affecting: Bibliografia (4 line(s) added, 1 removed).
- Added the local anthropometric dataset as a final reference in the manuscript and bumped the manuscript version to 0.3.1.
- Expanded the manuscript's anthropometric data extraction methodology in section 4.2, moved the detailed operational discussion out of section 2.4, added the new cited data-source bibliography entries, copied the available Hu et al. (2007) PDF into the bibliography folder, updated pdfs_em_falta.md, and bumped the manuscript version to 0.3.0.
- Updated repository files: `projecto-completo-2236-04052026-1553-05052026.md`, `projecto-completo.md`.
- Updated `projecto-completo-2236-04052026-1553-05052026.md` against `versions/projecto-completo-2236-04052026-1553-05052026-2026-05-06_09-10-00.md`, affecting: Estruturação de dados; Fundamentos conceptuais: toolkits, meta-design e end-user development.; 6.1 Papel da IA no sistema proposto; Bibliografia (18 line(s) added, 15 removed).
- Updated deploy.sh and tools/update_changelog.py so ./deploy.sh can generate a changelog entry automatically from the manuscript diff.
- Added deploy.sh to run the manuscript snapshot, changelog update, and git commit workflow sequentially.
- Added tools/update_changelog.py to prepend dated entries to CHANGELOG.md.
- Added tools/commit_from_changelog.py to stage changes and create a git commit from the latest changelog section.
- Added `tools/version_manuscript.py` to create timestamped manuscript snapshots in `versions/` using the `projecto-completo-hhmmss-ddmmyyyy.md` naming pattern.

## 2026-05-20

- Brief text corrections and comments added.
- Added AI Parametric Prosthetic hand Generator to the repository in projects;


## 2026-05-05

- Corrected the AI-related citation placeholders in `projecto-completo-2236-04052026-1553-05052026.md`, added the APA entry for `Elbreki et al. (2022)`, and verified/collocated the supporting PDFs in `projecto_completo_bibliografia/`.
- Added `tools/link_citations_to_bibliography.py` and applied it to the default thesis Markdown file so inline citations now link to matching bibliography entries at the end of the document, including disambiguation for `Romero et al., 2025` to the `da Silveira Romero et al. (2025)` reference.
- Replaced the broken `material` gitlink with a normal tracked folder in the main repository so the directory can be browsed correctly on GitHub, while keeping local cache and lock files out of version control.
- Consolidated the repository tooling into a single top-level `tools/` folder, moving the former `scripts/` CLIs and the Python helpers that were previously scattered under `material/`.
- Updated the moved tools to resolve `REPO_ROOT` and `material/` paths correctly from their new location, and refreshed the main documentation to point to `tools/...` commands.
- Cleaned the default converted thesis file `projecto-completo-2236-04052026-1553-05052026.md` to restore structural Markdown hierarchy, replacing stray backslash separators with horizontal rules, normalizing chapters 5 to 9 and their subsection headings, fixing table blocks, and separating glued figure captions from their source lines.
- Fixed `scripts/odt_to_md.py` table emission so Markdown tables are now written as contiguous pipe-table blocks instead of being broken by blank lines between rows.
- Improved `scripts/odt_to_md.py` with ODT-specific reconstruction heuristics so converted Markdown now better restores chapter headings stored as plain paragraphs, splits headings that were glued to body text, normalizes literal Markdown image lines, and converts long backslash runs into horizontal rules.
- Improved ODT caption reconstruction so figure captions no longer keep `Fonte original` glued onto the previous sentence in the generated Markdown.
- Re-tested the ODT-to-Markdown flow against the thesis ODT export to reduce structural degradation in the generated `.md`.
- Updated one converted thesis Markdown copy to correct the `1.6 Estrutura da dissertação` paragraph from five to nine chapters.

## 2026-05-05

- Updated the Markdown/DOCX/ODT converters to accept an explicit output filepath via `--output`, while keeping `--output-dir` for timestamped destination-folder output.
- Extended the shared Markdown parser and the ODT conversion flow to support simple ordered lists, so numbered list structure now survives the `.md -> .odt -> .md` round-trip more cleanly.
- Replaced the initial LibreOffice-dependent ODT wrappers with pure-Python `scripts/md_to_odt.py` and `scripts/odt_to_md.py`, so Markdown and LibreOffice Writer (`.odt`) conversion now works without calling LibreOffice.
- Updated `README.md` to document the direct ODT workflow and ODT image extraction behavior.

## 2026-05-05

- Updated `scripts/harper_lint.mjs` to use `pt-PT` as the default locale for this repository and to skip linting by default with an explicit message, since Harper does not yet support European Portuguese.
- Added explicit `--locale` switching for supported English variants such as `en-GB` when Harper linting is desired.
- Updated `README.md` to document the new default locale behavior and the opt-in English locale workflow.

## 2026-05-05

- Added a local Harper integration via `scripts/harper_lint.mjs`, backed by `harper.js` in Node.js, for offline grammar and style linting of Markdown and plain-text files.
- Added a minimal `package.json` for the Harper dependency and updated `.gitignore` to exclude `node_modules/`.
- Updated `README.md` with installation and usage examples for the new Harper-based linter.

## 2026-05-04

- Fixed `scripts/md_to_docx.py` so Markdown images are now embedded into the generated `.docx` package instead of being emitted as literal text, including support for local image paths and `[imageN]` reference definitions backed by `data:image/...`.
- Fixed the exporter parsing of escaped underscore separator lines so they are written as horizontal rules instead of long literal backslash sequences in the `.docx`.

## 2026-05-04

- Added `scripts/docx_to_md.py`, a dependency-free local CLI that converts `.docx` files back to timestamped Markdown copies in `docs/`.
- Updated `README.md` with usage notes for the new DOCX-to-Markdown exporter.

## 2026-05-04

- Updated `scripts/md_to_docx.py` so each export now creates a timestamped `.docx` copy in `docs/` by default, using the filename pattern `nome-do-ficheiro-hhmm-ddmmyyyy.docx`.
- Updated the exporter usage notes in `README.md` to reflect the new default output location and naming convention.

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
