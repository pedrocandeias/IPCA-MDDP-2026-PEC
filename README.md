# Mestrado Thesis Workspace

Este repositório organiza a dissertação, os documentos derivados, a pesquisa bibliográfica, as figuras, as tabelas e as ferramentas locais usadas ao longo do projeto.

O manuscrito editável principal é [`projecto-completo.md`](projecto-completo.md). A cópia DOCX de conveniência para leitura e revisão em LibreOffice é [`projecto-completo.docx`](projecto-completo.docx).

## Documentos principais

- `projecto-completo.md`: manuscrito consolidado em Markdown. Mantém uma linha de versão no topo.
- `projecto-completo.docx`: cópia DOCX principal para revisão no LibreOffice, incluindo imagens e comentários.
- `projecto-completo-repeticoes.docx`: versão derivada com cortes e condensações focados em repetições. Não substitui automaticamente o manuscrito principal.
- `sources/manuscript/annexes/data_extraction_explained.md`: material técnico integrado como Anexo A no manuscrito.
- `CHANGELOG.md`: registo cronológico das alterações do repositório.
- `AGENTS.md`: regras operacionais para edição, pesquisa, bibliografia, backups, commits e exportações.

Nota: ficheiros antigos como `sources/manuscript/baselines/Projecto completo_baseline.md` são históricos. O ficheiro ativo é `projecto-completo.md`.

## Estrutura do repositório

- `chapters/text/`: rascunhos e materiais textuais por capítulo.
- `chapters/html/`: exports HTML de capítulos.
- `docs/`: documentação de trabalho, exports datados, auditorias, relatórios e conversões.
- `figuras/`: figuras extraídas, corrigidas ou traduzidas para integração no manuscrito.
- `tabelas/`: fontes editáveis e notas de trabalho para tabelas.
- `sources/`: fontes de trabalho, documentos auxiliares e outputs de pesquisa.
- `sources/docx/`: documentos `.docx` de apoio.
- `sources/elicit/`: pesquisas, reports, notas e sessões locais do Elicit por capítulo/secção.
- `sources/manuscript/`: materiais derivados do próprio manuscrito, incluindo anexos, auditorias, versões base e revisões.
- `sources/notes/`: notas soltas ou datadas que não pertencem ao corpo principal do manuscrito.
- `material/`: biblioteca local de PDFs e recursos temáticos.
- `projecto_completo_bibliografia/`: PDFs e controlo bibliográfico específico do manuscrito.
- `projecto-completo_media/`: imagens associadas ao Markdown convertido/extraído.
- `versions/`: cópias cronológicas de segurança antes de alterações relevantes.
- `tools/`: scripts locais de conversão, extração, comentários, bibliografia e manutenção.
- `projects/`: projetos técnicos associados à investigação.
- `mendeley-downloader/`: utilitário separado para descarga em lote via API do Mendeley.

## Fluxo de trabalho recomendado

1. Confirmar o estado do repositório:

```bash
git status --short
```

2. Antes de uma revisão substantiva do manuscrito, criar uma cópia em `versions/`.

3. Editar o texto em `projecto-completo.md` quando a alteração for textual e canónica.

4. Quando a revisão ocorrer diretamente no LibreOffice, trabalhar sobre `projecto-completo.docx` e evitar regenerar o DOCX inteiro se for necessário preservar comentários.

5. Guardar exports datados em `docs/` e manter `projecto-completo.docx` como cópia principal.

6. Atualizar o `CHANGELOG.md` depois de cada alteração ao repositório.

7. Quando forem adicionadas citações ao manuscrito, atualizar também a bibliografia final, copiar PDFs locais para `projecto_completo_bibliografia/` quando disponíveis e manter `projecto_completo_bibliografia/pdfs_em_falta.md` atualizado.

## LibreOffice, DOCX e comentários

O fluxo atual usa LibreOffice, não Microsoft Word. Isto importa porque algumas operações de conversão podem perder comentários ou alterar a estrutura interna do DOCX.

Práticas recomendadas:

- Verificar se existe ficheiro lock `.~lock.*.docx#` antes de editar automaticamente um DOCX.
- Não commitar ficheiros `.~lock.*`.
- Para alterações pequenas em DOCX com comentários, preferir edição localizada do pacote DOCX em vez de regeneração completa.
- Validar o DOCX após alterações, confirmando que continua a abrir, que preserva `word/comments.xml` e que as imagens continuam embebidas.
- Criar cópias datadas em `docs/` ou `versions/` antes de intervenções sensíveis.

