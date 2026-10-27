# Dissertação de mestrado · Pedro Candeias

**[Página do projeto — Português](https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/)** · **[English](https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/en.html)**

**[Ler a dissertação](https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/manuscrito.html)** · **[Descarregar PDF](https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/tese.pdf)** · **[Explora o HandFab](https://handfab.pedrocandeias.net/)**

Este repositório público reúne a dissertação, os anexos e suplementos, as figuras, a bibliografia, os dados de apoio e os recursos necessários à sua consulta:

> **Integração do Design e da Inteligência Artificial em Processos Paramétricos para o Desenvolvimento de Próteses de Membros Superiores em Impressão 3D**

Autor: Pedro Miguel Candeias da Silva

Orientador: Professor Doutor Demétrio Ferreira Matos

Mestrado em Design e Desenvolvimento de Produto · IPCA · 2026

## Documentos principais

O ODT de referência foi gravado em **25/10/2026 às 20h30**, no ficheiro com identificador `23102026-1047`. O PDF correspondente tem **224 páginas**. Os endereços públicos da dissertação e do PDF mantêm-se.

| Documento | Conteúdo |
| --- | --- |
| [Dissertação — PDF](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_23102026-1047.pdf) | Documento paginado para leitura e descarga. |
| [Dissertação — ODT](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_23102026-1047.odt) | Fonte editável do PDF atual. |
| [Dissertação — Word (DOCX)](docs/documentos/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_04102026-1955-pangram.docx) | Versão Word mais recente disponível, gravada em 05/10/2026; anterior ao ODT/PDF atual. |
| [Bibliografia e PDFs de apoio](material/bibliografia/) | Biblioteca consolidada mantida no repositório público. |
| [Dissertação — Markdown](pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md) | Representação textual com fonte e revisão identificadas no próprio ficheiro. |
| [Dissertação — leitura online](https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/manuscrito.html) | Leitura com 268 citações interativas, 425 ligações nos índices, listas contínuas e regresso das notas de rodapé. Os PDFs da biblioteca consolidada ficam em `material/bibliografia/`; outras fontes de trabalho podem requerer acesso à investigação privada. A edição online conserva referências, excertos e DOI/URL. |
| [Apresentação — PowerPoint](docs/defesa/apresentacao/apresentacao_defesa.pptx) · [PDF](docs/defesa/apresentacao/apresentacao_defesa.pdf) | Apresentação da defesa, com notas de fala no PPTX. |
| [Guião falado — ODT](docs/defesa/apresentacao/guiao_falado.odt) · [PDF](docs/defesa/apresentacao/guiao_falado.pdf) | Guião autónomo de apoio à apresentação. |
| [Preparação da defesa — ODT](docs/defesa/preparacao_defesa_bernardo_providencia.odt) · [PDF](docs/defesa/preparacao_defesa_bernardo_providencia.pdf) | Caderno de preparação e fundamentação das respostas. |
| [Perguntas do júri — ODT](docs/defesa/perguntas_juri.odt) · [PDF](docs/defesa/perguntas_juri.pdf) | Perguntas e respostas para preparação da defesa. |

## Anexos e suplementos

Os Anexos A–D integram a dissertação e conservam fontes editáveis em [`componentes/anexos/`](componentes/anexos/).

| Conteúdo | Pasta |
| --- | --- |
| Dados antropométricos | [`suplementos/01_dados_antropometricos/`](suplementos/01_dados_antropometricos/) |
| Avaliação técnica da plataforma | [`suplementos/02_avaliacao_plataforma/`](suplementos/02_avaliacao_plataforma/) |
| Dicionário de parâmetros e percurso de configuração | [`suplementos/03_parametrizacao_percurso/`](suplementos/03_parametrizacao_percurso/) |
| Preparação para impressão e protótipos | [`suplementos/04_preparacao_impressao_prototipos/`](suplementos/04_preparacao_impressao_prototipos/) |

O [guia dos suplementos](suplementos/guia_dos_suplementos.md) descreve os quatro conjuntos. As figuras e tabelas da dissertação encontram-se em [`componentes/`](componentes/).

## HandFab e ferramentas

O [HandFab](https://handfab.pedrocandeias.net/) é o protótipo de investigação desenvolvido para a configuração paramétrica de próteses de membros superiores. O código e a documentação mantêm-se no [repositório da aplicação](https://github.com/pedrocandeias/ai-parametric-prosthetic-hand-generator).

As ferramentas bibliográficas têm repositórios próprios: [Mendeley Cite for LibreOffice](https://github.com/pedrocandeias/mendeley-libreoffice), [Mendeley Library Tools](https://github.com/pedrocandeias/mendeley-tools) e [Mendeley Downloader](https://github.com/pedrocandeias/mendeley-downloader). Os geradores e scripts internos deste projeto ficam no submódulo privado; o [guia de acesso](docs/investigacao_privada.md) explica a configuração local.

## Organização pública e investigação privada

- `componentes/` e `suplementos/`: figuras, anexos e dados de apoio à dissertação.
- `docs/documentos/` e `docs/defesa/`: documentos disponibilizados para consulta.
- `material/bibliografia/`: bibliografia e PDFs de apoio mantidos públicos.
- `tools/`: acesso às ferramentas externas e preparação opcional do ambiente privado.
- `investigacao_privada/`: submódulo de [investigação e arquivo](https://github.com/pedrocandeias/IPCA-MDDP-2026-PEC-investigacao), com acesso restrito.

Os relatórios Elicit, os restantes materiais de investigação, as notas, revisões, rascunhos, versões antigas, cópias de segurança e geradores passaram para o repositório privado. A pasta `material/bibliografia/` mantém-se pública. `archive/` foi retirado da raiz pública. Não é necessário obter o submódulo privado para ler os documentos, consultar o site ou descarregar os suplementos.

Para trabalhar com a investigação, dispondo de autorização:

```bash
git submodule update --init --checkout investigacao_privada
python3 tools/manutencao/preparar_investigacao_privada.py
```

O submódulo privado tem atualização automática desativada para não impedir a clonagem pública. Alguns ficheiros grandes usam Git LFS. O [guia de acesso à investigação](docs/investigacao_privada.md) explica a configuração local e a atualização do apontador do submódulo.

A separação altera a versão atual do repositório. O histórico público anterior foi preservado e pode continuar a conter ficheiros anteriormente publicados.

## Publicação do site

O GitHub Pages publica os ficheiros estáticos da branch `gh-pages`. As capturas de teste, validações, dados de preparação e cópias intermédias de publicação ficam no repositório privado; não são necessários para visitar o site. A branch de publicação não contém submódulos privados.

```bash
# Atualizar as páginas e os estilos sem substituir os documentos da defesa:
python3 tools/conversao/preparar_html_publicacao.py --preserve-defense
```

Os comandos de geração ficam disponíveis depois de inicializar o submódulo privado e preparar as ligações locais. Regenerar o HTML anotado a partir do ODT requer também os dados da investigação privada. As fontes, o procedimento completo, os manifestos e os registos de verificação estão no repositório privado. O [guia de acesso](docs/investigacao_privada.md) explica como obter o ambiente de autoria. Para leitura, usar o site ou os documentos públicos da tabela acima.

As regras de edição encontram-se em [`AGENTS.md`](AGENTS.md); as alterações são registadas em [`CHANGELOG.md`](CHANGELOG.md).
