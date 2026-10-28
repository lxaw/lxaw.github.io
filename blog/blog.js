// Blog: each post is blog/posts/<slug>.md, listed newest first in blog/posts.json.
// Rendering happens in the browser, so serve the site over HTTP when testing locally
// (e.g. `python3 -m http.server`); fetch() does not work from file://.
(function () {
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  // "2026-10-28" -> "Oct 2026" (short) or "28 Oct 2026"
  function formatDate(iso, short) {
    var p = (iso || '').split('-');
    if (p.length !== 3) return iso || '';
    var m = MONTHS[parseInt(p[1], 10) - 1] + ' ' + p[0];
    return short ? m : parseInt(p[2], 10) + ' ' + m;
  }

  function loadPosts(base) {
    return fetch(base + 'posts.json').then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    });
  }

  function message(el, text) {
    var li = document.createElement('li');
    li.className = 'post-empty';
    li.textContent = text;
    el.appendChild(li);
  }

  window.Blog = {
    // Fill a <ul class="post-list"> with links to every post.
    list: function (el, base) {
      loadPosts(base).then(function (posts) {
        el.innerHTML = '';
        if (!posts.length) return message(el, 'No posts yet.');
        posts.forEach(function (post) {
          var li = document.createElement('li');
          var date = document.createElement('span');
          date.className = 'post-date';
          date.textContent = formatDate(post.date, true);
          var a = document.createElement('a');
          a.href = base + 'post.html?p=' + encodeURIComponent(post.slug);
          a.textContent = post.title || 'Untitled';
          li.appendChild(date);
          li.appendChild(a);
          el.appendChild(li);
        });
      }).catch(function () {
        el.innerHTML = '';
        message(el, 'Could not load posts.');
      });
    },

    // Render the post named by ?p=<slug> into the given elements.
    render: function (titleEl, dateEl, bodyEl) {
      var slug = new URLSearchParams(location.search).get('p');
      loadPosts('').then(function (posts) {
        // Only fetch slugs that are in the manifest
        var post = posts.filter(function (p) { return p.slug === slug; })[0];
        if (!post) throw new Error('not found');
        titleEl.textContent = post.title || 'Untitled';
        dateEl.textContent = formatDate(post.date);
        document.title = (post.title || 'Untitled');
        return fetch('posts/' + encodeURIComponent(post.slug) + '.md').then(function (r) {
          if (!r.ok) throw new Error(r.status);
          return r.text();
        });
      }).then(function (md) {
        if (!md.trim()) {
          bodyEl.innerHTML = '<p class="post-empty">Nothing here yet.</p>';
          return;
        }
        bodyEl.innerHTML = marked.parse(md);
      }).catch(function () {
        titleEl.textContent = 'Post not found';
        bodyEl.innerHTML = '<p><a href="./">Back to all posts</a></p>';
      });
    }
  };
})();
