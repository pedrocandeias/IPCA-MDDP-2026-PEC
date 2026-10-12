# Preparação da defesa do projeto

Versão de trabalho: 0.16. 12/10/2026.

Curso: **Mestrado em Design e Desenvolvimento de Produto, UPCA**. Arguente indicado pelo autor: **Bernardo Providência**.

Base corrente: `pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt`, confrontado com os registos dos suplementos. Referência de paginação: `a30759_pedro-candeias-projeto-mestrado-mdddp-ipca-v10060211.pdf`. A preparação inicial usou `…04102026-1955.odt`; a comparação dos parágrafos não encontrou diferenças textuais entre os dois ODT. Os registos anteriores de proveniência mantêm a fonte efetivamente consultada. Manuscrito preservado.

O autor indicou 20 minutos para a apresentação e pediu a preparação de uma versão de 30 minutos. O guião contém uma versão desenvolvida de 30 minutos e um percurso reduzido de 20 minutos. Os 30 minutos são uma opção de preparação, não uma alteração do tempo autorizado para a prova. A língua de trabalho é português; aguarda confirmação para a apresentação. Não foram presumidas regras institucionais adicionais.

## Documentos

- [Notas pessoais para cada diapositivo](apresentacao/guiao_falado.odt): guião oral autónomo para os 25 diapositivos, também disponível em [PDF](apresentacao/guiao_falado.pdf). Inclui uma proposta de fala em primeira pessoa e apontamentos para desenvolver a explicação, com lembretes pessoais que não se leem ao júri. O texto está também nas notas do PPTX; este guião autónomo encontra-se na subpasta da apresentação e não integra o caderno de seis partes.
- [Apresentação da defesa](apresentacao/README.md): versão gráfica revista, em [PPTX editável](apresentacao/apresentacao_defesa.pptx) e [PDF](apresentacao/apresentacao_defesa.pdf), com 17 diapositivos principais e oito de apoio. O PPTX inclui notas de fala e metas para 20 minutos e para treino de 30 minutos.
- [Caderno completo de preparação em ODT](preparacao_defesa_bernardo_providencia.odt): reúne os seis Markdown desta pasta, incluindo este guia, o guião de apresentação, a contextualização e o perfil do arguente, as 47 perguntas com respostas simples e as evidências e pontos a alinhar. As ligações entre estas partes permitem navegar dentro do documento.
- [Guião e estrutura de apresentação](guiao_apresentacao.md): 17 blocos, tempos, mensagem central, conteúdos e propostas visuais; inclui abertura, fecho e percurso de demonstração.
- [Perguntas e respostas de treino para o júri](perguntas_juri.md), disponíveis em [PDF autónomo](perguntas_juri.pdf) e [ODT editável](perguntas_juri.odt): 47 perguntas com respostas em primeira pessoa e lembretes pessoais para consulta e preparação, na versão 0.7. Inclui 21 questões ligadas às publicações de Bernardo Providência. As respostas 7, 9 e 47 têm decisões pessoais do autor por confirmar.
- [Evidências e pontos a alinhar](evidencias_e_pontos_a_alinhar.md): relação entre afirmações, resultados, fontes e limites.
- [Manifesto das fontes](fontes.json): hashes dos ficheiros examinados e verificações dos CSV.
- [Contextualização académica do arguente](contexto_arguente.md): fontes públicas e temas para preparar a discussão.
- [Notas pessoais sobre Bernardo Providência e as suas publicações](perfil_bernardo_providencia.md): oito trabalhos de 2012–2025 e complemento ORCID com estudo adicional de esgrima; métodos, limites e implicações para a defesa, com níveis de acesso declarados.

## Argumento de trabalho

O projeto investigou como organizar e verificar a passagem entre referências antropométricas, parâmetros editáveis, geometria digital e peças físicas. O protótipo HandFab tornou explícitas decisões de configuração e revelou limites específicos dos modelos, com apoio de IA sujeito a regras e revisão humana.

