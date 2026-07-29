#!/usr/bin/env python3
"""Resolve três comentários bibliográficos e os marcadores editoriais [^9]–[^13]."""

from __future__ import annotations

import os
import re
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

OLD_REG_MD = (
    "As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas "
    "à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância "
    "ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pelo "
    "Regulamento (UE) 2017/745 (MDR), que classifica os dispositivos nas Classes I, IIa, IIb e "
    "III. Dispositivos terapêuticos activos, incluindo próteses mioeléctricas, enquadram-se "
    "geralmente nas classes intermédias ou superiores, o que exige avaliação por um organismo "
    "notificado para efeitos de marcação CE (Parlamento Europeu & Conselho da União Europeia, "
    "2017)."
)
NEW_REG_MD = (
    "As próteses de membro superior são classificadas como dispositivos médicos e estão sujeitas "
    "à regulamentação específica destinada a garantir a segurança, o desempenho e a vigilância "
    "ao longo de todo o ciclo de vida. Na União Europeia, o enquadramento é definido pelo "
    "Regulamento (UE) 2017/745, habitualmente designado pela sigla inglesa MDR (*Medical Device "
    "Regulation*). Nos termos do artigo 51.º, os dispositivos são integrados nas classes I, IIa, "
    "IIb e III de acordo com a finalidade prevista e os riscos intrínsecos, aplicando-se as regras "
    "do Anexo VIII. Assim, a classe de uma prótese de membro superior, incluindo uma prótese "
    "mioeléctrica, não decorre apenas do tipo de accionamento, mas das características e da "
    "finalidade previstas para o dispositivo. Antes da colocação no mercado, o fabricante deve "
    "aplicar o procedimento de avaliação da conformidade correspondente; os dispositivos "
    "considerados conformes ostentam a marcação CE e, nas classes IIa, IIb e III, o procedimento "
    "envolve um organismo notificado (Parlamento Europeu & Conselho da União Europeia, 2017)."
)

OLD_MACE_MD = (
    "O *design* universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente "
    "aplicada no *design* industrial, tendo como princípio orientador a concepção de produtos e "
    "ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações "
    "ou de *design* especializado. Os Sete Princípios do *design* universal, propostos por Ron "
    "Mace, são amplamente citados como um quadro normativo para avaliar equidade, flexibilidade, "
    "simplicidade, tolerância ao erro e redução do esforço físico (Story, 2006)."
)
NEW_MACE_MD = (
    "O *design* universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente "
    "aplicada no *design* industrial, tendo como princípio orientador a concepção de produtos e "
    "ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações "
    "ou de *design* especializado. Os Sete Princípios do *design* universal foram compilados por "
    "um grupo de dez investigadores e profissionais que incluiu Ron Mace e publicados em 1997 "
    "pelo *Center for Universal Design* da *North Carolina State University*. O quadro abrange uso "
    "equitativo, flexibilidade no uso, utilização simples e intuitiva, informação perceptível, "
    "tolerância ao erro, baixo esforço físico e dimensão e espaço adequados à aproximação e à "
    "utilização (Center for Universal Design, 1997)."
)

OLD_WIBERG_MD = (
    "Wiberg et al. (2019) demonstram, no sistema que avaliaram, que a determinação experimental "
    "dos constrangimentos do processo e a sua incorporação no modelo paramétrico permitiram gerar "
    "milhares de variantes com elevada taxa de sucesso funcional e reduzir reimpressões. [^9]"
)
NEW_WIBERG_MD = (
    "A revisão de Wiberg et al. (2019) organiza os métodos e as ferramentas de apoio ao DfAM "
    "segundo as diferentes etapas do processo de desenvolvimento, permitindo relacionar o apoio "
    "disponível com o momento do processo em que é necessário."
)

OLD_LINK_MD = (
    "Esta evidência reforça a necessidade de uma ligação sistemática entre as fases de *design* e "
    "fabrico, contrariando abordagens que tratam o fabrico como etapa posterior e correctiva "
    "(Chtioui et al., 2023; Wiberg et al., 2019)."
)
NEW_LINK_MD = OLD_LINK_MD.replace("Esta evidência", "Esta estrutura")

