#!/usr/bin/env python3
"""Corrige quatro blocos críticos de atribuição bibliográfica na versão 0.4.103."""

from __future__ import annotations

import os
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

from update_oldfrey_scope_099 import NS, qn, sensitive_state, set_space, text_of


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"


OLD_ROBUSTNESS_MD = (
    "A literatura converge para a ideia de que a robustez do modelo paramétrico é uma "
    "condição crítica para a personalização em escala. Modelos mal estruturados ou com "
    "dependências inconsistentes podem comprometer a simulação, a optimização e a "
    "configuração de famílias de produto (Lei et al., 2016; Wiberg et al., 2019)."
)
NEW_ROBUSTNESS_MD = (
    "A personalização em escala depende de uma definição controlada do espaço de "
    "variação. Os parâmetros de *design*, as relações entre esses parâmetros e os "
    "respectivos constrangimentos delimitam as combinações válidas e devem ser "
    "caracterizados por meio de simulação ou experimentação. Para o *design*, esta "
    "estrutura permite ampliar a variedade de soluções sem gerar configurações "
    "inviáveis ou difíceis de fabricar (Ozdemir et al., 2022)."
)
NEW_ROBUSTNESS_PARTS = (
    ("A personalização em escala depende de uma definição controlada do espaço de variação. Os parâmetros de ", False),
    ("design", True),
    (", as relações entre esses parâmetros e os respectivos constrangimentos delimitam as combinações válidas e devem ser caracterizados por meio de simulação ou experimentação. Para o ", False),
    ("design", True),
    (", esta estrutura permite ampliar a variedade de soluções sem gerar configurações inviáveis ou difíceis de fabricar (Ozdemir et al., 2022).", False),
)

OLD_CONFIGURATORS_MD = (
    "Controlar parâmetros constitui uma das condições centrais para transformar um "
    "modelo paramétrico num sistema configurável e persistente. Os ficheiros de "
    "configuração descrevem cada parâmetro segundo nome, tipo, valor inicial, limites, "
    "incrementos e grupo temático. Esta estrutura liga o código OpenSCAD ao espaço de "
    "alteração apresentado na interface. Em termos metodológicos, aproxima-se da lógica "
    "dos configuradores e das famílias de produto, nas quais a variação depende da "
    "preservação das relações do modelo-base (Ozdemir et al., 2022; Lei et al., 2016)."
)
NEW_CONFIGURATORS_MD = (
    "Controlar parâmetros constitui uma das condições centrais para transformar um "
    "modelo paramétrico num sistema configurável e persistente. Os ficheiros de "
    "configuração descrevem cada parâmetro segundo nome, tipo, valor inicial, limites, "
    "incrementos e grupo temático. Esta estrutura liga o código OpenSCAD ao espaço de "
    "alteração apresentado na interface. Em termos metodológicos, aproxima-se da lógica "
    "dos configuradores e da personalização em massa, em que uma arquitectura de base "
    "integra características variáveis e informação sobre a forma como podem ser "
    "modificadas (Ozdemir et al., 2022)."
)

