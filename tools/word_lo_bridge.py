#!/usr/bin/env python3
"""Ponte Word ↔ LibreOffice para o DOCX com Mendeley Cite (Word).

O LibreOffice preserva as citações vivas do Mendeley Cite (content
controls `MENDELEY_CITATION_v3` e `MENDELEY_BIBLIOGRAPHY`) ao gravar um
DOCX, mas descarta o estado do add-in: as partes `word/webextensions/*`,
a relação `webextensiontaskpanes` em `_rels/.rels` e as entradas
correspondentes em `[Content_Types].xml`. Sem elas, o Mendeley Cite no
Word deixa de reconhecer o documento.

Este script repõe essas peças a partir de uma cópia de referência
guardada antes da edição:

    word_lo_bridge.py backup  <doc.docx>            # antes de abrir no LO
    word_lo_bridge.py restore <doc.docx> [--from R] # depois de gravar no LO

`backup` cria `<doc>.pre-lo-backup.docx`. `restore` usa esse ficheiro
por omissão. O invólucro `editar_docx_libreoffice.sh` encadeia os dois
passos à volta de uma sessão do Writer.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

WEB_PARTS = [
    "word/webextensions/taskpanes.xml",
    "word/webextensions/webextension1.xml",
    "word/webextensions/_rels/taskpanes.xml.rels",
]
TASKPANES_REL_TYPE = ("http://schemas.microsoft.com/office/2011/"
                      "relationships/webextensiontaskpanes")
CT_OVERRIDES = {
    "word/webextensions/taskpanes.xml":
        "application/vnd.ms-office.webextensiontaskpanes+xml",
    "word/webextensions/webextension1.xml":
        "application/vnd.ms-office.webextension+xml",
}


def fail(msg: str) -> None:
    print(f"ERRO: {msg}")
    sys.exit(1)


def backup(docx: Path) -> Path:
    ref = docx.with_suffix(".pre-lo-backup.docx")
    shutil.copy2(docx, ref)
    with ZipFile(ref) as z:
        missing = [p for p in WEB_PARTS if p not in z.namelist()]
    if missing:
        fail(f"a cópia de referência não tem as partes Mendeley: {missing}")
    print(f"Referência guardada: {ref.name}")
    return ref


def merge_content_types(xml: str) -> str:
    for part, ctype in CT_OVERRIDES.items():
        if f'PartName="/{part}"' not in xml:
            xml = xml.replace(
                "</Types>",
                f'<Override PartName="/{part}" ContentType="{ctype}"/></Types>')
    return xml


def merge_root_rels(xml: str) -> str:
    if TASKPANES_REL_TYPE in xml:
        return xml
    used = set(re.findall(r'Id="(rId\d+)"', xml))
    n = 1
    while f"rId{n}" in used:
        n += 1
    rel = (f'<Relationship Id="rId{n}" Type="{TASKPANES_REL_TYPE}" '
           f'Target="word/webextensions/taskpanes.xml"/>')
    return xml.replace("</Relationships>", rel + "</Relationships>")


def restore(docx: Path, ref: Path) -> None:
    if not ref.exists():
        fail(f"referência não encontrada: {ref}")
    with ZipFile(ref) as z:
        ref_parts = {p: z.read(p) for p in WEB_PARTS if p in z.namelist()}
        ref_doc = z.read("word/document.xml").decode("utf-8", "replace")
    if len(ref_parts) != len(WEB_PARTS):
        fail("a referência não contém todas as partes Mendeley")

    with ZipFile(docx) as z:
        infos = z.infolist()
        parts = {i.filename: z.read(i.filename) for i in infos}

    doc = parts["word/document.xml"].decode("utf-8", "replace")
    n_ref = ref_doc.count("MENDELEY_CITATION_v3")
    n_now = doc.count("MENDELEY_CITATION_v3")
    if n_now == 0:
        fail("o documento gravado não tem nenhuma citação viva — "
             "não vou reparar às cegas; verifica o ficheiro")
    if n_now != n_ref:
        print(f"AVISO: nº de citações vivas mudou ({n_ref} -> {n_now}); "
              "normal se apagaste/adicionaste texto com citações. O próximo "
              "Refresh no Word reconcilia o estado do add-in.")

    already = all(p in parts for p in WEB_PARTS)
    for p, data in ref_parts.items():
        if p not in parts:
            parts[p] = data
    parts["[Content_Types].xml"] = merge_content_types(
        parts["[Content_Types].xml"].decode("utf-8")).encode("utf-8")
    parts["_rels/.rels"] = merge_root_rels(
        parts["_rels/.rels"].decode("utf-8")).encode("utf-8")

    names = {i.filename for i in infos}
    with NamedTemporaryFile(prefix=f".{docx.name}.", suffix=".tmp",
                            dir=docx.parent, delete=False) as h:
        tmp = Path(h.name)
    try:
        with ZipFile(tmp, "w", ZIP_DEFLATED) as out:
            for i in infos:
                out.writestr(i, parts[i.filename])
            for p in WEB_PARTS:
                if p not in names:
                    out.writestr(p, parts[p])
        with ZipFile(tmp) as check:
            if check.testzip() is not None:
                fail("o DOCX reparado está corrompido")
            for p in WEB_PARTS:
                if check.read(p) != ref_parts[p]:
                    fail(f"parte restaurada difere da referência: {p}")
        tmp.replace(docx)
    finally:
        tmp.unlink(missing_ok=True)

    estado = "já estava íntegro" if already else "restaurado"
    print(f"OK — estado do Mendeley Cite {estado}; {n_now} citações vivas; "
          "partes webextensions verificadas byte a byte.")


def main() -> None:
    if len(sys.argv) < 3 or sys.argv[1] not in ("backup", "restore"):
        print(__doc__)
        sys.exit(2)
    docx = Path(sys.argv[2]).resolve()
    if not docx.exists():
        fail(f"não existe: {docx}")
    if sys.argv[1] == "backup":
        backup(docx)
    else:
        ref = (Path(sys.argv[sys.argv.index("--from") + 1]).resolve()
               if "--from" in sys.argv
               else docx.with_suffix(".pre-lo-backup.docx"))
        restore(docx, ref)


if __name__ == "__main__":
    main()
