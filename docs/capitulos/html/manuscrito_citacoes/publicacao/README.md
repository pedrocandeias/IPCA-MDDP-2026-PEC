# Página do projeto e dissertação anotada

- Português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/>
- English: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/en.html>
- Dissertação em português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/manuscrito.html>

A página inicial apresenta a investigação e o repositório, com acesso ao manuscrito, à plataforma HandFab, ao respetivo código no GitHub e às ferramentas bibliográficas e documentais, incluindo a extensão independente [Mendeley Cite for LibreOffice](https://github.com/pedrocandeias/mendeley-libreoffice). As duas versões da apresentação são páginas HTML completas, ligadas por um seletor de língua; não dependem de JavaScript para leitura ou navegação.

## Aspeto visual

A homepage em português e inglês e o manuscrito usam a mesma base visual do HandFab: superfícies brancas, cinzentos neutros, botões escuros, contornos discretos e cantos arredondados. Os detalhes decorativos usam o gradiente violeta/rosa da aplicação. A tipografia sem serifas usa fontes do sistema, sem carregamentos externos; o manuscrito conserva espaçamento próprio para leitura longa. Os painéis das citações e o visualizador de imagens seguem o mesmo tema.

A referência é o código local de `ai-parametric-prosthetic-hand-generator/index.html` e `theme.css`, consultado em 13/10/2026. Os valores partilhados estão em `tools/conversao/tema_handfab.css`. O exportador incorpora esse CSS no HTML autónomo do manuscrito; a homepage carrega a cópia publicada em `assets/tema_handfab.css`. Os estilos de disposição de cada página permanecem nas respetivas pastas. A alteração visual preserva o texto e as ligações das duas línguas, o conteúdo do manuscrito e os dados das citações.

O índice lateral do manuscrito destaca a secção em leitura durante o scroll, com marcador violeta e `aria-current="location"`. O destaque acompanha a navegação por âncoras e mantém a entrada visível dentro do índice, sem deslocar o documento nem alterar o foco. Os asteriscos e as ações da homepage usam o violeta partilhado do tema; os botões têm letra de 18 px e o seletor de idioma apresenta PT/EN com nomes acessíveis completos.

## Fontes e geração

Os geradores e os ficheiros de configuração ficam no submódulo privado `investigacao_privada/`. Os caminhos abaixo são ligações locais preparadas pelo [script de acesso](../../../../../tools/manutencao/preparar_investigacao_privada.py), para quem tem autorização. O pacote `dist/` e a bibliografia consolidada mantêm-se públicos.

```bash
python3 tools/conversao/exportar_html_citacoes.py
python3 tools/conversao/preparar_html_publicacao.py
```

As fontes editáveis da apresentação encontram-se em `tools/conversao/homepage/`: `conteudo.json` contém os textos PT/EN, `template.html` a estrutura, `style.css` a apresentação e `lightbox.js`/`lightbox.css` o visualizador de imagens. O texto baseia-se no README deste repositório e nos guias das ferramentas. A fotografia é copiada, sem alterações, de `docs/defesa/apresentacao/assets/phoenix_montagem.jpg`, um registo da montagem experimental Phoenix do projeto.

Os documentos da defesa estão disponíveis em `docs/defesa/` no repositório. A homepage não apresenta uma secção nem ligações para a defesa. As cópias publicadas anteriormente mantêm os seus endereços diretos. A publicação copia apenas os oito ficheiros declarados em `DEFENSE_FILES`, de `docs/defesa/` para `dist/defesa/`. As perguntas do júri estão disponíveis nos endereços diretos `defesa/perguntas_juri.pdf` e `defesa/perguntas_juri.odt`. A pasta pessoal `guia_leitura_local/` está excluída desta lista e do Git.

O gerador escreve `dist/index.html`, `dist/en.html`, `dist/manuscrito.html`, `dist/tese.pdf` e os recursos partilhados em `dist/assets/`. O manuscrito deriva do HTML local validado e mantém os dados, as imagens e os painéis de citações. A lista de siglas e cada índice são contínuos, num único cartão, sem paginação nem cabeçalhos repetidos. A dedicatória tem secção própria, separada da declaração de utilização de IA. A versão de alojamento retira 405 ligações a PDFs locais, preservando referências, excertos e ligações DOI/URL. Os PDFs da biblioteca não integram o pacote.

O botão «Descarregar PDF» descarrega a última versão exportada do mesmo ODT que serve de fonte ao HTML, identificada em `../manifesto.json`. A publicação copia o PDF correspondente para `dist/tese.pdf`, regista a origem e o SHA-256 em `manifesto_publicacao.json` e inclui o hash na ligação para atualizar a cache quando o ficheiro mudar. O gerador exige que o ODT corresponda ao HTML e que o PDF tenha sido exportado após a última gravação do ODT. Para atualizar apenas o manuscrito e o PDF, preservando a homepage e os documentos da defesa já preparados, executar `python3 tools/conversao/preparar_html_publicacao.py --manuscript-only`.

As imagens da apresentação e as 34 imagens do manuscrito abrem uma lightbox acessível por clique ou teclado, com ajuste ao ecrã, tamanho original, deslocação e fecho por botão, Escape ou clique fora da imagem. O visualizador usa o ficheiro original disponível; não acrescenta resolução artificial.

`manifesto_publicacao.json` identifica as fontes e os hashes do HTML. `deploy_github.json` regista a publicação e a verificação.

## Redirecionamento da raiz

A raiz `https://pedrocandeias.github.io/` encaminha para a homepage deste projeto. A fonte encontra-se em `redirecionamento_raiz/`; a publicação usa o repositório separado `pedrocandeias/pedrocandeias.github.io`. O registo de verificação fica em `redirecionamento_github.json`.

## GitHub Pages

O GitHub Pages serve a raiz da branch `gh-pages`. Para atualizar, regenerar o pacote, copiar o conteúdo de `dist/` para uma cópia de trabalho dessa branch, atualizar o respetivo changelog, criar o commit e enviar a branch. O Pages publica automaticamente após o envio. O ficheiro `.nojekyll` deve permanecer na branch.

As alterações pendentes do manuscrito na branch `main` são independentes desta publicação. O README de `main` contém ligações para a apresentação e para o manuscrito.

## Excertos das citações

A publicação inclui 415 explicações reconciliadas com a versão atual, a partir das notas fornecidas pelo autor, apresentadas em «Relação com o texto», e 406 associações com excerto (auditoria Markdown, matriz histórica Excel e seis PDFs consultados diretamente). Nove associações permanecem sem transcrição, com notas específicas. Os painéis mostram a explicação correspondente a cada fonte, os excertos e as páginas, sem os caminhos internos nem o antigo bloco de avaliação histórica. Os registos de auditoria mantêm-se nos dados de apoio. Ver os relatórios em `../`.

## Edição de 25/10/2026

O pacote usa o manuscrito gravado em 25/10/2026, com 268 citações interativas, 425 ligações nos índices, 53 tabelas e 34 imagens. Inclui também a apresentação da defesa 1.6 e os guiões revistos. O manifesto da publicação identifica os ficheiros locais; `deploy_github.json` identifica separadamente a versão efetivamente publicada e a conferência dos endereços públicos.

## Terminologia e interface

A interface usa «dissertação» em português e «dissertation» em inglês. Os caminhos e identificadores internos com `manuscrito` são conservados para manter as ligações. O nome e a informação complementar do cabeçalho mantêm os tamanhos da homepage (19/14 px; nome a 18 px em telemóvel). Na edição de leitura, os botões do cabeçalho usam 22 px e a navegação lateral 20 px, passando a 18 px em telemóvel. «Início» tem fundo violeta claro, «Imprimir» fundo laranja claro e «Descarregar PDF» mantém o fundo violeta forte, com texto branco e ícone. Os botões do HandFab usam o mesmo gradiente violeta, rosa e laranja de `.handfab::before`, definido em `--brand-gradient`, com texto escuro. A altura do cabeçalho é tida em conta na navegação por âncoras.

Para regenerar as páginas e os recursos da interface sem substituir os documentos da defesa já preparados, executar `python3 tools/conversao/preparar_html_publicacao.py --preserve-defense`. A verificação da interface e as capturas estão identificadas em `../validacao_interface_dissertacao_2026_10_26.json`.
