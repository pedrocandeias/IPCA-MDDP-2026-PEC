# Rastreabilidade dos artefactos `[^n]` no DOCX

Data da verificação: 16 de Julho de 2026

Documento examinado: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`

SHA-256 do DOCX examinado: `2310d59dd45437e683ea786716d5628308ab234c7b7740641f49b3dae2c528d2`

## Actualização de 20 de Julho de 2026 — versão 0.4.98

Foram resolvidos os cinco marcadores editoriais que ainda permaneciam no Markdown, `[^9]` a `[^13]`, e o marcador `[^13]` que continuava visível no DOCX. A afirmação incompatível atribuída a Wiberg et al. (2019) foi substituída por uma descrição verificável da organização dos métodos e ferramentas de DfAM; a explicação das tecnologias de fabrico aditivo foi desenvolvida; «encomenda *online*» passou a «serviço externo de fabrico digital»; a repetição sobre a dispensa de moldes foi eliminada; e «penalizações» foi substituído por «sobrecustos tradicionalmente associados à produção de variantes».

Os três comentários nativos que existiam na versão imediatamente anterior foram igualmente encerrados. As duas chamadas relativas ao Regulamento (UE) 2017/745 passaram a apoiar-se na entrada normativa completa e no PDF oficial em português; «marcação CE» foi confirmada como a designação usada pelo próprio regulamento. A atribuição dos Sete Princípios deixou de ser feita apenas a Ron Mace: o texto identifica a autoria colectiva do grupo de dez investigadores e profissionais e cita o *Center for Universal Design* (1997), cujo documento original foi arquivado localmente. Story (2006), cujo texto integral permanecia indisponível, foi retirado; a aplicação na saúde passou a ser descrita segundo os critérios directamente confrontados em White e Mosca (2022). O DOCX e o Markdown actuais já não contêm marcadores `[^n]`, e o DOCX não contém comentários nativos por resolver.

## Actualização de 20 de Julho de 2026 — versão 0.4.97

O PDF integral `projecto_completo_bibliografia/IEC-62366-1_2015.pdf` confirmou que o documento disponível corresponde à primeira edição da IEC 62366-1, publicada em Fevereiro de 2015, e não à versão consolidada com a Emenda 1:2020. A citação no texto e a entrada bibliográfica foram, por isso, alinhadas com a edição efectivamente consultada: IEC 62366-1:2015 e International Electrotechnical Commission (2015). O texto integral permite verificar directamente o processo de engenharia de usabilidade e a distinção entre as avaliações realizadas durante o desenvolvimento e a avaliação final da interface.

A referência ao ISO/TC 168 foi mantida para sustentar o âmbito geral do comité. A redacção passou a reproduzir esse âmbito com maior precisão — desempenho, segurança, factores ambientais e possibilidade de intercâmbio entre componentes —, enquanto a ISO 8549-1:2020 continua a sustentar especificamente a terminologia do domínio.

## Actualização de 20 de Julho de 2026 — versão 0.4.96

As instruções bibliográficas associadas aos marcadores `[^2]`, `[^4]` e `[^5]` e aos comentários nativos equivalentes foram executadas. A referência completa do Regulamento (UE) 2017/745 e a de Story (2006) já existiam na bibliografia e foram confirmadas; a ligação directa ao regulamento foi retirada do texto corrente. Foram acrescentadas referências formais para o comité ISO/TC 168, a ISO 8549-1:2020 e a ISO 7250-1:2017. A designação incorrecta «ISO 62366» foi corrigida para IEC 62366-1:2015+A1:2020 e a norma foi igualmente acrescentada à bibliografia.

Os marcadores informais `[^2]`, `[^3]`, `[^4]` e `[^5]` foram removidos do Markdown canónico. Permanecem cinco marcadores, `[^9]` a `[^13]`, associados a decisões editoriais diferentes. Os sete comentários nativos do DOCX foram preservados para manter o histórico de revisão; seis referem agora tarefas bibliográficas executadas e um continua a pedir a explicação da expressão «geração contínua».

## Conclusão

As expressões `[^1]` a `[^13]` não são referências bibliográficas nem notas de rodapé académicas. São chamadas de notas de revisão escritas em sintaxe Markdown. Durante a conversão para DOCX, algumas chamadas foram preservadas como texto literal, mas as definições correspondentes não foram transferidas para notas de rodapé do Word.

Na primeira extracção efectuada durante esta verificação, o DOCX continha nove chamadas literais: `[^2]`, `[^3]`, `[^4]`, `[^5]`, `[^9]`, `[^10]`, `[^11]`, `[^12]` e `[^13]`. O documento foi entretanto revisto e guardado novamente. Na versão 0.4.98 já não permanece qualquer chamada literal `[^n]`; as observações originais continuam documentadas neste relatório e nas versões de segurança.

As definições exactas foram recuperadas de `docs/versoes/backups/projecto-completo-2026-07-07_17-31-00-after-pull-before-reapply-section.md`, linhas 1565–1601. A divergência transitória entre o Markdown e o DOCX foi eliminada na versão 0.4.98.

## Correspondência entre cada marcador e a passagem comentada

| Marcador | Estado no DOCX actual | Passagem a que se refere | Nota original recuperada | Sentido da observação |
| --- | --- | --- | --- | --- |
| `[^1]` | Resolvida; a chamada e o comentário nativo já não existem. | Secção 2.1, próteses mecânicas: «*feedback* proprioceptivo indirecto». | «definir o que é proprioceptivo» | Pedia uma explicação do significado de propriocepção neste contexto. A observação ficou registada neste relatório e deixou de permanecer como comentário por resolver no DOCX. |
| `[^2]` | Resolvida. | Secção 2.1, enquadramento regulatório: referência ao Regulamento (UE) 2017/745 relativo aos dispositivos médicos. | «Meter este link na bibliografia» | A entrada normativa completa foi integrada na bibliografia e o PDF oficial em português foi arquivado em `projecto_completo_bibliografia/Regulamento_UE_2017_745_dispositivos_medicos_PT.pdf`. |
| `[^3]` | Resolvida. | Secção 2.1, enquadramento regulatório: avaliação da conformidade e marcação CE. | «não é bem marcação, né. Tem que ser outra palavra» | O artigo 20.º e a definição do artigo 2.º, ponto 43, confirmam «marcação CE» como a terminologia oficial. A relação entre classe, avaliação da conformidade e organismo notificado foi reformulada com base nos artigos 20.º, 51.º e 52.º. |
| `[^4]` | Já não está visível no DOCX mais recente; estava depois de `ISO/TC 168` na primeira extracção. | Secção 2.1: comité técnico da ISO relativo a próteses e ortóteses. | «Cool, mas se calhar, só se calhar, linkar isto tb né?» | Pedia uma ligação ou referência formal para o comité ISO/TC 168 ou para as normas relevantes. |
| `[^5]` | Resolvida. | Secção 2.2: Sete Princípios do *design* universal. | «vamos adicionar a citação e bibliografia. faz sentido uma tabela?» | A atribuição isolada a Ron Mace foi corrigida: o texto identifica o grupo de dez autores e cita a publicação original do *Center for Universal Design* (1997). O PDF oficial foi arquivado localmente. |
| `[^6]` | A chamada literal já não existe. | Versão anterior da Secção 2.2: «modelos como o *Matching Person and Technology* (MPT) e quadros conceptuais baseados na Classificação Internacional de Funcionalidade (ICF)». | «explicar oque são todos estes modelos.» | Pedia a definição do MPT e da ICF. No texto actual, os nomes são apresentados por extenso e as siglas constam da lista de abreviaturas; a chamada foi eliminada. |
| `[^7]` | A chamada literal já não existe. | Versão anterior da Secção 2.3: expressão inglesa «*seed designs*». | «definir seed design» | Pedia a definição do conceito. O texto actual substitui a expressão por «modelos-base parametrizados», pelo que a chamada deixou de ser necessária. |
| `[^8]` | A chamada literal já não existe. | Versão anterior da Secção 2.3: «modelos simplesmente escalados». | «escalonados? amplicados e reduzidos? Que palavra utilizar?» | Registava uma dúvida lexical sobre a tradução de *scaled*. O texto actual usa «modelos ajustados apenas por escala global», resolvendo a ambiguidade. |
| `[^9]` | Resolvida na versão 0.4.98. | Secção 2.3: afirmação de que o sistema avaliado teria gerado milhares de variantes com elevada taxa de sucesso e reduzido reimpressões. | «toda esta frase podia ser melhorada» | A afirmação incompatível foi retirada. Wiberg et al. (2019) passou a sustentar apenas a organização dos métodos e ferramentas de DfAM ao longo das etapas do processo. |
| `[^10]` | Resolvida na versão 0.4.98. | Secção 2.3: enumeração de FDM, FFF, SLS, SLA e processos metálicos. | «Posso igualmente aumentar este secção um pouco. Está tudo super comprimido» | A explicação foi desenvolvida para distinguir extrusão de termoplástico, sinterização selectiva a laser, estereolitografia e processos metálicos em leito de pó, relacionando-os com os respectivos constrangimentos de projecto. |
| `[^11]` | Resolvida na versão 0.4.98. | Secção 2.3: alternativas de produção no fluxo *file-to-factory*. | «não me soa super bem.» | «Por meio de uma encomenda *online*» foi substituído por «mediante o envio do ficheiro a um serviço externo de fabrico digital». |
| `[^12]` | Resolvida na versão 0.4.98. | Secção 2.3: repetição sobre dispensa de moldes e dispositivos específicos. | «Estou a bater mal ou já escrevi isto?» | A repetição foi eliminada. O parágrafo passou a explicar a ligação entre variação digital, produção física e estratégias de personalização, sem repetir a afirmação apresentada no início da secção. |
| `[^13]` | Resolvida na versão 0.4.98. | Secção 2.3, implicações económicas para o *design* industrial. | «penalizações é um pouco forte» | «Penalizações tradicionais associadas à variação de produto» foi substituído por «sobrecustos tradicionalmente associados à produção de variantes». |

## Marcadores ainda visíveis por secção

| Secção | Marcadores | Quantidade |
| --- | --- | ---: |
| 2.1 — Prótese de membro superior e dispositivos médicos | — | 0 |
| 2.2 — *Design* industrial, *design* inclusivo e *design* centrado no utilizador | — | 0 |
| 2.3 — Fabrico aditivo e parametrização no *design* de produto | — | 0 |
| **Total no DOCX actual** |  | **0** |

## Comentários nativos do Word

A versão 0.4.98 não contém comentários nativos por resolver. O comentário anteriormente associado a *feedback* e os três comentários bibliográficos presentes na versão imediatamente anterior — dois relativos ao Regulamento (UE) 2017/745 e um à atribuição a Ron Mace — foram encerrados depois de as respectivas decisões editoriais e bibliográficas terem sido aplicadas.

## Implicação para a revisão

Todos os marcadores editoriais foram resolvidos e removidos sem serem convertidos em notas de rodapé académicas. A rastreabilidade das observações e das decisões tomadas permanece assegurada por este relatório, pela auditoria bibliográfica e pelas versões de segurança.
