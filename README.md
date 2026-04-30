# Mestrado Thesis Workspace

Este repositório organiza a redação da tese e os materiais de pesquisa associados, incluindo uma integração local com a API do [Elicit](https://docs.elicit.com/) para pesquisa bibliográfica e geração de relatórios.

## Estrutura do repositório

- `Projecto completo.md`: manuscrito principal consolidado
- `chapters/text/`: rascunhos de capítulos em `.txt`
- `chapters/html/`: exports HTML de capítulos
- `sources/docx/`: documentos de apoio em `.docx`
- `sources/capitulo2/`: fontes e exports de pesquisa do capítulo 2
- `scripts/elicit_api.py`: CLI local para usar a API do Elicit
- `docs/elicit-api.md`: notas curtas sobre a integração

## O que é preciso

Antes de usar a integração:

1. Ter Python 3 instalado
2. Ter conta no Elicit
3. Ter plano `Pro` ou superior no Elicit para acesso à API
4. Criar uma API key em `https://elicit.com/settings`

## Configuração passo a passo

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Exporte a chave da API no terminal:

```bash
export ELICIT_API_KEY="elk_live_..."
```

4. Valide a CLI local:

```bash
python3 -m py_compile scripts/elicit_api.py
```

## Como usar

### 1. Pesquisar papers

```bash
python3 scripts/elicit_api.py search "upper limb prosthetics personalization" --min-year 2020 --type RCT --max-results 5
```

Use este comando para encontrar artigos, filtrar por ano, tipo de estudo ou corpus.

### 2. Criar um relatório no Elicit

```bash
python3 scripts/elicit_api.py report "How can parametric design improve upper limb prosthetic personalization?" --title "Parametric Prosthetic Personalization"
```

O Elicit cria o relatório de forma assíncrona. A CLI faz polling até o relatório terminar, salvo se usar `--no-wait`.

### 3. Ver relatórios existentes

```bash
python3 scripts/elicit_api.py reports --limit 5
python3 scripts/elicit_api.py get-report <report_id>
```

### 4. Esperar explicitamente por um relatório

```bash
python3 scripts/elicit_api.py wait-report <report_id> --poll-seconds 30
```

### 5. Descarregar os ficheiros gerados

```bash
python3 scripts/elicit_api.py download-report <report_id>
```

Os outputs são guardados em `sources/elicit/reports/<report_id>/`.

## Workflow recomendado

1. Pesquisar literatura com `search`
2. Criar relatórios temáticos com `report`
3. Descarregar `.docx` e `.pdf` com `download-report`
4. Usar os resultados para atualizar `Projecto completo.md` e os ficheiros em `chapters/`
5. Manter fontes brutas em `sources/` e texto trabalhado no manuscrito

## Notas

- A autenticação usa `Authorization: Bearer <token>`.
- `POST /api/v1/search` e `POST /api/v1/search/trials` partilham rate limit.
- Os links temporários de download do Elicit expiram; por isso a CLI consulta novamente o relatório antes de descarregar.
- Esta integração segue a documentação oficial e o repositório `elicit/api-examples`.

## Referências

- Documentação oficial: https://docs.elicit.com/
- Exemplos oficiais: https://github.com/elicit/api-examples