OLD_TECH_MD = (
    "As tecnologias de fabrico aditivo (FA) utilizadas incluem modelação por deposição fundida "
    "(FDM) e fabrico por filamento fundido (FFF), ambos baseados na extrusão de termoplásticos, "
    "SLS (fusão selectiva a laser), SLA (estereolitografia) e processos industriais metálicos, o "
    "que reflecte a diversidade de rotas produtivas para componentes personalizados. Cada "
    "tecnologia implica requisitos específicos de projecto, reforçando a importância de integrar "
    "critérios técnicos no modelo paramétrico desde o início (Chtioui et al., 2023; Wiberg et al., "
    "2019).[^10]"
)
NEW_TECH_MD = (
    "As tecnologias de fabrico aditivo recorrem a materiais e mecanismos de consolidação "
    "distintos. A modelação por deposição fundida (FDM) e o fabrico por filamento fundido (FFF) "
    "depositam sucessivamente camadas de termoplástico extrudido; a sinterização selectiva a laser "
    "(SLS) consolida material em pó; e a estereolitografia (SLA) solidifica uma resina líquida por "
    "acção da luz. Os processos industriais para metais recorrem frequentemente à fusão em leito "
    "de pó. Estas diferenças condicionam a orientação de fabrico, as espessuras mínimas, a "
    "necessidade de suportes, o acabamento superficial e o desempenho mecânico. A tecnologia deve, "
    "por isso, ser considerada desde a definição do modelo paramétrico, e não apenas no momento da "
    "produção (Chtioui et al., 2023; Wiberg et al., 2019)."
)

OLD_FACTORY_MD = (
    "Este modelo “*file-to-factory*” viabiliza fluxos digitais em que o ficheiro parametrizado é "
    "convertido directamente em instruções de fabrico, seja localmente (impressão 3D "
    "descentralizada) ou por meio de uma encomenda *online*[^11]. A literatura associa esta lógica "
    "à democratização do *design* e à expansão de estratégias de customização em massa (*mass "
    "customization*) e personalização em massa (*mass personalization*), reduzindo custos marginais "
    "ao dispensar moldes e dispositivos específicos de fabrico.[^12] (Lei et al., 2016; van "
    "Stralen, 2018)."
)
NEW_FACTORY_MD = (
    "Este modelo “*file-to-factory*” viabiliza um fluxo digital em que o ficheiro parametrizado é "
    "convertido directamente em instruções de fabrico. A produção pode ocorrer localmente, por "
    "impressão 3D descentralizada, ou mediante o envio do ficheiro a um serviço externo de fabrico "
    "digital. Ao ligar a variação digital à produção física, este fluxo apoia estratégias de "
    "customização em massa (*mass customization*) e personalização em massa (*mass "
    "personalization*), nas quais diferentes configurações são produzidas a partir de uma "
    "estrutura comum (Lei et al., 2016; van Stralen, 2018)."
)

OLD_COST_MD = (
    "Em termos económicos, a Fabrico Aditivo permite reduzir [^13]penalizações tradicionais "
    "associadas à variação de produto, sustentando modelos de personalização acessíveis. Estudos "
    "orientados para famílias de produto indicam que a integração de modelos paramétricos com "
    "análises de custo e desempenho pode manter os custos relativamente estáveis mesmo com elevada "
    "diversidade geométrica (Lei et al., 2016; Yao et al., 2016)."
)
NEW_COST_MD = (
    "Em termos económicos, o fabrico aditivo pode reduzir os sobrecustos tradicionalmente "
    "associados à produção de variantes. Estudos orientados para famílias de produto indicam que a "
    "integração de modelos paramétricos com análises de custo e desempenho pode manter os custos "
    "relativamente estáveis mesmo com elevada diversidade geométrica (Lei et al., 2016; Yao et "
    "al., 2016)."
)

OLD_REG_BIB_MD = (
    '<a id="ref-parlamento-europeu-2017"></a> Parlamento Europeu, & Conselho da União Europeia. '
    "(2017). Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April "
    "2017 on medical devices. https://eur-lex.europa.eu/eli/reg/2017/745/oj"
)
NEW_REG_BIB_MD = (
    '<a id="ref-parlamento-europeu-2017"></a> Parlamento Europeu, & Conselho da União Europeia. '
    "(2017). *Regulamento (UE) 2017/745 do Parlamento Europeu e do Conselho, de 5 de abril de "
    "2017, relativo aos dispositivos médicos, que altera a Diretiva 2001/83/CE, o Regulamento "
    "(CE) n.º 178/2002 e o Regulamento (CE) n.º 1223/2009 e que revoga as Diretivas 90/385/CEE e "
    "93/42/CEE do Conselho*. *Jornal Oficial da União Europeia, L 117*, 1–175. "
    "https://eur-lex.europa.eu/eli/reg/2017/745/oj"
)

