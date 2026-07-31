# Notes — Capítulo 6.1

## Objective
Estabelecer o papel da IA no sistema proposto como camada de apoio à personalização, sugestão de parâmetros e apoio à decisão, sem a apresentar como substituto do modelo paramétrico nem da supervisão humana.

## Key Findings

- A pesquisa no Elicit confirma que existe literatura relevante sobre IA em próteses de membro superior, embora uma parte importante esteja centrada em controlo mioelétrico, classificação de biosinais e interfaces homem-máquina.
- A literatura mais útil para este projeto é a que posiciona a IA como **assistive layer**, isto é, como mecanismo de apoio dentro de workflows digitais mais amplos.
- O primeiro report de `6.1` reforça uma conclusão importante: a literatura atual continua **fragmentada** e não descreve sistemas completos que integrem, ao mesmo tempo, entrada antropométrica, CAD paramétrico explícito, sugestão de parâmetros por IA, supervisão clínica/técnica e fabrico por impressão 3D.
- O mesmo report mostra que a IA é usada predominantemente para:
  - interpretação de biosinais
  - controlo motor
  - reconhecimento de gestos
  - adaptação funcional
  e muito menos para mapeamento explícito entre antropometria e parâmetros CAD.
- O projeto em causa diferencia-se de abordagens puramente generativas ou de controlo porque:
  - mantém a geometria num modelo paramétrico explícito em OpenSCAD
  - usa a IA para sugerir parâmetros, não para substituir a estrutura do modelo
  - preserva revisão humana por clínico/protésico
  - integra renderização local em WASM e inferência segura no servidor
- A ausência de mecanismos claros de `clinician oversight` na literatura encontrada é, por si só, um argumento importante para a relevância da arquitetura proposta no projeto.
- O ruído principal nas pesquisas vem de `prosthodontics` e workflows dentários. Esses resultados só devem ser usados se contribuírem para conceitos transferíveis como CAD/CAM, apoio à decisão, personalização digital ou AI-assisted design.
- Até agora, os resultados mais promissores para `6.1` são:
  - *An Affordable AI-Driven and 3D-Printed Personalized Myoelectric Prosthesis: Design, Development, and Assessment*
  - *A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands*
  - *Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing*
  - *A Parametric Design Approach for Affordable Customized 3D Socket for Transradial Upper Limb Prostheses*
  - *Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling*
  - *Applying 3D Scanning and Printing Techniques to Produce Upper Limb Prostheses: Bibliometric Analysis and Scoping Review*

## Relevant Bibliography

- Romero, Enzo et al. *An Affordable AI-Driven and 3D-Printed Personalized Myoelectric Prosthesis: Design, Development, and Assessment*
- Gu, Yu et al. *A Data-Driven Design Framework for Structural Optimization to Enhance Wearing Adaptability of Prosthetic Hands*
- *Development of Parametric Prostheses for Different Levels of Human Hand Amputations Manufactured Through Additive Manufacturing*
- *A Parametric Design Approach for Affordable Customized 3D Socket for Transradial Upper Limb Prostheses*
- *Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling*
- *Applying 3D Scanning and Printing Techniques to Produce Upper Limb Prostheses: Bibliometric Analysis and Scoping Review*

## Working Shortlist

Primary anchors:

- Romero et al.
- Gu et al.
- *Development of Parametric Prostheses...*
- *A Parametric Design Approach for Affordable Customized 3D Socket...*

Support papers:

- *Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling*
- *Applying 3D Scanning and Printing Techniques...*

## Open Questions for 6.2

- How exactly does literature describe the translation from anthropometric input to configurable design parameters?
- Which papers discuss AI as support for parameter recommendation rather than autonomous generation?
- What evidence exists for combining anthropometric datasets, parametric CAD, and additive manufacturing in personalized prosthetic workflows?
