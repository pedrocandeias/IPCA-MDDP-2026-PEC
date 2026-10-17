# Redirecionamento da página raiz

A raiz `https://pedrocandeias.github.io/` encaminha para `https://pedrocandeias.github.io/IPCA-MDDP-2026-PEC/index.html`.

O ficheiro `index.html` é publicado na raiz da branch `main` do repositório `pedrocandeias/pedrocandeias.github.io`, juntamente com `.nojekyll`. O GitHub Pages usa essa branch como origem. Esta pasta conserva a fonte do redirecionamento; não integra o pacote `dist/` do site do projeto.

O redirecionamento usa `location.replace`, preservando parâmetros e fragmentos quando o JavaScript está disponível. O HTML inclui também `meta refresh` e uma ligação direta para navegação sem JavaScript. Trata-se de um redirecionamento no navegador; o GitHub Pages serve o documento HTML com estado 200, sem uma resposta HTTP 301 configurável por este ficheiro.

Para atualizar o destino, rever o URL no script, no `meta refresh`, na ligação canónica e na ligação visível, copiar o ficheiro para o repositório da raiz e fazer commit e push. A confirmação da publicação fica registada em `../redirecionamento_github.json`.
