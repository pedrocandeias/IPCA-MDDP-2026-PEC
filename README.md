# Mestrado Thesis Workspace

Este repositório organiza a redação da dissertação, a pesquisa bibliográfica, a biblioteca local de PDFs e os utilitários usados para manter tudo coerente ao longo do trabalho.

O foco principal é o manuscrito [Projecto completo.md](/home/pec/dev/mestrado/Projecto%20completo.md), mas o repositório inclui também:
- integração local com a API do [Elicit](https://docs.elicit.com/)
- utilitários para descarregar, organizar e sincronizar pesquisa bibliográfica
- scripts para enriquecimento e organização de biblioteca Mendeley
- ferramentas auxiliares para nomes de ficheiros, figuras, tabelas e manutenção da biblioteca local

## Estrutura do repositório

- `Projecto completo.md`: manuscrito principal consolidado
- `CHANGELOG.md`: registo de alterações do repositório
- `versions/`: cópias cronológicas do manuscrito antes de revisões substantivas
- `chapters/text/`: rascunhos de capítulos em texto
- `chapters/html/`: exports HTML de capítulos
- `sources/`: fontes de trabalho e outputs de pesquisa
- `sources/docx/`: documentos `.docx` de apoio
- `sources/elicit/`: pesquisas, reports, notes e sessões locais do Elicit organizados por capítulo/secção
- `material/`: biblioteca local de PDFs e recursos temáticos
- `projecto_completo_bibliografia/`: cache bibliográfica específica do manuscrito e controlo de PDFs em falta
- `mendeley-downloader/`: utilitário separado para descarga em lote de PDFs via API do Mendeley
- `tools/`: todas as ferramentas locais de integração, conversão e manutenção do repositório
- `docs/`: documentação curta sobre fluxos e integração local

## Estrutura do Elicit

O repositório usa uma organização local previsível para pesquisa bibliográfica:

- `sources/elicit/<capitulo>/<subsecção>/queries.md`
- `sources/elicit/<capitulo>/<subsecção>/searches/`
- `sources/elicit/<capitulo>/<subsecção>/reports/`
- `sources/elicit/<capitulo>/<subsecção>/notes.md`

Para sessões de agente:

- `sources/elicit/agent-sessions/<capitulo>/<subsecção>/<session-slug>/`

Isto permite manter perguntas, resultados, notas de leitura e exports ligados a uma secção concreta do manuscrito.

## Integração com a API do Elicit

### Requisitos

Antes de usar a integração:

1. Ter Python 3 instalado
2. Ter conta no Elicit
3. Ter plano `Pro` ou superior para acesso à API
4. Criar uma API key em `https://elicit.com/settings`

### Configuração

Exporta a chave da API no terminal:

```bash
export ELICIT_API_KEY="elk_live_..."
```

Valida a CLI local:

```bash
python3 -m py_compile tools/elicit_api.py
```

### Comandos principais

Pesquisar literatura:

```bash
python3 tools/elicit_api.py search "upper limb prosthetics personalization" --min-year 2020 --type RCT --max-results 5
```

Criar um report:

```bash
python3 tools/elicit_api.py report "How can parametric design improve upper limb prosthetic personalization?" --title "Parametric Prosthetic Personalization"
```

Listar e inspecionar reports:

```bash
python3 tools/elicit_api.py reports --limit 5
python3 tools/elicit_api.py get-report <report_id>
```

Esperar por um report:

```bash
python3 tools/elicit_api.py wait-report <report_id> --poll-seconds 30
```

Descarregar outputs:

```bash
python3 tools/elicit_api.py download-report <report_id>
```

Os outputs ficam organizados em `sources/elicit/...`, em vez de permanecerem apenas na interface web.

## Ferramentas em `tools/`

### `tools/elicit_api.py`

CLI principal para interagir com a API do Elicit:
- pesquisa
- criação de reports
- polling de estado
- descarga de `pdf`, `docx` e metadados

### `tools/elicit_agent_session_ingest.py`

Script de apoio para ingestão e extração de conteúdo de sessões locais do Elicit, preservando estrutura legível e materiais reutilizáveis.

### `tools/md_to_docx.py`

CLI local para exportar ficheiros Markdown para `.docx` sem dependências externas. Cada execução cria uma nova cópia em `docs/` com timestamp no nome, no formato `nome-do-ficheiro-hhmm-ddmmyyyy.docx`. Suporta o subset de Markdown mais usado neste repositório:
- headings
- parágrafos
- listas com marcadores
- citações em bloco
- blocos de código
- tabelas simples em pipe syntax
- imagens locais em sintaxe Markdown e referências `![...][imageN]`, incluindo `data:image/...`

Exemplo:

```bash
python3 tools/md_to_docx.py "Projecto completo.md"
```

Exemplos com destino explícito:

```bash
python3 tools/md_to_docx.py "Projecto completo.md" --output-dir sources/docx
python3 tools/md_to_docx.py "Projecto completo.md" --output sources/docx/projecto_completo.docx
```

### `tools/docx_to_md.py`

CLI local para converter ficheiros `.docx` de volta para Markdown. Cada execução cria uma nova cópia em `docs/` com timestamp no nome, no formato `nome-do-ficheiro-hhmm-ddmmyyyy.md`.

Suporta a recuperação de:
- headings
- parágrafos
- listas simples
- listas numeradas simples
- citações em bloco
- blocos de código
- tabelas Word simples

Exemplo:

```bash
python3 tools/docx_to_md.py "sources/docx/cap_2_3_Parametric Design and Additive Manufacturing for Product Customization.docx"
python3 tools/docx_to_md.py "sources/docx/cap_2_3_Parametric Design and Additive Manufacturing for Product Customization.docx" --output docs/cap_2_3.md
```

### `tools/md_to_odt.py`

CLI local para exportar ficheiros Markdown para `.odt` (LibreOffice Writer). Cada execução cria uma nova cópia em `docs/` com timestamp no nome, no formato `nome-do-ficheiro-hhmm-ddmmyyyy.odt`.

Esta ferramenta gera diretamente um pacote ODT em Python, sem depender do LibreOffice. Reaproveita o parser Markdown já usado no conversor `md_to_docx.py`.

Suporta headings, parágrafos, listas simples e numeradas, blocos de citação, blocos de código, tabelas simples e imagens Markdown.

Exemplo:

```bash
python3 tools/md_to_odt.py "Projecto completo.md"
python3 tools/md_to_odt.py "Projecto completo.md" --output docs/projecto_completo.odt
```

### `tools/odt_to_md.py`

CLI local para converter ficheiros `.odt` de volta para Markdown. Cada execução cria uma nova cópia em `docs/` com timestamp no nome, no formato `nome-do-ficheiro-hhmm-ddmmyyyy.md`.

Esta ferramenta lê diretamente o `content.xml` do pacote ODT em Python, sem depender do LibreOffice. Quando o ODT inclui imagens embebidas, extrai-as para uma pasta `<nome>_assets` ao lado do Markdown gerado.

Recupera headings, parágrafos, listas simples e numeradas, tabelas básicas e imagens embebidas.

Exemplo:

```bash
python3 tools/odt_to_md.py "docs/projecto-completo-1234-01012026.odt"
python3 tools/odt_to_md.py "docs/projecto-completo-1234-01012026.odt" --output docs/projecto_completo.md
```

### `tools/harper_lint.mjs`

CLI local para revisão gramatical e estilística com Harper, executada offline via `harper.js` em Node.js. Esta integração é adequada para ficheiros `.md`, `.txt` e outros textos curtos de trabalho, com suporte para seleção de dialeto inglês e ativação/desativação de regras.

Instalação:

```bash
npm install
```

Exemplos:

```bash
node tools/harper_lint.mjs check "Projecto completo.md"
node tools/harper_lint.mjs check docs/nota.md --locale en-GB --summary
node tools/harper_lint.mjs check docs/nota.md --json
node tools/harper_lint.mjs describe-rules
```

Notas:
- O wrapper assume `pt-PT` por defeito, para alinhar com o repositório. Nesse modo, a ferramenta não faz lint e avisa que o Harper ainda não suporta português europeu.
- Para lint real com Harper, mude explicitamente para um locale inglês suportado, por exemplo `--locale en-GB`.
- Harper suporta apenas inglês neste momento, incluindo os dialetos `en-US`, `en-GB`, `en-AU`, `en-CA` e `en-IN`.
- Para ajustar regras, passe `--config path/to/harper-rules.json` com um objeto JSON no formato esperado por `setLintConfig()`.

## Ferramentas de biblioteca em `tools/`

O diretório `material/` não guarda apenas PDFs. Também inclui utilitários para gestão da biblioteca e manutenção do corpus local.

### Ferramentas de Mendeley

Descritas com mais detalhe em [material/README.md](/home/pec/dev/mestrado/material/README.md).

- `mendeley-downloader/`
  utilitário separado, baseado na API do Mendeley, para descarregar em lote os ficheiros da biblioteca; usa uma app registada em `dev.mendeley.com`, expõe uma interface local em `http://localhost:5000` e, segundo o README próprio, funciona melhor com Python `3.8` ou anterior

- `tools/mendeley_organizer.py`
  organiza PDFs locais por correspondência com pastas Mendeley

- `tools/mendeley_enrich.py`
  enriquece registos com metadata via CrossRef e atualiza Mendeley/PDFs

- `tools/flag_titles.py`
  assinala problemas de nomes de ficheiros

- `tools/rename_pdfs.py`
  renomeia PDFs com base em metadata

### Ferramentas ligadas ao Elicit

- `tools/elicit_download.py`
  apoio à descarga de artigos a partir de listas/exportações locais

- `tools/elicit_fetch_missing.py`
  tentativa de recuperação de papers ainda em falta

- `tools/elicit_sync.py`
  sincronização e manutenção de dados auxiliares ligados ao workflow de pesquisa

- `material/elicit_missing_papers.csv`
  controlo local de artigos ainda por localizar

- `material/elicit_download_report.csv`
  ficheiro de trabalho para downloads por lote

- `material/elicit_download_report_workingfile.csv`
  variante de trabalho intermédia

### Outras ferramentas utilitárias

- `tools/extract_figures_tables.py`
  extração e apoio à organização de figuras/tabelas

- `material/figures_tables_index.md`
  índice local de figuras e tabelas

- `material/figures_tables_suggestions.md`
  notas de trabalho para seleção e utilização

- `tools/organize_toorganize.py`
  apoio à triagem de materiais ainda não organizados

## Biblioteca local

As subpastas de `material/` estão organizadas por tema, por exemplo:

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

Isto separa a biblioteca temática da bibliografia guardada na mesma pasta do manuscrito.

## Bibliografia do manuscrito

O diretório [projecto_completo_bibliografia](/home/pec/dev/mestrado/projecto_completo_bibliografia) serve para manter lado a lado:

- PDFs de suporte às referências efetivamente usadas em `Projecto completo.md`
- notas auxiliares sobre correspondências
- controlo do que ainda falta descarregar

O ficheiro [projecto_completo_bibliografia/pdfs_em_falta.md](/home/pec/dev/mestrado/projecto_completo_bibliografia/pdfs_em_falta.md) é o registo autoritativo das referências do manuscrito que ainda não têm PDF localizado em `material/` ou em `projecto_completo_bibliografia/`.

## Workflow recomendado

1. Trabalhar o texto em `Projecto completo.md`
2. Criar backup em `versions/` antes de revisões substantivas
3. Fazer pesquisa dirigida em `sources/elicit/`
4. Descarregar reports e guardar notas locais
5. Integrar incrementalmente no manuscrito
6. Atualizar a bibliografia final em `Projecto completo.md`
7. Copiar PDFs citados para `projecto_completo_bibliografia/`
8. Atualizar `projecto_completo_bibliografia/pdfs_em_falta.md`
9. Registar tudo no `CHANGELOG.md`

## Notas

- A integração do Elicit segue a documentação oficial e os exemplos públicos da API.
- Os links temporários de download do Elicit expiram; por isso a CLI volta a consultar o report antes de descarregar.
- O manuscrito não deve referir explicitamente o Elicit no corpo do texto académico; os outputs locais servem como material de apoio à escrita e verificação.

## Referências úteis

- Documentação oficial do Elicit: https://docs.elicit.com/
- Exemplos oficiais da API: https://github.com/elicit/api-examples
- Guia local das ferramentas Mendeley: [material/README.md](/home/pec/dev/mestrado/material/README.md)
