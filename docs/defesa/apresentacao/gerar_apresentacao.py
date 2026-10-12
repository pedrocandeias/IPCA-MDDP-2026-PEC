#!/usr/bin/env python3
"""Gera PPTX, gráfico e manifesto a partir das fontes locais da defesa."""
from pathlib import Path
import csv, json, hashlib, sys, shutil
from collections import defaultdict
try:
    import pptx
except ImportError:
    sys.path.insert(0, '/tmp/defesa_pptx_deps')
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.xmlchemy import OxmlElement
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from exportar_guiao_falado import ler_falas

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
ASSETS=HERE/'assets'
CSV=ROOT/'suplementos/04_preparacao_impressao_prototipos/registos/comparacao_dimensional_72_medicoes.csv'
ROWS=list(csv.DictReader(CSV.open()))
assert len(ROWS)==72 and all(r['numero_leituras']=='1' for r in ROWS)
PHOTO=ROOT/'suplementos/04_preparacao_impressao_prototipos/fotografias_reduzidas/teste-impressao-phoenix-15-anos-13221117.jpg'
shutil.copy2(PHOTO,ASSETS/'phoenix_montagem.jpg')
BG='F6F5F0'; INK='193536'; TEAL='007C78'; MUTED='566B6A'; LIGHT='E3ECE8'; WHITE='FFFFFF'; ORANGE='AD542D'
FONT='Liberation Sans'
prs=Presentation();prs.slide_width=Inches(13.333333);prs.slide_height=Inches(7.5)
prs.core_properties.title='HandFab: Defesa do projeto de mestrado'
prs.core_properties.subject='Design e Desenvolvimento de Produto · UPCA'
prs.core_properties.author='Pedro Miguel Candeias da Silva'
records=[]
t20=[30, 60, 60, 90, 60, 75, 75, 60, 75, 90, 75, 60, 90, 105, 60, 105, 30]
t30=[60, 90, 90, 120, 90, 90, 90, 90, 90, 120, 120, 120, 120, 150, 120, 180, 60]
assert sum(t20)==1200 and sum(t30)==1800

def rgb(c):return RGBColor.from_string(c)
def box(s,x,y,w,h,fill=LIGHT,line=None):
    sh=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill)
    if line:sh.line.color.rgb=rgb(line)
    else:sh.line.fill.background()
    sh._element.spPr.append(OxmlElement("a:effectLst"))
    return sh

def text(s,x,y,w,h,value,size=24,color=INK,bold=False,font=FONT,align=None):
    sh=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=sh.text_frame
    tf.clear();tf.word_wrap=True
    tf.margin_left=tf.margin_right=Inches(0);tf.margin_top=tf.margin_bottom=Inches(.025)
    for i,line in enumerate(value.split('\n')):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.text=line;p.font.name=font;p.font.size=Pt(size);p.font.bold=bold;p.font.color.rgb=rgb(color)
        p.space_after=Pt(7);p.line_spacing=1.1
        if align is not None:p.alignment=align
    return sh

def picture(s,path,x,y,w,h,bg=WHITE):
    box(s,x,y,w,h,bg)
    with Image.open(path) as im:iw,ih=im.size
    scale=min(w/iw,h/ih);pw,ph=iw*scale,ih*scale
    s.shapes.add_picture(str(path),Inches(x+(w-pw)/2),Inches(y+(h-ph)/2),width=Inches(pw),height=Inches(ph))

def slide(title,kicker,source,dark=False):
    i=len(records)+1;s=prs.slides.add_slide(prs.slide_layouts[6]);s.background.fill.solid();s.background.fill.fore_color.rgb=rgb(INK if dark else BG)
    fg=WHITE if dark else INK
    box(s,.45,.45,.12,.3,TEAL)
    text(s,.7,.4,11.8,.3,kicker.upper(),11,TEAL if not dark else '8DCCC1',True)
    text(s,.7,.94,11.9,1.0,title,32,fg,True)
    text(s,.7,6.96,11.55,.26,source,10,'B5CBC6' if dark else MUTED)
    text(s,12.25,6.93,.4,.3,str(i).zfill(2),11,fg,True,align=PP_ALIGN.RIGHT)
    records.append({'numero':i,'titulo':title,'principal':i<=17,'tempo_20_segundos':t20[i-1] if i<=17 else None,'tempo_30_segundos':t30[i-1] if i<=17 else None,'fonte':source})
    return s

