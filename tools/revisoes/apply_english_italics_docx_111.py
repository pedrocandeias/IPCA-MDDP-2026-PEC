#!/usr/bin/env python3
"""Aplica itálico aos estrangeirismos ingleses no DOCX canónico.

Reutiliza as listas e regras curadas de apply_english_italics_055.py e
acrescenta as salvaguardas que o DOCX gerido pelo Mendeley Cite exige:

  - a região da bibliografia é detectada pela primeira entrada («Akasaka…»)
    até ao cabeçalho «Anexo A», já que o cabeçalho «Bibliografia» foi
    perdido no DOCX; nada é alterado nessa região;
  - runs dentro de content controls do Mendeley (citações vivas e
    bibliografia) nunca são divididos;
  - runs que contenham notas de rodapé, comentários, imagens ou campos
    nunca são divididos — apenas runs de texto simples;
  - termos em maiúsculas integrais (p. ex. «DESIGN» na capa) não são
    italicizados;
  - índices e sumários (parágrafos com PAGEREF) ficam intactos, porque o
    Word os regenera;
  - só word/document.xml é alterado; notas de rodapé (footnotes.xml) e
    todas as outras partes ficam byte a byte idênticas (verificado).

Uso: apply_english_italics_docx_111.py [--apply]
"""

from __future__ import annotations

import re
import sys
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_english_italics_055 import (  # noqa: E402
    NS, SOURCE_PREFIXES, W, merge_spans, paragraph_text,
    split_text_node, target_docx_spans, text_node_is_italic,
)

ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
WNS = "{%s}" % W

UNSAFE_CHILDREN = [WNS + n for n in
                   ("footnoteReference", "endnoteReference",
                    "commentReference", "drawing", "fldChar", "instrText")]


def run_is_safe(node) -> bool:
    run = node.getparent()
    if run is None or run.tag != WNS + "r":
        return False
    if any(run.find(tag) is not None for tag in UNSAFE_CHILDREN):
        return False
    for anc in node.iterancestors():
        if anc.tag == WNS + "sdt":
            tag = anc.find(WNS + "sdtPr/" + WNS + "tag")
            if tag is not None and "MENDELEY" in (tag.get(WNS + "val") or ""):
                return False
    return True


def state(root) -> dict:
    return {
        "footnotes": len(root.findall(".//" + WNS + "footnoteReference")),
        "comments": len(root.findall(".//" + WNS + "commentReference")),
        "drawings": len(root.findall(".//" + WNS + "drawing")),
        "sdts": len(root.findall(".//" + WNS + "sdt")),
    }


def main() -> None:
    apply = "--apply" in sys.argv

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        parts = {i.filename: source.read(i.filename) for i in infos}
    other_hashes = {n: sha256(d).hexdigest() for n, d in parts.items()
                    if n != "word/document.xml"}

    root = etree.fromstring(parts["word/document.xml"])
    before = state(root)

    paras = root.findall(".//" + WNS + "p")
    bib_start = next((i for i, p in enumerate(paras)
                      if paragraph_text(p).strip().startswith("Akasaka")), None)
    bib_end = next((i for i in range((bib_start or 0) + 1, len(paras))
                    if re.match(r"Anexo\s+A", paragraph_text(paras[i]).strip())),
                   None)
    if bib_start is None or bib_end is None:
        raise RuntimeError("Não localizei a região da bibliografia")

    changes = 0
    touched_paras = 0
    in_abstract = False
    for i, paragraph in enumerate(paras):
        text = paragraph_text(paragraph)
        stripped = text.strip()
        if stripped.upper() == "ABSTRACT":
            in_abstract = True
        elif (stripped.upper().startswith("LISTA DE ABREVIATURAS")
              or stripped.upper().startswith("LISTA DE ACRÓNIMOS")):
            in_abstract = False

        if (not stripped or in_abstract
                or bib_start <= i < bib_end
                or stripped.startswith(("Adaptado de", "Reproduzido de",
                                        "Fonte:"))
                or stripped.startswith("INTEGRATION OF DESIGN")
                or stripped.startswith("INTEGRAÇÃO DO DESIGN")
                or any("PAGEREF" in (n.text or "")
                       for n in paragraph.iter(WNS + "instrText"))):
            continue

        targets = [(s, e) for s, e in target_docx_spans(text)
                   if not (text[s:e].isupper() and e - s > 3)
                   and not text[e:].startswith(" e Desenvolvimento de Produto")]
        if not targets:
            continue

        nodes = paragraph.findall(".//" + WNS + "t")
        offset = 0
        work = []
        for node in nodes:
            value = node.text or ""
            node_start, node_end = offset, offset + len(value)
            intervals = []
            for start, end in targets:
                a, b = max(start, node_start), min(end, node_end)
                if (a < b and not text_node_is_italic(node)
                        and run_is_safe(node)):
                    intervals.append((a - node_start, b - node_start))
            if intervals:
                work.append((node, merge_spans(intervals)))
            offset = node_end
        if work:
            touched_paras += 1
        for node, intervals in reversed(work):
            changes += split_text_node(node, intervals)

    after = state(root)
    if after != before:
        raise RuntimeError(f"Contagens alteradas: {before} -> {after}")

    print(f"Segmentos italicizados: {changes} em {touched_paras} parágrafos.")
    if not apply:
        print("DRY RUN — nada foi gravado. Use --apply.")
        return

    parts["word/document.xml"] = etree.tostring(
        root, xml_declaration=True, encoding="UTF-8", standalone=True)
    with NamedTemporaryFile(prefix=f".{DOCX.name}.", suffix=".tmp",
                            dir=DOCX.parent, delete=False) as h:
        tmp = Path(h.name)
    try:
        with ZipFile(tmp, "w", ZIP_DEFLATED) as out:
            for i in infos:
                out.writestr(i, parts[i.filename])
        with ZipFile(tmp) as check:
            if check.testzip() is not None:
                raise RuntimeError("DOCX resultante corrompido")
            result = {i.filename: sha256(check.read(i.filename)).hexdigest()
                      for i in check.infolist()
                      if i.filename != "word/document.xml"}
        if result != other_hashes:
            raise RuntimeError("Parte externa a document.xml foi alterada")
        tmp.replace(DOCX)
        print("DOCX gravado.")
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
