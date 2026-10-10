# PDFs em falta — bibliografia do manuscrito atual

Última verificação: 10 de outubro de 2026.

Fonte: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`, sincronizada no Markdown **0.4.114**. Este inventário substitui a lista relativa ao DOCX anterior, entretanto arquivado.

## Síntese

- 283 parágrafos bibliográficos no ODT, correspondentes a 158 entradas textuais distintas e 125 ocorrências repetidas. A contagem distingue textos, não necessariamente obras.
- 149 entradas com correspondência PDF local segundo as regras de DOI, título e associações anteriormente auditadas.
- 5 recursos institucionais, normativos, bases de dados ou repositórios sem PDF autónomo esperado neste inventário.
- 3 entradas completas sem PDF localizado e 1 entrada truncada que exige identificação bibliográfica.

## Entradas sem PDF localizado

| Referência | Título | Localização |
| --- | --- | --- |
| Adel (2020) | Progress in Polyethylene Terephthalate Recycling | https://hal.archives-ouvertes.fr/hal-02953197 |
| Gonzalez Avila (2024) | Facilitating Programming-Based 3D Computer-Aided Design Using Bidirectional Programming [Thesis] | https://hal.science/tel-04635570 |
| Li (2020) | An investigation of a generative parametric design approach for a robust solution development | https://doi.org/10.1017/dsd.2020.273 |

## Entrada truncada por esclarecer

- Texto presente no ODT: `Baumann, Mearch and Development Academy. https://doi.org/10.37868/sei.v5i1.id185`
- A conferência sequencial posterior identificou uma mistura de referências: o DOI pertence à entrada completa de Chtioui, Gaha e Benamara (2023), cujo PDF local é `Design_for_additive_manufacturing_Review_and_frame.pdf`. O restante texto de Baumann e Maria (2023) surge indevidamente anexado à primeira ocorrência de Østlie et al. (2012); existe também `baumann_maria_2023_prosthetic_limbs_germany.pdf`. Trata-se, portanto, de uma pendência de reconstrução bibliográfica, não de uma nova obra sem PDF. A classificação automática da entrada truncada em `bibliografia_local.json` deve ser lida à luz desta conferência manual, detalhada no relatório de sincronização e em `repeticoes_bibliografia.csv`.

## Recursos sem PDF autónomo esperado

- ASTM International. (2024). Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers. ASTM International. https://doi.org/10.1520/F3661-24
- daprice. (n.d.). Flexy Beast. GitHub. https://github.com/daprice/Flexy-Beast
- Delft University of Technology. (n.d.). DINED: 1D anthropometric database. https://dined.io.tudelft.nl/en/database/tool
- International Organization for Standardization. (n.d.). ISO/TC 168 - Prosthetics and orthotics. https://www.iso.org/committee/53630.html
- Brooks, C. (2026). OpenSCAD Web. GitHub. https://github.com/CameronBrooks11/openscad-web

## Método e limites

Confronto da bibliografia do ODT com os PDFs de `material/bibliografia/` e das restantes pastas de `material/`, reutilizando as regras locais de correspondência. As repetições exatas foram colapsadas apenas para este inventário; o manuscrito mantém a bibliografia da fonte. Três PDFs encontrados noutras pastas foram copiados para a pasta bibliográfica, preservando os originais.

A disponibilidade local não valida a adequação das citações, a exatidão dos metadados ou a conformidade integral com APA 7. As correspondências automáticas não equivalem a uma nova leitura integral dos artigos. O inventário completo, os critérios e as cópias estão registados em `docs/revisoes/manuscrito/sincronizacao_markdown_2026_10_10/bibliografia_local.json` e `pdfs_copiados.json`.

```bash
python3 docs/revisoes/manuscrito/sincronizacao_markdown_2026_10_10/conferir_bibliografia.py
```

O script regenera o inventário JSON; esta síntese e as decisões sobre entradas incompletas são revistas manualmente. Molenbroek (2003) e Steenbekkers (1998), constantes da lista anterior, não aparecem como entradas na bibliografia atual extraída; por isso deixaram de integrar a lista corrente de PDFs em falta.
