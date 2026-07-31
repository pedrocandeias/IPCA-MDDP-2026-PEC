# Auditoria da completude bibliográfica do DOCX canónico

- Documento: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`
- SHA-256: `cd38830d659707c2df46a549458010b8bdd52f3caeff33b1fc4e174988b76ad2`
- Fonte autoritativa das citações: **DOCX canónico**; o Markdown não foi lido.
- Intervalo materializado da bibliografia: parágrafos XML 2260–2591.
- Entradas bibliográficas lógicas: **171**.
- Controlos de citação Mendeley: **228**.
- Itens citados nos controlos: **375 ocorrências; 150 fontes únicas**.
- Menções autor–ano fora dos controlos Mendeley: **57**.
- Notas de rodapé: **11 referências; 11 definições**.
- Comentários: **0**.

## Veredicto

**A bibliografia do DOCX não está completa nem internamente coerente.** Foram confirmadas 13 lacunas ou incompatibilidades de fonte: 9 fontes vivas sem entrada coerente ou ligadas à obra errada e 4 atribuições manuais sem formalização bibliográfica suficiente. Acrescem 11 divergências de ano, anomalias formais nas citações e problemas materiais na lista de referências; estes pontos também impedem a aprovação da completude bibliográfica.

A disponibilidade local de PDFs é uma dimensão separada. Deve ser lida em `material/bibliografia/consolidacao_referencias_docx.md`, gerado directamente a partir desta mesma bibliografia do Word.

## 1. Fontes vivas sem entrada coerente ou com alvo incompatível

| Ocorrências | Citação apresentada | Fonte incorporada no Mendeley | Classificação | Diagnóstico |
| ---: | --- | --- | --- | --- |
| 1 | Østlie et al. (2011) | *Adult acquired major upper limb amputation in Norway: Prevalence, demographic features and amputation specific features. A population-based survey* | alvo de citação incompatível | O controlo aponta para o artigo de Østlie et al. (2011), mas a passagem, a legenda e a bibliografia usam o estudo distinto de Østlie et al. (2012). |
| 2 | (Parlamento Europeu e do Conselho Europeu, 2017) / Regulamento (UE) 2017/745 (2017) | *REGULAMENTO (UE)  2017/  745  DO  PARLAMENTO  EUROPEU  E  DO  CONSELHO* | entrada ausente | O Regulamento (UE) 2017/745 é citado duas vezes, mas não possui entrada na bibliografia materializada do DOCX. |
| 1 | (Resnik et al., 2022) | *Measuring Satisfaction With Upper Limb Prostheses: Orthotics and Prosthetics User Survey Revision That Includes Issues of Concern to Women* | alvo de citação incompatível | O controlo aponta para Resnik et al. (2022), sobre satisfação com próteses, enquanto a passagem regulatória e a bibliografia correspondem a Resnik et al. (2010). |
| 1 | (International Organization for Standardization, 2020 | *Prosthetics and orthotics-Vocabulary-Part 3: Terms relating to orthoses Prothèses et orthèses-Vocabulaire-Partie 3: Termes relatifs aux orthèses ISO 8549-3:2020(E) ii COPYRIGHT PROTECTED DOCUMENT* | alvo de citação incompatível | O controlo contém a ISO 8549-3:2020, relativa a ortóteses; o texto e a bibliografia invocam a ISO 8549-1:2020. |
| 1 | (Khanolkar et al., 2023; H. Li et al., 2020) | *AN INVESTIGATION of A GENERATIVE PARAMETRIC DESIGN APPROACH for A ROBUST SOLUTION DEVELOPMENT* | entrada ausente | Li et al. (2020), DOI 10.1017/dsd.2020.273, é citado, mas não possui entrada bibliográfica. |
| 1 | (Mikołajewska & Mikołajewski, 2014; Zhu & Zhong, 2022) | *Integrated IT environment for people with disabilities: A new concept* | entrada ausente | Mikołajewska e Mikołajewski (2014), DOI 10.2478/s11536-013-0254-6, é citado, mas não possui entrada bibliográfica. |
| 1 | (The Design Council, 2007) | *The Double Diamond* | entrada ausente | The Design Council (2007), *The Double Diamond*, é citado; a bibliografia contém apenas a fonte institucional distinta do Design Council (2020). |
| 2 | (Biddiss & Chau, 2007; Brack & Amalu, 2021; Henao et al., 2026; Walker et al., 2020) / (Biddiss & Chau, 2007; Cordella et al., 2016) | *Upper limb prosthesis use and abandonment: A survey of the last 25 years* | entrada ausente e colisão autor–ano | Biddiss e Chau (2007), DOI 10.1080/03093640600994581, é uma obra distinta da entrada Biddiss, Beaton e Chau (2007) já existente. |
| 2 | (ELhadad et al., 2025; Gonzalez Avila, 2024; Schöfer & Seibel, 2025) / (Gonzalez Avila, 2024; Trautmann, 2021) | *Faciliting programming based 3D Computer-aided design using bidirectional programming* | alvo de citação incompatível | O controlo de Gonzalez Avila (2024) contém *Faciliting programming based 3D Computer-aided design using bidirectional programming*, mas a entrada bibliográfica corresponde a *Understanding the challenges of OpenSCAD users for 3D printing*. |

## 2. Atribuições manuais sem formalização suficiente

| Parágrafo XML | Marcador localizado | Classificação | Diagnóstico |
| ---: | --- | --- | --- |
| 1748 | `M. Mendenhall (2020)` | entrada ausente | A origem do Paraglider/Flexible Flyer é indicada em formato autor–ano, mas não existe referência completa. |
| 2786 | `Fonte: artigo metodológico sobre reconstrução de modelos corporais 3D` | citação e entrada ausentes | A fonte foi identificada como Zhou et al. (2016), DOI 10.1016/j.ergon.2015.10.007, mas continua anónima no Anexo A. |
| 1758 | `MakerBlock/e-NABLE; CC BY-NC-SA 3.0` | referência técnica incompleta | A atribuição do Cyborg Beast não identifica URL, versão, revisão nem uma entrada bibliográfica completa. |
| 1753 | `UnLimbited/e-NABLE; CC BY-NC-SA 4.0` | referência técnica incompleta | A atribuição deve identificar Stephen Robert Davies, Drew Murray, Team UnLimbited, a versão V1.0, o URL e a revisão consultada. |

O varrimento automático das menções autor–ano escritas directamente no Word encontrou **57** ocorrências fora dos controlos Mendeley; foram identificadas **2** sem autor correspondente na bibliografia materializada e **1** com autor correspondente, mas ano divergente:

| Estado | Parágrafo XML | Menção | Contexto |
| --- | ---: | --- | --- |
| autor ausente | 573 | Parlamento Europeu & Conselho da União Europeia (2017) | …de uso real ao longo do ciclo de vida do dispositivo, o que reforça a natureza regulada e iterativa deste domínio, bem como a necessidade de sustentar a sua evolução em evidência (Parlamento Europeu & Conselho da União Europeia, 2017). |
| autor ausente | 1748 | M. Mendenhall (2020) | M. Mendenhall (2020), CC BY-SA 4.0; dependências CC BY 3.0 e CC BY-NC-SA 4.0 |
| ano divergente | 880 | Marinelli et al. (2023) | …componentes diretamente associados ao conforto, como os revestimentos de interface. Esta limitação reduz a compreensão dos fatores que condicionam a adoção, a continuidade de uso e(Marinelli et al., 2023; Richardson & Dillon, 2017; Walters et al., 2025). |

## 3. Anos apresentados que divergem da entrada bibliográfica auditada

| Fonte | Ano incorporado | Ano bibliográfico auditado | Citações apresentadas |
| --- | ---: | ---: | --- |
| van Niekerk et al. | 2021 | 2018 | (Van Niekerk et al., 2021) |
| Howard, Fisher, et al. | 2020 | 2022 | (Howard et al., 2020) |
| Howard, Davies, et al. | 2024 | 2022 | (Dechev et al., 2023; Howard et al., 2024; Sims et al., 2017) / (Fischer G et al., sem data; Howard et al., 2024; Von Hippel & Katz, 2002) / (Frangos et al., 2019; Howard et al., 2024; Thorsen et al., 2024) |
| Kuhl et al. | 2021 | 2020 | (Kuhl et al., 2021; Zhu & Zhong, 2022) |
| Thorsen et al. | 2024 | 2023 | (Frangos et al., 2019; Howard et al., 2024; Thorsen et al., 2024) / (Hussaini et al., 2023; Thorsen et al., 2024) / (Thorsen et al., 2024) |
| Frangos et al. | 2019 | 2016 | (Akasaka et al., 2022b; Frangos et al., 2019) / (Frangos et al., 2019; Howard et al., 2024; Thorsen et al., 2024) / (Frangos et al., 2019; Hussaini et al., 2023; Kerr et al., 2024) |
| Marinelli et al. | 2023 | 2022 | (Cordella et al., 2016; Marinelli et al., 2023) / (Cordella et al., 2016; Marinelli et al., 2023; Peerdeman et al., 2011) / (Domínguez-Ruiz et al., 2023; Marinelli et al., 2023) / Marinelli et al. (2023) / rdson & Dillon, 2017; Walters et al., 2025) |
| Henao et al. | 2026 | 2025 | (Biddiss & Chau, 2007; Brack & Amalu, 2021; Henao et al., 2026; Walker et al., 2020) |
| ELhadad et al. | 2025 | 2026 | (ELhadad et al., 2025; Gonzalez Avila, 2024; Schöfer & Seibel, 2025) |
| Barredo Arrieta et al. | 2019 | 2020 | (Arrieta et al., 2019) |
| Gordon et al. | 2014 | 2015 | (Gordon et al., 2014) |

## 4. Integridade material da lista bibliográfica

- Controlos Mendeley de bibliografia encontrados: **1**; o controlo existente está vazio e as entradas são parágrafos normais, pelo que um *Refresh* não garante a preservação da lista actual.
- Parágrafos autónomos que são continuação por URL/DOI: **3** (2290, 2549, 2566).
- DOI duplicados: **0**.
- Títulos normalizados duplicados: **0**.
- A entrada da IEC 62366-1:2015 está mutilada: «International Electrotechnical Commission. (2015). Internacional» seguida do URL.

## 5. Entradas potencialmente órfãs

A lista seguinte é conservadora: exclui as correspondências por DOI/título dos itens Mendeley e as citações autor–ano detectadas fora da bibliografia. Exige decisão humana porque alguns recursos técnicos podem ser mencionados sem a forma autor–ano.

| Parágrafo XML | Entrada |
| ---: | --- |
| 2266 | Akyol, E., Cabral Ramos Mota, R. C., & Somanath, S. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (Article 437, pp. 1-6). ACM. https://doi.org/10.1145/3411763.3451716 |
| 2279 | ASTM International. (2024). Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers. https://www.astm.org/f3661-24.html |
| 2287 | Baron, A., Gatzweiler, C., Geislinger, A., Huber, C., & Aszmann, O. C. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 274-287. https://doi.org/10.3390/prosthesis2040021 |
| 2309 | Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2831907 |
| 2343 | Design Council. (2020). Framework for innovation. https://www.designcouncil.org.uk/our-resources/framework-for-innovation/ |
| 2345 | Dexter, M., Crooks, E., Davies, P., & Simm, W. (2013). Open design and cystic fibrosis: Enabling participation in the design process. |
| 2351 | Elbreki, A. M., Alshari, K., Ramdan, S., & Rajab, Z. (2022). Practical design of an upper prosthetic limb using three dimensional printer with an artificial intelligence based controller. In 2022 International Conference on Engineering & MIS (ICEMIS). IEEE. https://doi.org/10.1109/ICEMIS56295.2022.9914291 |
| 2384 | Govender, R., Abrahmsén-Alami, S., Larsson, A., Borde, A., Liljeblad, A., & Folestad, S. (2020). Independent tailoring of dose and drug release via a modularized product design concept for mass customization. Pharmaceutics. |
| 2396 | Herneth, T., Hiesl, A., Stief, F., & Farago, D. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1-8). IEEE. https://doi.org/10.1109/IROS58592.2024.10801868 |
| 2400 | Hofmann, M. H., Griffiths, D., & Margetts, E. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858346 |
| 2416 | Idris, M. Z., Hashim, M. E. A. H. B., Albakry, N., & Septian, N. (2024). Exploring the integration of artificial intelligence in co-design framework for designer. https://ebpj.e-iph.co.uk/index.php/EBProceedings/article/download/6348/3640 |
| 2454 | Lindell, E., Tingsvik, H., Guo, L., & Peterson, J. (2021). 3D body scan as anthropometric tool for individualized prosthetic socks. https://sciendo.com/pdf/10.2478/aut-2021-0007 |
| 2468 | Mikołajewski, D., Rojek, I., Kotlarz, P., Dorożyński, J., & Kopowski, J. (2023). Personalization of the 3D-printed upper limb exoskeleton design: Mechanical and IT aspects. Applied Sciences. |
| 2474 | Molenbroek, J. F. M. (1998). Geron study on Dutch elderly anthropometry. DINED database. Delft University of Technology. https://dined.io.tudelft.nl |
| 2476 | Molenbroek, J. F. M., Kroon-Ramaekers, Y. M. T., & Snijders, C. J. (2003). Revision of the Dutch standard for furniture in schools. Ergonomics, 46(5), 491-498. https://doi.org/10.1080/0014013031000085635 |
| 2491 | OpenSCAD Community. (n.d.). OpenSCAD User Manual/Using OpenSCAD in a command line environment. Wikibooks. Retrieved July 7, 2026, from https://en.wikibooks.org/wiki/OpenSCADUserManual/UsingOpenSCADinacommandlineenvironment |
| 2492 | OpenSCAD Project. (n.d.-a). OpenSCAD: The programmers solid 3D CAD modeller. Retrieved July 7, 2026, from https://openscad.org/ |
| 2494 | OpenSCAD Project. (n.d.-b). OpenSCAD source repository [Computer software]. GitHub. Retrieved July 7, 2026, from https://github.com/openscad/openscad |
| 2506 | Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J. J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. In Volume 1: 39th Computers and Information in Engineering Conference (Article V001T02A006). ASME. https://doi.org/10.1115/DETC2019-97378 |
| 2508 | Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. JPO: Journal of Prosthetics and Orthotics, 22(2), 121-126. https://doi.org/10.1097/JPO.0b013e3181d427b7 |
| 2510 | Rezwana, J., & Maher, M. (2022). Understanding user perceptions, collaborative experience, and user engagement in different human-AI interaction designs for co-creative systems. https://arxiv.org/pdf/2204.13217 |
| 2545 | Steenbekkers, L. P. A., & van Beijsterveldt, C. E. M. (Eds.). (1998). Design-relevant characteristics of ageing users. Delft University Press. |

## 6. Anomalias formais nas citações Mendeley

| Itens citados no grupo | Texto apresentado | Anomalia |
| ---: | --- | --- |
| 1 | `(Alcará da Silva et al., sem data)` | ano apresentado como «sem data» |
| 2 | `(Fischer G et al., sem data; Francesca Costabile et al., 2007)` | ano apresentado como «sem data» |
| 3 | `(Fischer G et al., sem data; Howard et al., 2024; Von Hippel & Katz, 2002)` | ano apresentado como «sem data» |
| 3 | `(Fischer G et al., sem data; Kerr et al., 2024; Zhu & Zhong, 2022)` | ano apresentado como «sem data» |
| 1 | `ten Kate et al. (2017)` | início truncado |
| 1 | `(Baldock et al. (2023)` | parênteses desequilibrados |
| 1 | `(International Organization for Standardization, 2020` | parênteses desequilibrados |
| 3 | `(Lim et al., 2018; Nag et al., 2003; Rodríguez-Vega & Rodríguez-Vega,` | parênteses desequilibrados |
| 1 | `(Oldfrey et al., 2024 p. 575` | parênteses desequilibrados |
| 1 | `(Richardson & Dillon, (2017)` | parênteses desequilibrados |
| 1 | `Alluhydan et al. (2023` | parênteses desequilibrados |
| 2 | `Cameron Brooks, 2026; Nilsiam & Pearce, 2017)` | parênteses desequilibrados; abertura do grupo ausente |
| 2 | `chado et al., 2019; Nilsiam & Pearce, 2017)` | parênteses desequilibrados; início truncado; abertura do grupo ausente |
| 3 | `rdson & Dillon, 2017; Walters et al., 2025)` | parênteses desequilibrados; início truncado; abertura do grupo ausente |
| 1 | `Biddiss et al., (2007)` | vírgula indevida antes do ano |
| 1 | `Wendo et al., (2022)` | vírgula indevida antes do ano |

## 7. Critério de aprovação

A completude só poderá ser aprovada quando:

1. cada fonte viva tiver uma única entrada correspondente à obra efectivamente citada;
2. as atribuições de Zhou, Mendenhall, MakerBlock e Team UnLimbited estiverem formalizadas;
3. os anos das citações e das entradas estiverem uniformizados;
4. as entradas potencialmente órfãs forem citadas justificadamente ou removidas;
5. a bibliografia deixar de conter entradas mutiladas ou continuações autónomas;
6. a auditoria for repetida sobre o DOCX final e não devolver problemas impeditivos.

## 8. Método reproduzível

```bash
python3 tools/revisao/audit_docx_bibliographic_completeness.py
python3 tools/bibliografia/consolidate_docx_referenced_pdfs.py --apply
```

Itens Mendeley automaticamente associados a entradas: **141 de 150**; as nove excepções de identidade são mantidas fora desta contagem por decisão auditada.
