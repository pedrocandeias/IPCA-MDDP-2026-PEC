'use strict';
const citations = JSON.parse(document.getElementById('citation-data').textContent);
const panel = document.getElementById('citation-panel');
const sources = document.getElementById('panel-sources');
const closeButton = document.getElementById('close-panel');
let activeButton = null;
function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
function safeLink(label, href) {
  if (!href || /^(?:javascript|data|vbscript):/i.test(href)) return null;
  const node = element('a', '', label);
  node.href = href;
  node.target = '_blank';
  node.rel = 'noopener noreferrer';
  return node;
}
function positionPanel() {
  if (!activeButton || panel.hidden || window.innerWidth <= 700) return;
  const rect = activeButton.getBoundingClientRect();
  const width = panel.offsetWidth;
  const height = panel.offsetHeight;
  const left = Math.max(16, Math.min(rect.left - width / 2 + rect.width / 2, window.innerWidth - width - 16));
  let top = rect.bottom + 10;
  if (top + height > window.innerHeight - 16) top = rect.top - height - 10;
  top = Math.max(16, Math.min(top, window.innerHeight - height - 16));
  panel.style.left = left + 'px';
  panel.style.top = top + 'px';
}
function closePanel(restoreFocus = true) {
  panel.hidden = true;
  if (activeButton) {
    activeButton.setAttribute('aria-expanded', 'false');
    if (restoreFocus) activeButton.focus({preventScroll: true});
  }
  activeButton = null;
}
function sourceCard(source, index, total) {
  const card = element('section', 'source-card');
  card.append(element('span', 'source-number', 'FONTE ' + (index + 1) + ' DE ' + total));
  card.append(element('h3', '', source.label + ' — ' + source.title));
  card.append(element('p', 'source-reference', source.reference));
  const links = element('div', 'source-links');
  if (source.doi) links.append(safeLink('Abrir DOI ↗', 'https://doi.org/' + source.doi));
  else if (source.url && /^https?:\/\//i.test(source.url)) links.append(safeLink('Abrir fonte ↗', source.url));
  if (source.pdf) links.append(safeLink('Abrir PDF local ↗', source.pdf));
  card.append(links);
  if (source.locator) card.append(element('p', 'source-pages', 'Localizador da citação: ' + source.locator));
  const evidence = source.evidence;
  if (evidence) {
    card.append(element('p', 'excerpt-label', evidence.same_passage ? 'Excertos da auditoria · passagem semelhante' : 'Excertos guardados para esta obra'));
    if (!evidence.same_passage) card.append(element('p', 'source-pages', 'A auditoria não identifica com segurança esta passagem atual. Os excertos abaixo pertencem à mesma obra.'));
    for (const quote of evidence.excerpts) card.append(element('blockquote', '', quote));
    if (evidence.pages) card.append(element('p', 'source-pages', evidence.pages));
    const details = element('details');
    details.append(element('summary', '', 'Texto auditado e avaliação histórica'));
    for (const claim of evidence.claims) details.append(element('p', '', claim));
    if (evidence.assessment) details.append(element('p', '', 'Avaliação registada: ' + evidence.assessment));
    details.append(element('p', 'source-pages', 'Auditoria: secção ' + evidence.section));
    card.append(details);
  } else {
    card.append(element('p', 'missing-excerpt', 'Não foi encontrado um excerto inequivocamente associado a esta obra no Markdown da auditoria. A referência foi recuperada dos dados da citação no ODT.'));
  }
  return card;
}
function openPanel(button) {
  if (button === activeButton && !panel.hidden) return closePanel();
  closePanel(false);
  activeButton = button;
  const citation = citations[button.dataset.citation];
  document.getElementById('panel-title').textContent = citation.sources.length === 1 ? '1 referência' : citation.sources.length + ' referências';
  document.getElementById('panel-citation').textContent = citation.visible;
  sources.replaceChildren(...citation.sources.map((source, index) => sourceCard(source, index, citation.sources.length)));
  panel.hidden = false;
  panel.querySelector('.panel-scroll').scrollTop = 0;
  button.setAttribute('aria-expanded', 'true');
  positionPanel();
  closeButton.focus({preventScroll: true});
}
document.addEventListener('click', event => {
  const trigger = event.target.closest('.citation-star');
  if (trigger) return openPanel(trigger);
  if (!panel.hidden && !panel.contains(event.target)) closePanel(false);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !panel.hidden) {event.preventDefault(); closePanel();}
});
closeButton.addEventListener('click', () => closePanel());
window.addEventListener('resize', positionPanel);
window.addEventListener('scroll', positionPanel, {passive: true});
document.getElementById('print').addEventListener('click', () => window.print());
