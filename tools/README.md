# Ferramentas e geradores

Os geradores do site, da dissertação, das figuras e da apresentação, os conversores e os scripts internos são mantidos no submódulo privado `investigacao_privada/`.

Para obter os comandos num posto autorizado:

```bash
git submodule update --init --checkout investigacao_privada
python3 tools/manutencao/preparar_investigacao_privada.py
```

As ligações locais permitem continuar a executar os comandos habituais, como `python3 tools/conversao/preparar_html_publicacao.py --preserve-defense`, a partir da raiz deste repositório. A documentação completa das ferramentas acompanha os geradores no privado.

O script público `manutencao/preparar_investigacao_privada.py` prepara e verifica essas ligações. Não é necessário inicializar o submódulo para ler a dissertação ou consultar os ficheiros já publicados.

As ferramentas externas mantêm os seus repositórios e associações próprias:

- [HandFab](https://github.com/pedrocandeias/ai-parametric-prosthetic-hand-generator)
- [Mendeley Library Tools](https://github.com/pedrocandeias/mendeley-tools)
- [Mendeley Downloader](https://github.com/pedrocandeias/mendeley-downloader)
- [Mendeley Cite for LibreOffice](https://github.com/pedrocandeias/mendeley-libreoffice)

Ver o [guia de acesso à investigação privada](../docs/investigacao_privada.md).
