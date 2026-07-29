# Dissertação — espaço de trabalho

Este repositório reúne o manuscrito, os documentos finais no modelo do IPCA, os anexos, a bibliografia, as figuras, os dados de apoio e as ferramentas usadas na dissertação de Mestrado em Design e Desenvolvimento de Produto:

> **Integração do Design e da Inteligência Artificial em Processos Paramétricos para o Desenvolvimento de Próteses de Membros Superiores em Impressão 3D**

Autor: Pedro Miguel Candeias da Silva

Orientador: Demétrio Ferreira Matos

Estado documentado: 21 de Julho de 2026

Versão do manuscrito: 0.4.109

## Documentos principais

| Ficheiro | Função |
| --- | --- |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md) | Fonte textual consolidada do manuscrito, incluindo os Anexos A, B, C e D. |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx) | Documento revisto e formatado segundo o modelo institucional do IPCA. |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf) | PDF de revisão e inspecção visual do documento IPCA. |
| [`CHANGELOG.md`](CHANGELOG.md) | Registo cronológico das alterações realizadas. |
| [`AGENTS.md`](AGENTS.md) | Regras obrigatórias de edição, cópias de segurança, bibliografia, exportação e organização. |

Os três primeiros ficheiros constituem o conjunto canónico do manuscrito. As cópias anteriores, exportações datadas e documentos de verificação foram retirados do *root* e organizados em `docs/versoes/`; não substituem o manuscrito revisto.

## Estado actual

- O PDF canónico tem 209 páginas A4 e corresponde à versão 0.4.106 do manuscrito; a versão 0.4.109 do MD aguarda o próximo *Refresh* do Mendeley Cite no DOCX para regeneração dos exports.
- O DOCX conserva 12 notas de rodapé e 34 imagens, sem comentários nativos por resolver; figuras e tabelas usam numeração sequencial por campos SEQ (29 figuras, 31 tabelas), pendente de Ctrl+A → F9 no Word para actualizar campos e índices.
- A auditoria bibliográfica confrontou directamente 320 dos 434 pares afirmação–fonte relativos a *papers*; 114 pares permanecem pendentes.
- Os dez casos incompatíveis prioritários já confrontados foram corrigidos. Este resultado não constitui validação automática dos pares ainda pendentes.
- Existem localmente 140 dos 141 *papers* citados. Continua em falta Yao, Moon e Bi (2016), além de um capítulo de livro de Ghali (2008), contabilizado separadamente. O PDF de Dexter, Atkinson e Dearden (2013) foi obtido no arquivo Design4Health; o confronto revelou que a entrada bibliográfica actual conserva coautores incorrectos e ainda necessita de correcção no manuscrito.
- A bibliografia do DOCX contém 169 entradas, das quais 158 têm correspondência PDF validada na pasta consolidada. O inventário e os critérios de correspondência encontram-se em [`consolidacao_referencias_docx.md`](projecto_completo_bibliografia/consolidacao_referencias_docx.md).

O detalhe encontra-se na [`auditoria_referencias_texto_papers_061.md`](docs/revisoes/auditoria_referencias_texto_papers_061.md) e na lista autoritativa [`pdfs_em_falta.md`](projecto_completo_bibliografia/pdfs_em_falta.md).

## Organização das versões

| Pasta | Conteúdo |
| --- | --- |
| [`docs/versoes/backups/`](docs/versoes/backups/) | Cópias criadas antes de alterações substantivas, incluindo os antigos conteúdos da pasta `versions/`. |
| [`docs/versoes/exportacoes/`](docs/versoes/exportacoes/) | DOCX e PDF datados produzidos para revisão visual ou entrega intermédia. |
| [`docs/versoes/documentos-historicos/`](docs/versoes/documentos-historicos/) | Versões anteriores, documentos de validação e antigas cópias de conveniência que estavam no *root*. |

O ficheiro auxiliar `tabelas.docx` foi colocado em `sources/docx/`, junto dos restantes documentos DOCX de apoio.

## Anexos e suplementos

