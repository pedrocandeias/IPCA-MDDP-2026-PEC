# Relatório das alterações aos Anexos B e D — versão 0.4.71

- **Data da intervenção:** 19 de julho de 2026
- **Âmbito:** integração da verificação manual de acessibilidade no Anexo B e conversão do Anexo D para A4 vertical
- **Documento de partida:** `docs/versoes/backups/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto-2026-07-19_14-03-39-before-annex-b-accessibility-and-annex-d-a4.docx`
- **Estado final fechado da intervenção:** `docs/versoes/exportacoes/2026-07-19_14-34-12-anexo-b-acessibilidade-anexo-d-a4-071/`
- **Versão do manuscrito:** 0.4.70 → 0.4.71

## 1. Delimitação do estado auditado

Este relatório compara a cópia de segurança criada imediatamente antes da intervenção com o DOCX e o PDF fechados na exportação `2026-07-19_14-34-12-anexo-b-acessibilidade-anexo-d-a4-071`. Esta exportação constitui o estado final rastreável do trabalho descrito abaixo.

O DOCX canónico na raiz foi novamente gravado às 14:59, depois de concluída a intervenção, e encontrava-se aberto no LibreOffice durante a elaboração deste relatório. Por essa razão, essa gravação posterior não é atribuída à intervenção e não foi sobrescrita.

| Estado | Ficheiro | SHA-256 |
|---|---|---|
| DOCX anterior à intervenção | `docs/versoes/backups/...14-03-39-before-annex-b-accessibility-and-annex-d-a4.docx` | `c2b72cfcd9d8e0f343e4c064bc5823b566b5bc81f52a7317349f28b7fa90c582` |
| DOCX final fechado da intervenção | `docs/versoes/exportacoes/...14-34-12.../pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx` | `da7886d19ce74169c28de3ee5ffbde992ab1520c2d56fafcc634ad4458eef763` |
| PDF final fechado da intervenção | `docs/versoes/exportacoes/...14-34-12.../pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf` | `718717b01ceba23e6ff5a3f649a79c414dc92d0150ce1de485a4ec908da0928e` |
| DOCX canónico após gravação posterior, fora do âmbito | `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx` | `3d778479fb9892caea0f23fd98b23d3f6a715f19c3d14462f9603d9e855a0b4e` |

## 2. Ficheiros criados ou alterados pela intervenção

| Ficheiro | Tipo de alteração |
|---|---|
| `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md` | Versão 0.4.71; integração dos resultados de acessibilidade; reorganização das tabelas do Anexo D; actualização de páginas e dos índices locais. |
| `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx` | Integração cirúrgica no XML do documento; conversão da secção do Anexo D para A4 vertical; reconstrução das tabelas D.1 e D.2; correcção dos índices locais. O estado final desta alteração está preservado na exportação fechada. |
| `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.pdf` | Regeneração a partir do DOCX 0.4.71, com 187 páginas A4 verticais. |
| `CHANGELOG.md` | Registo da versão 0.4.71, da integração da avaliação manual e da alteração do Anexo D. |
| `tools/update_annex_b_accessibility_annex_d_portrait_071.py` | Novo programa reproduzível para aplicar e validar as alterações no DOCX. |
| `docs/versoes/backups/...14-03-39-before-annex-b-accessibility-and-annex-d-a4.docx` | Cópia de segurança anterior à intervenção. |
| `docs/versoes/exportacoes/2026-07-19_14-34-12-anexo-b-acessibilidade-anexo-d-a4-071/` | Exportação fechada com o par DOCX/PDF que representa o resultado final da intervenção. |

Os ficheiros `lista_verificacao_manual_acessibilidade_wcag_2_2.md`, `lista_verificacao_manual_acessibilidade_wcag_2_2.docx` e `manifesto_evidencias.csv` já tinham sido preparados ou alterados na intervenção anterior. Foram usados como fonte e referenciados no Anexo B, mas não foram reescritos durante a alteração dos Anexos B e D.