def card(s,x,y,w,num,title,body,h=3.4):
    box(s,x,y,w,h,WHITE)
    text(s,x+.22,y+.18,w-.44,.48,num,28,TEAL,True)
    text(s,x+.22,y+.87,w-.44,.85,title,23,INK,True)
    text(s,x+.22,y+1.8,w-.44,h-1.95,body,19,MUTED)

def row(s,y,a,b,c=None):
    box(s,.7,y,11.9,.79,WHITE)
    text(s,.95,y+.1,2.65,.58,a,20,TEAL,True)
    text(s,3.8,y+.1,4.15 if c else 8.25,.6,b,18)
    if c:text(s,8.2,y+.1,4.1,.6,c,18,MUTED)

# 01
s=slide('Da medida à peça física', 'Mestrado em Design e Desenvolvimento de Produto · UPCA', 'Imagem: produção do autor · Suplemento 4 · Phoenix, observação de montagem em bancada.')
text(s,.7,2.04,6.15,2.7,'Integração do design e da inteligência artificial em processos paramétricos para o desenvolvimento de próteses de membros superiores em impressão 3D',23,INK,True)
text(s,.7,4.95,6.1,.65,'Pedro Miguel Candeias da Silva',21,INK,True)
text(s,.7,5.63,6.1,.9,'Orientador: Doutor Demétrio Ferreira Matos\nProjeto de mestrado · 2026',17,MUTED)
s.shapes.add_picture(str(ASSETS/'upca_logo_oficial.png'), Inches(9.7), Inches(.45), width=Inches(2.9))
picture(s,ASSETS/'phoenix_montagem.jpg',7.1,2.02,5.5,3.76)
text(s,7.12,5.94,5.4,.52,'HandFab: da configuração à peça',18,TEAL,True)
# 02
s=slide('Como passar de uma medida a uma peça?', 'Problema de design', 'Contexto: Manero et al. (2019); Cabibihan et al. (2021) · Problema específico: manuscrito, 1.2 e 4.3-4.4.')
for x,num,t,b in [(.7,'01','Medida','O valor de referência'),(3.75,'02','Parâmetro','A variável do modelo'),(6.8,'03','Regra','Como a forma muda'),(9.85,'04','Peça','O resultado a verificar')]:card(s,x,2.25,2.78,num,t,b,3.0)
text(s,.9,5.76,11.5,.72,'O nome do parâmetro não garante a dimensão resultante.',27,INK,True)
# 03
s=slide('Perguntas de investigação e âmbito da avaliação', 'Perguntas e âmbito', 'Síntese das perguntas aprovadas · Formulações integrais no diapositivo 18 · Tabela 31.')
card(s,.7,2.05,3.8,'P1','Configuração e controlo','Como apoiar escolhas sobre o modelo?')
card(s,4.75,2.05,3.8,'P2','Avaliação e reprodução','Como examinar o processo e os resultados?')
card(s,8.8,2.05,3.8,'P3','Requisitos e experiência','Como responder às necessidades das pessoas?')
text(s,.9,5.95,11.5,.52,'Âmbito realizado: verificação técnica e dimensional, sem participantes.',22,TEAL,True)
# Objetivos explícitos, sintetizados sem eliminar os sete pontos do manuscrito.
s=slide('Objetivo geral e objetivos específicos', 'Objetivos da investigação', 'Síntese da secção 1.3 do manuscrito · Sete objetivos específicos, com o âmbito original preservado.')
box(s,.7,1.92,11.9,1.62,LIGHT)
text(s,.92,2.04,11.4,.26,'OBJETIVO GERAL',12,TEAL,True)
text(s,.92,2.35,11.4,1.12,'Produzir conhecimento através da prática de design, desenvolvendo e avaliando tecnicamente um sistema paramétrico apoiado por IA para a configuração preliminar de modelos de mão protésica destinados ao fabrico aditivo.',20,INK,True)
text(s,.92,3.64,11.4,.28,'OBJETIVOS ESPECÍFICOS',12,TEAL,True)
objectives=[
 'Analisar como o design traduz requisitos humanos em decisões de projeto e fabrico.',
 'Organizar dados antropométricos, preservando a sua caracterização e limitações.',
 'Adaptar modelos abertos de mão a uma estrutura paramétrica explícita em OpenSCAD.',
 'Integrar o percurso na web, com visualização e gestão de versões, até à impressão.',
 'Delimitar a IA à sugestão inicial, distinguindo regras geométricas e decisões humanas.',
 'Avaliar a coerência entre dados, parâmetros, geometria digital e protótipos físicos.',
 'Definir condições para avaliação clínica posterior, incluindo função e utilização.',
]
for i,objective in enumerate(objectives):
 x=.92 if i<4 else 7.02; y=4.12+(i if i<4 else i-4)*.66
 text(s,x,y,.42,.34,f'{i+1:02d}',16,TEAL,True)
 text(s,x+.48,y,5.12,.64,objective,17)

