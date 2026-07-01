#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import struct
import tempfile
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
PIC_NS = "http://schemas.openxmlformats.org/drawingml/2006/picture"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"

for prefix, uri in {
    "w": W_NS,
    "r": R_NS,
    "wp": WP_NS,
    "a": A_NS,
    "pic": PIC_NS,
}.items():
    ET.register_namespace(prefix, uri)

ET.register_namespace("", REL_NS)

EMU_PER_INCH = 914400


FIGURES = [
    ("Figura 2.1", "figuras/ch2_3d_printed_upper_limb_prostheses_a_figure2_p5.png"),
    ("Figura 2.2", "figuras/ch2_prosthesis_rejection_in_acquired_ma_figure1_p4.png"),
    ("Figura 2.3", "figuras/ch2_a_scoping_review_of_digital_fabrica_figure1_p2.png"),
    ("Figura 2.4", "figuras/ch2_implementation_of_3d_printing_techn_figure5_p8.png"),
    ("Figura 2.5", "figuras/ch2_2d_and_3d_anatomical_analyses_of_ha_figure1_p3.png"),
    ("Figura 2.6", "figuras/ch2_ai_driven_computer_aided_design_cad_figure1_p6.png"),
    ("Figura 2.7", "figuras/ch2_a_framework_for_configuring_partici_figure1_p4.png"),
    ("Figura 2.8", "figuras/ch2_a_scoping_review_of_digital_fabrica_figure10_p9.png"),
    ("Figura 3.1", "figuras/ch3_an_undergraduate_engineering_servic_figure1_p4.png"),
    ("Figura 4.1", "figuras/ch4_parametric_3d_modeling_of_a_customi_figure3_p2.png"),
    ("Figura 4.2", "figuras/ch4_customization_of_a_3d_printed_prost_figure8_p7.png"),
]


def qn(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def paragraph_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.findall(f".//{qn(W_NS, 't')}"))


def paragraph_has_drawing(p: ET.Element) -> bool:
    return p.find(f".//{qn(WP_NS, 'inline')}") is not None


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        header = fh.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a PNG file: {path}")
    return struct.unpack(">II", header[16:24])


def fit_size_emu(path: Path, max_width_in: float, max_height_in: float) -> tuple[int, int]:
    width_px, height_px = png_size(path)
    ratio = min(max_width_in / width_px, max_height_in / height_px)
    width_in = width_px * ratio
    height_in = height_px * ratio
    return round(width_in * EMU_PER_INCH), round(height_in * EMU_PER_INCH)


def next_rel_id(root: ET.Element) -> int:
    max_id = 0
    for rel in root.findall(qn(REL_NS, "Relationship")):
        rid = rel.attrib.get("Id", "")
        match = re.fullmatch(r"rId(\d+)", rid)
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1


def image_paragraph(rid: str, filename: str, cx: int, cy: int, docpr_id: int) -> ET.Element:
    p = ET.Element(qn(W_NS, "p"))
    p_pr = ET.SubElement(p, qn(W_NS, "pPr"))
    jc = ET.SubElement(p_pr, qn(W_NS, "jc"))
    jc.set(qn(W_NS, "val"), "center")
    r = ET.SubElement(p, qn(W_NS, "r"))
    drawing = ET.SubElement(r, qn(W_NS, "drawing"))
    inline = ET.SubElement(drawing, qn(WP_NS, "inline"))
    inline.set("distT", "0")
    inline.set("distB", "0")
    inline.set("distL", "0")
    inline.set("distR", "0")

    extent = ET.SubElement(inline, qn(WP_NS, "extent"))
    extent.set("cx", str(cx))
    extent.set("cy", str(cy))
    effect_extent = ET.SubElement(inline, qn(WP_NS, "effectExtent"))
    for attr in ("l", "t", "r", "b"):
        effect_extent.set(attr, "0")
    doc_pr = ET.SubElement(inline, qn(WP_NS, "docPr"))
    doc_pr.set("id", str(docpr_id))
    doc_pr.set("name", filename)
    c_nv_graphic = ET.SubElement(inline, qn(WP_NS, "cNvGraphicFramePr"))
    ET.SubElement(c_nv_graphic, qn(A_NS, "graphicFrameLocks")).set("noChangeAspect", "1")

    graphic = ET.SubElement(inline, qn(A_NS, "graphic"))
    graphic_data = ET.SubElement(graphic, qn(A_NS, "graphicData"))
    graphic_data.set("uri", PIC_NS)
    pic = ET.SubElement(graphic_data, qn(PIC_NS, "pic"))

    nv_pic_pr = ET.SubElement(pic, qn(PIC_NS, "nvPicPr"))
    c_nv_pr = ET.SubElement(nv_pic_pr, qn(PIC_NS, "cNvPr"))
    c_nv_pr.set("id", "0")
    c_nv_pr.set("name", filename)
    ET.SubElement(nv_pic_pr, qn(PIC_NS, "cNvPicPr"))

    blip_fill = ET.SubElement(pic, qn(PIC_NS, "blipFill"))
    blip = ET.SubElement(blip_fill, qn(A_NS, "blip"))
    blip.set(qn(R_NS, "embed"), rid)
    stretch = ET.SubElement(blip_fill, qn(A_NS, "stretch"))
    ET.SubElement(stretch, qn(A_NS, "fillRect"))

    sp_pr = ET.SubElement(pic, qn(PIC_NS, "spPr"))
    xfrm = ET.SubElement(sp_pr, qn(A_NS, "xfrm"))
    off = ET.SubElement(xfrm, qn(A_NS, "off"))
    off.set("x", "0")
    off.set("y", "0")
    ext = ET.SubElement(xfrm, qn(A_NS, "ext"))
    ext.set("cx", str(cx))
    ext.set("cy", str(cy))
    prst_geom = ET.SubElement(sp_pr, qn(A_NS, "prstGeom"))
    prst_geom.set("prst", "rect")
    ET.SubElement(prst_geom, qn(A_NS, "avLst"))

    return p


