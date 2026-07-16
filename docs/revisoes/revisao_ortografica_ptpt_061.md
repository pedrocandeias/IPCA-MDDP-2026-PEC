# Revisão ortográfica em português de Portugal — versão 0.4.61

## Resultado

Foi confirmada uma forma incompatível com o português europeu de referência: `inequidades`. Existem **duas ocorrências substantivas no Markdown**, nas linhas 751 e 755. No DOCX existem **três ocorrências**, nos parágrafos extraídos 275, 615 e 617, porque o parágrafo 275 é a entrada do índice derivada do título da subsecção; as duas ocorrências substantivas correspondem aos parágrafos 615 e 617. Propõe-se a substituição por `iniquidades`. O relatório não aplica a correcção nem altera o Markdown ou o DOCX canónicos.

Esta conclusão é estritamente ortográfica. Não significa que o texto esteja isento de questões de gramática, concordância, pontuação, clareza, estilo ou uniformização editorial, que ficaram deliberadamente fora do âmbito.

## Ficheiros examinados

- Markdown canónico: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md`, versão declarada 0.4.61, 3734 linhas, SHA-256 `3c8b43c30685f7a952c9563c68b96649d624f3c05fa33ab64db5eb8f0106ce9a`.
- DOCX canónico: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`, SHA-256 `aff74ace2f8b553e8b81e358e435bf7a4b08d3ec6ab71105882fa69995f4f635`.
- Data da revisão: 15 de julho de 2026.

As somas de verificação identificam exactamente o estado dos ficheiros que serviu de base ao relatório. Se o manuscrito for posteriormente modificado, as localizações e a conclusão devem ser revalidadas.

## Método

1. O DOCX foi examinado localmente com o LanguageTool 6.6, na variante `pt-PT` e no nível `PICKY`. O motor devolveu 4934 avisos, dos quais 3340 foram classificados pelo procedimento de auditoria como ocorrências lexicais, correspondentes a 733 formas distintas.
2. Os 733 candidatos lexicais foram submetidos a triagem humana no respectivo contexto. Um aviso do LanguageTool foi tratado apenas como pista e nunca como confirmação de erro.
3. O Markdown foi usado para confirmar a grafia, obter a linha exacta e efectuar uma segunda procura de erros de digitação evidentes, acentos anómalos, palavras duplicadas e sequências indevidamente aglutinadas.
4. Quando a extracção linear do DOCX produziu uma forma suspeita, o elemento correspondente em `word/document.xml` foi inspeccionado para distinguir o texto real de artefactos causados por quebras de linha, campos, índices ou fórmulas.
5. Foram excluídos o *Abstract*, a bibliografia, os títulos originais de obras, nomes próprios, siglas, código, identificadores, nomes de programas e modelos, estrangeirismos técnicos e todas as propostas relativas apenas a gramática, concordância, pontuação, estilo, clareza ou concisão.
6. Foi respeitada a grafia histórica já adoptada em grande parte do manuscrito. Formas como «projecto», «concepção», «detectar», «respectivo» e «proprioceptivo» não foram tratadas como erros ortográficos.

## Melhorias ortográficas confirmadas