# Referências que organizam o argumento
s=slide('Como a literatura orienta o projeto', 'Fundamentação e seleção', 'Referências já mobilizadas no manuscrito · Seleção para esta exposição pela função no argumento.')
items=[('Cross (1982)','Conhecimento de design','Aprendizagem a partir das decisões de projeto'),
       ('Frayling (1994); Zimmerman et al. (2007)','Investigação através do projeto','Análise documentada do artefacto'),
       ('Fischer et al. (2004)','Meta-design e modificação','Escolhas disponíveis no HandFab'),
       ('Manero et al. (2019); Cabibihan et al. (2021)','Próteses impressas em 3D','Contexto e necessidade de avaliação')]
for i,(a,b,c) in enumerate(items):
 y=2.12+i*.94;box(s,.7,y,11.9,.84,WHITE)
 text(s,.91,y+.12,3.8,.6,a,19,TEAL,True)
 text(s,4.85,y+.1,3.4,.62,b,18,INK,True)
 text(s,8.4,y+.1,3.95,.62,c,18,MUTED)
text(s,.94,6.2,11.4,.5,'Critério: utilidade para justificar decisões e interpretar os resultados.',21,INK,True)

# 04
s=slide('Investigar através do desenvolvimento do protótipo', 'Investigar através do projeto', 'Frayling (1994); Zimmerman et al. (2007) · Design Council (2007): organização do processo · Tabela 4.')
for i,(t,b) in enumerate([('Observar','A geometria não acompanha a escolha.'),('Decidir','Rever a relação entre valor e forma.'),('Alterar','Aplicar a regra no ponto adequado.'),('Verificar','Examinar novamente o resultado.')]):card(s,.7+i*3.05,2.1,2.78,str(i+1).zfill(2),t,b,3.55)
text(s,.9,6.05,11.4,.5,'O contributo depende de explicar a decisão e a sua consequência.',23,TEAL,True)
# 05
s=slide('HandFab: um percurso com decisões explícitas', 'Artefacto de investigação', 'Síntese do autor, Figuras 17-18 · Fischer et al. (2004): enquadramento conceptual da modificação.')
for i,(a,b) in enumerate([('Referência','Dados ou descrição'),('Revisão','Valores editáveis'),('Geometria','Regras do modelo'),('Exportação','Preparar o fabrico')]):card(s,.7+i*3.05,2.4,2.78,str(i+1).zfill(2),a,b,2.7)
box(s,3.8,1.97,2.67,.39,TEAL);text(s,3.92,2.0,2.4,.28,'IA: sugestão inicial',13,WHITE,True)
text(s,.9,5.67,11.4,.93,'As decisões de design definem as variações disponíveis e as condições de revisão.',25,INK,True)
# Fontes antropométricas
s=slide('Fontes antropométricas e critérios de utilização', 'Antropometria · Fontes', 'Gordon et al. (1989; 2014) · TU Delft, DINED (s.d.) · ISO 7250-1:2017 · Referências no diapositivo 25.')
card(s,.7,2.1,3.8,'Estudos','Gordon et al.','ANSUR 1988 / ANSUR II.\nPopulações e levantamentos distintos.',3.65)
card(s,4.75,2.1,3.8,'Base','TU Delft · DINED','Conjuntos utilizados:\nkima1993 · geron1998\ndined2004',3.65)
card(s,8.8,2.1,3.8,'Definições','ISO 7250-1:2017','Medidas do corpo e pontos anatómicos de referência.',3.65)
text(s,.94,6.15,11.4,.53,'Interpretar cada valor: população · idade · sexo · medida · unidade · estatística',21,TEAL,True)
# Base local e perfis
s=slide('Da base consolidada aos perfis do HandFab', 'Antropometria · Trabalho realizado', 'Fontes: manuscrito, 4.2; Suplemento 1 · Os números indicam registos, não participantes.')
card(s,.7,2.08,3.8,'01','Estudos originais','Medições e estatísticas publicadas pelos investigadores.',3.65)
card(s,4.75,2.08,3.8,'02','Base consolidada','Seleção e organização local. Uma linha por indicador, com origem identificada.',3.65)
card(s,8.8,2.08,3.8,'03','100 perfis','97 importados em lote\n2 por CSV\n1 criado manualmente',3.65)
text(s,.93,5.96,11.4,.42,'Exemplo: média + desvio-padrão da mesma medida → duas linhas estatísticas.',20,TEAL,True)
text(s,.93,6.45,11.4,.35,'A contagem de linhas não equivale à contagem de perfis ou de pessoas.',19,INK,True)
# 07
s=slide('Cada modelo exige regras próprias', 'Dois casos de projeto', 'Fonte: 4.4, 8.3, Tabelas 28-29 e Anexo C · Esquema explicativo, não comparação visual histórica.')
card(s,.7,2.03,5.8,'A','Paraglider Hand','Problema: a palma mantinha a escala da biblioteca.\nDecisão: corrigir a aplicação da escala.',3.5)
card(s,6.8,2.03,5.8,'B','UnLimbited Phoenix','Limite: largura mínima de cerca de 82 mm.\nConsequência: nem todos os pedidos são satisfeitos.',3.5)
text(s,.95,5.97,11.4,.57,'Configurar também exige reconhecer quando um modelo não responde ao pedido.',24,TEAL,True)
# 08
s=slide('A IA propõe um ponto de partida', 'Sugestão e controlo', 'Fonte: capítulo 6 e 8.2 · Cinco execuções no primeiro conjunto de ensaios reais.')
for i,(title,body) in enumerate([('Pedido','Descrição para a sugestão de IA.'),('Proposta','Valores iniciais para parâmetros conhecidos.'),('Revisão','A pessoa pode corrigir ou rejeitar os valores.'),('Geometria','Regras do modelo aplicadas aos valores aceites.')]):
 card(s,.7+i*3.05,2.14,2.78,str(i+1).zfill(2),title,body,3.55)
