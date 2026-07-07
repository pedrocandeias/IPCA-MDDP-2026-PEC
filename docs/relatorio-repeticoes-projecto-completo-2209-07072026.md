# Relatório de repetições no `projecto-completo.md`

Data: 2026-07-07  
Ficheiro analisado: `projecto-completo.md`  
Conversão DOCX gerada: `docs/projecto-completo-2209-07072026-convertido-de-docx.md`  
Pasta de imagens extraídas: `docs/projecto-completo-2209-07072026-convertido-de-docx_media/`

## 1. Síntese

A conversão atual do `projecto-completo.docx` para Markdown foi gerada com o conversor local `tools/docx_to_md.py`. O ficheiro convertido tem 2270 linhas e extraiu 20 imagens embebidas.

A análise de repetições incidiu sobre o `projecto-completo.md` de raiz, porque é o manuscrito editável principal. A repetição mais clara é uma frase duplicada no Capítulo 7. Para além disso, há sobreposição forte entre os capítulos 6 e 8 na descrição da validação antropométrica assistida por IA, sobretudo nos cenários de amputação unilateral, lateralidade, esquema vivo do modelo e comportamento estocástico da IA.

O problema principal não é haver muitos parágrafos exatamente repetidos. O problema é a repetição funcional de argumentos: a mesma cadeia metodológica aparece primeiro como arquitetura, depois como explicação conceptual, depois como validação e finalmente como discussão/conclusão.

## 2. Metodologia usada

- Conversão DOCX para Markdown: `python3 tools/docx_to_md.py projecto-completo.docx -o docs/projecto-completo-2209-07072026-convertido-de-docx.md`.
- Análise automática de blocos de prosa com mais de 160 caracteres.
- Exclusões na análise automática principal: bibliografia, tabelas, imagens, legendas, linhas iniciadas por `Fonte` e linhas iniciadas por `Figura` ou `Tabela`.
- Inclusão do Anexo A na análise, mas com as mesmas exclusões de tabelas e metadados repetitivos.
- Deteção de duplicados exatos por normalização textual.
- Deteção de frases próximas por similaridade textual e sobreposição lexical.
- Pesquisa dirigida por termos recorrentes: `lateralidade`, `esquema vivo`, `JSON`, `human-in-the-loop`, `supervisão humana`, `descrição livre`, `dados demográficos`, `validação clínica`.

Resultados automáticos:

- Parágrafos exatamente duplicados: 0.
- Frases exatamente duplicadas: 1 grupo.
- Pares de frases fortemente semelhantes: 4 pares.
- Repetições temáticas relevantes: 6 grupos editoriais.

## 3. Repetições prioritárias

### R1 - Duplicação exata de frase no Capítulo 7

Prioridade: alta  
Tipo: duplicação textual exata  
Localização:

- `projecto-completo.md:1222`
- `projecto-completo.md:1224`

Frase duplicada:

> Uma interface bem desenhada pode criar a sensação de evidência ou de neutralidade em decisões que continuam condicionadas por critérios de projeto, pressupostos técnicos e escolhas interpretativas.

Diagnóstico:

A frase surge integrada num parágrafo maior e volta a aparecer isolada logo a seguir. A segunda ocorrência não acrescenta conteúdo e quebra a progressão argumentativa.

Recomendação:

Remover a ocorrência isolada em `projecto-completo.md:1224`. Manter a ocorrência integrada no parágrafo anterior, porque aí a frase está contextualizada e conduz para a discussão sobre limites da interface.

### R2 - Sobreposição entre 6.3 e 8.2 sobre validação antropométrica por IA

Prioridade: alta  
Tipo: repetição de resultados e interpretação  
Localização principal:

- `projecto-completo.md:1098-1126`, Secção 6.3
- `projecto-completo.md:1263-1293`, Secção 8.2

Pontos repetidos:

- A validação é interna e não clínica.
- A IA transforma descrições incompletas em parâmetros plausíveis.
- O ensaio usa cenários com diferentes graus de detalhe.
- Medições completas são preservadas.
- Entradas parciais são completadas proporcionalmente.
- Entradas apenas demográficas geram medidas plausíveis.
- A lateralidade funcionou nos testes iniciais, mas falhou em pedidos explícitos de mão esquerda.
- A correção passou a tratar a lateralidade como decisão determinística da interface.

Evidência automática:

- `projecto-completo.md:1106` e `projecto-completo.md:1273` apresentam o mesmo segundo conjunto experimental, com formulações muito próximas.
- `projecto-completo.md:1122-1124` e `projecto-completo.md:1273` repetem a falha de lateralidade e a correção determinística.
- `projecto-completo.md:1120` e `projecto-completo.md:1293` repetem a variabilidade estrutural da IA.

Diagnóstico:

A Secção 6.3 mistura enquadramento, método, resultados e conclusão. A Secção 8.2 volta a apresentar os resultados, o que torna os capítulos redundantes. Como o Capítulo 8 é o lugar natural da avaliação, a descrição completa dos resultados deve ficar aí.

Recomendação:

Reestruturar a divisão de funções:

- Secção 6.3: manter apenas arquitetura da validação, critérios e protocolo.
- Secção 8.2: concentrar resultados, falhas observadas, tabela de síntese e interpretação.
- Na Secção 6.3, substituir os parágrafos de resultados por uma frase de remissão, por exemplo: "Os resultados desta validação são discutidos na Secção 8.2, onde se distinguem os cenários com medições completas, parciais e apenas demográficas."

### R3 - Repetição da descrição do pedido enviado à IA

Prioridade: alta  
Tipo: repetição metodológica e técnica  
Localização:

- `projecto-completo.md:1020`, Secção 5.4
- `projecto-completo.md:1090`, Secção 6.2
- `projecto-completo.md:1100`, Secção 6.3

Conteúdo repetido:

- Descrição livre do utilizador.
- Esquema vivo do modelo selecionado.
- Nomes dos parâmetros.
- Legendas.
- Tipos.
- Limites mínimos e máximos.
- Valores correntes.
- Resposta JSON.
- Filtragem de chaves desconhecidas.
- Aplicação aos controlos do modelo.

Evidência automática:

O par `projecto-completo.md:1020` e `projecto-completo.md:1090` foi detetado como semelhante. A formulação muda, mas a função informativa é praticamente a mesma.

Diagnóstico:

Esta repetição é compreensível porque os capítulos têm funções diferentes, mas fica excessiva. A arquitetura do pedido deve ser descrita uma vez com detalhe; as secções seguintes podem recuperar apenas o que é necessário para o argumento local.

Recomendação:

- Manter a descrição técnica completa em 5.4, porque ali se descreve a estrutura funcional da plataforma.
- Em 6.2, reduzir para a implicação conceptual: a IA opera dentro de uma gramática paramétrica declarada, não num espaço aberto.
- Em 6.3, reduzir para a função metodológica: a validação incidiu sobre a continuidade entre linguagem natural, esquema e geometria.

### R4 - Lateralidade repetida em várias secções

Prioridade: média-alta  
Tipo: repetição temática transversal  
Localização:

- `projecto-completo.md:652`, Secção 3.5
- `projecto-completo.md:1098-1124`, Secção 6.3
- `projecto-completo.md:1242`, Secção 8.1
- `projecto-completo.md:1273`, Secção 8.2
- `projecto-completo.md:1291`, Tabela 8.1
- `projecto-completo.md:1337-1339`, Secção 8.4
- `projecto-completo.md:1349-1351`, Secção 9.1
- `projecto-completo.md:1365`, Secção 9.3

Diagnóstico:

A lateralidade é um achado importante, mas aparece em quase todas as fases finais do texto. A repetição é parcialmente justificada porque funciona como critério, resultado, risco e recomendação futura. Ainda assim, a forma atual reexplica várias vezes o mesmo percurso: funcionou inicialmente, falhou em pedidos de mão esquerda, foi corrigida por controlo determinístico da interface.

Recomendação:

- 3.5: manter apenas como critério metodológico.
- 6.3: referir que a lateralidade foi testada, sem relatar a falha em detalhe.
- 8.2: concentrar a narrativa completa da falha e correção.
- 8.4: discutir a implicação crítica em uma frase.
- 9.1 e 9.3: evitar recontar o caso; referir apenas como contributo/limitação.

### R5 - Repetição de "validação interna, não clínica"

Prioridade: média  
Tipo: repetição de delimitação metodológica  
Localização:

- `projecto-completo.md:652`
- `projecto-completo.md:1098`
- `projecto-completo.md:1126`
- `projecto-completo.md:1244-1245`
- `projecto-completo.md:1337`

Diagnóstico:

A distinção entre validação interna e validação clínica é necessária e deve ser mantida. Contudo, aparece com formulações muito próximas em metodologia, integração de IA, avaliação e discussão. A repetição reforça cautela, mas também pode criar a sensação de insistência defensiva.

Recomendação:

- Manter a definição completa em 3.5 ou 6.3.
- Em 8.1, usar apenas como critério de leitura dos resultados.
- Em 8.4, discutir as consequências, sem repetir a definição.
- Em 9.3, transformar em limitação futura: necessidade de validação clínica, funcional e longitudinal.

### R6 - Repetição do enquadramento human-in-the-loop e supervisão humana

Prioridade: média  
Tipo: repetição conceptual  
Localização:

- `projecto-completo.md:446`, Secção 2.6
- `projecto-completo.md:1022`, Secção 5.4
- `projecto-completo.md:1078`, Secção 6.1
- `projecto-completo.md:1094`, Secção 6.2
- `projecto-completo.md:1132`, Secção 6.4
- `projecto-completo.md:1148`, Secção 6.4
- `projecto-completo.md:1204`, Secção 7.2
- `projecto-completo.md:1359`, Secção 9.2

Diagnóstico:

O conceito é estruturante para a dissertação, mas a mesma ideia regressa muitas vezes: a IA sugere, não decide; apoia, não valida; acelera, não substitui julgamento técnico. Esta repetição é argumentativamente coerente, mas pode ser condensada para evitar redundância.