OLD_EXPANSION_MD = (
    "Quanto à expansão, a separação entre modelos, parâmetros, interface, autenticação e "
    "persistência permite acrescentar modelos OpenSCAD sem redesenhar todo o percurso. A "
    "experiência com o Paraglider, o Phoenix, o Flexy Beast e o Cyborg Beast mostrou, "
    "contudo, que não basta adicionar um ficheiro `.scad`: é necessário declarar "
    "parâmetros, dependências, limites e modos de visualização e, em alguns casos, "
    "corrigir incompatibilidades ou preservar interfaces mecânicas herdadas. A expansão "
    "é, portanto, uma actividade controlada de adaptação do projecto, e não uma "
    "importação automática de geometrias (Lei et al., 2016; Ozdemir et al., 2022)."
)
NEW_EXPANSION_MD = (
    "Quanto à expansão, a separação entre modelos, parâmetros, interface, autenticação e "
    "persistência permite acrescentar modelos OpenSCAD sem redesenhar todo o percurso. Em "
    "sistemas de personalização, a arquitectura de base deve identificar as "
    "características variáveis e a forma como podem ser modificadas; os parâmetros, as "
    "respectivas dependências e os constrangimentos delimitam depois o espaço de soluções "
    "válidas (Ozdemir et al., 2022). No HandFab, a integração do Paraglider, do Phoenix, "
    "do Flexy Beast e do Cyborg Beast mostrou que não bastava acrescentar um ficheiro "
    "`.scad`: foi necessário declarar parâmetros, limites, dependências e modos de "
    "visualização e, em alguns casos, corrigir incompatibilidades ou preservar interfaces "
    "mecânicas herdadas. A expansão correspondeu, assim, a uma adaptação de *design* "
    "controlada, na qual a lógica geométrica e mecânica de cada modelo foi traduzida para "
    "a arquitectura configurável da plataforma; não constituiu uma importação automática "
    "de geometrias."
)
NEW_EXPANSION_PARTS = (
    ("Quanto à expansão, a separação entre modelos, parâmetros, interface, autenticação e persistência permite acrescentar modelos OpenSCAD sem redesenhar todo o percurso. Em sistemas de personalização, a arquitectura de base deve identificar as características variáveis e a forma como podem ser modificadas; os parâmetros, as respectivas dependências e os constrangimentos delimitam depois o espaço de soluções válidas (Ozdemir et al., 2022). No HandFab, a integração do Paraglider, do Phoenix, do Flexy Beast e do Cyborg Beast mostrou que não bastava acrescentar um ficheiro .scad: foi necessário declarar parâmetros, limites, dependências e modos de visualização e, em alguns casos, corrigir incompatibilidades ou preservar interfaces mecânicas herdadas. A expansão correspondeu, assim, a uma adaptação de ", False),
    ("design", True),
    (" controlada, na qual a lógica geométrica e mecânica de cada modelo foi traduzida para a arquitectura configurável da plataforma; não constituiu uma importação automática de geometrias.", False),
)

OLD_AI_MD = (
    "Em termos gerais, a IA pode ser entendida como um conjunto de métodos computacionais "
    "orientados para executar tarefas que requerem aprendizagem, reconhecimento de "
    "padrões, inferência ou geração de respostas com base em dados. Neste contexto, "
    "inferência designa o processo pelo qual um sistema aplica padrões aprendidos durante "
    "o treino a novos dados de entrada, produzindo uma classificação, previsão, "
    "recomendação ou resposta compatível com esses padrões. Esta definição evita tratar a "
    "IA como uma entidade única ou como sinónimo de inteligência humana generalizada. A "
    "maioria dos sistemas actuais opera sobre tipos específicos de problemas a partir de "
    "exemplos, regularidades e relações estatísticas aprendidas durante o treino, sem "
    "possuir uma capacidade geral de pensamento (Choudhury et al., 2025; Yüksel et al., "
    "2023)."
)
NEW_AI_MD = (
    "Em termos gerais, a IA pode ser entendida como um conjunto de métodos computacionais "
    "orientados para executar tarefas que requerem aprendizagem, reconhecimento de "
    "padrões, inferência ou geração de respostas com base em dados. Neste contexto, "
    "inferência designa o processo pelo qual um sistema aplica padrões aprendidos durante "
    "o treino a novos dados de entrada, produzindo uma classificação, previsão, "
    "recomendação ou resposta compatível com esses padrões. Entre as abordagens abrangidas "
    "pela IA, a aprendizagem automática permite que os sistemas aprendam a partir de "
    "dados, identifiquem padrões e produzam previsões ou decisões sem que cada resposta "
    "seja previamente programada (Wang & Hu, 2024). A aplicação destes sistemas permanece "
    "delimitada: no contexto do *design*, um algoritmo desenvolvido para um problema "
    "particular geralmente não é aplicável a outros e revela pouca capacidade de "
    "adaptação a condições diferentes (Yüksel et al., 2023). Por esse motivo, nesta "
    "dissertação, o desempenho numa tarefa específica não é equiparado a uma capacidade "
    "geral de pensamento."
)
NEW_AI_PARTS = (
    ("Em termos gerais, a IA pode ser entendida como um conjunto de métodos computacionais orientados para executar tarefas que requerem aprendizagem, reconhecimento de padrões, inferência ou geração de respostas com base em dados. Neste contexto, inferência designa o processo pelo qual um sistema aplica padrões aprendidos durante o treino a novos dados de entrada, produzindo uma classificação, previsão, recomendação ou resposta compatível com esses padrões. Entre as abordagens abrangidas pela IA, a aprendizagem automática permite que os sistemas aprendam a partir de dados, identifiquem padrões e produzam previsões ou decisões sem que cada resposta seja previamente programada (Wang & Hu, 2024). A aplicação destes sistemas permanece delimitada: no contexto do ", False),
    ("design", True),
    (", um algoritmo desenvolvido para um problema particular geralmente não é aplicável a outros e revela pouca capacidade de adaptação a condições diferentes (Yüksel et al., 2023). Por esse motivo, nesta dissertação, o desempenho numa tarefa específica não é equiparado a uma capacidade geral de pensamento.", False),
)

