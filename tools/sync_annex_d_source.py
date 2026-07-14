#!/usr/bin/env python3
"""Sincroniza o Anexo D autónomo com a fonte Markdown consolidada."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
ANNEX = (
    ROOT
    / "sources/manuscript/annexes/testes_preparacao_impressao"
    / "anexo_d_preparacao_impressao.md"
)

TABLE_ROWS = """| Tabela D.1 | Estimativas dos projectos de impressão arquivados | — |
| Tabela D.2 | Estimativas de preparação para impressão na condição digital comum | — |
| Tabela D.3 | Preparação da comparação dimensional da palma | — |"""


def main() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    annex = ANNEX.read_text(encoding="utf-8").strip()

    marker = "\n# Anexo D —"
    if marker in manuscript:
        manuscript = manuscript.split(marker, 1)[0].rstrip()

    if "| Tabela D.1 |" not in manuscript:
        anchor = (
            "| Tabela C.4 | Comparação das adaptações e excepções de escala | 143 |"
        )
        if anchor not in manuscript:
            raise RuntimeError("Não foi localizado o fim da lista de tabelas do Anexo C")
        manuscript = manuscript.replace(anchor, f"{anchor}\n{TABLE_ROWS}", 1)

    MANUSCRIPT.write_text(f"{manuscript}\n\n{annex}\n", encoding="utf-8")
    print(f"Anexo D sincronizado em {MANUSCRIPT}")


if __name__ == "__main__":
    main()
