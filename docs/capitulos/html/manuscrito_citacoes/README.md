# Manuscrito HTML com citações e excertos

Abrir [`pedro_candeias_manuscrito_citacoes.html`](pedro_candeias_manuscrito_citacoes.html) num navegador. O documento funciona localmente, sem servidor, e incorpora as 34 imagens, os estilos, o JavaScript e os dados das citações. As ligações aos PDFs locais requerem a estrutura do repositório; as ligações DOI requerem acesso à Internet.

O asterisco junto de cada citação abre um painel com uma secção por obra, incluindo referência, DOI/URL, PDF local quando associado e excertos disponíveis. O painel suporta clique, teclado, Escape, clique exterior e ecrãs pequenos. Citações múltiplas mostram todas as obras no mesmo painel rolável.

## Fontes e reprodução

- Documento: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`.
- Excertos: `docs/revisoes/bibliografia/auditoria_referencias_texto_papers_061.md`.
- PDFs: inventário `docs/revisoes/manuscrito/sincronizacao_markdown_2026_10_10/bibliografia_local.json`, complementado pelos caminhos registados na auditoria.
- Gerador: `tools/conversao/exportar_html_citacoes.py`.
- Fontes de apresentação: `tools/conversao/html_citacoes/template.html`, `style.css` e `script.js`.

Executar a partir da raiz:

```bash
python3 tools/conversao/exportar_html_citacoes.py
```

Requer Python com `lxml` e Pandoc. O gerador reutiliza o conversor ODT existente sobre uma cópia temporária, recupera o conteúdo comprimido `MLO_DATA_*` em `meta.xml` e associa cada grupo ao marcador `MLO_C_*` em `content.xml`. O ODT, o Markdown canónico e o relatório de auditoria permanecem intactos. Não foi efetuada qualquer publicação externa.

## Cobertura e limites

- **265 asteriscos**: 239 citações identificadas pelos marcadores Mendeley e 26 citações textuais adicionais com associação autor–ano inequívoca.
- **412 associações a obras**, relativas a 157 registos bibliográficos; 108 citações reúnem várias obras, com um máximo de quatro.
- **174 associações com excertos históricos disponíveis** no Markdown da auditoria. As restantes mostram a referência e a indicação de ausência de excerto associado.
- A comparação textual identifica **51 associações** com passagem histórica semelhante. Este resultado não constitui uma validação substantiva da afirmação atual.
- Para as outras associações com excerto, o painel esclarece que se trata de material guardado para a mesma obra e permite consultar o texto auditado e a avaliação histórica.
- As secções da auditoria que juntam várias obras sem uma atribuição individual inequívoca dos excertos não são convertidas numa atribuição automática a uma delas.
- A deteção adicional de citações textuais exclui os índices e a bibliografia principal e recusa associações autor–ano ambíguas. Não se presume que todos os anos ou nomes escritos no documento sejam citações.
- Os excertos são reproduzidos na língua em que foram guardados, sem tradução nem invenção de passagens em falta. As referências dos painéis são compostas a partir dos metadados da citação; não dependem dos blocos repetidos da bibliografia impressa.
- A bibliografia repetida e os restantes textos do ODT são preservados no corpo HTML. Os índices conservam a paginação estática da fonte.

## Ficheiros de apoio e verificação

- `citacoes.json`: dados de cada ocorrência, referência e excerto, incluindo proveniência histórica.
- `cobertura_excertos.csv`: cobertura por ocorrência e obra, com secção da auditoria e pontuação de semelhança textual.
- `manifesto.json`: contagens, fontes e SHA-256 dos documentos lidos.
- `validacao.json`: verificação do texto integral, das 53 tabelas, das 34 imagens incorporadas, dos 265 controlos e das ligações a PDFs locais; testes de interação em Chromium, em computador e telemóvel.
- `previsualizacao_computador.png` e `previsualizacao_telemovel.png`: verificação visual do painel com duas fontes.

O texto do corpo foi confrontado integralmente com o HTML produzido a partir do Markdown sincronizado 0.4.114, ignorando apenas espaços de formatação e os asteriscos acrescentados. Não houve diferenças textuais. O painel foi testado também com quatro referências, fecho por Escape, reposição do foco e ausência de erros JavaScript.