## 3. Alterações de conteúdo relacionadas com a acessibilidade

### 3.1 Capítulo 7

O parágrafo que declarava estarem por realizar as verificações manuais foi substituído por uma síntese conjunta da verificação automática e manual. A nova redacção explicita:

- oito estados examinados automaticamente;
- sete verificações manuais conformes e cinco não conformes;
- limitações na ordenação e descrição dos campos com o Orca;
- utilização apenas parcial da interface a 400% de ampliação;
- ausência de alternativa textual reconhecível para o visualizador tridimensional;
- impossibilidade de inferir conformidade global com as WCAG 2.2;
- manutenção das ocorrências automáticas de baixo contraste, apesar da classificação manual.

### 3.2 Capítulo 8

O parágrafo que afirmava que as verificações manuais não tinham sido executadas passou a apresentar os resultados observados. A nova redacção conserva as quatro categorias de barreiras automáticas e acrescenta as cinco não conformidades manuais, mantendo a distinção entre:

- detecção automática de problemas;
- observação manual da interface;
- acessibilidade percebida por utilizadores;
- declaração formal de conformidade com as WCAG.

## 4. Alterações no Anexo B

### 4.1 Metadados e enquadramento

No Markdown, a data das séries de ensaios passou de «13 e 14 de Julho de 2026» para «2, 13 e 14 de julho de 2026». O estado da avaliação passou de «verificações manuais ainda por realizar» para «resultados parciais nas verificações automáticas e manuais».

A terceira dimensão da avaliação foi alterada de «verificação automática» para «verificação automática e manual». A formulação «barreiras detectáveis» foi simplificada para «barreiras nos estados examinados», evitando sugerir cobertura integral.

### 4.2 Procedimento manual acrescentado

A Secção B.3 passou a identificar:

- data e hora: 2 de julho de 2026, às 16:02;
- sistema: Linux;
- navegador: Firefox 152.0.6, 64-bit;
- ambientes: `localhost:3000` e `handfab.pedrocandeias.net`;
- leitor de ecrã: Orca;
- verificação de reformulação: ampliação a 400% e largura equivalente a 320 píxeis CSS.

### 4.3 Título e estrutura da Secção B.6

O título «B.6 Resultados da verificação automática de acessibilidade digital» foi substituído por «B.6 Resultados da verificação de acessibilidade digital», porque a secção passou a incluir duas modalidades de verificação.

O título «B.6.3 Verificação manual pendente» foi substituído por «B.6.3 Verificação manual complementar». Foi removida a lista prospectiva de ensaios por realizar e acrescentada uma descrição dos resultados efectivamente registados.

### 4.4 Nova Tabela B.5

A anterior Tabela B.5, que identificava as séries técnicas de ensaio, foi substituída pela «Tabela B.5 — Resultados da verificação manual complementar de acessibilidade». A nova tabela tem doze verificações, além do cabeçalho:

| Verificação | Resultado integrado |
|---|---|
| Navegação por teclado | Conforme |
| Visibilidade do foco | Conforme |
| Ordem do foco | Não conforme |
| Nome, função e valor | Não conforme |
| Identificação e sugestão de correcção de erros | Conforme |
| Mensagens de estado | Conforme |
| Contraste e utilização da cor | Conforme na observação manual |
| Reformulação e ampliação | Não conforme |
| Dimensão mínima dos alvos | Conforme |
| Autenticação acessível | Conforme |
| Alternativa ao visualizador tridimensional | Não conforme |
| Percurso com leitor de ecrã | Não conforme |

A legenda foi configurada para permanecer com a primeira linha da tabela. As linhas foram marcadas para não serem divididas entre páginas. No PDF final, a tabela começa na página impressa 141 e continua na página seguinte.

### 4.5 Ressalva relativa ao contraste

