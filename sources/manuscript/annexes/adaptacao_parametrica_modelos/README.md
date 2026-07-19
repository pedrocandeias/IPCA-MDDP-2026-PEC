# Anexo C — notas de preparação

## Ficheiros

- `anexo_c_adaptacao_parametrica_modelos.md`: texto académico complementar ao dicionário da plataforma 14.67.0;
- `anexo_c_adaptacao_parametrica_modelos.docx`: versão editável para integração institucional;
- `anexo_c_adaptacao_parametrica_modelos.pdf`: versão final de leitura em 14 páginas A4;
- `figuras/figura_c1_fluxo_adaptacao_parametrica.svg`: diagrama vectorial editável de produção própria usado na secção C.2;
- `figuras/figura_c1_fluxo_adaptacao_parametrica.png`: derivado de apresentação usado na exportação DOCX/PDF, gerado a partir do SVG.

## Origem e método

O texto foi preparado por leitura comparada de `models/models-config.json`, do mapa antropométrico do servidor, dos modelos OpenSCAD activos, do relatório de adaptação antropométrica da plataforma, do Capítulo 4 e da fonte de trabalho `dicionario_parametros_v14.67.0`. A edição actual documenta o estado final examinado e distingue-o do estado histórico preservado no Suplemento 3 — Parametrização e percurso numérico. As relações e valores foram transcritos apenas quando confirmados nos ficheiros examinados. Os exemplos complementares foram recalculados a partir das fórmulas do código; não foram usados para inferir ajuste anatómico ou desempenho funcional.

A figura SVG foi desenhada especificamente para o anexo e representa o fluxo conceptual comum. A fonte editável e o PNG de apresentação encontram-se na pasta `figuras/`, junto das restantes imagens usadas no manuscrito. As ligações usam segmentos ortogonais para separar visualmente o percurso das caixas de texto. Na revisão 0.4.68, a paleta, a tipografia, os contornos e as setas foram uniformizados com as Figuras 5.3–5.5 através de `tools/generate_restyled_figures_068.py`; na revisão 0.4.69, as pontas das setas foram reduzidas e passaram a ter dimensões independentes da espessura das linhas, evitando a sobreposição com caixas e contornos. O PNG de 1800 × 1035 píxeis foi exportado do SVG com o Inkscape e constitui o derivado destinado à incorporação nos formatos finais. A figura não reproduz uma interface nem um resultado clínico.

## Relação com o Suplemento 3

O directório `dicionario_parametros_v14.67.0` permanece a fonte de trabalho do dicionário histórico de 42 parâmetros e do exemplo numérico Flexy Beast. A selecção entregue encontra-se em `suplementos/03_parametrizacao_percurso/`. O Anexo C não a substitui: documenta alterações posteriores, inclui o Cyborg Beast e explicita excepções e limitações descobertas na leitura dos modelos.
