# Changelog

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
