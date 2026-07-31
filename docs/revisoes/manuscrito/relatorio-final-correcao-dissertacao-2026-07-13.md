# Relatório final da correcção integral da dissertação

**Documento:** `projecto-completo.md`, versão 0.4.26
**Data:** 13 de Julho de 2026
**Versão de entrega prevista:** `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`

## 1. Síntese da intervenção

A correcção incidiu sobre o encadeamento entre problema, objectivos, perguntas, hipóteses, método, resultados e conclusões. O âmbito foi delimitado à avaliação técnica do protótipo: correspondência de perfis, conformidade das sugestões de IA com o esquema de parâmetros, geração geométrica, funcionamento dos módulos documentados, exportação, preparação para impressão e observação das peças físicas.

Foram retiradas formulações que podiam sugerir eficácia médica, adequação anatómica individual, conforto demonstrado, segurança, durabilidade, desempenho funcional ou prontidão para utilização real. Estas dimensões são agora apresentadas como matérias para estudos posteriores.

O capítulo metodológico passou a identificar ciclos concretos de Research Through Design, versões da plataforma, casos simulados, critérios de avaliação, tarefas determinísticas, tarefas atribuídas ao modelo de linguagem e decisões reservadas à supervisão humana. As conclusões respondem directamente às três perguntas reformuladas e distinguem contributos projectuais, técnicos, metodológicos e de conhecimento.

## 2. Correcções principais

- alinhamento entre problema, objectivo geral, objectivos específicos, perguntas e hipóteses;
- delimitação do protótipo como sistema experimental de investigação;
- explicitação dos ciclos de Research Through Design e do conhecimento produzido por cada correcção;
- descrição do algoritmo de correspondência de perfis antropométricos e dos seus critérios de pontuação;
- distinção entre parâmetros antropométricos, parâmetros geométricos, escolhas de apresentação e lateralidade;
- inclusão de um diagrama próprio da arquitectura da plataforma;
- identificação das fronteiras entre interface, servidor, Web Worker, OpenSCAD/WebAssembly, IA, visualização e exportação;
- descrição exacta dos modelos de linguagem, chamadas, limites e cenários avaliados;
- apresentação dos resultados de lateralidade antes e depois da correcção;
- identificação dos três projectos de preparação para impressão e das definições reutilizadas nas restantes peças;
- inclusão das fotografias dos protótipos e dos resultados de inspecção das malhas;
- moderação das conclusões sobre antropometria, IA, fabrico, função e utilização;
- correcção das discrepâncias ANSUR, DINED, unidades, contagens e caminhos dos ficheiros no anexo;
- ordenação alfabética das 161 entradas bibliográficas;
- remoção dos marcadores internos `(#ref-...)` do texto;
- uniformização da terminologia e da escrita em português europeu;
- actualização das listas de tabelas e figuras segundo a paginação calculada.

## 3. Verificações executadas

Na plataforma, a versão inspeccionada foi a 14.67.0 da branch `staging`, no commit `d5b6f0d5a41950663d54c70b9ab9bad7f8c2d53b`. Os dez ensaios unitários disponíveis terminaram sem falhas. A base `app.db` continha 100 perfis antropométricos, uma configuração guardada e quatro contas, sem inclusão de dados identificadores na dissertação.

Foram confirmados quatro modelos registados: Flexy Beast, UnLimbited Phoenix Hand, Paraglider Hand e Cyborg Beast. A comparação principal abrangeu os três primeiros. Foram também confirmados os três projectos de preparação para impressão, dois da Bambu Lab A1 e um da Prusa MINI. Segundo a informação fornecida pelo autor, as mesmas definições foram usadas nas restantes impressões.

A bateria Playwright não foi novamente executada, porque o executável local necessário não estava disponível. O arranque integral do servidor também ficou impedido pela ausência local da dependência `nodemailer`. Estas limitações estão declaradas na dissertação e não foram substituídas por pressupostos.

O documento final tem 146 páginas em formato A4, 23 tabelas, 24 figuras e 161 entradas bibliográficas. O pacote DOCX passou a verificação de integridade e contém 26 recursos gráficos, incluindo os elementos do modelo institucional. Foram confirmadas a paginação do índice e das listas, a apresentação da bibliografia, a legibilidade da Tabela 8.3 e a conservação dos sublinhados nos caminhos técnicos do Anexo A.

Os marcadores internos com a forma `(#ref-...)` foram retirados do texto e do DOCX final. As citações em autor-data e as entradas bibliográficas correspondentes foram conservadas; a referência de Burnap et al. (2019), por exemplo, permanece citada no corpo e registada na bibliografia.

