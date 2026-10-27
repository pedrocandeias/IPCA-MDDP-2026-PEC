# Investigação e arquivo privados

O repositório [IPCA-MDDP-2026-PEC-investigacao](https://github.com/pedrocandeias/IPCA-MDDP-2026-PEC-investigacao) é **privado** e está associado em `desenvolvimento/` como submódulo Git. O nome, o endereço e o commit associado são públicos; o conteúdo requer autorização.

Reúne também as capturas de teste, validações e ficheiros de preparação da publicação, além do material de investigação (exceto `material/bibliografia/`, que fica público), os relatórios Elicit, `docs/versoes/`, `docs/revisoes/`, os registos de desenvolvimento, notas, guias de investigação, rascunhos de capítulos e `archive/`. Os geradores do site, das figuras, dos documentos e da apresentação, com a respetiva configuração, estão também no privado. Os documentos atuais de leitura, a bibliografia consolidada, figuras, anexos e suplementos mantêm-se no repositório público.

## Obter o material autorizado

```bash
git submodule update --init --checkout desenvolvimento
python3 tools/manutencao/preparar_investigacao_privada.py
```

O preparador também atualiza as ligações locais que ainda apontem para o antigo nome `investigacao_privada/`, preservando os caminhos ocupados por ficheiros ou pastas.

A opção `--checkout` é intencional: a atualização automática deste submódulo está desativada em `.gitmodules`, para que uma clonagem pública não tente obter o conteúdo privado.

O script cria ligações locais como `material/investigacao/`, `docs/versoes/` e `tools/conversao/` para as pastas correspondentes do submódulo. Essas ligações são ignoradas no repositório público. Assim, os geradores e os procedimentos de cópia de segurança continuam a usar os caminhos existentes. `archive/` conserva-se apenas dentro do submódulo.

Para verificar as ligações sem alterar nada:

```bash
python3 tools/manutencao/preparar_investigacao_privada.py --check
```

Sete ficheiros grandes da importação inicial usam Git LFS. Se forem necessários, instalar Git LFS e executar:

```bash
git -C desenvolvimento lfs pull
```

## Guardar alterações

As alterações feitas através das ligações locais pertencem ao submódulo. Gravar e enviar primeiro nesse repositório; depois atualizar o apontador no público:

```bash
git -C desenvolvimento status
# Selecionar os ficheiros de investigação a guardar e criar o respetivo commit.
git -C desenvolvimento push origin main
git add desenvolvimento
# Criar e enviar o commit do apontador no repositório público.
```

O manifesto de transferência, com tamanhos e SHA-256, fica em `desenvolvimento/docs/migracao/manifesto_2026_10_26.json`. Os originais foram preservados. Caches de aplicações, credenciais e ficheiros temporários não integram a importação versionada.

O site é publicado a partir de `gh-pages`, que não inclui o submódulo. O processo de publicação não necessita de acesso ao repositório privado para servir o pacote já preparado.

A separação não reescreveu o histórico público anterior. A retirada das pastas da versão atual não elimina os ficheiros que já constavam de commits públicos antigos.

A pasta de trabalho `docs/capitulos/html/manuscrito_citacoes/` é privada e reaparece localmente como ligação de compatibilidade. Não é necessária no repositório público: o site usa as cópias estáticas existentes na branch `gh-pages`.