Foi acrescentado um parágrafo que impede uma interpretação incorrecta da classificação manual do contraste. O texto esclarece que:

- a observação manual foi classificada como conforme;
- a medição automática detectou 47 elementos com contraste insuficiente em oito estados;
- a versão, o ramo e o identificador da revisão da sessão manual não foram registados;
- os resultados são apresentados lado a lado e o contraste permanece uma prioridade de correcção;
- a avaliação não constitui uma declaração global de conformidade nem substitui avaliação com participantes.

### 4.6 Conclusão e numeração

A conclusão do Anexo B passou a identificar explicitamente as cinco não conformidades e as suas implicações para o projecto da interface.

No DOCX de partida, a secção técnica B.9 já não estava presente, mas as referências normativas conservavam o número B.10. As referências foram renumeradas para B.9. No Markdown foi igualmente removida a antiga «B.9 Ficha técnica e proveniência das evidências», incluindo a tabela redundante com identificadores de execução, para alinhar a estrutura principal com o DOCX e evitar reintroduzir pormenores técnicos que tinham sido retirados da dissertação.

### 4.7 Índice interno do Anexo B

As 19 remissões do índice interno foram corrigidas manualmente depois de se verificar que todas conservavam a página inicial do anexo.

| Entrada | Página final |
|---|---:|
| B.1 Finalidade | 137 |
| B.2 Âmbito e limites | 138 |
| B.3 Procedimento | 138 |
| B.4 Resultados de consistência da geração | 138 |
| B.4.1 Repetição da mesma configuração | 138 |
| B.4.2 Comparação entre navegadores | 139 |
| B.5 Resultados de recuperação e controlo | 139 |
| B.6 Resultados da verificação de acessibilidade digital | 140 |
| B.6.1 Percurso local autenticado | 140 |
| B.6.2 Superfície pública | 141 |
| B.6.3 Verificação manual complementar | 141 |
| B.7 Aprendizagens para o Design Industrial | 142 |
| B.8 Conclusão | 142 |
| B.9 Referências normativas | 143 |
| Tabela B.1 | 138 |
| Tabela B.2 | 139 |
| Tabela B.3 | 139 |
| Tabela B.4 | 140 |
| Tabela B.5 | 141 |

## 5. Alterações no Anexo D

### 5.1 Formato da secção

O Anexo D constituía a única secção A4 horizontal do DOCX. As propriedades da secção foram alteradas do seguinte modo:

| Propriedade | Antes | Depois |
|---|---:|---:|
| Largura da página | 16 838 twips | 11 906 twips |
| Altura da página | 11 906 twips | 16 838 twips |
| Orientação | Horizontal | Vertical |
| Margem esquerda | Configuração da secção horizontal | 1 701 twips |
| Margem direita | Configuração da secção horizontal | 1 418 twips |
| Margens superior e inferior | Configuração da secção horizontal | 1 985 twips |
| Cabeçalho e rodapé | Configuração da secção horizontal | 709 twips |

Depois da alteração, as dez secções do DOCX usam `w:w="11906"` e `w:h="16838"`, sem atributo de orientação horizontal.

### 5.2 Tabela D.1

A Tabela D.1 passou de onze colunas para seis:

| Antes | Depois |
|---|---|
| Modelo | Modelo e perfil |
| Perfil | Integrado na primeira coluna |
| Material | Material |
| Impressora | Equipamento |
| Camada | Integrada em Configuração |
| Enchimento | Integrado em Configuração |
| Suportes | Integrados em Configuração |
| Tempo estimado | Tempo estimado |
| Filamento estimado | Integrado em Material e custo estimados |
| Massa estimada | Integrada em Material e custo estimados |
| Custo | Integrado em Material e custo estimados |

Foram preservadas as quatro linhas de resultados e todos os valores de tempo, comprimento de filamento, massa e custo. A largura total passou a 8 787 twips, distribuída por `1450 + 900 + 1350 + 2200 + 1250 + 1637` twips.

