# Auditoria visual dos PNG em `figuras/`

**Data:** 2026-06-30  
**Estado:** pós-recorte limpo aplicado em 2026-06-30, com segunda regeneração após correcção do detector de legenda.  
**Objectivo:** verificar se os PNGs não incluem a legenda original e se o crop contém a imagem completa com margens brancas.  
**Âmbito:** todos os ficheiros `figuras/*.png` actualmente presentes no repositório.

## Síntese executiva

- A acção dominante foi aplicada aos `125` PNGs: recorte a partir dos PDFs de origem, exclusão da legenda original e recriação de margens brancas.
- Antes da operação, foi criada uma cópia de segurança em `versions/figuras-backup-2026-06-30_before-recrops/`.
- O extractor foi corrigido para escolher a ocorrência mais baixa da legenda na página e aceitar padrões compactos como `Fig.15.`; isto corrigiu `figuras/ch4_parametric_3d_modeling_of_a_customi_figure7_p5.png` e cobriu `figuras/ch4_a_u_iwuoha_design_and_3d_printing_o_figure15_p6.png`.
- A legenda original foi localizada e excluída geometricamente em `125` de `125` figuras.
- Imagens em branco ou sem conteúdo detectável: `0`.
- Margens pós-recorte: `125` OK, `0` apertadas, `0` em falha.
- Risco de crop/corte nas bordas: `125` baixo, `0` médio, `0` alto.
- As `11` figuras actualmente usadas no manuscrito passam os critérios automáticos de legenda excluída, margem branca e conteúdo não vazio.
- O detector visual de texto residual ainda marca `98` imagens como `provavel` e `12` como `possivel`; nesta fase estes sinais devem ser lidos como texto interno de gráficos/diagramas a rever visualmente, não como prova de legenda original mantida.
- Foram detectados `11` grupos de duplicados exactos; a duplicação continua a ser uma decisão editorial de integração, não um problema de crop.

## Comparação antes/depois

| Indicador | Antes da acção dominante | Depois da acção dominante |
| --- | ---: | ---: |
| Figuras auditadas | 125 | 125 |
| Legenda original excluída por geometria do PDF | n/a | 125 |
| Legenda original provável pela heurística visual | 113 | 0 confirmadas por geometria |
| Sinal textual residual provável | 113 | 98 |
| Sinal textual residual possível | 4 | 12 |
| Sinal textual não detectado | 8 | 15 |
| Margens OK | 9 | 125 |
| Margens apertadas | 4 | 0 |
| Margens em falha | 112 | 0 |
| Risco alto de corte | 102 | 0 |
| Risco médio de corte | 10 | 0 |
| Risco baixo de corte | 13 | 125 |
| Imagens em branco | n/a | 0 |

## Como ler a auditoria pós-recorte

- **Legenda original excluída:** a posição da legenda no PDF de origem foi localizada e o limite inferior do crop foi colocado antes dela.
- **Sinal textual residual:** a heurística detecta blocos escuros no terço inferior do PNG; depois do recorte, este campo tende a captar rótulos, eixos, notas internas ou texto próprio da figura.
- **Margem OK:** há margem branca suficiente em torno do conteúdo detectado e a densidade de pixels não brancos junto às bordas é baixa.
- **Revisão visual opcional:** recomendada apenas antes de integrar novas figuras no manuscrito, sobretudo quando a figura tem muito texto interno.
- A detecção de texto continua sem OCR; por isso, a validação principal para legendas originais nesta auditoria é geométrica, a partir dos PDFs.

## Contagem por acção actual

| Acção actual | Total |
| --- | ---: |
| OK pós-recorte | 15 |
| OK pós-recorte; revisão visual opcional | 110 |

## Contagem por capítulo

| Capítulo | Total | Usadas | Legenda excluída | Margem OK | Risco baixo | Imagem não vazia | Sinal textual residual | OK final |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 | 0 | 6 | 6 | 6 | 6 | 6 | 6 |
| 2 | 54 | 8 | 54 | 54 | 54 | 54 | 46 | 54 |
| 3 | 6 | 1 | 6 | 6 | 6 | 6 | 6 | 6 |
| 4 | 30 | 2 | 30 | 30 | 30 | 30 | 23 | 30 |
| 5 | 7 | 0 | 7 | 7 | 7 | 7 | 7 | 7 |
| 6 | 11 | 0 | 11 | 11 | 11 | 11 | 11 | 11 |
| 7 | 7 | 0 | 7 | 7 | 7 | 7 | 7 | 7 |
| 8 | 4 | 0 | 4 | 4 | 4 | 4 | 4 | 4 |