text(s,.95,6.0,11.3,.62,'A lateralidade segue uma regra explícita. A adequação anatómica requer avaliação.',21,TEAL,True)
# 09
s=slide('Configuração e pré-visualização no HandFab', 'Percurso ilustrado na plataforma', 'Capturas do manuscrito, Figura 22 · Sequência ilustrativa, sem nova execução de IA.')
picture(s,ASSETS/'figura_22_1.png',.7,2.03,5.78,3.78)
picture(s,ASSETS/'figura_22_3.png',6.82,2.03,5.78,3.78)
text(s,.95,6.03,5.3,.44,'Selecionar o modelo',23,INK,True)
text(s,7.05,6.03,5.3,.44,'Rever valores e gerar',23,INK,True)
# 10
s=slide('A avaliação acompanhou etapas diferentes', 'Método e evidência', 'Fonte: capítulo 8 e Anexos B a D · Os conjuntos respondem a perguntas distintas.')
for y,a,b,c in [(2.1,'Plataforma','Funcionamento e falhas','Registos de ensaio'),(3.01,'Sugestões de IA','Formato e valores propostos','Respostas documentadas'),(3.92,'Geometria','Propagação e exportação','Malhas por modelo e perfil'),(4.83,'Peças físicas','Preparação e dimensões','CSV e registos fotográficos')]:row(s,y,a,b,c)
text(s,.95,6.02,11.3,.43,'4 projetos na Série A · 12 casos na Série B · 72 medições físicas',22,TEAL,True)
# Chart: ranges across all three axes and four profiles, no inference beyond observed values.
fig,ax=plt.subplots(figsize=(10.7,4.5));fig.patch.set_facecolor('#'+BG);ax.set_facecolor('#'+BG)
groups=[]
for mi,m in enumerate(['Flexy Beast','Paraglider Hand','UnLimbited Phoenix']):
 for mat,color,offset in [('PLA','#'+TEAL,.13),('PETG','#'+ORANGE,-.13)]:
  vals=[float(r['desvio_malha_peca_mm']) for r in ROWS if r['modelo']==m and r['material']==mat]
  assert len(vals)==12
  y=2-mi+offset;lo,hi=min(vals),max(vals)
  ax.plot([lo,hi],[y,y],color=color,lw=5,solid_capstyle='round',label=mat if mi==0 else None)
  ax.scatter([lo,hi],[y,y],s=42,color=color,zorder=3)
  groups.append({'modelo':m,'material':mat,'n':len(vals),'min_mm':lo,'max_mm':hi})
