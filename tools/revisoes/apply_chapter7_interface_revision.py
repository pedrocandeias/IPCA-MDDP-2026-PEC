#!/usr/bin/env python3
"""Apply the evidence-aligned Chapter 7 interface revision to the thesis DOCX."""

from __future__ import annotations

import argparse
import os
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def qn(name: str) -> str:
    return f"{{{W}}}{name}"


def text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_text(paragraph: etree._Element, value: str) -> None:
    p_pr = paragraph.find(qn("pPr"))
    for child in list(paragraph):
        if child is not p_pr:
            paragraph.remove(child)
    run = etree.SubElement(paragraph, qn("r"))
    node = etree.SubElement(run, qn("t"))
    node.text = value


def find(root: etree._Element, prefix: str) -> etree._Element:
    matches = [
        p for p in root.xpath("//w:body/w:p", namespaces=NS)
        if text(p).startswith(prefix)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one paragraph beginning {prefix!r}; found {len(matches)}")
    return matches[0]


def replace(root: etree._Element, prefix: str, value: str) -> etree._Element:
    paragraph = find(root, prefix)
    set_text(paragraph, value)
    return paragraph


def insert_before(reference: etree._Element, value: str) -> None:
    paragraph = deepcopy(reference)
    set_text(paragraph, value)
    reference.addprevious(paragraph)


OUTLINE = (
    "A dissertação organiza-se em nove capítulos principais. O Capítulo 1 apresenta o enquadramento, "
    "o problema, os objectivos, as questões de investigação e a abordagem metodológica geral. O "
    "Capítulo 2 desenvolve o enquadramento teórico e o estado da arte. O Capítulo 3 explicita a "
    "metodologia de investigação. O Capítulo 4 descreve o desenvolvimento do modelo paramétrico. O "
    "Capítulo 5 aborda a plataforma web e a integração digital. O Capítulo 6 trata da integração da "
    "inteligência artificial. O Capítulo 7 apresenta os princípios de interface e as decisões de "
    "interacção implementadas. O Capítulo 8 reúne a avaliação e a discussão dos resultados. Por fim, "
    "o Capítulo 9 sintetiza as conclusões e os trabalhos futuros."
)

RANGES = (
    "O espaço de configuração apresentado não é ilimitado. A interface expõe apenas os campos "
    "declarados para o modelo, apresenta os intervalos existentes e exclui decisões como a lateralidade "
    "do pedido enviado à IA. Esta contenção orienta a configuração, mas não garante, por si só, que "
    "todas as entradas respeitem as mesmas regras. Os testes complementares mostraram que um valor "
    "acima do intervalo podia permanecer no estado interno da aplicação e que um campo numérico podia "
    "receber texto através de um pedido directo. Assim, o controlo visual deve ser acompanhado pela "
    "verificação do valor antes de este ser aplicado, guardado ou enviado para a geometria."
)

ACCESSIBILITY = (
    "A avaliação automática de acessibilidade examinou oito estados do percurso autenticado e "
    "identificou quatro categorias de barreira: contraste insuficiente, ausência de associação "
    "programática entre alguns rótulos e controlos, elementos interactivos aninhados e falta de nome "
    "acessível num elemento de selecção. Estes resultados permitem localizar decisões de interface a "
    "rever, mas não demonstram a experiência de pessoas com diferentes capacidades. As verificações "
    "manuais por teclado, ampliação, leitor de ecrã e alternativa ao visualizador tridimensional "
    "permanecem por realizar."
)

SECTION_71_END = (
    "Assim, esta secção descreve uma especificação projectual, as funções disponíveis e os limites já "
    "observados. Clareza, carga cognitiva, aprendizagem, acessibilidade percebida e adequação aos "
    "diferentes perfis permanecem questões para avaliação futura com participantes."
)

MECHANISMS = (
    "Quatro mecanismos concretizam essa função: exposição selectiva dos parâmetros; apresentação dos "
    "respectivos limites; diferenciação de permissões; e separação visual entre sugestão, configuração "
    "e geometria gerada. Em conjunto, estes mecanismos permitem examinar parte da relação entre valor, "
    "controlo e resultado, mas também condicionam o conjunto de alternativas que pode ser explorado "
    "(Bai et al., 2024; Peixoto et al., 2025; Quintero et al., 2018)."
)

NEUTRALITY = (
    "Esta condição impede considerar a interface neutra. Um valor apresentado como sugestão pode "
    "adquirir aparência de validade, mesmo quando resulta de uma referência populacional incompleta ou "
    "de uma saída probabilística. Por isso, a origem, a incerteza e o estatuto de cada valor devem "
    "permanecer visíveis; a versão avaliada implementa apenas parte dessa comunicação."
)

RECOVERY = (
    "A separação entre sugestão, configuração e geometria constitui uma decisão projectual observável. "
    "Uma resposta de IA inválida preservou o último estado válido e permitiu nova tentativa, mostrando "
    "capacidade de recuperação nesse percurso. Contudo, a aplicação de um valor acima do intervalo "
    "revelou que a reversibilidade e a limitação do espaço paramétrico ainda não estão asseguradas em "
    "todas as entradas. A aprendizagem resultante é que mensagens, limites e regras devem permanecer "
    "coerentes para além dos controlos visíveis da interface."
)

EVIDENCE = (
    "A evidência disponível permite descrever a organização das decisões, identificar salvaguardas "
    "incorporadas e localizar barreiras técnicas de acessibilidade. Não permite concluir que os "
    "diferentes perfis compreendem os limites, tomam melhores decisões ou utilizam a plataforma com "
    "menor esforço. Essas questões exigem observação de tarefas com participantes."
)


def apply(document_xml: bytes) -> bytes:
    root = etree.fromstring(document_xml, etree.XMLParser(remove_blank_text=False))
    if any(
        text(p).startswith("A avaliação automática de acessibilidade examinou oito estados")
        for p in root.xpath("//w:body/w:p", namespaces=NS)
    ):
        raise RuntimeError("The Chapter 7 interface revision is already present")

    replace(root, "A dissertação organiza-se em nove capítulos principais.", OUTLINE)
    replace(root, "O espaço de configuração apresentado não é ilimitado.", RANGES)
    end_71 = find(root, "Assim, esta secção descreve uma especificação projectual")
    insert_before(end_71, ACCESSIBILITY)
    set_text(end_71, SECTION_71_END)

    replace(root, "Quatro mecanismos concretizam essa função:", MECHANISMS)
    replace(root, "Esta condição impede considerar a interface neutra.", NEUTRALITY)
    evidence = find(root, "A evidência disponível permite descrever a organização das decisões")
    insert_before(evidence, RECOVERY)
    set_text(evidence, EVIDENCE)

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    path = args.docx.resolve()

    with ZipFile(path, "r") as archive:
        updated = apply(archive.read("word/document.xml"))

    fd, temporary = tempfile.mkstemp(suffix=".docx", dir=path.parent)
    os.close(fd)
    try:
        with ZipFile(path, "r") as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                data = updated if item.filename == "word/document.xml" else source.read(item.filename)
                target.writestr(item, data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


if __name__ == "__main__":
    main()
