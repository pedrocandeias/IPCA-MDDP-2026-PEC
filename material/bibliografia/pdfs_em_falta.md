# PDFs em falta — bibliografia do DOCX

Este relatório verifica a disponibilidade local do texto integral para as entradas materializadas na bibliografia do DOCX canónico. O Markdown que replica o manuscrito não é lido.

Última verificação: 2026-07-30.

## Síntese

- Documento: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`.
- SHA-256 do DOCX: `cd38830d659707c2df46a549458010b8bdd52f3caeff33b1fc4e174988b76ad2`.
- Entradas bibliográficas: **171**.
- Entradas com PDF local validado: **159**.
- Recursos sem PDF autónomo esperado: **10**.
- Entradas sem texto integral local: **2**.

## Entradas sem texto integral local

| N.º | Referência | Título | Localização bibliográfica | Estado |
| ---: | --- | --- | --- | --- |
| 1 | Molenbroek (2003) | *Revision of the Dutch standard for furniture in schools* | [https://doi.org/10.1080/0014013031000085635](https://doi.org/10.1080/0014013031000085635) | DOI confirmado na entrada; PDF local não localizado. |
| 2 | Steenbekkers (1998) | *Design-relevant characteristics of ageing users* | [Pesquisar no Crossref](https://search.crossref.org/?q=%22Design-relevant%20characteristics%20of%20ageing%20users%22) | DOI não identificado; PDF local não localizado. |

## Recursos sem PDF autónomo esperado

| Referência | Recurso |
| --- | --- |
| ASTM International. (2024) | *Standard guide for assessing fit accommodation of exoskeletons for manufacturers and designers* |
| Base local consolidada de dados antropométricos da mão e do membro superior distal. (2026) | *[Conjunto de dados]* |
| Brooks (2026) | *OpenSCAD Web [Computer software]* |
| daprice. (n.d.) | *Flexy Beast [README file]* |
| Design Council. (2020) | *Framework for innovation* |
| International Organization for Standardization. (n.d.) | *ISO/TC 168: Prosthetics and orthotics* |
| Molenbroek (1998) | *Geron study on Dutch elderly anthropometry* |
| OpenSCAD Community. (n.d.) | *OpenSCAD User Manual/Using OpenSCAD in a command line environment* |
| OpenSCAD Project. (n.d.-a) | *OpenSCAD: The programmers solid 3D CAD modeller* |
| OpenSCAD Project. (n.d.-b) | *OpenSCAD source repository [Computer software]* |

## Limite desta verificação

Este inventário responde apenas à pergunta «existe texto integral local para cada entrada bibliográfica?». Não demonstra que todas as citações do DOCX tenham uma entrada correcta. As citações ausentes, os controlos ligados à obra errada, as divergências de ano e as entradas potencialmente órfãs são registados em `docs/revisoes/bibliografia/auditoria_completude_bibliografica_docx_0_4_112.md`.

As duas entradas actualmente sem texto integral também figuram como potencialmente órfãs nessa auditoria. A decisão editorial sobre a sua manutenção deve preceder uma nova tentativa de obtenção.

## Método reproduzível

```bash
python3 tools/extraccao/generate_missing_pdfs_report.py
```
