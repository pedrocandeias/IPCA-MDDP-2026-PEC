# projecto_completo_bibliografia

- Documento de origem: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto.docx`
- Entradas bibliográficas identificadas: 169
- Entradas com PDF local validado nesta pasta: 158
- PDFs existentes na pasta: 182
- PDFs acrescentados na consolidação de 21 de Julho de 2026: 27
- Documentos citados sem texto integral local: 5
- Recursos digitais ou conjuntos de dados sem PDF autónomo esperado: 6

Ficheiros auxiliares:

- `consolidacao_referencias_docx.md`: relatório legível, incluindo critérios de correspondência e documentos sem texto integral;
- `copied_matches.json`: manifesto das 158 correspondências validadas;
- `pdfs_em_falta.md`: lista autoritativa dos *papers* citados ainda sem texto integral, com os documentos académicos não classificados como *paper* indicados separadamente.

Método de actualização:

```bash
python3 tools/consolidate_docx_referenced_pdfs.py --apply
python3 tools/generate_missing_pdfs_report.py
```

O emparelhamento utiliza DOI, título, autoria e ano. As associações históricas com nomes de ficheiro incorrectos só são aceites quando já foram confrontadas documentalmente na auditoria bibliográfica.