Recomendação:

- 2.6: manter como fundamento teórico.
- 5.4: ligar o conceito à arquitetura funcional, em uma frase.
- 6.1-6.2: manter como definição operacional da IA no sistema.
- 6.4: concentrar riscos e salvaguardas, evitando repetir a definição.
- 7.2: focar a distribuição de papéis entre designer, técnico e utilizador.
- 9.2: sintetizar como contributo, sem nova explicação.

### R7 - Repetição sobre entradas incompletas, parciais ou demográficas

Prioridade: média  
Tipo: repetição de resultado experimental  
Localização:

- `projecto-completo.md:1104`
- `projecto-completo.md:1108`
- `projecto-completo.md:1263-1273`
- `projecto-completo.md:1293`
- `projecto-completo.md:1335`
- `projecto-completo.md:1349`

Diagnóstico:

O argumento aparece como desenho experimental, resultado, discussão e conclusão. A repetição é menos problemática do que R2, mas contribui para a redundância geral entre os capítulos 6, 8 e 9.

Recomendação:

Manter a descrição experimental em 8.2 e deixar em 6.3 apenas a indicação dos três tipos de entrada testados. Na conclusão, reduzir a uma síntese curta: o sistema aceita descrições incompletas e produz pontos de partida verificáveis, mas não substitui medição ou validação.

### R8 - Repetição sobre variabilidade estocástica e propriedades invariantes

Prioridade: média  
Tipo: repetição de interpretação metodológica  
Localização:

- `projecto-completo.md:1118-1120`
- `projecto-completo.md:1293`
- `projecto-completo.md:1337`
- `projecto-completo.md:1365`

Diagnóstico:

A ideia é importante: a avaliação deve privilegiar propriedades invariantes, taxas de aprovação e comportamento geral, não valores isolados. No entanto, a formulação aparece como resultado, discussão e trabalho futuro.

Recomendação:

- 8.2: manter a observação empírica.
- 8.4: discutir a consequência metodológica.
- 9.3: manter apenas a proposta futura de quantificação com múltiplas extrações por perfil.

## 4. Pares de frases detetados automaticamente

| Local A | Local B | Tipo de sobreposição | Ação sugerida |
|---|---|---|---|
| `projecto-completo.md:1222` | `projecto-completo.md:1224` | Duplicação exata | Remover a segunda ocorrência |
| `projecto-completo.md:1106` | `projecto-completo.md:1273` | Segundo conjunto experimental, medições completas e lado amputado | Manter resultados completos em 8.2; abreviar 6.3 |
| `projecto-completo.md:1106` | `projecto-completo.md:1273` | Três cenários de amputação unilateral | Evitar recontar o mesmo ensaio em 6.3 |
| `projecto-completo.md:1020` | `projecto-completo.md:1090` | Descrição do pedido enviado à IA | Manter detalhe técnico em 5.4; reduzir 6.2 |
| `projecto-completo.md:1120` | `projecto-completo.md:1293` | Variabilidade estrutural dos parâmetros de hardware | Concentrar resultados em 8.2 |

## 5. Repetições aceitáveis ou estruturais

Nem todas as repetições devem ser corrigidas. Algumas cumprem função académica:

- A lista de acrónimos repete siglas que aparecem no texto, mas isso é intencional.
- A bibliografia não foi tratada como repetição textual, porque autores, títulos, DOIs e nomes de revistas repetem padrões formais.
- As legendas, fontes de figuras e tabelas foram excluídas da deteção principal.
- O Anexo A repete termos como "mão direita", "P5", "P50", "P95", "CSV" e "dados antropométricos"; isto é esperado porque descreve extração e codificação de dados.
- A repetição controlada de conceitos centrais, como IA, parametrização e validação, é aceitável quando cada ocorrência cumpre uma função diferente: teoria, método, implementação, avaliação ou conclusão.

## 6. Plano de correção recomendado

1. Corrigir primeiro R1, removendo a frase isolada duplicada no Capítulo 7.
2. Separar claramente as funções de 6.3 e 8.2:
   - 6.3 deve explicar protocolo e critérios.
   - 8.2 deve concentrar resultados e interpretação.
3. Consolidar a descrição do pedido enviado à IA:
   - detalhe técnico em 5.4;
   - implicação conceptual em 6.2;
   - remissão metodológica em 6.3.
4. Transformar a lateralidade num caso único bem narrado em 8.2, com referências curtas nos restantes capítulos.
5. Rever 9.1-9.3 depois das alterações, porque as conclusões devem sintetizar sem reabrir a explicação dos resultados.

## 7. Observações adicionais de limpeza editorial

Durante a leitura foram encontrados dois problemas formais relacionados com as repetições:

- Em `projecto-completo.md:1094`, falta espaço em `human-in-the-loop.O sistema`.
- Em `projecto-completo.md:1124`, há uma junção entre frases: `modelo de linguagem.A principal conclusão`.

Estas duas ocorrências não são repetições, mas devem ser corrigidas na mesma passagem editorial porque dificultam a leitura dos blocos onde se concentram as redundâncias.