Os Anexos A–D integram o manuscrito consolidado e conservam fontes editáveis em
`sources/manuscript/annexes/`. O Anexo D reúne a preparação para impressão, os
resultados dimensionais, a montagem e articulação da UnLimbited Phoenix e o
registo fotográfico dos protótipos integrado no Capítulo 8.

| Anexo ou suplemento | Conteúdo | Fonte editável |
| --- | --- | --- |
| Anexo A | Extracção, normalização, cobertura e limitações dos dados antropométricos | [`data_extraction_explained.md`](sources/manuscript/annexes/data_extraction_explained.md) |
| Anexo B | Avaliação complementar do processo paramétrico e da interface HandFab | [`anexo_b_avaliacao_processo_interface_handfab.md`](sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.md) |
| Anexo C | Adaptação paramétrica dos modelos Flexy Beast, Cyborg Beast, Paraglider Hand e UnLimbited Phoenix | [`anexo_c_adaptacao_parametrica_modelos.md`](sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.md) |
| Anexo D | Preparação para fabrico, comparação dimensional, compatibilidade com orientações de escala, montagem e articulação | [`anexo_d_preparacao_impressao.md`](sources/manuscript/annexes/testes_preparacao_impressao/anexo_d_preparacao_impressao.md) |
| Suplemento 1 | Dados antropométricos usados para estruturar a base local | [`01_dados_antropometricos/`](suplementos/01_dados_antropometricos/) |
| Suplemento 2 | Protocolos, metadados e resultados seleccionados da avaliação técnica da plataforma | [`02_avaliacao_plataforma/`](suplementos/02_avaliacao_plataforma/) |
| Suplemento 3 | Dicionário de parâmetros e percurso rastreável entre perfil, cálculos e malhas | [`03_parametrizacao_percurso/`](suplementos/03_parametrizacao_percurso/) |
| Suplemento 4 | Projectos de preparação, resultados, medições, montagem e fotografias dos protótipos | [`04_preparacao_impressao_prototipos/`](suplementos/04_preparacao_impressao_prototipos/) |

O pacote agregado é descrito em [`guia_dos_suplementos.md`](suplementos/guia_dos_suplementos.md), e [`manifesto_ficheiros.csv`](suplementos/manifesto_ficheiros.csv) identifica a origem e a função de cada ficheiro entregue. Os DOCX e PDF autónomos dos Anexos B, C e D servem para revisão isolada. Quando um anexo integrado for alterado, é necessário voltar a inseri-lo no manuscrito principal e actualizar a paginação.

## Plataforma HandFab

A plataforma desenvolvida para a investigação encontra-se num repositório de aplicação separado:

- código local principal: `/home/pec/dev/ai-parametric-prosthetic-hand-generator`;
- ambiente local de desenvolvimento: `http://localhost:3000/dashboard`;
- versão pública: <https://handfab.pedrocandeias.net/>.

O conteúdo de `projects/ai-parametric-prosthetic-hand-generator/` neste repositório deve ser tratado como material de apoio ou cópia de trabalho, não como substituto automático do repositório operacional acima indicado.

A plataforma é apresentada na dissertação como protótipo funcional de investigação. Os ensaios documentam o comportamento técnico nos casos examinados; não demonstram adequação clínica, conforto, eficácia protésica, usabilidade com participantes, segurança ou durabilidade.

## Estrutura do repositório

- `chapters/text/`: rascunhos e materiais textuais por capítulo.
- `chapters/html/`: exportações HTML históricas de capítulos.
- `docs/`: relatórios de revisão, auditorias e documentação de trabalho.
- `docs/versoes/`: cópias de segurança, exportações datadas e documentos históricos.
- `figuras/`: figuras integradas ou preparadas para o manuscrito.
- `tabelas/`: fontes editáveis e notas relativas às tabelas.
- `sources/docx/`: documentos DOCX de apoio.
- `sources/manuscript/`: anexos, suplementos, auditorias, versões de referência e notas de revisão do manuscrito.
- `sources/elicit/`: pesquisas, relatórios, sessões e notas de investigação organizadas por capítulo e secção.
- `suplementos/`: pacote agregado de entrega com os quatro conjuntos suplementares e o respectivo manifesto.
- `material/`: biblioteca local de artigos, normas e materiais de referência; os originais não devem ser sobrescritos.
- `projecto_completo_bibliografia/`: PDFs associados à bibliografia e lista de publicações ainda sem cópia local.
- `projecto-completo_media/`: recursos gráficos usados pelo Markdown consolidado.
- `tools/`: **todos os scripts do repositório**, organizados por finalidade — ver `tools/README.md` para o índice completo e a secção «Ferramentas» abaixo para os comandos correntes.
- `archive/` e `recovered/`: materiais históricos ou recuperados; não são fontes activas.

