# Página do projeto e manuscrito anotado

- Português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/>
- English: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/en.html>
- Manuscrito em português: <https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/manuscrito.html>

A página inicial apresenta a investigação e o repositório, com acesso ao manuscrito, à plataforma HandFab, ao respetivo código no GitHub e às ferramentas bibliográficas e documentais, incluindo a extensão independente [Mendeley Cite for LibreOffice](https://github.com/pedrocandeias/mendeley-libreoffice). As duas versões da apresentação são páginas HTML completas, ligadas por um seletor de língua; não dependem de JavaScript para leitura ou navegação.

## Fontes e geração

```bash
python3 tools/conversao/preparar_html_publicacao.py
```

As fontes editáveis da apresentação encontram-se em `tools/conversao/homepage/`: `conteudo.json` contém os textos PT/EN, `template.html` a estrutura, `style.css` a apresentação e `lightbox.js`/`lightbox.css` o visualizador de imagens. O texto baseia-se no README deste repositório e nos guias das ferramentas. A fotografia é copiada, sem alterações, de `docs/defesa/apresentacao/assets/phoenix_montagem.jpg`, um registo da montagem experimental Phoenix do projeto.

O gerador escreve `dist/index.html`, `dist/en.html`, `dist/manuscrito.html` e os recursos partilhados em `dist/assets/`. O manuscrito deriva do HTML local validado e mantém os dados, as imagens e os painéis de citações. A versão de alojamento retira 407 ligações a PDFs locais, preservando referências, excertos e ligações DOI/URL. Os PDFs da biblioteca não integram o pacote.

As imagens da apresentação e as 34 imagens do manuscrito abrem uma lightbox acessível por clique ou teclado, com ajuste ao ecrã, tamanho original, deslocação e fecho por botão, Escape ou clique fora da imagem. O visualizador usa o ficheiro original disponível; não acrescenta resolução artificial.

`manifesto_publicacao.json` identifica as fontes e os hashes do HTML. `deploy_github.json` regista a publicação e a verificação.

## GitHub Pages

O GitHub Pages serve a raiz da branch `gh-pages`. Para atualizar, regenerar o pacote, copiar o conteúdo de `dist/` para uma cópia de trabalho dessa branch, atualizar o respetivo changelog, criar o commit e enviar a branch. O Pages publica automaticamente após o envio. O ficheiro `.nojekyll` deve permanecer na branch.

As alterações pendentes do manuscrito na branch `main` são independentes desta publicação. O README de `main` contém ligações para a apresentação e para o manuscrito.

## Excertos das citações

A publicação inclui 416 explicações fornecidas pelo autor, apresentadas em «Relação com o texto», e 408 associações com excerto (auditoria Markdown, matriz histórica Excel e seis PDFs consultados diretamente). Oito associações permanecem sem transcrição, com notas específicas. Os painéis mostram a explicação correspondente a cada fonte, os excertos e as páginas, sem os caminhos internos nem o antigo bloco de avaliação histórica. Os registos de auditoria mantêm-se nos dados de apoio. Ver os relatórios em `../`.
