#!/usr/bin/env python3
"""Renumera as tabelas no DOCX canónico e remove os órfãos da antiga Figura 30.

Intervenções em word/document.xml (todas as outras partes ficam intactas):
  1. A legenda «Tabela 4 — Ciclos de Research Through Design», cujo número
     era texto literal, passa a usar um campo SEQ Tabela como as restantes;
     o Word renumera as tabelas seguintes ao actualizar campos (Ctrl+A, F9)
     e o índice de tabelas regenera-se na actualização.
  2. São removidos os três parágrafos órfãos da figura eliminada pelo autor
     (frase introdutória, legenda «Figura 30 — Tarefas funcionais…» e o
     crédito «Reproduzido de …» com a citação viva associada).
  3. As referências a tabelas no corpo do texto (texto literal, sem campos
     REF) são alinhadas com o Markdown 0.4.109, usado como gabarito por
     correspondência de contexto.

Requer o ficheiro fechado no Word. Notas de rodapé, comentários e imagens
não são tocados; o script verifica as contagens antes e depois.
"""

from __future__ import annotations

import json
import re
import sys
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

ROOT = Path(__file__).resolve().parents[2]
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
WNS = "{%s}" % W

REF_RE = re.compile(r"Tabelas?\s+\d+(?:\s+e\s+\d+|\s+a\s+\d+)?")
DOTTED_RE = re.compile(r"(Figura|Tabela)(s?\s+)(\d+\.\d+)"
                       r"(?:(\s+e\s+)(\d+\.\d+))?")

# Numeração por capítulo -> sequencial (derivada em renumber_figures_tables_108)
FIG_MAP = {"1.1": "1", "2.1": "2", "2.2": "3", "2.3": "4", "2.4": "5",
           "2.5": "6", "2.6": "7", "2.7": "8", "2.8": "9", "3.1": "10",
           "3.2": "11", "4.1": "12", "4.2": "13", "4.3": "14", "5.1": "15",
           "5.2": "16", "5.3": "17", "5.4": "18", "5.5": "19", "5.6": "20",
           "5.7": "21", "5.8": "22", "5.9": "23", "5.10": "24", "6.1": "25",
           "7.1": "26", "8.1": "27", "8.2": "28", "8.3": "29"}
TAB_MAP = {"2.1": "1", "2.2": "2", "2.3": "3", "3.1": "4", "3.2": "5",
           "3.3": "6", "4.1": "7", "4.2": "8", "4.3": "9", "4.4": "10",
           "4.5": "11", "4.6": "12", "4.7": "13", "4.8": "14", "4.9": "15",
           "4.10": "16", "4.11": "17", "5.1": "18", "5.2": "19", "5.3": "20",
           "6.1": "21", "6.2": "22", "8.1": "23", "8.2": "24", "8.3": "25",
           "8.4": "26", "8.5": "27", "8.6": "28", "8.7": "29", "8.8": "30",
           "9.1": "31"}


def norm_ctx(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())[-40:]


def para_text(p) -> str:
    return "".join(n.text or "" for n in p.iter(WNS + "t"))


def md_reference_index() -> list[dict]:
    md = MD.read_text(encoding="utf-8")
    refs = []
    for m in REF_RE.finditer(md):
        after = re.sub(r"[^a-z0-9]", "",
                       md[m.end():m.end() + 70].lower())[:40]
        refs.append({"ctx": norm_ctx(md[max(0, m.start() - 70):m.start()]),
                     "after": after, "ref": m.group(0)})
    return refs


def match_md_ref(ctx: str, md_refs: list[dict],
                 after: str = "") -> str | None:
    for size in (40, 24, 14):
        tail = ctx[-size:]
        if not tail:
            break
        hits = {r["ref"] for r in md_refs if r["ctx"].endswith(tail)}
        if len(hits) == 1:
            return hits.pop()
    if after:
        for size in (40, 24, 14):
            head = after[:size]
            if not head:
                break
            hits = {r["ref"] for r in md_refs
                    if r.get("after", "").startswith(head)}
            if len(hits) == 1:
                return hits.pop()
    return None


