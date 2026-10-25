# Apresentação da defesa

Versão 1.6. 25/10/2026. Mestrado em Design e Desenvolvimento de Produto, Universidade Politécnica do Cávado e do Ave (UPCA).

- [Apresentação editável em PPTX](apresentacao_defesa.pptx).
- [Apresentação em PDF](apresentacao_defesa.pdf).
- [As minhas notas para cada diapositivo (ODT)](guiao_falado.odt), [PDF](guiao_falado.pdf) e [fonte editável Markdown](guiao_falado.md).
- [Guião de preparação](../guiao_apresentacao.md).

Os diapositivos 1 a 23 constituem o percurso principal, com metas de tempo que somam 20 minutos. Os diapositivos 24 a 30 são de apoio à discussão. Todos incluem notas pessoais com uma proposta de fala em «O que quero dizer» e lembretes de ensaio em «Lembrar-me». As referências ficam em «Fontes para consulta». Os primeiros 23 incluem ainda «Se precisar de desenvolver», com exemplos e explicações de apoio para o treino de 30 minutos. Estes apontamentos opcionais podem ser adaptados à fala; os lembretes não se leem ao júri. A fala principal tem 2164 palavras e os acrescentos têm 1210. Estas durações precisam de ser confirmadas por ensaio, incluindo pausas e explicação das imagens.

A narrativa começa pela motivação do desenvolvimento: barreiras de acesso a próteses adaptadas, especialmente em contextos de baixos e médios rendimentos, e a possibilidade de explorar modelos abertos e impressão 3D. Apresenta depois o problema, os objetivos e a metodologia, incluindo a integração de IA na investigação e o percurso de pesquisa e agregação de bibliografia com Elicit. Seguem-se o HandFab, os casos Paraglider e Phoenix e os resultados técnicos. As imagens são capturas e fotografias existentes no manuscrito e nos suplementos. A sequência de interface é ilustrativa, não uma demonstração ao vivo.

O diapositivo 5 apresenta o objetivo geral e uma síntese dos sete objetivos específicos da secção 1.3 do manuscrito. Os diapositivos anteriores foram mantidos e renumerados; as metas de tempo foram redistribuídas para conservar os 20 minutos. A capa utiliza o logótipo oficial da UPCA em português.

## Critério de redação

A revisão de estilo revê títulos, texto projetado e fala para evitar tríades retóricas, travessões e fórmulas de contraste enfático. As explicações ligam cada decisão ao resultado observado. As perguntas aprovadas mantêm a redação integral no apoio, assim como os dados e as enumerações técnicas necessárias. O diapositivo 14 mostra a interface de assistência de IA; o percurso é explicado nas notas.

A versão 1.4 reescreveu as notas como apontamentos pessoais do autor para o ensaio, com frases naturais em primeira pessoa e lembretes concretos. Nessa versão, o texto projetado dos 25 diapositivos foi preservado.

A versão 1.4.1 explicita, na nota opcional do diapositivo 3, a diferença entre verificação técnica e avaliação da experiência de utilização.

A versão 1.4.2 conserva a edição pessoal dos apontamentos dos diapositivos 1 e 2 e a clarificação do diapositivo 3, sincronizando o guião com as notas do PPTX.

## Fontes e ficheiros

### Critério de seleção das referências para a exposição

Os diapositivos 6 a 12 tornam explícita a relação entre as decisões do projeto e a fundamentação usada. A seleção privilegia obras já usadas no manuscrito com uma função direta no argumento da apresentação; não constitui uma nova revisão sistemática nem uma reconstrução da ordem em que o autor conheceu as obras.

| Referências | Função na exposição | Limite da atribuição |
|---|---|---|
| Cross (1982) | Enquadrar formas de conhecimento próprias do design. | A aplicação ao HandFab é uma interpretação do projeto; o autor não estudou este protótipo. |
| Frayling; Zimmerman et al. (2007) | Enquadrar investigação através do desenvolvimento e análise de artefactos. | Construir software não demonstra, por si só, uma contribuição de investigação. |
| Fischer et al. (2004) | Discutir condições de modificação e o espaço de configuração. | Parâmetros editáveis não demonstram participação ou codesign. |
| Design Council (2007) | Explicar a organização dos momentos de exploração e escolha. | Distinguir organização do processo de método de avaliação dos resultados. |
| Manero et al. (2019); Cabibihan et al. (2021) | Contextualizar próteses impressas em 3D e a necessidade de avaliar funcionalidade e durabilidade. | Os resultados daqueles estudos não validam os modelos produzidos neste projeto. |
| Gordon et al. (1989; 2014); TU Delft, DINED (s.d.) | Identificar levantamentos e conjuntos usados como fontes antropométricas. | Distinguir ANSUR 1988 de ANSUR II e identificar separadamente os conjuntos DINED. |
| ISO 7250-1:2017 | Enquadrar a definição das medidas e dos pontos anatómicos. | Não implica que todas as fontes tenham seguido a mesma edição ou protocolo. |

