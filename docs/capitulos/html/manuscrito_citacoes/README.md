# Manuscrito HTML com citações e excertos

Abrir [`pedro_candeias_manuscrito_citacoes.html`](pedro_candeias_manuscrito_citacoes.html) num navegador. O documento funciona localmente, sem servidor, e incorpora as 34 imagens, os estilos, o JavaScript e os dados das citações. As ligações aos PDFs locais requerem a estrutura do repositório; as ligações DOI requerem acesso à Internet.

O asterisco junto de cada citação abre um painel com uma secção por obra, incluindo referência, DOI/URL, PDF local quando associado e excertos disponíveis. O painel suporta clique, teclado, Escape, clique exterior e ecrãs pequenos. Citações múltiplas mostram todas as obras no mesmo painel rolável.

## Fontes e reprodução

- Documento: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`.
- Auditoria Markdown: `docs/revisoes/bibliografia/auditoria_referencias_texto_papers_061.md`.
- Matriz histórica: `material/bibliografia/auditoria_citacoes/referencias_evidencia_docx_2026-07-22.xlsx`.
- Excertos complementares conferidos diretamente em seis PDFs: `excertos_complementares.json`, com página, hash e nota de leitura.
- PDFs: inventário `docs/revisoes/manuscrito/sincronizacao_markdown_2026_10_10/bibliografia_local.json`, complementado pelos caminhos registados na auditoria.
- Gerador: `tools/conversao/exportar_html_citacoes.py`.
- Fontes de apresentação: `tools/conversao/html_citacoes/template.html`, `style.css` e `script.js`.

Executar a partir da raiz:

```bash
python3 tools/conversao/exportar_html_citacoes.py
```

Requer Python com `lxml`, `openpyxl`, `PyMuPDF` e Pandoc. O gerador reutiliza o conversor ODT existente sobre uma cópia temporária, recupera o conteúdo comprimido `MLO_DATA_*` em `meta.xml` e associa cada grupo ao marcador `MLO_C_*` em `content.xml`. O ODT, o Markdown canónico e o relatório de auditoria permanecem intactos. A versão publicada e os recursos da homepage encontram-se em `publicacao/`; executar também `python3 tools/conversao/preparar_html_publicacao.py` após regenerar o HTML local.

## Cobertura e limites

- **269 asteriscos**: 239 citações identificadas pelos marcadores Mendeley e 30 citações textuais com associação autor–ano inequívoca. A normalização de travessões e caracteres diacríticos recuperou quatro controlos adicionais.
- **416 associações a obras**, relativas a 157 registos; 108 citações reúnem várias obras, com um máximo de quatro.
- **408 associações com excerto**: 290 usam a auditoria Markdown, 109 usam a matriz histórica Excel e nove usam as seis consultas diretas de PDFs complementares. A versão anterior tinha 174 associações preenchidas.
- Os excertos Markdown existentes são preferidos; a matriz completa as obras sem excerto recuperado. Cada linha da matriz é associada por DOI ou título inequívoco, com rejeição de conflitos. A página do PDF, a linha da folha, o método de recuperação e a classificação histórica ficam identificados.
- A presença do excerto no texto extraído da página do PDF é conferida quando possível. Uma extração não coincidente mantém a transcrição histórica com essa limitação explícita; não se afirma que houve uma nova revisão visual.
- Os excertos complementares são conferidos automaticamente na página indicada e pelo hash do PDF a cada geração. As notas de leitura delimitam o suporte. A discrepância entre Østlie (2011), citado no ODT, e Østlie (2012), identificado na auditoria como origem das percentagens de rejeição, aparece no painel sem alterar o manuscrito.
- **Oito associações, relativas a sete obras, continuam sem excerto**: Adel (2020), Gonzalez Avila (2024; duas ocorrências), ASTM (2024), Li (2020), daprice, ISO/TC 168 e DINED. Cada painel apresenta uma nota específica; não é preenchido com uma transcrição de outra obra. Ver `excertos_pendentes.csv`.
- A semelhança entre passagens e a presença de um excerto no PDF não constituem confirmação de que toda a afirmação atual é sustentada. As avaliações da matriz conservam a sua proveniência histórica, incluindo as classificações assistidas por software.
- Os excertos mantêm a língua da fonte. A bibliografia repetida e o texto integral do ODT são preservados. Os índices conservam a paginação estática da fonte.

## Ficheiros de apoio e verificação

- `recuperacao_matriz.json`: decisão de correspondência e estado da conferência de cada linha da matriz.
- `excertos_complementares.json`: transcrições de PDFs e notas específicas das pendências.
- `excertos_pendentes.csv`: ocorrências ainda sem excerto e contexto correspondente.
- `citacoes.json`: dados de cada ocorrência, referência e excerto, incluindo proveniência histórica.
- `cobertura_excertos.csv`: cobertura por ocorrência e obra, com secção da auditoria e pontuação de semelhança textual.
- `manifesto.json`: contagens, fontes e SHA-256 dos documentos lidos.
- `validacao.json`: verificação do texto integral, das 53 tabelas, das 34 imagens incorporadas, dos 269 controlos e das ligações a PDFs locais; testes de interação em Chromium, em computador e telemóvel.
- `previsualizacao_computador.png` e `previsualizacao_telemovel.png`: verificação visual do painel com duas fontes.

O texto do corpo foi confrontado integralmente com o HTML produzido a partir do Markdown sincronizado 0.4.114, ignorando apenas espaços de formatação e os asteriscos acrescentados. Não houve diferenças textuais. O painel foi testado também com quatro referências, fecho por Escape, reposição do foco e ausência de erros JavaScript.
