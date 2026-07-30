#!/usr/bin/env python3
"""Sincroniza o Anexo D autónomo com a fonte Markdown consolidada."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
ANNEX = (
    ROOT
    / "anexos/testes_preparacao_impressao"
    / "anexo_d_preparacao_impressao.md"
)

TABLE_ROWS = """| Tabela D.1 | Estimativas dos projectos de preparação digital para impressão 3D com configuração analisada | — |
| Tabela D.2 | Estimativas de preparação para impressão na condição digital comum | — |
| Tabela D.3 | Comparação dimensional da palma no eixo X em PLA e PETG | — |"""


def main() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    annex = ANNEX.read_text(encoding="utf-8").strip()
    annex = annex.replace(
        "](figuras/",
        "](anexos/testes_preparacao_impressao/figuras/",
    )

    marker = "\n# Anexo D —"
    if marker in manuscript:
        manuscript = manuscript.split(marker, 1)[0].rstrip()

    if "| Tabela D.1 |" not in manuscript:
        anchors = [
            line
            for line in manuscript.splitlines()
            if line.startswith(
                "| Tabela C.4 | Comparação das adaptações e excepções de escala |"
            )
        ]
        if len(anchors) != 1:
            raise RuntimeError("Não foi localizado o fim da lista de tabelas do Anexo C")
        anchor = anchors[0]
        manuscript = manuscript.replace(anchor, f"{anchor}\n{TABLE_ROWS}", 1)

    MANUSCRIPT.write_text(f"{manuscript}\n\n{annex}\n", encoding="utf-8")
    print(f"Anexo D sincronizado em {MANUSCRIPT}")


if __name__ == "__main__":
    main()
