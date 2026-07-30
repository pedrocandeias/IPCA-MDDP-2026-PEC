#!/usr/bin/env python3
"""Gera as fontes SVG das Figuras 2.2, 2.3, 2.6, 2.7, 3.1, 6.1 e C.1."""

from __future__ import annotations

import base64
import html
from io import BytesIO
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
FIGURES = ROOT / "componentes" / "figuras"

INK = "#1f2933"
LINE = "#59636d"
TEAL = "#ddefea"
PEACH = "#f8e7dd"
LAVENDER = "#e8e1f2"
BLUE = "#dce9f6"
SAND = "#f3ebdd"
GREEN = "#edf1df"
WHITE = "#ffffff"
RED = "#b5453c"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def header(width: int, height: int, title: str, description: str, *,
           compact_arrows: bool = False) -> str:
    marker_width = 14 if compact_arrows else 12
    marker_height = 14 if compact_arrows else 12
    marker_ref = 12.5 if compact_arrows else 10
    marker_middle = marker_height / 2
    marker_units = "userSpaceOnUse" if compact_arrows else "strokeWidth"
    arrow_stroke = 3 if compact_arrows else 4
    dashed_stroke = 2.5 if compact_arrows else 3.5
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(description)}</desc>
  <defs>
    <marker id="arrow" markerWidth="{marker_width}" markerHeight="{marker_height}" refX="{marker_ref}" refY="{marker_middle}" orient="auto-start-reverse" markerUnits="{marker_units}">
      <path d="M0,0 L{marker_width},{marker_middle} L0,{marker_height} z" fill="{LINE}"/>
    </marker>
    <marker id="arrow-red" markerWidth="{marker_width}" markerHeight="{marker_height}" refX="{marker_ref}" refY="{marker_middle}" orient="auto-start-reverse" markerUnits="{marker_units}">
      <path d="M0,0 L{marker_width},{marker_middle} L0,{marker_height} z" fill="{RED}"/>
    </marker>
    <style>
      text {{ font-family: Arial, Helvetica, sans-serif; fill: {INK}; }}
      .outline {{ stroke: {LINE}; stroke-width: 3; }}
      .arrow {{ fill: none; stroke: {LINE}; stroke-width: {arrow_stroke}; marker-end: url(#arrow); }}
      .arrow-both {{ fill: none; stroke: {LINE}; stroke-width: {arrow_stroke}; marker-start: url(#arrow); marker-end: url(#arrow); }}
      .dashed {{ fill: none; stroke: {LINE}; stroke-width: {dashed_stroke}; stroke-dasharray: 12 9; marker-end: url(#arrow); }}
      .red-dashed {{ fill: none; stroke: {RED}; stroke-width: {dashed_stroke}; stroke-dasharray: 12 9; marker-end: url(#arrow-red); }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="{WHITE}"/>
'''


def footer() -> str:
    return "</svg>\n"


def rect(x: float, y: float, width: float, height: float, fill: str, *, rx: int = 18,
         stroke: str = LINE, stroke_width: float = 3, extra: str = "") -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" {extra}/>'
    )


def multiline(x: float, center_y: float, lines: list[str], *, size: int = 28,
              line_height: int | None = None, weight: int = 400, anchor: str = "middle",
              fill: str = INK) -> str:
    if line_height is None:
        line_height = round(size * 1.2)
    start = center_y - ((len(lines) - 1) * line_height) / 2 + size * 0.34
    spans = "".join(
        f'<tspan x="{x}" y="{start + index * line_height}">{esc(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    return (
        f'<text text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}">{spans}</text>'
    )


def label(x: float, y: float, value: str, *, size: int = 28, weight: int = 700,
          anchor: str = "middle", fill: str = INK) -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}">{esc(value)}</text>'
    )


def path(d: str, *, cls: str = "arrow", stroke: str | None = None) -> str:
    override = f' stroke="{stroke}"' if stroke else ""
    return f'<path d="{d}" class="{cls}"{override}/>'


def write(pathname: Path, content: str) -> None:
    pathname.write_text(content, encoding="utf-8")
    print(f"Gerado: {pathname.relative_to(ROOT)}")


def figure_2_2() -> None:
    width, height = 1600, 1080
    parts = [header(
        width, height,
        "Utilização e rejeição de próteses do membro superior adquiridas",
        "Árvore com 224 inquéritos respondidos, separando ausência de utilização, uso primário, rejeição e uso continuado.",
        compact_arrows=True,
    )]

    boxes = [
        (630, 40, BLUE, ["Inquéritos respondidos", "n = 224"]),
        (230, 350, PEACH, ["Nunca utilizou uma prótese", "n = 15", "6,7%"]),
        (1030, 350, TEAL, ["Uso primário de prótese", "n = 209", "93,3%"]),
        (20, 750, LAVENDER, ["Rejeição primária", "n = 10", "4,5% de 224"]),
        (420, 750, SAND, ["A aguardar pela primeira", "prótese na data", "do inquérito", "n = 5", "2,2% de 224"]),
        (820, 750, LAVENDER, ["Prótese secundária", "rejeitada", "n = 28", "13,4% de 209", "12,5% de 224"]),
        (1220, 750, GREEN, ["Uso continuado", "de prótese", "n = 181", "86,6% de 209", "80,8% de 224"]),
    ]
    for x, y, fill, lines in boxes:
        parts.append(rect(x, y, 360, 230, fill))
        text_size = 24 if y == 750 else 27
        parts.append(multiline(x + 180, y + 115, lines, size=text_size,
                               line_height=29 if y == 750 else 34,
                               weight=700 if len(lines) <= 2 else 600))

    parts.extend([
        path("M810 270 V310 H410 V350"),
        path("M810 270 V310 H1210 V350"),
        path("M410 580 V680 H200 V750"),
        path("M410 580 V680 H600 V750"),
        path("M1210 580 V680 H1000 V750"),
        path("M1210 580 V680 H1400 V750"),
    ])
    parts.append(footer())
    write(FIGURES / "figura_2_2_utilizacao_rejeicao_proteses_estilizada.svg", "\n".join(parts))


def stage(parts: list[str], x: float, y: float, width: float, height: float,
          fill: str, lines: list[str], *, size: int = 24) -> None:
    parts.append(rect(x, y, width, height, fill, rx=14))
    parts.append(multiline(x + width / 2, y + height / 2, lines, size=size,
                           line_height=round(size * 1.15), weight=600))


def band(parts: list[str], x: float, y: float, width: float, value: str, fill: str) -> None:
    parts.append(rect(x, y, width, 48, fill, rx=10, stroke_width=2.5))
    parts.append(multiline(x + width / 2, y + 24, [value], size=22, weight=600))


def figure_2_3() -> None:
    width, height = 1600, 1085
    parts = [header(
        width, height,
        "Comparação entre fluxos tradicional, CAD/CAM e de fabrico aditivo",
        "Três sequências de produção distinguem etapas digitais, automatizadas e de trabalho manual.",
        compact_arrows=True,
    )]

    parts.append(label(40, 55, "Fluxo tradicional", size=32, anchor="start"))
    x6 = [40, 295, 550, 805, 1060, 1315]
    traditional = [
        ["Molde", "negativo"], ["Molde", "positivo"], ["Retificação", "manual do molde"],
        ["Fabrico manual", "por laminagem"], ["Pós-processamento,", "montagem", "e alinhamento"],
        ["Ajustes", "finais"],
    ]
    for index, (x, lines) in enumerate(zip(x6, traditional)):
        stage(parts, x, 80, 225, 125, PEACH if index < 4 else SAND, lines,
              size=20 if index == 4 else 22)
        if index < 5:
            parts.append(path(f"M{x + 225} 142 H{x6[index + 1]}"))
    band(parts, 40, 225, 1500, "Trabalho manual", PEACH)

    parts.append(label(40, 350, "Fluxo CAD/CAM", size=32, anchor="start"))
    cadcam = [
        ["Digitalização"], ["Retificação", "virtual"], ["Molde CNC"],
        ["Fabrico", "manual"], ["Pós-processamento,", "montagem", "e alinhamento"],
        ["Ajustes", "finais"],
    ]
    for index, (x, lines) in enumerate(zip(x6, cadcam)):
        stage(parts, x, 375, 225, 125, TEAL if index < 3 else PEACH, lines,
              size=20 if index == 4 else 22)
        if index < 5:
            parts.append(path(f"M{x + 225} 437 H{x6[index + 1]}"))
    band(parts, 40, 520, 735, "Ambiente digital", TEAL)
    band(parts, 805, 520, 735, "Trabalho manual", PEACH)

    parts.append(label(40, 645, "Fluxo de fabrico aditivo", size=32, anchor="start"))
    x5 = [40, 350, 660, 970, 1280]
    additive = [
        (TEAL, ["Digitalização"]), (TEAL, ["Retificação", "virtual"]),
        (LAVENDER, ["Produção automatizada", "por fabrico aditivo"]),
        (PEACH, ["Pós-processamento,", "montagem", "e alinhamento"]),
        (SAND, ["Ajustes", "finais"]),
    ]
    for index, (x, (fill, lines)) in enumerate(zip(x5, additive)):
        stage(parts, x, 670, 280, 125, fill, lines, size=20 if index == 3 else 22)
        if index < 4:
            parts.append(path(f"M{x + 280} 732 H{x5[index + 1]}"))
    band(parts, 40, 815, 900, "Ambiente digital e produção automatizada", TEAL)
    band(parts, 970, 815, 590, "Trabalho manual", PEACH)

    parts.append(footer())
    write(FIGURES / "figura_2_3_fluxo_digital_proteses_estilizada.svg", "\n".join(parts))


def icon_data(image: Image.Image, crop: tuple[int, int, int, int]) -> tuple[str, int, int]:
    icon = image.crop(crop).convert("RGBA")
    gray = icon.convert("L")
    alpha = gray.point(lambda value: 255 if value < 175 else 0)
    bounds = alpha.getbbox()
    if not bounds:
        raise RuntimeError(f"Ícone não detectado no recorte {crop}")
    icon = icon.crop(bounds)
    alpha = alpha.crop(bounds)
    recoloured = Image.new("RGBA", icon.size, (*tuple(int(INK[index:index + 2], 16) for index in (1, 3, 5)), 0))
    recoloured.putalpha(alpha)
    buffer = BytesIO()
    recoloured.save(buffer, format="PNG", optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("ascii"), recoloured.width, recoloured.height


def embedded_icon(parts: list[str], data: tuple[str, int, int], x: float, center_y: float,
                  max_width: float = 86, max_height: float = 86) -> None:
    encoded, width, height = data
    scale = min(max_width / width, max_height / height)
    shown_width, shown_height = width * scale, height * scale
    parts.append(
        f'<image x="{x}" y="{center_y - shown_height / 2}" width="{shown_width}" '
        f'height="{shown_height}" href="data:image/png;base64,{encoded}"/>'
    )


def panel(parts: list[str], x: float, width: float, heading: str, header_fill: str,
          body_fill: str) -> None:
    parts.append(rect(x, 40, width, 870, body_fill, rx=20))
    parts.append(f'<path d="M{x + 20} 40 H{x + width - 20} Q{x + width} 40 {x + width} 60 V145 H{x} V60 Q{x} 40 {x + 20} 40 Z" fill="{header_fill}"/>')
    parts.append(multiline(x + width / 2, 92, [heading], size=34, weight=700))


def figure_2_6() -> None:
    width, height = 2200, 950
    original = Image.open(FIGURES / "ch2_ai_driven_computer_aided_design_cad_figure1_p6_pt.png")
    crops = {
        "requirements": (74, 105, 158, 206),
        "constraints": (73, 250, 204, 352),
        "materials": (74, 382, 161, 480),
        "optimisation": (742, 101, 826, 188),
        "features": (478, 250, 565, 350),
        "hybrid": (476, 380, 568, 480),
        "models": (965, 114, 1043, 213),
        "parameters": (950, 246, 1039, 356),
    }
    icons = {name: icon_data(original, crop) for name, crop in crops.items()}
    parts = [header(
        width, height,
        "Fluxo de CAD apoiado por inteligência artificial",
        "Três painéis de entrada, processamento por IA e saída; os oito ícones da figura adaptada original são preservados.",
    )]
    panel(parts, 50, 470, "1 · Entrada", TEAL, "#f2f8f6")
    panel(parts, 620, 800, "2 · Processamento por IA", LAVENDER, "#f7f4fa")
    panel(parts, 1530, 620, "3 · Saída", PEACH, "#fcf6f1")

    for y in (170, 410, 650):
        parts.append(f'<line x1="80" y1="{y + 220}" x2="490" y2="{y + 220}" stroke="{LINE}" stroke-width="2" opacity="0.35"/>' if y < 650 else "")

    left_rows = [
        (255, "requirements", ["Requisitos", "de projeto"]),
        (510, "constraints", ["Restrições"]),
        (765, "materials", ["Propriedades", "do material"]),
    ]
    for y, key, lines in left_rows:
        embedded_icon(parts, icons[key], 95, y, 100, 100)
        parts.append(multiline(300, y, lines, size=30, line_height=36, weight=700))

    processing_rows = [
        (260, "optimisation", ["Otimização por redes neuronais"], ["Multiobjetivo: peso, resistência e custo"]),
        (510, "features", ["Extração de características (CNN)"], []),
        (755, "hybrid", ["Arquitetura híbrida CNN–LSTM"], []),
    ]
    for y, key, heading_lines, detail in processing_rows:
        embedded_icon(parts, icons[key], 675, y, 92, 92)
        parts.append(multiline(1040, y - (18 if detail else 0), heading_lines, size=29,
                               line_height=35, weight=700))
        if detail:
            parts.append(multiline(1040, y + 45, detail, size=22, weight=400))
        if y < 755:
            parts.append(f'<line x1="660" y1="{y + 125}" x2="1380" y2="{y + 125}" stroke="{LINE}" stroke-width="2" opacity="0.35"/>')

    output_rows = [
        (260, "models", ["33 modelos CAD", "otimizados"]),
        (510, "parameters", ["Parâmetros de projeto", "otimizados"]),
        (755, None, ["Ciclos de projeto", "reduzidos"]),
    ]
    for y, key, lines in output_rows:
        if key:
            embedded_icon(parts, icons[key], 1580, y, 92, 92)
        else:
            parts.append(multiline(1625, y, ["↘"], size=70, weight=400, fill=LINE))
        parts.append(multiline(1885, y, lines, size=29, line_height=35, weight=700))
        if y < 755:
            parts.append(f'<line x1="1570" y1="{y + 125}" x2="2110" y2="{y + 125}" stroke="{LINE}" stroke-width="2" opacity="0.35"/>')

    parts.extend([
        path("M520 475 H620"),
        path("M1420 440 H1530"),
        path("M1530 555 H1420", cls="dashed"),
        multiline(1475, 620, ["refinamento", "iterativo"], size=21, line_height=25, weight=600),
    ])
    parts.append(footer())
    write(FIGURES / "figura_2_6_fluxo_cad_ia_estilizado.svg", "\n".join(parts))


def figure_2_7() -> None:
    width, height = 1800, 928
    parts = [header(
        width, height,
        "Processo para configurar participação em ecossistemas de inovação e cocriação",
        "Processo iterativo com cinco fases principais, prototipagem, teste em ambiente real e envolvimento continuado dos utilizadores.",
        compact_arrows=True,
    )]
    stages = [
        (40, TEAL, ["Diálogo e", "construção", "de equipa"]),
        (400, BLUE, ["Exploração", "do desafio"]),
        (760, LAVENDER, ["Criação", "de ideias"]),
        (1120, PEACH, ["Teste com", "utilizadores"]),
        (1480, GREEN, ["Implementação"]),
    ]
    for x, fill, lines in stages:
        stage(parts, x, 320, 280, 145, fill, lines, size=26 if x == 40 else 28)
    for left, right in zip(stages, stages[1:]):
        parts.append(path(f"M{left[0] + 280} 378 H{right[0]}"))
        parts.append(path(f"M{right[0]} 410 H{left[0] + 280}"))

    stage(parts, 895, 65, 280, 130, BLUE, ["Prototipagem"], size=29)
    parts.extend([
        path("M900 320 V245 H965 V195"),
        path("M1105 195 V245 H1260 V320"),
        path("M1260 465 V535 H900 V465"),
        path("M1300 465 V590 H860 V465"),
    ])

    parts.append(rect(1240, 45, 420, 185, SAND, rx=24))
    parts.append(multiline(1450, 126, ["Teste em ambiente real", "ou em condições semelhantes"],
                           size=27, line_height=34, weight=600))
    parts.append(path("M1450 230 V275 H1260 V320", cls="dashed"))

    parts.append(f'<path d="M80 670 H1660 L1720 720 L1660 770 H80 Z" fill="{SAND}" stroke="{LINE}" stroke-width="3"/>')
    parts.append(multiline(870, 720, ["Envolver utilizadores desde as fases iniciais até às fases finais do processo"],
                           size=27, weight=600))
    parts.append(f'<path d="M80 790 H1660 L1720 840 L1660 890 H80 Z" fill="{PEACH}" stroke="{LINE}" stroke-width="3"/>')
    parts.append(multiline(870, 840, ["Processo de design de longa duração: vários meses ou anos"],
                           size=27, weight=600))
    parts.append(footer())
    write(FIGURES / "figura_2_7_participacao_cocriacao_estilizada.svg", "\n".join(parts))


def figure_3_1() -> None:
    width, height = 1800, 647
    parts = [header(
        width, height,
        "Processo interdisciplinar de desenvolvimento de uma prótese",
        "Seis fases ligam exploração a entrega, alimentadas por referências técnicas e pelo perfil do utilizador, com ciclos de correção, ajuste e novo teste.",
        compact_arrows=True,
    )]
    parts.append(rect(20, 50, 250, 210, TEAL, rx=16))
    parts.append(multiline(145, 90, ["Referências técnicas"], size=21, weight=700))
    parts.append(multiline(145, 165, ["Designs semelhantes", "Tecnologias disponíveis", "Dados do", "membro residual"],
                           size=17, line_height=24, weight=400))
    parts.append(rect(20, 385, 250, 210, PEACH, rx=16))
    parts.append(multiline(145, 425, ["Perfil do utilizador"], size=21, weight=700))
    parts.append(multiline(145, 500, ["Capacidades", "Necessidades funcionais", "Preferências"],
                           size=17, line_height=25, weight=400))

    stage_data = [
        (280, TEAL, ["Exploração"]), (530, BLUE, ["Enquadramento"]),
        (780, LAVENDER, ["Conceito"]), (1030, PEACH, ["Prototipagem"]),
        (1280, SAND, ["Teste"]), (1530, GREEN, ["Entrega"]),
    ]
    for x, fill, lines in stage_data:
        stage(parts, x, 255, 220, 110, fill, lines, size=24)
    for left, right in zip(stage_data, stage_data[1:]):
        parts.append(path(f"M{left[0] + 220} 310 H{right[0]}"))
    parts.extend([
        path("M270 155 H275 V290 H280"),
        path("M270 490 H275 V330 H280"),
        path("M1640 255 V55 H890 V255", cls="dashed"),
    ])

    notes = [
        (780, LAVENDER, ["Correções", "de design"]),
        (1030, PEACH, ["Ajustes"]),
        (1280, SAND, ["Novo teste"]),
    ]
    for x, fill, lines in notes:
        stage(parts, x, 445, 220, 100, fill, lines, size=21)
        parts.append(path(f"M{x + 110} 445 V365", cls="dashed"))
    parts.append(footer())
    write(FIGURES / "figura_3_1_processo_interdisciplinar_estilizada.svg", "\n".join(parts))


def figure_6_1() -> None:
    width, height = 2400, 844
    parts = [header(
        width, height,
        "Relação entre desafios de compreensão e princípios de IA responsável",
        "Nove desafios de inteligência artificial explicável relacionam-se com seis princípios e convergem para IA responsável.",
    )]
    parts.append(rect(30, 40, 1060, 764, "#f7faf9", rx=24))
    parts.append(label(560, 95, "Desafios associados à XAI", size=34))
    challenges = [
        ["Interpretabilidade", "versus desempenho"],
        ["Conceitos e", "métricas de XAI"],
        ["Explicabilidade em", "aprendizagem profunda"],
        ["XAI e segurança:", "aprendizagem adversarial"],
        ["Justificação, explicação", "e estudos críticos de dados"],
        ["Ciência de dados", "orientada por teoria"],
        ["Implementação", "e orientações"],
        ["XAI e confiança", "nos resultados"],
        ["XAI e fusão", "de dados"],
    ]
    challenge_fills = [TEAL, BLUE, LAVENDER, BLUE, SAND, TEAL, PEACH, GREEN, LAVENDER]
    for index, (lines, fill) in enumerate(zip(challenges, challenge_fills)):
        row, column = divmod(index, 3)
        x, y = 70 + column * 335, 135 + row * 180
        parts.append(rect(x, y, 300, 140, fill, rx=16, stroke_width=2.5))
        parts.append(multiline(x + 150, y + 70, lines, size=22, line_height=27, weight=600))
    parts.append(rect(405, 695, 310, 75, TEAL, rx=37))
    parts.append(multiline(560, 732, ["XAI"], size=34, weight=700))

    parts.append(rect(1220, 90, 790, 664, "#faf9fc", rx=24))
    parts.append(label(1615, 145, "Princípios de IA responsável", size=34))
    principles = [
        (1260, 210, TEAL, ["Equidade"]),
        (1515, 210, BLUE, ["Privacidade"]),
        (1770, 210, LAVENDER, ["Responsabilização"]),
        (1260, 435, PEACH, ["Ética"]),
        (1515, 435, SAND, ["Transparência"]),
        (1770, 435, GREEN, ["Segurança", "e proteção"]),
    ]
    for x, y, fill, lines in principles:
        parts.append(rect(x, y, 215, 165, fill, rx=16))
        principle_size = 20 if lines == ["Responsabilização"] else 25
        parts.append(multiline(x + 107.5, y + 82.5, lines, size=principle_size,
                               line_height=31, weight=600))

    parts.append(rect(2130, 270, 240, 300, TEAL, rx=38, stroke_width=4))
    parts.append(multiline(2250, 420, ["IA", "responsável"], size=34, line_height=42, weight=700))
    parts.extend([
        path("M1090 422 H1220"),
        path("M2010 422 H2130"),
    ])
    parts.append(footer())
    write(FIGURES / "figura_6_1_ia_responsavel_estilizada.svg", "\n".join(parts))


def figure_c_1() -> None:
    width, height = 1600, 920
    parts = [header(
        width, height,
        "Fluxo de adaptação paramétrica dos modelos protésicos",
        "Entradas e mapa comum alimentam regras de quatro modelos; seguem-se verificações, geometria intermédia e decisão de projeto.",
        compact_arrows=True,
    )]
    parts.append(label(800, 55, "Da medida à variante geométrica: regras específicas de cada modelo", size=34))

    def content_box(x: int, y: int, w: int, h: int, fill: str, heading: str,
                    lines: list[str], small_last: bool = False) -> None:
        parts.append(rect(x, y, w, h, fill, rx=18))
        parts.append(multiline(x + w / 2, y + 42, [heading], size=25, weight=700))
        start = y + 88
        for index, line in enumerate(lines):
            size = 18 if small_last and index == len(lines) - 1 else 19
            parts.append(label(x + 30, start + index * 34, line, size=size, weight=400, anchor="start"))

    content_box(45, 118, 260, 195, TEAL, "Entradas", [
        "• Medida individual", "• Referência populacional", "• Ajuste manual", "Unidade canónica: mm",
    ], True)
    content_box(382, 118, 330, 195, SAND, "Mapa comum", [
        "Nome anatómico comum", "Campo disponível no modelo", "Intervalo declarado", "Campos ausentes são omitidos",
    ], True)
    parts.append(path("M305 215 H382"))

    models = [
        (790, 90, TEAL, "Flexy Beast", ["Palma: fórmula Cyborg Beast", "Dedos: proporções face ao médio"]),
        (1195, 90, PEACH, "Cyborg Beast", ["Escala da palma e alavancas", "Divisão proximal/distal calibrada"]),
        (790, 270, LAVENDER, "Paraglider Hand", ["Palma: escala uniforme", "Dedos: escalas próprias"]),
        (1195, 270, BLUE, "UnLimbited Phoenix", ["Escala global com limite mínimo", "Alongamento em zonas sem furos"]),
    ]
    for x, y, fill, heading, lines in models:
        parts.append(rect(x, y, 340, 135, fill, rx=16))
        parts.append(multiline(x + 170, y + 38, [heading], size=25, weight=700))
        parts.append(multiline(x + 170, y + 88, lines, size=19, line_height=30, weight=400))

    parts.extend([
        path("M712 157 H790"),
        path("M712 137 H740 V72 H1160 V157 H1195"),
        path("M712 283 H755 V337 H790"),
        path("M712 247 H1160 V337 H1195"),
    ])

    content_box(285, 505, 430, 165, PEACH, "Verificações necessárias", [
        "• limites e dependências internas", "• furos, folgas e interfaces mecânicas",
        "• comportamento fora da gama do modelo",
    ], True)
    content_box(865, 505, 450, 165, BLUE, "Resultado intermédio", [
        "Geometria OpenSCAD regenerada", "Malha STL/3MF mensurável",
        "Não equivale a ajuste anatómico validado",
    ], True)
    parts.extend([
        path("M960 405 V455 H650 V505"),
        path("M1365 405 V455 H1200 V505"),
        path("M715 588 H865"),
    ])

    parts.append(rect(360, 760, 880, 100, GREEN, rx=18))
    parts.append(multiline(800, 792, ["Decisão de projeto"], size=25, weight=700))
    parts.append(multiline(800, 835, ["Aceitar, corrigir, limitar ou rejeitar a configuração antes do fabrico"],
                           size=21, weight=400))
    parts.append(path("M1090 670 V715 H800 V760"))
    parts.append(footer())
    write(FIGURES / "figura_c1_fluxo_adaptacao_parametrica.svg", "\n".join(parts))


def main() -> None:
    figure_2_2()
    figure_2_3()
    figure_2_6()
    figure_2_7()
    figure_3_1()
    figure_6_1()
    figure_c_1()


if __name__ == "__main__":
    main()
