# Agent Sessions

Store extracted Elicit agent-session material here using:

`material/investigacao/elicit/agent-sessions/<chapter>/<subsection>/<session-slug>/`

Each session folder should contain:

- `raw/` with the original exported files
- `extracted/` with readable text extracted from `docx`, `pdf`, `txt`, or `md`
- `bibliography_apa.txt` when an APA sources export is available
- `inline_citations.txt` when citation anchors were extracted from pasted Elicit HTML
- `manifest.json` with file inventory and basic detection metadata
- `README.md` summarizing title, chapter, subsection, extracted artifacts, and bibliography count

Use `tools/elicit/elicit_agent_session_ingest.py` to ingest local exports into this structure.

If Elicit only exposes inline citations in the browser UI, save the copied console HTML snippet as a local `.html` file and ingest it with the session files. The script will preserve readable text and extract the `data-citation-anchor` button labels into `inline_citations.txt`.
If Elicit lets you copy the generated prose with Markdown-style footnotes such as `[^1]` and footnote definitions at the end, prefer saving that as `.md` or `.txt`. The ingest script will extract both the inline footnote markers and the bibliography lines into the local session folder.
