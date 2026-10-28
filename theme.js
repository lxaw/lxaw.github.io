// Light/dark toggle. Loaded in <head> so the saved theme applies before first paint.
(function () {
  var root = document.documentElement;
  var KEY = 'theme';

  function saved() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }

  function current() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  var initial = saved();
  if (initial === 'light' || initial === 'dark') root.setAttribute('data-theme', initial);

  var SUN = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var MOON = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';

  function render(btn) {
    var dark = current() === 'dark';
    // Show the icon for the mode you'd switch to
    btn.innerHTML = dark ? SUN : MOON;
    var label = dark ? 'Switch to light mode' : 'Switch to dark mode';
    btn.setAttribute('aria-label', label);
    btn.title = label;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.querySelector('nav');
    if (!nav) return;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle';
    render(btn);
    btn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      render(btn);
    });
    nav.appendChild(btn);

    // Mark the nav link for the current page; blog posts count as the Blog page
    var here = location.pathname.replace(/index\.html$/, '');
    if (/\/blog\/post\.html$/.test(here)) here = here.replace(/post\.html$/, '');
    var links = nav.querySelectorAll(':scope > a');
    for (var i = 0; i < links.length; i++) {
      var path = links[i].pathname.replace(/index\.html$/, '');
      if (path === here) links[i].classList.add('active');
    }
  });
})();
