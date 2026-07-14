# Dicionário de parâmetros e percurso numérico — HandFab 14.67.0

Este suplemento preserva o dicionário completo dos parâmetros numéricos dos três modelos avaliados na dissertação — Flexy Beast, Paraglider Hand e UnLimbited Phoenix — e um percurso verificável entre um perfil de ensaio, os parâmetros aplicados, as relações OpenSCAD e três malhas 3MF exportadas.

## Versão e origem

- Plataforma: HandFab 14.67.0
- Confirmação Git: `bcef0db`
- Configuração-fonte: `models/models-config.json`
- Execução arquivada usada no exemplo: campanha de 8 de Julho de 2026, perfil `child_8`
- Modelo do exemplo: `flexy_beast`

O CSV é regenerado directamente a partir da configuração existente na confirmação Git indicada. O exemplo reutiliza os ficheiros arquivados pela campanha de preparação para impressão. A origem demográfica declara Brasil, país ausente da base antropométrica; por isso, o exemplo demonstra a cadeia técnica e os limites aplicados, não adequação populacional ou individual.

## Conteúdo

- `parameter_dictionary.csv`: 42 parâmetros numéricos, com modelo, grupo, unidade, valor inicial, mínimo, máximo, incremento, designação e descrição em português, papel e exclusão da IA.
- `example_flexy_beast_child_8/params.json`: perfil de ensaio e valores aplicados.
- `example_flexy_beast_child_8/palm.3mf`: malha da palma.
- `example_flexy_beast_child_8/middle_base.3mf`: malha do segmento proximal do dedo médio.
- `example_flexy_beast_child_8/middle_tip.3mf`: malha do segmento distal do dedo médio.
- `example_flexy_beast_child_8/trace.json`: limites, cálculos derivados, proporções digitais, métricas das malhas e checksums.
- `SHA256SUMS`: integridade dos ficheiros suplementares.

## Regeneração

```bash
python3 generate_supplement.py \
  --repository /home/pec/dev/ai-parametric-prosthetic-hand-generator \
  --commit bcef0db
sha256sum -c SHA256SUMS
```

O script requer Python, Git e `trimesh`. A medição concatena os objectos de cada 3MF e regista a caixa envolvente nos eixos XYZ, as três extensões por ordem decrescente, estanquidade, volume quando a malha é fechada e número de faces.

## Limite de interpretação

Os valores do exemplo resultam de um perfil de ensaio e de uma extracção de IA conservada como evidência. O percurso prova que valores aceites pelo esquema produzem transformações identificáveis e malhas mensuráveis. Não demonstra ajuste anatómico, conforto, função, segurança ou validade clínica.
