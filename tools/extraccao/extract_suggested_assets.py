"""
Extract figures (as PNG images) and tables (as Markdown) referenced in
figures_tables_suggestions.md into ./figuras/ (images) and
material/tabelas-extraidas/ (tables extracted from the papers).

Usage:
    python3 tools/extraccao/extract_suggested_assets.py
"""

import os
import re
import sys
import fitz          # PyMuPDF
import pdfplumber
from difflib import SequenceMatcher
from pathlib import Path

# ── Config ───────────────────────────────────────────────────────────────────
ROOT      = Path(__file__).resolve().parents[2]
MATERIAL_DIR = ROOT / "material"
SUGG_FILE = MATERIAL_DIR / "figures_tables_suggestions.md"
FIG_DIR   = ROOT / "componentes" / "figuras"
TAB_DIR   = MATERIAL_DIR / "tabelas-extraidas"
MIN_IMG_W = 80    # pixels — skip tiny decorative images
MIN_IMG_H = 80
FUZZY_THR = 0.40  # minimum match ratio for title → filename

# ── Build PDF index ───────────────────────────────────────────────────────────
def build_pdf_index(base: Path) -> dict[str, Path]:
    """Return {lowercase_stem: path} for every PDF under base."""
    index = {}
    for p in base.rglob("*.pdf"):
        index[p.stem.lower()] = p
    return index

