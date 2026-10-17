# Página do projeto e manuscrito anotado

- Português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/>
- English: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/en.html>
- Manuscrito em português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/manuscrito.html>

A página inicial apresenta a investigação e o repositório, com acesso ao manuscrito, à plataforma HandFab, ao respetivo código no GitHub e às ferramentas bibliográficas e documentais, incluindo a extensão independente [Mendeley Cite for LibreOffice](https://github.com/pedrocandeias/mendeley-libreoffice). As duas versões da apresentação são páginas HTML completas, ligadas por um seletor de língua; não dependem de JavaScript para leitura ou navegação.

## Aspeto visual

A homepage em português e inglês e o manuscrito usam a mesma base visual do HandFab: superfícies brancas, cinzentos neutros, botões escuros, contornos discretos e cantos arredondados. Os detalhes decorativos usam o gradiente violeta/rosa da aplicação. A tipografia sem serifas usa fontes do sistema, sem carregamentos externos; o manuscrito conserva espaçamento próprio para leitura longa. Os painéis das citações e o visualizador de imagens seguem o mesmo tema.

A referência é o código local de `ai-parametric-prosthetic-hand-generator/index.html` e `theme.css`, consultado em 13/10/2026. Os valores partilhados estão em `tools/conversao/tema_handfab.css`. O exportador incorpora esse CSS no HTML autónomo do manuscrito; a homepage carrega a cópia publicada em `assets/tema_handfab.css`. Os estilos de disposição de cada página permanecem nas respetivas pastas. A alteração visual preserva o texto e as ligações das duas línguas, o conteúdo do manuscrito e os dados das citações.

O índice lateral do manuscrito destaca a secção em leitura durante o scroll, com marcador violeta e `aria-current="location"`. O destaque acompanha a navegação por âncoras e mantém a entrada visível dentro do índice, sem deslocar o documento nem alterar o foco. Os asteriscos e as ações da homepage usam o violeta partilhado do tema; os botões têm letra de 18 px e o seletor de idioma apresenta PT/EN com nomes acessíveis completos.

## Fontes e geração

```bash
python3 tools/conversao/exportar_html_citacoes.py
python3 tools/conversao/preparar_html_publicacao.py
```

As fontes editáveis da apresentação encontram-se em `tools/conversao/homepage/`: `conteudo.json` contém os textos PT/EN, `template.html` a estrutura, `style.css` a apresentação e `lightbox.js`/`lightbox.css` o visualizador de imagens. O texto baseia-se no README deste repositório e nos guias das ferramentas. A fotografia é copiada, sem alterações, de `docs/defesa/apresentacao/assets/phoenix_montagem.jpg`, um registo da montagem experimental Phoenix do projeto.

Os documentos da defesa estão disponíveis em `docs/defesa/` no repositório. A homepage não apresenta uma secção nem ligações para a defesa. As cópias publicadas anteriormente mantêm os seus endereços diretos. A publicação copia apenas os oito ficheiros declarados em `DEFENSE_FILES`, de `docs/defesa/` para `dist/defesa/`. As perguntas do júri estão disponíveis nos endereços diretos `defesa/perguntas_juri.pdf` e `defesa/perguntas_juri.odt`. A pasta pessoal `guia_leitura_local/` está excluída desta lista e do Git.

O gerador escreve `dist/index.html`, `dist/en.html`, `dist/manuscrito.html` e os recursos partilhados em `dist/assets/`. O manuscrito deriva do HTML local validado e mantém os dados, as imagens e os painéis de citações. A versão de alojamento retira 407 ligações a PDFs locais, preservando referências, excertos e ligações DOI/URL. Os PDFs da biblioteca não integram o pacote.

As imagens da apresentação e as 34 imagens do manuscrito abrem uma lightbox acessível por clique ou teclado, com ajuste ao ecrã, tamanho original, deslocação e fecho por botão, Escape ou clique fora da imagem. O visualizador usa o ficheiro original disponível; não acrescenta resolução artificial.

`manifesto_publicacao.json` identifica as fontes e os hashes do HTML. `deploy_github.json` regista a publicação e a verificação.

## Redirecionamento da raiz

A raiz `https://pedrocandeias.github.io/` encaminha para a homepage deste projeto. A fonte encontra-se em `redirecionamento_raiz/`; a publicação usa o repositório separado `pedrocandeias/pedrocandeias.github.io`. O registo de verificação fica em `redirecionamento_github.json`.

## GitHub Pages

O GitHub Pages serve a raiz da branch `gh-pages`. Para atualizar, regenerar o pacote, copiar o conteúdo de `dist/` para uma cópia de trabalho dessa branch, atualizar o respetivo changelog, criar o commit e enviar a branch. O Pages publica automaticamente após o envio. O ficheiro `.nojekyll` deve permanecer na branch.

As alterações pendentes do manuscrito na branch `main` são independentes desta publicação. O README de `main` contém ligações para a apresentação e para o manuscrito.

## Excertos das citações

A publicação inclui 416 explicações fornecidas pelo autor, apresentadas em «Relação com o texto», e 408 associações com excerto (auditoria Markdown, matriz histórica Excel e seis PDFs consultados diretamente). Oito associações permanecem sem transcrição, com notas específicas. Os painéis mostram a explicação correspondente a cada fonte, os excertos e as páginas, sem os caminhos internos nem o antigo bloco de avaliação histórica. Os registos de auditoria mantêm-se nos dados de apoio. Ver os relatórios em `../`.