def rewrite_paragraph_refs(p, md_refs) -> tuple[int, list[str]]:
    """Alinha as referências de um parágrafo com o MD. Devolve (n, avisos)."""
    runs = [n for n in p.iter(WNS + "t")]
    text = "".join(n.text or "" for n in runs)
    changes = []
    problems = []
    # 1) referências pontuadas (numeração por capítulo esquecida no DOCX)
    for m in DOTTED_RE.finditer(text):
        kind = m.group(1)
        table = FIG_MAP if kind == "Figura" else TAB_MAP
        try:
            new = f"{kind}{m.group(2)}{table[m.group(3)]}"
            if m.group(5):
                new += f"{m.group(4)}{table[m.group(5)]}"
        except KeyError:
            problems.append(f"numeração por capítulo desconhecida: {m.group(0)!r}")
            continue
        changes.append((m.start(), m.end(), new))
    dotted_spans = [(s, e) for s, e, _ in changes]
    # 2) referências simples a tabelas, alinhadas com o MD
    for m in REF_RE.finditer(text):
        if any(s <= m.start() < e for s, e in dotted_spans):
            continue
        if re.match(r"\.\d", text[m.end():m.end() + 2]):
            continue  # parte de uma referência pontuada já tratada
        old = m.group(0)
        after = re.sub(r"[^a-z0-9]", "",
                       text[m.end():m.end() + 70].lower())[:40]
        want = match_md_ref(norm_ctx(text[:m.start()]), md_refs, after)
        if want is None:
            # regra geral: tabelas >= 4 avançam uma unidade (inserção da RTD)
            nums = [int(x) for x in re.findall(r"\d+", old)]
            bumped = re.sub(r"\d+",
                            lambda x: str(int(x.group(0)) + 1)
                            if int(x.group(0)) >= 4 else x.group(0), old)
            if any(n >= 4 for n in nums):
                changes.append((m.start(), m.end(), bumped))
                problems.append(
                    f"sem MD, aplicada regra +1: {old!r} -> {bumped!r} "
                    f"(ctx …{text[max(0,m.start()-35):m.start()]})")
            continue
        if want != old:
            changes.append((m.start(), m.end(), want))
    changes.sort(key=lambda c: c[0])
    if not changes:
        return 0, problems
    # aplica de trás para a frente sobre o texto contínuo e redistribui
    new_text = text
    for start, end, want in reversed(changes):
        new_text = new_text[:start] + want + new_text[end:]
    # redistribuição: primeiro run recebe tudo, restantes esvaziam —
    # apenas em parágrafos simples; se houver campos, tratar com cuidado
    has_fields = any(True for _ in p.iter(WNS + "fldSimple")) or \
        any(True for _ in p.iter(WNS + "instrText"))
    if has_fields:
        # edita apenas o run que contém o número, sem tocar no resto
        offset = 0
        spans = []
        for n in runs:
            l = len(n.text or "")
            spans.append((offset, offset + l, n))
            offset += l
        for start, end, want in reversed(changes):
            hit = [(s, e, n) for s, e, n in spans if s <= start and end <= e]
            if not hit:
                problems.append(f"referência atravessa runs com campos: {text[start:end]!r}")
                continue
            s, e, n = hit[0]
            n.text = n.text[:start - s] + want + n.text[end - s:]
        return len(changes), problems
    for i, n in enumerate(runs):
        n.text = new_text if i == 0 else ""
        if i == 0 and (new_text.startswith(" ") or new_text.endswith(" ")):
            n.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return len(changes), problems


def state(root) -> dict:
    return {
        "footnotes": len(root.findall(".//" + WNS + "footnoteReference")),
        "comments": len(root.findall(".//" + WNS + "commentReference")),
        "drawings": len(root.findall(".//" + WNS + "drawing")),
    }


def main() -> None:
    apply = "--apply" in sys.argv
    md_refs = md_reference_index()

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        parts = {i.filename: source.read(i.filename) for i in infos}
    other_hashes = {n: sha256(d).hexdigest() for n, d in parts.items()
                    if n != "word/document.xml"}

    root = etree.fromstring(parts["word/document.xml"])
    before = state(root)

    body = root.find(WNS + "body")
    paras = list(root.iter(WNS + "p"))

    # 1 — legenda RTD: literal -> campo SEQ
    rtd = [p for p in paras
           if para_text(p).startswith("Tabela 4 — Ciclos de Research")]
    if len(rtd) != 1:
        raise RuntimeError(f"Legenda RTD: esperava 1, encontrei {len(rtd)}")
    p = rtd[0]
    run = next(r for r in p.iter(WNS + "r")
               if "".join(t.text or "" for t in r.iter(WNS + "t")) == "4")
    fld = etree.Element(WNS + "fldSimple")
    fld.set(WNS + "instr", r" SEQ Tabela \* ARABIC ")
    fld.append(deepcopy(run))   # o run «4» fica como valor em cache do campo
    run.addnext(fld)
    run.getparent().remove(run)
    print("1) Legenda RTD convertida para campo SEQ Tabela.")

    # 2 — órfãos da antiga Figura 30
    removed = 0
    for p in list(root.iter(WNS + "p")):
        txt = para_text(p).strip()
        if (txt.startswith("A Figura 30 apresenta um precedente")
                or txt.startswith("Figura 30 — Tarefas funcionais")
                or (txt.startswith("Reproduzido de")
                    and "myoelectric" in txt.lower())):
            parent = p.getparent()
            parent.remove(p)
            removed += 1
    print(f"2) Parágrafos órfãos removidos: {removed}")

    # 3 — referências no corpo
    changed, all_problems = 0, []
    for p in root.iter(WNS + "p"):
        txt = para_text(p)
        if not REF_RE.search(txt) and not DOTTED_RE.search(txt):
            continue
        if txt.startswith(("Tabela ", "Figura ")):
            continue  # legendas e índice
        if any("PAGEREF" in (i.text or "") for i in p.iter(WNS + "instrText")):
            continue  # índice de ilustrações / TOC
        n, problems = rewrite_paragraph_refs(p, md_refs)
        changed += n
        all_problems.extend(problems)
    print(f"3) Referências alinhadas com o MD: {changed}")
    for pr in all_problems:
        print("   AVISO:", pr)

    after = state(root)
    if after != before:
        raise RuntimeError(f"Contagens alteradas: {before} -> {after}")

    if not apply:
        print("\nDRY RUN — nada foi gravado. Use --apply.")
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
        print("\nDOCX gravado. No Word: Ctrl+A, F9 e actualizar os índices.")
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