def insert_figures(input_docx: Path, output_docx: Path, repo_root: Path) -> None:
    with ZipFile(input_docx) as zin:
        document_root = ET.fromstring(zin.read("word/document.xml"))
        rels_root = ET.fromstring(zin.read("word/_rels/document.xml.rels"))
        existing_names = set(zin.namelist())

        body = document_root.find(f".//{qn(W_NS, 'body')}")
        if body is None:
            raise RuntimeError("Could not find document body")
        children = list(body)

        next_rid_number = next_rel_id(rels_root)
        docpr_id = 1
        inserted: list[tuple[str, Path, str]] = []

        for label, rel_path in FIGURES:
            image_path = repo_root / rel_path
            if not image_path.exists():
                raise FileNotFoundError(image_path)

            caption_index = None
            for idx, child in enumerate(children):
                if child.tag == qn(W_NS, "p") and paragraph_text(child).startswith(label):
                    caption_index = idx
                    break
            if caption_index is None:
                raise RuntimeError(f"Caption not found: {label}")
            if caption_index > 0 and children[caption_index - 1].tag == qn(W_NS, "p"):
                if paragraph_has_drawing(children[caption_index - 1]):
                    continue

            insert_index = caption_index
            if caption_index > 0 and children[caption_index - 1].tag == qn(W_NS, "p"):
                if paragraph_text(children[caption_index - 1]).strip() == "":
                    insert_index = caption_index - 1

            rid = f"rId{next_rid_number}"
            next_rid_number += 1
            target = f"media/{image_path.name}"
            media_name = f"word/{target}"
            if media_name in existing_names:
                target = f"media/figure_{docpr_id}_{image_path.name}"
                media_name = f"word/{target}"

            rel = ET.SubElement(rels_root, qn(REL_NS, "Relationship"))
            rel.set("Id", rid)
            rel.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
            rel.set("Target", target)

            cx, cy = fit_size_emu(image_path, max_width_in=5.9, max_height_in=4.4)
            figure_p = image_paragraph(rid, image_path.name, cx, cy, docpr_id)
            docpr_id += 1

            old_child = children[insert_index]
            body.remove(old_child)
            body.insert(insert_index, figure_p)
            children = list(body)
            inserted.append((media_name, image_path, label))

        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp_path = Path(tmp.name)

        skip = {"word/document.xml", "word/_rels/document.xml.rels"} | {media for media, _, _ in inserted}
        with ZipFile(tmp_path, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename in skip:
                    continue
                zout.writestr(item, zin.read(item.filename))
            zout.writestr("word/document.xml", ET.tostring(document_root, encoding="utf-8", xml_declaration=True))
            zout.writestr(
                "word/_rels/document.xml.rels",
                ET.tostring(rels_root, encoding="utf-8", xml_declaration=True),
            )
            for media_name, image_path, _ in inserted:
                zout.write(image_path, media_name)

    shutil.move(tmp_path, output_docx)
    print(f"Inserted {len(inserted)} figures into {output_docx}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Insert manuscript figures into a DOCX file.")
    parser.add_argument("input_docx", type=Path)
    parser.add_argument("output_docx", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    insert_figures(args.input_docx, args.output_docx, args.repo_root)


if __name__ == "__main__":
    main()
