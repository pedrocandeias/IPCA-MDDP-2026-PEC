# Guia opcional de caracterização dimensional e verificação da montagem do Anexo D

As palmas dos doze casos foram medidas em PLA e PETG nos eixos X, Y e Z, com um
valor registado por eixo. Este guia descreve uma eventual extensão metrológica com
três leituras independentes e uma possível verificação sistemática da montagem e
articulação. Nenhuma destas extensões é necessária para a comparação dimensional
descritiva apresentada na dissertação.

## 1. O que é necessário antes de medir

Começar por reunir apenas as peças que possam ser associadas sem ambiguidade a um
ficheiro digital. Para cada peça preencher `inventario_especimes_fisicos.csv` com:

- identificador escrito na peça ou atribuído no momento do inventário;
- modelo e perfil (`child_8`, `teen_15`, `adult_28` ou `elderly_70`);
- componente, material e impressora;
- ficheiro 3MF correspondente;
- estado da peça: completa, incompleta, danificada ou sem correspondência digital;
- possibilidade de medição e de montagem.

Uma peça sem correspondência segura com o modelo, o perfil e o ficheiro não deve
ser usada no cálculo do desvio dimensional. Pode ser fotografada como registo de
prototipagem, mas fica fora da comparação malha–peça.

## 2. Conjunto recomendado para uma extensão metrológica

Para aprofundar os resultados já integrados, o conjunto recomendado abrange os
doze casos digitais nos dois materiais. Se não for possível repetir o conjunto
integral, o subconjunto deve ser delimitado e justificado. Em qualquer caso, deve incluir:

1. uma palma identificada de cada modelo que tenha sido efectivamente produzida;
2. os três eixos X, Y e Z de cada palma seleccionada;
3. três leituras independentes por eixo;
4. pelo menos uma fotografia geral por espécime e uma fotografia de cada eixo com
   o paquímetro colocado nos extremos usados.

Se existirem palmas de vários perfis do mesmo modelo, devem ser incluídas. Se só
existirem segmentos ou dedos, estes podem ser inventariados, mas não devem ser
forçados para a folha das palmas.

## 3. Material necessário

- paquímetro digital ou analógico, com resolução conhecida;
- superfície plana e iluminação uniforme;
- etiquetas removíveis para os identificadores;
- telemóvel ou câmara para fotografar os pontos de contacto;
- `tabela_comparacao_dimensional.csv`;
- ficheiros 3MF das palmas correspondentes.

Registar a marca/modelo do paquímetro, resolução, data, pessoa que mediu e
temperatura ambiente aproximada. Não é necessário comprimir a peça para obter uma
leitura mais próxima da malha.

## 4. Medição dimensional

Para cada palma:

1. confirmar o identificador e o 3MF correspondente;
2. remover apenas suportes e rebarbas que não pertençam à geometria projectada;
3. orientar a peça como no ficheiro digital;
4. medir a extensão total X entre os extremos transversais;
5. retirar e voltar a colocar o paquímetro;
6. repetir até obter três leituras independentes;
7. repetir o procedimento para Y e Z;
8. conservar os valores já integrados e registar as três novas leituras numa folha própria, sem substituir o registo original;
9. registar em notas qualquer dificuldade de contacto, deformação ou extremo
   instável;
10. fotografar cada posição de medição.

Se o paquímetro não conseguir contactar de forma estável os extremos definidos,
assinalar «não realizável». Não escolher outro ponto apenas na peça física: mudar o
ponto obrigaria a repetir também a medição da malha.

Depois de preencher as leituras, executar:

```bash
python3 tools/calcular_resultados_dimensionais_fisicos.py
```

O programa cria `resultados_dimensionais_fisicos_calculados.csv`, calculando média,
amplitude, desvio absoluto e desvio percentual. O ficheiro original com as leituras
não é substituído.

## 5. Verificação de montagem e articulação

Preencher `folha_montagem_articulacao.csv` apenas para os componentes realmente
disponíveis. A sequência recomendada é:

1. fotografar todas as peças antes da montagem;
2. verificar se os pinos entram sem corte, lixagem ou deformação permanente;
3. registar intervenções correctivas, mesmo quando a montagem acaba por resultar;
4. observar separadamente polegar, indicador, médio, anelar e mindinho;
5. assinalar colisões, bloqueios e folgas visíveis;
6. quando cabos, elásticos e restantes componentes estiverem presentes, accionar
   manualmente o mecanismo;
7. executar cinco ciclos completos de fecho e libertação;
8. registar se existe fecho, retorno e alteração visível após os ciclos;
9. opcionalmente, observar o envolvimento de cilindros rígidos de 30, 50 e 70 mm;
10. fotografar a posição aberta, a posição fechada e qualquer falha observada.

Uma mão incompleta pode sustentar uma observação de compatibilidade entre peças,
mas não um resultado de fecho ou retorno. No Flexy Beast, as juntas não foram
produzidas em material flexível; por isso, o comportamento elástico e o retorno
previstos pelo modelo original continuam como não avaliados.

## 6. O que entregar para integração na dissertação

Depois da execução, reunir:

- `inventario_especimes_fisicos.csv` preenchido;
- `tabela_comparacao_dimensional.csv` com as três leituras;
- `resultados_dimensionais_fisicos_calculados.csv`;
- `folha_montagem_articulacao.csv` preenchida;
- fotografias nomeadas como `modelo_perfil_especime_eixo.jpg` ou
  `modelo_perfil_especime_montagem.jpg`;
- marca e resolução do paquímetro;
- notas sobre peças excluídas, falhas e intervenções correctivas.

Com estes elementos podem ser acrescentadas ao Capítulo 8 uma tabela dimensional,
uma tabela de montagem e uma selecção de fotografias próprias. Os resultados devem
ser apresentados como verificação dimensional e de montagem em bancada, não como
adequação anatómica individual, desempenho estrutural ou eficácia protésica.
