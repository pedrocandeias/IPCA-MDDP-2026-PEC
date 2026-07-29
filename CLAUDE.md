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
├── deploy.sh                 # único executável fora de tools/ (ponto de entrada)
├── tools/                    # TODOS os scripts — ver tools/README.md (índice)
│   ├── backup_docx.sh, docx_to_pdf.sh, editar_docx_libreoffice.sh,
│   │   word_lo_bridge.py, install_hooks.sh, md_to_docx.py, docx_to_md.py
│   │                         # pontos de entrada — ficam na raiz de tools/
│   ├── conversao/            # md_to_odt, odt_to_md, link_citations
│   ├── bibliografia/         # PDFs citados; ponte para o Mendeley
│   ├── extraccao/            # extract_figures_tables.py, comentários, tabelas
│   ├── revisao/              # LanguageTool, Harper, Grammarly, citações
│   ├── manutencao/           # version_manuscript, update_changelog, paginação
│   ├── pdfs/                 # organize_toorganize, flag_titles, rename_pdfs
│   ├── elicit/               # elicit_*.py
│   ├── revisoes/             # 95 revisões pontuais já aplicadas — NÃO recorrer
│   ├── hooks/                # pre-commit versionado
│   ├── mendeley-tools/       # SUBMÓDULO — ver abaixo
│   └── mendeley-downloader/  # SUBMÓDULO — fork de Davo00/mendeley-downloader
├── material/                 # colecção de papers e dados (sem scripts, sem docs)
│   ├── elicit_missing_papers.csv
│   ├── figures_tables_index.md        # auto-generated caption index (overwrite freely)
│   ├── figures_tables_suggestions.md  # curated placement suggestions per thesis section
│   └── <topic folders>/      # organised PDFs
```

### Onde colocar um script novo

- Nada de executáveis fora de `tools/` (excepção: `deploy.sh`).
- Uma correcção pontual ao manuscrito é um **script novo** em `tools/revisoes/`,
  com o número seguinte — nunca editar um antigo, que é registo histórico.
- Uma ferramenta reutilizável vai para a subpasta da sua finalidade; só entra na
  raiz de `tools/` se for para escrever à mão com frequência.
- Dentro de uma subpasta, a raiz do repositório é
  `Path(__file__).resolve().parents[2]`. Nunca escrever caminhos absolutos.
- Ao mover um script, verificar `deploy.sh`, `tools/hooks/pre-commit`,
  `.claude/settings.local.json` (permissões por caminho) e o README.

### Submódulo mendeley-tools

Os scripts Mendeley são ferramentas independentes, com repositório próprio
(`github.com/pedrocandeias/mendeley-tools`), consumidas aqui como submódulo em
`tools/mendeley-tools/`. Não são específicas deste manuscrito e não devem
passar a ser: os caminhos do projecto entram por `--material` e `--md`, ou
pelas variáveis `MENDELEY_MATERIAL` e `MENDELEY_MANUSCRIPT`.

Ao alterar um script `mendeley_*`:

1. Editar dentro de `tools/mendeley-tools/` e actualizar aí o `README.md` (guia
   de utilizador, em inglês e para leitores não técnicos) e o `CHANGELOG.md`
   (semver) — **não** o README da raiz nem `material/`.
2. Fazer *commit* e *push* no submódulo primeiro, depois registar o novo ponteiro
   no repositório do mestrado (`git add tools/mendeley-tools`).
3. Nada de caminhos escritos no código: nenhum script pode assumir que existe um
   manuscrito ou uma pasta `material` ao lado.

`tools/bibliografia/fetch_mendeley_referenced_pdfs.py` pertence ao mestrado mas importa
`mendeley_enrich` do submódulo, acrescentando-o ao `sys.path` (o hífen do nome
da pasta impede o *import* directo).

### Submódulo mendeley-downloader

`tools/mendeley-downloader/` é um *fork* de `Davo00/mendeley-downloader`
(Apache 2.0) em `pedrocandeias/mendeley-downloader`, com alterações próprias.
Ao alterar algo, fazer *commit* e *push* no *fork* e só depois registar o
ponteiro aqui. Duas regras:

- `config.yml` contém `clientId`/`clientSecret` e está no `.gitignore` do
  submódulo — **nunca** versionar nem imprimir o seu conteúdo.
- `venv/` não é versionado; recria-se a partir de `requirements-modern.txt`.

Se aparecer outra pasta de projecto na raiz, verificar antes de mover se é um
*gitlink* órfão: `git ls-tree HEAD <pasta>` a devolver modo `160000` sem
entrada correspondente em `.gitmodules` significa que um clone novo recebe uma
pasta vazia e que os *commits* locais existem apenas nesse disco.

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
cd /home/pec/dev/mestrado
python3 tools/extraccao/extract_figures_tables.py
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
| `tools/extraccao/extract_figures_tables.py` | The extraction script (edit to improve caption detection if needed) |

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
