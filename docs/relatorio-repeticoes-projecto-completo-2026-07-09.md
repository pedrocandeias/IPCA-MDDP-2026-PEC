# Relatório de repetições no `projecto-completo.md`

Data: 2026-07-09
Ficheiro analisado: `projecto-completo.md`
Versão analisada: 0.4.18
Fonte derivada produzida: `docs/projecto-completo-sem-repeticoes.md`
DOCX derivado produzido: `projecto-completo-sem-repetições.docx`

## 1. Síntese

A revisão incidiu sobre o `projecto-completo.md` atual, por ser a fonte editável principal do manuscrito. O `projecto-completo.docx` de raiz encontrava-se modificado localmente e com ficheiro de bloqueio do LibreOffice; por isso, não foi usado como fonte textual para evitar misturar uma cópia DOCX 0.4.17 com o Markdown 0.4.18.

O problema principal já não é a existência de muitos duplicados exatos. A versão 0.4.18 tem apenas um grupo de frase exatamente duplicada, no Capítulo 7. O restante problema é funcional: alguns blocos dos capítulos 6, 8 e 9 voltam a explicar a mesma cadeia de validação assistida por IA, sobretudo a descrição do pedido enviado ao modelo, a lateralidade, a variabilidade estocástica e a delimitação entre validação interna e validação clínica.

Foi produzida uma versão derivada, `docs/projecto-completo-sem-repeticoes.md`, com cortes e condensações focados nesses pontos. Esta versão não substitui automaticamente o manuscrito principal.

## 2. Metodologia

- Análise automática de blocos de prosa com mais de 80 caracteres.
- Exclusão de tabelas, imagens, legendas, linhas de fonte, notas, headings e bibliografia na contagem principal.
- Normalização textual para detetar parágrafos e frases exatamente repetidos.
- Pesquisa dirigida por termos recorrentes: `lateralidade`, `esquema vivo`, `JSON`, `human-in-the-loop`, `validação clínica`, `variabilidade estocástica`, `invariantes` e `descrições incompletas`.
- Leitura editorial das zonas críticas dos capítulos 5, 6, 7, 8 e 9.

Resultados automáticos:

| Ficheiro | Linhas | Palavras no corpo antes da bibliografia | Parágrafos duplicados | Frases duplicadas |
|---|---:|---:|---:|---:|
| `projecto-completo.md` | 2348 | 40443 | 0 | 1 grupo |
| `docs/projecto-completo-sem-repeticoes.md` | 2326 | 39631 | 0 | 0 |

## 3. Repetições corrigidas

### R1 - Frase duplicada no Capítulo 7

Prioridade: alta
Tipo: duplicação textual exata
Localização no original:

- `projecto-completo.md:1380`
- `projecto-completo.md:1382`

A segunda ocorrência isolada foi removida. A formulação integrada no parágrafo crítico foi mantida, porque aí cumpre função argumentativa.

Local na versão derivada:

- `docs/projecto-completo-sem-repeticoes.md:1360`

### R2 - Sobreposição entre o protocolo de 6.3 e os resultados de 8.2/8.3

Prioridade: alta
Tipo: repetição funcional de método, resultados e interpretação
Locais principais no original:

- `projecto-completo.md:1256-1284`
- `projecto-completo.md:1434-1492`
- `projecto-completo.md:1494-1534`

A Secção 6.3 foi reduzida para protocolo, critérios e escopo. Os resultados, fragilidades e correções ficaram concentrados nas Secções 8.2 e 8.3.

Locais na versão derivada:

- `docs/projecto-completo-sem-repeticoes.md:1256-1266`
- `docs/projecto-completo-sem-repeticoes.md:1412-1470`
- `docs/projecto-completo-sem-repeticoes.md:1472-1512`

### R3 - Descrição repetida do pedido enviado à IA

Prioridade: alta
Tipo: repetição técnica
Locais no original:

- `projecto-completo.md:1176-1178`
- `projecto-completo.md:1248`
- `projecto-completo.md:1258`

O detalhe técnico completo foi preservado em 5.4. Em 6.2 e 6.3, a descrição foi resumida para explicitar apenas a função conceptual e metodológica: a IA opera dentro de uma gramática paramétrica declarada e filtrada pela aplicação.

Locais na versão derivada:

- `docs/projecto-completo-sem-repeticoes.md:1176-1178`
- `docs/projecto-completo-sem-repeticoes.md:1248`
- `docs/projecto-completo-sem-repeticoes.md:1258`

### R4 - Lateralidade repetida em vários momentos finais

Prioridade: média-alta
Tipo: repetição temática transversal
Locais no original:

- `projecto-completo.md:1260-1284`
- `projecto-completo.md:1472`
- `projecto-completo.md:1490`
- `projecto-completo.md:1542`
- `projecto-completo.md:1564`
- `projecto-completo.md:1584`

A narrativa completa da falha e da correção fica em 8.2. Em 6.3, a lateralidade permanece como critério de verificação. Em 8.4 e 9.1-9.3, a referência foi mantida apenas como síntese de limite, salvaguarda ou trabalho futuro.

### R5 - Variabilidade estocástica e invariantes

Prioridade: média
Tipo: repetição de interpretação metodológica
Locais no original:

- `projecto-completo.md:1274-1278`
- `projecto-completo.md:1492`
- `projecto-completo.md:1542`
- `projecto-completo.md:1586`

A observação empírica ficou em 8.2. A discussão de limites ficou condensada em 8.4. A necessidade de quantificação futura foi preservada em 9.3.

Local revisto na versão derivada:

- `docs/projecto-completo-sem-repeticoes.md:1470`
- `docs/projecto-completo-sem-repeticoes.md:1520`
- `docs/projecto-completo-sem-repeticoes.md:1564`

## 4. Limpezas editoriais associadas

Foram corrigidos artefactos formais que dificultavam a leitura das zonas revistas:

- junções de frase: `smartphones.É`, `multiutilizador.Esta`, `human-in-the-loop.O`, `linguagem.A`;
- erro tipográfico em `próteses e e encaixes`;
- erro de concordância em `IA supervisionado`;
- pontuação antes de citação em `modelo.(Panchal...)`;
- formulação truncada em `próteses e ortóteses. ou clínico`;
- contagem interna de resultados, de `quatro resultados principais` para `cinco resultados principais`;
- espaço duplicado em `ponto de partida  de dimensões`.

## 5. Resultado

A versão derivada reduziu a sobreposição entre capítulos sem remover conceitos estruturantes. A repetição aceitável de termos nucleares, como IA, parametrização, validação, OpenSCAD e lateralidade, foi preservada quando cada ocorrência cumpre uma função diferente: enquadramento, método, resultado, discussão ou limitação futura.

Após a correção do exportador local `tools/md_to_docx.py`, o DOCX derivado foi regenerado e validado com 22 tabelas Word, 20 imagens embebidas e zero parágrafos com tabelas Markdown brutas, incluindo a tabela `A.6.1 Campos`, onde se encontrava a linha `population`.
