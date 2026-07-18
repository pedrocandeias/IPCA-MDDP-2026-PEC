# Rastreabilidade dos artefactos `[^n]` no DOCX

Data da verificação: 16 de Julho de 2026

Documento examinado: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`

SHA-256 do DOCX examinado: `5480d546628805262f7697906baa64377cbd8fa43e80784271093361ca19152c`

## Conclusão

As expressões `[^1]` a `[^13]` não são referências bibliográficas nem notas de rodapé académicas. São chamadas de notas de revisão escritas em sintaxe Markdown. Durante a conversão para DOCX, algumas chamadas foram preservadas como texto literal, mas as definições correspondentes não foram transferidas para notas de rodapé do Word.

Na primeira extracção efectuada durante esta verificação, o DOCX continha nove chamadas literais: `[^2]`, `[^3]`, `[^4]`, `[^5]`, `[^9]`, `[^10]`, `[^11]`, `[^12]` e `[^13]`. O documento foi entretanto guardado novamente. Na versão final identificada pelo hash acima permanecem apenas **duas chamadas literais**, `[^9]` e `[^13]`. As restantes onze já não aparecem como texto literal, embora as observações que lhes deram origem possam ser recuperadas nas versões de segurança.

As definições exactas foram recuperadas de `docs/versoes/backups/projecto-completo-2026-07-07_17-31-00-after-pull-before-reapply-section.md`, linhas 1565–1601. O Markdown canónico actual ainda contém as nove chamadas identificadas na primeira extracção, mas já não contém as respectivas definições; existe, portanto, uma divergência transitória entre o Markdown e o DOCX mais recente.

## Correspondência entre cada marcador e a passagem comentada

| Marcador | Estado no DOCX actual | Passagem a que se refere | Nota original recuperada | Sentido da observação |
| --- | --- | --- | --- | --- |
| `[^1]` | A chamada literal já não existe. Permanece um comentário nativo do Word sobre a mesma palavra. | Secção 2.1, próteses mecânicas: «*feedback* proprioceptivo indirecto». | «definir o que é proprioceptivo» | Pedia uma explicação do significado de propriocepção neste contexto. O DOCX conserva ainda o comentário nativo «Trocar “feedback”», ancorado apenas na palavra *feedback*. |
| `[^2]` | Já não está visível no DOCX mais recente; estava antes de «EU» na primeira extracção. | Secção 2.1, enquadramento regulatório: referência ao Regulamento (UE) 2017/745 relativo aos dispositivos médicos. | «Meter este link na bibliografia» | Pedia que a ligação para o regulamento fosse convertida numa referência bibliográfica formal. A chamada tinha ficado colocada no interior da designação «(EU)», mas referia-se ao regulamento e à ligação que a seguia, não à sigla `EU`. |
| `[^3]` | Já não está visível no DOCX mais recente; estava depois de «marcação CE» na primeira extracção. | Secção 2.1, enquadramento regulatório: «avaliação por um organismo notificado para efeitos de marcação CE». | «não é bem marcação, né. Tem que ser outra palavra» | Questionava a expressão «marcação CE». É uma dúvida terminológica editorial, não uma remissão para uma fonte. A expressão deve ser confirmada segundo a terminologia oficial antes de qualquer substituição. |
| `[^4]` | Já não está visível no DOCX mais recente; estava depois de `ISO/TC 168` na primeira extracção. | Secção 2.1: comité técnico da ISO relativo a próteses e ortóteses. | «Cool, mas se calhar, só se calhar, linkar isto tb né?» | Pedia uma ligação ou referência formal para o comité ISO/TC 168 ou para as normas relevantes. |
| `[^5]` | Já não está visível no DOCX mais recente; estava depois de «Ron Mace» na primeira extracção. | Secção 2.2: Sete Princípios do *design* universal atribuídos a Ron Mace. | «vamos adicionar a citação e bibliografia. faz sentido uma tabela?» | Pedia uma fonte bibliográfica para a atribuição dos sete princípios e levantava a possibilidade de os apresentar numa tabela. A citação a Story (2006) encontra-se no final do período. |
| `[^6]` | A chamada literal já não existe. | Versão anterior da Secção 2.2: «modelos como o *Matching Person and Technology* (MPT) e quadros conceptuais baseados na Classificação Internacional de Funcionalidade (ICF)». | «explicar oque são todos estes modelos.» | Pedia a definição do MPT e da ICF. No texto actual, os nomes são apresentados por extenso e as siglas constam da lista de abreviaturas; a chamada foi eliminada. |
| `[^7]` | A chamada literal já não existe. | Versão anterior da Secção 2.3: expressão inglesa «*seed designs*». | «definir seed design» | Pedia a definição do conceito. O texto actual substitui a expressão por «modelos-base parametrizados», pelo que a chamada deixou de ser necessária. |
| `[^8]` | A chamada literal já não existe. | Versão anterior da Secção 2.3: «modelos simplesmente escalados». | «escalonados? amplicados e reduzidos? Que palavra utilizar?» | Registava uma dúvida lexical sobre a tradução de *scaled*. O texto actual usa «modelos ajustados apenas por escala global», resolvendo a ambiguidade. |
| `[^9]` | **Visível** no final do período sobre Wiberg et al. (2019). | Secção 2.3: afirmação de que o sistema avaliado teria gerado milhares de variantes com elevada taxa de sucesso e reduzido reimpressões. | «toda esta frase podia ser melhorada» | Pedia a reformulação integral do período. A auditoria bibliográfica posterior concluiu ainda que a associação é incompatível: Wiberg et al. é uma revisão e não demonstra um sistema experimental com milhares de variantes ou redução de reimpressões. Não é apenas um problema estilístico; a afirmação exige correcção substantiva ou outra fonte. |
| `[^10]` | Já não está visível no DOCX mais recente; estava no final do período na primeira extracção. | Secção 2.3: enumeração de FDM, FFF, SLS, SLA e processos metálicos, seguida da relação com requisitos de projecto. | «Posso igualmente aumentar este secção um pouco. Está tudo super comprimido» | Pedia o desenvolvimento da subsecção, por considerar a explicação demasiado condensada. O marcador referia-se ao parágrafo e, por extensão, à subsecção «Integração com Fabrico Aditivo e *Design for Additive Manufacturing*». |
| `[^11]` | Já não está visível no DOCX mais recente; estava depois de «encomenda *online*» na primeira extracção. | Secção 2.3: fluxo «*file-to-factory*» executado localmente ou por meio de uma encomenda *online*. | «não me soa super bem.» | Expressa insatisfação com a formulação «por meio de uma encomenda *online*». A intenção parece ser distinguir fabrico local de submissão do ficheiro a um serviço externo de fabrico ou produção por encomenda. |
| `[^12]` | Já não está visível no DOCX mais recente; estava depois do período sobre dispensa de moldes na primeira extracção. | Secção 2.3: associação entre *file-to-factory*, democratização do *design*, personalização em massa e redução de custos marginais. | «Estou a bater mal ou já escrevi isto?» | Assinala possível repetição. A ideia de produzir geometrias sem moldes ou ferramentas dedicadas já aparece no início da Secção 2.3; a nota pede verificação de redundância, não uma nova citação. |
| `[^13]` | **Visível** imediatamente antes de «penalizações». | Secção 2.3, implicações para o *design* industrial: «reduzir penalizações tradicionais associadas à variação de produto». | «penalizações é um pouco forte» | Questiona especificamente a escolha lexical «penalizações». Alternativas semanticamente mais neutras incluem «custos tradicionalmente associados à variação do produto», «sobrecustos associados à variedade» ou «limitações económicas associadas à variação», devendo a escolha final respeitar o sentido demonstrado pelas fontes. |

## Marcadores ainda visíveis por secção

| Secção | Marcadores | Quantidade |
| --- | --- | ---: |
| 2.1 — Prótese de membro superior e dispositivos médicos | — | 0 |
| 2.2 — *Design* industrial, *design* inclusivo e *design* centrado no utilizador | — | 0 |
| 2.3 — Fabrico aditivo e parametrização no *design* de produto | `[^9]`, `[^13]` | 2 |
| **Total no DOCX actual** |  | **2** |

## Comentário nativo do Word relacionado

Além dos marcadores Markdown, o DOCX contém um comentário nativo do Word, criado em 16 de Julho de 2026 e atribuído a «Unknown Author». O comentário está ancorado na palavra *feedback*, na expressão «*feedback* proprioceptivo indirecto», e contém o texto exacto:

> Trocar “feedback”

Este comentário nativo corresponde ao mesmo segmento anteriormente assinalado por `[^1]`, mas constitui um mecanismo diferente: aparece em `word/comments.xml` e está correctamente associado a um intervalo do texto do Word.

## Implicação para a revisão

Os dois marcadores ainda visíveis podem ser removidos do DOCX sem perda de informação depois de as decisões editoriais correspondentes serem tomadas. Nenhum destes marcadores deve ser convertido automaticamente em nota de rodapé, porque o seu conteúdo é informal, inclui dúvidas já resolvidas e, no caso de `[^9]`, aponta para um problema substantivo de suporte bibliográfico que exige revisão do texto.
