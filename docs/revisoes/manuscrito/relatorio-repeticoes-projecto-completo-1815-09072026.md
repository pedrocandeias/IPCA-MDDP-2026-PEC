# Relatório de repetições no `projecto-completo.docx`

Data: 2026-07-09  
Ficheiro analisado: `projecto-completo.docx`  
Ficheiro derivado criado: `projecto-completo-sem-repeticoes.docx`

## 1. Síntese

Foi realizada uma nova revisão de repetições sobre o DOCX atual, preservando o manuscrito principal. A versão derivada `projecto-completo-sem-repeticoes.docx` reduz redundâncias funcionais sobretudo nos capítulos 6, 7, 8 e 9, sem regenerar o documento a partir de Markdown.

A intervenção foi feita diretamente sobre `word/document.xml`, em cópia do DOCX original. Esta opção foi escolhida para manter intactos os ficheiros internos de comentários, notas de rodapé, estilos, numeração, imagens e relações do pacote DOCX.

## 2. Metodologia

- Fonte: `projecto-completo.docx`.
- Saída: `projecto-completo-sem-repeticoes.docx`.
- Conversão auxiliar para leitura: `/tmp/projecto-completo-sem-repeticoes.md` (não versionada).
- Análise automática: parágrafos de prosa e frases com mais de 80 caracteres.
- Exclusões da análise automática principal: tabelas, bibliografia, legendas, linhas de fonte, cabeçalhos e elementos formais.
- Edição: substituições localizadas em parágrafos e remoção de parágrafos redundantes, sem intervenção sobre tabelas.

## 3. Resultados automáticos

Antes da edição:

- Parágrafos de prosa analisados: 508.
- Frases analisadas com 80+ caracteres: 1126.
- Parágrafos exatamente duplicados: 0.
- Frases exatamente duplicadas relevantes: 2 grupos.

Depois da edição:

- Parágrafos de prosa analisados: 497.
- Frases analisadas com 80+ caracteres: 1090.
- Parágrafos exatamente duplicados: 0.
- Frases exatamente duplicadas relevantes: 0.

O único duplicado automático residual é uma citação parentética repetida, não uma repetição editorial de argumento.

## 4. Repetições corrigidas

### R1 - Repetição exata em 7.3

Foi removida a segunda ocorrência isolada da frase sobre a falsa neutralidade da interface. A ocorrência integrada no parágrafo argumentativo foi mantida.

### R2 - Sobreposição entre 6.3 e 8.2

A Secção 6.3 foi reduzida ao desenho do protocolo, aos critérios de verificação e ao alcance metodológico. Os resultados detalhados sobre entradas completas, parciais, demográficas, lateralidade e variabilidade da IA ficam concentrados na Secção 8.2.

### R3 - Repetição da validação geométrica em 6.3 e 8.3

A Secção 6.3 deixou de recontar a execução dos três modelos. Passou a remeter para a Secção 8.3, onde a validação geométrica é discutida com os resultados e tabelas próprias.

### R4 - Repetição sobre lateralidade

A narrativa completa da falha de lateralidade e da correção determinística foi concentrada na Secção 8.2. Em 6.3 ficou apenas a indicação de que a lateralidade integra o protocolo como critério crítico.

### R5 - Repetição sobre IA como apoio e não autoridade

Foram condensados os parágrafos de 6.1, 6.2 e 6.4 que reiteravam a mesma ideia: a IA sugere, mas não decide nem valida clinicamente. A ideia permanece, mas com menos reformulações sucessivas.

### R6 - Repetição inicial em 7.1

Foi removida a duplicação imediata da frase sobre não exigir contacto direto com a estrutura interna do código/modelo.

### R7 - Duplicação em 8.4

Foi removido o segundo parágrafo quase idêntico sobre a correção da lateralidade, limites dos modelos e caráter preliminar dos resultados.

### R8 - Conclusão demasiado repetitiva em 9.1

A enumeração final dos resultados foi condensada para evitar reabrir a análise detalhada de 8.2 e 8.3. A conclusão mantém os contributos principais, mas sem repetir a discussão de resultados.

## 5. Correções formais associadas

Foram corrigidos problemas de junção ou pontuação encontrados durante a revisão:

- `human-in-the-loop.O sistema` -> `human-in-the-loop. O sistema`.
- `modelo.(Panchal` -> `modelo. (Panchal`.
- `erro.Do ponto de vista` -> `erro. Do ponto de vista`.
- `técnico especialista de próteses e ortóteses. ou clínico` -> `técnico especialista em próteses e ortóteses, ou clínico`.

## 6. Tabelas, comentários e notas de rodapé

A edição evitou modificar tabelas e preservou a estrutura interna do DOCX:

| Elemento | `projecto-completo.docx` | `projecto-completo-sem-repeticoes.docx` |
|---|---:|---:|
| Tabelas | 22 | 22 |
| Linhas de tabela | 234 | 234 |
| Células de tabela | 687 | 687 |
| Comentários | 24 | 24 |
| Referências de comentários | 24 | 24 |
| Notas de rodapé | 18 | 18 |
| Referências de notas de rodapé | 16 | 16 |

Os ficheiros internos `word/comments.xml`, `word/commentsExtended.xml` e `word/footnotes.xml` ficaram byte a byte iguais aos do DOCX original. Os comentários foram extraídos com `tools/extract_docx_comments.py` e continuam legíveis na versão derivada.

## 7. Validação

Validações concluídas:

- `unzip -t projecto-completo-sem-repeticoes.docx`: sem erros.
- Parsing XML de `word/document.xml`, `word/comments.xml`, `word/footnotes.xml`, `word/styles.xml` e `word/numbering.xml`: OK.
- Extração de comentários: 24 comentários encontrados.
- Contagem de tabelas, comentários e notas de rodapé: preservada.

Validação não concluída:

- A conversão via LibreOffice para PDF foi tentada, mas a execução foi bloqueada pelo ambiente `snap-confine` dentro da sandbox e o pedido de execução fora da sandbox expirou no revisor automático.

## 8. Observação final

O ficheiro `projecto-completo-sem-repeticoes.docx` deve ser tratado como versão derivada de revisão editorial. O `projecto-completo.docx` e o `projecto-completo.md` não foram substituídos.
