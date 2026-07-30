# Fonte de trabalho do Suplemento 1 — Dados antropométricos

Este directório conserva os três CSV e os dois scripts Python referidos no Anexo A da dissertação. Os ficheiros foram copiados do repositório local `ai-parametric-prosthetic-hand-generator`, no estado correspondente ao *commit* `bcef0db` (`v14.67.0`), e regenerados em 13 de julho de 2026.

## Conteúdo

- `ansur_1988_complete.csv`: 2.726 linhas de dados e uma linha de cabeçalho.
- `ansur_1988_hand_arm.csv`: 696 linhas de dados e uma linha de cabeçalho.
- `multi_population_hand.csv`: 1.790 linhas de dados e uma linha de cabeçalho.
- `generate_ansur_csv.py`: gera os dois CSV ANSUR.
- `generate_multi_population_hand_csv.py`: gera o CSV multipopulacional.
- `SHA256SUMS`: resumos criptográficos dos cinco ficheiros.

## Regeneração

Executar, a partir deste directório:

```bash
python3 generate_ansur_csv.py
python3 generate_multi_population_hand_csv.py
sha256sum -c SHA256SUMS
```

O ensaio de regeneração realizado em 13 de julho de 2026 produziu novamente 2.726, 696 e 1.790 linhas de dados e preservou todos os resumos SHA-256 registados.

## Rastreabilidade

- Versão funcional documentada na dissertação: `14.67.0`.
- *Commit* de origem dos dados: `bcef0db`.
- Repositório de origem: `/home/pec/dev/ai-parametric-prosthetic-hand-generator`.
- Localização pública da plataforma: <https://handfab.pedrocandeias.net/>.

O caminho local do repositório serve apenas para identificar a proveniência no ambiente de desenvolvimento. O pacote mínimo entregue com a dissertação encontra-se em `suplementos/01_dados_antropometricos/` e contém os três CSV, sem duplicar os programas auxiliares de geração.