## Figuras actualmente usadas no manuscrito

| Ficheiro | PDF de origem | Dimensões | Legenda original | Margem | Risco | Sinal textual residual | Estado actual |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| `figuras/ch2_2d_and_3d_anatomical_analyses_of_ha_figure1_p3.png` | `2D and 3D anatomical analyses of hand dimensions for custom-made gloves.pdf` | 1126x832 | excluída | OK | baixo | nao_detectada (0.21) | OK pós-recorte |
| `figuras/ch2_3d_printed_upper_limb_prostheses_a_figure2_p5.png` | `3D-printed upper limb prostheses a review.pdf` | 1283x1229 | excluída | OK | baixo | provavel (1.00) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_framework_for_configuring_partici_figure1_p4.png` | `A framework for configuring participation in living labs.pdf` | 597x154 | excluída | OK | baixo | nao_detectada (0.03) | OK pós-recorte |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure10_p9.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | 1461x1042 | excluída | OK | baixo | provavel (1.00) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure1_p2.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | 753x196 | excluída | OK | baixo | provavel (0.67) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_ai_driven_computer_aided_design_cad_figure1_p6.png` | `AI-DRIVEN COMPUTER-AIDED DESIGN CAD SYSTEMS LEVERAGING NEURAL NETWORKS FOR OPTIMIZED ENGINEERING PRODUCT DEVELOPMENT (2025).pdf` | 1304x604 | excluída | OK | baixo | possivel (0.62) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_implementation_of_3d_printing_techn_figure5_p8.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | 1125x595 | excluída | OK | baixo | provavel (1.00) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_prosthesis_rejection_in_acquired_ma_figure1_p4.png` | `Prosthesis rejection in acquired major upper-limb amputees a population-based survey.pdf` | 766x548 | excluída | OK | baixo | provavel (1.00) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_an_undergraduate_engineering_servic_figure1_p4.png` | `An Undergraduate Engineering Service Learning Project Involving 3D-Printed Prosthetic Hands for Children.pdf` | 1273x425 | excluída | OK | baixo | provavel (1.00) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure8_p7.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | 801x380 | excluída | OK | baixo | possivel (0.65) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure3_p2.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | 490x364 | excluída | OK | baixo | possivel (0.46) | OK pós-recorte; revisão visual opcional |

## Auditoria completa por capítulo