## 4. Fontes sem ficheiro local confirmado

As referências seguintes constam da bibliografia, mas não foi localizado um PDF correspondente em `material/` ou `material/bibliografia/`:

1. Atallah et al. (2025), *The current state of 3D-printed prostheses clinical outcomes: A systematic review*.
2. Bustamante et al. (2018), *A parametric 3D-printed body-powered hand prosthesis based on the four-bar linkage mechanism*.
3. Cabibihan et al. (2021), *Suitability of the openly accessible 3D printed prosthetic hands for war-wounded children*.
4. Diment et al. (2018), *Three-dimensional printed upper-limb prostheses lack randomised controlled trials: A systematic review*.
5. ELhadad et al. (2026), *LLM-based 3D model generation of MHE for OpenSCAD*.
6. Ghali (2008), *Constructive solid geometry*.
7. Gonzalez Avila et al. (2024), *Understanding the challenges of OpenSCAD users for 3D printing*.
8. Gordon et al. (2015), *2012 anthropometric survey of U.S. Army personnel: Methods and summary statistics*.
9. Mistarihi (2020), *A data set on anthropometric measurements and degree of discomfort of physically disabled workers for ergonomic requirements in work space design*.
10. Molenbroek et al. (2003), *Revision of the Dutch standard for furniture in schools*.
11. Romani e Levi (2020), *Parametric design for online user customization of 3D printed assistive technology for rheumatic diseases*.
12. Schöfer e Seibel (2025), *Augmented design automation: Leveraging parametric designs using large language models*.
13. Steenbekkers e van Beijsterveldt (1998), *Design-relevant characteristics of ageing users*.
14. Trautmann (2021), *Product customization and generative design*.
15. Zuniga et al. (2015), *Cyborg beast: A low-cost 3D-printed prosthetic hand for children with upper-limb differences*.

Os elementos seguintes são recursos digitais ou software, pelo que pode não existir um PDF editorial. Mantêm-se identificados para confirmação documental:

1. Brooks (2026), *OpenSCAD Web*.
2. Molenbroek (1998), entrada DINED relativa ao estudo Geron.
3. OpenSCAD Community (s.d.), manual de utilização em linha de comando.
4. OpenSCAD Project (s.d.-a), sítio oficial do OpenSCAD.
5. OpenSCAD Project (s.d.-b), repositório oficial do código do OpenSCAD.

O PDF de Wendo et al. (2022) foi localizado em `material/bibliografia/` e retirado da lista de faltas.

## 5. Elementos adicionais que reforçariam a dissertação

Os elementos seguintes aumentariam a sustentação metodológica e técnica do trabalho. A sua inclusão deve depender da existência de dados verificáveis. Quando um ensaio ainda não tiver sido realizado, o texto deve apresentá-lo como trabalho futuro.

### 5.1 Prioridade elevada

| Elemento a acrescentar | Local recomendado | Conteúdo concreto | Base necessária |
| --- | --- | --- | --- |
| Caso numérico completo, desde o perfil até à geometria | Capítulo 4, após a explicação do algoritmo de correspondência | Apresentar um perfil de ensaio, a fonte antropométrica seleccionada, os valores de entrada, as conversões, os parâmetros derivados, os limites aplicados, as variáveis OpenSCAD afectadas e as dimensões finais da malha. | Dados e cálculos guardados para um dos cenários já avaliados. |
| Quadro integral das execuções de IA | Capítulo 6 para o protocolo; Capítulo 8 ou apêndice para os resultados | Registar, por execução, data, fornecedor, identificador do modelo, definições de geração, entrada, saída JSON, correcções efectuadas pelo servidor, avisos, falhas e decisão final do autor. Acrescentar medidas de dispersão entre respostas quando existirem várias execuções do mesmo cenário. | Registos originais das chamadas ou nova recolha controlada. |
| Matriz de ensaios funcionais da plataforma | Capítulo 3 para o método; Capítulo 8 para os resultados | Relacionar autenticação, criação de perfil, selecção do modelo, sugestão por IA, alteração manual, geração, visualização, exportação e recuperação de erro com pré-condição, passos, resultado esperado, resultado observado, versão e ambiente. | Execução documentada dos casos. Os dez ensaios unitários podem constituir uma parte desta matriz. |
| Verificação dimensional da passagem digital-física | Capítulo 8 | Comparar, para peças identificadas, a dimensão pedida, a dimensão da malha exportada e a dimensão medida na peça com paquímetro. Indicar pontos de medição, resolução do instrumento, erro absoluto e erro percentual. | Novas medições das peças existentes ou produção de exemplares identificados. |
| Registo completo das impressões | Capítulo 3 para o protocolo; Capítulo 8 ou apêndice para os resultados | Atribuir um código a cada peça e indicar modelo, perfil de ensaio, impressora, programa de preparação para impressão 3D, material, configuração usada, camada, paredes, enchimento, orientação, suportes, temperatura, tempo, massa, falhas e observações de montagem. Explicar que os quatro projectos de preparação digital com configuração analisada documentam as definições dos respectivos casos. | Projectos 3MF, fotografias, histórico das impressoras e notas do processo. Campos sem registo devem ser assinalados como indisponíveis. |
| Cronologia das iterações de Research Through Design | Final do Capítulo 3 ou início do Capítulo 9 | Organizar as iterações por data ou versão, indicando questão de design, artefacto alterado, observação, decisão e conhecimento produzido. Incluir os casos de lateralidade, escala do Paraglider, limite mínimo do Phoenix e inspecção das malhas. | Histórico do código, notas e resultados já existentes. |
| Discussão comparativa com o estado da arte | Capítulo 9 | Comparar o protótipo com plataformas e estudos citados segundo integração antropométrica, configuração paramétrica, execução no navegador, papel da IA, exportação, fabrico e tipo de avaliação. Explicitar em que aspectos o trabalho confirma, diverge ou acrescenta conhecimento à literatura. | Fontes já citadas, após confirmação do conteúdo dos artigos originais. |