Ferramentas relevantes:

- `tools/extract_docx_comments.py`: extrai comentários de DOCX e ajuda a mapear texto comentado.
- `tools/recover_docx_comments.py`: recupera comentários após exports baseados em Markdown quando a estrutura permite.
- `tools/docx_to_md.py`: converte DOCX para Markdown e extrai imagens embebidas.
- `tools/backup_docx.sh`: cria um backup datado de `projecto-completo.docx` em `versions/` e regenera sempre `projecto-completo.pdf` a partir do DOCX atual.
- `tools/docx_to_pdf.sh`: regenera `projecto-completo.pdf` a partir do `projecto-completo.docx` atual (fonte única da conversão DOCX→PDF).
- `tools/install_hooks.sh`: instala os git hooks versionados do repositório (aponta `core.hooksPath` para `tools/hooks/`).

## Backup do DOCX e PDF

```bash
./tools/backup_docx.sh [etiqueta]
```

Guarda uma cópia datada em `versions/projecto-completo-docx-<timestamp>-<etiqueta>.docx` e, no mesmo passo, regenera `projecto-completo.pdf` a partir do `projecto-completo.docx` atual usando LibreOffice em modo headless. Correr sempre que o DOCX for alterado, para o PDF acompanhar a versão mais recente.

### PDF automático no commit

O PDF é mantido em sincronia automaticamente por um git hook `pre-commit` versionado (`tools/hooks/pre-commit`): sempre que `projecto-completo.docx` faz parte de um commit, o hook regenera `projecto-completo.pdf` e adiciona-o ao mesmo commit. Instalar os hooks uma vez por clone:

```bash
./tools/install_hooks.sh
```

Isto aponta `core.hooksPath` para `tools/hooks/`, pelo que os hooks ficam versionados com o repositório. Não usar `git commit --no-verify` quando o DOCX foi alterado.

## Conversão entre formatos

### Markdown para DOCX

```bash
python3 tools/md_to_docx.py projecto-completo.md
python3 tools/md_to_docx.py projecto-completo.md --output docs/projecto-completo-revisao.docx
```

O conversor local suporta headings, parágrafos, listas simples, citações, blocos de código, tabelas simples e imagens Markdown.

### DOCX para Markdown

```bash
python3 tools/docx_to_md.py projecto-completo.docx -o docs/projecto-completo-convertido.md
```

Quando o DOCX contém imagens embebidas, o conversor cria uma pasta `_media` ao lado do Markdown gerado.

### Markdown para ODT

```bash
python3 tools/md_to_odt.py projecto-completo.md
python3 tools/md_to_odt.py projecto-completo.md --output docs/projecto-completo.odt
```

### ODT para Markdown

```bash
python3 tools/odt_to_md.py docs/projecto-completo.odt --output docs/projecto-completo-odt.md
```

## Figuras e tabelas

- As figuras de trabalho vivem em `figuras/`.
- As auditorias e contact sheets de figuras ficam em `docs/`.
- As fontes editáveis de tabelas ficam em `tabelas/`.
- O ficheiro `tabelas.docx` é um documento consolidado de trabalho, não substitui automaticamente as tabelas integradas no manuscrito.

Relatórios úteis recentes:

- `docs/figuras-auditoria-2026-06-30.md`
- `docs/figuras-imagens-auditoria-2026-06-30.md`
- `docs/figuras-correcoes-visuais-2026-07-01.md`
- `docs/figuras-recorte-margem-superior-2026-07-02.md`
- `docs/relatorio-repeticoes-projecto-completo-2209-07072026.md`

## Bibliografia do manuscrito

O diretório [`projecto_completo_bibliografia`](projecto_completo_bibliografia) mantém lado a lado:

- PDFs correspondentes às referências usadas no manuscrito.
- notas auxiliares de correspondência.
- controlo de PDFs ainda em falta.

O ficheiro [`projecto_completo_bibliografia/pdfs_em_falta.md`](projecto_completo_bibliografia/pdfs_em_falta.md) é o registo autoritativo das referências do manuscrito que ainda não têm PDF localizado em `material/` ou em `projecto_completo_bibliografia/`.

## Biblioteca local

As subpastas de `material/` estão organizadas por tema. Exemplos:

- `material/prosthetics-design/`
- `material/prosthetics-user/`
- `material/prosthetics-control/`
- `material/parametrico/`
- `material/3dprinting-prosthetics/`
- `material/colaboracao/`
- `material/reabilitacao/`
- `material/lower-limb/`
- `material/antropometria/`
- `material/normas/`

