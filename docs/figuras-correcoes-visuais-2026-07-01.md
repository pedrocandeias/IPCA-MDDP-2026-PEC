# Correcções visuais de figuras

**Data:** 2026-07-01  
**Âmbito:** correcção manual de PNGs em `figuras/` que a auditoria geométrica anterior não detectou como problemáticos.

## Síntese

Foram corrigidos recortes que continham apenas fragmentos de figuras, cabeçalhos, texto corrido de artigo ou elementos adjacentes à figura original. A pasta `figuras/` foi preservada antes da intervenção em:

`versions/figuras-backup-2026-07-01_10-13-33_before-visual-fixes/`

As folhas de contacto em `docs/figuras-contact-sheets-2026-06-30/` foram regeneradas depois das correcções.

## Ficheiros corrigidos

| Ficheiro | Problema corrigido |
| --- | --- |
| `figuras/ch2_a_framework_for_configuring_partici_figure1_p4.png` | Fragmento inferior da figura; passou a conter o diagrama completo do processo de living lab. |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure1_p2.png` | Recorte parcial do fluxo AM; passou a conter os três fluxos completos sem texto lateral. |
| `figuras/ch2_ai_in_co_creation_the_usability_and_figure7_p7.png` | Fragmento inferior do diagrama; passou a conter o enquadramento conceptual completo. |
| `figuras/ch2_biometric_analysis_hand_parameters_figure1_p2.png` | Cabeçalho de página; passou a conter a imagem anatómica das posições da mão. |
| `figuras/ch2_estimation_of_anthropometric_hand_m_figure1_p3.png` | Fragmento inferior de desenho; passou a conter a figura de comprimentos relevantes da mão. |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure1_p3.png` | Fragmento do desenho; passou a conter a medição completa dos dedos D2 e D3. |
| `figuras/ch4_a_data_driven_design_framework_for_figure1_p2.png` | Página com texto corrido e figura; passou a conter apenas o framework D3Frame. |
| `figuras/ch6_a_data_driven_design_framework_for_figure1_p2.png` | Duplicado corrigido da figura D3Frame. |
| `figuras/ch6_a_data_driven_design_framework_for_figure9_p7.png` | Texto corrido em vez de gráfico; passou a conter o gráfico de similaridade de movimento. |
| `figuras/ch2_a_framework_to_study_human_ai_colla_figure14_p46.png` | Texto corrido em vez da figura; passou a conter o diagrama XAI/responsible AI. |
| `figuras/ch6_a_framework_to_study_human_ai_colla_figure14_p46.png` | Duplicado corrigido do diagrama XAI/responsible AI. |

## Validação

- Abertura visual dos ficheiros corrigidos com `view_image`.
- Regeneração das folhas de contacto por capítulo e folha global.
- Filtragem dimensional pós-correcção sem outliers restantes por altura baixa, largura baixa ou proporção extrema.
