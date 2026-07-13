#!/usr/bin/env python3
"""Migrate the thesis DOCX body into the IPCA final template.

The script keeps the institutional front matter and styles from the IPCA
template, imports the body from a source DOCX, normalizes paragraph/table/caption
styles, copies media and hyperlink relationships, preserves footnotes, and can
optionally insert a static table of contents generated from a previous PDF text
extraction.
"""

from __future__ import annotations

import argparse
import json
import re
from copy import deepcopy
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
XML = "http://www.w3.org/XML/1998/namespace"
DC = "http://purl.org/dc/elements/1.1/"
CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
NS = {"w": W, "r": R, "a": A, "wp": WP, "rel": REL}

BODY_MAX_IMAGE_CX = 5_579_745  # IPCA body section text width, in EMU.
STYLE_BODY = "TextoNormal-IPCA"
STYLE_PREAMBLE = "TtulosPrembulo-IPCA"
STYLE_HEADING_PREFIX = "Cabealho"
STYLE_TOC_PREFIX = "ndice"
STYLE_CAPTION = "Legenda"
STYLE_NOTE = "Nota-IPCA"
STYLE_BIBLIOGRAPHY = "Bibliografia"
STYLE_TABLE = "Tabelacomgrelha"
STYLE_QUOTE = "CitaesLinha-IPCA"
TITLE = (
    "INTEGRAÇÃO DO DESIGN E DA INTELIGÊNCIA ARTIFICIAL EM PROCESSOS PARAMÉTRICOS "
    "PARA O DESENVOLVIMENTO DE PRÓTESES DE MEMBROS SUPERIORES EM IMPRESSÃO 3D."
)
EN_TITLE = (
    "INTEGRATION OF DESIGN AND ARTIFICIAL INTELLIGENCE IN PARAMETRIC PROCESSES "
    "FOR THE DEVELOPMENT OF 3D-PRINTED UPPER-LIMB PROSTHESES"
)
AUTHOR = "Pedro Miguel Candeias da Silva"
SUPERVISOR = "Demétrio Ferreira Matos"
COURSE = "Design e Desenvolvimento de Produto"
DEGREE_LINE = "para obtenção do Grau de Mestre em Design e Desenvolvimento de Produto"
CONCLUSION = "julho, 2026"
DECLARATION_DATE = "13/07/2026"


def qn(ns: str, name: str) -> str:
    return f"{{{ns}}}{name}"


def wt(el: etree._Element) -> str:
    return "".join(el.xpath(".//w:t/text()", namespaces=NS)).strip()


