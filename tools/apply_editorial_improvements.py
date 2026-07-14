#!/usr/bin/env python3
"""Apply the 2026-07-13 editorial pass to the thesis Markdown and DOCX.

The script keeps the two manuscript representations synchronized, preserves the
DOCX package and formatting, splits only explicitly identified paragraphs, and
normalizes figure provenance without rewriting bibliographic reference titles.
"""

from __future__ import annotations

import argparse
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W}


def qn(ns: str, name: str) -> str:
    return f"{{{ns}}}{name}"


PARAGRAPH_SPLITS = {
    (
        "A partir desta leitura, os requisitos de projecto podem ser organizados em categorias interdependentes. "
        "Os requisitos funcionais incluem padrões de preensão, graus de liberdade, amplitude de movimento, força, "
        "velocidade e capacidade de realizar atividades da vida diária. Os requisitos ergonómicos assumem particular "
        "centralidade, destacando-se o conforto, o baixo peso, a usabilidade, a facilidade de colocação e remoção da "
        "prótese e a adequação ao uso quotidiano prolongado. Ao nível técnico, definem-se parâmetros relativos a "
        "atuadores, sistemas de transmissão, sensores, estratégias de controlo, fontes de energia e selecção de "
        "materiais com propriedades mecânicas adequadas e compatibilidade biológica. Em termos de fabrico, emergem "
        "exigências de modularidade, reparabilidade, custo controlado e compatibilidade com fluxos de fabrico digital e "
        "aditivo. Acrescem ainda requisitos estéticos e psicossociais, relacionados com a identidade, a aceitação social "
        "e a incorporação corporal, cuja relevância é reiterada tanto por utilizadores como por clínicos e familiares "
        "(Biddiss et al., 2007; Brack & Amalu, 2021; Henao et al., 2025; Walker et al., 2019)."
    ): [
        "A partir desta leitura, os requisitos de projecto podem ser organizados em categorias interdependentes. Os requisitos funcionais incluem padrões de preensão, graus de liberdade, amplitude de movimento, força, velocidade e capacidade de realizar actividades da vida diária.",
        "Os requisitos ergonómicos assumem particular centralidade, destacando-se o conforto, o baixo peso, a usabilidade, a facilidade de colocação e remoção da prótese e a adequação ao uso quotidiano prolongado. Ao nível técnico, definem-se parâmetros relativos a actuadores, sistemas de transmissão, sensores, estratégias de controlo, fontes de energia e selecção de materiais com propriedades mecânicas adequadas e compatibilidade biológica.",
        "Em termos de fabrico, emergem exigências de modularidade, reparabilidade, custo controlado e compatibilidade com fluxos de fabrico digital e aditivo. Acrescem ainda requisitos estéticos e psicossociais, relacionados com a identidade, a aceitação social e a incorporação corporal, cuja relevância é reiterada tanto por utilizadores como por clínicos e familiares (Biddiss et al., 2007; Brack & Amalu, 2021; Henao et al., 2025; Walker et al., 2019).",
    ],
    (
        "O desenvolvimento do modelo paramétrico não ocorreu, desde o início, como uma sequência linear orientada para "
        "uma solução estável e definitiva. Pelo contrário, evoluiu através de ciclos sucessivos de formulação, teste, "
        "correcção e reconfiguração, em coerência com a perspectiva de Research Through Design, segundo a qual o próprio "
        "processo projectual constitui um meio de produção de conhecimento (Zimmerman, Forlizzi, & Evenson, 2007). Neste "
        "enquadramento, cada versão do modelo funcionou simultaneamente como protótipo operativo e como dispositivo "
        "crítico, permitindo tornar visíveis as limitações, reformular os critérios e aprofundar a compreensão das "
        "relações entre dados antropométricos, organização geométrica, requisitos funcionais e constrangimentos de fabrico."
    ): [
        "O desenvolvimento do modelo paramétrico não ocorreu, desde o início, como uma sequência linear orientada para uma solução estável e definitiva. Pelo contrário, evoluiu através de ciclos sucessivos de formulação, teste, correcção e reconfiguração, em coerência com a perspectiva de Research Through Design, segundo a qual o próprio processo projectual constitui um meio de produção de conhecimento (Zimmerman, Forlizzi, & Evenson, 2007).",
        "Neste enquadramento, cada versão do modelo funcionou simultaneamente como protótipo operativo e como dispositivo crítico, permitindo tornar visíveis as limitações, reformular os critérios e aprofundar a compreensão das relações entre dados antropométricos, organização geométrica, requisitos funcionais e constrangimentos de fabrico.",
    ],
    (
        "A necessidade de iteração tornou-se particularmente evidente porque a modelação paramétrica, apesar da sua "
        "aparência sistemática, depende de um equilíbrio delicado entre abstração e concretização. Numa fase inicial, a "
        "estrutura do sistema assentou na definição de um conjunto de parâmetros julgados essenciais e numa primeira "
        "hierarquia entre variáveis de entrada, valores derivados e restrições. No entanto, à medida que o modelo foi "
        "sendo testado em diferentes cenários, verificou-se que a mera disponibilidade de muitos parâmetros não aumentava, "
        "por si só, a capacidade de personalização. Pelo contrário, a exposição excessiva de variáveis tendia a tornar o "
        "sistema mais opaco, menos previsível e mais vulnerável a incoerências geométricas, confirmando a importância de "
        "limitar e estruturar cuidadosamente o espaço configurável (Ozdemir, Verlinden, & Cascini, 2022; Lei, Yao, Moon, & Bi, 2016)."
    ): [
        "A necessidade de iteração tornou-se particularmente evidente porque a modelação paramétrica, apesar da sua aparência sistemática, depende de um equilíbrio delicado entre abstracção e concretização. Numa fase inicial, a estrutura do sistema assentou na definição de um conjunto de parâmetros julgados essenciais e numa primeira hierarquia entre variáveis de entrada, valores derivados e restrições.",
        "À medida que o modelo foi testado em diferentes cenários, verificou-se que a mera disponibilidade de muitos parâmetros não aumentava, por si só, a capacidade de personalização. Pelo contrário, a exposição excessiva de variáveis tendia a tornar o sistema mais opaco, menos previsível e mais vulnerável a incoerências geométricas, confirmando a importância de limitar e estruturar cuidadosamente o espaço configurável (Ozdemir, Verlinden, & Cascini, 2022; Lei, Yao, Moon, & Bi, 2016).",
    ],
    (
        "À medida que a estrutura geral se consolidou, o trabalho iterativo deslocou-se para a decomposição do sistema em "
        "módulos relativamente autónomos. Esta organização modular permitiu isolar problemas, testar componentes de "
        "forma localizada e introduzir alterações sem comprometer integralmente o comportamento global do modelo. No "
        "contexto do presente projecto, esta estratégia revelou-se especialmente útil na articulação entre elementos "
        "estruturais, zonas de contacto, interfaces mecânicas e componentes de ligação. Para além de organizar o código, a "
        "divisão do modelo em módulos contribuiu para clarificar progressivamente a lógica do objecto, aproximando-o de "
        "uma estrutura configurável, mais sistemática e compatível com futuros contextos de interface ou de configuração "
        "apoiada (Nilsiam & Pearce, 2017)."
    ): [
        "À medida que a estrutura geral se consolidou, o trabalho iterativo deslocou-se para a decomposição do sistema em módulos relativamente autónomos. Esta organização modular permitiu isolar problemas, testar componentes de forma localizada e introduzir alterações sem comprometer integralmente o comportamento global do modelo.",
        "No contexto do presente projecto, esta estratégia revelou-se especialmente útil na articulação entre elementos estruturais, zonas de contacto, interfaces mecânicas e componentes de ligação. Para além de organizar o código, a divisão do modelo em módulos contribuiu para clarificar progressivamente a lógica do objecto, aproximando-o de uma estrutura configurável, mais sistemática e compatível com futuros contextos de interface ou de configuração apoiada (Nilsiam & Pearce, 2017).",
    ],
    (
        "As iterações também mostraram que a robustez de um modelo paramétrico só se torna legível quando confrontado com "
        "situações-limite. Um sistema pode parecer estável dentro de uma faixa reduzida de variação e, ainda assim, revelar "
        "fragilidades relevantes quando submetido a combinações menos previsíveis de parâmetros. Foi precisamente nesse "
        "tipo de ensaio que surgiram problemas como interseções indevidas entre componentes, espessuras insuficientes em "
        "zonas críticas, desalinhamentos de interfaces, incompatibilidades entre dimensões derivadas e perdas localizadas "
        "de coerência proporcional. O refinamento consistiu, assim, menos na correcção pontual de erros isolados e mais na "
        "identificação de padrões recorrentes de instabilidade, o que levou à introdução progressiva de verificações "
        "condicionais, limites paramétricos e ajustes automáticos."
    ): [
        "As iterações também mostraram que a robustez de um modelo paramétrico só se torna legível quando confrontado com situações-limite. Um sistema pode parecer estável dentro de uma faixa reduzida de variação e, ainda assim, revelar fragilidades relevantes quando submetido a combinações menos previsíveis de parâmetros.",
        "Nesse tipo de ensaio surgiram problemas como intersecções indevidas entre componentes, espessuras insuficientes em zonas críticas, desalinhamentos de interfaces, incompatibilidades entre dimensões derivadas e perdas localizadas de coerência proporcional. O refinamento incidiu, assim, na identificação de padrões recorrentes de instabilidade e conduziu à introdução progressiva de verificações condicionais, limites paramétricos e ajustes automáticos.",
    ],
    (
        "Outro eixo central do processo prendeu-se à relação entre personalização e fabrico. Nem todas as variações "
        "formalmente admissíveis se revelaram compatíveis com as exigências do fabrico. Algumas configurações geravam "
        "geometrias excessivamente finas, folgas insuficientes ou desproporcionadas, transições abruptas e zonas "
        "potencialmente frágeis no contexto da impressão 3D. Neste sentido, a evolução do modelo confirmou a relevância de "
        "integrar critérios de Design for Additive Manufacturing à própria lógica paramétrica, em vez de tratá-los como "
        "uma verificação externa e posterior. A literatura sobre DfAM aponta precisamente para a necessidade de incorporar "
        "tolerâncias, espessuras mínimas, orientações de fabrico e limites materiais desde a fase de concepção, reduzindo "
        "falhas e encurtando os ciclos de reimpressão e de correcção (Chtioui, Gaha, & Benamara, 2023; Wiberg et al., 2019)."
    ): [
        "Outro eixo central do processo prendeu-se à relação entre personalização e fabrico. Nem todas as variações formalmente admissíveis se revelaram compatíveis com as exigências do fabrico. Algumas configurações geravam geometrias excessivamente finas, folgas insuficientes ou desproporcionadas, transições abruptas e zonas potencialmente frágeis no contexto da impressão 3D.",
        "A evolução do modelo reforçou, nos casos examinados, a relevância de integrar critérios de Design for Additive Manufacturing na própria lógica paramétrica, em vez de os tratar como uma verificação externa e posterior. A literatura sobre DfAM aponta igualmente para a incorporação de tolerâncias, espessuras mínimas, orientações de fabrico e limites materiais desde a fase de concepção, reduzindo falhas e encurtando os ciclos de reimpressão e de correcção (Chtioui, Gaha, & Benamara, 2023; Wiberg et al., 2019).",
    ],
    (
        "A discussão intermédia decorrente destas iterações permite tirar algumas conclusões provisórias. Em primeiro "
        "lugar, confirma-se que a modelação paramétrica baseada em código constitui um enquadramento adequado para "
        "estruturar sistemas configuráveis, desde que a arquitetura seja disciplinada e os parâmetros expostos sejam "
        "criteriosamente seleccionados. Em segundo lugar, verifica-se que a robustez do sistema depende menos da "
        "quantidade de variáveis disponíveis do que da qualidade das relações estabelecidas entre elas. Em terceiro lugar, "
        "torna-se claro que a personalização eficaz exige integração simultânea de critérios antropométricos, funcionais e "
        "produtivos, não podendo ser reduzida a mera transformação geométrica. Por fim, a iteração evidencia-se como "
        "mecanismo indispensável de convergência: não encerra definitivamente o sistema, mas estabiliza uma versão "
        "suficientemente consistente para sustentar as fases seguintes de plataforma, integração digital e exploração apoiada."
    ): [
        "As iterações documentadas sustentam quatro observações circunscritas aos modelos avaliados. Primeiro, a modelação paramétrica baseada em código permitiu estruturar os sistemas configuráveis testados quando a arquitectura e as dependências entre parâmetros foram explicitadas. Segundo, as falhas observadas indicaram que a estabilidade paramétrica dependeu da qualidade das relações codificadas, e não apenas da quantidade de variáveis disponíveis.",
        "Terceiro, a personalização examinada exigiu a articulação de critérios antropométricos, funcionais e produtivos, não se reduzindo a uma transformação geométrica. Por fim, a iteração funcionou como mecanismo de convergência: não encerrou definitivamente o sistema, mas estabilizou uma versão adequada às fases subsequentes de integração na plataforma e de avaliação técnica.",
    ],
    (
        "Neste enquadramento, a IA assume a função de camada complementar de apoio à configuração, operando sobre uma "
        "base paramétrica já definida e articulando-se com a lógica geométrica do modelo, a decisão de projecto e a "
        "verificação técnica. A literatura sobre modelação paramétrica aplicada a próteses personalizadas e sobre fabrico "
        "aditivo mostra que existe fundamento técnico para construir geometrias configuráveis com base em regras "
        "explícitas, parâmetros dimensionais e relações geométricas controladas. Estudos sobre próteses paramétricas para "
        "diferentes níveis de amputação de membros superiores, sobre a personalização de dedos protésicos por modelação "
        "paramétrica e sobre encaixes protésicos personalizados para próteses transradiais mostram que a personalização "
        "pode ser estruturada através de modelos explícitos e fluxos CAD/CAM ajustáveis (da Silveira Romero et al., 2025; "
        "Lim et al., 2018; Saldarriaga et al., 2024). O sistema aqui proposto parte desta premissa: a geometria é produzida "
        "por um modelo paramétrico explícito, definido em OpenSCAD e manipulável através de parâmetros cuja origem e "
        "efeito podem ser identificados."
    ): [
        "Neste enquadramento, a IA assume a função de camada complementar de apoio à configuração, operando sobre uma base paramétrica já definida e articulando-se com a lógica geométrica do modelo, a decisão de projecto e a verificação técnica. Os trabalhos de da Silveira Romero et al. (2025), Lim et al. (2018) e Saldarriaga et al. (2024) fornecem fundamento técnico para construir geometrias configuráveis com regras explícitas, parâmetros dimensionais e relações geométricas controladas.",
        "Em conjunto, esses estudos mostram que a personalização pode ser estruturada através de modelos explícitos e fluxos CAD/CAM ajustáveis. O sistema aqui proposto parte desta premissa: a geometria é produzida por um modelo paramétrico definido em OpenSCAD e manipulável através de parâmetros cuja origem e efeito podem ser identificados.",
    ],
    (
        "Esta leitura é coerente com a arquitectura da plataforma descrita no capítulo anterior. O sistema separa a camada "
        "de interface, a lógica paramétrica, a renderização local em WebAssembly e a comunicação controlada com serviços "
        "externos de IA. Tal organização preserva uma ligação verificável entre a entrada inicial, a sugestão produzida "
        "pela IA e o resultado geométrico gerado pelo modelo. O sistema mantém a IA sob supervisão: sugere valores sem "
        "determinar a configuração, apoia a exploração sem validar o resultado e acelera tarefas sem substituir o "
        "julgamento técnico. Esta opção é importante, considerando que a supervisão clínica ou técnica permanece limitada "
        "em vários estudos que articulam modelação digital, CAD, IA, co-design apoiado ou impressão 3D (Romero et al., "
        "2025; Elbreki et al., 2022; Idris et al., 2024). O valor da IA reside no apoio a um processo já estruturado por "
        "lógica paramétrica explícita, requisitos de fabrico e responsabilidade humana."
    ): [
        "Esta leitura é coerente com a arquitectura da plataforma descrita no capítulo anterior. O sistema separa a camada de interface, a lógica paramétrica, a renderização local em WebAssembly e a comunicação controlada com serviços externos de IA. Tal organização preserva uma ligação verificável entre a entrada inicial, a sugestão produzida pela IA e o resultado geométrico gerado pelo modelo.",
        "O sistema mantém a IA sob supervisão: sugere valores sem determinar a configuração, apoia a exploração sem validar o resultado e acelera tarefas sem substituir o julgamento técnico. Esta opção responde à supervisão clínica ou técnica limitada nos estudos que articulam modelação digital, CAD, IA, co-design apoiado ou impressão 3D (Romero et al., 2025; Elbreki et al., 2022; Idris et al., 2024). O valor da IA reside no apoio a um processo já estruturado por lógica paramétrica explícita, requisitos de fabrico e responsabilidade humana.",
    ],
    (
        "Uma interface bem desenhada pode criar uma sensação de evidência ou neutralidade em decisões condicionadas por "
        "critérios de projecto, pressupostos técnicos e escolhas interpretativas. A apresentação de um parâmetro como "
        "controlo disponível, ou de uma sugestão com aparência de coerência técnica, não significa que a solução esteja "
        "validada ou represente a melhor opção em todos os contextos. A mediação da interface deve ser avaliada pela "
        "eficiência e pela forma como torna visíveis dependências, incertezas e responsabilidades. A literatura analisada "
        "reforça esta cautela: resultados positivos de usabilidade ou rapidez de afinação mantêm a necessidade de definir "
        "quem decide, quais parâmetros podem ser alterados, quais decisões ficam pré-estruturadas pelo sistema e em que "
        "condições essas alterações são seguras ou adequadas (Peixoto et al., 2025; Quintero et al., 2018; Bai et al., 2024)."
    ): [
        "Uma interface bem desenhada pode criar uma sensação de evidência ou neutralidade em decisões condicionadas por critérios de projecto, pressupostos técnicos e escolhas interpretativas. A apresentação de um parâmetro como controlo disponível, ou de uma sugestão com aparência de coerência técnica, não significa que a solução esteja validada ou represente a melhor opção em todos os contextos.",
        "A mediação da interface deve ser avaliada pela eficiência e pela forma como torna visíveis dependências, incertezas e responsabilidades. Peixoto et al. (2025), Quintero et al. (2018) e Bai et al. (2024) reforçam esta cautela: resultados positivos de usabilidade ou rapidez de afinação mantêm a necessidade de definir quem decide, quais parâmetros podem ser alterados, quais decisões ficam pré-estruturadas pelo sistema e em que condições essas alterações são seguras ou adequadas.",
    ],
}


