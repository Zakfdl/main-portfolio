/* ==========================================================================
   BERRIZAK.COM — ZAKARIA FADL
   High-Craft Editorial Portfolio
   Progressive enhancement: 100% functional without JavaScript.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;

  /* ── Footer Year ───────────────────────────────────── */
  var yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* ── Theme Toggle (Persisted, Light Default) ───────── */
  var themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme') || 'light';
      var next = current === 'light' ? 'dark' : 'light';
      root.setAttribute('data-theme', next);
      try {
        localStorage.removeItem('bz-theme');
        localStorage.setItem('bz-light-theme', next);
      } catch (e) {
        /* storage restricted */
      }
    });
  }

  /* ── Mobile Navigation ─────────────────────────────── */
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');

  function setNavOpen(open) {
    if (!navToggle || !navLinks) return;
    navToggle.setAttribute('aria-expanded', String(open));
    navLinks.setAttribute('data-open', String(open));
  }

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var isOpen = navToggle.getAttribute('aria-expanded') === 'true';
      setNavOpen(!isOpen);
    });

    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        setNavOpen(false);
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true') {
        setNavOpen(false);
        navToggle.focus();
      }
    });
  }

  /* ── Active Nav Link On Scroll ─────────────────────── */
  var sections = document.querySelectorAll('main section[id]');
  var navAnchors = document.querySelectorAll('#navLinks a[href^="#"]');
  if (sections.length && navAnchors.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        navAnchors.forEach(function (a) {
          if (a.getAttribute('href') === '#' + id) {
            a.setAttribute('aria-current', 'page');
          } else {
            a.removeAttribute('aria-current');
          }
        });
      });
    }, { rootMargin: '-40% 0px -50% 0px' });

    sections.forEach(function (section) {
      observer.observe(section);
    });
  }

  /* ── Reveal Elements On Scroll ─────────────────────── */
  var revealEls = document.querySelectorAll('.reveal');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    var revObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });

    revealEls.forEach(function (el) {
      revObs.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  /* ── Blueprint Before / After State Switcher ───────── */
  var stateBoxes = document.querySelectorAll('.js-states');
  stateBoxes.forEach(function (box) {
    var buttons = box.querySelectorAll('.state-btn');
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetState = btn.getAttribute('data-state');
        box.setAttribute('data-current', targetState);
        buttons.forEach(function (b) {
          b.classList.toggle('is-active', b === btn);
          b.setAttribute('aria-pressed', String(b === btn));
        });
        box.querySelectorAll('[data-show]').forEach(function (stage) {
          stage.hidden = stage.getAttribute('data-show') !== targetState;
        });
      });
    });
  });

  /* ── Formspree Contact Form Submission ──────────────── */
  var form = document.getElementById('contactForm');
  var formMsg = document.getElementById('formMsg');
  var submitBtn = document.getElementById('formSubmit');

  if (form && submitBtn) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var sendingLabel = form.getAttribute('data-sending-label') || 'Sending…';
      var successMsg = form.getAttribute('data-success-msg') || 'Message sent successfully.';
      var errorMsg = form.getAttribute('data-error-msg') || 'Something went wrong. Please email directly.';
      var originalBtnText = submitBtn.textContent;

      submitBtn.disabled = true;
      submitBtn.textContent = sendingLabel;
      if (formMsg) {
        formMsg.hidden = true;
        formMsg.className = 'form-msg';
      }

      var formData = new FormData(form);

      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: { 'Accept': 'application/json' }
      })
      .then(function (response) {
        if (response.ok) {
          form.reset();
          if (formMsg) {
            formMsg.textContent = successMsg;
            formMsg.className = 'form-msg is-success';
            formMsg.hidden = false;
          }
        } else {
          throw new Error('Form submission failed');
        }
      })
      .catch(function () {
        if (formMsg) {
          formMsg.textContent = errorMsg;
          formMsg.className = 'form-msg is-error';
          formMsg.hidden = false;
        }
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = originalBtnText;
      });
    });
  }

})();