OLD_MONITORING_MD = (
    "Um aspecto estruturante desta lacuna é a ausência de fluxos metodológicos "
    "consistentes e acessíveis que articulem medição, decisão de projecto e validação. "
    "Esta ausência dificulta a utilização de dados objectivos para orientar ajustes "
    "individualizados. Mesmo quando são propostas soluções baseadas em sensores e na "
    "monitorização do uso, persistem barreiras práticas, como o custo, a autonomia da "
    "bateria, a disponibilidade de equipamentos e a necessidade de formação técnica, o "
    "que limita a sua adopção como prática clínica regular (Chadwell et al., 2020; "
    "Richardson & Dillon, 2017)."
)
NEW_MONITORING_MD = (
    "Na avaliação das próteses do membro superior, a literatura identifica a falta de "
    "critérios comuns e de medidas especificamente desenvolvidas para esta população, o "
    "que limita a produção de dados objectivos e comparáveis sobre a experiência e o "
    "desempenho dos dispositivos (Cordella et al., 2016; Jones et al., 2023). Para o "
    "*design*, Chadwell et al. (2020) assinalam que continuam a existir poucos dados "
    "objectivos sobre os ajustamentos do dispositivo que poderiam aumentar a sua "
    "utilidade no ambiente quotidiano do utilizador. A monitorização em contexto real "
    "pode complementar as avaliações clínicas e contribuir para o desenvolvimento de "
    "dispositivos mais ajustados às necessidades individuais. Contudo, a sua aplicação "
    "por meio de sensores continua condicionada pelo custo, pela autonomia limitada das "
    "baterias, pela disponibilidade dos equipamentos e pela formação necessária à "
    "recolha e interpretação dos dados, o que dificulta a adopção desta prática em "
    "contexto clínico corrente."
)
NEW_MONITORING_PARTS = (
    ("Na avaliação das próteses do membro superior, a literatura identifica a falta de critérios comuns e de medidas especificamente desenvolvidas para esta população, o que limita a produção de dados objectivos e comparáveis sobre a experiência e o desempenho dos dispositivos (Cordella et al., 2016; Jones et al., 2023). Para o ", False),
    ("design", True),
    (", Chadwell et al. (2020) assinalam que continuam a existir poucos dados objectivos sobre os ajustamentos do dispositivo que poderiam aumentar a sua utilidade no ambiente quotidiano do utilizador. A monitorização em contexto real pode complementar as avaliações clínicas e contribuir para o desenvolvimento de dispositivos mais ajustados às necessidades individuais. Contudo, a sua aplicação por meio de sensores continua condicionada pelo custo, pela autonomia limitada das baterias, pela disponibilidade dos equipamentos e pela formação necessária à recolha e interpretação dos dados, o que dificulta a adopção desta prática em contexto clínico corrente.", False),
)

OLD_PROOF_MD = (
    "O estudo acrescenta uma relação documentada entre entrada, decisão e artefacto, mas "
    "permanece no nível de prova de conceito técnica identificado como frequente na "
    "literatura (Chadwell et al., 2020; Samuelsson et al., 2012; Windrich et al., 2016)"
)
NEW_PROOF_MD = (
    "O estudo documenta a relação entre os dados de entrada, as decisões de *design* e o "
    "artefacto produzido, mas permanece no domínio de uma avaliação técnica preliminar. "
    "Esta delimitação é coerente com as limitações identificadas na investigação sobre "
    "próteses do membro superior: predominância de demonstrações de viabilidade sem "
    "avaliação da eficácia, estudos com amostras reduzidas e métodos de avaliação "
    "heterogéneos e escassez de dados objectivos sobre a utilização quotidiana dos "
    "dispositivos (Diment et al., 2018; Chadwell et al., 2020; Jones et al., 2023)"
)
NEW_PROOF_PARTS = (
    ("O estudo documenta a relação entre os dados de entrada, as decisões de ", False),
    ("design", True),
    (" e o artefacto produzido, mas permanece no domínio de uma avaliação técnica preliminar. Esta delimitação é coerente com as limitações identificadas na investigação sobre próteses do membro superior: predominância de demonstrações de viabilidade sem avaliação da eficácia, estudos com amostras reduzidas e métodos de avaliação heterogéneos e escassez de dados objectivos sobre a utilização quotidiana dos dispositivos (Diment et al., 2018; Chadwell et al., 2020; Jones et al., 2023)", False),
)


