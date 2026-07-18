#!/usr/bin/env python3
"""Integra as cinco figuras com setas reduzidas na versão 0.4.69."""

from __future__ import annotations

from update_restyled_figures_068 import ANNEX, CANONICAL, ROOT, replace_media


CANONICAL_MEDIA = {
    "word/media/image5.jpeg": (
        ROOT / "figuras/figura_2_2_utilizacao_rejeicao_proteses_estilizada.jpeg",
        (2160, 1458),
    ),
    "word/media/image6.png": (
        ROOT / "figuras/figura_2_3_fluxo_digital_proteses_estilizada.png",
        (2394, 1623),
    ),
    "word/media/image10.png": (
        ROOT / "figuras/figura_2_7_participacao_cocriacao_estilizada.png",
        (2032, 1048),
    ),
    "word/media/image12.png": (
        ROOT / "figuras/figura_3_1_processo_interdisciplinar_estilizada.png",
        (2070, 744),
    ),
    "word/media/image34.png": (
        ROOT / "sources/manuscript/annexes/adaptacao_parametrica_modelos/figura_c1_fluxo_adaptacao_parametrica.png",
        (1800, 1035),
    ),
}

ANNEX_MEDIA = {
    "word/media/image1.png": CANONICAL_MEDIA["word/media/image34.png"],
}


def main() -> None:
    replace_media(CANONICAL, CANONICAL_MEDIA)
    replace_media(ANNEX, ANNEX_MEDIA)


if __name__ == "__main__":
    main()
