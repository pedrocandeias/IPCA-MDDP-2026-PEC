# Lista de verificação manual de acessibilidade — WCAG 2.2, nível AA

Esta grelha operacionaliza as 12 verificações pendentes definidas em `2026-07-14_00-03-19_a11y-local/results/a11y-manual-checklist.json`. Deve ser preenchida durante a avaliação manual da plataforma. A sua conclusão não substitui uma auditoria integral de conformidade com as WCAG 2.2.

## Dados da sessão

| Campo | Registo |
|---|---|
| Avaliador | Pedro Candeias |
| Data e hora | 2 de julho de 2026, 16:02 |
| Endereço ou ambiente examinado | `http://localhost:3000` e `https://handfab.pedrocandeias.net/` |
| Versão, ramo e identificador da revisão | Não registados na sessão manual |
| Sistema operativo | Linux |
| Navegador e versão | Firefox 152.0.6 (64-bit) |
| Tecnologia de apoio utilizada | Orca; versão não registada |
| Resolução, ampliação e outras condições relevantes | Ampliação a 400% e largura equivalente a 320 píxeis CSS; resolução nativa não registada |

## Instruções de preenchimento

Em cada linha, assinalar apenas um resultado: **Conforme**, **Não conforme**, **Não aplicável** ou **Inconclusivo**. Sempre que o resultado seja «Não conforme», «Não aplicável» ou «Inconclusivo», justificar a classificação na última coluna. As evidências devem identificar o ecrã ou etapa, o elemento afectado e, quando disponível, o nome do ficheiro de imagem, vídeo ou registo técnico associado.

## Grelha de verificação

