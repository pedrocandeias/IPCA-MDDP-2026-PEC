# Manuscrito HTML com citações e excertos

Abrir [`pedro_candeias_manuscrito_citacoes.html`](pedro_candeias_manuscrito_citacoes.html) num navegador. O documento funciona localmente, sem servidor, e incorpora as 34 imagens, os estilos, o JavaScript e os dados das citações. As ligações aos PDFs locais requerem a estrutura do repositório; as ligações DOI requerem acesso à Internet.

O asterisco junto de cada citação abre um painel com uma secção por obra, incluindo referência, DOI/URL, PDF local quando associado e excertos disponíveis. O painel suporta clique, teclado, Escape, clique exterior e ecrãs pequenos. Citações múltiplas mostram todas as obras no mesmo painel rolável.

As entradas do índice principal ligam aos títulos correspondentes. Os índices de figuras e tabelas ligam às legendas, e os índices dos anexos têm a entrada completa clicável. As siglas e os índices são organizados em folhas de leitura, com definições alinhadas, níveis hierárquicos e números de página numa coluna própria. As páginas indicadas nas entradas continuam a corresponder ao ODT; os rodapés numeram apenas as folhas de cada lista. A impressão inicia cada folha numa página nova. O número isolado «xx», artefacto da paginação original, é omitido. O módulo `tools/conversao/ligar_indices_html.py`, chamado pelo exportador, verifica destinos únicos e regista as correspondências em `ligacoes_indices.json`.

O bloco administrativo de declaração de reprodução, incluindo a assinatura e o título repetido antes do resumo, é omitido desta edição HTML. A capa e a folha de rosto idênticas do ODT são apresentadas uma única vez, com título, autor, orientador, instituição e data. A transformação é feita por `tools/conversao/preparar_leitura_html.py` e registada em `adaptacoes_leitura.json`; os documentos canónicos permanecem intactos.

## Fontes e reprodução

As 416 explicações fornecidas pelo autor estão guardadas em `docs/revisoes/bibliografia/explicacoes_citacoes_reescritas.txt` e `explicacoes_citacoes_versao_simples.txt`. Os dois ficheiros originais contêm explicações idênticas e são preservados. As revisões de 11/10/2026 estão em `docs/revisoes/bibliografia/explicacoes_citacoes_revistas.json`: 267 notas foram simplificadas para descrever o contributo da fonte, retirando comentários sobre o que não demonstra. Cada revisão guarda o texto original e o substituto. O painel apresenta «Relação com o texto» para cada fonte, seguida dos excertos e páginas; o bloco de avaliação histórica foi retirado da apresentação. Os registos históricos continuam nos dados de apoio.

Para importar futuras revisões dos TXT, executar `python3 tools/conversao/importar_explicacoes_citacoes.py` antes de regenerar o HTML. O importador verifica os identificadores, as referências, o contexto e a concordância das duas versões; guarda o resultado em `explicacoes_citacoes.json`. O exportador de HTML recusa reutilizar uma explicação se a passagem ou a referência tiver mudado. Depois da verificação dos TXT, o importador aplica as revisões editoriais e confirma que cada texto original ainda corresponde à ocorrência. Se os TXT forem alterados, é necessário reconciliar as revisões correspondentes. Este processo não constitui uma nova verificação das fontes.

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
- Os excertos mantêm a língua da fonte. A bibliografia e o corpo académico são preservados; as omissões da edição de leitura estão discriminadas em `adaptacoes_leitura.json`. Os índices conservam as páginas de referência da fonte.

## Ficheiros de apoio e verificação

- `recuperacao_matriz.json`: decisão de correspondência e estado da conferência de cada linha da matriz.
- `excertos_complementares.json`: transcrições de PDFs e notas específicas das pendências.
- `excertos_pendentes.csv`: ocorrências ainda sem excerto e contexto correspondente.
- `citacoes.json`: dados de cada ocorrência, referência e excerto, incluindo proveniência histórica.
- `explicacoes_citacoes.json`: explicações revistas por ocorrência e fonte, hashes dos TXT recebidos e do contexto ao qual se aplicam.
- `cobertura_excertos.csv`: cobertura por ocorrência e obra, com secção da auditoria e pontuação de semelhança textual.
- `manifesto.json`: contagens, fontes e SHA-256 dos documentos lidos.
- `validacao.json`: verificação das adaptações declaradas e da preservação do restante texto, das 53 tabelas, das 34 imagens incorporadas, dos 269 controlos e das ligações a PDFs locais; testes de interação em Chromium, em computador e telemóvel.
- `previsualizacao_computador.png` e `previsualizacao_telemovel.png`: verificação visual do painel com duas fontes.

A edição inicial foi confrontada com o HTML produzido a partir do Markdown sincronizado 0.4.114. Na edição de leitura, a comparação desconta apenas o bloco administrativo omitido e os elementos de apresentação declarados em `adaptacoes_leitura.json`. O painel foi testado também com quatro referências, fecho por Escape, reposição do foco e ausência de erros JavaScript.
