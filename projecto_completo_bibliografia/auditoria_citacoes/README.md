# Matriz de citações e evidência

## Ficheiros

- `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.docx`: cópia congelada do DOCX canónico usada como fonte;
- `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.pdf`: conversão paginada da cópia, com 268 páginas A4;
- `referencias_evidencia_docx_2026-07-22.xlsx`: folha de cálculo final, com 417 linhas, uma por referência dentro de cada ocorrência de citação.

O SHA-256 da cópia de trabalho do DOCX é `09e09bc6d5d27dd79449778a61db1c739e7cbd392252b3b09f7207f645eaa2e3`. No fecho da auditoria, este valor continuava idêntico ao do DOCX canónico; o original não foi alterado por este trabalho.

## Estrutura da folha principal

As colunas seguem a ordem pedida:

1. página do nosso DOCX;
2. texto do nosso DOCX referenciado;
3. título do paper;
4. autor do paper;
5. ano de publicação do paper;
6. texto extraído do paper para fundamentar a referência no nosso DOCX.

A coluna 2 inclui a frase citante e, quando existem na mesma página, até duas frases anteriores. A coluna 6 preserva a língua original e começa por `[PDF, p. n]`, em que `n` é a página física, contada a partir de 1, do PDF local. O título contém uma hiperligação relativa para o PDF correspondente.

## Cobertura e limites

- entradas bibliográficas reconhecidas no DOCX: **169**;
- PDFs associados pelo manifesto bibliográfico validado: **158**;
- ocorrências registadas: **417**;
- ocorrências com excerto paginado: **411**;
- transcrições curtas confirmadas por revisão visual de PDFs sem camada textual: **7**;
- ocorrências associadas a uma fonte sem PDF local: **3**;
- ocorrências sem correspondência bibliográfica inequívoca: **3**.

As células vermelhas assinalam estes seis casos pendentes. As três fontes resolvidas sem PDF local são Design Council (citado como 2007), Ghali (2008) e Brooks (2026). As três citações não resolvidas são `Dickinson et al., 2024`, `Flexible Flyer (2020)` e `TU Delft, 1993–2004`.

Os excertos automáticos são candidatos de fundamentação obtidos por recuperação lexical bilingue sobre o texto integral local. Servem para acelerar a verificação, mas não substituem a leitura crítica do paper. As transcrições visuais foram usadas apenas para Chapman et al. (2025), Frayling (1994) e Guo (2025), cujos PDFs locais não disponibilizam texto integral pesquisável.

O índice, a bibliografia final e a lista de referências normativas foram excluídos da deteção de ocorrências. Foram mantidas as citações existentes no corpo, nas tabelas, nas legendas e nos anexos.

## Regeneração

```bash
python3 tools/generate_citation_evidence_sheet.py \
  --docx projecto_completo_bibliografia/auditoria_citacoes/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.docx \
  --pdf projecto_completo_bibliografia/auditoria_citacoes/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.pdf \
  --manifest projecto_completo_bibliografia/copied_matches.json \
  --output projecto_completo_bibliografia/auditoria_citacoes/referencias_evidencia_docx_2026-07-22.xlsx
```

