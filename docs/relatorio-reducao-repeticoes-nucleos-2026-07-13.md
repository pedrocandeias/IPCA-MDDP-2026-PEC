# Relatório da redução dos núcleos repetidos

**Documento:** `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`

**Versão da fonte:** 0.4.30

**Data:** 13 de Julho de 2026

## Objectivo e critério

A revisão incidiu nos quatro núcleos transversais identificados pelo relatório de revisão académica: mediação do designer entre tecnologia e pessoa; supervisão humana da inteligência artificial; distinção entre personalização e variação ilimitada; e vantagens gerais da parametrização. O critério não foi eliminar todas as recorrências terminológicas, mas atribuir uma função diferente e verificável a cada capítulo:

- Capítulo 2: fundamentação teórica e crítica;
- Capítulo 3: operacionalização metodológica e unidade de análise;
- Capítulos 5–7: arquitectura, contrato técnico e decisões implementadas;
- Capítulo 9: síntese dos contributos e limites.

## Alterações realizadas

| Localização | Problema anterior | Função preservada após a revisão |
| --- | --- | --- |
| 3.2 | Reapresentava o designer como mediador em termos próximos do Capítulo 2 | Define a cadeia de decisões e transformações do protótipo como unidade de análise |
| 6.1 | Repetia em vários parágrafos que a IA era apoio, não substituição humana | Delimita entrada, saída e fronteira entre sugestão probabilística e geometria determinística |
| 6.2 | Reapresentava a teoria da parametrização e da personalização limitada | Documenta os dois objectos de dados, o pedido, o contrato e o alcance restrito de «apoio à decisão» |
| 6.4 | Repetia a necessidade genérica de supervisão e responsabilidade | Distingue estados do fluxo, salvaguardas implementadas, riscos residuais e limites éticos observáveis |
| 7.1 | Repetia clareza, mediação e carga cognitiva como efeitos esperados | Descreve as seis operações da interface, o esquema activo, os limites e a pré-visualização |
| 7.2 | Reapresentava extensamente participação, autonomia e supervisão | Especifica os três perfis, permissões e decisões que a plataforma não implementa |
| 7.3 | Repetia a mediação digital em formulações sucessivas | Identifica quatro mecanismos de mediação e distingue implementação de efeitos ainda não avaliados |
| 9.2 | Retomava os quatro temas como síntese | Mantido, por cumprir a função própria de formular os contributos finais |

As Secções 2.6–2.8 e 5.2 não foram abreviadas nesta passagem. As primeiras constituem o lugar adequado para a fundamentação; a segunda descreve a arquitectura implementada e fornece o referente técnico necessário aos Capítulos 6 e 7.

## Resultado quantitativo

| Secção | Palavras antes | Palavras depois |
| --- | ---: | ---: |
| 3.2 | 276 | 273 |
| 6.1 | 636 | 277 |
| 6.2 | 1.022 | 642 |
| 6.4 | 646 | 400 |
| 7.1 | 581 | 250 |
| 7.2 | 913 | 346 |
| 7.3 | 600 | 249 |
| 9.2 | 229 | 229 |
| **Total** | **4.903** | **2.666** |

A redução corresponde a 2.237 palavras, aproximadamente 45,6% do conjunto auditado. A contagem inclui títulos e blocos de legendas existentes nas secções, pelo que deve ser entendida como indicador comparativo, não como extensão líquida exclusiva da prosa.

## Verificação documental

- O DOCX mantém 30 tabelas e 28 elementos de desenho.
- A Tabela 6.1 e as Figuras 6.1 e 7.1 foram preservadas com as respectivas legendas e fontes.
- As Secções 3.2, 6.1, 6.2, 6.4 e 7.1–7.3 foram sincronizadas entre Markdown e DOCX.
- A síntese de contributos da Secção 9.2 foi preservada.
- A cópia anterior à revisão encontra-se em `versions/`, com a etiqueta `before-repetition-core-pass`.

## Limite da revisão

Esta passagem reduz reapresentações teóricas nos locais assinalados, mas não elimina a recorrência necessária de termos como «parâmetro», «supervisão», «configuração» ou «mediação». Esses termos continuam a surgir quando identificam uma regra, um componente, um resultado ou uma conclusão diferente. A paginação estática deve ser novamente confirmada após a próxima exportação final para PDF.
