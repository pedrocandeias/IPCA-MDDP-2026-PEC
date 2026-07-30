# Protocolo de medição dimensional das peças físicas

**Estado dos dados integrados.** A comparação actual contém um valor registado
por eixo e por palma em PLA e PETG, obtido à temperatura ambiente. Este resultado
é apresentado de forma descritiva, sem cálculo de amplitude ou de incerteza. As
três leituras independentes descritas neste protocolo constituem uma extensão
metrológica opcional, necessária apenas se um estudo futuro pretender caracterizar
a dispersão associada ao reposicionamento do paquímetro.

## Finalidade

Este protocolo compara a geometria digital exportada com a peça produzida. O
objectivo é observar a materialização dimensional do projecto, e não avaliar o
ajuste anatómico a uma pessoa. A unidade de análise é a palma impressa de uma
configuração identificada da plataforma HandFab.

## Instrumentos e condições

- paquímetro com resolução indicada no registo do ensaio;
- ficheiro 3MF correspondente à peça;
- folha `tabela_comparacao_dimensional.csv`;
- peça limpa, sem suportes ou rebarbas que alterem os extremos medidos;
- temperatura ambiente e material registados;
- identificação do modelo, perfil, material, impressora e data de produção.

## Pontos de medição

Para cada palma são usados três pontos globais que podem ser reconstruídos a
partir do ficheiro 3MF:

1. **extensão X:** distância entre os dois extremos da peça no eixo X do ficheiro;
2. **extensão Y:** distância entre os dois extremos da peça no eixo Y do ficheiro;
3. **extensão Z:** distância entre os dois extremos da peça no eixo Z do ficheiro.

Na peça física, X corresponde à dimensão transversal, Y à dimensão longitudinal e
Z à espessura, depois de a palma ser orientada como no ficheiro exportado. Os
extremos devem ser identificados antes da primeira leitura e mantidos em todas as
repetições. Se a forma impedir o contacto estável do paquímetro, a medição é
classificada como não realizável e a razão é registada; não se escolhe outro ponto
sem actualizar também a medição digital.

## Procedimento

1. Confirmar que o identificador da peça coincide com o modelo e o perfil do 3MF.
2. Remover apenas suportes e rebarbas não pertencentes à geometria projectada.
3. Orientar a peça segundo os eixos X, Y e Z do ficheiro.
4. Encostar o paquímetro aos extremos do eixo sem comprimir ou deformar a peça.
5. Registar a leitura com a resolução efectiva do instrumento.
6. Retirar e voltar a posicionar o paquímetro antes de cada repetição.
7. Realizar três leituras independentes por eixo.
8. Registar qualquer dificuldade de contacto, deformação ou dano observado.

## Tratamento dos resultados

Para cada ponto são calculados:

```text
média da peça = (leitura 1 + leitura 2 + leitura 3) / 3
amplitude = leitura máxima − leitura mínima
desvio malha–peça = média da peça − medida da malha
desvio percentual = 100 × desvio malha–peça / medida da malha
```

Um desvio negativo indica que a peça ficou menor do que a malha; um desvio
positivo indica que ficou maior. A comparação não deve ser transformada numa
afirmação sobre adequação anatómica individual, resistência, segurança ou
funcionamento protésico.

## Interpretação da entrada paramétrica

O campo «Entrada» contextualiza a decisão paramétrica, mas não é necessariamente
igual à extensão exterior da malha. No Flexy Beast e no Paraglider, a geometria
da palma inclui interfaces e margens de montagem. No Paraglider, os campos
`palm_length_mm` e `palm_thickness_mm` são contextuais e não controlam os eixos Y
e Z de forma independente. Por isso, o desvio dimensional é calculado entre
malha e peça física, e não entre entrada e peça.
