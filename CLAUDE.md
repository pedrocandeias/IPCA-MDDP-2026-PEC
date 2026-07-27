# CLAUDE.md — Mestrado project

## Fontes de verdade do manuscrito (desde 2026-07-22)

O manuscrito existe em três ficheiros com papéis distintos — usar sempre
"DOCX" ou "MD" quando a distinção importar, nunca apenas "manuscrito":

- **DOCX** (`…revisto.docx`) — **documento de trabalho e de entrega; fonte de
  verdade do conteúdo.** É editado no Word e gerido pelo Mendeley Cite
  (citações vivas, bibliografia num content control `MENDELEY_BIBLIOGRAPHY`
  regenerada a partir da biblioteca Mendeley na nuvem). Não editar o DOCX por
  script enquanto o autor o tiver aberto no Word; correcções bibliográficas
  fazem-se preferencialmente nos registos Mendeley + Refresh no Word.
- **MD** (`…revisto.md`) — **espelho versionado para auditoria, diffs e
  histórico.** Sincronizado a partir do DOCX por scripts dedicados em
  `tools/`. É aqui que vive a linha `Versão do documento: X.Y.Z` (bump a cada
  sincronização/edição, ver regras abaixo). As âncoras `<a id="ref-…">` da
  bibliografia devem ser preservadas.
- **PDF** (`…revisto.pdf`) — export para entrega, regenerado a partir do DOCX.

A numeração de figuras e tabelas é sequencial contínua (Figura 1…, Tabela 1…),
como no DOCX; os anexos usam numeração por letra (B.1, C.1, D.1…). Os números
nas legendas do DOCX são texto literal (sem campos SEQ) — o Word não renumera
automaticamente.

## Repository layout

```
/home/pec/dev/mestrado/
├── pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.{md,docx,pdf}
│                              # DOCX = fonte de verdade; MD = espelho; PDF = export
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
