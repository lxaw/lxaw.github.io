// Site nav and light/dark toggle. Loaded in <head> so the saved theme applies
// before first paint. Every page has an empty <nav></nav>; the links are filled
// in here so they only need to change in one place.
(function () {
  var root = document.documentElement;
  var KEY = 'theme';

  // Nav links, relative to the site root (the folder this script lives in)
  var NAV = [
    ['Home', 'index.html'],
    ['Books', 'books_read.html'],
    ['Papers', 'papers_read.html'],
    ['History', 'history.html'],
    ['Blog', 'blog/']
  ];
  // Only readable while this script first runs, not in later callbacks
  var SITE_ROOT = document.currentScript ? document.currentScript.src : location.href;

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
    NAV.forEach(function (item, i) {
      // Same spacing as links written on separate lines in HTML
      if (i) nav.appendChild(document.createTextNode(' '));
      var a = document.createElement('a');
      a.href = new URL(item[1], SITE_ROOT).href;
      a.textContent = item[0];
      nav.appendChild(a);
    });
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