def pstyle(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


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


def make_ppr(
    style_id: str | None = None,
    jc: str | None = None,
    page_break: bool = False,
    suppress_numbering: bool = False,
    ilvl: str = "0",
    preserve_num_pr: etree._Element | None = None,
) -> etree._Element:
    p_pr = etree.Element(qn(W, "pPr"))
    if style_id:
        ps = etree.SubElement(p_pr, qn(W, "pStyle"))
        ps.set(qn(W, "val"), style_id)
    if page_break:
        etree.SubElement(p_pr, qn(W, "pageBreakBefore"))
    if suppress_numbering:
        num_pr = etree.SubElement(p_pr, qn(W, "numPr"))
        il = etree.SubElement(num_pr, qn(W, "ilvl"))
        il.set(qn(W, "val"), ilvl)
        ni = etree.SubElement(num_pr, qn(W, "numId"))
        ni.set(qn(W, "val"), "0")
    elif preserve_num_pr is not None:
        p_pr.append(deepcopy(preserve_num_pr))
    if jc:
        j = etree.SubElement(p_pr, qn(W, "jc"))
        j.set(qn(W, "val"), jc)
    return p_pr


def set_paragraph_style(
    p: etree._Element,
    style_id: str,
    jc: str | None = None,
    page_break: bool = False,
    suppress_numbering: bool = False,
    ilvl: str = "0",
    preserve_num_pr: bool = False,
) -> None:
    old = p.find("w:pPr", NS)
    old_num = old.find("w:numPr", NS) if old is not None and preserve_num_pr else None
    if old is not None:
        p.remove(old)
    p.insert(
        0,
        make_ppr(
            style_id,
            jc=jc,
            page_break=page_break,
            suppress_numbering=suppress_numbering,
            ilvl=ilvl,
            preserve_num_pr=old_num,
        ),
    )


def make_text_para(
    text: str,
    style_id: str,
    jc: str | None = None,
    page_break: bool = False,
    suppress_numbering: bool = False,
    ilvl: str = "0",
) -> etree._Element:
    p = etree.Element(qn(W, "p"))
    p.append(
        make_ppr(
            style_id,
            jc=jc,
            page_break=page_break,
            suppress_numbering=suppress_numbering,
            ilvl=ilvl,
        )
    )
    r = etree.SubElement(p, qn(W, "r"))
    t = etree.SubElement(r, qn(W, "t"))
    if text.startswith(" ") or text.endswith(" "):
        t.set(qn(XML, "space"), "preserve")
    t.text = text
    return p


def strip_comments(el: etree._Element) -> None:
    for n in list(el.xpath(".//w:commentRangeStart|.//w:commentRangeEnd", namespaces=NS)):
        parent = n.getparent()
        if parent is not None:
            parent.remove(n)
    for n in list(el.xpath(".//w:commentReference", namespaces=NS)):
        r = n.getparent()
        parent = r.getparent() if r is not None else None
        if parent is not None and r is not None and r.tag == qn(W, "r"):
            parent.remove(r)
        elif r is not None:
            r.remove(n)


def clean_run_formatting(el: etree._Element) -> None:
    removable = {"rFonts", "sz", "szCs", "color", "highlight", "shd", "lang"}
    for r_pr in el.xpath(".//w:rPr", namespaces=NS):
        for child in list(r_pr):
            if etree.QName(child).localname in removable:
                r_pr.remove(child)
        if len(r_pr) == 0:
            parent = r_pr.getparent()
            if parent is not None:
                parent.remove(r_pr)


def remove_anchor_markup(el: etree._Element) -> None:
    anchor_re = re.compile(r'<a\s+id="[^"]+"\s*>\s*</a>\s*')
    for t in el.xpath(".//w:t", namespaces=NS):
        if t.text:
            t.text = anchor_re.sub("", t.text)


def remove_visible_ref_markers(el: etree._Element) -> None:
    marker_re = re.compile(r"\s*\(#ref-[^)]+\)")
    for t in el.xpath(".//w:t", namespaces=NS):
        if t.text:
            t.text = marker_re.sub("", t.text)


def heading_style_and_level(text: str, source_style: str) -> tuple[str, str]:
    s = " ".join(text.split())
    chapter = re.match(r"^Capítulo\s+\d+\s+[—-]\s*", s, flags=re.I)
    if chapter:
        return f"{STYLE_HEADING_PREFIX}1", "0"
    numbered = re.match(r"^\d+(?:\.\d+)+\s+", s)
    if numbered:
        depth = numbered.group(0).strip().count(".") + 1
        return f"{STYLE_HEADING_PREFIX}{min(depth, 5)}", str(min(depth - 1, 4))
    annex = re.match(r"^A(?:\.\d+)+\s+", s)
    if annex:
        depth = annex.group(0).strip().count(".") + 1
        return f"{STYLE_HEADING_PREFIX}{min(depth, 5)}", str(min(depth - 1, 4))
    if source_style == "Heading2":
        return f"{STYLE_HEADING_PREFIX}2", "1"
    return f"{STYLE_HEADING_PREFIX}3", "2"


def transform_heading(
    text: str, source_style: str
) -> tuple[str, str, str, bool, str] | None:
    s = " ".join(text.split())
    if not s:
        return None
    if source_style == "Heading2" and s.lower() == "bibliografia":
        return STYLE_PREAMBLE, "Referências Bibliográficas", "0", True, "bibliography"
    if source_style == "Heading2" and s.startswith("Anexo "):
        return STYLE_PREAMBLE, s, "0", True, "annex"
    if source_style.startswith("Heading"):
        style_id, ilvl = heading_style_and_level(s, source_style)
        return style_id, s, ilvl, True, "main"
    return None


def make_toc_para(title: str, level: int, page: str) -> etree._Element:
    p = etree.Element(qn(W, "p"))
    p.append(make_ppr(f"{STYLE_TOC_PREFIX}{min(max(level, 1), 5)}"))
    r = etree.SubElement(p, qn(W, "r"))
    t = etree.SubElement(r, qn(W, "t"))
    t.text = title
    etree.SubElement(r, qn(W, "tab"))
    r_page = etree.SubElement(p, qn(W, "r"))
    t_page = etree.SubElement(r_page, qn(W, "t"))
    t_page.text = str(page)
    return p


def clear_toc_sdt(sdt: etree._Element) -> etree._Element:
    sdt = deepcopy(sdt)
    content = sdt.find("w:sdtContent", NS)
    if content is None:
        return sdt
    first_p = content.find(".//w:p", NS)
    old_p_pr = (
        deepcopy(first_p.find("w:pPr", NS))
        if first_p is not None and first_p.find("w:pPr", NS) is not None
        else None
    )
    for ch in list(content):
        content.remove(ch)
    p = etree.Element(qn(W, "p"))
    if old_p_pr is not None:
        p.append(old_p_pr)
    content.append(p)
    return sdt


def add_update_fields(settings_xml: bytes) -> bytes:
    settings = etree.fromstring(settings_xml)
    upd = settings.find("w:updateFields", NS)
    if upd is None:
        upd = etree.Element(qn(W, "updateFields"))
        settings.insert(0, upd)
    upd.set(qn(W, "val"), "true")
    return etree.tostring(settings, xml_declaration=True, encoding="UTF-8", standalone=True)


def update_core_properties(core_xml: bytes) -> bytes:
    core = etree.fromstring(core_xml)
    for tag, value in [
        (qn(DC, "title"), TITLE),
        (qn(DC, "subject"), "Projeto de Mestrado em Design e Desenvolvimento de Produto"),
        (qn(DC, "creator"), "Pedro Miguel Candeias da Silva"),
        (qn(CP, "lastModifiedBy"), "Pedro Miguel Candeias da Silva"),
    ]:
        node = core.find(tag)
        if node is None:
            node = etree.SubElement(core, tag)
        node.text = value
    return etree.tostring(core, xml_declaration=True, encoding="UTF-8", standalone=True)


def serialize(el: etree._Element) -> bytes:
    return etree.tostring(el, xml_declaration=True, encoding="UTF-8", standalone=True)


def read_toc_entries(path: Path | None) -> list[dict[str, str]]:
    if not path:
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def read_entries(path: Path | None) -> list[dict[str, str]]:
    if not path:
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def first_child_index(children: list[etree._Element], predicate) -> int:
    for idx, child in enumerate(children):
        if predicate(child):
            return idx
    raise ValueError("Expected document marker not found")


def has_section_break(p: etree._Element) -> bool:
    return bool(p.xpath("./w:pPr/w:sectPr", namespaces=NS))


def extract_acronyms(source_children: list[etree._Element]) -> list[str]:
    heading_idx = first_child_index(
        source_children,
        lambda ch: ch.tag == qn(W, "p") and wt(ch).lower().startswith("lista de acr"),
    )
    rows: list[str] = []
    for child in source_children[heading_idx + 1 :]:
        if child.tag == qn(W, "p") and pstyle(child).startswith("Heading") and wt(child):
            break
        if child.tag != qn(W, "tbl"):
            continue
        for row in child.xpath("./w:tr", namespaces=NS):
            cells = row.xpath("./w:tc", namespaces=NS)
            if len(cells) < 2:
                continue
            key = wt(cells[0])
            value = wt(cells[1])
            if not key or not value:
                continue
            if key.lower() in {"acrónimo", "sigla"}:
                continue
            rows.append(f"{key} – {value}")
        break
    return rows


def collect_caption_entries(source_children: list[etree._Element], prefix: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for child in source_children:
        if child.tag != qn(W, "p"):
            continue
        text = wt(child)
        if text.startswith(prefix):
            entries.append({"title": text, "page": ""})
    return entries


def append_static_list(
    target: list[etree._Element],
    heading: str,
    entries: list[dict[str, str]],
) -> None:
    target.append(make_text_para(heading, STYLE_PREAMBLE, page_break=True))
    for item in entries:
        target.append(make_toc_para(item["title"], int(item.get("level", 1)), item.get("page", "")))


def extract_frontmatter(path: Path | None) -> dict[str, list[str] | str]:
    if not path:
        return {}
    with ZipFile(path) as z:
        doc = etree.fromstring(z.read("word/document.xml"))
        paras = [wt(p) for p in doc.xpath("//w:body//w:p", namespaces=NS)]
    data: dict[str, list[str] | str] = {}
    for heading, next_heading, body_key, key_key in [
        ("Resumo", "Abstract", "resumo", "palavras"),
        ("Abstract", "Lista de acrónimos", "abstract", "keywords"),
    ]:
        try:
            start = paras.index(heading) + 1
        except ValueError:
            continue
        try:
            end = paras.index(next_heading, start)
        except ValueError:
            end = len(paras)
        body: list[str] = []
        keyword = ""
        for item in paras[start:end]:
            if not item:
                continue
            if item.lower().startswith(("palavras-chave:", "keywords:")):
                keyword = item
            else:
                body.append(item)
        if body:
            data[body_key] = body
        if keyword:
            data[key_key] = keyword
    return data


def apply_frontmatter(children: list[etree._Element], frontmatter: dict[str, list[str] | str]) -> None:
    if not frontmatter:
        return

    def find_child_text(value: str) -> int | None:
        for idx, child in enumerate(children):
            if wt(child) == value:
                return idx
        return None

    def replace_section(heading: str, body_key: str, key_key: str) -> None:
        idx = find_child_text(heading)
        if idx is None:
            return
        body = list(frontmatter.get(body_key, []))
        keyword = str(frontmatter.get(key_key, ""))
        cursor = idx + 1
        body_i = 0
        while cursor < len(children):
            text = wt(children[cursor])
            if text.startswith(("Palavras-chave:", "Keywords:")):
                if keyword:
                    replace_full_text(children[cursor], keyword)
                break
            if text in {"ABSTRACT", "Agradecimentos", "Dedicatória", "Lista de Abreviaturas e/ou Siglas"}:
                break
            if children[cursor].tag == qn(W, "p") and text:
                replace_full_text(children[cursor], body[body_i] if body_i < len(body) else "")
                body_i += 1
            cursor += 1

    replace_section("RESUMO", "resumo", "palavras")
    replace_section("ABSTRACT", "abstract", "keywords")

    title_idx = find_child_text("thEME TITLE")
    if title_idx is None:
        title_idx = find_child_text("THEME TITLE")
    if title_idx is not None:
        replace_full_text(children[title_idx], EN_TITLE)
    subtitle_idx = find_child_text("tHEME SUBTITLE")
    if subtitle_idx is None:
        subtitle_idx = find_child_text("THEME SUBTITLE")
    if subtitle_idx is not None:
        replace_full_text(children[subtitle_idx], "")


def apply_project_details(children: list[etree._Element]) -> None:
    replacements = {
        "Título do Tema": TITLE,
        "TÍTULO DO TEMA": TITLE,
        "SUBTÍTULO DO TEMA": "",
        "SUBTÍTULO DO TEMA (SE APLICÁVEL)": "",
        "SubTítulo do Tema (se aplicável)": "",
        "Subtítulo do Tema (se aplicável)": "",
        "Nome completo do mestrando": AUTHOR,
        "nome do orientador": SUPERVISOR,
        "nome do coorientador (se aplicável)": "",
        "Coorientador": "",
        "mês, ano": CONCLUSION,
        "para obtenção do Grau de Mestre em _______________________": DEGREE_LINE,
        "para obtenção do Grau de Mestre em nome do mestrado": DEGREE_LINE,
        "Nome: Nome completo do mestrando (OBRIGATÓRIO)": f"Nome: {AUTHOR}",
        "Endereço eletrónico: Endereço Eletrónico (OPCIONAL)": "Endereço eletrónico:",
        "Título do Projeto: Título do Tema (OBRIGATÓRIO)": f"Título do Projeto: {TITLE}",
        "Subtítulo do Projeto:  Subtítulo do Tema (SE APLICÁVEL)": "Subtítulo do Projeto:",
        "Orientador: Nome do Orientador (OBRIGATÓRIO)": f"Orientador: {SUPERVISOR}",
        "Coorientador: Nome do Coorientador (SE APLICÁVEL)": "Coorientador:",
        "Ano de conclusão: mês, ano": f"Ano de conclusão: {CONCLUSION}",
        "Designação do Curso de Mestrado: Mestrado em Nome do Mestrado.": (
            f"Designação do Curso de Mestrado: Mestrado em {COURSE}"
        ),
        "Instituto Politécnico do Cávado e do Ave, ___/___/______": (
            f"Instituto Politécnico do Cávado e do Ave, {DECLARATION_DATE}"
        ),
    }
    partial_replacements = {
        "Nome completo do mestrando": AUTHOR,
        "nome do orientador": SUPERVISOR,
        "nome do coorientador (se aplicável)": "",
        "para obtenção do Grau de Mestre em _______________________": DEGREE_LINE,
        "para obtenção do Grau de Mestre em nome do mestrado": DEGREE_LINE,
        "mês, ano": CONCLUSION,
        "Nome completo do mestrando (OBRIGATÓRIO)": AUTHOR,
        "Título do Tema (OBRIGATÓRIO)": TITLE,
        "Nome do Orientador (OBRIGATÓRIO)": SUPERVISOR,
        "Nome do Coorientador (SE APLICÁVEL)": "",
        "Nome do Mestrado": COURSE,
        "SubTítulo do Tema (se aplicável)": "",
        "___/___/______": DECLARATION_DATE,
    }
    for child in children:
        if child.tag != qn(W, "p"):
            continue
        text = wt(child)
        normalized = " ".join(text.split())
        if text in replacements:
            replace_full_text(child, replacements[text])
        elif normalized in replacements:
            replace_full_text(child, replacements[normalized])
        elif text.startswith("☐ É AUTORIZADA A REPRODUÇÃO INTEGRAL"):
            replace_full_text(child, "☒" + text[1:])
        else:
            for t in child.xpath(".//w:t", namespaces=NS):
                if not t.text:
                    continue
                for old, new in partial_replacements.items():
                    t.text = t.text.replace(old, new)


def migrate(
    template: Path,
    source: Path,
    output: Path,
    toc_entries: list[dict[str, str]],
    table_entries: list[dict[str, str]],
    figure_entries: list[dict[str, str]],
    frontmatter: dict[str, list[str] | str],
) -> None:
    with ZipFile(template) as zt, ZipFile(source) as zs:
        files = {n: zt.read(n) for n in zt.namelist()}
        target_doc = etree.fromstring(files["word/document.xml"])
        source_doc = etree.fromstring(zs.read("word/document.xml"))
        target_body = target_doc.find(".//w:body", NS)
        source_body = source_doc.find(".//w:body", NS)
        target_rels = etree.fromstring(files["word/_rels/document.xml.rels"])
        source_rels = etree.fromstring(zs.read("word/_rels/document.xml.rels"))
        source_rel_by_id = {rel.get("Id"): rel for rel in source_rels}
        target_rel_ids = {rel.get("Id") for rel in target_rels}
        nums = [
            int(m.group(1))
            for rid in target_rel_ids
            for m in [re.match(r"rId(\d+)$", rid or "")]
            if m
        ]
        rid_box = {"value": max(nums + [0]) + 1}
        media_box = {"value": 1}
        rel_map: dict[str, str] = {}
        existing_media = {n for n in files if n.startswith("word/media/")}

        def allocate_rid() -> str:
            rid = f"rId{rid_box['value']}"
            rid_box["value"] += 1
            return rid

        def add_relationship(rel_type: str, target: str, target_mode: str | None = None) -> str:
            rid = allocate_rid()
            rel = etree.Element(qn(REL, "Relationship"))
            rel.set("Id", rid)
            rel.set("Type", rel_type)
            rel.set("Target", target)
            if target_mode:
                rel.set("TargetMode", target_mode)
            target_rels.append(rel)
            return rid

        def map_source_rel(rid: str) -> str:
            if rid in rel_map:
                return rel_map[rid]
            srel = source_rel_by_id.get(rid)
            if srel is None:
                return rid
            typ = srel.get("Type")
            tgt = srel.get("Target")
            mode = srel.get("TargetMode")
            if typ.endswith("/image"):
                src_name = str(PurePosixPath("word") / tgt)
                ext = PurePosixPath(src_name).suffix or ".png"
                while True:
                    new_media = f"word/media/source_image{media_box['value']:02d}{ext}"
                    media_box["value"] += 1
                    if new_media not in existing_media:
                        break
                files[new_media] = zs.read(src_name)
                existing_media.add(new_media)
                new_id = add_relationship(typ, f"media/{PurePosixPath(new_media).name}")
            elif typ.endswith("/hyperlink"):
                new_id = add_relationship(typ, tgt, mode or "External")
            else:
                new_id = add_relationship(typ, tgt, mode)
            rel_map[rid] = new_id
            return new_id

        def remap_relationship_refs(el: etree._Element) -> None:
            for blip in el.xpath(".//a:blip[@r:embed]", namespaces=NS):
                blip.set(qn(R, "embed"), map_source_rel(blip.get(qn(R, "embed"))))
            for h in el.xpath(".//w:hyperlink[@r:id]", namespaces=NS):
                h.set(qn(R, "id"), map_source_rel(h.get(qn(R, "id"))))

        def scale_drawings(el: etree._Element) -> None:
            for extent in el.xpath(".//wp:extent[@cx and @cy]", namespaces=NS):
                try:
                    cx = int(extent.get("cx"))
                    cy = int(extent.get("cy"))
                except (TypeError, ValueError):
                    continue
                if cx <= BODY_MAX_IMAGE_CX:
                    continue
                ratio = BODY_MAX_IMAGE_CX / cx
                extent.set("cx", str(BODY_MAX_IMAGE_CX))
                extent.set("cy", str(int(cy * ratio)))
                drawing = extent.getparent()
                while drawing is not None and etree.QName(drawing).localname not in {"inline", "anchor"}:
                    drawing = drawing.getparent()
                if drawing is not None:
                    for aext in drawing.xpath(".//a:ext[@cx and @cy]", namespaces=NS):
                        aext.set("cx", str(BODY_MAX_IMAGE_CX))
                        aext.set("cy", str(int(cy * ratio)))

        def process_common(el: etree._Element) -> None:
            strip_comments(el)
            remap_relationship_refs(el)
            scale_drawings(el)
            remove_visible_ref_markers(el)
            clean_run_formatting(el)

        children = list(target_body)
        if wt(children[0]) == "Título do Tema":
            replace_full_text(children[0], TITLE)
        if wt(children[1]).lower().startswith("subtítulo"):
            replace_full_text(children[1], "")
        apply_project_details(target_doc.xpath("//w:p", namespaces=NS))
        apply_frontmatter(children, frontmatter)

        source_children = list(source_body)
        source_start = first_child_index(
            source_children,
            lambda ch: ch.tag == qn(W, "p") and wt(ch).startswith("Capítulo 1"),
        )
        acronyms = extract_acronyms(source_children)
        if not table_entries:
            table_entries = collect_caption_entries(source_children[source_start:], "Tabela ")
        if not figure_entries:
            figure_entries = collect_caption_entries(source_children[source_start:], "Figura ")

        abbr_idx = first_child_index(
            children,
            lambda ch: ch.tag == qn(W, "p") and wt(ch).startswith("Lista de Abreviaturas"),
        )
        apoios_idx = first_child_index(
            children,
            lambda ch: ch.tag == qn(W, "p") and wt(ch) == "APOIOS",
        )
        resumo_title_idx = first_child_index(
            children[apoios_idx + 1 :],
            lambda ch: ch.tag == qn(W, "p") and pstyle(ch) == "TtulodeCapaefolhaderosto-IPCA",
        ) + apoios_idx + 1
        agradecimentos_idx = first_child_index(
            children,
            lambda ch: ch.tag == qn(W, "p") and wt(ch) == "Agradecimentos",
        )
        toc_idx = first_child_index(
            children,
            lambda ch: ch.tag == qn(W, "p") and wt(ch) == "ÍNDICE",
        )
        body_template_idx = first_child_index(
            children,
            lambda ch: ch.tag == qn(W, "p") and pstyle(ch) == f"{STYLE_HEADING_PREFIX}1",
        )
        pre_body_break_start = body_template_idx
        while pre_body_break_start > toc_idx:
            previous = children[pre_body_break_start - 1]
            if previous.tag == qn(W, "p") and (has_section_break(previous) or not wt(previous)):
                pre_body_break_start -= 1
                continue
            break

        new_body_children: list[etree._Element] = []
        # Keep cover, title page, declaration, resumo and abstract. Omit optional
        # template-only sections with instructional placeholders.
        new_body_children.extend(deepcopy(ch) for ch in children[:apoios_idx])
        new_body_children.extend(deepcopy(ch) for ch in children[resumo_title_idx:agradecimentos_idx])
        new_body_children.append(deepcopy(children[abbr_idx]))
        for line in acronyms:
            new_body_children.append(make_text_para(line, STYLE_BODY))
        append_static_list(new_body_children, "Lista de Tabelas", table_entries)
        append_static_list(new_body_children, "Lista de Figuras", figure_entries)
        new_body_children.append(make_text_para(wt(children[toc_idx]), STYLE_PREAMBLE, page_break=True))
        if toc_entries:
            for item in toc_entries:
                new_body_children.append(
                    make_toc_para(item["title"], int(item.get("level", 1)), item.get("page", ""))
                )
        for ch in children[pre_body_break_start:body_template_idx]:
            new_body_children.append(deepcopy(ch))

        bibliography_mode = False
        inserted_body_heading = False
        for ch in source_children[source_start:]:
            if ch.tag == qn(W, "sectPr"):
                continue
            if ch.tag == qn(W, "p"):
                text = wt(ch)
                has_drawing = bool(ch.xpath(".//w:drawing", namespaces=NS))
                st = pstyle(ch)
                if not text and not has_drawing:
                    continue
                if st.startswith("Heading"):
                    tr = transform_heading(text, st)
                    if tr is None:
                        continue
                    style_id, new_text, ilvl, suppress, mode = tr
                    if mode == "bibliography":
                        bibliography_mode = True
                    elif mode in {"annex", "main"} and text.startswith("Capítulo"):
                        bibliography_mode = False
                    page_break = style_id in {f"{STYLE_HEADING_PREFIX}1", STYLE_PREAMBLE} and inserted_body_heading
                    if style_id in {f"{STYLE_HEADING_PREFIX}1", STYLE_PREAMBLE}:
                        inserted_body_heading = True
                    new_body_children.append(
                        make_text_para(
                            new_text,
                            style_id,
                            page_break=page_break,
                            suppress_numbering=suppress,
                            ilvl=ilvl,
                        )
                    )
                    continue
                p = deepcopy(ch)
                process_common(p)
                if bibliography_mode:
                    remove_anchor_markup(p)
                    if not wt(p):
                        continue
                    set_paragraph_style(p, STYLE_BIBLIOGRAPHY)
                elif text.startswith(("Figura ", "Tabela ", "Quadro ")):
                    set_paragraph_style(p, STYLE_CAPTION)
                elif has_drawing:
                    set_paragraph_style(p, "Normal", jc="center")
                elif text.startswith(("Fonte", "Adaptado", "Produção própria")):
                    set_paragraph_style(p, STYLE_NOTE)
                elif st == "Quote":
                    set_paragraph_style(p, STYLE_QUOTE)
                else:
                    set_paragraph_style(p, STYLE_BODY)
                new_body_children.append(p)
            elif ch.tag == qn(W, "tbl"):
                tbl = deepcopy(ch)
                process_common(tbl)
                tbl_pr = tbl.find("w:tblPr", NS)
                if tbl_pr is None:
                    tbl_pr = etree.Element(qn(W, "tblPr"))
                    tbl.insert(0, tbl_pr)
                for old in tbl_pr.xpath("./w:tblStyle", namespaces=NS):
                    tbl_pr.remove(old)
                tbl_style = etree.Element(qn(W, "tblStyle"))
                tbl_style.set(qn(W, "val"), STYLE_TABLE)
                tbl_pr.insert(0, tbl_style)
                tbl_w = tbl_pr.find("w:tblW", NS)
                if tbl_w is None:
                    tbl_w = etree.SubElement(tbl_pr, qn(W, "tblW"))
                tbl_w.set(qn(W, "w"), "5000")
                tbl_w.set(qn(W, "type"), "pct")
                rows = tbl.xpath("./w:tr", namespaces=NS)
                if rows:
                    tr_pr = rows[0].find("w:trPr", NS)
                    if tr_pr is None:
                        tr_pr = etree.Element(qn(W, "trPr"))
                        rows[0].insert(0, tr_pr)
                    if tr_pr.find("w:tblHeader", NS) is None:
                        etree.SubElement(tr_pr, qn(W, "tblHeader"))
                for p in tbl.xpath(".//w:p", namespaces=NS):
                    set_paragraph_style(p, STYLE_BODY)
                if rows:
                    for r in rows[0].xpath(".//w:r", namespaces=NS):
                        r_pr = r.find("w:rPr", NS)
                        if r_pr is None:
                            r_pr = etree.Element(qn(W, "rPr"))
                            r.insert(0, r_pr)
                        if r_pr.find("w:b", NS) is None:
                            etree.SubElement(r_pr, qn(W, "b"))
                new_body_children.append(tbl)

        # Use the first body-content section properties from the IPCA template:
        # decimal page numbering starts at 1 and body margins/header/footer are applied.
        body_sect = deepcopy(target_doc.xpath("//w:sectPr", namespaces=NS)[15])
        for ch in list(target_body):
            target_body.remove(ch)
        for ch in new_body_children:
            target_body.append(ch)
        target_body.append(body_sect)

        files["word/document.xml"] = serialize(target_doc)
        files["word/_rels/document.xml.rels"] = serialize(target_rels)
        files["word/settings.xml"] = add_update_fields(files["word/settings.xml"])
        if "docProps/core.xml" in files:
            files["docProps/core.xml"] = update_core_properties(files["docProps/core.xml"])
        if "word/footnotes.xml" in zs.namelist():
            footnotes = etree.fromstring(zs.read("word/footnotes.xml"))
            remove_visible_ref_markers(footnotes)
            clean_run_formatting(footnotes)
            files["word/footnotes.xml"] = serialize(footnotes)

    with ZipFile(output, "w", compression=ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--toc-json", type=Path)
    parser.add_argument("--tables-json", type=Path)
    parser.add_argument("--figures-json", type=Path)
    parser.add_argument("--frontmatter-source", type=Path)
    args = parser.parse_args()
    migrate(
        args.template,
        args.source,
        args.output,
        read_toc_entries(args.toc_json),
        read_entries(args.tables_json),
        read_entries(args.figures_json),
        extract_frontmatter(args.frontmatter_source),
    )


if __name__ == "__main__":
    main()