BIBLIOGRAPHY = (
    (
        '<a id="ref-chadwell-2020"></a> Chadwell, A., Kenney, L., Thies, S., Galpin, A., & Head, J. (2020). Technology for monitoring everyday prosthesis use: A systematic review.',
        '<a id="ref-chadwell-2020"></a> Chadwell, A., Diment, L., Micó-Amigo, M., Morgado Ramírez, D. Z., Dickinson, A., Granat, M., Kenney, L., Kheng, S., Sobuh, M., Ssekitoleko, R., & Worsley, P. (2020). Technology for monitoring everyday prosthesis use: A systematic review. *Journal of NeuroEngineering and Rehabilitation, 17*, Article 93. https://doi.org/10.1186/s12984-020-00711-4',
        "Chadwell, A., Kenney, L., Thies, S., Galpin, A., & Head, J. (2020). Technology for monitoring everyday prosthesis use: A systematic review.",
        (
            ("Chadwell, A., Diment, L., Micó-Amigo, M., Morgado Ramírez, D. Z., Dickinson, A., Granat, M., Kenney, L., Kheng, S., Sobuh, M., Ssekitoleko, R., & Worsley, P. (2020). Technology for monitoring everyday prosthesis use: A systematic review. ", False),
            ("Journal of NeuroEngineering and Rehabilitation, 17", True),
            (", Article 93. https://doi.org/10.1186/s12984-020-00711-4", False),
        ),
    ),
    (
        '<a id="ref-cordella-2016"></a> Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users.',
        '<a id="ref-cordella-2016"></a> Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users. *Frontiers in Neuroscience, 10*, Article 209. https://doi.org/10.3389/fnins.2016.00209',
        "Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users.",
        (
            ("Cordella, F., Ciancio, A. L., Sacchetti, R., Davalli, A., Cutti, A. G., Guglielmelli, E., & Zollo, L. (2016). Literature review on needs of upper limb prosthesis users. ", False),
            ("Frontiers in Neuroscience, 10", True),
            (", Article 209. https://doi.org/10.3389/fnins.2016.00209", False),
        ),
    ),
    (
        '<a id="ref-lei-2016"></a> Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. https://dr.ntu.edu.sg/bitstream/10356/83735/1/An%20additive%20manufacturing%20process%20model%20for%20product%20family%20design.pdf',
        '<a id="ref-lei-2016"></a> Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. *Journal of Engineering Design, 27*(11), 751–767. https://doi.org/10.1080/09544828.2016.1228101',
        "Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. https://dr.ntu.edu.sg/bitstream/10356/83735/1/An%20additive%20manufacturing%20process%20model%20for%20product%20family%20design.pdf",
        (
            ("Lei, N., Yao, X., Moon, S. K., & Bi, G. (2016). An additive manufacturing process model for product family design. ", False),
            ("Journal of Engineering Design, 27", True),
            ("(11), 751–767. https://doi.org/10.1080/09544828.2016.1228101", False),
        ),
    ),
    (
        '<a id="ref-ozdemir-2022"></a> Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0F2B66A61E2CE6410F9D1F335244EB9C/S2053470122000038a.pdf/div-class-title-design-methodology-for-mass-personalisation-enabled-by-digital-manufacturing-div.pdf',
        '<a id="ref-ozdemir-2022"></a> Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. *Design Science, 8*, e7. https://doi.org/10.1017/dsj.2022.3',
        "Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0F2B66A61E2CE6410F9D1F335244EB9C/S2053470122000038a.pdf/div-class-title-design-methodology-for-mass-personalisation-enabled-by-digital-manufacturing-div.pdf",
        (
            ("Ozdemir, M., Verlinden, J., & Cascini, G. (2022). Design methodology for mass personalisation enabled by digital manufacturing. ", False),
            ("Design Science, 8", True),
            (", e7. https://doi.org/10.1017/dsj.2022.3", False),
        ),
    ),
    (
        '<a id="ref-richardson-2017"></a> Richardson, C., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review.',
        '<a id="ref-richardson-2017"></a> Richardson, A., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review. *Prosthetics and Orthotics International, 41*(1), 6–18. https://doi.org/10.1177/0309364616631343',
        "Richardson, C., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review.",
        (
            ("Richardson, A., & Dillon, M. P. (2017). User experience of transtibial prosthetic liners: A systematic review. ", False),
            ("Prosthetics and Orthotics International, 41", True),
            ("(1), 6–18. https://doi.org/10.1177/0309364616631343", False),
        ),
    ),
)


