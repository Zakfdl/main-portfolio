# berrizak.com — Zakaria Fadl Portfolio

Bilingual (English / Arabic) portfolio site for Zakaria Fadl, Senior E-Commerce Specialist & Growth Director. Designed with an authentic gallery editorial aesthetic inspired by top creative directors and strategic portfolios (*Minimal Gallery*, *Siteinspire*, Tobias van Schneider, Paco Coursey).

## Folder Structure

```
/index.html                          English homepage
/ar/index.html                       Arabic homepage
/case-studies/index.html             Case studies index (English)
/case-studies/[slug]/index.html      Six English case-study pages
/ar/case-studies/index.html          Case studies index (Arabic)
/ar/case-studies/[slug]/index.html   Six Arabic case-study pages
/certificates/index.html             Organized certificates gallery & PDF viewer (English)
/ar/certificates/index.html          Organized certificates gallery & PDF viewer (Arabic)
/assets/css/styles.css               High-craft editorial stylesheet (Warm Alabaster Light + Studio Basalt Dark, LTR/RTL)
/assets/js/main.js                   Progressive-enhancement JS (theme toggle, mobile nav, scroll reveals, blueprint states, Formspree)
/assets/js/certs.js                  Certificates filtering, Split Reader mode & dual-engine PDF viewer
/assets/certificates/                26 verified Coursera certificate PDFs
/assets/images/                      Brand icons, favicon set, OG cover
/build_site.py                       Single generator script (regenerates all 19 HTML pages + sitemap.xml from data)
/robots.txt
/sitemap.xml
/404.html
/site.webmanifest
/README.md
```

Case-study slugs: `corner-filter`, `ghodoq-shark`, `altowayan`, `qeyam`, `taif-almasia`, `gmraa`.

## Design Philosophy

- **Authentic, Human, Creative:** Eliminates all generic AI tropes (no pitch-black/neon-green cyberpunk palettes, no fake macOS terminal dots, no simulated log consoles, no toy SaaS calculators).
- **Color System:** Warm Alabaster / Heavy Paper default canvas (`#FBF9F5`), deep architectural ink typography (`#121316`), tactile terracotta / burnt sienna accent (`#C4442C`), and warm studio basalt for dark mode (`#111215`).
- **Typography:** Refined, tight-tracked editorial sans (`Plus Jakarta Sans`) paired with modern, balanced Arabic typefaces (`IBM Plex Sans Arabic` and `Readex Pro`).
- **Executive Dossier:** Highlights the current appointment at **Ajlan & Bros Holding** alongside verified client outcomes across Saudi Arabia and the GCC.
- **Works Without JavaScript:** 100% of content, case studies, blueprints, and links are fully functional static HTML. JavaScript progressively enhances theme switching, scroll animations, and Formspree form submission.
- **Bilingual Architecture:** English at root (`/`); Arabic at `/ar/` with native `dir="rtl"` typography, layout mirrors, and complete `hreflang` alternates.

## Deploying to Hostinger

1. Download or use `berrizak_redesign.zip`.
2. **Log in to Hostinger hPanel** and open **Files → File Manager** for `berrizak.com`.
3. Navigate into `public_html/`.
4. Upload `berrizak_redesign.zip` and extract its contents directly into `public_html/`.
5. Verify `https://berrizak.com/` and `https://berrizak.com/ar/`.
