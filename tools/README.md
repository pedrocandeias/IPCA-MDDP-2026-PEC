# tools/ — índice das ferramentas

Todos os *scripts* do repositório vivem aqui. Nada executável fica em
`material/`, `docs/` ou na raiz, com uma única excepção deliberada:
`deploy.sh`, o ponto de entrada de topo.

Os comandos assumem que são corridos **a partir da raiz do repositório**
(`/home/pec/dev/mestrado`), não de dentro de `tools/`. Todos os *scripts*
Python descobrem a raiz a partir da sua própria localização, pelo que não é
preciso mudar de directório.

```
tools/
├── <pontos de entrada>      # os comandos do dia-a-dia, ver abaixo
├── conversao/               # formatos derivados (ODT, ligação de citações)
├── bibliografia/            # PDFs referenciados e ponte para o Mendeley
├── mendeley-tools/          # SUBMÓDULO — organizar e enriquecer a biblioteca
├── mendeley-downloader/     # SUBMÓDULO — descarregar a biblioteca (fork)
├── extraccao/               # extrair figuras, tabelas, comentários, dados
├── revisao/                 # revisão linguística e auditoria de citações
├── manutencao/              # versão, changelog, paginação, commits
├── pdfs/                    # organizar a colecção de PDFs e suplementos
├── elicit/                  # pesquisa bibliográfica via Elicit
├── revisoes/                # 96 scripts de revisão pontual (histórico)
└── hooks/                   # git hooks versionados
```

---

## Pontos de entrada (raiz de `tools/`)

Estes ficam na raiz porque são escritos à mão com frequência; os caminhos são
estáveis e estão na lista de permissões do Claude Code.

| Comando | O que faz |
|---|---|
| `./tools/backup_docx.sh [etiqueta]` | Cópia de segurança datada do DOCX canónico em `docs/versoes/backups/` e regeneração do PDF |
| `./tools/docx_to_pdf.sh` | Converte o DOCX canónico no PDF canónico (LibreOffice *headless*). Fonte de verdade da conversão |
| `./tools/editar_docx_libreoffice.sh [ficheiro.docx]` | Abre o DOCX no Writer preservando o estado do Mendeley Cite |
| `python3 tools/word_lo_bridge.py backup\|restore <docx>` | Os dois passos da ponte acima, à mão |
| `./tools/install_hooks.sh` | Instala os *hooks* versionados (`core.hooksPath` → `tools/hooks`) |
| `python3 tools/md_to_docx.py --help` | Markdown → DOCX simples |
| `python3 tools/docx_to_md.py --help` | DOCX → Markdown |

---

## `conversao/` — formatos derivados

| Script | O que faz |
|---|---|
| `md_to_odt.py` | Markdown → ODT, reaproveitando o analisador de `md_to_docx.py` |
| `odt_to_md.py` | ODT → Markdown |
| `link_citations_to_bibliography.py` | Liga cada citação do texto à sua entrada na bibliografia |

## `bibliografia/` — PDFs referenciados

| Script | O que faz |
|---|---|
| `consolidate_docx_referenced_pdfs.py` | Reúne os PDFs citados no DOCX e assinala os que faltam |
| `fetch_mendeley_referenced_pdfs.py` | Descarrega do Mendeley os PDFs em falta, emparelhando por DOI e título |

As cinco ferramentas Mendeley (organizador, enriquecedor, deduplicador,
sincronização de DOIs e normalizador de títulos) estão no submódulo
`mendeley-tools/` e têm guia próprio em `tools/mendeley-tools/README.md`.
Num clone novo:

```bash
git submodule update --init tools/mendeley-tools
```

Como são ferramentas independentes, os caminhos deste projecto passam-se por
opção (`--material`, `--md`) ou por variável de ambiente:

```bash
export MENDELEY_MATERIAL=/home/pec/dev/mestrado/material
export MENDELEY_MANUSCRIPT=/home/pec/dev/mestrado/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md
```

## `mendeley-downloader/` — descarregar a biblioteca (submódulo)