| ID | Critério WCAG 2.2 | Procedimento de verificação manual | Resultado | Evidência e observações |
|---|---|---|---|---|
| MAN-KEYBOARD | 2.1.1 — Teclado (*Keyboard*); 2.1.2 — Sem bloqueio do teclado (*No Keyboard Trap*) | Percorrer a autenticação, o painel principal, a selecção e configuração do modelo, a sugestão de IA, a geração da geometria e a exportação utilizando apenas o teclado. Confirmar que todas as operações essenciais são alcançáveis, accionáveis e reversíveis e que não existem bloqueios do foco. | Conforme |  |
| MAN-FOCUS-VISIBLE | 2.4.7 — Foco visível (*Focus Visible*); 2.4.11 — Foco não oculto (*Focus Not Obscured*) | Confirmar que o indicador de foco permanece sempre visível e não é ocultado por cabeçalhos fixos, janelas modais ou pelo visualizador tridimensional. | Conforme|  |
| MAN-FOCUS-ORDER | 2.4.3 — Ordem do foco (*Focus Order*) | Confirmar que a ordem de tabulação segue uma sequência lógica em cada ecrã e dentro das janelas modais, incluindo a autenticação e a exportação. | Não conforme | No percurso com o Orca, a ordenação dos campos não foi sempre suficientemente clara para orientar a sequência de interacção. |
| MAN-NAMES | 4.1.2 — Nome, função e valor (*Name, Role, Value*); 1.3.1 — Informação e relações (*Info and Relationships*) | Confirmar que cada controlo paramétrico e campo de formulário possui um nome acessível e um rótulo associado. Verificar com tecnologia de apoio se a função, o estado e o valor são anunciados correctamente. | Não conforme | No percurso com o Orca, algumas descrições de campos necessitavam de maior especificidade e clareza. |
| MAN-ERRORS | 3.3.1 — Identificação de erros (*Error Identification*); 3.3.3 — Sugestão de correcção (*Error Suggestion*) | Provocar erros de autenticação, perfil e exportação. Confirmar que são identificados por texto, e não apenas por cor, que ficam associados ao campo correspondente e que são acompanhados por instruções de correcção. | Conforme |  |
| MAN-STATUS | 4.1.3 — Mensagens de estado (*Status Messages*) | Confirmar que as mensagens dinâmicas de geração, aplicação de sugestões, erro e exportação são anunciadas pela tecnologia de apoio, por exemplo através de `role="status"` ou `aria-live`, sem deslocar indevidamente o foco. | Conforme |  |
| MAN-CONTRAST | 1.4.3 — Contraste mínimo (*Contrast — Minimum*); 1.4.1 — Utilização da cor (*Use of Color*) | Verificar contraste mínimo de 4,5:1 no texto e de 3:1 nos componentes e estados de foco. Confirmar que nenhuma informação, incluindo sucesso ou erro, depende exclusivamente da cor. | Conforme |  |
| MAN-REFLOW | 1.4.10 — Reformulação do conteúdo (*Reflow*); 1.4.4 — Redimensionamento do texto (*Resize Text*) | Examinar a interface com ampliação de 400% e largura equivalente a 320 píxeis CSS. Confirmar que não há perda de conteúdo ou funcionalidade essencial nem deslocamento bidireccional em conteúdo linear. | Não conforme | O ensaio foi executado. Com ampliação a 400% e largura equivalente a 320 píxeis CSS, a interface permaneceu apenas parcialmente utilizável. |
| MAN-TARGET | 2.5.8 — Dimensão mínima do alvo (*Target Size — Minimum*) | Confirmar que os elementos interactivos apresentam pelo menos 24 × 24 píxeis CSS ou espaçamento equivalente, incluindo amostras de cor, ícones de ajuda e caixas de selecção da exportação. | Conforme |  |
| MAN-AUTH | 3.3.8 — Autenticação acessível, nível mínimo (*Accessible Authentication — Minimum*) | Confirmar que a autenticação não exige um teste cognitivo sem alternativa e que permite colar a palavra-passe e utilizar gestores de palavras-passe. | Conforme |  |
| MAN-3D-ALT | 1.1.1 — Conteúdo não textual (*Non-text Content*); 1.3.1 — Informação e relações (*Info and Relationships*) | Confirmar que o visualizador tridimensional e os estados exclusivamente visuais possuem alternativa adequada. Verificar se os parâmetros, o estado e as operações essenciais podem ser compreendidos sem depender da imagem gerada. | Não conforme | No percurso com o Orca, o visualizador tridimensional não foi identificado como imagem e não foi anunciada qualquer alternativa textual. |
| MAN-SR | Percurso exploratório com leitor de ecrã | Executar o percurso completo com NVDA, VoiceOver ou Orca. Confirmar que nomes, funções, estados, instruções, erros e alterações são anunciados de forma compreensível em todas as etapas. | Não conforme | O percurso com o Orca revelou limitações na ordenação e na clareza das descrições dos campos. |

## Síntese da avaliação

| Campo | Registo |
|---|---|
| Número de verificações conformes | 7 |
| Número de verificações não conformes | 5 |
| Número de verificações não aplicáveis | 0 |
| Número de verificações inconclusivas | 0 |
| Principais problemas encontrados | Ordenação e descrição de campos insuficientemente claras no percurso com o Orca; ausência de identificação ou alternativa textual para o visualizador tridimensional; utilização apenas parcial da interface com ampliação a 400% e largura equivalente a 320 píxeis CSS. |
| Acções de correcção prioritárias | Rever a ordem de foco e de leitura; tornar os nomes e descrições dos campos mais específicos; fornecer uma alternativa textual ao visualizador tridimensional; corrigir a reformulação do conteúdo em ampliação elevada e repetir os ensaios com o Orca. |
| Localização das evidências associadas | Registo manual neste ficheiro; não foram indicados ficheiros autónomos de imagem, vídeo ou registo técnico. |

## Proveniência

- Protocolo de origem: `2026-07-14_00-03-19_a11y-local/results/a11y-manual-checklist.json`.
- O ficheiro DOCX com o mesmo nome é gerado a partir deste Markdown através do Pandoc 3.1.3 e do LibreOffice Writer 26.2.4.2.
- Método de geração: conversão temporária do Markdown para HTML com o Pandoc e exportação do HTML para DOCX através do filtro `Office Open XML Text` do LibreOffice Writer.
