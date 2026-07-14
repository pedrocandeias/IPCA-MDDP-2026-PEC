# Dissertação — espaço de trabalho

Este repositório reúne o manuscrito, os documentos finais no modelo do IPCA, os anexos, a bibliografia, as figuras, os dados de apoio e as ferramentas usadas na dissertação de Mestrado em Design e Desenvolvimento de Produto:

> **Integração do Design e da Inteligência Artificial em Processos Paramétricos para o Desenvolvimento de Próteses de Membros Superiores em Impressão 3D**

Autor: Pedro Miguel Candeias da Silva

Orientador: Demétrio Ferreira Matos

Estado documentado: 14 de Julho de 2026

Versão do manuscrito: 0.4.39

## Documentos principais

| Ficheiro | Função |
| --- | --- |
| [`projecto-completo.md`](projecto-completo.md) | Fonte textual consolidada do manuscrito, incluindo os Anexos A, B e C. |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx) | Documento revisto e formatado segundo o modelo institucional do IPCA. |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf) | PDF de revisão e inspecção visual do documento IPCA. |
| [`projecto-completo.docx`](projecto-completo.docx) | Cópia de conveniência sincronizada com o DOCX revisto. |
| [`projecto-completo.pdf`](projecto-completo.pdf) | PDF sincronizado com a cópia DOCX principal. |
| [`pedro-candeias-projeto-mestrado-mdddp-ipca-2026.docx`](pedro-candeias-projeto-mestrado-mdddp-ipca-2026.docx) | Versão institucional anterior à revisão académica integral; deve ser conservada como referência histórica. |
| [`CHANGELOG.md`](CHANGELOG.md) | Registo cronológico das alterações realizadas. |
| [`AGENTS.md`](AGENTS.md) | Regras obrigatórias de edição, cópias de segurança, bibliografia, exportação e organização. |

Os ficheiros `projecto-completo-sem-repetições.docx`, `parametros-validacao-0.4.29.*` e outros documentos datados são derivados históricos ou documentos de verificação. Não substituem o manuscrito revisto.

## Anexos e suplementos

Os três anexos integram o manuscrito consolidado e mantêm fontes editáveis próprias em `sources/manuscript/annexes/`.

| Anexo ou suplemento | Conteúdo | Fonte editável |
| --- | --- | --- |
| Anexo A | Extracção, normalização, cobertura e limitações dos dados antropométricos | [`data_extraction_explained.md`](sources/manuscript/annexes/data_extraction_explained.md) |
| Anexo B | Avaliação complementar do processo paramétrico e da interface HandFab | [`anexo_b_avaliacao_processo_interface_handfab.md`](sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.md) |
| Anexo C | Adaptação paramétrica dos modelos Flexy Beast, Cyborg Beast, Paraglider Hand e UnLimbited Phoenix | [`anexo_c_adaptacao_parametrica_modelos.md`](sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.md) |
| Suplemento antropométrico 14.67.0 | Três CSV, dois geradores, verificações e somas SHA-256 | [`dados_antropometricos_v14.67.0/`](sources/manuscript/annexes/dados_antropometricos_v14.67.0/) |
| Dicionário de parâmetros 14.67.0 | Parâmetros, exemplo numérico, malhas e regeneração do suplemento | [`dicionario_parametros_v14.67.0/`](sources/manuscript/annexes/dicionario_parametros_v14.67.0/) |