As fontes foram conferidas no manuscrito de referência e nos PDFs locais de Cross, Fischer, Zimmerman, Manero e ISO 7250-1. A relação conceptual de Fischer foi também conferida no [registo institucional da publicação](https://research.manchester.ac.uk/en/publications/meta-design-a-manifesto-for-end-user-development/); o artigo de [Cabibihan et al. (2021)](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2020.594196/full) e a [descrição institucional dos conjuntos DINED](https://dined.io.tudelft.nl/en/database/introduction) foram consultados nas fontes primárias. A pendência relativa à entrada de Frayling mantém-se assinalada.

### Antropometria e contribuição da base local

O diapositivo 11 identifica as fontes e o significado das medidas; o diapositivo 12 mostra a tabela de perfis; as notas explicam a passagem dos estudos originais para a organização local e para a aplicação. A composição dos 100 perfis (97 importados em lote, dois por CSV e um criado manualmente) segue a secção 4.2 do ODT. Não se afirma uma correspondência automática entre uma linha e um perfil, nem que todos os perfis tenham a mesma via de entrada.

Conferida a compilação multipopulacional distribuída: 1790 linhas, incluindo 852 linhas DINED. Os ficheiros ANSUR completo e subconjunto são sobrepostos. Estes valores descrevem registos estatísticos e não participantes. A fonte de apoio é `suplementos/01_dados_antropometricos/descricao_do_suplemento_1.md`; os valores e os ficheiros do suplemento foram preservados.

### Motivação e metodologia na versão 1.6

O diapositivo 2 apresenta as dificuldades de acesso e personalização que motivaram o desenvolvimento do projeto. As secções 1.1–1.2 e a Lacuna 5 do estado da arte foram conferidas no ODT de 23/10/2026. As barreiras de custo, manutenção, adaptação e apoio especializado constituem o enquadramento da investigação; não se afirma uma redução de custos medida nem uma implantação em países de baixos rendimentos.

Os diapositivos 6–8 desenvolvem a metodologia. O Double Diamond organiza momentos de exploração e convergência; Research Through Design enquadra a aprendizagem documentada nos ciclos de desenvolvimento e avaliação. A IA é apresentada no apoio ao trabalho do investigador e na sugestão de parâmetros dentro do HandFab.

O percurso do Elicit liga pergunta, pesquisa, agregação, verificação dos originais e síntese bibliográfica. O exemplo provém do pacote local da secção 6.1: a distinção entre estudos de controlo de próteses e estudos de configuração com dados antropométricos, com resultados fora do foco registados na pesquisa 03. A existência de relatórios e sínteses automáticas não é apresentada como prova de uma revisão sistemática integral. O arquivo das sessões conserva fontes e exportações por secção.

Fontes locais desta revisão:

- `material/investigacao/elicit/capitulo-6/6.1/searches/search-03.md`;
- `material/investigacao/elicit/capitulo-6/6.1/reports/5aaf1fab-74a5-4a0b-a871-eadf2ec0e219/notes.md`;
- `material/investigacao/elicit/agent-sessions/INDEX.md`;
- declaração de utilização de IA e secções 1.1–1.2 e 3.1–3.3 do manuscrito.

São 23 diapositivos principais e sete de apoio. As metas mantêm 20 minutos, com distribuição ajustada e fala principal de 2164 palavras. O guião desenvolvido mantém a meta de 30 minutos. Estes tempos precisam de ensaio. As notas pessoais anteriormente editadas pelo autor nos diapositivos 1 e 2 foram conservadas, passando o antigo diapositivo 2 para o número 3. Criada cópia de segurança dos materiais de defesa antes da revisão em `docs/versoes/backups/defesa_2026-10-25_20-05-47_antes_motivacao_metodologia.zip`.

### Revisão visual da versão 1.5

O percurso principal passa a 20 diapositivos, com oito de apoio. O HandFab surge logo no problema de configuração. Capturas ampliadas mostram o catálogo, os perfis antropométricos, a assistência de IA, os parâmetros, as cores e a exportação. As fotografias da placa de impressão e das séries de peças precedem os resultados dimensionais. A montagem Phoenix passa para o percurso principal, com uma fotografia geral e um pormenor da articulação. As falhas da plataforma ficam disponíveis no apoio.

Os originais fotográficos foram copiados integralmente do Suplemento 4 para permitir ampliação com maior qualidade. Os enquadramentos das capturas são feitos no PPTX, preservando as imagens incorporadas. `imagens_diapositivos.json` regista as regiões utilizadas; `assets_manifesto.json` identifica os originais e os seus hashes. As fotografias não são tratadas como comparações históricas antes/depois ou como avaliação com participantes. As notas pessoais foram adaptadas às imagens e conservam as edições do autor.

### Proveniência dos ficheiros

A base da apresentação anterior é `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`; o PDF de paginação é `a30759_pedro-candeias-projeto-mestrado-mdddp-ipca-v10060211.pdf`. A primeira apresentação utilizou o ODT `…04102026-1955.odt`; a comparação dos parágrafos não encontrou diferenças textuais entre os dois ODT. A fonte corrente foi atualizada na preparação da fala. A proveniência histórica das imagens mantém a indicação do ficheiro de onde foram extraídas. As afirmações foram confrontadas com os documentos de preparação e os registos dos suplementos. O manuscrito não foi alterado.

- `gerar_apresentacao.py`: conteúdo visual, disposição gráfica e geração do gráfico dimensional; lê a fala de `guiao_falado.md` para atualizar as notas.
- `guiao_falado.md`: fonte autoritativa da fala, dos acrescentos opcionais e das indicações de apresentação dos 30 diapositivos.
- `exportar_guiao_falado.py`: leitura estruturada da fala e exportação ODT pelo Pandoc, com as famílias tipográficas e a página do caderno de preparação, texto de 12 pt e cada diapositivo iniciado em nova página. Verifica os 30 títulos e todos os parágrafos da fala na exportação.
- `tempos_fala.json`: contagens de palavras e estimativas explícitas de leitura, sem as confundir com ensaio cronometrado.
- `diapositivos.json`: texto das notas, títulos, fontes e tempos por diapositivo.
- `manifesto.json`: fontes locais, hashes SHA-256 e pendências.
- `assets_manifesto.json`: correspondência das imagens extraídas com as figuras e os membros do ZIP do ODT. As imagens em `assets/figura_*` foram copiadas desses membros sem alteração do conteúdo.
- `assets/upca_logo_oficial.svg` e `.png`: logótipo obtido da [página institucional de normas gráficas](https://ipca.pt/apresentacao/normas-graficas/), com SVG original preservado. A derivação PNG mantém cores e proporções; origem, hashes e método em `assets/upca_logo_proveniencia.json` e `preparar_logo_upca.py`.
- `assets/phoenix_montagem.jpg`: cópia da fotografia identificada no manifesto, proveniente do Suplemento 4.
- `assets/desvios_dimensionais.png` e `.svg`: gráfico calculado a partir do CSV de 72 medições; cada segmento representa mínimo e máximo de 12 valores de um modelo/material. É uma síntese descritiva, sem intervalos de confiança ou tolerâncias de aceitação.
- `resumo_dimensional.json`: valores numéricos apresentados no gráfico e no diapositivo de apoio.
- `verificacao.json`: contagem de páginas, presença das notas e do texto na exportação, limites dos objetos e hashes dos ficheiros verificados. A apresentação foi também inspecionada visualmente.

O formato é 16:9, com letra Liberation Sans. Textos e esquemas são editáveis no PPTX; fotografias e gráfico são imagens incorporadas. O PDF permite conferir a apresentação visual e não inclui as notas do apresentador.

## Regeneração

Dependências Python: `python-pptx`, `Pillow` e `matplotlib`. Usar um ambiente Python com estas bibliotecas; nesta sessão, `python-pptx` e as suas dependências foram instaladas em `/tmp/defesa_pptx_deps`, que o script usa como alternativa se a biblioteca não estiver disponível no ambiente. Esse diretório é temporário.

A partir da raiz do repositório:

```bash
python3 docs/defesa/apresentacao/gerar_apresentacao.py
python3 docs/defesa/apresentacao/exportar_guiao_falado.py
libreoffice -env:UserInstallation=file:///tmp/defesa_impress_preview --headless --convert-to 'pdf:impress_pdf_Export:{"UseTaggedPDF":{"type":"boolean","value":"false"}}' --outdir docs/defesa/apresentacao docs/defesa/apresentacao/apresentacao_defesa.pptx
libreoffice -env:UserInstallation=file:///tmp/defesa_fala_preview --headless --convert-to 'pdf:writer_pdf_Export:{"UseTaggedPDF":{"type":"boolean","value":"false"}}' --outdir docs/defesa/apresentacao docs/defesa/apresentacao/guiao_falado.odt
```

Antes de regenerar, transpor para `guiao_falado.md` quaisquer alterações pessoais feitas diretamente nas notas do PPTX. Na versão 1.4.2, o PDF foi exportado da edição mais recente do PPTX do autor, e a sincronização do guião foi conferida.

O gerador substitui os derivados da apresentação. As imagens extraídas são uma cópia da versão indicada no manifesto; não são extraídas novamente pelo gerador. Se forem alteradas no manuscrito, devem ser atualizadas juntamente com a sua proveniência. O gerador confere as 72 linhas, uma leitura por combinação, 12 valores por grupo e a soma dos tempos.

## Antes da versão final

Confirmar condições e data da prova. Alinhar a redação das conclusões com o registo de montagem Phoenix: existe observação de bancada de um espécime, embora algumas passagens do manuscrito a excluam do âmbito realizado. Conferir a entrada incompleta de Frayling na bibliografia. Ensaiar a exposição e decidir se haverá vídeo ou apresentação de peças.

Estas pendências são também registadas no manifesto e nas notas pertinentes. A sequência visual e as metas de tempo devem ser conferidas no ensaio.