BODY = (
    (OLD_ROBUSTNESS_MD, NEW_ROBUSTNESS_MD, NEW_ROBUSTNESS_PARTS),
    (OLD_CONFIGURATORS_MD, NEW_CONFIGURATORS_MD, ((NEW_CONFIGURATORS_MD, False),)),
    (OLD_EXPANSION_MD, NEW_EXPANSION_MD, NEW_EXPANSION_PARTS),
    (OLD_AI_MD, NEW_AI_MD, NEW_AI_PARTS),
    (OLD_MONITORING_MD, NEW_MONITORING_MD, NEW_MONITORING_PARTS),
    (OLD_PROOF_MD, NEW_PROOF_MD, NEW_PROOF_PARTS),
)


def add_run(paragraph: etree._Element, value: str, *, italic: bool) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    set_space(node)


def replace_paragraph(root: etree._Element, old: str, parts: tuple[tuple[str, bool], ...]) -> None:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == old]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo inesperado no DOCX: {len(matches)} para {old[:80]!r}")
    paragraph = matches[0]
    if paragraph.xpath(
        ".//w:footnoteReference | .//w:commentReference | .//w:commentRangeStart | "
        ".//w:commentRangeEnd | .//w:drawing",
        namespaces=NS,
    ):
        raise RuntimeError(f"O parágrafo contém estrutura sensível: {old[:80]!r}")
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    if markdown.count("Versão do documento: 0.4.102") != 1:
        raise RuntimeError("Versão Markdown inesperada")
    markdown = markdown.replace(
        "Versão do documento: 0.4.102", "Versão do documento: 0.4.103", 1
    )
    for old, new, _ in BODY:
        if markdown.count(old) != 1 or new in markdown:
            raise RuntimeError(f"Estado Markdown inesperado para {old[:80]!r}")
        markdown = markdown.replace(old, new, 1)
    for old, new, _, _ in BIBLIOGRAPHY:
        if markdown.count(old) != 1 or new in markdown:
            raise RuntimeError(f"Bibliografia Markdown inesperada para {old[:80]!r}")
        markdown = markdown.replace(old, new, 1)
    return markdown


def main() -> None:
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    parser = etree.XMLParser(remove_blank_text=False)
    root = etree.fromstring(entries["word/document.xml"], parser)
    before = sensitive_state(root)

    version_matches = [
        p
        for p in root.xpath("//w:p", namespaces=NS)
        if text_of(p) == "Versão do documento: 0.4.102"
    ]
    if version_matches:
        replace_paragraph(
            root,
            "Versão do documento: 0.4.102",
            (("Versão do documento: 0.4.103", False),),
        )
    for old_md, _, parts in BODY:
        old_docx = old_md.replace("*", "").replace("`", "")
        replace_paragraph(root, old_docx, parts)
    for _, _, old_docx, parts in BIBLIOGRAPHY:
        replace_paragraph(root, old_docx, parts)

    after = sensitive_state(root)
    if after != before:
        raise RuntimeError(f"Estrutura sensível alterada: {before} -> {after}")
    paragraphs = [text_of(p) for p in root.xpath("//w:p", namespaces=NS)]
    for old_md, new_md, _ in BODY:
        old_docx = old_md.replace("*", "").replace("`", "")
        new_docx = new_md.replace("*", "").replace("`", "")
        if old_docx in paragraphs or paragraphs.count(new_docx) != 1:
            raise RuntimeError(f"Substituição DOCX incompleta: {old_docx[:80]!r}")
    for _, new_md, old_docx, _ in BIBLIOGRAPHY:
        new_docx = new_md.split("</a> ", 1)[1].replace("*", "")
        if old_docx in paragraphs or paragraphs.count(new_docx) != 1:
            raise RuntimeError(f"Bibliografia DOCX incompleta: {old_docx[:80]!r}")

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "Quatro blocos bibliográficos corrigidos; "
        f"notas={after['footnotes']}, comentários={after['comments']}, "
        f"imagens={after['drawings']}, tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