ax.set_yticks([2,1,0],['Flexy Beast','Paraglider Hand','UnLimbited Phoenix'],fontsize=16)
ax.set_xlim(-.6,.025);ax.set_ylim(-.55,2.6);ax.axvline(0,color='#'+MUTED,lw=1)
ax.set_xticks([-.6,-.4,-.2,0],['−0,6','−0,4','−0,2','0']);ax.tick_params(axis='x',labelsize=15);ax.tick_params(axis='y',length=0,pad=12)
ax.set_xlabel('Dimensão física − dimensão da malha (mm)',fontsize=16,labelpad=12)
ax.spines[['top','right','left']].set_visible(False);ax.spines['bottom'].set_color('#'+MUTED)
ax.grid(axis='x',alpha=.2);ax.legend(loc='upper left',bbox_to_anchor=(0,1.18),frameon=False,ncol=2,fontsize=15)
fig.subplots_adjust(left=.29,right=.97,top=.81,bottom=.2)
fig.savefig(ASSETS/'desvios_dimensionais.png',dpi=190);fig.savefig(ASSETS/'desvios_dimensionais.svg');plt.close(fig)
(HERE/'resumo_dimensional.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n')
# 11
s=slide('Peça e malha: diferenças medidas, com limites', 'Resultados dimensionais', 'Fonte: Suplemento 4, comparacao_dimensional_72_medicoes.csv · Gráfico calculado a partir dos registos.')
picture(s,ASSETS/'desvios_dimensionais.png',.7,1.95,11.9,4.26,bg=BG)
text(s,.92,6.25,11.5,.47,'Amplitude por grupo, calculada com uma leitura por combinação.',21,TEAL,True)
# 12
s=slide('As falhas também definem o próximo passo', 'Limites encontrados', 'Fonte: 8.1.2 e Anexo B · Ensaios de recuperação e auditoria de acessibilidade.')
card(s,.7,2.08,5.8,'Controlo','Valores fora do limite','Um valor simulado acima do limite chegou ao estado interno.',3.7)
card(s,6.8,2.08,5.8,'Acessibilidade','Barreiras no percurso','5 de 12 itens falharam na verificação manual.',3.7)
text(s,.95,6.13,11.3,.43,'Problemas identificados orientam revisões concretas do sistema.',23,TEAL,True)
# 13
s=slide('O contributo para a configuração do produto', 'Resposta às perguntas', 'Síntese da Tabela 31 e de 9.1-9.4 · Cross (1982): enquadramento do conhecimento de design.')
text(s,.94,2.0,2.55,.35,'EIXO',12,TEAL,True);text(s,3.8,2.0,4.0,.35,'EVIDÊNCIA OBTIDA',12,TEAL,True);text(s,8.2,2.0,4.1,.35,'POR AVALIAR',12,ORANGE,True)
row(s,2.65,'Configuração','Valores editáveis e revisão','Conforto e adequação individual')
row(s,3.7,'Avaliação','Verificação técnica e dimensional','Usabilidade e durabilidade')
row(s,4.75,'Requisitos','Regras e escolhas disponíveis','Aceitação e autonomia')
text(s,.94,6.0,11.2,.56,'Explicar como cada escolha de configuração afeta a forma.',26,INK,True)
# 14
s=slide('As regras de cada modelo condicionam o resultado', 'Conclusão', 'Projeto HandFab · Pedro Miguel Candeias da Silva · Mestrado em Design e Desenvolvimento de Produto.', dark=True)
picture(s,ASSETS/'figura_28_1.jpg',.7,2.18,11.9,2.62,bg=INK)
text(s,.9,5.29,11.3,.95,'Próximo passo\nAvaliar decisões e tarefas com as pessoas a quem o processo se destina.',25,WHITE,True)
# 15
s=slide('Perguntas de investigação aprovadas', 'Apoio · Formulações integrais', 'Fonte: manuscrito, 9.1. Diapositivo fora do percurso principal de 20 minutos.')
qs=['Como o design de produto, métodos paramétricos e inteligência artificial podem melhorar a personalização, o conforto e a adequação funcional de próteses, mantendo a acessibilidade e o controlo sobre as decisões de projeto?', 'Quais metodologias e ferramentas validam a eficácia, a usabilidade, a durabilidade e a possibilidade de reproduzir os resultados de próteses impressas em 3D?', 'Como é que o design industrial concilia requisitos anatómicos, funcionais, ergonómicos, estéticos e simbólicos, promovendo a aceitação, a dignidade e a autonomia?']
for i,q in enumerate(qs):
 text(s,.78,2.03+i*1.47,.65,.5,f'P{i+1}',23,TEAL,True);text(s,1.62,2.03+i*1.47,10.8,1.3,q,22)