A defesa deverá apoiar este argumento em dois casos concretos de decisão, num percurso visual da plataforma e nos resultados da comparação geométrica e material. O eixo disciplinar é o design e desenvolvimento de produto: requisito, decisão, efeito na forma ou no uso previsto, materialização e conhecimento obtido. A revisão bibliográfica fornece a fundamentação; a apresentação deve concentrar-se nas decisões do projeto e na aprendizagem obtida ao verificar os seus efeitos. Os detalhes de implementação são apresentados quando explicam essas decisões.

## Estado da preparação

- Estrutura narrativa e distribuição temporal preparadas.
- Perguntas de investigação e limites extraídos do manuscrito.
- Confirmadas 72 linhas de comparação dimensional e 12 casos da Série B nos CSV.
- Identificada divergência sobre a montagem Phoenix entre algumas conclusões e o registo de bancada; ver documento de evidências.
- Ainda por definir: data, restantes elementos do júri, orientações específicas, língua definitiva e condições para demonstração ou apresentação de peças.
- Primeira versão gráfica produzida, com fotografias, capturas da plataforma, gráfico calculado a partir dos CSV e notas em todos os diapositivos.
- Texto oral completo produzido: 2109 palavras no percurso principal e 844 nos acrescentos opcionais, além das falas dos diapositivos de apoio.
- Ainda por realizar: revisão da apresentação com o autor, eventual gravação de demonstração e ensaio cronometrado. Os 20 e 30 minutos reservam tempo para pausas e explicação das imagens; são metas que precisam de ser ajustadas ao ritmo do autor.

## Método de preparação

Leitura direta do conteúdo do ODT e conferência dos CSV do Suplemento 4. Os guiões são propostas de comunicação, não relatos de novos ensaios. Não foram executadas novas avaliações da plataforma nem modificados resultados, imagens, citações ou o manuscrito.

### Exportação do caderno ODT

Gerar novamente a partir da raiz do projeto com `python3 docs/defesa/exportar_odt.py`. As fontes autoritativas são os seis Markdown desta pasta, reunidos pela seguinte ordem: `README.md`, `guiao_apresentacao.md`, `contexto_arguente.md`, `perfil_bernardo_providencia.md`, `perguntas_juri.md` e `evidencias_e_pontos_a_alinhar.md`. O script confere a inclusão de todos os Markdown e exporta através do Pandoc, transferindo os estilos do template IPCA convertido e arquivado em `docs/revisoes/manuscrito/estilos_template_ipca_2026_10_05/projeto-mestrado-template-ipca.odt`. Reutiliza as funções de apresentação dos suplementos, sem alterar o template ou o manuscrito. A grelha das tabelas é definida para este caderno, pois o template não contém tabelas.

O ODT mantém as hiperligações externas e locais; as remissões entre os seis documentos reunidos passam a ligações internas. Cada parte seguinte começa em nova página. Os CSV, o manifesto JSON e os restantes ficheiros de apoio continuam acessíveis por ligação, sem serem transcritos. A verificação abrange a presença das seis partes, as 47 perguntas e respostas, a integridade XML/ZIP e a apresentação através de exportação temporária para PDF no LibreOffice, com perfil isolado. A regeneração substitui o ODT; as revisões devem ser feitas nas fontes Markdown.

### Exportação das perguntas do júri

A fonte é `perguntas_juri.md`. Depois de gerar o caderno, executar `python3 docs/defesa/exportar_perguntas_juri.py` na raiz do projeto. O script usa Pandoc e os estilos do caderno para produzir `perguntas_juri.odt`, com as 47 perguntas, respostas e notas de apoio. Os títulos e a etiqueta de resposta mantêm-se junto do texto seguinte.

Para atualizar ambos os PDF, converter os ODT com LibreOffice, usando um perfil temporário isolado:

```bash
libreoffice -env:UserInstallation=file:///tmp/mestrado_defesa_pdf --headless --convert-to pdf --outdir docs/defesa docs/defesa/perguntas_juri.odt docs/defesa/preparacao_defesa_bernardo_providencia.odt
```

As alterações de conteúdo devem ser feitas no Markdown antes de regenerar os documentos.