CABIBIHAN_BIB_MD = (
    '<a id="ref-cabibihan-2018"></a> Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & '
    "Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high "
    "accuracy shape and size. IEEE Access, 6, 25029-25039. "
    "https://doi.org/10.1109/ACCESS.2018.2831907"
)
CENTER_BIB_MD = (
    '<a id="ref-center-universal-design-1997"></a> Center for Universal Design. (1997). '
    "*The principles of universal design* (Version 2.0). North Carolina State University. "
    "https://design.ncsu.edu/research/center-for-universal-design/"
)


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text_of(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS))


def add_run(paragraph: etree._Element, value: str, *, italic: bool = False) -> None:
    run = etree.SubElement(paragraph, qn("r"))
    if italic:
        properties = etree.SubElement(run, qn("rPr"))
        etree.SubElement(properties, qn("i"))
        etree.SubElement(properties, qn("iCs"))
    node = etree.SubElement(run, qn("t"))
    node.text = value
    if value[:1].isspace() or value[-1:].isspace():
        node.set(XML_SPACE, "preserve")


def find_paragraph(root: etree._Element, exact: str) -> etree._Element:
    matches = [p for p in root.xpath("//w:p", namespaces=NS) if text_of(p) == exact]
    if len(matches) != 1:
        raise RuntimeError(f"Parágrafo DOCX inesperado para {exact[:80]!r}: {len(matches)}")
    return matches[0]


def replace_paragraph(
    root: etree._Element, exact: str, parts: tuple[tuple[str, bool], ...]
) -> etree._Element:
    paragraph = find_paragraph(root, exact)
    properties = paragraph.find(qn("pPr"))
    properties_copy = deepcopy(properties) if properties is not None else None
    for child in list(paragraph):
        paragraph.remove(child)
    if properties_copy is not None:
        paragraph.append(properties_copy)
    for value, italic in parts:
        add_run(paragraph, value, italic=italic)
    return paragraph


def remove_comments(document: etree._Element, comments: etree._Element) -> None:
    for tag in ("commentRangeStart", "commentRangeEnd"):
        for node in document.xpath(f"//w:{tag}", namespaces=NS):
            node.getparent().remove(node)
    for reference in document.xpath("//w:commentReference", namespaces=NS):
        run = reference.getparent()
        parent = run.getparent()
        if text_of(run):
            run.remove(reference)
        else:
            parent.remove(run)
    for comment in comments.xpath("//w:comment", namespaces=NS):
        comment.getparent().remove(comment)


def update_markdown() -> str:
    markdown = MD.read_text(encoding="utf-8")
    replacements = (
        ("Versão do documento: 0.4.97", "Versão do documento: 0.4.98"),
        (OLD_REG_MD, NEW_REG_MD),
        (OLD_MACE_MD, NEW_MACE_MD),
        (OLD_WIBERG_MD, NEW_WIBERG_MD),
        (OLD_LINK_MD, NEW_LINK_MD),
        (OLD_TECH_MD, NEW_TECH_MD),
        (OLD_FACTORY_MD, NEW_FACTORY_MD),
        (OLD_COST_MD, NEW_COST_MD),
        (OLD_REG_BIB_MD, NEW_REG_BIB_MD),
    )
    for old, _ in replacements:
        count = markdown.count(old)
        if count != 1:
            raise RuntimeError(f"Ocorrências Markdown inesperadas para {old[:80]!r}: {count}")
    if markdown.count(CABIBIHAN_BIB_MD) != 1 or CENTER_BIB_MD in markdown:
        raise RuntimeError("Âncora bibliográfica do Center for Universal Design inesperada")
    for old, new in replacements:
        markdown = markdown.replace(old, new, 1)
    markdown = markdown.replace(
        CABIBIHAN_BIB_MD, f"{CABIBIHAN_BIB_MD}\n\n{CENTER_BIB_MD}", 1
    )
    if re.search(r"\[\^(?:9|10|11|12|13)\]", markdown):
        raise RuntimeError("Permaneceram marcadores editoriais [^9]–[^13] no Markdown")
    return markdown