# 16
s=slide('Os números representam conjuntos diferentes', 'Apoio · Desenho da avaliação', 'Fonte: capítulo 8, Anexo D e CSV das Séries A/B e medições físicas.')
card(s,.7,2.08,3.8,'4','Projetos da Série A','Condições diferentes. Comparação direta entre equipamentos limitada.')
card(s,4.75,2.08,3.8,'12','Casos da Série B','3 modelos × 4 perfis. Preparação digital concluída, com avisos.')
card(s,8.8,2.08,3.8,'72','Medições físicas','3 modelos × 4 perfis × 3 eixos × 2 materiais. Uma leitura por combinação.')
text(s,.96,6.08,11.2,.45,'Perfis de ensaio: 8, 15, 28 e 70 anos. Não correspondem a participantes.',21,TEAL,True)
# 17
s=slide('Valores registados: amplitude por grupo', 'Apoio · Comparação dimensional', 'Fonte: comparacao_dimensional_72_medicoes.csv · Diferença = dimensão física − dimensão da malha.')
text(s,.9,1.93,4,.35,'MODELO / MATERIAL',13,TEAL,True);text(s,6,1.93,3,.35,'MÍNIMO (mm)',13,TEAL,True);text(s,9,1.93,3,.35,'MÁXIMO (mm)',13,TEAL,True)
for i,g in enumerate(groups):
 y=2.5+i*.61;box(s,.7,y,11.9,.54,WHITE)
 text(s,.95,y+.04,5,.42,g['modelo']+' · '+g['material'],18)
 text(s,6,y+.04,2.5,.42,f"{g['min_mm']:.3f}".replace('.',','),19,TEAL,True)
 text(s,9,y+.04,2.5,.42,f"{g['max_mm']:.3f}".replace('.',','),19,TEAL,True)
