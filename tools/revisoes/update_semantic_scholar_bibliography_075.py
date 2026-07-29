#!/usr/bin/env python3
"""Completa 26 referências que ainda apontavam para o Semantic Scholar.

O programa sincroniza o Markdown e o DOCX canónicos. No DOCX altera apenas
``word/document.xml`` e confirma que as notas de rodapé, os comentários, as
imagens e todos os restantes componentes do pacote permanecem intactos.
"""

from __future__ import annotations

import html
import os
from hashlib import sha256
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.md"
DOCX = ROOT / "pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


ENTRIES = {
    "Akyol, P., Barker, T., Hall, R., Morrissey, K., McCarthy, J., & Mackley, K. L. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. https://www.semanticscholar.org/paper/ea18361f7564fb19db367899adb6295a07bfa05c":
        "Akyol, E., Cabral Ramos Mota, R. C., & Somanath, S. (2021). DiaFit: Designing customizable wearables for Type 1 diabetes monitoring. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (Article 437, pp. 1-6). ACM. https://doi.org/10.1145/3411763.3451716",
    "Bates, T., Fergason, J., & Pierrie, S. N. (2020). Technological advances in prosthesis design and rehabilitation following upper extremity limb loss. https://www.semanticscholar.org/paper/905056ffa9fa963e8df8b974d90b94c05a5f7e29":
        "Bates, T. J., Fergason, J. R., & Pierrie, S. N. (2020). Technological advances in prosthesis design and rehabilitation following upper extremity limb loss. Current Reviews in Musculoskeletal Medicine, 13(4), 485-493. https://doi.org/10.1007/s12178-020-09656-6",
    "Burnap, A., Hauser, J., & Timoshenko, A. (2019). Design and evaluation of product aesthetics: A human-machine hybrid approach. https://www.semanticscholar.org/paper/7a7994f2de74a61cbdeb3c230d1ee343a0d5e783":
        "Burnap, A., Hauser, J. R., & Timoshenko, A. (2019). Design and evaluation of product aesthetics: A human-machine hybrid approach. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3421771",
    "Çıklaçandır, S., Yilmaz, M., Ozmert, O. S., Şahin, A. M., & Mihçin, S. (2022). Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design. https://www.semanticscholar.org/paper/a24aab5d4434a01eeeda73c8a62f921580ceba54":
        "Çıklaçandır, S., Yılmaz, M., Özmert, O. S., Şahin, A. M., & Mihçin, S. (2022). Comparison of traditional, MRI, and 3D scanning anthropometric measurements in hand prosthesis design. In 2022 Medical Technologies Congress (TIPTEKNO) (pp. 1-4). IEEE. https://doi.org/10.1109/TIPTEKNO56568.2022.9960218",
    "Fisher, M., & Johansen, E. (2020). Human-centered design for medical devices and diagnostics in global health. https://www.semanticscholar.org/paper/89c3c6bd56f4d0b54f5da3e3c96f18e815d9f5d4":
        "Fisher, M., & Johansen, E. (2020). Human-centered design for medical devices and diagnostics in global health. Global Health Innovation, 3(1), 1-15. https://doi.org/10.15641/ghi.v3i1.762",
    "Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI co-design and co-creation: A review of emerging approaches, challenges, and future directions. https://www.semanticscholar.org/paper/61c04706b7af0be5be4b0d15f595d4ab41874d12":
        "Kadenhe, N., Al Musleh, M., & Lompot, A. (2025). Human-AI co-design and co-creation: A review of emerging approaches, challenges, and future directions. Proceedings of the AAAI Symposium Series, 6(1), 265-270. https://doi.org/10.1609/aaaiss.v6i1.36061",
    "Kandikjan, T., Djokikj, J., Mircheski, I., & Angeleska, E. (2022). Integrating parametric design and additive manufacturing knowledge in industrial design education. https://www.semanticscholar.org/paper/7d28a8c124ef0a3599dd937791a3f3e093775ac0":
        "Kandikjan, T., Djokikj, J., Mircheski, I., & Angeleska, E. (2022). Integrating parametric design and additive manufacturing knowledge in industrial design education. Materials Today: Proceedings, 70, 687-693. https://doi.org/10.1016/j.matpr.2022.10.124",
    "Khanolkar, P., Vrolijk, A., & Olechowski, A. (2023). Mapping artificial intelligence-based methods to engineering design stages: A focused literature review. https://www.semanticscholar.org/paper/4d63443d45e1a7156c5972ef009ed07bb0650117":
        "Khanolkar, P. M., Vrolijk, A., & Olechowski, A. (2023). Mapping artificial intelligence-based methods to engineering design stages: A focused literature review. Artificial Intelligence for Engineering Design, Analysis and Manufacturing, 37, e25. https://doi.org/10.1017/S0890060423000203",
    "Krahe, C., Bräunche, A., Jacob, A., Stricker, N., & Lanza, G. (2020). Deep learning for automated product design. https://www.semanticscholar.org/paper/a5b9b4f63805f2b1773bc8214b29e38dbac27975":
        "Krahe, C., Bräunche, A., Jacob, A., Stricker, N., & Lanza, G. (2020). Deep learning for automated product design. Procedia CIRP, 91, 3-8. https://doi.org/10.1016/j.procir.2020.01.135",
    "Millet, A., Akle, A. A., & Legardeur, J. (2018). Human centred criteria for healthcare design. https://www.semanticscholar.org/paper/267b655f123f4f167f1f9e7e6c8a1f17f73a73d0":
        "Millet, A., Abi Akle, A., & Legardeur, J. (2018, July 5-6). Human centred criteria for healthcare design [Conference paper]. 25e colloque des Sciences de la conception et de l’innovation (CONFERE 2018), Budapest, Hungary. https://hal.science/hal-01938985",
    "Panchal, J. H., Fuge, M., Liu, Y., Missoum, S., & Tucker, C. S. (2019). Special issue: Machine learning for engineering design. Journal of Mechanical Design. https://www.semanticscholar.org/paper/2c4f7ca9381db7debefe61d04da51f9e8e63d09d":
        "Panchal, J. H., Fuge, M., Liu, Y., Missoum, S., & Tucker, C. S. (2019). Special issue: Machine learning for engineering design. Journal of Mechanical Design, 141(11), 110301. https://doi.org/10.1115/1.4044690",
    "Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. https://www.semanticscholar.org/paper/40a0b51e5b01234cec3e807158b26a284ea77e0f":
        "Ramnath, S., Haghighi, P., Kim, J. H., Detwiler, D., Berry, M., Shah, J. J., Aulig, N., Wollstadt, P., & Menzel, S. (2019). Automatically generating 60,000 CAD variants for big data applications. In Volume 1: 39th Computers and Information in Engineering Conference (Article V001T02A006). ASME. https://doi.org/10.1115/DETC2019-97378",
    "Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. https://www.semanticscholar.org/paper/71e1fef52dde69cbcea4f62c709f7c6689f9463d":
        "Resnik, L., Klinger, S. L., Krauthamer, V., & Barnabe, K. (2010). U.S. Food and Drug Administration regulation of prosthetic research, development, and testing. JPO: Journal of Prosthetics and Orthotics, 22(2), 121-126. https://doi.org/10.1097/JPO.0b013e3181d427b7",
    "Saeidnia, H. R., & Ausloos, M. (2024). Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework. https://www.semanticscholar.org/paper/e2b8a10036428046443e24dc33ec5306876afdbb":
        "Saeidnia, H. R., & Ausloos, M. (2024). Integrating artificial intelligence into design thinking: A comprehensive examination of the principles and potentialities of AI for design thinking framework. InfoScience Trends, 1(2), 1-9. https://doi.org/10.61186/ist.202401.01.09",
    "Shah, S., & Robinson, I. (2006). User involvement in healthcare technology development and assessment: Structured literature review. https://www.semanticscholar.org/paper/299d5b2c1d65791cc4c9f2db76edf20f479adcbc":
        "Shah, S. G. S., & Robinson, I. (2006). User involvement in healthcare technology development and assessment: Structured literature review. International Journal of Health Care Quality Assurance, 19(6), 500-515. https://doi.org/10.1108/09526860610687619",
    "Smail, L. C., Neal, C., Wilkins, C., & Packham, T. (2020). Comfort and function remain key factors in upper limb prosthetic abandonment: Findings of a scoping review. https://www.semanticscholar.org/paper/b5eb3fd2414ebedaa5d2283451268fafa2db0a81":
        "Smail, L. C., Neal, C., Wilkins, C., & Packham, T. L. (2021). Comfort and function remain key factors in upper limb prosthetic abandonment: Findings of a scoping review. Disability and Rehabilitation: Assistive Technology, 16(8), 821-830. https://doi.org/10.1080/17483107.2020.1738567",
    "Story, M. (2006). Applying the principles of universal design to medical devices. https://www.semanticscholar.org/paper/d0d84425d517331607c9120290ed26d1bf2e1862":
        "Story, M. F. (2006). Applying the principles of universal design to medical devices. In J. M. Winters & M. F. Story (Eds.), Medical instrumentation: Accessibility and usability considerations (pp. 83-92). CRC Press. https://doi.org/10.1201/9781420006223-6",
    "Stralen, M. V. (2018). Mass customization: A critical perspective on parametric design, digital fabrication and design democratization. https://www.semanticscholar.org/paper/a18f2c4d248e791d2a9b84f3cab268d5a377cc10":
        "van Stralen, M. (2018). Mass customization: A critical perspective on parametric design, digital fabrication and design democratization. In Proceedings of the 22nd Congress of the Iberoamerican Society of Digital Graphics (pp. 142-149). Blucher. https://doi.org/10.5151/sigradi2018-1770",
    "Virós-i-Martin, A., & Selva, D. (2021). A framework to study human-AI collaborative design space exploration. https://www.semanticscholar.org/paper/716be148371af443169531b0856ae07dfe400869":
        "Virós-i-Martin, A., & Selva, D. (2021). A framework to study human-AI collaborative design space exploration. In Volume 6: 33rd International Conference on Design Theory and Methodology (Article V006T06A052). ASME. https://doi.org/10.1115/DETC2021-67619",
    "Walters, S., Seminati, E., Metcalfe, B., Bailey, N. Y., & Pegg, E. C. (2025). Demystifying upper limb hybrid prostheses: A scoping review. https://www.semanticscholar.org/paper/d659aff9bb182a3c92377571973e6e077a3b1838":
        "Walters, S., Seminati, E., Metcalfe, B., Bailey, N. Y., & Pegg, E. C. (2025). Demystifying upper limb hybrid prostheses: A scoping review. Frontiers in Rehabilitation Sciences, 6, 1610336. https://doi.org/10.3389/fresc.2025.1610336",
    "Wang, X., & Hu, B. (2024). Machine learning algorithms for improved product design user experience. https://www.semanticscholar.org/paper/717e7ad25dcafec12f01b6732773bdf9c5a49661":
        "Wang, X., & Hu, B. (2024). Machine learning algorithms for improved product design user experience. IEEE Access, 12, 112810-112821. https://doi.org/10.1109/ACCESS.2024.3442085",
    "White, J., & Mosca, E. I. (2022). Developing innovative solutions for universal design in healthcare and other sectors. https://www.semanticscholar.org/paper/df2bb0d53af547bd89b2c716933c2a544bf422b1":
        "White, J., & Mosca, E. I. (2022). Developing innovative solutions for universal design in healthcare and other sectors. Studies in Health Technology and Informatics, 297, 340-347. https://doi.org/10.3233/SHTI220858",
    "Wiberg, A., Persson, J., & Ölvander, J. (2019). Design for additive manufacturing: A review of available design methods and software. https://www.semanticscholar.org/paper/e03bf769f344512519f1005baa1d6b83fe4fc8ed":
        "Wiberg, A., Persson, J., & Ölvander, J. (2019). Design for additive manufacturing: A review of available design methods and software. Rapid Prototyping Journal, 25(6), 1080-1094. https://doi.org/10.1108/RPJ-10-2018-0262",
    "Wilke, H., Badke-Schaub, P., & Thoring, K. (2020). The healthcare design dilemma: Perils of a technology-driven design process for medical products. https://www.semanticscholar.org/paper/078781d9389d4618fc1b5db9347ab68ca7ef46d9":
        "Wilke, H., Badke-Schaub, P., & Thoring, K. (2020). The healthcare design dilemma: Perils of a technology-driven design process for medical products. Proceedings of the Design Society: DESIGN Conference, 1, 2217-2226. https://doi.org/10.1017/dsd.2020.133",
    "Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive manufactured variable platforms in product families. https://www.semanticscholar.org/paper/f7bc9dc2a80714c18ac068f45b99408b0f4fe65e":
        "Yao, X., Moon, S. K., & Bi, G. (2016). A cost-driven design methodology for additive manufactured variable platforms in product families. Journal of Mechanical Design, 138(4), 041701. https://doi.org/10.1115/1.4032504",
    "Yüksel, N., Börklü, H. R., Sezer, H. K., & Canyurt, O. (2023). Review of artificial intelligence applications in engineering design perspective. https://www.semanticscholar.org/paper/cd38b58edf6690459767097aca745a3806824236":
        "Yüksel, N., Börklü, H. R., Sezer, H. K., & Canyurt, O. (2023). Review of artificial intelligence applications in engineering design perspective. Engineering Applications of Artificial Intelligence, 118, 105697. https://doi.org/10.1016/j.engappai.2022.105697",
}