## Ferramentas

Todos os *scripts* do repositório estão em `tools/`, agrupados por finalidade;
a única excepção é `deploy.sh`, o ponto de entrada de topo. O índice completo,
com uma linha por ferramenta, está em [`tools/README.md`](tools/README.md).

Os comandos correm-se **a partir da raiz do repositório** — cada *script*
Python descobre a raiz pela sua própria localização, pelo que não é preciso
mudar de directório.

| Pasta | Para que serve | Ferramentas |
| --- | --- | --- |
| `tools/` (raiz) | Comandos do dia-a-dia | `backup_docx.sh`, `docx_to_pdf.sh`, `editar_docx_libreoffice.sh`, `word_lo_bridge.py`, `install_hooks.sh`, `md_to_docx.py`, `docx_to_md.py` |
| `tools/conversao/` | Formatos derivados | `md_to_odt.py`, `odt_to_md.py`, `link_citations_to_bibliography.py` |
| `tools/bibliografia/` | PDFs citados | `consolidate_docx_referenced_pdfs.py`, `fetch_mendeley_referenced_pdfs.py` |
| `tools/mendeley-tools/` | Biblioteca Mendeley (submódulo) | organizador, enriquecedor, deduplicador, sincronização de DOIs, normalizador de títulos |
| `tools/extraccao/` | Extrair do documento | `extract_figures_tables.py`, `extract_suggested_assets.py`, `extract_docx_comments.py`, `recover_docx_comments.py`, `extract_print_and_dimensional_tables.py`, `read_xlsx_cells.py`, `generate_missing_pdfs_report.py` |
| `tools/revisao/` | Revisão e citações | `audit_docx_languagetool.py`, `generate_languagetool_filtered_reports.py`, `harper_lint.mjs`, `grammarly_api.py`, `generate_citation_evidence_sheet.py`, `generate_citation_traceability_sheet.py` |
| `tools/manutencao/` | Versão e changelog | `version_manuscript.py`, `update_changelog.py`, `commit_from_changelog.py`, `synchronise_docx_pagination.py`, `sync_annex_d_source.py` |
| `tools/pdfs/` | Colecção de PDFs | `organize_toorganize.py`, `flag_titles.py`, `rename_pdfs.py`, `build_supplements_package.py`, `calcular_resultados_dimensionais_fisicos.py` |
| `tools/elicit/` | Pesquisa bibliográfica | `elicit_sync.py`, `elicit_download.py`, `elicit_fetch_missing.py`, `elicit_api.py`, `elicit_agent_session_ingest.py` |
| `tools/revisoes/` | 95 revisões pontuais já aplicadas | histórico — **não voltar a correr** (ver abaixo) |
| `tools/hooks/` | Git hooks versionados | `pre-commit` (regenera o PDF) |

As secções seguintes descrevem os percursos completos: conversão documental,
normalização da biblioteca Mendeley, revisão académica e verificações.

`./deploy.sh` encadeia os três *scripts* de `tools/manutencao/`: acrescenta a
entrada ao changelog, incrementa a versão do manuscrito e faz o *commit*.

Num clone novo, o submódulo das ferramentas Mendeley obtém-se com:

```bash
git submodule update --init tools/mendeley-tools
```

### Os scripts de `tools/revisoes/`

Cada um destes 95 *scripts* foi escrito para **uma** alteração concreta ao
manuscrito e já foi corrido; o sufixo numérico (`_045` … `_113`) dá a ordem de
aplicação e o `CHANGELOG.md` descreve o resultado de cada um. Foram escritos
contra uma versão específica do DOCX, pelo que aplicá-los hoje duplicaria
texto ou corromperia a numeração. Ficam versionados como registo de como cada
alteração foi feita, e como ponto de partida para escrever a seguinte.

