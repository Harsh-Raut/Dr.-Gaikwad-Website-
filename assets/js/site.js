/* Dr. Gaikwad's Institute — shared site behaviour */
(function () {
  'use strict';

  // Reveal-on-scroll, respecting reduced-motion.
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.rise');
  if (reduce || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(items, function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    Array.prototype.forEach.call(items, function (el) { io.observe(el); });
  }

  // Mobile navigation.
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('nav.main');
  if (toggle && nav) {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Close' : 'Menu';
      if (open) {
        nav.style.cssText = 'display:flex;position:absolute;top:100%;left:0;right:0;flex-direction:column;' +
          'align-items:stretch;background:var(--paper-2);border-top:1px solid var(--rule);' +
          'border-bottom:1px solid var(--rule);padding:8px 18px 14px;box-shadow:var(--shadow-md);';
      } else {
        nav.style.cssText = '';
      }
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && window.innerWidth <= 1080) {
        nav.classList.remove('open');
        nav.style.cssText = '';
        toggle.setAttribute('aria-expanded', 'false');
        toggle.textContent = 'Menu';
      }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080 && nav.classList.contains('open')) {
        nav.classList.remove('open');
        nav.style.cssText = '';
        toggle.setAttribute('aria-expanded', 'false');
        toggle.textContent = 'Menu';
      }
    });
  }

  // Enquiry form — demo handler. Replace with the live endpoint at launch.
  var form = document.querySelector('form[data-enquiry]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('[data-form-status]');
      if (note) {
        note.textContent = 'This is a design preview — the form is not yet connected. ' +
          'At launch this submits to the institute and notifies the counsellor on WhatsApp.';
        note.style.color = 'var(--brass)';
      }
    });
  }
})();

/* ------------------------------------------------------------------ i18n
   English ships in the HTML; the Marathi sits alongside it in data-mr.
   Toggling swaps textContent in place — no fetch, no reload, no flash.
   The choice is remembered and re-applied before paint on the next page. */
(function () {
  'use strict';

  var KEY = 'dgi-lang';
  var root = document.documentElement;

  function apply(lang) {
    var toMr = lang === 'mr';
    var nodes = document.querySelectorAll('[data-mr]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      // Stash the original English once, so switching back is lossless.
      if (el.getAttribute('data-en') === null) {
        el.setAttribute('data-en', el.firstChild && el.firstChild.nodeType === 3
          ? el.firstChild.nodeValue : el.textContent);
      }
      var text = toMr ? el.getAttribute('data-mr') : el.getAttribute('data-en');
      // Replace only the element's own leading text node, leaving child
      // elements (links, <b>, <small>) untouched.
      if (el.firstChild && el.firstChild.nodeType === 3) {
        el.firstChild.nodeValue = text;
      } else {
        el.insertBefore(document.createTextNode(text), el.firstChild);
      }
    }
    root.setAttribute('lang', toMr ? 'mr' : 'en');
    var btns = document.querySelectorAll('.lang-btn');
    for (var j = 0; j < btns.length; j++) {
      var on = btns[j].getAttribute('data-lang') === lang;
      btns[j].classList.toggle('is-on', on);
      btns[j].setAttribute('aria-pressed', String(on));
    }
    try { localStorage.setItem(KEY, lang); } catch (e) {}
  }

  var saved;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'mr') apply('mr');

  document.addEventListener('click', function (e) {
    var btn = e.target.closest ? e.target.closest('.lang-btn') : null;
    if (!btn) return;
    apply(btn.getAttribute('data-lang'));
  });
})();