TEXT_REPLACEMENTS = {
    "Smail et al., 2020": ("Smail et al., 2021", 2),
    "Stralen, 2018": ("van Stralen, 2018", 5),
}


def xml_text(value: str) -> bytes:
    return html.escape(value, quote=False).encode("utf-8")


def document_state(xml: bytes) -> dict[str, int]:
    root = etree.fromstring(xml)
    return {
        "footnote_references": int(root.xpath("count(//w:footnoteReference)", namespaces=NS)),
        "comment_starts": int(root.xpath("count(//w:commentRangeStart)", namespaces=NS)),
        "comment_ends": int(root.xpath("count(//w:commentRangeEnd)", namespaces=NS)),
        "comment_references": int(root.xpath("count(//w:commentReference)", namespaces=NS)),
        "drawings": int(root.xpath("count(//w:drawing)", namespaces=NS)),
    }


def main() -> None:
    md = MD.read_text(encoding="utf-8")
    if md.count("Versão do documento: 0.4.74") != 1:
        raise RuntimeError("A versão de origem do Markdown não é 0.4.74")
    if len(ENTRIES) != 26:
        raise RuntimeError(f"Esperava 26 entradas; encontrei {len(ENTRIES)}")

    with ZipFile(DOCX) as source:
        infos = source.infolist()
        entries = {info.filename: source.read(info.filename) for info in infos}

    document = entries["word/document.xml"]
    before_state = document_state(document)
    before_other_hashes = {
        name: sha256(data).hexdigest()
        for name, data in entries.items()
        if name != "word/document.xml"
    }

    for old, new in ENTRIES.items():
        if md.count(old) != 1:
            raise RuntimeError(f"Entrada Markdown não encontrada uma única vez: {old[:80]}")
        if document.count(xml_text(old)) != 1:
            raise RuntimeError(f"Entrada DOCX não encontrada uma única vez: {old[:80]}")
        md = md.replace(old, new, 1)
        document = document.replace(xml_text(old), xml_text(new), 1)

    for old, (new, expected) in TEXT_REPLACEMENTS.items():
        if md.count(old) != expected:
            raise RuntimeError(
                f"Contagem inesperada no Markdown para {old!r}: {md.count(old)}"
            )
        if document.count(xml_text(old)) != expected:
            raise RuntimeError(
                f"Contagem inesperada no DOCX para {old!r}: {document.count(xml_text(old))}"
            )
        md = md.replace(old, new)
        document = document.replace(xml_text(old), xml_text(new))

    md = md.replace("Versão do documento: 0.4.74", "Versão do documento: 0.4.75", 1)
    md = md.replace('<a id="ref-smail-2020"></a>', '<a id="ref-smail-2021"></a>', 1)

    if "semanticscholar" in md.casefold() or b"semanticscholar" in document.lower():
        raise RuntimeError("Permaneceram ligações do Semantic Scholar no manuscrito")
    if document_state(document) != before_state:
        raise RuntimeError("A contagem de notas, comentários ou imagens foi alterada")

    entries["word/document.xml"] = document
    with NamedTemporaryFile(
        prefix=f".{DOCX.name}.", suffix=".tmp", dir=DOCX.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as output:
            for info in infos:
                output.writestr(info, entries[info.filename])
        with ZipFile(temporary) as result:
            if result.testzip() is not None:
                raise RuntimeError("O pacote DOCX resultante está corrompido")
            after_other_hashes = {
                info.filename: sha256(result.read(info.filename)).hexdigest()
                for info in result.infolist()
                if info.filename != "word/document.xml"
            }
        if after_other_hashes != before_other_hashes:
            raise RuntimeError("Um componente externo a word/document.xml foi alterado")
        MD.write_text(md, encoding="utf-8")
        os.replace(temporary, DOCX)
    finally:
        temporary.unlink(missing_ok=True)

    print(
        "26 referências normalizadas; "
        f"notas={before_state['footnote_references']}, "
        f"comentários={before_state['comment_references']}, "
        f"imagens={before_state['drawings']}"
    )


if __name__ == "__main__":
    main()