### Capítulo 1

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch1_implementation_of_3d_printing_techn_figure1_p4.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | não | 801x551 | excluída | OK | baixo | 32/50/39/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch1_implementation_of_3d_printing_techn_figure3_p6.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | não | 1046x462 | excluída | OK | baixo | 32/50/39/50 | provavel (1.00; 3 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch1_implementation_of_3d_printing_techn_figure4_p7.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | não | 590x993 | excluída | OK | baixo | 50/50/45/50 | provavel (1.00; 4 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch1_interdisciplinary_based_development_figure1_p2.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 1035x396 | excluída | OK | baixo | 32/50/50/51 | provavel (1.00; 95 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch1_review_of_robotic_prostheses_manufa_figure12_p20.png` | `Review of Robotic Prostheses Manufactured with 3D Printing Advances, Challenges, and Future Perspectives.pdf` | não | 919x371 | excluída | OK | baixo | 50/50/38/50 | provavel (1.00; 1 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch1_review_of_robotic_prostheses_manufa_figure1_p3.png` | `Review of Robotic Prostheses Manufactured with 3D Printing Advances, Challenges, and Future Perspectives.pdf` | não | 1175x447 | excluída | OK | baixo | 32/50/47/50 | possivel (0.64; 14 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 2

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch2_2d_and_3d_anatomical_analyses_of_ha_figure1_p3.png` | `2D and 3D anatomical analyses of hand dimensions for custom-made gloves.pdf` | sim | 1126x832 | excluída | OK | baixo | 32/50/45/50 | nao_detectada (0.21; 13 comp.) | OK pós-recorte |
| `figuras/ch2_2d_and_3d_anatomical_analyses_of_ha_figure4_p4.png` | `2D and 3D anatomical analyses of hand dimensions for custom-made gloves.pdf` | não | 786x625 | excluída | OK | baixo | 32/50/44/50 | provavel (1.00; 10 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_3d_printed_upper_limb_prostheses_a_figure2_p5.png` | `3D-printed upper limb prostheses a review.pdf` | sim | 1283x1229 | excluída | OK | baixo | 32/50/32/52 | provavel (1.00; 11 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_3d_printed_upper_limb_prostheses_a_figure3_p5.png` | `3D-printed upper limb prostheses a review.pdf` | não | 669x555 | excluída | OK | baixo | 52/50/32/54 | provavel (0.84; 46 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_3d_printed_upper_limb_prostheses_a_figure4_p6.png` | `3D-printed upper limb prostheses a review.pdf` | não | 1251x964 | excluída | OK | baixo | 50/50/32/50 | provavel (0.90; 54 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_3d_printed_upper_limb_prostheses_a_figure8_p11.png` | `3D-printed upper limb prostheses a review.pdf` | não | 668x410 | excluída | OK | baixo | 51/50/32/52 | possivel (0.43; 18 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_framework_for_configuring_partici_figure1_p4.png` | `A framework for configuring participation in living labs.pdf` | sim | 597x154 | excluída | OK | baixo | 32/32/46/50 | nao_detectada (0.03; 0 comp.) | OK pós-recorte |
| `figuras/ch2_a_framework_for_configuring_partici_figure6_p12.png` | `A framework for configuring participation in living labs.pdf` | não | 1843x596 | excluída | OK | baixo | 32/50/50/50 | provavel (1.00; 77 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_framework_to_study_human_ai_colla_figure12_p31.png` | `A Framework to Study Human-AI Collaborative Design Space Exploration (2021).pdf` | não | 953x515 | excluída | OK | baixo | 32/50/49/50 | provavel (0.74; 50 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_framework_to_study_human_ai_colla_figure14_p46.png` | `A Framework to Study Human-AI Collaborative Design Space Exploration (2021).pdf` | não | 1252x629 | excluída | OK | baixo | 50/50/32/50 | provavel (1.00; 484 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_review_of_technology_materials_an_figure2_p2.png` | `A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. .pdf` | não | 494x781 | excluída | OK | baixo | 50/50/34/52 | possivel (0.48; 13 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_review_of_technology_materials_an_figure7_p4.png` | `A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. .pdf` | não | 657x334 | excluída | OK | baixo | 32/50/37/51 | nao_detectada (0.30; 3 comp.) | OK pós-recorte |
| `figuras/ch2_a_review_of_technology_materials_an_figure8_p4.png` | `A review of technology, materials and R&D challenges of upper limb prosthesis for improved user suitability. .pdf` | não | 1472x618 | excluída | OK | baixo | 50/50/35/50 | provavel (1.00; 132 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure10_p9.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | sim | 1461x1042 | excluída | OK | baixo | 51/51/33/51 | provavel (1.00; 183 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure11_p10.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1521x1231 | excluída | OK | baixo | 32/50/33/50 | provavel (1.00; 192 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure12_p11.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1461x1021 | excluída | OK | baixo | 50/51/33/52 | provavel (1.00; 229 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure14_p13.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1459x1063 | excluída | OK | baixo | 51/52/33/51 | provavel (1.00; 259 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure1_p2.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | sim | 753x196 | excluída | OK | baixo | 32/50/32/50 | provavel (0.67; 31 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure7_p7.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1461x572 | excluída | OK | baixo | 50/50/33/50 | provavel (1.00; 85 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_a_scoping_review_of_digital_fabrica_figure9_p8.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1521x1072 | excluída | OK | baixo | 32/50/33/50 | provavel (1.00; 103 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_ai_driven_computer_aided_design_cad_figure1_p6.png` | `AI-DRIVEN COMPUTER-AIDED DESIGN CAD SYSTEMS LEVERAGING NEURAL NETWORKS FOR OPTIMIZED ENGINEERING PRODUCT DEVELOPMENT (2025).pdf` | sim | 1304x604 | excluída | OK | baixo | 52/51/61/51 | possivel (0.62; 34 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_ai_driven_computer_aided_design_cad_figure4_p9.png` | `AI-DRIVEN COMPUTER-AIDED DESIGN CAD SYSTEMS LEVERAGING NEURAL NETWORKS FOR OPTIMIZED ENGINEERING PRODUCT DEVELOPMENT (2025).pdf` | não | 1258x944 | excluída | OK | baixo | 32/51/51/51 | provavel (1.00; 60 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_ai_in_co_creation_the_usability_and_figure6_p6.png` | `AI in Co-Creation_ The usability and impact of AI tools for cocreation in participatory design to generate innovative and user-centric design solution.pdf` | não | 579x545 | excluída | OK | baixo | 47/50/35/50 | possivel (0.50; 24 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_ai_in_co_creation_the_usability_and_figure7_p7.png` | `AI in Co-Creation_ The usability and impact of AI tools for cocreation in participatory design to generate innovative and user-centric design solution.pdf` | não | 788x184 | excluída | OK | baixo | 32/50/35/50 | nao_detectada (0.01; 0 comp.) | OK pós-recorte |
| `figuras/ch2_an_affordable_ai_driven_and_3d_prin_figure11_p12.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x620 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 246 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_an_affordable_ai_driven_and_3d_prin_figure1_p3.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x992 | excluída | OK | baixo | 32/50/48/50 | provavel (1.00; 165 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_an_affordable_ai_driven_and_3d_prin_figure8_p9.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x824 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 46 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_an_introductory_study_of_common_gra_figure1_p3.png` | `An introductory study of common grasps used by adults during performance of activities of daily living.pdf` | não | 575x926 | excluída | OK | baixo | 51/32/44/50 | provavel (1.00; 10 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_an_introductory_study_of_common_gra_figure4_p5.png` | `An introductory study of common grasps used by adults during performance of activities of daily living.pdf` | não | 1065x816 | excluída | OK | baixo | 32/51/45/50 | provavel (1.00; 22 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_applying_3d_scanning_and_printing_t_figure3_p7.png` | `Applying 3D Scanning and Printing Techniques to Produce Upper Limb Prostheses Bibliometric Analysis and Scoping Review.pdf` | não | 1432x1067 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 154 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_automated_design_and_rapid_manufact_figure1_p4.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 779x442 | excluída | OK | baixo | 50/50/32/50 | provavel (1.00; 67 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_automated_design_and_rapid_manufact_figure2_p4.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 1361x296 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 220 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_biometric_analysis_hand_parameters_figure1_p2.png` | `Biometric analysis hand parameters in young adults for prosthetic hand and ergonomic product applications.pdf` | não | 1476x131 | excluída | OK | baixo | 50/50/50/50 | nao_detectada (0.00; 0 comp.) | OK pós-recorte |
| `figuras/ch2_biometric_analysis_hand_parameters_figure3_p3.png` | `Biometric analysis hand parameters in young adults for prosthetic hand and ergonomic product applications.pdf` | não | 1421x715 | excluída | OK | baixo | 41/50/32/51 | provavel (1.00; 308 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_d_mcdonagh_innovating_alongside_des_figure5_p4.png` | `D-McDonagh-Innovating-alongside-designers.pdf` | não | 806x536 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 243 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_designing_industrial_design_in_the_figure1_p7.png` | `Designing Industrial Design in the Highly Regulated Medical Device Development Process. Defining our valuable contribution towards usability.pdf` | não | 824x426 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 21 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_designing_industrial_design_in_the_figure2_p7.png` | `Designing Industrial Design in the Highly Regulated Medical Device Development Process. Defining our valuable contribution towards usability.pdf` | não | 657x1457 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 13 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_estimation_of_anthropometric_hand_m_figure1_p3.png` | `Estimation of anthropometric hand measurements using the ratio scaling method for the design of sewn gloves.pdf` | não | 359x143 | excluída | OK | baixo | 32/51/32/50 | nao_detectada (0.04; 2 comp.) | OK pós-recorte |
| `figuras/ch2_fit_comparison_of_custom_casts_crea_figure1_p5.png` | `Fit Comparison of Custom Casts Created Through Photogrammetry FDM Rapid-Prototyping of Ipsilateral Versus Mirrored Contr (2025).pdf` | não | 1401x1211 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 23 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_hand_anthropometric_measurement_and_figure1_p2.png` | `HAND ANTHROPOMETRIC MEASUREMENT AND GRIP STRENGTH FOR BASKETBALL AND.pdf` | não | 450x412 | excluída | OK | baixo | 33/50/32/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_implementation_of_3d_printing_techn_figure5_p8.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | sim | 1125x595 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 3 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_implementation_of_3d_printing_techn_figure6_p8.png` | `Implementation of 3D Printing Technology in the Field of Prosthetics Past, Present, and Future.pdf` | não | 1102x645 | excluída | OK | baixo | 32/50/50/50 | nao_detectada (0.24; 12 comp.) | OK pós-recorte |
| `figuras/ch2_integrating_generative_design_and_t_figure2_p5.png` | `Integrating generative design and topology optimisation with product design values (2022).pdf` | não | 1130x1237 | excluída | OK | baixo | 32/50/56/51 | provavel (1.00; 103 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_integrating_generative_design_and_t_figure7_p8.png` | `Integrating generative design and topology optimisation with product design values (2022).pdf` | não | 1187x955 | excluída | OK | baixo | 32/50/50/50 | provavel (1.00; 126 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_open_source_3d_printing_in_the_pros_figure1_p3.png` | `Open-Source 3D Printing in the Prosthetic Field—The Case of Upper Limb Prostheses A Review.pdf` | não | 1555x780 | excluída | OK | baixo | 46/50/50/50 | provavel (1.00; 104 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_prosthesis_rejection_in_acquired_ma_figure1_p4.png` | `Prosthesis rejection in acquired major upper-limb amputees a population-based survey.pdf` | sim | 766x548 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 146 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_rethinking_designer_agency_a_case_s_figure1_p4.png` | `Rethinking designer agency A case study of co-creation between designers and AI.pdf` | não | 1301x727 | excluída | OK | baixo | 53/50/50/50 | provavel (1.00; 228 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_rethinking_designer_agency_a_case_s_figure2_p13.png` | `Rethinking designer agency A case study of co-creation between designers and AI.pdf` | não | 1298x519 | excluída | OK | baixo | 50/50/50/50 | provavel (0.69; 38 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_shaping_the_future_of_upper_extremi_figure1_p5.png` | `Shaping the Future of Upper Extremity Prostheses Through 3D Printing.pdf` | não | 914x846 | excluída | OK | baixo | 32/50/50/50 | provavel (0.94; 15 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_shaping_the_future_of_upper_extremi_figure2_p6.png` | `Shaping the Future of Upper Extremity Prostheses Through 3D Printing.pdf` | não | 1555x1098 | excluída | OK | baixo | 47/50/49/50 | provavel (1.00; 87 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_shaping_the_future_of_upper_extremi_figure8_p12.png` | `Shaping the Future of Upper Extremity Prostheses Through 3D Printing.pdf` | não | 1499x911 | excluída | OK | baixo | 32/51/51/51 | provavel (0.96; 61 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_shaping_the_future_of_upper_extremi_figure9_p13.png` | `Shaping the Future of Upper Extremity Prostheses Through 3D Printing.pdf` | não | 1555x982 | excluída | OK | baixo | 47/50/50/50 | provavel (0.77; 18 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch2_the_current_state_of_3d_printed_pro_figure1_p4.png` | `The Current State of 3D-Printed Prostheses Clinical Outcomes: A Systematic Review.pdf` | não | 1555x1299 | excluída | OK | baixo | 47/50/50/50 | nao_detectada (0.26; 16 comp.) | OK pós-recorte |
| `figuras/ch2_understanding_user_perceptions_coll_figure3_p7.png` | `Understanding User Perceptions Collaborative Experience and User Engagement in Different Human-AI Interaction Designs fo (2022).pdf` | não | 1198x974 | excluída | OK | baixo | 32/51/50/50 | provavel (1.00; 225 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 3

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch3_a_method_for_3_d_printing_patient_s_figure1_p4.png` | `A_Method_for_3-D_Printing_Patient-Specific_Prosthetic_Arms_With_High_Accuracy_Shape_and_Size.pdf` | não | 691x351 | excluída | OK | baixo | 32/50/50/50 | provavel (1.00; 1 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_a_method_for_3_d_printing_patient_s_figure2_p4.png` | `A_Method_for_3-D_Printing_Patient-Specific_Prosthetic_Arms_With_High_Accuracy_Shape_and_Size.pdf` | não | 1496x617 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 12 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_a_scoping_review_of_digital_fabrica_figure3_p4.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1521x775 | excluída | OK | baixo | 32/50/42/50 | provavel (1.00; 292 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_an_undergraduate_engineering_servic_figure1_p4.png` | `An Undergraduate Engineering Service Learning Project Involving 3D-Printed Prosthetic Hands for Children.pdf` | sim | 1273x425 | excluída | OK | baixo | 33/50/50/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_an_undergraduate_engineering_servic_figure4_p6.png` | `An Undergraduate Engineering Service Learning Project Involving 3D-Printed Prosthetic Hands for Children.pdf` | não | 1156x649 | excluída | OK | baixo | 33/53/50/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch3_interdisciplinary_based_development_figure1_p2.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 1035x396 | excluída | OK | baixo | 32/50/50/51 | provavel (1.00; 95 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 4

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch4_a_data_driven_design_framework_for_figure1_p2.png` | `A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands.pdf` | não | 1529x668 | excluída | OK | baixo | 38/50/32/51 | provavel (1.00; 376 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_a_parametric_design_approach_for_af_figure2_p2.png` | `A_Parametric_Design_Approach_for_Affordable_Customized_3D_Socket_for_Transradial_Upper_Limb_Prostheses.pdf` | não | 1492x439 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 131 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_a_parametric_design_approach_for_af_figure4_p3.png` | `A_Parametric_Design_Approach_for_Affordable_Customized_3D_Socket_for_Transradial_Upper_Limb_Prostheses.pdf` | não | 631x380 | excluída | OK | baixo | 32/50/48/50 | provavel (0.67; 3 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_a_parametric_design_approach_for_af_figure9_p4.png` | `A_Parametric_Design_Approach_for_Affordable_Customized_3D_Socket_for_Transradial_Upper_Limb_Prostheses.pdf` | não | 1333x489 | excluída | OK | baixo | 50/50/32/50 | provavel (0.87; 37 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_a_u_iwuoha_design_and_3d_printing_o_figure15_p6.png` | `A U Iwuoha - Design and 3d-printing of a body-powered prosthetic limb for amputee.pdf` | não | 1591x519 | excluída | OK | baixo | 38/50/32/50 | provavel (1.00; 10 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_automated_design_and_rapid_manufact_figure12_p9.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 719x336 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_automated_design_and_rapid_manufact_figure13_p10.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 1016x401 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 2 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_automated_design_and_rapid_manufact_figure14_p10.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 776x401 | excluída | OK | baixo | 33/50/32/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_automated_design_and_rapid_manufact_figure5_p6.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 722x620 | excluída | OK | baixo | 51/50/32/50 | provavel (1.00; 81 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_automated_design_and_rapid_manufact_figure9_p8.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 625x623 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 34 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure1_p3.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | não | 251x123 | excluída | OK | baixo | 32/50/50/50 | nao_detectada (0.00; 0 comp.) | OK pós-recorte |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure5_p6.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | não | 801x496 | excluída | OK | baixo | 32/50/50/50 | provavel (1.00; 65 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure6_p6.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | não | 1520x518 | excluída | OK | baixo | 50/50/50/51 | possivel (0.62; 47 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_customization_of_a_3d_printed_prost_figure8_p7.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | sim | 801x380 | excluída | OK | baixo | 50/50/50/50 | possivel (0.65; 32 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_development_of_parametric_prosthese_figure19_p15.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1160x847 | excluída | OK | baixo | 32/51/49/51 | nao_detectada (0.28; 19 comp.) | OK pós-recorte |
| `figuras/ch4_development_of_parametric_prosthese_figure22_p18.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1555x552 | excluída | OK | baixo | 47/50/47/50 | nao_detectada (0.33; 6 comp.) | OK pós-recorte |
| `figuras/ch4_development_of_parametric_prosthese_figure23_p18.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 772x573 | excluída | OK | baixo | 32/50/48/50 | provavel (1.00; 2 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_development_of_parametric_prosthese_figure25_p19.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1111x526 | excluída | OK | baixo | 32/50/46/50 | nao_detectada (0.28; 6 comp.) | OK pós-recorte |
| `figuras/ch4_development_of_parametric_prosthese_figure5_p7.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1168x865 | excluída | OK | baixo | 50/50/44/50 | provavel (1.00; 177 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_development_of_parametric_prosthese_figure6_p8.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1555x1347 | excluída | OK | baixo | 47/50/50/50 | provavel (1.00; 317 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_development_of_parametric_prosthese_figure8_p10.png` | `Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing.pdf` | não | 1555x436 | excluída | OK | baixo | 47/50/49/50 | nao_detectada (0.25; 0 comp.) | OK pós-recorte |
| `figuras/ch4_enhancing_mobility_with_customized_figure6_p7.png` | `Enhancing mobility with customized prosthetic designs driven by genetic algorithms.pdf` | não | 1063x515 | excluída | OK | baixo | 32/50/49/50 | nao_detectada (0.34; 22 comp.) | OK pós-recorte |
| `figuras/ch4_interdisciplinary_based_development_figure8_p9.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 740x367 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 1 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_interdisciplinary_based_development_figure9_p9.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 626x539 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 10 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure1_p2.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | não | 760x450 | excluída | OK | baixo | 50/50/48/50 | provavel (0.92; 61 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure3_p2.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | sim | 490x364 | excluída | OK | baixo | 50/50/49/50 | possivel (0.46; 27 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure4_p3.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | não | 767x444 | excluída | OK | baixo | 50/50/50/50 | provavel (0.66; 19 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure7_p5.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | não | 636x370 | excluída | OK | baixo | 50/51/50/50 | possivel (0.47; 20 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure8_p5.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | não | 443x304 | excluída | OK | baixo | 50/50/51/50 | nao_detectada (0.17; 7 comp.) | OK pós-recorte |
| `figuras/ch4_parametric_3d_modeling_of_a_customi_figure9_p5.png` | `Parametric 3D Modeling of a Customized Prosthetic Hand Finger for Additive Manufacturing.pdf` | não | 629x373 | excluída | OK | baixo | 50/50/50/50 | provavel (0.66; 28 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 5

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch5_a_parametric_design_approach_for_af_figure10_p5.png` | `A_Parametric_Design_Approach_for_Affordable_Customized_3D_Socket_for_Transradial_Upper_Limb_Prostheses.pdf` | não | 1530x380 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 203 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_an_affordable_ai_driven_and_3d_prin_figure4_p5.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 696x271 | excluída | OK | baixo | 32/50/48/50 | possivel (0.42; 8 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_an_affordable_ai_driven_and_3d_prin_figure8_p9.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x824 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 46 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_automated_design_and_rapid_manufact_figure1_p4.png` | `Automated Design and Rapid Manufacturing of Low-Cost Customized Upper Limb Prostheses.pdf` | não | 779x442 | excluída | OK | baixo | 50/50/32/50 | provavel (1.00; 67 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_mixuan_li_parametric_design_and_thr_figure1_p4.png` | `Mixuan Li - Parametric design and three-dimensional printing enabling Occupational therapists to develop custom hand grips [2025]..pdf` | não | 1461x1191 | excluída | OK | baixo | 32/50/40/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_mixuan_li_parametric_design_and_thr_figure2_p5.png` | `Mixuan Li - Parametric design and three-dimensional printing enabling Occupational therapists to develop custom hand grips [2025]..pdf` | não | 766x614 | excluída | OK | baixo | 50/32/41/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch5_mixuan_li_parametric_design_and_thr_figure3_p7.png` | `Mixuan Li - Parametric design and three-dimensional printing enabling Occupational therapists to develop custom hand grips [2025]..pdf` | não | 1509x695 | excluída | OK | baixo | 50/50/41/50 | provavel (1.00; 9 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 6

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch6_a_data_driven_design_framework_for_figure1_p2.png` | `A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands.pdf` | não | 1529x668 | excluída | OK | baixo | 38/50/32/51 | provavel (1.00; 376 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_a_data_driven_design_framework_for_figure6_p5.png` | `A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands.pdf` | não | 1529x536 | excluída | OK | baixo | 38/50/50/51 | provavel (1.00; 111 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_a_data_driven_design_framework_for_figure8_p7.png` | `A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands.pdf` | não | 1529x516 | excluída | OK | baixo | 38/50/42/51 | provavel (1.00; 72 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_a_data_driven_design_framework_for_figure9_p7.png` | `A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands.pdf` | não | 1528x261 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 265 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_a_framework_to_study_human_ai_colla_figure12_p31.png` | `A Framework to Study Human-AI Collaborative Design Space Exploration (2021).pdf` | não | 953x515 | excluída | OK | baixo | 32/50/49/50 | provavel (0.74; 50 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_a_framework_to_study_human_ai_colla_figure14_p46.png` | `A Framework to Study Human-AI Collaborative Design Space Exploration (2021).pdf` | não | 1252x629 | excluída | OK | baixo | 50/50/32/50 | provavel (1.00; 484 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_an_affordable_ai_driven_and_3d_prin_figure6_p8.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x686 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 187 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_an_affordable_ai_driven_and_3d_prin_figure7_p8.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1459x740 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 103 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_customization_of_a_3d_printed_prost_figure6_p6.png` | `Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling.pdf` | não | 1520x518 | excluída | OK | baixo | 50/50/50/51 | possivel (0.62; 47 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_enhancing_mobility_with_customized_figure1_p4.png` | `Enhancing mobility with customized prosthetic designs driven by genetic algorithms.pdf` | não | 854x598 | excluída | OK | baixo | 51/51/49/54 | provavel (1.00; 77 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch6_rethinking_designer_agency_a_case_s_figure4_p14.png` | `Rethinking designer agency A case study of co-creation between designers and AI.pdf` | não | 1145x505 | excluída | OK | baixo | 50/50/50/50 | provavel (0.71; 46 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 7

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch7_an_undergraduate_engineering_servic_figure4_p6.png` | `An Undergraduate Engineering Service Learning Project Involving 3D-Printed Prosthetic Hands for Children.pdf` | não | 1156x649 | excluída | OK | baixo | 33/53/50/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_interdisciplinary_based_development_figure4_p6.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 529x496 | excluída | OK | baixo | 50/50/33/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_interdisciplinary_based_development_figure9_p9.png` | `Interdisciplinary-Based Development of User-Friendly Customized 3D Printed Upper Limb Prosthesis.pdf` | não | 626x539 | excluída | OK | baixo | 32/50/32/50 | provavel (1.00; 10 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_mixuan_li_parametric_design_and_thr_figure2_p5.png` | `Mixuan Li - Parametric design and three-dimensional printing enabling Occupational therapists to develop custom hand grips [2025]..pdf` | não | 766x614 | excluída | OK | baixo | 50/32/41/50 | provavel (1.00; 0 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_understanding_user_perceptions_coll_figure2_p6.png` | `Understanding User Perceptions Collaborative Experience and User Engagement in Different Human-AI Interaction Designs fo (2022).pdf` | não | 1288x603 | excluída | OK | baixo | 50/50/50/50 | possivel (0.44; 27 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_understanding_user_perceptions_coll_figure4_p8.png` | `Understanding User Perceptions Collaborative Experience and User Engagement in Different Human-AI Interaction Designs fo (2022).pdf` | não | 1289x391 | excluída | OK | baixo | 50/50/50/50 | provavel (1.00; 141 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch7_understanding_user_perceptions_coll_figure5_p10.png` | `Understanding User Perceptions Collaborative Experience and User Engagement in Different Human-AI Interaction Designs fo (2022).pdf` | não | 1179x742 | excluída | OK | baixo | 50/50/32/50 | provavel (1.00; 106 comp.) | OK pós-recorte; revisão visual opcional |

### Capítulo 8

| Ficheiro | PDF de origem | Usada | Dimensões | Legenda original | Margem | Risco | Margens px topo/direita/baixo/esquerda | Sinal textual residual | Estado actual |
| --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| `figuras/ch8_a_method_for_3_d_printing_patient_s_figure4_p6.png` | `A_Method_for_3-D_Printing_Patient-Specific_Prosthetic_Arms_With_High_Accuracy_Shape_and_Size.pdf` | não | 1496x1010 | excluída | OK | baixo | 32/50/60/50 | provavel (1.00; 157 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch8_a_method_for_3_d_printing_patient_s_figure5_p7.png` | `A_Method_for_3-D_Printing_Patient-Specific_Prosthetic_Arms_With_High_Accuracy_Shape_and_Size.pdf` | não | 1496x921 | excluída | OK | baixo | 32/50/53/50 | provavel (1.00; 179 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch8_a_scoping_review_of_digital_fabrica_figure3_p4.png` | `A scoping review of digital fabrication techniques applied to prosthetics and orthotics.pdf` | não | 1521x775 | excluída | OK | baixo | 32/50/42/50 | provavel (1.00; 292 comp.) | OK pós-recorte; revisão visual opcional |
| `figuras/ch8_an_affordable_ai_driven_and_3d_prin_figure10_p11.png` | `An_Affordable_AI-Driven_and_3D-Printed_Personalized_Myoelectric_Prosthesis_Design_Development_and_Assessment.pdf` | não | 1496x937 | excluída | OK | baixo | 32/50/41/50 | provavel (1.00; 11 comp.) | OK pós-recorte; revisão visual opcional |