EXACT_REPLACEMENTS = {
    "Versão do documento: 0.4.26": "Versão do documento: 0.4.27",
    "após o treinamento": "após o treino",
    "integraçãoe a integração": "integração",
    "tratam a fabrico": "tratam o fabrico",
    "para definir corretamente o âmbito da ferramenta": "para definir correctamente o âmbito da ferramenta.",
    "“seed designs” ou modelos-base parametrizados": "modelos-base parametrizados",
    "uma prática de human-in-the-loop": "uma prática de supervisão humana contínua",
    "abordagens human-in-the-loop": "abordagens de supervisão humana contínua",
    "com recurso ao framework Express.js": "com recurso à infra-estrutura Express.js",
    "“frente” (frontend) e “retaguarda” (backend)": "cliente e servidor",
    "carga computacional do backend": "carga computacional do servidor",
    "associados ao backend": "associados ao servidor",
    "backend do protótipo": "servidor do protótipo",
    "thread principal do navegador": "linha principal de execução do navegador",
    "Fonte adaptada. Referência original: ": "Adaptado de ",
    "Akasaka, M., Veeckman, C., Georges, A., Schuurman, D., & Coorevits, L. (2022). A framework for configuring participation in living labs.": "Akasaka, F., Mitake, Y., Watanabe, K., & Shimomura, Y. (2022). A framework for ‘configuring participation’ in living labs. Design Science, 8, e28.",
    "https://www.semanticscholar.org/paper/305d55af5fda06b4d1b33e7d29c1f16d1b7ea488": "https://doi.org/10.1017/dsj.2022.22",
    "A literatura evidencia que as abordagens inclusivas e centradas no utilizador recorrem": "Fisher e Johansen (2020) e Shah e Robinson (2006) descrevem que as abordagens inclusivas e centradas no utilizador recorrem",
    "Estudos aplicados demonstram que, ao determinar experimentalmente constrangimentos do processo e incorporá-los ao modelo paramétrico, é possível gerar milhares de variantes únicas com elevada taxa de sucesso funcional, minimizando as reimpressões (Wiberg et al., 2019).": "Wiberg et al. (2019) demonstram, no sistema que avaliaram, que a determinação experimental dos constrangimentos do processo e a sua incorporação no modelo paramétrico permitiram gerar milhares de variantes com elevada taxa de sucesso funcional e reduzir reimpressões.",
    "Embora os princípios sejam transversais, a literatura evidencia diferenças por tipo de dispositivo:": "Embora os princípios sejam transversais, os estudos analisados distinguem requisitos e métodos segundo o tipo de dispositivo:",
    "A literatura evidencia uma articulação insuficiente entre as necessidades expressas pelos utilizadores": "Cordella et al. (2016) e Manz et al. (2022) identificam uma articulação insuficiente entre as necessidades expressas pelos utilizadores",
    "Em termos práticos, a literatura mostra que não há um método universalmente superior;": "Em termos práticos, Çıklaçandır et al. (2022) e Herbst et al. (2021) mostram que não há um método universalmente superior;",
    "FDM/FFF (extrusão de termoplásticos)": "modelação por deposição fundida (FDM) e fabrico por filamento fundido (FFF), ambos baseados na extrusão de termoplásticos",
    "o processamento de pedidos à API": "o processamento de pedidos à interface de programação de aplicações (Application Programming Interface — API)",
    "«geometria exportada» designa a malha STL ou 3MF": "«geometria exportada» designa o ficheiro resultante nos formatos Stereolithography (STL) ou 3D Manufacturing Format (3MF)",
    "exporta ficheiros STL e 3MF": "exporta ficheiros nos formatos Stereolithography (STL) e 3D Manufacturing Format (3MF)",
    "### 2.2 Design Industrial, Design Inclusivo e Design Centrado no Utilizador": "### 2.2 Design industrial, design inclusivo e design centrado no utilizador",
    "### Design Inclusivo e Design Universal": "### Design inclusivo e design universal",
    "### Design Centrado no Utilizador e Design Centrado no Humano": "### Design centrado no utilizador e design centrado no humano",
}