Aplicação web que autentica na conta Mendeley e descarrega os PDFs da
biblioteca. É um *fork* de
[`Davo00/mendeley-downloader`](https://github.com/Davo00/mendeley-downloader)
(Apache 2.0) em
[`pedrocandeias/mendeley-downloader`](https://github.com/pedrocandeias/mendeley-downloader),
com alterações próprias ao *script* principal, ao `Dockerfile` e ao *template*
da listagem.

```bash
git submodule update --init tools/mendeley-downloader
cd tools/mendeley-downloader
cp config.yml.example config.yml       # preencher clientId e clientSecret
python3 -m venv venv && ./venv/bin/pip install -r requirements-modern.txt
./venv/bin/python mendeley-downloader.py
```

As credenciais são obtidas em <https://dev.mendeley.com/myapps.html>.
`config.yml` **contém segredos e está no `.gitignore`** do submódulo — nunca o
versionar. O `venv/` também não é versionado; recria-se com o comando acima.

Complementa as `mendeley-tools`: o *downloader* traz os ficheiros, as
`mendeley-tools` tratam dos metadados.

## `extraccao/` — extrair conteúdo dos documentos

| Script | O que faz |
|---|---|
| `extract_figures_tables.py` | Percorre os PDFs de `material/` e escreve `material/figures_tables_index.md` (~2 min para ~370 PDFs) |
| `extract_suggested_assets.py` | Lê `figures_tables_suggestions.md` e extrai as figuras e tabelas dos artigos para `material/figuras-extraidas/` e `material/tabelas-extraidas/` |
| `extract_docx_comments.py` | Exporta os comentários do DOCX |
| `recover_docx_comments.py` | Recupera comentários de um DOCX danificado |
| `extract_print_and_dimensional_tables.py` | Extrai as tabelas de impressão e as dimensionais |
| `read_xlsx_cells.py` | Lê células de um XLSX (apoio à verificação de dados) |
| `generate_missing_pdfs_report.py` | Relatório dos textos integrais em falta, extraído directamente da bibliografia do DOCX |

## `revisao/` — revisão linguística e citações

| Script | O que faz |
|---|---|
| `audit_docx_languagetool.py` | Passa o DOCX pelo LanguageTool e produz o relatório de ocorrências |
| `audit_docx_bibliographic_completeness.py` | Audita controlos Mendeley, citações directas e bibliografia materializada no DOCX |
| `generate_languagetool_filtered_reports.py` | Filtra o relatório anterior por tipo de erro |
| `harper_lint.mjs` | Revisão com o Harper (Node) |
| `grammarly_api.py` | Revisão via API do Grammarly |
| `generate_citation_evidence_sheet.py` | Folha de prova por citação, para auditoria |
| `generate_citation_traceability_sheet.py` | Rastreabilidade citação ↔ bibliografia ↔ PDF |

## `manutencao/` — versão, changelog e paginação

| Script | O que faz |
|---|---|
| `version_manuscript.py` | Incrementa a linha `Versão do documento: X.Y.Z` no MD |
| `update_changelog.py` | Acrescenta entrada ao `CHANGELOG.md` (`--auto` compara com o remoto) |
| `commit_from_changelog.py` | Encena e faz *commit* usando a última entrada do changelog |
| `synchronise_docx_pagination.py` | Sincroniza a paginação estática dos índices a partir de um PDF provisório |
| `sync_annex_d_source.py` | Sincroniza a fonte do Anexo D |

Os três primeiros são orquestrados por `./deploy.sh` — ver a raiz do repositório.

## `pdfs/` — colecção de PDFs e suplementos

| Script | O que faz |
|---|---|
| `organize_toorganize.py` | Distribui os PDFs soltos pelas pastas temáticas de `material/` |
| `flag_titles.py` | Assinala nomes de ficheiro problemáticos (correr antes do organizador Mendeley) |
| `rename_pdfs.py` | Renomeia PDFs a partir dos metadados |
| `build_supplements_package.py` | Monta os pacotes de suplementos para entrega |
| `calcular_resultados_dimensionais_fisicos.py` | Calcula os resultados dimensionais das medições físicas |

## `elicit/` — pesquisa bibliográfica

| Script | O que faz |
|---|---|
| `elicit_sync.py` | Sincroniza os resultados do Elicit com as fontes dos capítulos |
| `elicit_download.py` | Descarrega os PDFs dos resultados |
| `elicit_fetch_missing.py` | Volta a tentar os que falharam |
| `elicit_api.py` | Camada de acesso à API (não se corre directamente) |
| `elicit_agent_session_ingest.py` | Importa uma sessão de agente do Elicit |

## `revisoes/` — 96 revisões pontuais (histórico)

Cada um destes *scripts* foi escrito para **uma** alteração concreta ao
manuscrito e já foi corrido. O sufixo numérico (`_045` … `_114`) corresponde à
ordem em que foram aplicados e as entradas do `CHANGELOG.md` descrevem o
resultado de cada um.

**Não voltar a correr.** Foram escritos contra uma versão específica do DOCX;
aplicá-los hoje duplicaria texto ou corromperia a numeração. Ficam
versionados como registo de como cada alteração foi feita — e como ponto de
partida quando for preciso escrever um novo do mesmo género.

Dois deles continuam a ser fluxo de trabalho vivo, documentados no README
da raiz, e por isso não têm sufixo numérico:

| Script | O que faz |
|---|---|
| `integrate_annexes_bc.py` | Integra os Anexos B e C no DOCX (impede inclusão dupla) |
| `apply_annex_local_indexes.py` | Move as entradas detalhadas dos anexos para índices próprios |

## `hooks/` — git hooks versionados

`pre-commit` regenera o PDF quando o DOCX canónico entra num *commit*.
Instalar uma vez por clone com `./tools/install_hooks.sh`. Não usar
`git commit --no-verify` quando o DOCX foi alterado.

---

## Convenções

- **Um *script* por alteração.** Uma correcção pontual ao manuscrito escreve-se
  como *script* novo em `revisoes/`, com o número seguinte, e não editando um
  antigo.
- **A raiz do repositório descobre-se pela localização do ficheiro**
  (`Path(__file__).resolve().parents[2]` dentro de uma subpasta). Nunca
  escrever caminhos absolutos.
- **Nada de executáveis fora de `tools/`**, com a excepção de `deploy.sh`.
- O submódulo `mendeley-tools/` não pode depender deste repositório: recebe os
  caminhos por opção ou variável de ambiente.