| Forma encontrada | Localização | Excerto curto | Proposta | Fundamento ortográfico | Confiança |
| --- | --- | --- | --- | --- | --- |
| `inequidades` | Duas ocorrências substantivas no Markdown: linha 751, título «Lacuna 5 — Acesso, custo, manutenção e inequidades sistémicas»; linha 755, primeiro parágrafo da mesma subsecção. Três ocorrências no DOCX: parágrafo extraído 275, entrada do índice derivada do título; parágrafo 615, título substantivo; parágrafo 617, texto substantivo. | «agravar as inequidades» | `iniquidades` | Em português europeu, a forma registada é [`iniquidade`](https://www.infopedia.pt/dicionarios/lingua-portuguesa/iniquidade), do latim *iniquitate-*. O plural `iniquidades` é também o usado no [Plano Nacional de Saúde 2021–2030](https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/POR_Portugal_Plano-Nacional-de-Saude_2021-2030.pdf) para designar desigualdades evitáveis e injustas em saúde. `Inequidade` não é a grafia portuguesa de referência para este conceito. | Muito elevada |

## Principais candidatos rejeitados

| Forma assinalada | Localização rastreável | Verificação contextual | Decisão | Confiança |
| --- | --- | --- | --- | --- |
| `apresentadoao` | DOCX, parágrafos extraídos 12 e 47; folha de rosto; sem ocorrência no Markdown | O XML contém `Projeto apresentado`, seguido de uma quebra de linha (`w:br`), e depois `ao Instituto Politécnico do Cávado e do Ave`. O extractor suprimiu a quebra e criou artificialmente a aglutinação. | Rejeitado: falso positivo da extracção, não erro do documento. | Muito elevada |
| `julho` → `Julho` | DOCX, parágrafos extraídos 18 e 53; data da folha de rosto | Em português, os nomes dos meses escrevem-se com inicial minúscula. A linha isolada não transforma `julho` em nome próprio. | Rejeitado: a proposta introduziria uma grafia inadequada. | Muito elevada |
| `projecto`, `concepção`, `detectar`, `detecção`, `respectivo` e formas relacionadas | Exemplos no Markdown: linhas 9, 291, 399, 497, 796, 1027 e 1146 | São formas compatíveis com a grafia sem o Acordo Ortográfico de 1990, amplamente adoptada no manuscrito. A sua substituição seria uma decisão de uniformização ortográfica global, não a correcção de lapsos inequívocos. | Rejeitado neste relatório. | Elevada |
| `proprioceptivo` | Markdown, linha 307, Secção 2.1 | Forma anterior ao Acordo Ortográfico, coerente com o critério gráfico adoptado no manuscrito. | Rejeitado neste relatório. | Elevada |
| `ortoprotesia` | Markdown, linha 385, tabela da equipa multidisciplinar | Palavra portuguesa dicionarizada que designa a disciplina correspondente; não exige acento gráfico. | Rejeitado: falso positivo lexical. | Muito elevada |
| `OpenSCAD`, `PLA`, `PETG`, `Flexy`, `Beast`, `UnLimbited` e formas semelhantes | Ocorrências distribuídas pelo manuscrito | Nomes de programas, materiais, modelos e identificadores técnicos. A ausência no dicionário geral não indica erro. | Excluídos pelo âmbito. | Muito elevada |

## Verificação das terminações em «-bilidade»

Foram encontradas 183 ocorrências, correspondentes a 31 formas distintas quando se ignoram maiúsculas e minúsculas. Incluem, entre outras, `acessibilidade`, `aceitabilidade`, `biocompatibilidade`, `comorbilidades`, `comparabilidade`, `compatibilidade`, `durabilidade`, `escalabilidade`, `interoperabilidade`, `responsabilidade`, `usabilidade`, `verificabilidade`, `viabilidade` e `visibilidade`.

Nenhuma destas formas foi assinalada apenas por terminar em «-bilidade». Não foi encontrada qualquer excepção com erro ortográfico inequívoco. Esta decisão aplica directamente a regra indicada para a revisão: a terminação é produtiva e, por si só, não constitui indício de palavra inventada.

## Conclusão operacional

- Correcções ortográficas propostas: **uma forma em duas localizações substantivas**; o DOCX contém ainda uma terceira ocorrência, derivada, na entrada do índice.
- Formas distintas sugeridas automaticamente e revistas: **733**.
- Formas terminadas em «-bilidade» verificadas: **31**, em **183** ocorrências.
- Alterações efectuadas no manuscrito: **0**.

Recomenda-se aplicar manualmente apenas `inequidades` → `iniquidades` nas duas localizações de fonte indicadas e actualizar a entrada correspondente no índice do DOCX. Não se recomenda aplicar automaticamente as restantes sugestões ortográficas do LanguageTool. Uma futura decisão de converter integralmente o manuscrito para o Acordo Ortográfico de 1990 deve ser tratada como uma operação editorial separada, global e validada por contexto.