def normalise(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def best_match(title: str, index: dict[str, Path]) -> tuple[Path | None, float]:
    nt = normalise(title)
    best_path, best_score = None, 0.0
    for stem, path in index.items():
        ns = normalise(stem)
        score = SequenceMatcher(None, nt, ns).ratio()
        # bonus if all words of the title appear in the stem
        t_words = set(nt.split())
        s_words = set(ns.split())
        overlap  = len(t_words & s_words) / max(len(t_words), 1)
        combined = 0.6 * score + 0.4 * overlap
        if combined > best_score:
            best_score  = combined
            best_path   = path
    return best_path, best_score

# ── Parse suggestions file ────────────────────────────────────────────────────
# Each entry looks like:
#   - `Paper Title` — **Figure 3** (p. 6): Description text.
ENTRY_RE = re.compile(
    r"-\s+`([^`]+)`\s+[—–]\s+\*\*([A-Za-z]+[\w\s]*?)\s+(\S+)\*\*\s+\(p[p]?\.\s*(\d+(?:[-–]\d+)?)\).*"
)

def parse_suggestions(path: Path):
    """Return list of (chapter_label, paper_title, asset_type, asset_num, page_str, description)."""
    chapter_label = "ch0"
    results = []
    with open(path) as f:
        for line in f:
            ch = re.match(r"^## Chapter (\d+)", line)
            if ch:
                chapter_label = f"ch{ch.group(1)}"
                continue
            m = ENTRY_RE.match(line.strip())
            if not m:
                continue
            title, atype, anum, page_str = m.group(1), m.group(2), m.group(3), m.group(4)
            atype_clean = atype.strip().lower()   # "figure" or "table"
            results.append((chapter_label, title, atype_clean, anum, page_str))
    return results

# ── Safe filename helper ──────────────────────────────────────────────────────
def safe(s: str, maxlen=40) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", s.lower())
    return s[:maxlen].strip("_")

# ── Figure extraction ─────────────────────────────────────────────────────────
RENDER_DPI = 150

def _find_figure_crop(page, fig_num_str: str) -> "fitz.Rect":
    """
    Return a crop rect that isolates Figure fig_num_str on this page.
    Falls back to the full page rect if the figure cannot be located.
    """
    page_rect = page.rect
    page_h    = page_rect.height
    page_w    = page_rect.width

    # ── 1. Find caption ───────────────────────────────────────────────────────
    # Prefer "Figure N." (with period) — almost never appears in in-text refs.
    # Fall back to "Figure N" and take the LAST hit (captions are at the bottom).
    caption_rect = None
    for pat in [
        f"Figure {fig_num_str}.", f"FIGURE {fig_num_str}.",
        f"Fig. {fig_num_str}.", f"FIG. {fig_num_str}.",
    ]:
        hits = page.search_for(pat)
        if hits:
            caption_rect = hits[-1]
            break
    if caption_rect is None:
        for pat in [
            f"Figure {fig_num_str}", f"Fig. {fig_num_str}", f"Fig {fig_num_str}",
            f"FIGURE {fig_num_str}", f"FIG. {fig_num_str}",
        ]:
            hits = page.search_for(pat)
            if hits:
                caption_rect = hits[-1]
                break
    if caption_rect is None:
        return page_rect

    cap_top = caption_rect.y0
    cap_bot = caption_rect.y1

    blocks      = page.get_text("blocks")
    text_blocks = [b for b in blocks if b[6] == 0]
    body_min_w  = page_w * 0.30

    def is_body_text(b):
        return (b[2] - b[0]) >= body_min_w

    # ── 2. Top boundary ───────────────────────────────────────────────────────
    # Only consider body-text blocks that end clearly before the caption
    # (≥ 30 pt gap). This excludes figure labels that sit just above the caption.
    body_above = [b for b in text_blocks
                  if b[3] < cap_top - 30 and is_body_text(b)]
    top_y = (max(b[3] for b in body_above) + 5) if body_above \
            else max(page_rect.y0, cap_top - page_h * 0.65)

    # ── 3. Bottom boundary ────────────────────────────────────────────────────
    # Find the full caption text block (the search hit is just the first line).
    # Require the candidate block to start on the same side of the midpoint as
    # the caption hit — this prevents wide blocks in the opposite column from
    # being picked up in two-column layouts.
    _cap_left = caption_rect.x0 < page_w / 2
    cap_block = next(
        (b for b in text_blocks if b[1] <= cap_top + 2 and b[3] >= cap_top - 2
         and is_body_text(b)
         and (_cap_left == (b[0] < page_w / 2))),
        None,
    )
    # Stop right after the caption block — don't search for next body text.
    # This prevents consecutive figures from merging and eliminates trailing
    # whitespace when the figure is at the bottom of the page.
    bot_y = min(page_rect.y1, (cap_block[3] if cap_block else cap_bot) + 25)

    # ── 4. Two-column detection ───────────────────────────────────────────────
    # The caption is ALWAYS in the same column as the figure, so its x-position
    # is the primary indicator.  We only narrow the crop when the caption is
    # clearly off-centre AND there is opposing-side text confirming two columns.
    px_mid     = page_w / 2
    min_blk_w  = page_w * 0.12
    cap_x_mid  = (caption_rect.x0 + caption_rect.x1) / 2
    cap_x_frac = cap_x_mid / page_w   # 0..1

    if cap_x_frac < 0.44:
        # Caption is in the LEFT column — check for body text in the right column
        # Only blocks that START before the caption (inside the figure region) count;
        # blocks below the caption belong to the next paragraph, not the right column.
        opposite = [b for b in text_blocks
                    if b[0] > page_w * 0.50 and (b[2] - b[0]) > min_blk_w
                    and b[1] < cap_top]
        if len(opposite) >= 2:
            right_start = min(b[0] for b in opposite)
            x0, x1 = page_rect.x0, right_start - 5
        else:
            x0, x1 = page_rect.x0, page_rect.x1
    elif cap_x_frac > 0.52:
        # Caption is in the RIGHT column — check for body text in the left column
        opposite = [b for b in text_blocks
                    if b[2] < page_w * 0.50 and (b[2] - b[0]) > min_blk_w
                    and b[1] < cap_top]
        if len(opposite) >= 2:
            left_end = max(b[2] for b in opposite)
            x0, x1 = left_end + 5, page_rect.x1
        else:
            x0, x1 = page_rect.x0, page_rect.x1
    else:
        x0, x1 = page_rect.x0, page_rect.x1

    crop = fitz.Rect(x0, max(page_rect.y0, top_y - 5), x1, bot_y)
    return crop & page_rect


def extract_figures(pdf_path: Path, page_num: int, out_dir: Path, base_name: str,
                    fig_num_str: str = ""):
    """Render the figure region on page_num (0-indexed) as a high-res PNG."""
    saved = []
    try:
        doc = fitz.open(pdf_path)
        if page_num >= len(doc):
            return saved
        page = doc[page_num]

        crop = _find_figure_crop(page, fig_num_str) if fig_num_str else page.rect

        mat = fitz.Matrix(RENDER_DPI / 72, RENDER_DPI / 72)
        pix = page.get_pixmap(matrix=mat, clip=crop, alpha=False)
        fname = out_dir / f"{base_name}.png"
        pix.save(str(fname))
        saved.append(fname)
        doc.close()
    except Exception as e:
        print(f"    [figure error] {e}")
    return saved

# ── Table extraction ──────────────────────────────────────────────────────────
def table_to_markdown(table) -> str:
    """Convert a pdfplumber table (list of lists) to a Markdown table string."""
    if not table:
        return ""
    rows = [[str(cell or "").replace("\n", " ").strip() for cell in row] for row in table]
    # Drop fully-empty rows
    rows = [r for r in rows if any(c for c in r)]
    if not rows:
        return ""
    col_widths = [max(len(r[i]) for r in rows if i < len(r)) for i in range(len(rows[0]))]
    def fmt_row(r):
        cells = [r[i] if i < len(r) else "" for i in range(len(rows[0]))]
        return "| " + " | ".join(c.ljust(col_widths[i]) for i, c in enumerate(cells)) + " |"
    sep = "| " + " | ".join("-" * w for w in col_widths) + " |"
    lines = [fmt_row(rows[0]), sep] + [fmt_row(r) for r in rows[1:]]
    return "\n".join(lines)

def extract_tables(pdf_path: Path, page_num: int, out_dir: Path, base_name: str,
                   paper_title: str, asset_num: str, chapter: str):
    """Extract all tables from page_num (0-indexed) and save as Markdown."""
    saved = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if page_num >= len(pdf.pages):
                return saved
            page = pdf.pages[page_num]
            tables = page.extract_tables()
            if not tables:
                # Fall back to raw text crop for the page
                text = page.extract_text() or ""
                if text.strip():
                    fname = out_dir / f"{base_name}_rawtext.md"
                    content = (
                        f"# {paper_title} — {chapter.upper()} {asset_num}\n\n"
                        f"> Table could not be parsed automatically. Raw page text:\n\n"
                        f"```\n{text}\n```\n"
                    )
                    fname.write_text(content, encoding="utf-8")
                    saved.append(fname)
                return saved
            for i, table in enumerate(tables):
                md = table_to_markdown(table)
                if not md:
                    continue
                fname = out_dir / f"{base_name}_{i}.md"
                content = (
                    f"# {paper_title}\n\n"
                    f"**Chapter:** {chapter.upper()}  |  **{asset_num}**  |  p. {page_num + 1}\n\n"
                    f"{md}\n"
                )
                fname.write_text(content, encoding="utf-8")
                saved.append(fname)
    except Exception as e:
        print(f"    [table error] {e}")
    return saved

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    FIG_DIR.mkdir(exist_ok=True)
    TAB_DIR.mkdir(exist_ok=True)

    print("Building PDF index…")
    index = build_pdf_index(MATERIAL_DIR)
    print(f"  {len(index)} PDFs indexed.\n")

    print("Parsing suggestions…")
    entries = parse_suggestions(SUGG_FILE)
    print(f"  {len(entries)} entries found.\n")

    no_match   = []
    low_match  = []
    figs_saved = 0
    tabs_saved = 0

    seen_combos: set[str] = set()   # avoid duplicating same page twice for same paper

    for chapter, title, atype, anum, page_str in entries:
        # deduplicate identical extractions
        combo_key = f"{chapter}|{title}|{atype}|{anum}|{page_str}"
        if combo_key in seen_combos:
            continue
        seen_combos.add(combo_key)

        # parse page (use first number if range)
        page_1indexed = int(re.split(r"[-–]", page_str)[0])
        page_0indexed = page_1indexed - 1

        # find PDF
        pdf_path, score = best_match(title, index)
        if pdf_path is None or score < FUZZY_THR:
            low_match.append((score, title, atype, anum))
            continue

        # build output base name
        base_name = f"{chapter}_{safe(title, 35)}_{atype}{safe(anum, 6)}_p{page_1indexed}"

        print(f"[{chapter}] {atype.upper()} {anum} — {title[:55]}")
        print(f"       → {pdf_path.name}  (score={score:.2f}, p.{page_1indexed})")

        if atype == "figure":
            out_dir = FIG_DIR
            saved   = extract_figures(pdf_path, page_0indexed, out_dir, base_name, fig_num_str=anum)
            if saved:
                figs_saved += len(saved)
                print(f"       ✓ {len(saved)} image(s) saved")
            else:
                print("       ✗ no images found on that page")
        elif atype == "table":
            out_dir = TAB_DIR
            saved   = extract_tables(pdf_path, page_0indexed, out_dir, base_name,
                                     title, f"{atype.title()} {anum}", chapter)
            if saved:
                tabs_saved += len(saved)
                print(f"       ✓ {len(saved)} table file(s) saved")
            else:
                print("       ✗ no tables found on that page")

    print(f"\n{'='*60}")
    print(f"  Figures saved : {figs_saved}")
    print(f"  Tables  saved : {tabs_saved}")
    if low_match:
        print(f"\n  Could not match {len(low_match)} entries (score < {FUZZY_THR}):")
        for score, title, atype, anum in sorted(low_match):
            print(f"    [{score:.2f}] {atype} {anum} — {title[:70]}")

if __name__ == "__main__":
    main()
