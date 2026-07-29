#!/usr/bin/env python3
"""Integra no DOCX 0.4.72 a observação de montagem da Phoenix.

A intervenção altera apenas ``word/document.xml``. Todos os restantes componentes
do pacote DOCX são copiados sem modificação e a contagem de referências a notas,
comentários e imagens é validada antes da substituição do ficheiro canónico.
"""

from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx")
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_run_text(run: etree._Element, value: str) -> None:
    texts = run.xpath("./w:t", namespaces=NS)
    if len(texts) != 1:
        raise RuntimeError(f"Esperava um único elemento de texto; encontrei {len(texts)}")
    texts[0].text = value
    if value[:1].isspace() or value[-1:].isspace():
        texts[0].set(XML_SPACE, "preserve")
    else:
        texts[0].attrib.pop(XML_SPACE, None)


def document_state(root: etree._Element) -> dict[str, int]:
    return {
        "footnote_references": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "comment_references": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def main() -> None:
    if not DOCX.exists():
        raise SystemExit(f"Ficheiro não encontrado: {DOCX}")

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    before_other_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }
    root = etree.fromstring(entries["word/document.xml"])
    before_state = document_state(root)
    paragraphs = root.xpath("//w:body/w:p", namespaces=NS)

    old_heading_start = (
        "- Verificação de montagem e articulação: o protocolo e a folha de registo"
    )
    new_heading_start = (
        "- Verificação de montagem e articulação: a folha contém uma observação da"
    )
    old_continuation = (
        "foram preparados, mas não existem ainda observações preenchidas que "
        "permitam apresentar resultados de movimento, fecho ou retorno."
    )
    new_continuation = (
        "UnLimbited Phoenix, correspondente ao perfil de ensaio de 15 anos e "
        "produzida em PLA. A montagem foi concluída, os pinos foram colocados sem "
        "dano ou correcção, os cinco dedos apresentaram movimento livre e foram "
        "observados o fecho por cabo e o retorno. Depois de ensaios repetidos, os "
        "elásticos das articulações alargaram e tiveram de ser substituídos. Não "
        "ficaram registados o número exacto de ciclos nem os ensaios com cilindros; "
        "por isso, o resultado permanece parcial."
    )
    starts = [
        p
        for p in paragraphs
        if paragraph_text(p) in {old_heading_start, new_heading_start}
    ]
    continuations = [
        p
        for p in paragraphs
        if paragraph_text(p) in {old_continuation, new_continuation}
    ]
    if len(starts) != 1 or len(continuations) != 1:
        raise RuntimeError(
            "Não foi possível identificar univocamente o registo de montagem antigo"
        )

    start = starts[0]
    continuation = continuations[0]
    if start.getnext() is not continuation:
        raise RuntimeError("Os dois parágrafos do registo antigo deixaram de ser adjacentes")
    if paragraph_text(start) == old_heading_start:
        runs = start.xpath("./w:r", namespaces=NS)
        if len(runs) != 3:
            raise RuntimeError("A formatação do início do registo de montagem foi alterada")
        set_run_text(runs[2], " a folha contém uma observação da")
        set_run_text(
            continuation.xpath("./w:r", namespaces=NS)[0], new_continuation
        )

    # O rótulo e a continuação pertencem ao mesmo ponto. Impede que o rótulo
    # fique isolado no fundo de uma página.
    paragraph_properties = start.find(f"{{{W}}}pPr")
    if paragraph_properties is None:
        paragraph_properties = etree.Element(f"{{{W}}}pPr")
        start.insert(0, paragraph_properties)
    if paragraph_properties.find(f"{{{W}}}keepNext") is None:
        paragraph_properties.append(etree.Element(f"{{{W}}}keepNext"))

    petg_text = (
        "- Que as peças em PETG foram impressas, manipuladas e medidas sem "
        "dificuldades impeditivas do procedimento. Como enquadramento da literatura, "
        "o PETG apresentou maior resistência à deformação térmica no estudo de "
        "Hsueh et al. (2021) e maior ductilidade no estudo de Martins et al. (2024)."
    )
    petg_paragraphs = [p for p in paragraphs if paragraph_text(p) == petg_text]
    if len(petg_paragraphs) != 1:
        raise RuntimeError("Não foi possível identificar o último ponto de D.8")
    phoenix_text = (
        "- Que, num espécime UnLimbited Phoenix correspondente ao perfil de ensaio "
        "de 15 anos e produzido em PLA, a montagem foi concluída e foram observados "
        "o movimento livre dos cinco dedos, o fecho por cabo e o retorno; os "
        "elásticos das articulações alargaram durante os ensaios repetidos e tiveram "
        "de ser substituídos."
    )
    existing_phoenix = [p for p in paragraphs if paragraph_text(p) == phoenix_text]
    if len(existing_phoenix) > 1:
        raise RuntimeError("O novo ponto de D.8 aparece mais de uma vez")
    if not existing_phoenix:
        petg = petg_paragraphs[0]
        phoenix = deepcopy(petg)
        phoenix_runs = phoenix.xpath("./w:r", namespaces=NS)
        if len(phoenix_runs) != 1:
            raise RuntimeError("A formatação do ponto de D.8 foi alterada")
        set_run_text(phoenix_runs[0], phoenix_text)
        petg.addnext(phoenix)

    after_state = document_state(root)
    if after_state != before_state:
        raise RuntimeError(
            f"Referências internas alteradas: antes={before_state}; depois={after_state}"
        )

    entries["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True
    )

    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            result_entries = {
                info.filename: result.read(info.filename) for info in result.infolist()
            }
        after_other_hashes = {
            name: sha256(data).hexdigest()
            for name, data in result_entries.items()
            if name != "word/document.xml"
        }
        if after_other_hashes != before_other_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        DOCX.unlink()
        temporary.replace(DOCX)
    finally:
        if temporary.exists():
            temporary.unlink()

    print(
        "Anexo D actualizado no DOCX; "
        f"notas={before_state['footnote_references']}, "
        f"comentários={before_state['comment_references']}, "
        f"imagens={before_state['drawings']}"
    )


if __name__ == "__main__":
    main()