# 18
s=slide('Phoenix: uma montagem observada em bancada', 'Apoio · Alcance da evidência física', 'Fonte: Figura 29 e montagem_phoenix_15_anos.csv · Espécime PHX-TEEN15-MONT-001.')
picture(s,ASSETS/'figura_29_1.jpg',.7,2.01,8.0,3.9)
text(s,9.03,2.18,3.5,1.3,'1 espécime\nPLA · perfil de 15 anos',24,TEAL,True)
text(s,9.03,3.82,3.5,2.33,'Movimento manual observado.\nElásticos substituídos.\nNúmero de ciclos não registado.',21)
text(s,.94,6.25,11.4,.4,'Observação de montagem e movimento; sem avaliação em utilização protésica.',21,TEAL,True)
# 19
s=slide('Repetição e acessibilidade: resultados delimitados', 'Apoio · Verificações da plataforma', 'Fonte: 8.1.2 e Anexo B. Repetições idênticas dentro da configuração examinada.')
card(s,.7,2.14,5.8,'7 / 5 / 5','Exportações concluídas','Flexy Beast / Paraglider / Phoenix. Objetivo inicial: 10 por modelo.',3.6)
card(s,6.8,2.14,5.8,'7 conformes · 5 falhas','Verificação manual','12 itens. A auditoria identificou barreiras a corrigir.',3.6)
# 20
s=slide('Dois usos de inteligência artificial', 'Apoio · Transparência e responsabilidade', 'Fonte: declaração inicial do manuscrito e capítulo 6.')
card(s,.7,2.14,5.8,'Na elaboração','Ferramentas de apoio','Pesquisa e organização, texto, código e ficheiros complementares.',3.6)
card(s,6.8,2.14,5.8,'No HandFab','Objeto de investigação','Sugestões iniciais de parâmetros, sujeitas a revisão.',3.6)
text(s,.94,5.99,11.3,.7,'O autor assume a responsabilidade pelo conteúdo e pelas decisões do projeto.',21,TEAL,True)
# Referências de apoio: design
s=slide('Referências: design e investigação', 'Apoio · Referências', 'Seleção da bibliografia do manuscrito · A ligação ao HandFab é uma interpretação aplicada ao projeto.')
refs=[('Cross (1982)','Designerly ways of knowing. Design Studies, 3(4), 221-227. DOI: 10.1016/0142-694X(82)90040-0'),
('Fischer et al. (2004)','Meta-design: A manifesto for end-user development. Communications of the ACM, 47(9), 33-37. DOI: 10.1145/1015864.1015884'),
('Frayling (1994)','Research in art and design. Royal College of Art Research Papers, 1(1).'),
('Zimmerman et al. (2007)','Research through design as a method for interaction design research in HCI. CHI, 493-502. DOI: 10.1145/1240624.1240704'),
('Design Council (2007)','Eleven lessons: Managing design in eleven global brands: A study of the design process.')]
for i,(a,b) in enumerate(refs):
 y=2.02+i*.89
 text(s,.8,y,3.05,.7,a,18,TEAL,True);text(s,4.03,y,8.48,.78,b,17)