def update_document(document: etree._Element) -> None:
    old_reg_docx = OLD_REG_MD.replace("activos", "ativos").replace("projecto", "projeto")
    replace_paragraph(
        document,
        old_reg_docx,
        (
            (
                "As próteses de membro superior são classificadas como dispositivos médicos e "
                "estão sujeitas à regulamentação específica destinada a garantir a segurança, o "
                "desempenho e a vigilância ao longo de todo o ciclo de vida. Na União Europeia, o "
                "enquadramento é definido pelo Regulamento (UE) 2017/745, habitualmente designado "
                "pela sigla inglesa MDR (",
                False,
            ),
            ("Medical Device Regulation", True),
            (
                "). Nos termos do artigo 51.º, os dispositivos são integrados nas classes I, IIa, "
                "IIb e III de acordo com a finalidade prevista e os riscos intrínsecos, aplicando-"
                "se as regras do Anexo VIII. Assim, a classe de uma prótese de membro superior, "
                "incluindo uma prótese mioeléctrica, não decorre apenas do tipo de acionamento, mas "
                "das características e da finalidade previstas para o dispositivo. Antes da "
                "colocação no mercado, o fabricante deve aplicar o procedimento de avaliação da "
                "conformidade correspondente; os dispositivos considerados conformes ostentam a "
                "marcação CE e, nas classes IIa, IIb e III, o procedimento envolve um organismo "
                "notificado (Parlamento Europeu & Conselho da União Europeia, 2017).",
                False,
            ),
        ),
    )

    old_mace_docx = (
        OLD_MACE_MD.replace("*", "")
        .replace("concepção", "conceção")
        .replace("projecto", "projeto")
    )
    replace_paragraph(
        document,
        old_mace_docx,
        (
            ("O ", False),
            ("design", True),
            (" universal, por sua vez, é frequentemente enquadrado como uma abordagem amplamente aplicada no ", False),
            ("design", True),
            (" industrial, tendo como princípio orientador a conceção de produtos e ambientes utilizáveis pelo maior número possível de pessoas, sem necessidade de adaptações ou de ", False),
            ("design", True),
            (" especializado. Os Sete Princípios do ", False),
            ("design", True),
            (" universal foram compilados por um grupo de dez investigadores e profissionais que incluiu Ron Mace e publicados em 1997 pelo ", False),
            ("Center for Universal Design", True),
            (" da ", False),
            ("North Carolina State University", True),
            (". O quadro abrange uso equitativo, flexibilidade no uso, utilização simples e intuitiva, informação percetível, tolerância ao erro, baixo esforço físico e dimensão e espaço adequados à aproximação e à utilização (Center for Universal Design, 1997).", False),
        ),
    )

    replace_paragraph(
        document,
        OLD_WIBERG_MD.removesuffix(" [^9]"),
        ((NEW_WIBERG_MD, False),),
    )
    replace_paragraph(
        document,
        OLD_LINK_MD.replace("*", ""),
        (
            ("Esta estrutura reforça a necessidade de uma ligação sistemática entre as fases de ", False),
            ("design", True),
            (" e fabrico, contrariando abordagens que tratam o fabrico como etapa posterior e correctiva (Chtioui et al., 2023; Wiberg et al., 2019).", False),
        ),
    )
    old_tech_docx = OLD_TECH_MD.removesuffix("[^10]")
    replace_paragraph(
        document,
        old_tech_docx,
        ((NEW_TECH_MD.replace("selectiva", "seletiva").replace("acção", "ação"), False),),
    )
    old_factory_docx = (
        OLD_FACTORY_MD.replace("*", "")
        .replace("[^11]", "")
        .replace("[^12]", "")
        .replace("fabrico. (Lei", "fabrico (Lei")
    )
    old_factory_paragraph = find_paragraph(document, old_factory_docx)
    footnote_runs = old_factory_paragraph.xpath(
        ".//w:r[w:footnoteReference[@w:id='3']]", namespaces=NS
    )
    if len(footnote_runs) != 1:
        raise RuntimeError(f"Nota de rodapé de file-to-factory inesperada: {len(footnote_runs)}")
    factory_footnote_run = deepcopy(footnote_runs[0])
    factory_paragraph = replace_paragraph(
        document,
        old_factory_docx,
        (
            ("Este modelo “", False),
            ("file-to-factory", True),
            ("”", False),
            (" viabiliza um fluxo digital em que o ficheiro parametrizado é convertido directamente em instruções de fabrico. A produção pode ocorrer localmente, por impressão 3D descentralizada, ou mediante o envio do ficheiro a um serviço externo de fabrico digital. Ao ligar a variação digital à produção física, este fluxo apoia estratégias de customização em massa (", False),
            ("mass customization", True),
            (") e personalização em massa (", False),
            ("mass personalization", True),
            ("), nas quais diferentes configurações são produzidas a partir de uma estrutura comum (Lei et al., 2016; van Stralen, 2018).", False),
        ),
    )
    factory_runs = factory_paragraph.xpath("./w:r", namespaces=NS)
    if len(factory_runs) != 8:
        raise RuntimeError(f"Estrutura reconstruída de file-to-factory inesperada: {len(factory_runs)}")
    factory_runs[2].addnext(factory_footnote_run)
    replace_paragraph(
        document,
        OLD_COST_MD,
        ((NEW_COST_MD, False),),
    )

    old_reg_bib_docx = OLD_REG_BIB_MD.split("></a> ", 1)[1]
    replace_paragraph(
        document,
        old_reg_bib_docx,
        (
            ("Parlamento Europeu, & Conselho da União Europeia. (2017). ", False),
            (
                "Regulamento (UE) 2017/745 do Parlamento Europeu e do Conselho, de 5 de abril de "
                "2017, relativo aos dispositivos médicos, que altera a Diretiva 2001/83/CE, o "
                "Regulamento (CE) n.º 178/2002 e o Regulamento (CE) n.º 1223/2009 e que revoga as "
                "Diretivas 90/385/CEE e 93/42/CEE do Conselho",
                True,
            ),
            (". ", False),
            ("Jornal Oficial da União Europeia, L 117", True),
            (", 1–175. https://eur-lex.europa.eu/eli/reg/2017/745/oj", False),
        ),
    )

    cabibihan_docx = CABIBIHAN_BIB_MD.split("></a> ", 1)[1]
    anchor = find_paragraph(document, cabibihan_docx)
    ppr = anchor.find(qn("pPr"))
    new_paragraph = etree.Element(qn("p"))
    if ppr is not None:
        new_paragraph.append(deepcopy(ppr))
    add_run(new_paragraph, "Center for Universal Design. (1997). ")
    add_run(new_paragraph, "The principles of universal design", italic=True)
    add_run(
        new_paragraph,
        " (Version 2.0). North Carolina State University. "
        "https://design.ncsu.edu/research/center-for-universal-design/",
    )
    anchor.addnext(new_paragraph)