As duas excepções — `integrate_annexes_bc.py` e
`apply_annex_local_indexes.py` — continuam a ser fluxo de trabalho vivo e
estão documentadas em «Integração dos Anexos B e C», abaixo.

## Fluxo de edição do manuscrito

Antes de qualquer alteração substantiva:

```bash
git status --short
./tools/backup_docx.sh nome-da-alteracao
```

`backup_docx.sh` cria uma cópia datada do DOCX canónico em `docs/versoes/backups/` e regenera o PDF canónico com o mesmo nome-base.

Depois de uma alteração:

1. actualizar a versão no início de `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md`;
2. sincronizar o conteúdo com o DOCX revisto;
3. regenerar o PDF;
4. verificar índice, listas de tabelas e figuras, paginação, imagens e quebras;
5. acrescentar uma entrada no topo de `CHANGELOG.md`;
6. executar uma verificação final do pacote DOCX e do PDF.

O repositório contém transformações específicas em `tools/revisoes/`. Estes scripts registam revisões já aplicadas; não devem ser executados indiscriminadamente sobre uma versão posterior sem confirmar que os seus pontos de inserção ainda correspondem ao documento actual.

### Integração dos Anexos B e C

As fontes editáveis dos anexos são convertidas para DOCX e integradas no documento IPCA por:

```bash
python3 tools/md_to_docx.py \
  sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.md \
  --output sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.docx

python3 tools/md_to_docx.py \
  sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.md \
  --output sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.docx

python3 tools/revisoes/integrate_annexes_bc.py \
  --markdown pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md \
  --docx pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx

python3 tools/revisoes/apply_annex_local_indexes.py \
  pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx \
  --version 0.4.39
```

O integrador impede uma segunda inclusão acidental. O segundo comando conserva no índice principal apenas o título e a página inicial de cada anexo, deslocando as entradas detalhadas para índices próprios no início dos Anexos A, B e C. Depois destas operações, a paginação estática deve ser actualizada a partir de um PDF provisório com `tools/manutencao/synchronise_docx_pagination.py`.

## Conversão e verificação documental

### Markdown para DOCX simples

```bash
python3 tools/md_to_docx.py \
  pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md \
  --output docs/versoes/exportacoes/manuscrito-revisao.docx
```

Este conversor cria um DOCX genérico. Não substitui, por si só, a formatação institucional do documento IPCA.

### DOCX para Markdown

```bash
python3 tools/docx_to_md.py \
  pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx \
  -o docs/versoes/exportacoes/manuscrito-convertido.md
```

### DOCX para PDF

```bash
./tools/docx_to_pdf.sh
```

O comando converte o DOCX canónico no PDF canónico através do LibreOffice em modo *headless*.

### Editar o DOCX no LibreOffice sem perder o Mendeley Cite

O DOCX canónico é gerido pelo Mendeley Cite do Word. O LibreOffice preserva as citações vivas ao gravar, mas descarta o estado do add-in (`word/webextensions/`), o que impediria o Word de voltar a reconhecê-las. A ponte repõe essas peças automaticamente:

```bash
tools/editar_docx_libreoffice.sh
```

O comando guarda uma cópia de referência, abre o Writer e, quando este fecha, restaura o estado do Mendeley Cite com verificação byte a byte. Em alternativa, os passos podem ser corridos à mão com `python3 tools/word_lo_bridge.py backup <docx>` antes da edição e `… restore <docx>` depois de gravar.

Cuidados: fechar as restantes janelas do LibreOffice antes de usar o invólucro; editar prosa à vontade mas evitar alterar texto dentro de uma citação (o Word passa a tratá-la como *manual override*); inserir citações novas continua a fazer-se no Word.

### Normalizar a biblioteca Mendeley

A bibliografia do DOCX é regenerada a partir da biblioteca Mendeley na nuvem, pelo que erros de inserção nos registos — títulos em MAIÚSCULAS, apelidos em maiúsculas, entidades HTML, quebras de linha da extracção de PDF, ponto final, nomes de ficheiro usados como título — passam tal e qual para o manuscrito. A auditoria corre sem escrever nada:

