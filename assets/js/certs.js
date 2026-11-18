/* ==========================================================================
   BERRIZAK.COM — CERTIFICATES ARCHIVE & SMOOTH PDF VIEWER
   Dual-engine viewer: HiDPI PDF.js canvas renderer + automatic native iframe
   fallback (for file:// local browsing or offline/CDN resilience).
   Zero external build dependencies. Bilingual (EN + AR / RTL-aware).
   ========================================================================== */
(function () {
  'use strict';

  var dataEl = document.getElementById('certsData');
  if (!dataEl) return;

  var PAYLOAD;
  try {
    PAYLOAD = JSON.parse(dataEl.textContent);
  } catch (e) {
    return;
  }

  var LANG = PAYLOAD.lang === 'ar' ? 'ar' : 'en';
  var IS_RTL = LANG === 'ar';
  var ASSET_ROOT = PAYLOAD.assetRoot || '../';
  var CERTS = Array.isArray(PAYLOAD.certs) ? PAYLOAD.certs : [];
  var PROGRAMS = Array.isArray(PAYLOAD.programs) ? PAYLOAD.programs : [];
  var UI = PAYLOAD.ui || {};

  function createIssuerEl(cert, small) {
    var wrap = document.createElement('span');
    wrap.className = 'issuer-lockup' + (small ? ' issuer-lockup--sm' : '');
    var keys = Array.isArray(cert.issuerKeys) && cert.issuerKeys.length ? cert.issuerKeys : [cert.issuerKey];
    var labels = { google: 'Google', ibm: 'IBM', meta: 'Meta', skillup: 'SkillUp', coursera: 'Coursera' };
    keys.forEach(function (k, idx) {
      if (idx > 0) {
        var sep = document.createElement('span');
        sep.className = 'issuer-sep';
        sep.textContent = '&';
        wrap.appendChild(sep);
      }
      var brand = document.createElement('span');
      brand.className = 'issuer-brand';
      var img = document.createElement('img');
      img.src = ASSET_ROOT + 'assets/images/issuers/' + k + '.png';
      if (k === 'skillup') {
        img.className = 'issuer-wordmark';
        img.alt = 'SkillUp';
        brand.appendChild(img);
      } else {
        img.className = 'issuer-icon' + (k === 'coursera' ? ' issuer-icon--round' : '');
        img.alt = '';
        var txt = document.createElement('span');
        txt.textContent = labels[k] || cert.issuer;
        brand.appendChild(img);
        brand.appendChild(txt);
      }
      wrap.appendChild(brand);
    });
    return wrap;
  }
  var BY_CODE = Object.create(null);
  CERTS.forEach(function (c, idx) {
    c._index = idx;
    BY_CODE[c.code.toUpperCase()] = c;
  });

  var BY_PROG = Object.create(null);
  PROGRAMS.forEach(function (p) {
    BY_PROG[p.code] = p;
  });

  /* ── PDF.js Lazy Loader + In-Memory Byte Cache ───────── */
  var PDFJS_VER = '3.11.174';
  var CDN_SOURCES = [
    {
      lib: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/' + PDFJS_VER + '/pdf.min.js',
      worker: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/' + PDFJS_VER + '/pdf.worker.min.js',
      cmap: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/' + PDFJS_VER + '/cmaps/'
    },
    {
      lib: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@' + PDFJS_VER + '/build/pdf.min.js',
      worker: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@' + PDFJS_VER + '/build/pdf.worker.min.js',
      cmap: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@' + PDFJS_VER + '/cmaps/'
    }
  ];

  var pdfJsPromise = null;
  var activeCdn = CDN_SOURCES[0];
  var pdfBytesCache = new Map();
  var MAX_BYTE_CACHE = 16;

  function canUseFetchEngine() {
    return window.location.protocol === 'http:' || window.location.protocol === 'https:';
  }

  function loadScript(src, timeoutMs) {
    return new Promise(function (resolve, reject) {
      var done = false;
      var s = document.createElement('script');
      s.src = src;
      s.async = true;
      var timer = window.setTimeout(function () {
        if (done) return;
        done = true;
        s.remove();
        reject(new Error('Script load timeout'));
      }, timeoutMs || 6500);

      s.onload = function () {
        if (done) return;
        done = true;
        window.clearTimeout(timer);
        resolve();
      };
      s.onerror = function () {
        if (done) return;
        done = true;
        window.clearTimeout(timer);
        s.remove();
        reject(new Error('Script load error'));
      };
      document.head.appendChild(s);
    });
  }

  function configureWorker(pdfjsLib, workerUrl) {
    try {
      var blob = new Blob(['importScripts("' + workerUrl + '");'], { type: 'application/javascript' });
      pdfjsLib.GlobalWorkerOptions.workerSrc = URL.createObjectURL(blob);
    } catch (e) {
      pdfjsLib.GlobalWorkerOptions.workerSrc = workerUrl;
    }
  }

  function ensurePdfJs() {
    if (!canUseFetchEngine()) {
      return Promise.reject(new Error('file-protocol'));
    }
    if (window.pdfjsLib) {
      return Promise.resolve(window.pdfjsLib);
    }
    if (pdfJsPromise) {
      return pdfJsPromise;
    }

    pdfJsPromise = (function trySource(idx) {
      if (idx >= CDN_SOURCES.length) {
        return Promise.reject(new Error('pdfjs-unavailable'));
      }
      var cdn = CDN_SOURCES[idx];
      return loadScript(cdn.lib, 3200)
        .then(function () {
          if (!window.pdfjsLib) throw new Error('pdfjs-missing');
          activeCdn = cdn;
          configureWorker(window.pdfjsLib, cdn.worker);
          return window.pdfjsLib;
        })
        .catch(function () {
          return trySource(idx + 1);
        });
    })(0);

    return pdfJsPromise;
  }

  function fetchPdfBytes(url) {
    if (pdfBytesCache.has(url)) {
      var cached = pdfBytesCache.get(url);
      /* Refresh LRU order */
      pdfBytesCache.delete(url);
      pdfBytesCache.set(url, cached);
      return cached;
    }

    var promise = fetch(url, { credentials: 'same-origin' })
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.arrayBuffer();
      })
      .then(function (buf) {
        return new Uint8Array(buf);
      })
      .catch(function (err) {
        pdfBytesCache.delete(url);
        throw err;
      });

    if (pdfBytesCache.size >= MAX_BYTE_CACHE) {
      var oldestKey = pdfBytesCache.keys().next().value;
      if (oldestKey) pdfBytesCache.delete(oldestKey);
    }
    pdfBytesCache.set(url, promise);
    return promise;
  }

  function prefetchUrl(url) {
    if (!url || !canUseFetchEngine() || pdfBytesCache.has(url)) return;
    fetchPdfBytes(url).catch(function () {
      /* ignore background prefetch failures */
    });
  }

  /* ── Shared PDF Viewport Controller ──────────────────── */
  function createPdfViewport(opts) {
    var root = opts.root;
    var stage = root.querySelector('[data-pdf-stage]');
    var canvasWrap = root.querySelector('[data-pdf-canvas-wrap]');
    var canvas = root.querySelector('[data-pdf-canvas]');
    var fallbackWrap = root.querySelector('[data-pdf-fallback]');
    var fallbackFrame = root.querySelector('[data-pdf-iframe]');
    var loadingEl = root.querySelector('[data-pdf-loading]');
    var errorEl = root.querySelector('[data-pdf-error]');
    var zoomGroup = root.querySelector('[data-pdf-zoom-group]');
    var zoomLabel = root.querySelector('[data-pdf-zoom-val]');
    var pageLabel = root.querySelector('[data-pdf-page-val]');
    var pageControls = root.querySelector('[data-pdf-page-controls]');
    var fitPageBtn = root.querySelector('[data-pdf-action="fit-page"]');
    var fitWidthBtn = root.querySelector('[data-pdf-action="fit-width"]');
    var prevPageBtn = root.querySelector('[data-pdf-action="prev-page"]');
    var nextPageBtn = root.querySelector('[data-pdf-action="next-page"]');

    var state = {
      cert: null,
      doc: null,
      pageNum: 1,
      numPages: 1,
      zoomMode: opts.defaultZoomMode || 'fit-page',
      scale: 1,
      renderToken: 0,
      renderTask: null,
      usingFallback: false,
      neighbors: []
    };

    function setLoading(isLoading) {
      if (loadingEl) loadingEl.hidden = !isLoading;
      if (canvasWrap) canvasWrap.classList.toggle('is-loading', isLoading);
    }

    function setError(hasError) {
      if (errorEl) errorEl.hidden = !hasError;
    }

    function updateControlsUI() {
      if (zoomGroup) {
        zoomGroup.hidden = state.usingFallback;
      }
      if (zoomLabel) {
        zoomLabel.textContent = state.usingFallback
          ? 'PDF'
          : Math.round(state.scale * 100) + '%';
      }
      if (fitPageBtn) {
        fitPageBtn.classList.toggle('is-active', !state.usingFallback && state.zoomMode === 'fit-page');
        fitPageBtn.disabled = state.usingFallback;
      }
      if (fitWidthBtn) {
        fitWidthBtn.classList.toggle('is-active', !state.usingFallback && state.zoomMode === 'fit-width');
        fitWidthBtn.disabled = state.usingFallback;
      }
      root.querySelectorAll('[data-pdf-action="zoom-in"], [data-pdf-action="zoom-out"]').forEach(function (b) {
        b.disabled = state.usingFallback;
      });

      if (pageControls) {
        pageControls.hidden = state.usingFallback || state.numPages <= 1;
      }
      if (pageLabel) {
        pageLabel.textContent = state.pageNum + ' / ' + state.numPages;
      }
      if (prevPageBtn) prevPageBtn.disabled = state.pageNum <= 1;
      if (nextPageBtn) nextPageBtn.disabled = state.pageNum >= state.numPages;
    }

    function showNativeFallback(cert) {
      state.usingFallback = true;
      setLoading(false);
      setError(false);
      if (canvasWrap) canvasWrap.hidden = true;
      if (fallbackWrap && fallbackFrame) {
        fallbackWrap.hidden = false;
        var targetSrc = cert.pdf + '#view=FitH&navpanes=0';
        if (fallbackFrame.getAttribute('src') !== targetSrc) {
          fallbackFrame.setAttribute('src', targetSrc);
        }
        fallbackFrame.setAttribute('title', cert.title);
      }
      updateControlsUI();
    }

    function computeScaleForPage(page) {
      var baseViewport = page.getViewport({ scale: 1 });
      var pad = window.innerWidth < 640 ? 20 : 48;
      var availW = Math.max((stage ? stage.clientWidth : 640) - pad, 240);
      var availH = Math.max((stage ? stage.clientHeight : 480) - pad, 240);

      if (state.zoomMode === 'fit-width') {
        return Math.min(Math.max(availW / baseViewport.width, 0.35), 2.5);
      }
      if (state.zoomMode === 'fit-page') {
        var sW = availW / baseViewport.width;
        var sH = availH / baseViewport.height;
        return Math.min(Math.max(Math.min(sW, sH), 0.3), 2.5);
      }
      return Math.min(Math.max(state.scale, 0.4), 2.8);
    }

    function renderCurrentPage(token) {
      if (!state.doc || !canvas || !canvasWrap) return Promise.resolve();
      if (state.renderTask) {
        try { state.renderTask.cancel(); } catch (e) {}
        state.renderTask = null;
      }

      return state.doc.getPage(state.pageNum).then(function (page) {
        if (token !== state.renderToken) return;

        var cssScale = computeScaleForPage(page);
        state.scale = cssScale;
        var dpr = Math.min(window.devicePixelRatio || 1, 2.5);
        var cssViewport = page.getViewport({ scale: cssScale });
        var pixelViewport = page.getViewport({ scale: cssScale * dpr });

        var ctx = canvas.getContext('2d', { alpha: false });
        canvas.width = Math.floor(pixelViewport.width);
        canvas.height = Math.floor(pixelViewport.height);
        canvas.style.width = Math.floor(cssViewport.width) + 'px';
        canvas.style.height = Math.floor(cssViewport.height) + 'px';

        canvasWrap.hidden = false;
        if (fallbackWrap) fallbackWrap.hidden = true;
        updateControlsUI();

        /* Update pannable state */
        if (stage) {
          var isOverflow = (cssViewport.width > stage.clientWidth - 20) ||
                           (cssViewport.height > stage.clientHeight - 20);
          stage.classList.toggle('is-pannable', isOverflow);
        }

        var renderTask = page.render({
          canvasContext: ctx,
          viewport: pixelViewport
        });
        state.renderTask = renderTask;

        return renderTask.promise.then(function () {
          if (token !== state.renderToken) return;
          state.renderTask = null;
          setLoading(false);
          canvasWrap.classList.add('is-ready');

          /* Silently prefetch neighbor PDFs for instant next/prev transitions */
          state.neighbors.forEach(prefetchUrl);
        });
      }).catch(function (err) {
        if (err && err.name === 'RenderingCancelledException') return;
        if (token === state.renderToken && state.cert) {
          showNativeFallback(state.cert);
        }
      });
    }

    function loadCert(cert, neighbors) {
      if (!cert) return;
      state.cert = cert;
      state.neighbors = neighbors || [];
      state.pageNum = 1;
      state.numPages = 1;
      state.usingFallback = false;
      state.renderToken += 1;
      var token = state.renderToken;

      if (state.renderTask) {
        try { state.renderTask.cancel(); } catch (e) {}
        state.renderTask = null;
      }

      if (!canUseFetchEngine()) {
        showNativeFallback(cert);
        return;
      }

      setError(false);
      setLoading(true);
      if (canvasWrap) {
        canvasWrap.classList.remove('is-ready');
      }
      if (fallbackWrap) fallbackWrap.hidden = true;
      if (stage) {
        stage.scrollTop = 0;
        stage.scrollLeft = 0;
      }

      if (state.doc) {
        try { state.doc.destroy(); } catch (e) {}
        state.doc = null;
      }

      Promise.all([ensurePdfJs(), fetchPdfBytes(cert.pdf)])
        .then(function (results) {
          if (token !== state.renderToken) return;
          var pdfjsLib = results[0];
          var bytes = results[1];
          /* Clone Uint8Array so worker buffer transfer does not detach cached bytes */
          var loadingTask = pdfjsLib.getDocument({
            data: bytes.slice(0),
            cMapUrl: activeCdn.cmap,
            cMapPacked: true
          });
          return loadingTask.promise;
        })
        .then(function (doc) {
          if (!doc || token !== state.renderToken) {
            if (doc) {
              try { doc.destroy(); } catch (e) {}
            }
            return;
          }
          state.doc = doc;
          state.numPages = doc.numPages || 1;
          return renderCurrentPage(token);
        })
        .catch(function () {
          if (token !== state.renderToken) return;
          showNativeFallback(cert);
        });
    }

    function setZoom(mode, customScale) {
      if (state.usingFallback || !state.doc) return;
      state.zoomMode = mode;
      if (typeof customScale === 'number') {
        state.scale = Math.min(Math.max(customScale, 0.4), 2.8);
      }
      renderCurrentPage(state.renderToken);
    }

    function zoomBy(delta) {
      if (state.usingFallback || !state.doc) return;
      setZoom('custom', state.scale + delta);
    }

    function refreshFit() {
      if (!state.doc || state.usingFallback) return;
      if (state.zoomMode === 'fit-page' || state.zoomMode === 'fit-width') {
        renderCurrentPage(state.renderToken);
      }
    }

    /* Wire toolbar actions */
    root.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-pdf-action]');
      if (!btn) return;
      var act = btn.getAttribute('data-pdf-action');
      if (act === 'zoom-in') zoomBy(0.2);
      else if (act === 'zoom-out') zoomBy(-0.2);
      else if (act === 'fit-page') setZoom('fit-page');
      else if (act === 'fit-width') setZoom('fit-width');
      else if (act === 'prev-page' && state.pageNum > 1) {
        state.pageNum -= 1;
        renderCurrentPage(state.renderToken);
      } else if (act === 'next-page' && state.pageNum < state.numPages) {
        state.pageNum += 1;
        renderCurrentPage(state.renderToken);
      }
    });

    /* Double-click canvas toggles Fit Page <-> 150% */
    if (canvas) {
      canvas.addEventListener('dblclick', function () {
        if (state.usingFallback || !state.doc) return;
        if (state.zoomMode === 'custom' && state.scale > 1.25) {
          setZoom('fit-page');
        } else {
          setZoom('custom', 1.5);
        }
      });
    }

    /* Ctrl/Cmd + Wheel zoom */
    if (stage) {
      stage.addEventListener('wheel', function (e) {
        if (!(e.ctrlKey || e.metaKey) || state.usingFallback || !state.doc) return;
        e.preventDefault();
        zoomBy(e.deltaY < 0 ? 0.14 : -0.14);
      }, { passive: false });

      /* Drag-to-pan when zoomed */
      var drag = null;
      stage.addEventListener('pointerdown', function (e) {
        if (e.button !== 0 || !stage.classList.contains('is-pannable')) return;
        if (e.target.closest('button, a')) return;
        drag = {
          x: e.clientX,
          y: e.clientY,
          sl: stage.scrollLeft,
          st: stage.scrollTop
        };
        stage.classList.add('is-dragging');
        if (stage.setPointerCapture) {
          try { stage.setPointerCapture(e.pointerId); } catch (err) {}
        }
      });
      stage.addEventListener('pointermove', function (e) {
        if (!drag) return;
        stage.scrollLeft = drag.sl - (e.clientX - drag.x);
        stage.scrollTop = drag.st - (e.clientY - drag.y);
      });
      var endDrag = function () {
        if (!drag) return;
        drag = null;
        stage.classList.remove('is-dragging');
      };
      stage.addEventListener('pointerup', endDrag);
      stage.addEventListener('pointercancel', endDrag);
    }

    /* Responsive re-fit on container resize */
    var resizeTimer = null;
    if ('ResizeObserver' in window && stage) {
      var ro = new ResizeObserver(function () {
        window.clearTimeout(resizeTimer);
        resizeTimer = window.setTimeout(refreshFit, 120);
      });
      ro.observe(stage);
    }

    return {
      loadCert: loadCert,
      zoomBy: zoomBy,
      setZoom: setZoom,
      refreshFit: refreshFit,
      getState: function () { return state; }
    };
  }

  /* ── Filtering, View Modes & Directory State ─────────── */
  var dirSection = document.getElementById('certsDirectory');
  var cardsGrid = document.getElementById('certsGrid');
  var emptyState = document.getElementById('certsEmpty');
  var countEl = document.getElementById('certsCount');
  var searchInput = document.getElementById('certSearch');
  var clearSearchBtn = document.getElementById('certSearchClear');
  var catTabs = document.querySelectorAll('[data-filter-cat]');
  var issuerBtns = document.querySelectorAll('[data-filter-issuer]');
  var viewBtns = document.querySelectorAll('[data-view-mode]');
  var splitShell = document.getElementById('certsSplitShell');
  var splitList = document.getElementById('splitReaderList');
  var splitRoot = document.getElementById('splitReaderViewport');

  var filterState = {
    cat: 'all',
    issuer: 'all',
    query: '',
    view: 'cards'
  };

  var filteredCerts = CERTS.slice();
  var splitSelectedCode = CERTS[0] ? CERTS[0].code : null;
  var splitViewport = splitRoot ? createPdfViewport({
    root: splitRoot,
    defaultZoomMode: 'fit-width'
  }) : null;

  function matchesFilter(cert) {
    if (filterState.cat !== 'all' && cert.cat !== filterState.cat) return false;
    if (filterState.issuer !== 'all') {
      var keys = Array.isArray(cert.issuerKeys) ? cert.issuerKeys : [cert.issuerKey];
      if (keys.indexOf(filterState.issuer) === -1) return false;
    }
    if (filterState.query) {
      var q = filterState.query.toLowerCase();
      var hay = (
        cert.title + ' ' +
        cert.titleAr + ' ' +
        cert.desc + ' ' +
        cert.issuer + ' ' +
        cert.code + ' ' +
        cert.typeLabel + ' ' +
        (cert.parentTitle || '')
      ).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    return true;
  }

  function updateUrlParam(key, value) {
    try {
      var url = new URL(window.location.href);
      if (value) url.searchParams.set(key, value);
      else url.searchParams.delete(key);
      window.history.replaceState(null, '', url.toString());
    } catch (e) {}
  }

  function setSplitActiveCert(code) {
    var cert = BY_CODE[(code || '').toUpperCase()] || filteredCerts[0] || CERTS[0];
    if (!cert || !splitViewport || !splitRoot) return;
    splitSelectedCode = cert.code;

    /* Update header metadata in split pane */
    var metaEl = splitRoot.querySelector('[data-pdf-meta]');
    var titleEl = splitRoot.querySelector('[data-pdf-title]');
    var verifyEl = splitRoot.querySelector('[data-pdf-verify]');
    var dlEl = splitRoot.querySelector('[data-pdf-download]');
    var openEl = splitRoot.querySelector('[data-pdf-newtab]');
    var expandEl = splitRoot.querySelector('[data-pdf-expand]');

    if (metaEl) {
      metaEl.innerHTML = '';
      metaEl.appendChild(createIssuerEl(cert, true));
      var metaType = document.createElement('span');
      metaType.textContent = ' · ' + cert.typeLabel;
      metaEl.appendChild(metaType);
    }
    if (titleEl) titleEl.textContent = cert.title;
    if (verifyEl) verifyEl.href = cert.verifyUrl;
    if (dlEl) {
      dlEl.href = cert.pdf;
      dlEl.setAttribute('download', cert.filename);
    }
    if (openEl) openEl.href = cert.pdf;
    if (expandEl) expandEl.setAttribute('data-open-cert', cert.code);

    if (splitList) {
      splitList.querySelectorAll('.split-item').forEach(function (item) {
        var active = item.getAttribute('data-split-code') === cert.code;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-current', active ? 'true' : 'false');
      });
    }

    var idx = filteredCerts.indexOf(cert);
    var neighbors = [];
    if (idx >= 0) {
      if (filteredCerts[idx + 1]) neighbors.push(filteredCerts[idx + 1].pdf);
      if (filteredCerts[idx - 1]) neighbors.push(filteredCerts[idx - 1].pdf);
    }
    splitViewport.loadCert(cert, neighbors);
  }

  function renderSplitList() {
    if (!splitList) return;
    splitList.innerHTML = '';
    if (!filteredCerts.length) {
      var emptyMsg = document.createElement('div');
      emptyMsg.className = 'split-empty';
      emptyMsg.textContent = UI.noResults || 'No matching certificates.';
      splitList.appendChild(emptyMsg);
      return;
    }

    var frag = document.createDocumentFragment();
    filteredCerts.forEach(function (cert, i) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'split-item' + (cert.code === splitSelectedCode ? ' is-active' : '');
      btn.setAttribute('data-split-code', cert.code);
      btn.setAttribute('aria-current', cert.code === splitSelectedCode ? 'true' : 'false');

      var top = document.createElement('div');
      top.className = 'split-item-top';
      var iss = document.createElement('span');
      iss.className = 'split-item-issuer';
      iss.appendChild(createIssuerEl(cert, true));
      var tp = document.createElement('span');
      tp.className = 'split-item-date';
      tp.textContent = cert.typeLabel;
      top.appendChild(iss);
      top.appendChild(tp);

      var ttl = document.createElement('div');
      ttl.className = 'split-item-title';
      ttl.textContent = cert.title;

      btn.appendChild(top);
      btn.appendChild(ttl);

      if (cert.parentTitle) {
        var par = document.createElement('div');
        par.className = 'split-item-parent';
        par.textContent = cert.parentTitle;
        btn.appendChild(par);
      }

      btn.addEventListener('click', function () {
        setSplitActiveCert(cert.code);
      });
      frag.appendChild(btn);
    });
    splitList.appendChild(frag);
  }

  function applyFilters() {
    filteredCerts = CERTS.filter(matchesFilter);
    var visibleCodes = Object.create(null);
    filteredCerts.forEach(function (c) { visibleCodes[c.code] = true; });

    if (cardsGrid) {
      var cards = cardsGrid.querySelectorAll('[data-cert-code]');
      cards.forEach(function (card) {
        var code = card.getAttribute('data-cert-code');
        var show = !!visibleCodes[code];
        card.hidden = !show;
        if (show) card.classList.add('is-visible');
      });
    }

    if (countEl) {
      var tpl = UI.countTemplate || '{n} of {total}';
      countEl.textContent = tpl
        .replace('{n}', String(filteredCerts.length))
        .replace('{total}', String(CERTS.length));
    }

    if (emptyState) {
      emptyState.hidden = filteredCerts.length > 0;
    }

    if (clearSearchBtn) {
      clearSearchBtn.hidden = !filterState.query;
    }

    if (filterState.view === 'split') {
      renderSplitList();
      if (filteredCerts.length && !visibleCodes[splitSelectedCode]) {
        setSplitActiveCert(filteredCerts[0].code);
      }
    }
  }

  function setViewMode(mode) {
    filterState.view = mode === 'split' ? 'split' : 'cards';
    viewBtns.forEach(function (b) {
      var isAct = b.getAttribute('data-view-mode') === filterState.view;
      b.classList.toggle('is-active', isAct);
      b.setAttribute('aria-pressed', String(isAct));
    });

    if (cardsGrid) cardsGrid.hidden = filterState.view === 'split';
    if (splitShell) splitShell.hidden = filterState.view !== 'split';

    if (filterState.view === 'split') {
      renderSplitList();
      setSplitActiveCert(splitSelectedCode);
      if (splitViewport) {
        window.setTimeout(function () { splitViewport.refreshFit(); }, 60);
      }
    }
  }

  /* Bind Directory Filters */
  catTabs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterState.cat = btn.getAttribute('data-filter-cat') || 'all';
      catTabs.forEach(function (b) {
        var act = b === btn;
        b.classList.toggle('is-active', act);
        b.setAttribute('aria-selected', String(act));
      });
      applyFilters();
    });
  });

  issuerBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterState.issuer = btn.getAttribute('data-filter-issuer') || 'all';
      issuerBtns.forEach(function (b) {
        var act = b === btn;
        b.classList.toggle('is-active', act);
        b.setAttribute('aria-pressed', String(act));
      });
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', function () {
      filterState.query = searchInput.value.trim();
      applyFilters();
    });
  }

  if (clearSearchBtn) {
    clearSearchBtn.addEventListener('click', function () {
      if (searchInput) searchInput.value = '';
      filterState.query = '';
      applyFilters();
      if (searchInput) searchInput.focus();
    });
  }

  var resetBtn = document.getElementById('certsReset');
  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      filterState.cat = 'all';
      filterState.issuer = 'all';
      filterState.query = '';
      if (searchInput) searchInput.value = '';
      catTabs.forEach(function (b) {
        var act = b.getAttribute('data-filter-cat') === 'all';
        b.classList.toggle('is-active', act);
        b.setAttribute('aria-selected', String(act));
      });
      issuerBtns.forEach(function (b) {
        var act = b.getAttribute('data-filter-issuer') === 'all';
        b.classList.toggle('is-active', act);
        b.setAttribute('aria-pressed', String(act));
      });
      applyFilters();
    });
  }

  viewBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      setViewMode(btn.getAttribute('data-view-mode'));
    });
  });

  var heroReaderBtn = document.getElementById('openReaderModeBtn');
  if (heroReaderBtn) {
    heroReaderBtn.addEventListener('click', function () {
      if (window.innerWidth >= 960 && splitShell) {
        setViewMode('split');
        if (dirSection) dirSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } else {
        openModal(CERTS[0] ? CERTS[0].code : '', heroReaderBtn);
      }
    });
  }

  /* ── Theater Modal PDF Viewer ────────────────────────── */
  var modal = document.getElementById('pdfModal');
  var modalDialog = modal ? modal.querySelector('.pdf-modal-dialog') : null;
  var modalRail = document.getElementById('pdfModalRail');
  var modalToggleRail = document.getElementById('pdfToggleRail');
  var modalViewport = modal ? createPdfViewport({
    root: modal,
    defaultZoomMode: 'fit-page'
  }) : null;

  var modalState = {
    isOpen: false,
    queue: CERTS.slice(),
    activeIndex: 0,
    lastFocused: null
  };

  function renderModalRail() {
    if (!modalRail) return;
    modalRail.innerHTML = '';
    var frag = document.createDocumentFragment();
    modalState.queue.forEach(function (cert, idx) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'pdf-rail-item' + (idx === modalState.activeIndex ? ' is-active' : '');
      btn.setAttribute('data-rail-index', String(idx));

      var num = document.createElement('span');
      num.className = 'pdf-rail-num';
      num.textContent = (idx < 9 ? '0' : '') + (idx + 1);

      var info = document.createElement('span');
      info.className = 'pdf-rail-info';

      var ttl = document.createElement('span');
      ttl.className = 'pdf-rail-title';
      ttl.textContent = cert.title;

      var sub = document.createElement('span');
      sub.className = 'pdf-rail-sub';
      sub.appendChild(createIssuerEl(cert, true));
      var subType = document.createElement('span');
      subType.textContent = ' · ' + cert.typeLabel;
      sub.appendChild(subType);

      info.appendChild(ttl);
      info.appendChild(sub);
      btn.appendChild(num);
      btn.appendChild(info);

      btn.addEventListener('click', function () {
        selectModalIndex(idx);
      });
      frag.appendChild(btn);
    });
    modalRail.appendChild(frag);
  }

  function updateModalMetadata(cert) {
    if (!modal) return;
    var badgeEl = modal.querySelector('[data-modal-badge]');
    var titleEl = modal.querySelector('[data-modal-title]');
    var subEl = modal.querySelector('[data-modal-sub]');
    var verifyEl = modal.querySelector('[data-pdf-verify]');
    var dlEl = modal.querySelector('[data-pdf-download]');
    var openEl = modal.querySelector('[data-pdf-newtab]');
    var codeEl = modal.querySelector('[data-modal-code]');
    var parentEl = modal.querySelector('[data-modal-parent]');
    var counterEl = modal.querySelector('[data-modal-counter]');
    var prevBtn = modal.querySelector('[data-modal-nav="prev"]');
    var nextBtn = modal.querySelector('[data-modal-nav="next"]');

    if (badgeEl) {
      badgeEl.innerHTML = '';
      badgeEl.appendChild(createIssuerEl(cert, true));
      var bType = document.createElement('span');
      bType.textContent = ' · ' + cert.typeLabel;
      badgeEl.appendChild(bType);
    }
    if (titleEl) titleEl.textContent = cert.title;
    if (subEl) subEl.textContent = cert.catLabel || '';
    if (verifyEl) verifyEl.href = cert.verifyUrl;
    if (dlEl) {
      dlEl.href = cert.pdf;
      dlEl.setAttribute('download', cert.filename);
    }
    if (openEl) openEl.href = cert.pdf;
    if (codeEl) codeEl.textContent = cert.code;

    if (parentEl) {
      if (cert.parentCode && BY_PROG[cert.parentCode]) {
        var p = BY_PROG[cert.parentCode];
        parentEl.hidden = false;
        parentEl.textContent = (UI.partOf || 'Part of:') + ' ' + p.title;
        parentEl.setAttribute('data-open-cert', p.code);
      } else {
        parentEl.hidden = true;
      }
    }

    if (counterEl) {
      counterEl.textContent = (modalState.activeIndex + 1) + ' / ' + modalState.queue.length;
    }
    if (prevBtn) prevBtn.disabled = modalState.queue.length <= 1;
    if (nextBtn) nextBtn.disabled = modalState.queue.length <= 1;

    if (modalRail) {
      modalRail.querySelectorAll('.pdf-rail-item').forEach(function (item, i) {
        var act = i === modalState.activeIndex;
        item.classList.toggle('is-active', act);
        if (act) {
          item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      });
    }
  }

  function selectModalIndex(idx) {
    if (!modalState.queue.length || !modalViewport) return;
    var n = modalState.queue.length;
    modalState.activeIndex = ((idx % n) + n) % n;
    var cert = modalState.queue[modalState.activeIndex];
    updateModalMetadata(cert);
    updateUrlParam('cert', cert.code);

    var neighbors = [];
    if (n > 1) {
      neighbors.push(modalState.queue[(modalState.activeIndex + 1) % n].pdf);
      neighbors.push(modalState.queue[(modalState.activeIndex - 1 + n) % n].pdf);
    }
    modalViewport.loadCert(cert, neighbors);
  }

  function openModal(code, triggerEl) {
    if (!modal || !modalViewport) return;
    var cert = BY_CODE[(code || '').toUpperCase()];
    if (!cert) cert = CERTS[0];
    if (!cert) return;

    /* Use active filtered list if it contains the requested cert, otherwise full list */
    var inFiltered = filteredCerts.indexOf(cert) !== -1;
    modalState.queue = inFiltered && filteredCerts.length ? filteredCerts.slice() : CERTS.slice();
    modalState.activeIndex = Math.max(0, modalState.queue.indexOf(cert));
    modalState.lastFocused = triggerEl || document.activeElement;
    modalState.isOpen = true;

    renderModalRail();
    modal.hidden = false;
    document.documentElement.classList.add('pdf-modal-open');

    /* Allow layout frame before measuring stage dimensions */
    window.requestAnimationFrame(function () {
      modal.classList.add('is-open');
      selectModalIndex(modalState.activeIndex);
      var closeBtn = modal.querySelector('[data-modal-close]');
      if (closeBtn) closeBtn.focus();
    });
  }

  function closeModal() {
    if (!modal || !modalState.isOpen) return;
    modalState.isOpen = false;
    modal.classList.remove('is-open');
    document.documentElement.classList.remove('pdf-modal-open');
    updateUrlParam('cert', '');

    if (document.fullscreenElement === modalDialog && document.exitFullscreen) {
      try { document.exitFullscreen(); } catch (e) {}
    }

    window.setTimeout(function () {
      if (!modalState.isOpen) {
        modal.hidden = true;
      }
      if (modalState.lastFocused && typeof modalState.lastFocused.focus === 'function') {
        try { modalState.lastFocused.focus(); } catch (e) {}
      }
    }, 180);
  }

  function stepModal(dir) {
    selectModalIndex(modalState.activeIndex + dir);
  }

  if (modal) {
    modal.addEventListener('click', function (e) {
      if (e.target.closest('[data-modal-close]') || e.target === modal) {
        closeModal();
        return;
      }
      var navBtn = e.target.closest('[data-modal-nav]');
      if (navBtn) {
        var dir = navBtn.getAttribute('data-modal-nav') === 'next' ? 1 : -1;
        stepModal(dir);
        return;
      }
      var fsBtn = e.target.closest('[data-modal-fullscreen]');
      if (fsBtn && modalDialog && modalDialog.requestFullscreen) {
        if (document.fullscreenElement) {
          document.exitFullscreen();
        } else {
          modalDialog.requestFullscreen().catch(function () {});
        }
      }
    });

    if (modalToggleRail) {
      modalToggleRail.addEventListener('click', function () {
        var collapsed = modal.classList.toggle('is-rail-collapsed');
        modalToggleRail.setAttribute('aria-expanded', String(!collapsed));
        window.setTimeout(function () {
          if (modalViewport) modalViewport.refreshFit();
        }, 210);
      });
    }

    /* Touch swipe left/right inside modal header/backdrop area when not zoomed */
    var touchStart = null;
    var modalBody = modal.querySelector('.pdf-modal-main');
    if (modalBody) {
      modalBody.addEventListener('touchstart', function (e) {
        if (e.touches.length !== 1) return;
        var st = modalViewport.getState();
        if (st.zoomMode === 'custom' && st.scale > 1.05) return;
        touchStart = { x: e.touches[0].clientX, y: e.touches[0].clientY, t: Date.now() };
      }, { passive: true });
      modalBody.addEventListener('touchend', function (e) {
        if (!touchStart || e.changedTouches.length !== 1) return;
        var dx = e.changedTouches[0].clientX - touchStart.x;
        var dy = e.changedTouches[0].clientY - touchStart.y;
        var dt = Date.now() - touchStart.t;
        touchStart = null;
        if (dt < 450 && Math.abs(dx) > 64 && Math.abs(dx) > Math.abs(dy) * 1.6) {
          var goNext = IS_RTL ? dx > 0 : dx < 0;
          stepModal(goNext ? 1 : -1);
        }
      }, { passive: true });
    }
  }

  /* Global delegation for any [data-open-cert] button/link on the page */
  document.addEventListener('click', function (e) {
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey || e.button !== 0) return;
    var trigger = e.target.closest('[data-open-cert]');
    if (!trigger) return;
    var code = trigger.getAttribute('data-open-cert');
    if (!code) return;
    e.preventDefault();
    openModal(code, trigger);
  });

  /* Keyboard shortcuts & focus trap while Theater Modal is open */
  document.addEventListener('keydown', function (e) {
    if (!modalState.isOpen) return;
    if (e.key === 'Tab' && modalDialog) {
      var focusables = Array.prototype.slice.call(
        modalDialog.querySelectorAll('a[href]:not([hidden]), button:not([disabled]):not([hidden]), [tabindex]:not([tabindex="-1"])')
      ).filter(function (el) { return el.offsetParent !== null; });
      if (focusables.length) {
        var first = focusables[0];
        var last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
      return;
    }
    if (e.key === 'Escape') {
      e.preventDefault();
      closeModal();
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      stepModal(IS_RTL ? -1 : 1);
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      stepModal(IS_RTL ? 1 : -1);
    } else if (e.key === '+' || e.key === '=') {
      e.preventDefault();
      modalViewport.zoomBy(0.2);
    } else if (e.key === '-') {
      e.preventDefault();
      modalViewport.zoomBy(-0.2);
    } else if (e.key === '0') {
      e.preventDefault();
      modalViewport.setZoom('fit-page');
    } else if ((e.key === 'f' || e.key === 'F') && modalDialog && modalDialog.requestFullscreen) {
      e.preventDefault();
      if (document.fullscreenElement) document.exitFullscreen();
      else modalDialog.requestFullscreen().catch(function () {});
    }
  });

  /* ── Initialize from URL Query Parameters ────────────── */
  applyFilters();
  try {
    var params = new URLSearchParams(window.location.search);
    var catParam = params.get('category');
    if (catParam) {
      var matchingTab = document.querySelector('[data-filter-cat="' + catParam + '"]');
      if (matchingTab) matchingTab.click();
    }
    var viewParam = params.get('view');
    if (viewParam === 'reader' && window.innerWidth >= 960) {
      setViewMode('split');
    }
    var certParam = params.get('cert');
    if (certParam && BY_CODE[certParam.toUpperCase()]) {
      openModal(certParam.toUpperCase(), null);
    }
  } catch (e) {}
})();