### 5.3 Tabela D.2

A Tabela D.2 passou de doze colunas para sete. Foram retiradas da repetição linha a linha as colunas Material, Impressora, Camada, Enchimento e Suportes, porque essas condições comuns já estão declaradas imediatamente antes, na Secção D.3.2. Permaneceram:

- modelo;
- perfil;
- tempo estimado;
- filamento estimado;
- massa estimada;
- custo estimado;
- número de placas A1.

Foram preservadas as doze combinações de modelo e perfil e todos os respectivos valores. A largura total passou a 8 787 twips, distribuída por `1350 + 1050 + 1350 + 1450 + 1200 + 1250 + 1137` twips.

### 5.4 Tabela D.3

A Tabela D.3 conservou as sete colunas e os 12 casos dimensionais. A primeira coluna foi alargada para reduzir a divisão dos nomes dos modelos. A grelha final usa `1700 + 1000 + 1217 + 1217 + 1217 + 1217 + 1219` twips, num total de 8 787 twips.

### 5.5 Legendas, linhas e divisão entre páginas

As legendas das Tabelas D.1, D.2 e D.3 receberam a propriedade «manter com o parágrafo seguinte». As linhas das tabelas foram configuradas para não se dividirem entre duas páginas. Esta alteração eliminou a legenda isolada da Tabela D.1 no fundo da página anterior.

No PDF final:

- a Tabela D.1 começa na página 162;
- a Tabela D.2 começa na página 162 e a última linha continua na página seguinte;
- a Tabela D.3 começa na página 164;
- todas as colunas permanecem dentro das margens da página A4 vertical.

### 5.6 Índice interno do Anexo D

As 18 remissões do índice interno foram corrigidas, substituindo o valor único 159 pelas páginas efectivas.

| Entrada | Página final |
|---|---:|
| D.1 Finalidade | 159 |
| D.2 Distinção entre estimativa e medição real | 160 |
| D.3 Variáveis, controlos e materiais | 160 |
| D.3.1 Série A | 160 |
| D.3.2 Série B | 161 |
| D.4 Resultados | 161 |
| D.4.1 Série A | 162 |
| D.4.2 Série B | 162 |
| D.4.3 Geometria | 163 |
| D.4.4 Comparação entre entrada, malha e peça física | 164 |
| D.4.5 Registo fotográfico dos protótipos | 165 |
| D.5 Compatibilidade com orientações de dimensionamento | 166 |
| D.6 Limites de comparabilidade | 166 |
| D.7 Campos que não puderam ser obtidos | 167 |
| D.8 O que pode e não pode ser afirmado na dissertação | 167 |
| Tabela D.1 | 162 |
| Tabela D.2 | 162 |
| Tabela D.3 | 164 |

No Markdown, as três entradas das tabelas D.1–D.3 foram retiradas do índice de tabelas do Anexo C e colocadas num novo «Índice de tabelas do Anexo D», junto do início do anexo correspondente.

## 6. Alterações de paginação

### 6.1 Estrutura principal

A introdução da nova tabela e a recomposição do documento alteraram a paginação. Foram sincronizadas 67 entradas no DOCX e nove entradas adicionais nas listas do Markdown; os índices locais dos Anexos B e D foram depois corrigidos explicitamente.

| Elemento principal | Antes | Depois |
|---|---:|---:|
| Capítulo 3 | 36 | 37 |
| Capítulo 4 | 44 | 45 |
| Capítulo 5 | 61 | 63 |
| Capítulo 6 | 79 | 81 |
| Capítulo 8 | 89 | 91 |
| Capítulo 9 | 103 | 105 |
| Referências bibliográficas | 107 | 109 |
| Anexo A | 119 | 121 |
| Anexo B | 134 | 137 |
| Anexo C | 140 | 144 |
| Anexo D | 155 | 159 |