WORD_REPLACEMENTS = {
    "Design Industrial": "design industrial",
    "Design Inclusivo": "design inclusivo",
    "Design Universal": "design universal",
    "Design Centrado no Utilizador": "design centrado no utilizador",
    "Design Centrado no Humano": "design centrado no humano",
    "arquitetura": "arquitectura",
    "Arquitetura": "Arquitectura",
    "projetado": "projectado",
    "projetados": "projectados",
    "treinamento": "treino",
    "adoção": "adopção",
    "diretamente": "directamente",
    "direto": "directo",
    "direta": "directa",
    "atual": "actual",
    "atuais": "actuais",
    "atualmente": "actualmente",
    "atualização": "actualização",
    "atualizada": "actualizada",
    "atualizado": "actualizado",
    "ação": "acção",
    "ações": "acções",
    "atividade": "actividade",
    "atividades": "actividades",
    "ativa": "activa",
    "ativas": "activas",
    "ativo": "activo",
    "ativos": "activos",
    "atuadores": "actuadores",
    "ato": "acto",
    "efetivo": "efectivo",
    "efetiva": "efectiva",
    "efetivos": "efectivos",
    "efetivas": "efectivas",
    "efetivamente": "efectivamente",
    "exato": "exacto",
    "exata": "exacta",
    "exatos": "exactos",
    "exatas": "exactas",
    "exatamente": "exactamente",
    "exceção": "excepção",
    "exceções": "excepções",
    "interseção": "intersecção",
    "interseções": "intersecções",
    "otimização": "optimização",
    "Otimização": "Optimização",
    "otimizado": "optimizado",
    "otimizada": "optimizada",
    "reflete": "reflecte",
    "refletem": "reflectem",
    "respetivo": "respectivo",
    "respetiva": "respectiva",
    "respetivos": "respectivos",
    "respetivas": "respectivas",
    "seleção": "selecção",
    "seletiva": "selectiva",
    "seletivo": "selectivo",
    "selecionado": "seleccionado",
    "selecionada": "seleccionada",
    "selecionados": "seleccionados",
    "selecionadas": "seleccionadas",
    "subjetivo": "subjectivo",
    "subjetiva": "subjectiva",
    "subjetivos": "subjectivos",
    "subjetivas": "subjectivas",
    "tátil": "táctil",
    "vetor": "vector",
}