Os DOCX e PDF autónomos dos Anexos B e C servem para revisão isolada. Quando estes anexos forem alterados, é necessário voltar a integrá-los no manuscrito principal e actualizar a paginação.

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
- `docs/`: relatórios de revisão, auditorias, exportações datadas e documentação de trabalho.
- `figuras/`: figuras integradas ou preparadas para o manuscrito.
- `tabelas/`: fontes editáveis e notas relativas às tabelas.
- `sources/docx/`: documentos DOCX de apoio.
- `sources/manuscript/`: anexos, suplementos, auditorias, versões de referência e notas de revisão do manuscrito.
- `sources/elicit/`: pesquisas, relatórios, sessões e notas de investigação organizadas por capítulo e secção.
- `material/`: biblioteca local de artigos, normas e materiais de referência; os originais não devem ser sobrescritos.
- `projecto_completo_bibliografia/`: PDFs associados à bibliografia e lista de publicações ainda sem cópia local.
- `projecto-completo_media/`: recursos gráficos usados pelo Markdown consolidado.
- `versions/`: cópias cronológicas criadas antes de alterações substantivas.
- `tools/`: conversores, verificadores e transformações documentais.
- `archive/` e `recovered/`: materiais históricos ou recuperados; não são fontes activas.

## Fluxo de edição do manuscrito

Antes de qualquer alteração substantiva:

```bash
git status --short
./tools/backup_docx.sh nome-da-alteracao
```

`backup_docx.sh` cria uma cópia datada de `projecto-completo.docx` em `versions/` e regenera `projecto-completo.pdf`. Para uma intervenção no documento IPCA revisto, deve ser criada também uma cópia datada de `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`.

Depois de uma alteração:

1. actualizar a versão no início de `projecto-completo.md`;
2. sincronizar o conteúdo com o DOCX revisto;
3. regenerar os PDF;
4. verificar índice, listas de tabelas e figuras, paginação, imagens e quebras;
5. acrescentar uma entrada no topo de `CHANGELOG.md`;
6. executar uma verificação final do pacote DOCX e do PDF.

O repositório contém transformações específicas em `tools/apply_*.py`. Estes scripts registam revisões já aplicadas; não devem ser executados indiscriminadamente sobre uma versão posterior sem confirmar que os seus pontos de inserção ainda correspondem ao documento actual.

### Integração dos Anexos B e C

As fontes editáveis dos anexos são convertidas para DOCX e integradas no documento IPCA por:

```bash
python3 tools/md_to_docx.py \
  sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.md \
  --output sources/manuscript/annexes/testes_plataforma/anexo_b_avaliacao_processo_interface_handfab.docx

python3 tools/md_to_docx.py \
  sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.md \
  --output sources/manuscript/annexes/adaptacao_parametrica_modelos/anexo_c_adaptacao_parametrica_modelos.docx

python3 tools/integrate_annexes_bc.py \
  --markdown projecto-completo.md \
  --docx pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx

python3 tools/apply_annex_local_indexes.py \
  pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx \
  --version 0.4.39
```

O integrador impede uma segunda inclusão acidental. O segundo comando conserva no índice principal apenas o título e a página inicial de cada anexo, deslocando as entradas detalhadas para índices próprios no início dos Anexos A, B e C. Depois destas operações, a paginação estática deve ser actualizada a partir de um PDF provisório com `tools/synchronise_docx_pagination.py`.

## Conversão e verificação documental

### Markdown para DOCX simples

```bash
python3 tools/md_to_docx.py projecto-completo.md --output docs/projecto-completo-revisao.docx
```

Este conversor cria um DOCX genérico. Não substitui, por si só, a formatação institucional do documento IPCA.

### DOCX para Markdown

```bash
python3 tools/docx_to_md.py projecto-completo.docx -o docs/projecto-completo-convertido.md
```

### DOCX para PDF

```bash
./tools/docx_to_pdf.sh
```

O comando converte `projecto-completo.docx` para `projecto-completo.pdf` através de LibreOffice em modo headless.

### Verificações rápidas

```bash
unzip -t projecto-completo.docx
pdfinfo projecto-completo.pdf
pdftotext -layout projecto-completo.pdf /tmp/projecto-completo.txt
rg -n "Anexo [ABC]|Tabela [BC]\.|Figura C\.1" /tmp/projecto-completo.txt
```

Os hooks versionados podem ser instalados com:

```bash
./tools/install_hooks.sh
```

Quando `projecto-completo.docx` faz parte de um commit, o hook `pre-commit` regenera e adiciona `projecto-completo.pdf`. Não usar `git commit --no-verify` quando o DOCX foi alterado.

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