### 5.2 Prioridade intermédia

| Elemento a acrescentar | Local recomendado | Conteúdo concreto | Base necessária |
| --- | --- | --- | --- |
| Quadro de correspondência entre requisitos e evidência | Final dos Capítulos 3 e 8 | Para cada objectivo e requisito, indicar actividade, critério, resultado, secção de discussão e conclusão. Marcar como não avaliada qualquer dimensão sem ensaio próprio. | Conteúdo actual da dissertação. |
| Dicionário técnico de parâmetros | Capítulo 4 ou apêndice | Para cada variável, indicar nome no código, significado, unidade, origem, valor inicial, intervalo, fórmula, componente afectado e modelo em que é usada. Separar medidas antropométricas, parâmetros derivados e opções visuais. | Código da versão identificada na dissertação. |
| Caracterização mais explícita da base antropométrica | Capítulo 4 e Anexo A | Apresentar uma tabela por fonte com população, sexo, idade, mão medida, protocolo, dimensão amostral, medidas disponíveis e limitações de comparação. Explicar a prioridade dada às fontes e o tratamento de países ausentes. | CSV, artigos originais e regras implementadas. |
| Quadro de contributos | Capítulo 9 | Distinguir contributo projectual, técnico, metodológico e de conhecimento; associar cada contributo à evidência que o suporta e ao seu limite. | Resultados actuais, sem ampliar o âmbito. |
| Glossário operacional curto | Capítulo 1 ou 3 | Fixar o uso de personalização, configuração, parametrização, modelo paramétrico, plataforma, protótipo, verificação técnica, avaliação e validação clínica. | Decisões terminológicas já adoptadas no texto. |
| Confirmação bibliográfica dirigida | Referências e passagens teóricas correspondentes | Confirmar autores, ano, título, DOI ou URL e relação directa entre a fonte e a afirmação. Substituir ligações de agregadores por DOI ou página editorial quando a fonte original estiver disponível. | Consulta dos artigos e recursos originais. |

### 5.3 Conteúdos que exigem novos estudos

Avaliações de conforto, segurança, desempenho em tarefas, uso prolongado, adequação anatómica individual ou eficácia médica exigem participantes, procedimentos próprios, critérios éticos e, consoante o caso, colaboração clínica. Estes conteúdos não devem ser acrescentados como resultados com base nas simulações ou nas peças actuais.

Uma comparação entre PLA e PETG exigiria espécimes equivalentes, parâmetros controlados e ensaios definidos para a propriedade em causa. A existência de materiais configurados no programa ou de peças produzidas com condições distintas não sustenta conclusões comparativas.

Antes da entrega, os reforços com melhor relação entre esforço e valor académico são a cronologia de Research Through Design, o caso numérico completo, o quadro de correspondência entre objectivos e evidência e a discussão comparativa com a literatura. Estes quatro elementos podem ser construídos sobretudo a partir de material já existente.

## 6. Estado final

O manuscrito encontra-se preparado para leitura final do autor e do orientador. A evidência apresentada sustenta um protótipo técnico de investigação e um processo de desenvolvimento projectual documentado. A entrega deve conservar a delimitação actual e evitar recuperar formulações anteriores sobre eficácia, conforto, segurança ou adequação clínica.