Os scripts Mendeley são ferramentas independentes, mantidas no repositório
[`mendeley-tools`](https://github.com/pedrocandeias/mendeley-tools) e usadas aqui como submódulo em `tools/mendeley-tools/`. Num clone novo, obtêm-se com:

```bash
git submodule update --init tools/mendeley-tools
```

```bash
cd tools/mendeley-tools
python3 mendeley_normalise_titles.py --report /tmp/auditoria.md
python3 mendeley_normalise_titles.py --overrides mendeley_title_overrides.json --apply
```

As credenciais vêm do `keyring` usado pelo `mendeley-auth`, que só está instalado no interpretador da ferramenta; se o `python3` do sistema falhar com `ModuleNotFoundError: keyring`, usar `~/.local/share/uv/tools/mendeley-mcp/bin/python` no lugar de `python3`.

Como as ferramentas não pressupõem este repositório, os caminhos deste projecto indicam-se por opção — `--material` para a pasta dos PDFs e `--md` para a bibliografia do manuscrito — ou uma vez por sessão:

```bash
export MENDELEY_MATERIAL=/home/pec/dev/mestrado/material
export MENDELEY_MANUSCRIPT=/home/pec/dev/mestrado/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md
```

O script prefere o título do CrossRef quando o registo tem DOI. Nos casos em que o próprio CrossRef guarda o título em maiúsculas, a grafia correcta é fixada à mão em `mendeley_title_overrides.json` (um valor `null` exclui o registo). A ferramenta é idempotente: uma segunda execução não regrava o que já está correcto. As correções só aparecem no manuscrito depois do *Refresh* do Mendeley Cite no Word. O guia completo das cinco ferramentas está em `tools/mendeley-tools/README.md`.

### Verificações rápidas

```bash
unzip -t pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx
pdfinfo pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf
pdftotext -layout pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf /tmp/manuscrito-revisto.txt
rg -n "Anexo [ABCD]|Tabela [BCD]\.|Figura [CD]\.1" /tmp/manuscrito-revisto.txt
```

Os hooks versionados podem ser instalados com:

```bash
./tools/install_hooks.sh
```

Quando o DOCX canónico faz parte de um *commit*, o *hook* `pre-commit` regenera e adiciona o PDF com o mesmo nome-base. Não usar `git commit --no-verify` quando o DOCX foi alterado.

## Revisão académica

O relatório principal de revisão encontra-se em:

- [`docs/relatorio-revisao-academica-integral-dissertacao-2026-07-13.md`](docs/relatorio-revisao-academica-integral-dissertacao-2026-07-13.md)

Os pontos resolvidos são identificados por `[X]`. Uma marca só deve ser acrescentada quando a correcção estiver presente no manuscrito, no documento revisto e, quando aplicável, na evidência ou no anexo correspondente.

## Bibliografia e investigação

Sempre que uma citação ou referência for acrescentada ou corrigida:

1. uniformizar a citação no texto;
2. actualizar a entrada bibliográfica em APA 7;
3. localizar e copiar o PDF para `projecto_completo_bibliografia/`, quando disponível;
4. actualizar [`projecto_completo_bibliografia/pdfs_em_falta.md`](projecto_completo_bibliografia/pdfs_em_falta.md).

As pesquisas e relatórios de apoio são guardados em `sources/elicit/`. O manuscrito não deve mencionar o Elicit como fonte académica; as afirmações devem apoiar-se nos artigos e documentos originais.

## Convenções

- escrever em português europeu;
- manter o enquadramento de uma dissertação em Design e Desenvolvimento de Produto;
- distinguir requisitos, decisões implementadas, observações técnicas e propriedades ainda não avaliadas;
- evitar afirmar validação clínica, funcional ou de utilização quando apenas existe verificação técnica;
- usar nomes de ficheiro claros e evitar variantes como `final2`, `novo` ou `corrigido-final`;
- não apagar nem sobrescrever materiais originais em `material/`;
- guardar derivados junto da respectiva fonte ou em `docs/`;
- actualizar o `CHANGELOG.md` depois de cada alteração;
- interpretar `cpd` como `commit, push, deploy`.