ADAPTED_FIGURES = {"2.3", "2.6", "2.7", "2.8", "3.1", "4.1", "4.2", "5.3", "6.1"}
OWN_FIGURES = {"5.1", "5.2", "8.1", "8.2", "8.3"}
REPRODUCED_FIGURES = {"1.1", "2.1", "2.2", "2.4", "2.5", "3.2", "4.3", "5.4", "7.1", "8.4"}
FIGURE_LICENSES = {"2.7": "CC BY 4.0", "5.3": "CC BY 3.0"}
LICENSED_SOURCE_PREFIXES = {
    "Adaptado de Akasaka, F., Mitake, Y., Watanabe, K., & Shimomura, Y. (2022).": "CC BY 4.0",
}


def apply_exact(text: str) -> str:
    for old, new in EXACT_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def apply_words(text: str) -> str:
    text = apply_exact(text)
    for old, new in sorted(WORD_REPLACEMENTS.items(), key=lambda item: -len(item[0])):
        text = re.sub(rf"(?<!\w){re.escape(old)}(?!\w)", new, text)
    return text


def figure_number(text: str) -> str | None:
    match = re.match(r"Figura\s+(\d+\.\d+)\b", text)
    return match.group(1) if match else None


def provenance_prefix(number: str) -> str:
    if number in ADAPTED_FIGURES:
        return "Adaptado de "
    if number in OWN_FIGURES:
        return "Fonte: produção própria."
    if number in REPRODUCED_FIGURES:
        return "Reproduzido de "
    raise ValueError(f"Figure {number} is not classified")


