# CLAUDE.md — Mestrado project

## Repository layout

```
/home/pec/dev/mestrado/
├── Projecto completo.md      # master project document (versioned)
├── versions/                 # timestamped snapshots of Projecto completo.md
├── material/                 # library management tooling & paper collection
│   ├── CHANGELOG.md          # tooling changelog (semver)
│   ├── elicit_missing_papers.csv
│   ├── organize_toorganize.py
│   └── <topic folders>/      # organised PDFs
```

## After every change

### 1 — Update CHANGELOG.md
File: `/home/pec/dev/mestrado/material/CHANGELOG.md`

- Add an entry under `## [Unreleased]` describing what changed.
- Use Keep-a-Changelog conventions: `### Added`, `### Changed`, `### Fixed`, `### Removed`.
- When releasing, replace `[Unreleased]` with `[X.Y.Z] — YYYY-MM-DD` and open a fresh `## [Unreleased]` section above it.
- Bump **patch** (0.0.x) for fixes and small tweaks; **minor** (0.x.0) for new features or scripts; **major** (x.0.0) for breaking changes.

### 2 — Bump version in Projecto completo.md
File: `/home/pec/dev/mestrado/Projecto completo.md`

- The first line is `**Versão do documento:** \`X.Y.Z\``. Increment it on every edit.
- Bump **patch** for wording/typo fixes; **minor** for new sections or substantial rewrites; **major** for structural reorganisation.

### 3 — Copy anthropometric CSVs to dados antropométricos
After generating or updating any anthropometric CSV in `/home/pec/dev/ai-parametric-prosthetic-hand-generator/data/`, copy it to:

```
/home/pec/dev/mestrado/material/antropometria/dados antropométricos/
```

Example:
```bash
cp /home/pec/dev/ai-parametric-prosthetic-hand-generator/data/multi_population_hand.csv \
   "/home/pec/dev/mestrado/material/antropometria/dados antropométricos/"
```