def main() -> None:
    markdown = update_markdown()
    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}
    mutable = {"word/document.xml", "word/comments.xml"}
    external_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name not in mutable
    }
    parser = etree.XMLParser(remove_blank_text=False)
    document = etree.fromstring(entries["word/document.xml"], parser)
    comments = etree.fromstring(entries["word/comments.xml"], parser)
    before_footnotes = len(document.xpath("//w:footnoteReference", namespaces=NS))
    before_drawings = len(document.xpath("//w:drawing", namespaces=NS))
    before_tables = len(document.xpath("//w:tbl", namespaces=NS))
    before_comment_defs = len(comments.xpath("//w:comment", namespaces=NS))

    update_document(document)
    remove_comments(document, comments)

    body = text_of(document)
    required = (
        "habitualmente designado pela sigla inglesa MDR",
        "Center for Universal Design. (1997). The principles of universal design",
        "A revisão de Wiberg et al. (2019) organiza os métodos",
        "serviço externo de fabrico digital",
        "reduzir os sobrecustos tradicionalmente associados à produção de variantes",
        "Jornal Oficial da União Europeia, L 117",
    )
    for value in required:
        if value not in body:
            raise RuntimeError(f"Conteúdo DOCX em falta: {value}")
    if re.search(r"\[\^(?:9|10|11|12|13)\]", body):
        raise RuntimeError("Permaneceram marcadores editoriais no DOCX")
    if document.xpath(
        "//w:commentRangeStart|//w:commentRangeEnd|//w:commentReference", namespaces=NS
    ):
        raise RuntimeError("Permaneceram âncoras de comentários no DOCX")
    if comments.xpath("//w:comment", namespaces=NS):
        raise RuntimeError("Permaneceram comentários no DOCX")
    after = {
        "footnotes": len(document.xpath("//w:footnoteReference", namespaces=NS)),
        "drawings": len(document.xpath("//w:drawing", namespaces=NS)),
        "tables": len(document.xpath("//w:tbl", namespaces=NS)),
    }
    before_sensitive = {
        "footnotes": before_footnotes,
        "drawings": before_drawings,
        "tables": before_tables,
    }
    if after != before_sensitive:
        raise RuntimeError(
            f"A estrutura sensível do DOCX foi alterada: {before_sensitive} -> {after}"
        )

    entries["word/document.xml"] = etree.tostring(
        document, xml_declaration=True, encoding="UTF-8", standalone=True
    )
    entries["word/comments.xml"] = etree.tostring(
        comments, xml_declaration=True, encoding="UTF-8", standalone=True
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
                if info.filename not in mutable
            }
        if result_hashes != external_hashes:
            raise RuntimeError("Um componente não autorizado do DOCX foi alterado")
        MD.write_text(markdown, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        f"Versão 0.4.98 concluída; comentários resolvidos={before_comment_defs}; "
        f"notas de rodapé={after['footnotes']}; imagens={after['drawings']}; "
        f"tabelas={after['tables']}"
    )


if __name__ == "__main__":
    main()