def replace_provenance_text(text: str, number: str) -> str:
    target = provenance_prefix(number)
    replacement = text
    if number in OWN_FIGURES:
        if text in {"Produção própria", "Produção própria.", "Fonte: produção própria", "Fonte: produção própria."}:
            return target
        return text
    for prefix in ("Fonte original: ", "Adaptado de fonte original: ", "Adaptado de ", "Adaptação de ", "Reproduzido de "):
        if text.startswith(prefix):
            replacement = target + text[len(prefix) :]
            break
    license_name = FIGURE_LICENSES.get(number)
    if license_name and f"Licença: {license_name}." not in replacement:
        replacement = replacement.rstrip() + f" Licença: {license_name}."
    return replacement


def process_markdown(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for old, parts in PARAGRAPH_SPLITS.items():
        count = text.count(old)
        if count != 1:
            raise ValueError(f"Markdown paragraph expected once, found {count}: {old[:80]}")
        text = text.replace(old, "\n\n".join(parts))

    lines = text.splitlines()
    in_references = False
    current_figure: str | None = None
    output: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == "## Referências Bibliográficas":
            in_references = True
        elif stripped.startswith("# Anexo A"):
            in_references = False

        number = figure_number(stripped)
        if number:
            current_figure = number
        elif current_figure and (
            stripped.startswith("Fonte original:")
            or stripped.startswith("Adaptado de")
            or stripped.startswith("Adaptação de")
            or stripped.startswith("Reproduzido de")
            or stripped.startswith("Produção própria")
            or stripped.startswith("Fonte: produção própria")
        ):
            line = replace_provenance_text(line, current_figure)
            current_figure = None

        if not in_references and not stripped.startswith(("Fonte original:", "Adaptado de", "Adaptação de", "Reproduzido de")):
            line = apply_words(line)
        else:
            line = apply_exact(line)
        for prefix, license_name in LICENSED_SOURCE_PREFIXES.items():
            if line.startswith(prefix) and f"Licença: {license_name}." not in line:
                line = line.rstrip() + f" Licença: {license_name}."
        output.append(line)
    path.write_text("\n".join(output) + "\n", encoding="utf-8")


def paragraph_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def replace_full_text(p: etree._Element, text: str) -> None:
    ts = p.xpath(".//w:t", namespaces=NS)
    if not ts:
        r = etree.SubElement(p, qn(W, "r"))
        t = etree.SubElement(r, qn(W, "t"))
        t.text = text
        return
    ts[0].text = text
    if text.startswith(" ") or text.endswith(" "):
        ts[0].set(qn(XML, "space"), "preserve")
    for t in ts[1:]:
        t.text = ""


def clone_plain_paragraph(source: etree._Element, text: str) -> etree._Element:
    p = etree.Element(qn(W, "p"), nsmap=source.nsmap)
    p_pr = source.find("w:pPr", NS)
    if p_pr is not None:
        p.append(deepcopy(p_pr))
    r = etree.SubElement(p, qn(W, "r"))
    first_rpr = source.find(".//w:r/w:rPr", NS)
    if first_rpr is not None:
        r.append(deepcopy(first_rpr))
    t = etree.SubElement(r, qn(W, "t"))
    t.text = text
    return p


def process_document_xml(data: bytes) -> bytes:
    root = etree.fromstring(data)
    body = root.find("w:body", NS)
    if body is None:
        raise ValueError("DOCX body not found")

    split_counts = {key: 0 for key in PARAGRAPH_SPLITS}
    for p in list(body.xpath(".//w:p", namespaces=NS)):
        text = paragraph_text(p)
        if text in PARAGRAPH_SPLITS:
            split_counts[text] += 1
            parts = PARAGRAPH_SPLITS[text]
            replace_full_text(p, parts[0])
            parent = p.getparent()
            index = parent.index(p)
            for offset, part in enumerate(parts[1:], 1):
                parent.insert(index + offset, clone_plain_paragraph(p, part))

    missing = [old[:80] for old, count in split_counts.items() if count != 1]
    if missing:
        raise ValueError(f"DOCX split paragraphs missing or duplicated: {missing}")

    in_references = False
    current_figure: str | None = None
    for p in body.xpath(".//w:p", namespaces=NS):
        text = paragraph_text(p)
        if text == "Referências Bibliográficas":
            in_references = True
        elif text.startswith("Anexo A"):
            in_references = False

        number = figure_number(text)
        if number:
            current_figure = number
        elif current_figure and (
            text.startswith("Fonte original:")
            or text.startswith("Adaptado de")
            or text.startswith("Adaptação de")
            or text.startswith("Reproduzido de")
            or text.startswith("Produção própria")
            or text.startswith("Fonte: produção própria")
        ):
            new_text = replace_provenance_text(text, current_figure)
            if new_text != text:
                # Only replace the provenance prefix to preserve hyperlink runs.
                old_prefix = text[: len(text) - len(text.lstrip())]
                del old_prefix
                for t in p.xpath(".//w:t", namespaces=NS):
                    node_text = t.text or ""
                    for prefix in (
                        "Fonte original: ",
                        "Adaptado de fonte original: ",
                        "Adaptado de ",
                        "Adaptação de ",
                        "Reproduzido de ",
                        "Produção própria.",
                        "Produção própria",
                        "Fonte: produção própria.",
                        "Fonte: produção própria",
                    ):
                        if node_text.startswith(prefix):
                            replacement = provenance_prefix(current_figure)
                            if current_figure in OWN_FIGURES:
                                t.text = replacement + node_text[len(prefix) :]
                            else:
                                t.text = replacement + node_text[len(prefix) :]
                            break
                    else:
                        continue
                    break
                license_name = FIGURE_LICENSES.get(current_figure)
                if license_name:
                    ts = p.xpath(".//w:t", namespaces=NS)
                    if ts and f"Licença: {license_name}." not in paragraph_text(p):
                        ts[-1].text = (ts[-1].text or "").rstrip() + f" Licença: {license_name}."
            current_figure = None

        source_or_reference = in_references or text.startswith(
            ("Fonte original:", "Adaptado de", "Adaptação de", "Reproduzido de")
        )
        for t in p.xpath(".//w:t", namespaces=NS):
            if t.text:
                t.text = apply_exact(t.text) if source_or_reference else apply_words(t.text)
        updated_text = paragraph_text(p)
        for prefix, license_name in LICENSED_SOURCE_PREFIXES.items():
            if updated_text.startswith(prefix) and f"Licença: {license_name}." not in updated_text:
                ts = p.xpath(".//w:t", namespaces=NS)
                if ts:
                    ts[-1].text = (ts[-1].text or "").rstrip() + f" Licença: {license_name}."
                break

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def process_docx(path: Path) -> None:
    with ZipFile(path, "r") as zin:
        members = [(info, zin.read(info.filename)) for info in zin.infolist()]

    fd, temp_name = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    temp = Path(temp_name)
    try:
        with ZipFile(temp, "w", ZIP_DEFLATED) as zout:
            for info, data in members:
                if info.filename == "word/document.xml":
                    data = process_document_xml(data)
                zout.writestr(info, data)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--docx", type=Path, required=True)
    args = parser.parse_args()
    process_markdown(args.markdown)
    process_docx(args.docx)
    print(f"Markdown: {args.markdown}")
    print(f"DOCX: {args.docx}")


if __name__ == "__main__":
    main()
