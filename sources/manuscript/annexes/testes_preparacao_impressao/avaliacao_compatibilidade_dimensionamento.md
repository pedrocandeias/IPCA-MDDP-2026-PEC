# Avaliação de compatibilidade com orientações de dimensionamento

## Finalidade e alcance

Esta nota compara as regras de escala aplicadas pela plataforma com os dois
documentos de dimensionamento existentes em `docs/sizing_values/`. A comparação
serve para examinar a compatibilidade das decisões de projecto com orientações
publicadas para os modelos de origem. Não demonstra adequação anatómica a uma
pessoa, ajuste ao membro residual, conforto ou adequação funcional.

## Flexy Beast e gráfico do Cyborg Beast

O Flexy Beast integrado na plataforma combina elementos do Flexy Hand e do
Cyborg Beast e adopta, para a escala uniforme inicial da mão, a relação:

```text
factor de escala = (palm_breadth_mm + 5) / 55
```

O ficheiro `cyborg_beast_Scaling_Chart.pdf` apresenta uma regressão por idade para
o Cyborg Beast, calculada a partir de uma amostra de onze crianças dos 3 aos 16
anos. Por se tratar de outro modelo e de uma regressão baseada apenas na idade, o
gráfico é usado como referência contextual, e não como valor esperado obrigatório
para o Flexy Beast.

| Perfil de ensaio | Regra dimensional da plataforma | Escala obtida | Referência etária Cyborg Beast | Interpretação |
|---|---:|---:|---:|---|
| `child_8` | (64 + 5) / 55 | 125,5% | 126% aos 8 anos | Valores muito próximos, apesar de resultarem de entradas e modelos distintos. |
| `teen_15` | (78 + 5) / 55 | 150,9% | 133% aos 15 anos | Diferença esperável entre uma regra baseada na largura introduzida e uma regressão baseada apenas na idade; não permite escolher um valor como mais adequado. |
| `adult_28` | (90 + 5) / 55 | 172,7% | não aplicável | O perfil está fora do intervalo etário do gráfico. |
| `elderly_70` | (84 + 5) / 55 | 161,8% | não aplicável | O perfil está fora do intervalo etário do gráfico. |

O caso infantil mostra compatibilidade pontual entre as duas abordagens. O caso
de 15 anos evidencia que a idade, por si só, não substitui uma dimensão da mão.
Esta leitura não constitui validação antropométrica do Flexy Beast.

## UnLimbited Phoenix

No Phoenix, a plataforma calcula uma escala uniforme a partir de uma largura de
referência interna de 82 mm e limita o resultado ao intervalo de 100% a 160%:

```text
HandPerc = limitar(palm_breadth_mm / 82 × 100, 100, 160)
```

A folha `unlimbed_phoenix_hand_v3_sizing_values.xlsx` apresenta uma geometria
Phoenix a 100% com largura de mão de 65 mm e comprimento de 135 mm, bem como uma
sequência de factores entre 1,00 e 1,65. A largura de 65 mm não é directamente
comparável com os 82 mm usados pela plataforma, porque os documentos não definem
o mesmo ponto de medição e a caixa exterior da palma inclui elementos
construtivos. Sem essa equivalência geométrica, uma comparação numérica directa
produziria uma falsa precisão.

| Perfil de ensaio | Largura introduzida | Escala calculada | Intervalo da folha Phoenix | Resultado |
|---|---:|---:|---:|---|
| `child_8` | 82 mm | 100,0% | 100%–165% | Dentro do intervalo; coincide com o piso aplicado pela plataforma. |
| `teen_15` | 88 mm | 107,3% | 100%–165% | Dentro do intervalo. |
| `adult_28` | 90 mm | 109,8% | 100%–165% | Dentro do intervalo. |
| `elderly_70` | 84 mm | 102,4% | 100%–165% | Dentro do intervalo. |

Os quatro casos respeitam o intervalo de escala indicado na folha. Este resultado
mostra compatibilidade com a gama de factores disponível, mas não prova que o
Phoenix seja anatomicamente adequado aos perfis de ensaio. A regra também explica
por que razão uma entrada inferior a 82 mm não reduz o modelo abaixo de 100%: o
piso preserva o limite construtivo adoptado para esta geometria.

## Paraglider Hand

Os ficheiros locais de dimensionamento não contêm uma tabela específica para o
Paraglider Hand. Por esse motivo, não foi criada uma comparação externa para este
modelo. A sua avaliação permanece limitada à aplicação da regra de escala
documentada, às dimensões obtidas na malha e à preparação para impressão.

## Conclusão

As tabelas existentes permitem verificar dois aspectos delimitados: a proximidade
pontual do perfil infantil Flexy à referência etária do Cyborg Beast e a inclusão
das quatro escalas Phoenix na gama de factores da folha de origem. Não permitem
avaliar correspondência anatómica individual nem funcionamento. Para esse fim
seriam necessários pontos de medição equivalentes, medidas directas da pessoa e
um protocolo de ajuste e utilização.
