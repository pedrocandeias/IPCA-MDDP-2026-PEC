# Elicit API

Este repositório tem uma integração local mínima com o Elicit em `scripts/elicit_api.py`, alinhada com os exemplos oficiais em `elicit/api-examples`.

## Configuração

Crie uma chave no Elicit Account Settings e exporte-a no terminal:

```bash
export ELICIT_API_KEY="elk_live_..."
```

Também pode copiar `.env.example` para o seu fluxo local de variáveis de ambiente.

## Comandos

Pesquisar papers:

```bash
python3 scripts/elicit_api.py search "upper limb prosthetics personalization" --min-year 2020 --type RCT --max-results 5
```

Criar relatório:

```bash
python3 scripts/elicit_api.py report "How can parametric design improve upper limb prosthetic personalization?" --title "Parametric Prosthetic Personalization"
```

Ver estado de um relatório:

```bash
python3 scripts/elicit_api.py reports --limit 5
python3 scripts/elicit_api.py get-report <report_id>
python3 scripts/elicit_api.py wait-report <report_id> --poll-seconds 30
```

Descarregar outputs concluídos para `sources/elicit/reports/<report_id>/`:

```bash
python3 scripts/elicit_api.py download-report <report_id>
```

## Notas

- A API oficial usa `Authorization: Bearer <token>`.
- `POST /api/v1/search` e `POST /api/v1/search/trials` partilham o mesmo rate limit.
- `POST /api/v1/reports` cria jobs assíncronos; a documentação recomenda polling a cada 30–60 segundos.
- Os links `docxUrl` e `pdfUrl` de relatórios concluídos expiram, por isso o script volta a consultar o relatório antes de descarregar.
- Os exemplos oficiais do Elicit incluem versões simples em `curl`, `javascript` e `python`, além de uma CLI stdlib-only semelhante a esta.

Fontes oficiais:
- https://docs.elicit.com/
- https://github.com/elicit/api-examples
