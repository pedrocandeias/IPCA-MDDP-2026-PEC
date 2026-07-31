# Decisões editoriais sobre as propostas do LanguageTool

## Âmbito

Foram revistas individualmente as 176 ocorrências filtradas pelo LanguageTool 6.6 no manuscrito 0.4.60. A revisão não tratou os avisos como erros confirmados: cada proposta foi confrontada com a sintaxe da frase, o significado técnico, o registo académico e a terminologia já estabilizada na dissertação.

Foram aceites 81 propostas e rejeitadas 95. Numa das ocorrências de gramática, o segmento assinalado pelo motor estava correcto, mas a leitura do contexto revelou um erro adjacente — «o estado final da plataforma foi inspeccionada» —, corrigido para «foi inspeccionado». As decisões aceites, esta correcção contextual e os ajustes da releitura final produziram 80 substituições no Markdown e 84 no DOCX; a diferença resulta sobretudo de entradas repetidas nos índices do documento institucional.

## Síntese por categoria

| Categoria | Propostas revistas | Aceites | Rejeitadas | Critério principal |
| --- | ---: | ---: | ---: | --- |
| Concordância | 10 | 4 | 6 | Corrigiram-se erros inequívocos e uma formulação ambígua; conservaram-se concordâncias legítimas com orações infinitivas, enumerações e sujeitos compostos. |
| Gramática | 4 | 2 | 2 | Adoptaram-se o conjuntivo depois de «sem pressupor que» e o artigo em «equivalem a uma avaliação»; rejeitaram-se uma leitura errada da crase e uma associação sintáctica incorrecta do motor. |
| Clareza | 11 | 10 | 1 | Substituíram-se relações espaciais vagas por relações operacionais como «nos intervalos», «segundo as relações» e «na própria transformação»; manteve-se «torna-se difícil», por ser mais natural do que a sugestão. |
| Redundância | 17 | 10 | 7 | Retiraram-se expressões dispensáveis quando não acrescentavam significado; conservaram-se marcas temporais, quantitativas ou de totalidade necessárias à interpretação. |
| Concisão | 67 | 23 | 44 | Aceitaram-se reformulações naturais e precisas; rejeitaram-se gerúndios ambíguos, advérbios pouco idiomáticos e trocas de «em que» por «onde» em referentes abstractos. |
| Registo formal e académico | 29 | 24 | 5 | «Através de» foi substituído apenas quando era possível indicar melhor o mecanismo, o critério ou a base da operação; rejeitaram-se falsos avisos relativos a «escalas», «vias» e «limites», bem como alterações que eliminariam prudência científica. |
| Pontuação | 10 | 2 | 8 | Acrescentaram-se vírgulas em duas construções parentéticas com «por exemplo»; rejeitaram-se vírgulas indevidas em coordenações e alterações às parenteses necessárias das fórmulas. |
| Estilo | 28 | 6 | 22 | Dividiram-se frases realmente extensas e reformularam-se construções vagas; manteve-se a repetição deliberada em enumerações de capítulos, fases, riscos, perfis e camadas. |

## Exemplos de propostas aceites

- «pela Regulamento» foi corrigido para «pelo Regulamento».
- «sistema estruturado de variáveis capaz de descrever» passou a «componentes de um sistema estruturado capaz de descrever», eliminando a ambiguidade do referente de «capaz».
- «não são medida da robustez» passou a «não constituem uma medida da robustez».
- «valores dentro dos intervalos» passou a «valores nos intervalos».
- «documentada através de episódios» passou a «documentada com base em episódios», porque os episódios constituem a base documental e não um meio físico de passagem.
- «referência populacional através de uma pontuação» passou a «referência populacional com base numa pontuação».
- A explicação da homotetia global foi dividida em duas frases e passou a explicitar que uma proporção única não é aplicada a todas as partes da prótese.

## Exemplos de propostas rejeitadas

- «Replicar artificialmente estas funções continua a ser um desafio» foi mantido: o sujeito é a oração infinitiva «Replicar artificialmente estas funções», no singular.
- «Gerar muitas alternativas não equivale a resolver bem o problema» foi mantido pelo mesmo motivo.
- «Entre os factores físicos incluem-se...» e «Entre os principais desafios destacam-se...» foram mantidos, porque os verbos concordam com enumerações plurais.
- «Posterior à pré-visualização» foi mantido: a contracção da preposição «a» com o artigo feminino está correcta.
- «Alternativas mais prováveis» foi mantido porque exprime probabilidade relativa e é contrastado com «alternativas menos prováveis».
- «Alterações posteriores» foi mantido nas passagens em que «posteriores» distingue alterações realizadas depois do fecho dos ensaios.
- As propostas para substituir «em que» por «onde» foram rejeitadas quando o antecedente era uma abordagem, um fluxo, um cenário ou outro conceito abstracto, e não um lugar.
- Sugestões como «controladamente», «limitadamente», «articuladamente» e «semelhantemente» foram rejeitadas por serem menos naturais ou menos precisas no contexto académico.
- As repetições iniciais em sequências como «O Capítulo...», «A fase...», «Um segundo risco...» e «No caso...» foram mantidas por estruturarem enumerações deliberadas.
- Os parênteses duplos em fórmulas foram mantidos por representarem níveis de agrupamento matemático, não pontuação duplicada.

## Resultado da segunda análise

Depois da aplicação e da releitura, os relatórios foram regenerados sobre o DOCX 0.4.61. Permaneceram 97 avisos filtrados: seis de concordância, dois de gramática, um de clareza, sete de redundância, 45 de concisão, cinco de registo formal e académico, oito de pontuação e 23 de estilo. Estes avisos correspondem às propostas rejeitadas ou a regras que continuam a assinalar construções deliberadamente mantidas; não devem ser aplicados automaticamente.