# Referências de apoio: domínio e dados
s=slide('Referências: próteses e antropometria', 'Apoio · Referências', 'Dados e atribuições: Suplemento 1 · Ensaios do projeto: Suplementos 2-4 · Obras distintas com funções próprias.')
refs=[('Manero et al. (2019)','Implementation of 3D printing technology in the field of prosthetics: Past, present, and future. DOI: 10.3390/ijerph16091641'),
('Cabibihan et al. (2021)','Suitability of the openly accessible 3D printed prosthetic hands for war-wounded children. DOI: 10.3389/frobt.2020.594196'),
('Gordon et al. (1989; 2014)','1988 / 2012 anthropometric survey of U.S. Army personnel: Methods and summary statistics. Relatórios distintos: ANSUR 1988 / ANSUR II.'),
('TU Delft · DINED (s.d.)','DINED: 1D anthropometric database [Base de dados]. Consulta: 02/05/2026. https://dined.io.tudelft.nl/en/database/tool'),
('ISO (2017)','ISO 7250-1:2017. Basic human body measurements for technological design: Part 1: Body measurement definitions and landmarks (2.ª ed.).')]
for i,(a,b) in enumerate(refs):
 y=2.02+i*.89
 text(s,.8,y,3.05,.7,a,18,TEAL,True);text(s,4.03,y,8.48,.78,b,17)

falas=ler_falas()
assert len(falas)==len(records)==len(prs.slides)==25
for s, record in zip(prs.slides, records):
    n=record['numero']; f=falas[n]
    assert record['titulo']==f['titulo'], (n, record['titulo'], f['titulo'])
    record.update(f)
    tempo=(f"{t20[n-1]//60}:{t20[n-1]%60:02d} no percurso principal; "
           f"{t30[n-1]//60}:{t30[n-1]%60:02d} no treino desenvolvido") if n<=17 else 'apoio à discussão'
    s.notes_slide.notes_text_frame.text=(
        f'Tempo para me orientar: {tempo}. Confirmar no ensaio.\n\n'
        f'O QUE QUERO DIZER\n{f["fala"]}\n\n'
        + (f'SE PRECISAR DE DESENVOLVER\n{f["aprofundamento"]}\n\n' if f['aprofundamento'] else '')
        + f'LEMBRAR-ME (não ler ao júri)\n{f["indicacao"]}\n\nFONTES PARA CONSULTA\n{record["fonte"]}')

out=HERE/'apresentacao_defesa.pptx';prs.save(out)
(HERE/'diapositivos.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
sources=[ASSETS/'upca_logo_oficial.svg',ASSETS/'upca_logo_oficial.png',ROOT/'pedro-candeias-projeto-mestrado-mdddp-ipca-2026-revisto_v1_06102026-0210.odt',ROOT/'a30759_pedro-candeias-projeto-mestrado-mdddp-ipca-v10060211.pdf',ROOT/'docs/defesa/guiao_apresentacao.md',HERE/'guiao_falado.md',ROOT/'suplementos/01_dados_antropometricos/descricao_do_suplemento_1.md',ROOT/'suplementos/01_dados_antropometricos/multi_population_hand.csv',CSV,PHOTO,ROOT/'suplementos/04_preparacao_impressao_prototipos/registos/resultados_serie_b.csv',ROOT/'suplementos/04_preparacao_impressao_prototipos/registos/montagem_phoenix_15_anos.csv']
manifest={'data':'2026-10-12','estado':'Versão 1.4.2: notas pessoais para leitura e ensaio; sujeita a ensaio','formato':'16:9','diapositivos_principais':17,'apoio':8,'tempo_principal_segundos':sum(t20),'tempo_treino_segundos':sum(t30),'fontes':[{'caminho':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],'fotografias':'Imagens extraídas do ODT e cópia de fotografia do Suplemento 4, sem alteração do conteúdo. Redimensionamento proporcional na apresentação.','grafico':'Amplitude min/max de desvio_malha_peca_mm por modelo/material; 12 valores por grupo; sem inferência estatística.','pendencias':['Confirmar condições e data da defesa.','Confirmar operador principal previsto e razões para ausência de participantes.','Alinhar as conclusões do manuscrito com o registo de montagem Phoenix.','Conferir a entrada bibliográfica incompleta de Frayling, preservada conforme o manuscrito.','Ensaiar e ajustar o tempo; não houve ensaio cronometrado nem gravação de demonstração.']}
(HERE/'manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(out, len(prs.slides),'diapositivos; notas em todos; percurso principal 20 min; treino 30 min.')
