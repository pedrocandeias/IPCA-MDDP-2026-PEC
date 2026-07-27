#!/usr/bin/env python3
"""Sincroniza o Markdown canónico com o DOCX gerido pelo Mendeley Cite (v0.4.107).

Alterações aplicadas apenas ao Markdown:
  1. Remoção da Figura 8.4 (frase introdutória, imagem, legenda, crédito e
     linha do índice de figuras), eliminada pelo autor no DOCX.
  2. Desambiguação das citações "Romero et al., 2025" segundo os dados das
     citações vivas do Mendeley Cite: "R. C. da S. Romero et al." para
     da Silveira Romero, Costa, Reis & Vimieiro (2025) e "E. Romero et al."
     para Romero, Garcia, Parra et al. (2025).
  3. Correcção de cinco entradas bibliográficas com autores e/ou DOI
     errados, confirmados no CrossRef: Baron 2020, Cabibihan 2018,
     Henao 2025, Herneth 2024 e Hofmann 2016.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"

OLD_VERSION = "Versão do documento: 0.4.106"
NEW_VERSION = "Versão do documento: 0.4.107"

REMOVE_LINES = [
    "| Figura 8.4 | Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior. | 108 |",
    "A Figura 8.4 apresenta um precedente de avaliação funcional baseado em tarefas quotidianas. No presente trabalho, funciona como enquadramento de uma etapa futura posterior à verificação técnica e material (Romero et al., 2025).",
    "![](projecto-completo_media/image20.png)",
    "Figura 8.4 — Tarefas funcionais usadas em avaliação de prótese personalizada de membro superior.",
    "Reproduzido de Romero, E., Garcia, J. G., Parra, M., Caballa, S., Saldarriaga, A. M., Luque, E. F., Rodriguez, D. J., Abarca, V. E., & Elias, D. A. (2025). An affordable AI-driven and 3D-printed personalized myoelectric prosthesis: Design, development, and assessment. IEEE Access, 13. https://doi.org/10.1109/ACCESS.2025.3596475",
]

REPLACEMENTS: list[tuple[str, str, int]] = [
    ("(Moreo, 2016; Romero et al., 2025)",
     "(Moreo, 2016; R. C. da S. Romero et al., 2025)", 2),
    ("(Machado et al., 2019; Moreo, 2016; Romero et al., 2025)",
     "(Machado et al., 2019; Moreo, 2016; R. C. da S. Romero et al., 2025)", 1),
    ("(Machado et al., 2019; Romero et al., 2025)",
     "(Machado et al., 2019; E. Romero et al., 2025)", 1),
    ("(Gu et al., 2024; da Silveira Romero et al., 2025; Saldarriaga et al., 2024)",
     "(Gu et al., 2024; R. C. da S. Romero et al., 2025; Saldarriaga et al., 2024)", 1),
    ("(Lim et al., 2018; Saldarriaga et al., 2024; da Silveira Romero et al., 2025)",
     "(Lim et al., 2018; Saldarriaga et al., 2024; R. C. da S. Romero et al., 2025)", 1),
    # Entradas bibliográficas corrigidas (autores e DOI confirmados no CrossRef)
    ('<a id="ref-baron-2020"></a> Baron, A., Gatzweiler, C., Geislinger, A., Huber, C., & Aszmann, O. C. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 274-287. https://doi.org/10.3390/prosthesis2040021',
     '<a id="ref-baron-2020"></a> Baron, J., Hazubski, S., & Otte, A. (2020). 3D multi-material printing of an anthropomorphic, personalized replacement hand for use in neuroprosthetics using 3D scanning and computer-aided design: First proof-of-technical-concept study. Prosthesis, 2(4), 362-370. https://doi.org/10.3390/prosthesis2040034', 1),
    ('<a id="ref-cabibihan-2018"></a> Cabibihan, J.-J., Pattofatto, S., Jomaa, M., Benallal, A., & Carrozza, M. C. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2831907',
     '<a id="ref-cabibihan-2018"></a> Cabibihan, J.-J., Abubasha, M. K., & Thakor, N. V. (2018). A method for 3-D printing patient-specific prosthetic arms with high accuracy shape and size. IEEE Access, 6, 25029-25039. https://doi.org/10.1109/ACCESS.2018.2825224', 1),
    ("<a id=\"ref-henao-2025\"></a> Henao, J. C., Phillips, S. T., Brooks, T. L., Pienta, K. J., Brantley, J. S., & Carey, S. L. (2025). Upper-limb prosthetic requirements from the healthcare providers, end-users and relatives' perspectives. Journal of Hand Therapy. Advance online publication. https://doi.org/10.1016/j.jht.2025.01.004",
     "<a id=\"ref-henao-2025\"></a> Henao, S. C., Cuartas-Escobar, S., Salazar-Salgado, S., & Posada-Borrero, A. M. (2025). Upper-limb prosthetic requirements from the healthcare providers, end-users and relatives' perspectives. Journal of Hand Therapy. Advance online publication. https://doi.org/10.1016/j.jht.2025.04.006", 1),
    ('<a id="ref-herneth-2024"></a> Herneth, T., Hiesl, A., Stief, F., & Farago, D. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1-8). IEEE. https://doi.org/10.1109/IROS58592.2024.10801868',
     '<a id="ref-herneth-2024"></a> Herneth, C., Ganguly, A., & Haddadin, S. (2024). Functional kinematic and kinetic requirements of the upper limb during activities of daily living: A recommendation on necessary joint capabilities for prosthetic arms. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 191-198). IEEE. https://doi.org/10.1109/IROS58592.2024.10802080', 1),
    ('<a id="ref-hofmann-2016"></a> Hofmann, M. H., Griffiths, D., & Margetts, E. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858346',
     '<a id="ref-hofmann-2016"></a> Hofmann, M., Harris, J., Hudson, S. E., & Mankoff, J. (2016). Helping hands: Requirements for a prototyping methodology for upper-limb prosthetics users. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (pp. 1769-1780). ACM. https://doi.org/10.1145/2858036.2858340', 1),
]


def main() -> None:
    text = MD.read_text(encoding="utf-8")
    if text.count(OLD_VERSION) != 1:
        raise RuntimeError("A versão de origem do Markdown não é 0.4.106")

    for line in REMOVE_LINES:
        if text.count(line) != 1:
            raise RuntimeError(f"Linha a remover não é única: {line[:60]!r}")
    for old, _new, n in REPLACEMENTS:
        if text.count(old) != n:
            raise RuntimeError(
                f"Esperava {n} ocorrência(s), encontrei {text.count(old)}: "
                f"{old[:60]!r}")

    lines = text.split("\n")
    out: list[str] = []
    removing = set(REMOVE_LINES)
    i = 0
    while i < len(lines):
        if lines[i] in removing:
            # remove também a linha vazia seguinte, se existir
            i += 1
            if i < len(lines) and lines[i] == "":
                i += 1
            continue
        out.append(lines[i])
        i += 1
    text = "\n".join(out)

    for old, new, _n in REPLACEMENTS:
        text = text.replace(old, new)
    text = text.replace(OLD_VERSION, NEW_VERSION, 1)

    MD.write_text(text, encoding="utf-8")
    print("Markdown sincronizado e versão actualizada para 0.4.107.")


if __name__ == "__main__":
    main()