Não sobrescrever PDFs originais em `material/`. Criar derivados editados junto do capítulo ou tema que os usa.

## Pesquisa com Elicit

O repositório mantém uma cópia local de pesquisas, reports e sessões para que o trabalho seja auditável fora da interface web.

Estrutura recomendada:

```text
sources/elicit/<capitulo>/<subsecção>/queries.md
sources/elicit/<capitulo>/<subsecção>/searches/
sources/elicit/<capitulo>/<subsecção>/reports/
sources/elicit/<capitulo>/<subsecção>/notes.md
sources/elicit/agent-sessions/<capitulo>/<subsecção>/<session-slug>/
```

Configuração da API:

```bash
export ELICIT_API_KEY="elk_live_..."
python3 -m py_compile tools/elicit_api.py
```

Exemplos:

```bash
python3 tools/elicit_api.py search "upper limb prosthetics personalization" --min-year 2020 --max-results 5
python3 tools/elicit_api.py report "How can parametric design improve upper limb prosthetic personalization?" --title "Parametric Prosthetic Personalization"
python3 tools/elicit_api.py reports --limit 5
python3 tools/elicit_api.py get-report <report_id>
python3 tools/elicit_api.py wait-report <report_id> --poll-seconds 30
python3 tools/elicit_api.py download-report <report_id>
```

Não referir explicitamente o Elicit no corpo académico do manuscrito. Os outputs locais servem como material de apoio, síntese e verificação.

## Ferramentas principais

- `tools/md_to_docx.py`: exportação Markdown para DOCX.
- `tools/docx_to_md.py`: conversão DOCX para Markdown com extração de imagens.
- `tools/md_to_odt.py`: exportação Markdown para ODT.
- `tools/odt_to_md.py`: conversão ODT para Markdown.
- `tools/extract_docx_comments.py`: extração e mapeamento de comentários DOCX.
- `tools/recover_docx_comments.py`: recuperação de comentários DOCX.
- `tools/insert_docx_figures.py`: apoio à inserção de figuras em DOCX.
- `tools/link_citations_to_bibliography.py`: ligação de citações à bibliografia.
- `tools/elicit_api.py`: CLI principal para a API do Elicit.
- `tools/elicit_agent_session_ingest.py`: ingestão de sessões locais do Elicit.
- `tools/harper_lint.mjs`: lint offline com Harper para textos em inglês.

Validação rápida de scripts:

```bash
python3 -m py_compile tools/docx_to_md.py tools/md_to_docx.py tools/md_to_odt.py tools/odt_to_md.py
node tools/harper_lint.mjs --help
```

## Mendeley e manutenção da biblioteca

Ver também [`material/README.md`](material/README.md).

- `mendeley-downloader/`: utilitário separado para descarga em lote via API do Mendeley.
- `tools/mendeley_organizer.py`: organiza PDFs locais por correspondência com pastas Mendeley.
- `tools/mendeley_enrich.py`: enriquece registos com metadata.
- `tools/flag_titles.py`: assinala problemas em nomes de ficheiros.
- `tools/rename_pdfs.py`: renomeia PDFs com base em metadata.
- `tools/elicit_download.py`, `tools/elicit_fetch_missing.py`, `tools/elicit_sync.py`: apoio à descarga e sincronização de materiais de pesquisa.

## Comandos úteis

Listar ficheiros:

```bash
rg --files .
find chapters sources material -maxdepth 2 -type f
```

Procurar texto no manuscrito:

```bash
rg -n "termo a procurar" projecto-completo.md
```

Ver exports recentes:

```bash
ls -lt docs | head
```

Ver estado Git:

```bash
git status --short
git log -5 --oneline
```

## Convenções

- Usar português europeu no manuscrito.
- Preferir nomes em minúsculas com underscores ou hífen, seguindo o padrão local.
- Evitar variantes como `final`, `final2` ou `new`.
- Guardar outputs derivados junto da respetiva fonte ou em `docs/`.
- Não mover nem apagar materiais brutos em `material/`.
- Atualizar o `CHANGELOG.md` sempre que o repositório for alterado.
- Quando o utilizador disser `cpd`, tratar como `commit, push, deploy`.

## Referências úteis

- Documentação oficial do Elicit: https://docs.elicit.com/
- Exemplos oficiais da API do Elicit: https://github.com/elicit/api-examples
- Guia local das ferramentas Mendeley: [`material/README.md`](material/README.md)
