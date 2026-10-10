# Sincronização do Markdown com o ODT — 10 de outubro de 2026

O manuscrito `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md` foi atualizado para **0.4.114** a partir de `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`. O ODT e o PDF de referência foram preservados. Não se efetuou uma revisão de conteúdo nem uma nova exportação DOCX/PDF.

## Proveniência e reprodução

Cópia de segurança do Markdown anterior: `docs/versoes/backups/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto-2026-10-10_17-01-10-antes_sincronizacao_odt_0.4.114.md`.

```bash
python3 tools/conversao/sincronizar_manuscrito_odt.py \
  pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt \
  --output /tmp/manuscrito_sincronizado.md \
  --assets componentes/figuras/manuscrito_odt_2026_10_10 \
  --report /tmp/conversao_manuscrito.json \
  --version 0.4.114
```

Os caminhos das imagens destinam-se ao Markdown colocado na raiz. Para uma futura substituição do ficheiro canónico, criar primeiro nova cópia de segurança e atualizar a versão e o CHANGELOG.

Conversão com Pandoc 3.1.3 e pré-processamento de uma cópia temporária do XML: recuperação do texto visível dos controlos do LibreOffice; recuperação das linhas de cabeçalho das tabelas que o leitor ODT omitia; materialização dos índices; normalização das listas que envolviam títulos de capítulo; remoção das citações em bloco artificiais decorrentes dos estilos IPCA. Os espaços nos limites de itálicos e negritos foram reposicionados para garantir Markdown válido.

As 34 imagens foram extraídas diretamente do ZIP ODT, sem alteração, para `componentes/figuras/manuscrito_odt_2026_10_10/`. O manifesto nessa pasta regista a origem e o SHA-256 de cada imagem. O ficheiro `conversao.json` regista o SHA-256 da fonte e as contagens da estrutura convertida.

## Verificação

- Nove capítulos principais e quatro anexos presentes.
- 53 tabelas, 34 imagens e 11 notas de rodapé recuperadas.
- Correspondência textual dos 2287 parágrafos com mais de 35 caracteres, incluindo texto das tabelas e bibliografia, após normalização dos espaços e dos marcadores de notas.
- Índices preservados como texto estático, com a paginação do documento de origem. As ligações internas que o leitor não conseguiu resolver foram convertidas em texto, preservando o rótulo e a página; os identificadores constam de `conversao.json`.
- A apresentação paginada continua a ser a do ODT/PDF. O Markdown não reproduz margens, tipos de letra, posicionamento flutuante ou campos atualizáveis do Writer.

## Bibliografia e pendências da fonte

O ODT contém **283 parágrafos bibliográficos**, com **158 textos distintos** e **125 ocorrências repetidas**. A repetição também é visível no PDF de referência. Foi preservada no Markdown, para que esta sincronização não substitua uma decisão editorial sobre a bibliografia.

Uma das entradas encontra-se truncada: `Baumann, Mearch and Development Academy. https://doi.org/10.37868/sei.v5i1.id185`. Esta entrada e eventuais variantes de metadados permanecem por rever no ODT; a sincronização não certifica conformidade integral com APA 7.

O inventário de PDFs foi atualizado em `material/bibliografia/pdfs_em_falta.md`, tendo o anterior sido guardado em `docs/versoes/backups/pdfs_em_falta_2026-10-10_antes_sincronizacao_0.4.114.md`. O script `conferir_bibliografia.py` regenera `bibliografia_local.json`, reutilizando as regras locais de correspondência. Três PDFs já existentes noutras pastas de `material/` foram copiados para `material/bibliografia/`; origens, destinos e hashes estão em `pdfs_copiados.json`.

O ficheiro `entradas-nao-reconhecidas-importacao-2026-09-23.md` foi removido por indicação do autor, que confirmou a resolução das tarefas. As referências a esse ficheiro nos registos históricos foram preservadas como proveniência.

## Conferência das repetições

A comparação sequencial identificou um bloco de **125 entradas exatamente iguais**, nas posições bibliográficas **18–142** e **158–282**: começa em **Ciklacandir et al. (2022)** e termina em **Østlie et al. (2011)**. Todas as entradas intermédias desses dois blocos coincidem, pela mesma ordem. A lista integral está em `repeticoes_bibliografia.csv`; as posições contam parágrafos bibliográficos não vazios, a partir de 1.

Há ainda uma repetição parcial de **Østlie et al. (2012)**, nas posições 143 e 283. Na posição 143, a referência continua indevidamente com o fragmento `F., & Maria, M. (2023). Improving access to prosthetic limbs in Germany…`, relativo a Baumann e Maria. A posição 17 começa com `Baumann, Mearch and Development Academy…` e termina com o DOI `10.37868/sei.v5i1.id185`, que também consta da entrada completa de **Chtioui, Gaha e Benamara (2023)**, na posição 157. A sequência sugere uma inserção acidental de um bloco bibliográfico dentro de outra entrada; esta é uma interpretação da estrutura, não uma confirmação da operação que originou o problema.

No PDF de referência, o início do bloco repetido encontra-se nas páginas físicas **149 e 160**, e Østlie (2011/2012) nas páginas físicas **159 e 171**. Estes números são os do visualizador de PDF, não a paginação impressa da dissertação. O ODT e o Markdown não foram alterados nesta conferência.
