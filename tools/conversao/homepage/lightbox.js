(() => {
  const english = document.documentElement.lang === 'en';
  const labels = english ? {open:'Enlarge image',close:'Close image',zoom:'Original size',fit:'Fit to screen',image:'Image preview'} : {open:'Ampliar imagem',close:'Fechar imagem',zoom:'Tamanho original',fit:'Ajustar ao ecrã',image:'Pré-visualização da imagem'};
  const dialog = document.createElement('dialog');
  dialog.className = 'image-lightbox';
  dialog.setAttribute('aria-label', labels.image);
  dialog.innerHTML = '<div class="lightbox-toolbar"><p class="lightbox-title"></p><button type="button" class="lightbox-zoom" aria-pressed="false"></button><button type="button" class="lightbox-close"></button></div><div class="lightbox-stage"><img alt=""></div>';
  document.body.append(dialog);
  const title = dialog.querySelector('.lightbox-title');
  const preview = dialog.querySelector('img');
  const zoom = dialog.querySelector('.lightbox-zoom');
  const close = dialog.querySelector('.lightbox-close');
  const stage = dialog.querySelector('.lightbox-stage');
  close.textContent = labels.close + ' ×';
  zoom.textContent = labels.zoom;
  close.addEventListener('click', () => dialog.close());
  zoom.addEventListener('click', () => {
    const original = dialog.classList.toggle('original-size');
    zoom.setAttribute('aria-pressed', String(original));
    zoom.textContent = original ? labels.fit : labels.zoom;
  });
  dialog.addEventListener('click', event => {
    if (event.target === dialog || event.target === stage) dialog.close();
  });
  dialog.addEventListener('close', () => {
    dialog.classList.remove('original-size');
    document.documentElement.classList.remove('lightbox-open');
    zoom.setAttribute('aria-pressed', 'false');
    zoom.textContent = labels.zoom;
    preview.removeAttribute('src');
  });
  document.querySelectorAll('.hero-image img, article img').forEach(image => {
    image.classList.add('expandable-image');
    image.tabIndex = 0;
    image.setAttribute('role', 'button');
    image.setAttribute('aria-haspopup', 'dialog');
    image.setAttribute('aria-label', labels.open + (image.alt ? ': ' + image.alt : ''));
    const open = event => {
      event.preventDefault();
      const description = image.alt || image.closest('figure')?.querySelector('figcaption')?.textContent || labels.image;
      preview.src = image.currentSrc || image.src;
      preview.alt = description;
      title.textContent = description;
      document.documentElement.classList.add('lightbox-open');
      dialog.showModal();
      stage.scrollTo(0, 0);
    };
    image.addEventListener('click', open);
    image.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') open(event);
    });
  });
})();