### 6.2 Lista global de tabelas

| Tabela | Antes | Depois | Tabela | Antes | Depois |
|---|---:|---:|---|---:|---:|
| 2.1 | 9 | 10 | 2.2 | 27 | 28 |
| 2.3 | 34 | 35 | 3.1 | 36 | 37 |
| 3.3 | 39 | 41 | 4.1 | 46 | 47 |
| 4.2 | 46 | 48 | 4.3 | 48 | 49 |
| 4.4 | 49 | 50 | 4.5 | 50 | 51 |
| 4.6 | 52 | 53 | 4.7 | 54 | 55 |
| 4.9 | 57 | 58 | 4.10 | 58 | 60 |
| 4.11 | 59 | 61 | 5.1 | 63 | 66 |
| 6.1 | 80 | 82 | 6.2 | 83 | 85 |
| 8.1 | 89 | 91 | 8.3 | 93 | 95 |
| 8.4 | 96 | 99 | 8.5 | 98 | 100 |
| 8.6 | 99 | 102 | 9.1 | 103 | 106 |

### 6.3 Lista global de figuras

| Figura | Antes | Depois | Figura | Antes | Depois |
|---|---:|---:|---|---:|---:|
| 3.2 | 42 | 43 | 4.1 | 45 | 46 |
| 4.2 | 48 | 49 | 4.3 | 53 | 54 |
| 5.1 | 62 | 64 | 5.2 | 63 | 65 |
| 5.6 | 71 | 73 | 5.7 | 72 | 74 |
| 8.1 | 94 | 97 | 8.2 | 94 | 97 |
| 8.3 | 95 | 97 | 8.4 | 95 | 98 |
| C.1 | 145 | 147 |  |  |  |

### 6.4 Entradas não alteradas automaticamente

O sincronizador reteve as páginas anteriores quando não conseguiu localizar inequivocamente a ocorrência no PDF. Esta situação foi registada para:

- Tabelas 3.2, 4.8, 8.2, 8.7 e 8.8;
- Figuras 2.8, 5.3, 5.8 e 7.1;
- os títulos «Optimização, Geração e Avaliação de Desempenho», «Da dimensão linear à forma como dado de projecto», «Interpretação e aplicação de dados antropométricos no projecto», «Limitações e lacunas», «Lacuna 4», «3.3 Estrutura metodológica do projecto», «Bases de dados antropométricas», «4.4 Iterações e decisões de projecto», «5.2 Arquitectura geral do sistema», «Capítulo 7» e «7.1 Estratégia de interacção e decisões de UI/UX».

Os índices dos Anexos B e D foram verificados directamente no PDF e corrigidos apesar desta limitação do sincronizador.

## 7. Preservação de notas de rodapé, comentários e relações

O programa alterou apenas `word/document.xml`. Antes de gravar, comparou as referências a notas e comentários e impediu a gravação se a sequência fosse alterada.

| Parte protegida | SHA-256 antes | SHA-256 depois |
|---|---|---|
| `word/comments.xml` | `69cd171824dff71711120741a2709a276f069f68794e073ec688496e4d162aaa` | Igual |
| `word/footnotes.xml` | `67f1e028d157932806cef7fe11cb3eeecd9b405fed1e5bb9da486f626c6d58c2` | Igual |
| `word/_rels/document.xml.rels` | `43b021d531a4b8a1222b58d525c77d4d6de5bca5eccdfe57e14dea464226b9bb` | Igual |

As contagens no corpo permaneceram inalteradas:

- 15 referências a comentários antes e depois;
- 12 referências a notas de rodapé antes e depois.

As imagens, estilos, cabeçalhos, rodapés e ficheiros de relações do DOCX não foram substituídos pelo programa.

## 8. Programa de actualização criado

Foi criado `tools/update_annex_b_accessibility_annex_d_portrait_071.py`. O programa:

- abre o DOCX como arquivo ZIP;
- altera `word/document.xml` com `lxml`;
- preserva as propriedades de parágrafo e de execução relevantes;
- conserva marcadores de comentário, marcadores internos e chamadas de notas;
- reconstrói as Tabelas B.5, D.1 e D.2;
- redimensiona a Tabela D.3;
- converte a secção final para A4 vertical;
- impede a divisão das linhas das tabelas;
- mantém as legendas junto das tabelas;
- actualiza os índices internos dos Anexos B e D;
- valida a ausência das formulações obsoletas;
- grava através de um ficheiro temporário e substitui o DOCX apenas depois de todas as validações passarem.

Foram acrescentados dois modos restritos para correcções idempotentes:

- `--captions-only`, para as propriedades finais das legendas e larguras;
- `--annex-indexes-only`, para as páginas dos índices internos.

## 9. Validações realizadas

| Verificação | Resultado |
|---|---|
| Integridade ZIP do DOCX com `unzip -t` | Sem erros |
| Compilação do programa com `py_compile` | Sem erros |
| Tamanho das dez secções do DOCX | 10 × A4 vertical |
| Número de páginas do PDF | 187 |
| Tamanho das páginas do PDF | 187 × 595,304 × 841,89 pontos, A4 |
| Rotação das páginas do PDF | 187 × 0° |
| Verificação visual da Tabela B.5 | Legível; legenda e primeiras linhas na página 141 |
| Verificação visual das Tabelas D.1 e D.2 | Legíveis e dentro das margens na página 162 |
| Verificação visual da Tabela D.3 | Legível e dentro das margens na página 164 |
| Pesquisa de «Verificação manual pendente» | Nenhuma ocorrência no estado final da intervenção |
| Pesquisa de «Permanecem por avaliar manualmente» | Nenhuma ocorrência no estado final da intervenção |
| Pesquisa de «B.10 Referências normativas» | Nenhuma ocorrência no estado final da intervenção |
| Verificação de espaços em branco com `git diff --check` | Sem erros |

A primeira tentativa de conversão reutilizou uma instância antiga do LibreOffice e não produziu um PDF actualizado. A exportação final foi, por isso, executada com um perfil isolado do LibreOffice e validada pelo carimbo temporal, pelo tamanho, pelo SHA-256 e pela leitura directa das páginas.

## 10. Limites e estado posterior

### 10.1 Gravação posterior do DOCX canónico

Depois de encerrada a intervenção, o DOCX canónico foi gravado novamente às 14:59. O ficheiro passou de 11 110 741 bytes no estado final fechado para 11 113 935 bytes e o SHA-256 passou de `da7886...` para `3d7784...`. O ficheiro de bloqueio do LibreOffice estava presente durante a elaboração deste relatório.

Consequentemente:

- a exportação das 14:34–14:42 é a referência exacta para auditar esta intervenção;
- o PDF canónico ainda corresponde ao estado final fechado da intervenção, não necessariamente à gravação posterior do DOCX;
- não foi feita qualquer tentativa de substituir o DOCX enquanto este se encontrava aberto.

### 10.2 Equivalência integral entre Markdown e DOCX

As passagens e tabelas directamente alteradas foram sincronizadas nos dois formatos, mas a intervenção não constituiu uma reconciliação integral de todo o Markdown com todo o DOCX. Permanecem diferenças anteriores fora do âmbito imediato, entre as quais:

- variantes de redacção em B.1–B.3;
- maior concisão de alguns cenários de controlo no Markdown;
- uma Secção D.9 presente no Markdown, enquanto o DOCX integra o registo fotográfico em D.4.5.

Estas diferenças devem ser objecto de uma comparação de três vias autónoma, usando a exportação 0.4.71 como base e a gravação actual do DOCX como versão do utilizador, para evitar apagar alterações entretanto efectuadas no LibreOffice.
