# Changelog

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
