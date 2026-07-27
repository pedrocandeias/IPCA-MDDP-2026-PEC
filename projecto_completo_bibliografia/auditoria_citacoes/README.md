# Matriz de citações e evidência

## Ficheiros

- `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.docx`: cópia congelada do DOCX canónico usada como fonte;
- `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.pdf`: conversão paginada da cópia, com 268 páginas A4;
- `classificacoes_codex_340_independentes_2026-07-23.json`: registo reproduzível da classificação Codex das 340 células que estavam vazias;
- `referencias_evidencia_docx_2026-07-22.xlsx`: folha de cálculo final, com 417 linhas classificadas, uma por referência dentro de cada ocorrência de citação.

O SHA-256 da cópia de trabalho do DOCX é `09e09bc6d5d27dd79449778a61db1c739e7cbd392252b3b09f7207f645eaa2e3`. No fecho da auditoria, este valor continuava idêntico ao do DOCX canónico; o original não foi alterado por este trabalho.

## Estrutura da folha principal

As colunas seguem a ordem pedida:

1. página do nosso DOCX;
2. texto do nosso DOCX referenciado;
3. título do paper;
4. autor do paper;
5. ano de publicação do paper;
6. texto extraído do paper para fundamentar a referência no nosso DOCX;
7. grau de resposta da citação ao texto do nosso DOCX.

A coluna 2 inclui a frase citante e, quando existem na mesma página, até duas frases anteriores. A coluna 6 preserva a língua original e começa por `[PDF, p. n]`, em que `n` é a página física, contada a partir de 1, do PDF local. O título contém uma hiperligação relativa para o PDF correspondente.

A coluna 7 usa exclusivamente três classificações: `Responde totalmente`, `Responde parcialmente` e `Não responde`. Todas as células classificadas incluem um comentário de proveniência. As 77 classificações preexistentes conservam o comentário e a pontuação de correspondência originais; as 340 classificações Codex identificam o ficheiro de decisões e apresentam a respetiva justificação. A lista suspensa limita os valores admitidos às três opções definidas.

## Cobertura e limites

- entradas bibliográficas reconhecidas no DOCX: **169**;
- PDFs associados pelo manifesto bibliográfico validado: **158**;
- ocorrências registadas: **417**;
- ocorrências com excerto paginado: **411**;
- transcrições curtas confirmadas por revisão visual de PDFs sem camada textual: **7**;
- ocorrências associadas a uma fonte sem PDF local: **3**;
- ocorrências sem correspondência bibliográfica inequívoca: **3**.
- classificações preexistentes, preservadas sem alteração: **77**;
  - `Responde totalmente`: **47**;
  - `Responde parcialmente`: **29**;
  - `Não responde`: **1**;
- classificações independentes Codex: **340**;
  - `Responde totalmente`: **232**;
  - `Responde parcialmente`: **100**;
  - `Não responde`: **8**;
- total de ocorrências classificadas: **417**;
  - `Responde totalmente`: **279**;
  - `Responde parcialmente`: **129**;
  - `Não responde`: **9**;
- ocorrências que aguardam classificação: **0**.

As células vermelhas na coluna de excertos assinalam seis limitações da recuperação documental automática, não classificações pendentes. Três dizem respeito a fontes sem PDF local — Design Council (citado como 2007), Ghali (2008) e Brooks (2026) — e três a citações que não tinham correspondência bibliográfica inequívoca no DOCX congelado: `Dickinson et al., 2024`, `Flexible Flyer (2020)` e `TU Delft, 1993–2004`. Estas ocorrências foram verificadas em fontes públicas primárias ou autoritativas; a ausência de um excerto paginado de PDF local permanece explicitamente visível.

Os excertos automáticos são candidatos de fundamentação obtidos por recuperação lexical bilingue sobre o texto integral local. Servem para acelerar a verificação, mas não substituem a leitura crítica do paper. As transcrições visuais foram usadas apenas para Chapman et al. (2025), Frayling (1994) e Guo (2025), cujos PDFs locais não disponibilizam texto integral pesquisável.

As classificações foram importadas de `rastreabilidade_citacoes.xlsx`, que contém 90 leituras humanas. Foram associados 81 veredictos legíveis a 77 ocorrências únicas da cópia congelada; quatro leituras duplicadas convergiram para ocorrências já classificadas. Três veredictos parciais relativos à referência assinalada como ambígua de Romero et al. (2025) não foram transferidos, porque a correspondência bibliográfica não é suficientemente segura. As seis leituras marcadas como ilegíveis também permaneceram sem classificação.

As 340 células que permaneciam vazias foram classificadas numa passagem independente de Codex, com base apenas no texto do DOCX e nos excertos da matriz, nos PDFs locais quando necessário e em fontes públicas primárias ou autoritativas para os seis casos sem excerto local. `rastreabilidade_citacoes.xlsx` foi explicitamente excluído desta passagem e não foi consultado. As 77 classificações preexistentes foram preservadas integralmente e verificadas por um SHA-256 calculado sobre os respetivos valores e comentários.

O ficheiro `classificacoes_codex_340_independentes_2026-07-23.json` identifica a matriz de base pelo respetivo SHA-256, fixa a sequência e o conteúdo das 340 linhas vazias e regista as decisões. O programa `tools/apply_independent_citation_classifications.py` recusa usar `rastreabilidade_citacoes.xlsx`, aplica decisões apenas a células vazias e interrompe a execução se qualquer classificação preexistente tiver sido alterada.

O índice, a bibliografia final e a lista de referências normativas foram excluídos da deteção de ocorrências. Foram mantidas as citações existentes no corpo, nas tabelas, nas legendas e nos anexos.

## Regeneração

```bash
python3 tools/generate_citation_evidence_sheet.py \
  --docx projecto_completo_bibliografia/auditoria_citacoes/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.docx \
  --pdf projecto_completo_bibliografia/auditoria_citacoes/pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_fonte_2026-07-22_20-36-42.pdf \
  --manifest projecto_completo_bibliografia/copied_matches.json \
  --reviewed-workbook projecto_completo_bibliografia/auditoria_citacoes/rastreabilidade_citacoes.xlsx \
  --output projecto_completo_bibliografia/auditoria_citacoes/referencias_evidencia_docx_2026-07-22.xlsx
```

O comando anterior documenta a criação da matriz de base e a proveniência histórica das 77 classificações preexistentes; não fez parte da revisão independente Codex das restantes 340 linhas. Essa passagem é reproduzida separadamente, sem aceitar o ficheiro de rastreabilidade como entrada:

```bash
python3 tools/apply_independent_citation_classifications.py \
  --workbook projecto_completo_bibliografia/auditoria_citacoes/referencias_evidencia_docx_2026-07-22.xlsx \
  --decisions projecto_completo_bibliografia/auditoria_citacoes/classificacoes_codex_340_independentes_2026-07-23.json
```
