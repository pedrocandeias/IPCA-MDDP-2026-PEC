# CLAUDE.md — Mestrado project

## Repository layout

```
/home/pec/dev/mestrado/
├── pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.{md,docx,pdf}
│                              # canonical manuscript and matching exports
├── docs/versoes/             # backups, dated exports and historical documents
├── material/                 # library management tooling & paper collection
│   ├── CHANGELOG.md          # tooling changelog (semver)
│   ├── elicit_missing_papers.csv
│   ├── organize_toorganize.py
│   ├── extract_figures_tables.py      # extracts figure/table captions from all PDFs
│   ├── figures_tables_index.md        # auto-generated caption index (overwrite freely)
│   ├── figures_tables_suggestions.md  # curated placement suggestions per thesis section
│   └── <topic folders>/      # organised PDFs
```

## After every change

### 1 — Update README.md
File: `/home/pec/dev/mestrado/README.md`

- Review and update the README after every repository change.
- Keep the documented manuscript version, date, project status, bibliography status, directory structure and working commands consistent with the repository's current state.
- When a change does not require a new section, confirm that the existing description and links remain accurate and update any affected status line or workflow note.
- Do not use the README as a detailed change log; keep the explanation concise and place the chronological detail in the root `CHANGELOG.md`.

### 2 — Update CHANGELOG.md
File: `/home/pec/dev/mestrado/CHANGELOG.md`

- Add a short dated entry at the top describing what changed.
- Keep manuscript-version details in the same entry when the canonical manuscript changes.

### 3 — Bump version in the canonical manuscript
File: `/home/pec/dev/mestrado/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md`

- The version line is `Versão do documento: X.Y.Z`. Increment it on every manuscript edit.
- Bump **patch** for wording/typo fixes; **minor** for new sections or substantial rewrites; **major** for structural reorganisation.

### 4 — Regenerate figures/tables index and suggestions (when PDFs change)

Run these two steps whenever new PDFs are added to `material/` or when the thesis structure changes significantly:

**Step 1 — Rebuild the index** (re-extracts captions from all PDFs):
```bash
cd /home/pec/dev/mestrado/material
python3 extract_figures_tables.py
```
Output: `material/figures_tables_index.md` (overwritten in place). Takes ~2 min for ~370 PDFs.

**Step 2 — Rebuild the suggestions** (re-matches index to thesis chapters):

Ask Claude:
> "Read `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md` and match figures and tables from `material/figures_tables_index.md`. Regenerate `material/figures_tables_suggestions.md` with the proposed figure and placement. Do it one chapter/subchapter at a time."

Claude will spawn an agent that reads both files in chunks and writes the updated `figures_tables_suggestions.md`.

**When to re-run:**
- After adding a batch of new PDFs to any topic folder
- After a major restructure or new chapter in the canonical revised manuscript
- After significant edits to existing sections change what figures are appropriate

**Files produced:**
| File | Purpose |
|------|---------|
| `material/figures_tables_index.md` | Raw index of all captions (auto-generated, overwrite freely) |
| `material/figures_tables_suggestions.md` | Curated placement suggestions per thesis section (review before use) |
| `tools/extract_figures_tables.py` | The extraction script (edit to improve caption detection if needed) |

### 5 — Copy anthropometric CSVs to dados antropométricos
After generating or updating any anthropometric CSV in `/home/pec/dev/ai-parametric-prosthetic-hand-generator/data/`, copy it to:

```
/home/pec/dev/mestrado/material/antropometria/dados antropométricos/
```

Example:
```bash
cp /home/pec/dev/ai-parametric-prosthetic-hand-generator/data/multi_population_hand.csv \
   "/home/pec/dev/mestrado/material/antropometria/dados antropométricos/"
```
