# -*- coding: utf-8 -*-
"""Static site generator for berrizak.com (EN + AR). Run: python build_site.py"""
import hashlib, json, os

OUT = os.path.dirname(os.path.abspath(__file__))

def asset_v(rel_path):
    p = os.path.join(OUT, rel_path)
    try:
        with open(p, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:8]
    except OSError:
        return "1"

CSS_V = asset_v("assets/css/styles.css")
MAIN_JS_V = asset_v("assets/js/main.js")
CERTS_JS_V = asset_v("assets/js/certs.js")
SITE = "https://berrizak.com/"
FORM = "https://formspree.io/f/xlgwyjar"
CV = "https://drive.google.com/file/d/1w4YUDUS22nG43a_o8UkP_7yZ_w_jPmtU/view?usp=sharing"
LI = "https://www.linkedin.com/in/zakaria-fadl-56b3b4384/"
WA = "https://wa.me/966570674043"

FONTS = ("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800"
         "&family=JetBrains+Mono:wght@500;600;700"
         "&family=Readex+Pro:wght@400;600;700;800"
         "&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap")

THEME_BOOT = ("<script>(function(){try{localStorage.removeItem('bz-theme');"
              "var t=localStorage.getItem('bz-light-theme');"
              "if(t!=='dark'){t='light';}"
              "document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>")

def svg(paths, size=20):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

ICON = {
    "cart": svg('<path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.6a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/>'),
    "funnel": svg('<path d="M3 4h18l-7 8.5V19l-4 2v-8.5z"/>'),
    "search": svg('<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>'),
    "chart": svg('<path d="M4 20V11M10 20V5M16 20v-8M21 20H3"/>'),
    "target": svg('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>'),
    "sync": svg('<path d="M20 12a8 8 0 0 1-14.3 4.9M4 12a8 8 0 0 1 14.3-4.9"/><path d="M18.5 3v4.2h-4.2M5.5 21v-4.2h4.2"/>'),
    "layout": svg('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 9v11"/>'),
    "compass": svg('<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>'),
    "doc": svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    "rail": svg('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16"/>'),
    "sun": '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "moon": '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
}

# ─────────────────────────── UI STRINGS ───────────────────────────
T = {
 "en": {
  "skip": "Skip to content", "role": "Senior E-Commerce Specialist", "menu": "Toggle menu", "theme": "Toggle colour theme",
  "nav": [("#work", "Work"), ("#approach", "Approach"), ("#experience", "Experience"), ("#capabilities", "Capabilities"), ("#services", "Services"), ("certificates/", "Certificates"), ("#contact", "Contact")],
  "nav_cs": "Case Studies",
  "home_title": "Zakaria Fadl | Senior E-Commerce Specialist & Growth Director — Saudi Arabia",
  "home_desc": "Senior E-Commerce Specialist with 6+ years scaling online stores across Salla, Shopify, Zid and WooCommerce in Saudi Arabia. CRO, analytics, SEO and GEO.",
  "eyebrow": "Senior E-Commerce Specialist · Ajlan & Bros Holding · Riyadh",
  "h1_name": "Zakaria Fadl",
  "h1a": "Scaling commerce systems.", "h1b": "Fixing funnel friction.",
  "hero_sub": "6+ years <strong>building, operating, and scaling</strong> high-performing online stores across Saudi Arabia and the GCC on Salla, Shopify, Zid, and WooCommerce. Transforming complex catalogs and fragmented channels into cohesive, high-converting revenue engines.",
  "cta_work": "Explore Selected Work ↓", "cta_cv": "Curriculum Vitae (PDF) ↗", "cta_wa": "WhatsApp",
  "tele": [("6", "+", "Years in GCC Commerce"), ("6", "", "Store Turnarounds"), ("4", "", "Core Platforms"), ("26", "", "Verified Credentials")],
  "dossier_label": "Executive Dossier & Focus",
  "dossier_badge": "Active Appointment",
  "dossier_co": "Ajlan & Bros Holding",
  "dossier_role": "Senior E-Commerce Specialist · April 2026 – Present",
  "dossier_scope": "Leading e-commerce strategy & ajstore.com optimization across KSA",
  "dossier_highlights_title": "Key Verified Outcomes",
  "dossier_foot_label": "GCC Commerce Focus: Salla · Shopify · Zid · WooCommerce",
  "dossier_view_all": "View all projects →",
  "platforms": "Operating Ecosystem",
  "work_tag": "Selected Work", "work_title": "Six Stores. Six Structural Bottlenecks.",
  "work_desc": "Real engagements across automotive parts, fitness, retail, medical devices, and home goods in Saudi Arabia. Each case study documents the diagnosis, the technical implementation, and the verified outcome.",
  "all_cs": "All Case Studies →", "read_cs": "Open Case Study →",
  "approach_tag": "Strategic Approach", "approach_title": "Operator First. Strategist Second.",
  "approach_lead": "I bridge technical store execution, behavioral analytics, and commercial revenue.",
  "about_p": [
    "One day that means building a complete GA4 and GTM tracking container from scratch; the next, architecting custom Excel automation to eliminate ERP inventory sync errors; the next, drafting an evidence-based CRO test from Clarity heatmaps.",
    "Working knowledge of <strong>HTML, CSS, and modern web architectures</strong> means I understand implementation, not just strategy — when I recommend a change to a product hierarchy or checkout flow, I know exactly what it takes to build it.",
    "I specialise in the Saudi and GCC market, with deep hands-on expertise in <strong>Salla</strong>, alongside Shopify, Zid, WooCommerce, and Amazon Marketplace."],
  "principles": [
    ("Funnel Diagnosis Before Ad Spend", "Pages and checkout funnels are judged by their effect on conversion — Clarity heatmaps, GA4 drop-off funnels, and structured A/B tests replace subjective opinions before scaling ad spend."),
    ("Measurement Built from Ground Zero", "You cannot optimize what you do not measure accurately. GA4 properties and GTM containers are built from scratch with custom e-commerce event triggers for solid attribution."),
    ("Technical SEO & GEO Readiness", "Structuring product catalogs, clean taxonomy, and structured schema to capture high-intent commercial search while ensuring discoverability across emerging AI answer engines."),
    ("Operational Automation & Data Reliability", "Eliminating inventory overselling and broken feeds between ERP systems and store platforms through automated data mapping and documented workflows.")],
  "exp_tag": "Career Journey", "exp_title": "Professional Experience", "exp_desc": "From e-commerce coordinator to senior specialist — scaling online stores in Saudi Arabia since 2019.",
  "cap_tag": "Capabilities", "cap_title": "Disciplines, Backed by Evidence", "cap_desc": "Grouped by core discipline, each linked to the client engagements where it was delivered — no self-rated skill bars.",
  "stack_cols": ["Platforms", "Analytics & Tracking", "SEO & Discovery", "Data & Automation"],
  "svc_tag": "Services", "svc_title": "Ways to Work Together", "svc_desc": "Full-time senior roles, strategic consulting projects, or fractional e-commerce leadership.",
  "cert_tag": "Credentials", "cert_title": "Verified Certifications", "cert_desc": "26 verified Coursera credentials across AI, SEO/GEO, Data Analytics, Python, and E-Commerce — with inline PDF previews and public verification links.",
  "cert_verified": "✓ verified", "all_certs": "All Certificates (26) →",
  "cert_preview": "Preview PDF", "cert_verify_btn": "Verify ↗", "cert_dl_btn": "Download PDF",
  "cert_archive_h": "Full Credential Vault & Interactive PDF Viewer",
  "cert_archive_sub": "3 flagship multi-course programs, 15 specialization courses, and 8 standalone courses & projects — searchable by topic and issuer.",
  "cert_archive_cta": "Open Certificates Page (26) →",
  "certs_page_title": "Certificates & Credentials | Verified PDF Archive — Zakaria Fadl",
  "certs_page_desc": "26 verified Coursera certificates by Google, IBM, Meta, SkillUp, and Coursera across AI, Technical SEO & GEO, Data Analytics, Python, and E-Commerce — with an inline PDF viewer.",
  "certs_page_tag": "Verified Credentials Archive",
  "certs_page_h1": "26 Verified Certificates & Credentials",
  "certs_page_lede": "Every certificate issued via Coursera — organized by specialization track and discipline, with instant inline PDF previewing, zoom controls, and direct verification links.",
  "certs_h": "Certificates",
  "certs_cta_reader": "Open Interactive PDF Reader",
  "certs_cta_browse": "Browse All 26 Credentials ↓",
  "certs_kpis": [("26", "Verified PDF Certificates"), ("3", "Flagship Multi-Course Programs"), ("5", "Issuing Partners (Google · IBM · Meta · SkillUp · Coursera)"), ("100%", "Publicly Verifiable on Coursera")],
  "certs_prog_tag": "Structured Learning Paths", "certs_prog_title": "Three Flagship Programs & Specializations",
  "certs_prog_desc": "Multi-course professional certificates and specializations where every individual module PDF is also included and previewable below.",
  "certs_dir_tag": "Complete Directory", "certs_dir_title": "All 26 Certificates",
  "certs_dir_desc": "Filter by discipline or issuer, search by keyword or verification ID, or switch to Split Reader mode to glide through PDFs side by side.",
  "certs_included": "Included Course Certificates",
  "certs_preview_prog": "Preview Program PDF",
  "certs_cats": [("all", "All"), ("ai", "AI & GenAI"), ("seo", "SEO & GEO"), ("data", "Data & Python"), ("ecommerce", "E-Commerce & Web")],
  "certs_issuers": [("all", "All"), ("google", "Google"), ("ibm", "IBM"), ("meta", "Meta"), ("skillup", "SkillUp"), ("coursera", "Coursera")],
  "certs_issuer_lbl": "Issuer:",
  "certs_search_ph": "Search title, skill, or verify ID…",
  "certs_view_cards": "Cards", "certs_view_split": "Split PDF Reader",
  "certs_count_tpl": "Showing {n} of {total} certificates",
  "certs_empty": "No certificates match the current filters.",
  "certs_reset": "Reset filters",
  "certs_part_of": "Part of",
  "pdf_fit_page": "Fit Page", "pdf_fit_width": "Fit Width",
  "pdf_zoom_in": "Zoom in", "pdf_zoom_out": "Zoom out",
  "pdf_new_tab": "New Tab ↗", "pdf_expand": "Theater ⤢", "pdf_rail": "Queue",
  "pdf_loading": "Rendering PDF…", "pdf_hints": "← → Navigate · + / − Zoom · 0 Fit · Esc Close",
  "pdf_prev_cert": "Previous certificate", "pdf_next_cert": "Next certificate", "pdf_close": "Close viewer",
  "ct_tag": "Direct Contact", "ct_title": "Have a store that should be converting better?",
  "ct_sub": "Scaling an existing store, launching a new flagship, or hiring an experienced operator — tell me what you are looking to achieve and I will reply within a working day.",
  "ct_phone": "Phone / WhatsApp", "ct_email": "Email", "ct_li": "LinkedIn",
  "form_h": "Send a Message", "form_name": "Full name", "form_email": "Email address", "form_msg": "What is happening with your store?",
  "form_priv": "Sent via Formspree. Used only to reply to your inquiry — never shared.", "form_send": "Send Message →",
  "form_sending": "Sending…", "form_ok": "Message sent successfully — I will get back to you shortly.", "form_err": "Something went wrong. Please email directly at zakfdl22@gmail.com.",
  "form_fb": "Prefer direct email? Write to", "footer": "Riyadh, Saudi Arabia · All rights reserved",
  "cs_index_title": "Case Studies | E-Commerce Results in Saudi Arabia — Zakaria Fadl",
  "cs_index_desc": "Six e-commerce engagements across Saudi Arabia — automotive parts, fitness, retail, medical, and home goods. Each page covers the diagnosis, the approach, the tools used, and the result.",
  "cs_index_h": "Case Studies", "home": "Home",
  "cs_sections": ["Context", "The Problem", "My Responsibility", "What Was Done", "Result", "How It Was Measured", "Strategic Takeaway"],
  "bp_caption": "Architectural system schematic: before vs. after implementation.",
  "side_tools": "Tools & Platforms", "side_exp": "Related Expertise", "side_rel": "Related Case Studies",
  "back": "← All Case Studies", "visit": "Visit Store", "cs_cta_h": "Facing a similar bottleneck?", "cs_cta_btn": "Let's Talk →",
  "e404_t": "Page Not Found", "e404_p": "This page may have moved or no longer exists.", "e404_b": "Back to Homepage",
 },
 "ar": {
  "skip": "الانتقال إلى المحتوى", "role": "أخصائي تجارة إلكترونية أول", "menu": "فتح القائمة", "theme": "تبديل نمط الألوان",
  "nav": [("#work", "الأعمال"), ("#approach", "المنهجية"), ("#experience", "المسيرة"), ("#capabilities", "القدرات"), ("#services", "الخدمات"), ("certificates/", "الشهادات"), ("#contact", "تواصل")],
  "nav_cs": "دراسات الحالة",
  "home_title": "زكريا فضل | أخصائي تجارة إلكترونية أول — السعودية",
  "home_desc": "أخصائي تجارة إلكترونية أول بخبرة تتجاوز 6 سنوات في تطوير المتاجر الإلكترونية عبر سلة وShopify وZid وWooCommerce في السعودية. تحسين معدل التحويل، والتحليلات، وتحسين محركات البحث.",
  "eyebrow": "أخصائي تجارة إلكترونية أول · مجموعة عجلان وإخوانه القابضة · الرياض",
  "h1_name": "زكريا فضل",
  "h1a": "بناء أنظمة التجارة الإلكترونية.", "h1b": "ومعالجة تسرب الإيرادات.",
  "hero_sub": "أكثر من 6 سنوات في <strong>بناء وتشغيل وتطوير</strong> المتاجر الإلكترونية في السعودية ودول الخليج عبر منصات سلة وShopify وZid وWooCommerce. تحويل الكتالوجات المعقدة والقنوات المتفرقة إلى محركات إيرادات متماسكة وعالية التحويل.",
  "cta_work": "استعرض الأعمال المختارة ↓", "cta_cv": "السيرة الذاتية (PDF) ↗", "cta_wa": "واتساب",
  "tele": [("6", "+", "سنوات في التجارة الإلكترونية"), ("6", "", "مشاريع متاجر موثقة"), ("4", "", "منصات رئيسية"), ("26", "", "شهادة مهنية موثقة")],
  "dossier_label": "الموجز التنفيذي والتركيز",
  "dossier_badge": "الموقع الحالي",
  "dossier_co": "مجموعة عجلان وإخوانه القابضة",
  "dossier_role": "أخصائي تجارة إلكترونية أول · أبريل 2026 – حتى الآن",
  "dossier_scope": "قيادة استراتيجية التجارة الإلكترونية وتطوير ajstore.com في السعودية",
  "dossier_highlights_title": "أبرز النتائج الموثقة",
  "dossier_foot_label": "نطاق السوق: السعودية والخليج · سلة · Shopify · زد · ووكومرس",
  "dossier_view_all": "استعرض كافة المشاريع ←",
  "platforms": "منظومة العمل والتقنيات",
  "work_tag": "أعمال مختارة", "work_title": "ستة متاجر. ستة أنواع من التسرّب الهيكلي.",
  "work_desc": "مشاريع واقعية في قطع غيار السيارات، واللياقة البدنية، والتجزئة، والأجهزة الطبية، والإنارة المنزلية في السعودية. توثق كل دراسة حالة التشخيص، والتنفيذ التقني، والنتائج المقاسة.",
  "all_cs": "جميع دراسات الحالة ←", "read_cs": "فتح دراسة الحالة ←",
  "approach_tag": "المنهجية الاستراتيجية", "approach_title": "منفّذ أولًا، ثم استراتيجي.",
  "approach_lead": "أربط بين التنفيذ التقني للمتاجر، والتحليلات السلوكية، والإيرادات التجارية.",
  "about_p": [
    "يومًا أبني حاوية GA4 وGoogle Tag Manager متكاملة من الصفر؛ وفي اليوم التالي أبتكر أداة أتمتة عبر Excel تقضي على أخطاء مزامنة المخزون مع نظام ERP؛ ثم أصوغ فرضية اختبار لتحسين التحويل مستندة إلى خرائط حرارة Clarity.",
    "المعرفة العملية بلغات <strong>HTML وCSS والتقنيات الحديثة</strong> تعني فهمًا عميقًا للتنفيذ وليس فقط الاستراتيجية — فعندما أوصي بتعديل بنية المنتجات أو مسار الدفع، أعرف تمامًا متطلبات بنائها تقنيًا.",
    "أتخصص في سوق السعودية ودول الخليج، بخبرة عملية عميقة في <strong>منصة سلة</strong>، إلى جانب Shopify وZid وWooCommerce وسوق أمازون."],
  "principles": [
    ("تشخيص مسار الشراء قبل الإنفاق الإعلاني", "تُقيَّم الصفحات ومسارات الدفع بأثرها على التحويل — خرائط حرارة Clarity ومسارات انخفاض الزوار في GA4 واختبارات A/B المنظمة تحل محل الآراء الشخصية قبل التوسع في الإعلانات."),
    ("بناء منظومة القياس من الصفر", "لا يمكن تحسين ما لا تقيسه بدقة. تُبنى خصائص GA4 وحاويات GTM من الصفر بأحداث تجارة إلكترونية مخصصة تضمن دقة نموذج النسب والتحليلات."),
    ("جاهزية SEO التقني ومحركات الذكاء الاصطناعي (GEO)", "تنظيم كتالوجات المنتجات والتصنيفات والبيانات المنظمة لاقتناص عمليات البحث عالية النية، وضمان قابلية الاكتشاف في محركات الإجابة بالذكاء الاصطناعي."),
    ("أتمتة العمليات وموثوقية البيانات", "القضاء على بيع منتجات غير متوفرة وتضارب البيانات بين نظام ERP والمتجر الإلكتروني عبر مسارات أتمتة وتوثيق دقيق لفرق العمليات.")],
  "exp_tag": "المسيرة المهنية", "exp_title": "الخبرات العملية", "exp_desc": "من منسّق تجارة إلكترونية إلى أخصائي أول — قيادة وتطوير المتاجر في السعودية منذ 2019.",
  "cap_tag": "القدرات", "cap_title": "تخصصات مدعومة بالأدلة", "cap_desc": "مصنّفة حسب التخصص، وكل منها مرتبط بالمشاريع التي طُبّقت فيها عمليًا — دون تقييمات ذاتية.",
  "stack_cols": ["المنصات", "التحليلات والتتبع", "محركات البحث والاكتشاف", "البيانات والأتمتة"],
  "svc_tag": "الخدمات", "svc_title": "طرق التعاون", "svc_desc": "أدوار قيادية بدوام كامل، أو مشاريع استشارية، أو قيادة جزئية للتجارة الإلكترونية.",
  "cert_tag": "المؤهلات", "cert_title": "الشهادات المهنية الموثقة", "cert_desc": "26 شهادة موثقة عبر Coursera في الذكاء الاصطناعي، وSEO وGEO، وتحليل البيانات وPython، والتجارة الإلكترونية — مع معاينة PDF مباشرة وروابط تحقق رسمية.",
  "cert_verified": "✓ موثقة", "all_certs": "جميع الشهادات (26) ←",
  "cert_preview": "معاينة PDF", "cert_verify_btn": "تحقق ↗", "cert_dl_btn": "تحميل PDF",
  "cert_archive_h": "أرشيف الشهادات الكامل وعارض PDF السلس",
  "cert_archive_sub": "3 برامج احترافية وتخصصات رئيسية، و15 شهادة دورات ضمن التخصصات، و8 دورات ومشاريع مستقلة — قابلة للتصفية والبحث والمعاينة الفورية.",
  "cert_archive_cta": "فتح صفحة الشهادات (26) ←",
  "certs_page_title": "الشهادات المهنية | أرشيف موثق مع عارض PDF — زكريا فضل",
  "certs_page_desc": "26 شهادة موثقة عبر Coursera من Google وIBM وMeta وSkillUp في الذكاء الاصطناعي، وSEO وGEO، وتحليل البيانات وPython، والتجارة الإلكترونية — مع عارض PDF تفاعلي سلس.",
  "certs_page_tag": "أرشيف المؤهلات الموثقة",
  "certs_page_h1": "26 شهادة مهنية ومؤهلًا موثقًا",
  "certs_page_lede": "جميع الشهادات الصادرة عبر Coursera — منظمة حسب البرامج التخصصية والمسارات المهنية، مع عارض PDF تفاعلي سلس وتكبير دقيق وروابط تحقق رسمية.",
  "certs_h": "الشهادات",
  "certs_cta_reader": "فتح عارض PDF التفاعلي",
  "certs_cta_browse": "تصفح جميع الشهادات (26) ↓",
  "certs_kpis": [("26", "شهادة PDF موثقة"), ("3", "برامج وشهادات تخصصية"), ("5", "جهات مانحة (Google · IBM · Meta · SkillUp · Coursera)"), ("100%", "قابلة للتحقق المباشر عبر Coursera")],
  "certs_prog_tag": "المسارات التخصصية", "certs_prog_title": "ثلاثة برامج احترافية وتخصصات رئيسية",
  "certs_prog_desc": "شهادات احترافية وتخصصات متعددة الدورات، مع إتاحة كل شهادة دورة فرعية للمعاينة الفورية بصيغة PDF أدناه.",
  "certs_dir_tag": "الدليل الكامل", "certs_dir_title": "جميع الشهادات (26)",
  "certs_dir_desc": "صفِّ حسب التخصص أو الجهة المانحة، أو ابحث بالاسم أو رمز التحقق، أو انتقل إلى وضع القراءة المقسم لمعاينة ملفات PDF بسلاسة.",
  "certs_included": "شهادات الدورات المشمولة",
  "certs_preview_prog": "معاينة شهادة البرنامج PDF",
  "certs_cats": [("all", "الكل"), ("ai", "الذكاء الاصطناعي"), ("seo", "SEO وGEO"), ("data", "البيانات وPython"), ("ecommerce", "التجارة والمنصات")],
  "certs_issuers": [("all", "الكل"), ("google", "Google"), ("ibm", "IBM"), ("meta", "Meta"), ("skillup", "SkillUp"), ("coursera", "Coursera")],
  "certs_issuer_lbl": "الجهة المانحة:",
  "certs_search_ph": "ابحث بالعنوان أو المهارة أو رمز التحقق…",
  "certs_view_cards": "البطاقات", "certs_view_split": "عارض PDF المقسم",
  "certs_count_tpl": "عرض {n} من أصل {total} شهادة",
  "certs_empty": "لا توجد شهادات مطابقة لخيارات البحث الحالية.",
  "certs_reset": "إعادة ضبط الفلاتر",
  "certs_part_of": "ضمن برنامج",
  "pdf_fit_page": "ملاءمة الصفحة", "pdf_fit_width": "ملاءمة العرض",
  "pdf_zoom_in": "تكبير", "pdf_zoom_out": "تصغير",
  "pdf_new_tab": "تبويب جديد ↗", "pdf_expand": "تكبير العارض ⤢", "pdf_rail": "القائمة",
  "pdf_loading": "جارٍ عرض ملف PDF…", "pdf_hints": "← → تنقل · + / − تكبير · 0 ملاءمة · Esc إغلاق",
  "pdf_prev_cert": "الشهادة السابقة", "pdf_next_cert": "الشهادة التالية", "pdf_close": "إغلاق العارض",
  "ct_tag": "تواصل مباشر", "ct_title": "هل لديك متجر يُفترض أن يحقق تحويلًا أفضل؟",
  "ct_sub": "توسيع متجر قائم، أو إطلاق متجر جديد، أو توظيف مسؤول تشغيل أول — أخبرني بما تسعى لتحقيقه وسأرد خلال يوم عمل.",
  "ct_phone": "الهاتف / واتساب", "ct_email": "البريد الإلكتروني", "ct_li": "لينكدإن",
  "form_h": "إرسال رسالة", "form_name": "الاسم الكامل", "form_email": "البريد الإلكتروني", "form_msg": "ما الذي يحدث في متجرك؟",
  "form_priv": "تُرسل عبر Formspree. تُستخدم فقط للرد على استفسارك — ولا تتم مشاركتها.", "form_send": "إرسال الرسالة ←",
  "form_sending": "جارٍ الإرسال…", "form_ok": "تم إرسال الرسالة بنجاح — سأتواصل معك قريبًا.", "form_err": "حدث خطأ ما. يرجى المراسلة مباشرة على zakfdl22@gmail.com.",
  "form_fb": "تفضّل المراسلة المباشرة؟ راسلني على", "footer": "الرياض، المملكة العربية السعودية · جميع الحقوق محفوظة",
  "cs_index_title": "دراسات الحالة | نتائج التجارة الإلكترونية في السعودية — زكريا فضل",
  "cs_index_desc": "ست مشاريع تجارة إلكترونية في السعودية — قطع غيار سيارات، ولياقة بدنية، وتجزئة، ومنتجات طبية، وإنارة منزلية. تغطي كل دراسة المشكلة، والأسلوب المتبع، والأدوات المستخدمة، والنتيجة.",
  "cs_index_h": "دراسات الحالة", "home": "الرئيسية",
  "cs_sections": ["السياق", "المشكلة الهيكلية", "مسؤوليتي", "ما تم تنفيذه", "النتيجة المقاسة", "طريقة القياس", "الدروس المستفادة"],
  "bp_caption": "مخطط بنية النظام: مقارنة بين قبل وبعد التنفيذ.",
  "side_tools": "الأدوات والمنصات", "side_exp": "خبرات ذات صلة", "side_rel": "دراسات حالة ذات صلة",
  "back": "→ جميع دراسات الحالة", "visit": "زيارة المتجر", "cs_cta_h": "تواجه مشكلة مشابهة؟", "cs_cta_btn": "لنتحدث ←",
  "e404_t": "الصفحة غير موجودة", "e404_p": "ربما نُقلت هذه الصفحة أو لم تعد موجودة.", "e404_b": "العودة للرئيسية",
 },
}

# ─────────────────────────── CASE STUDIES ───────────────────────────
CASES = [
 {
  "slug": "corner-filter", "url": "cornerfilter.sa", "platform": "Salla",
  "name": {"en": "Corner Filter", "ar": "كورنر فلتر"},
  "sector": {"en": "Automotive parts · Saudi Arabia", "ar": "قطع غيار السيارات · السعودية"},
  "seo_title": {"en": "Corner Filter Case Study | Automotive Parts E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة كورنر فلتر | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "A high-traffic Salla store for automotive filters where poor product discoverability was driving bounce and abandoned carts.",
           "ar": "متجر على منصة سلة لفلاتر السيارات يحظى بحركة زوار جيدة، لكن ضعف إمكانية اكتشاف المنتجات كان يرفع معدل الارتداد ويزيد من عربات التسوق المتروكة."},
  "result": {"en": "Product page engagement improved by an estimated 35%, alongside a reduction in bounce rate, following the navigation and filtering changes.",
             "ar": "تحسّن تفاعل المستخدمين مع صفحات المنتج بنسبة تقديرية بلغت 35%، إلى جانب انخفاض في معدل الارتداد، بعد إجراء التعديلات على التنقل والفلترة."},
  "card": {"kpi": "+35%", "kpi_lbl": {"en": "est. product-page engagement", "ar": "تفاعل تقديري مع صفحات المنتج"},
           "from": {"en": "Flat catalogue", "ar": "كتالوج غير منظم"}, "to": {"en": "Fitment-first filters", "ar": "فلترة حسب توافق المركبة"}},
  "kpis": [("+35%", {"en": "Est. product-page engagement", "ar": "تفاعل تقديري مع صفحات المنتج"}),
           ("↓", {"en": "Bounce rate after changes", "ar": "انخفاض معدل الارتداد"}),
           ("Clarity", {"en": "Heatmaps + session recordings", "ar": "خرائط حرارة وتسجيلات جلسات"}),
           ("Salla", {"en": "Platform", "ar": "المنصة"})],
  "bp": {"title": {"en": "Product discovery flow", "ar": "مسار اكتشاف المنتج"},
         "before": [("Category page", "Filters", "muted"), ("Long product grid", "No fitment filter", "bad"), ("Scroll → bounce", "Cart abandoned", "bad")],
         "before_ar": [("صفحة الفئة", "فلاتر", "muted"), ("قائمة منتجات طويلة", "دون فلترة حسب المركبة", "bad"), ("تمرير ← ارتداد", "عربة متروكة", "bad")],
         "after": [("Make", "Vehicle", "ok"), ("Model · Year", "Fitment", "ok"), ("Filter type", "Oil · Air · Cabin", "ok"), ("Matching parts", "Tracked in GA4", "ok")],
         "after_ar": [("الشركة المصنّعة", "المركبة", "ok"), ("الطراز · السنة", "التوافق", "ok"), ("نوع الفلتر", "زيت · هواء · مكيف", "ok"), ("القطع المطابقة", "مُتتبَّعة في GA4", "ok")]},
  "context": {"en": "Corner Filter sells automotive filters on Salla to a Saudi customer base that searches by precise vehicle fitment. The store had solid traffic, but the catalog and filtering system were not built for that kind of specificity.",
              "ar": "يبيع متجر كورنر فلتر فلاتر السيارات عبر منصة سلة لعملاء في السعودية يبحثون عادة عن توافق دقيق مع مركبتهم. كان المتجر يحظى بحركة زوار جيدة، لكن نظام التصنيف والفلترة لم يكن مصممًا لهذا المستوى من الدقة."},
  "problem": {"en": "Customers could not filter effectively to find the exact part they needed. In a category where fitment specificity is everything, that gap showed up as high bounce rates, shallow session depth, and abandoned carts despite adequate traffic.",
              "ar": "لم يكن بإمكان العملاء تصفية المنتجات بفعالية للوصول إلى القطعة المناسبة. وفي فئة منتجات تعتمد بالكامل على دقة التوافق، ظهرت هذه الفجوة في صورة معدل ارتداد مرتفع، وجلسات تصفح قصيرة، وعربات تسوق متروكة رغم وجود حركة زوار كافية."},
  "resp": {"en": "Owned the CRO and UX diagnosis for the catalog, navigation, and measurement setup.", "ar": "تولّيت تشخيص تجربة المستخدم وتحسين معدل التحويل للكتالوج والتنقل وإعداد قياس الأداء."},
  "done": {"en": ["Ran a UX audit using Microsoft Clarity heatmaps and session recordings to see exactly where users dropped off.", "Restructured navigation and the filtering system around how customers actually search for parts.", "Improved product page hierarchy and category architecture.", "Implemented GTM event tracking so the impact of each change could be measured precisely through GA4."],
           "ar": ["إجراء تدقيق لتجربة المستخدم باستخدام خرائط الحرارة وتسجيلات الجلسات من Microsoft Clarity لتحديد نقاط تسرب المستخدمين بدقة.", "إعادة هيكلة التنقل ونظام الفلترة بما يتوافق مع طريقة بحث العملاء الفعلية عن القطع.", "تحسين تسلسل صفحة المنتج وبنية الفئات.", "إعداد تتبع الأحداث عبر Google Tag Manager لقياس أثر كل تغيير بدقة من خلال GA4."]},
  "measured": {"en": "Measured through GA4 engagement and bounce-rate metrics across a before/after window, cross-referenced with Clarity session recordings.", "ar": "تم القياس من خلال مؤشرات التفاعل ومعدل الارتداد في GA4 عبر فترة مقارنة قبل وبعد التعديل، بالتوازي مع مراجعة تسجيلات الجلسات في Clarity."},
  "showed": {"en": "On high-SKU technical catalogs, filter usability often affects conversion earlier in the journey than checkout design does.", "ar": "في الكتالوجات التقنية ذات عدد المنتجات الكبير، تؤثر سهولة استخدام الفلاتر غالبًا على التحويل في مرحلة مبكرة من رحلة المستخدم أكثر من تصميم صفحة الدفع."},
  "tools": ["Salla", "Microsoft Clarity", "Google Analytics 4", "Google Tag Manager"],
  "expertise": {"en": ["Conversion Rate Optimization", "Analytics & Tracking"], "ar": ["تحسين معدل التحويل", "التحليلات والتتبع"]},
  "related": ["ghodoq-shark", "altowayan"],
 },
 {
  "slug": "ghodoq-shark", "url": "ghodoqshark.com", "platform": "Shopify",
  "name": {"en": "Ghadak Al-Sharq", "ar": "غدق الشرق"},
  "sector": {"en": "Fitness & sporting goods · Saudi Arabia", "ar": "اللياقة البدنية والمعدات الرياضية · السعودية"},
  "seo_title": {"en": "Ghadak Al-Sharq Case Study | Fitness & Sporting Goods E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة غدق الشرق | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "A competitive fitness brand with no digital strategy, minimal organic visibility, and paid campaigns running without attribution.",
           "ar": "علامة تجارية رياضية في سوق تنافسي دون استراتيجية رقمية واضحة، وحضور محدود في نتائج البحث العضوي، وحملات إعلانية مدفوعة تعمل دون نموذج نسب واضح."},
  "result": {"en": "Organic traffic increased by an estimated 40% in the months following the SEO work, and paid advertising return improved after the campaign restructure.",
             "ar": "ارتفعت الزيارات العضوية بنسبة تقديرية بلغت 40% في الأشهر التي تلت أعمال تحسين محركات البحث، كما تحسّن عائد الإعلانات المدفوعة بعد إعادة هيكلة الحملات."},
  "card": {"kpi": "+40%", "kpi_lbl": {"en": "est. organic traffic lift", "ar": "زيارات عضوية تقديرية"},
           "from": {"en": "Unattributed ad spend", "ar": "إنفاق دون نسب"}, "to": {"en": "Structured campaigns", "ar": "حملات مُهيكلة"}},
  "kpis": [("+40%", {"en": "Est. organic traffic", "ar": "زيارات عضوية تقديرية"}),
           ("↑", {"en": "Paid-ad return after restructure", "ar": "تحسّن عائد الإعلانات"}),
           ("SEO + Paid", {"en": "Scope", "ar": "النطاق"}),
           ("Shopify", {"en": "Platform", "ar": "المنصة"})],
  "bp": {"title": {"en": "Acquisition architecture", "ar": "بنية الاستحواذ"},
         "before": [("Ad spend", "One mixed campaign", "bad"), ("No exclusions", "Overlapping audiences", "bad"), ("Return unknown", "No attribution", "bad")],
         "before_ar": [("إنفاق إعلاني", "حملة واحدة مختلطة", "bad"), ("دون استبعاد", "جماهير متداخلة", "bad"), ("العائد مجهول", "دون نسب", "bad")],
         "after": [("Intent research", "Semrush · Ahrefs", "ok"), [("Search", "Brand / non-brand", "ok"), ("Meta", "Prospecting · retargeting", "ok"), ("Organic", "Technical SEO + content", "ok")], ("GA4 attribution", "ROAS by channel", "ok")],
         "after_ar": [("بحث نية الشراء", "Semrush · Ahrefs", "ok"), [("البحث", "علامة / عام", "ok"), ("Meta", "استهداف · إعادة استهداف", "ok"), ("عضوي", "SEO تقني + محتوى", "ok")], ("نسب GA4", "العائد لكل قناة", "ok")]},
  "context": {"en": "Ghadak Al-Sharq operates in a crowded fitness-brand category where paid media spend and organic search visibility both compound over time — or drain budget when they aren't structured correctly.",
              "ar": "تعمل غدق الشرق في فئة مزدحمة من العلامات التجارية الرياضية، حيث يتراكم أثر الإنفاق الإعلاني والحضور في نتائج البحث العضوي مع الوقت — أو يستنزف الميزانية إن لم تتم هيكلته بشكل صحيح."},
  "problem": {"en": "The brand had no digital strategy in place, almost no organic search presence, and paid campaigns that were burning budget with no way to measure real return.",
              "ar": "لم يكن لدى العلامة التجارية استراتيجية رقمية، وكان حضورها في نتائج البحث العضوي شبه معدوم، إلى جانب حملات مدفوعة تستهلك الميزانية دون إمكانية قياس العائد الفعلي منها."},
  "resp": {"en": "Built the brand's digital strategy from the ground up, covering SEO and paid media.", "ar": "بناء الاستراتيجية الرقمية للعلامة التجارية من الصفر، شاملةً تحسين محركات البحث والإعلانات المدفوعة."},
  "done": {"en": ["Conducted comprehensive keyword research aligned with buyer intent.", "Ran a technical SEO overhaul, fixing crawlability and on-page structure issues.", "Restructured paid campaigns with proper campaign architecture, exclusion audiences, and bid-strategy alignment.", "Established a content plan mapped to the funnel, from awareness through purchase intent."],
           "ar": ["إجراء بحث شامل عن الكلمات المفتاحية بما يتوافق مع نية الشراء لدى العملاء.", "تنفيذ تدقيق تقني شامل لتحسين محركات البحث، ومعالجة مشكلات الزحف وبنية الصفحات.", "إعادة هيكلة الحملات المدفوعة عبر بنية حملات صحيحة، وجماهير استبعاد، ومحاذاة استراتيجية المزايدة.", "وضع خطة محتوى متوافقة مع مراحل قمع المبيعات، من مرحلة الوعي وصولًا إلى نية الشراء."]},
  "measured": {"en": "Tracked via GA4 organic-traffic trends and platform-reported ROAS, compared across a before/after window.", "ar": "تم التتبع من خلال اتجاهات الزيارات العضوية في GA4 وعائد الإنفاق الإعلاني المسجّل في المنصات الإعلانية، بالمقارنة بين فترتي ما قبل وما بعد التعديل."},
  "showed": {"en": "Fixing attribution before scaling ad spend prevents budget from being wasted on channels that only look like they're working.", "ar": "معالجة نموذج نسب الأداء قبل زيادة الميزانية الإعلانية يمنع هدر الإنفاق على قنوات تبدو فعّالة دون أن تكون كذلك فعليًا."},
  "tools": ["Google Ads", "Meta Ads Manager", "Semrush", "Ahrefs", "Google Analytics 4", "Google Tag Manager"],
  "expertise": {"en": ["Search Engine Optimization", "Digital Marketing & Paid Media"], "ar": ["تحسين محركات البحث", "التسويق الرقمي والإعلانات المدفوعة"]},
  "related": ["altowayan", "qeyam"],
 },
 {
  "slug": "altowayan", "url": "altowayan.com", "platform": "Multi-platform",
  "name": {"en": "Al-Towayan", "ar": "الطويان"},
  "sector": {"en": "Retail · Saudi Arabia", "ar": "التجزئة · السعودية"},
  "seo_title": {"en": "Al-Towayan Case Study | Retail E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة الطويان | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "A store operating with no analytics or conversion tracking, and a product catalog with structural issues affecting both UX and SEO.",
           "ar": "متجر يعمل دون أي أدوات تحليلات أو تتبع للتحويلات، مع كتالوج منتجات يعاني من مشكلات بنيوية أثّرت على تجربة المستخدم وتحسين محركات البحث معًا."},
  "result": {"en": "The store moved from having no usable conversion data to complete funnel tracking across the purchase journey, surfacing UX issues within the first week that could then be addressed with evidence.",
             "ar": "انتقل المتجر من عدم وجود بيانات تحويل قابلة للاستخدام إلى تتبع كامل لمسار الشراء بأكمله، ما كشف عن مشكلات في تجربة المستخدم خلال الأسبوع الأول أمكن معالجتها استنادًا إلى بيانات فعلية."},
  "card": {"kpi": "0 → Full", "kpi_lbl": {"en": "funnel tracking coverage", "ar": "تغطية تتبع مسار الشراء"},
           "from": {"en": "Decisions by guesswork", "ar": "قرارات بالتخمين"}, "to": {"en": "Evidence in week one", "ar": "أدلة من الأسبوع الأول"}},
  "kpis": [("0 → Full", {"en": "Funnel tracking coverage", "ar": "تغطية تتبع مسار الشراء"}),
           ("Week 1", {"en": "UX issues surfaced", "ar": "رصد مشكلات تجربة المستخدم"}),
           ("GA4 + GTM", {"en": "Built from scratch", "ar": "بُنيت من الصفر"}),
           ("Catalog", {"en": "Restructured for crawlability", "ar": "أُعيدت هيكلته للفهرسة"})],
  "bp": {"title": {"en": "GA4 e-commerce event funnel", "ar": "مسار أحداث GA4 للتجارة الإلكترونية"},
         "before": [("view_item", "not tracked", "muted"), ("add_to_cart", "not tracked", "muted"), ("begin_checkout", "not tracked", "muted"), ("purchase", "not tracked", "muted")],
         "before_ar": [("view_item", "غير مُتتبَّع", "muted"), ("add_to_cart", "غير مُتتبَّع", "muted"), ("begin_checkout", "غير مُتتبَّع", "muted"), ("purchase", "غير مُتتبَّع", "muted")],
         "after": [("view_item", "GTM trigger", "ok"), ("add_to_cart", "GTM trigger", "ok"), ("begin_checkout", "Checkout steps", "ok"), ("purchase", "Confirmation", "ok")],
         "after_ar": [("view_item", "مشغّل GTM", "ok"), ("add_to_cart", "مشغّل GTM", "ok"), ("begin_checkout", "خطوات الدفع", "ok"), ("purchase", "تأكيد الشراء", "ok")]},
  "context": {"en": "Al-Towayan had been running without any measurement infrastructure — decisions about the store were being made without data to validate or guide them.",
              "ar": "كان متجر الطويان يعمل دون أي بنية تحتية للقياس، حيث كانت القرارات المتعلقة بالمتجر تُتخذ دون بيانات تدعمها أو توجّهها."},
  "problem": {"en": "No analytics, no conversion tracking, and a fragmented product catalog causing both UX friction and SEO inefficiency.",
              "ar": "غياب تام للتحليلات وتتبع التحويلات، إلى جانب كتالوج منتجات مجزأ تسبب في احتكاك بتجربة المستخدم وضعف في كفاءة تحسين محركات البحث."},
  "resp": {"en": "Built the store's measurement infrastructure from scratch and led the catalog restructuring alongside it.", "ar": "بناء البنية التحتية لقياس الأداء للمتجر من الصفر، وقيادة إعادة هيكلة الكتالوج بالتوازي معها."},
  "done": {"en": ["Set up GA4 with full e-commerce tracking.", "Built a GTM container with event triggers covering add-to-cart, checkout steps, and purchase confirmation.", "Integrated Search Console for organic-search visibility.", "Restructured the product catalog to address crawlability and indexation issues."],
           "ar": ["إعداد GA4 مع تتبع كامل للتجارة الإلكترونية.", "بناء حاوية Google Tag Manager بمشغّلات أحداث تغطي الإضافة إلى السلة، وخطوات الدفع، وتأكيد الشراء.", "ربط Search Console لمتابعة الظهور في نتائج البحث العضوي.", "إعادة هيكلة كتالوج المنتجات لمعالجة مشكلات الزحف والفهرسة."]},
  "measured": {"en": "Verified through GA4 exploration and funnel reports once the new tracking setup went live.", "ar": "تم التحقق من ذلك عبر تقارير الاستكشاف ومسار التحويل في GA4 فور تفعيل إعداد التتبع الجديد."},
  "showed": {"en": "Measurement infrastructure needs to come before optimization work, not after it — otherwise every recommendation is a guess.", "ar": "يجب أن تُبنى البنية التحتية للقياس قبل أعمال التحسين وليس بعدها، وإلا فإن أي توصية ستكون مجرد تخمين."},
  "tools": ["Google Analytics 4", "Google Tag Manager", "Search Console", "Semrush"],
  "expertise": {"en": ["Analytics & Tracking", "Technical SEO"], "ar": ["التحليلات والتتبع", "تحسين محركات البحث التقني"]},
  "related": ["qeyam", "taif-almasia"],
 },
 {
  "slug": "qeyam", "url": "qeyam.sa", "platform": "Salla",
  "name": {"en": "Qeyam", "ar": "قيم"},
  "sector": {"en": "Retail · Saudi Arabia", "ar": "التجزئة · السعودية"},
  "seo_title": {"en": "Qeyam Case Study | Retail E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة قيم | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "An inherited store with below-average conversion rates, fragmented marketplace integrations, and paid ads running without proper attribution.",
           "ar": "متجر تم استلامه بمعدلات تحويل أقل من المتوسط، وتكاملات متفرقة مع الأسواق الإلكترونية، وحملات إعلانية مدفوعة تعمل دون نموذج نسب دقيق."},
  "result": {"en": "The rebuild contributed to revenue growth across several sales channels, with conversion-rate improvements confirmed through structured A/B testing and improved paid-ad efficiency from better attribution.",
             "ar": "ساهمت إعادة البناء في تحقيق نمو في الإيرادات عبر عدة قنوات بيع، مع تأكيد تحسّن معدلات التحويل من خلال اختبارات A/B منهجية، إلى جانب تحسّن كفاءة الإعلانات المدفوعة بفضل نموذج نسب أدق."},
  "card": {"kpi": "A/B", "kpi_lbl": {"en": "validated conversion gains", "ar": "تحسينات تحويل مُثبتة باختبارات"},
           "from": {"en": "Channels in silos", "ar": "قنوات منعزلة"}, "to": {"en": "One growth system", "ar": "منظومة نمو موحّدة"}},
  "kpis": [("A/B", {"en": "Validated CRO improvements", "ar": "تحسينات تحويل مُثبتة"}),
           ("Multi-channel", {"en": "Revenue growth", "ar": "نمو الإيرادات"}),
           ("1", {"en": "Unified KPI dashboard", "ar": "لوحة مؤشرات موحّدة"}),
           ("Salla", {"en": "Platform", "ar": "المنصة"})],
  "bp": {"title": {"en": "Channel unification", "ar": "توحيد القنوات"},
         "before": [[("Salla store", "Own CRO guesses", "bad"), ("Marketplaces", "Inconsistent data", "bad"), ("Paid ads", "No attribution", "bad")], ("No single view", "Which channel pays?", "muted")],
         "before_ar": [[("متجر سلة", "تحسينات بالتخمين", "bad"), ("الأسواق الإلكترونية", "بيانات غير متسقة", "bad"), ("الإعلانات", "دون نسب", "bad")], ("لا رؤية موحّدة", "أي قناة تربح؟", "muted")],
         "after": [[("Salla store", "Hypothesis-driven A/B", "ok"), ("Marketplaces", "Unified data + pricing", "ok"), ("Paid ads", "Clear attribution", "ok")], ("KPI dashboard", "All channels, one place", "ok")],
         "after_ar": [[("متجر سلة", "اختبارات A/B بفرضيات", "ok"), ("الأسواق الإلكترونية", "بيانات وتسعير موحّد", "ok"), ("الإعلانات", "نسب واضح", "ok")], ("لوحة المؤشرات", "كل القنوات في مكان واحد", "ok")]},
  "context": {"en": "Stepping into the Senior E-Commerce Specialist role at Qeyam meant inheriting a store where several growth levers — CRO, marketplaces, and paid media — were each working in isolation, without a unifying strategy.",
              "ar": "تولي منصب أخصائي التجارة الإلكترونية الأول في قيم عنى استلام متجر كانت فيه عدة أدوات نمو — تحسين معدل التحويل، والأسواق الإلكترونية، والإعلانات المدفوعة — تعمل كل منها بمعزل عن الأخرى دون استراتيجية موحّدة."},
  "problem": {"en": "Below-average conversion rates across the board, marketplace integrations operating without a unified strategy, and paid campaigns with no proper attribution — making it hard to tell which channels were actually profitable.",
              "ar": "معدلات تحويل أقل من المتوسط بشكل عام، وتكاملات مع الأسواق الإلكترونية تعمل دون استراتيجية موحّدة، وحملات مدفوعة دون نموذج نسب واضح — ما جعل من الصعب تحديد القنوات المربحة فعليًا."},
  "resp": {"en": "As Senior E-Commerce Specialist, led a full growth-strategy rebuild across CRO, marketplaces, and paid media.", "ar": "بصفتي أخصائي التجارة الإلكترونية الأول، قدت عملية إعادة بناء كاملة لاستراتيجية النمو شملت تحسين التحويل والأسواق الإلكترونية والإعلانات المدفوعة."},
  "done": {"en": ["Rebuilt the CRO framework around systematic, hypothesis-driven testing.", "Unified marketplace integrations with consistent product data and pricing logic across channels.", "Rebuilt paid ad campaigns with clearer attribution and audience strategy.", "Established KPI dashboards giving visibility across all channels in one place."],
           "ar": ["إعادة بناء إطار عمل تحسين التحويل استنادًا إلى اختبارات منهجية قائمة على الفرضيات.", "توحيد تكاملات الأسواق الإلكترونية عبر بيانات منتجات ومنطق تسعير متسق بين القنوات.", "إعادة بناء حملات الإعلانات المدفوعة بنسب أوضح واستراتيجية جماهير محددة.", "إعداد لوحات مؤشرات أداء رئيسية توفّر رؤية موحّدة عبر جميع القنوات."]},
  "measured": {"en": "Tracked through KPI dashboards covering channel-level revenue and conversion rate across a before/after comparison window.", "ar": "تم التتبع عبر لوحات مؤشرات الأداء الرئيسية التي تغطي الإيرادات ومعدل التحويل على مستوى كل قناة، بالمقارنة بين فترتي ما قبل وما بعد إعادة البناء."},
  "showed": {"en": "Unifying marketplace data quality is often a prerequisite for reliable attribution — you can't trust the numbers until the channels agree with each other.", "ar": "توحيد جودة بيانات الأسواق الإلكترونية غالبًا ما يكون شرطًا أساسيًا لدقة نموذج النسب — إذ لا يمكن الوثوق بالأرقام حتى تتفق القنوات مع بعضها البعض."},
  "tools": ["Salla", "Google Ads", "Meta Ads Manager", "Google Analytics 4", "Google Tag Manager"],
  "expertise": {"en": ["Growth Strategy", "Marketplace Management", "Conversion Rate Optimization"], "ar": ["استراتيجية النمو", "إدارة الأسواق الإلكترونية", "تحسين معدل التحويل"]},
  "related": ["taif-almasia", "gmraa"],
 },
 {
  "slug": "taif-almasia", "url": "taifalmasia.com", "platform": "Multi-platform",
  "name": {"en": "Taif Almasia Medical Company", "ar": "شركة طيف الماسية الطبية"},
  "sector": {"en": "Medical products · Saudi Arabia", "ar": "المنتجات الطبية · السعودية"},
  "seo_title": {"en": "Taif Almasia Case Study | Medical Products E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة شركة طيف الماسية الطبية | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "An ERP and online store that were perpetually out of sync, causing overselling and hours of manual reconciliation every week.",
           "ar": "نظام تخطيط موارد المؤسسة (ERP) والمتجر الإلكتروني كانا في حالة عدم تزامن مستمر، ما تسبب في بيع منتجات غير متوفرة واستهلاك ساعات أسبوعية للتسوية اليدوية."},
  "result": {"en": "Manual reconciliation effort was reduced by an estimated 70% per week, and data accuracy improved to near-zero sync errors after the automation was deployed.",
             "ar": "انخفض جهد التسوية اليدوية بنسبة تقديرية بلغت 70% أسبوعيًا، وتحسّنت دقة البيانات لتصل إلى أخطاء تزامن شبه معدومة بعد تفعيل الأداة."},
  "card": {"kpi": "−70%", "kpi_lbl": {"en": "est. weekly manual reconciliation", "ar": "تسوية يدوية أسبوعية (تقديري)"},
           "from": {"en": "Overselling stock", "ar": "بيع منتجات غير متوفرة"}, "to": {"en": "Near-zero sync errors", "ar": "أخطاء تزامن شبه معدومة"}},
  "kpis": [("−70%", {"en": "Est. weekly manual reconciliation", "ar": "تسوية يدوية أسبوعية (تقديري)"}),
           ("≈0", {"en": "Sync errors after rollout", "ar": "أخطاء تزامن بعد التفعيل"}),
           ("Excel", {"en": "No middleware cost", "ar": "دون تكلفة برمجيات وسيطة"}),
           ("Docs", {"en": "Team-maintainable workflow", "ar": "سير عمل يصونه الفريق"})],
  "bp": {"title": {"en": "ERP → store sync pipeline", "ar": "مسار مزامنة ERP ← المتجر"},
         "before": [("ERP export", "Raw format", "muted"), ("Manual copy", "Hours every week", "bad"), ("Online store", "Overselling · missed orders", "bad")],
         "before_ar": [("تصدير ERP", "صيغة خام", "muted"), ("نسخ يدوي", "ساعات أسبوعيًا", "bad"), ("المتجر الإلكتروني", "بيع غير متوفر · طلبات مفقودة", "bad")],
         "after": [("ERP export", "Raw format", "ok"), ("Clean & map", "Excel automation", "ok"), ("Validation", "Anomalies caught", "ok"), ("Store import", "Accurate stock", "ok")],
         "after_ar": [("تصدير ERP", "صيغة خام", "ok"), ("تنظيف ومطابقة", "أتمتة Excel", "ok"), ("التحقق", "رصد التباينات", "ok"), ("رفع للمتجر", "مخزون دقيق", "ok")]},
  "context": {"en": "Taif Almasia Medical Company's online store depended on inventory counts flowing correctly from its ERP system. When that sync broke down, it created direct operational and customer-trust problems.",
              "ar": "اعتمد المتجر الإلكتروني لشركة طيف الماسية الطبية على تدفق دقيق لبيانات المخزون من نظام تخطيط موارد المؤسسة. وعندما تعطّل هذا التزامن، نتجت عنه مشكلات تشغيلية مباشرة وتأثير سلبي على ثقة العملاء."},
  "problem": {"en": "The ERP system and online store were regularly out of sync — causing overselling of out-of-stock medical products, missed orders, and the operations team spending hours every week manually reconciling data between the two systems.",
              "ar": "كان نظام تخطيط الموارد والمتجر الإلكتروني يخرجان عن التزامن بشكل متكرر، ما تسبب في بيع منتجات طبية غير متوفرة فعليًا، وطلبات مفقودة، وإنفاق فريق العمليات ساعات أسبوعيًا في تسوية البيانات يدويًا بين النظامين."},
  "resp": {"en": "Designed and built the reconciliation tool that closed the gap between the two systems.", "ar": "تصميم وبناء أداة التسوية التي سدّت الفجوة بين النظامين."},
  "done": {"en": ["Analyzed the data structure and export formats of both the ERP system and the store platform.", "Built a custom Excel-based automation tool that pulled ERP exports, cleaned and mapped the data to the store's required format, and enabled fast, accurate syncing.", "Added validation checks to catch anomalies before they were pushed live.", "Documented the full workflow so the operations team could maintain it independently."],
           "ar": ["تحليل بنية البيانات وصيغ التصدير في كل من نظام ERP ومنصة المتجر.", "بناء أداة أتمتة مخصصة عبر Excel تسحب بيانات التصدير من ERP، وتنظفها وتطابقها مع الصيغة المطلوبة للمتجر، وتمكّن من التزامن السريع والدقيق.", "إضافة عمليات تحقق لرصد أي تباينات قبل رفعها إلى المتجر مباشرة.", "توثيق سير العمل بالكامل ليتمكن فريق العمليات من صيانته بشكل مستقل."]},
  "measured": {"en": "Compared weekly reconciliation hours logged by the operations team before and after the tool's rollout.", "ar": "تمت المقارنة بين ساعات التسوية الأسبوعية المسجّلة من فريق العمليات قبل تفعيل الأداة وبعده."},
  "showed": {"en": "A well-documented spreadsheet tool can solve a real integration problem without the cost or lead time of middleware software.", "ar": "يمكن لأداة جداول بيانات موثقة بعناية أن تحل مشكلة تكامل حقيقية دون تكلفة أو وقت انتظار برمجيات الربط الوسيطة."},
  "tools": ["Excel (Advanced)", "ERP data mapping", "Process documentation"],
  "expertise": {"en": ["Operations & Automation", "Data Reconciliation"], "ar": ["العمليات والأتمتة", "تسوية البيانات"]},
  "related": ["gmraa", "corner-filter"],
 },
 {
  "slug": "gmraa", "url": "gmraa.com", "platform": "Salla",
  "name": {"en": "Gmraa", "ar": "قمراء للإنارة"},
  "sector": {"en": "Home lighting · Saudi Arabia", "ar": "الإنارة المنزلية · السعودية"},
  "seo_title": {"en": "Gmraa Case Study | Home Lighting E-Commerce Results — Zakaria Fadl", "ar": "دراسة حالة قمراء للإنارة | نتائج التجارة الإلكترونية — زكريا فضل"},
  "lede": {"en": "A new Saudi lighting store launching on Salla with a high-SKU catalog and no SEO or analytics foundation in place.",
           "ar": "متجر إنارة سعودي جديد يتم إطلاقه على منصة سلة بكتالوج كبير من المنتجات، دون أي أساس لتحسين محركات البحث أو التحليلات."},
  "result": {"en": "The store launched with an SEO architecture, full conversion tracking, and a catalog structured for both navigation and search-engine indexing already in place — avoiding the technical debt that builds up when these foundations are added after launch.",
             "ar": "أُطلق المتجر ببنية تحسين محركات بحث جاهزة، وتتبع كامل للتحويلات، وكتالوج منظم لخدمة التنقل والفهرسة معًا منذ البداية — ما جنّب المتجر الدين التقني الذي يتراكم عادة عند إضافة هذه الأسس بعد الإطلاق."},
  "card": {"kpi": "Day 1", "kpi_lbl": {"en": "tracking + SEO live at launch", "ar": "تتبع وSEO جاهزان عند الإطلاق"},
           "from": {"en": "Unstructured catalogue", "ar": "كتالوج غير منظم"}, "to": {"en": "Launch-ready foundation", "ar": "أساس جاهز للإطلاق"}},
  "kpis": [("Day 1", {"en": "Tracking live at launch", "ar": "تتبع مفعّل عند الإطلاق"}),
           ("4", {"en": "Category pillars", "ar": "فئات رئيسية"}),
           ("Schema", {"en": "Structured data + sitemap", "ar": "بيانات منظمة + خريطة موقع"}),
           ("Salla", {"en": "Platform", "ar": "المنصة"})],
  "bp": {"title": {"en": "Pre-launch foundation", "ar": "أساس ما قبل الإطلاق"},
         "before": [("High-SKU catalogue", "No structure", "bad"), ("No analytics", "Blind launch", "bad"), ("No SEO base", "Retrofit later", "bad")],
         "before_ar": [("كتالوج كبير", "دون بنية", "bad"), ("دون تحليلات", "إطلاق دون رؤية", "bad"), ("دون أساس SEO", "إصلاح لاحق مكلف", "bad")],
         "after": [("Gmraa", "Salla", "ok"), [("Chandeliers", "", "ok"), ("Indoor", "", "ok"), ("Outdoor", "", "ok"), ("Spotlights", "", "ok")], [("GA4 + GTM", "E-commerce events", "ok"), ("Schema + sitemap", "Core Web Vitals", "ok")]],
         "after_ar": [("قمراء", "سلة", "ok"), [("ثريات", "", "ok"), ("إنارة داخلية", "", "ok"), ("إنارة خارجية", "", "ok"), ("سبوت لايت", "", "ok")], [("GA4 + GTM", "أحداث التجارة", "ok"), ("Schema + خريطة", "Core Web Vitals", "ok")]]},
  "context": {"en": "Gmraa (قمراء للإنارة) entered a competitive lighting category on Salla with a catalog spanning chandeliers, indoor and outdoor fixtures, and spotlights — needing structure and tracking in place from day one rather than retrofitted later.",
              "ar": "دخلت قمراء للإنارة فئة تنافسية في مجال الإنارة عبر منصة سلة، بكتالوج يشمل الثريات والإنارة الداخلية والخارجية وأجهزة السبوت لايت، وكانت بحاجة إلى بنية تصنيف وتتبع منذ اليوم الأول بدلًا من إضافتها لاحقًا."},
  "problem": {"en": "No SEO foundation, no analytics, and a high-SKU catalog that needed proper structure before launch rather than after.",
              "ar": "غياب تام لأساس تحسين محركات البحث والتحليلات، مع كتالوج كبير من المنتجات كان بحاجة إلى بنية تصنيف صحيحة قبل الإطلاق وليس بعده."},
  "resp": {"en": "Built the store's full digital foundation ahead of launch on Salla.", "ar": "بناء الأساس الرقمي الكامل للمتجر قبل إطلاقه على منصة سلة."},
  "done": {"en": ["Organized the product catalog into categories aligned with how Saudi buyers actually search (chandeliers, indoor lighting, outdoor lighting, spotlights).", "Set up GA4 and GTM with complete e-commerce event tracking ahead of launch.", "Optimized product page structure and metadata for search visibility.", "Implemented a technical SEO foundation, including sitemap, structured data, and Core Web Vitals improvements."],
           "ar": ["تنظيم كتالوج المنتجات في فئات تعكس طريقة بحث المشترين السعوديين الفعلية (ثريات، إنارة داخلية، إنارة خارجية، سبوت لايت).", "إعداد GA4 وGoogle Tag Manager بتتبع كامل لأحداث التجارة الإلكترونية قبل الإطلاق.", "تحسين بنية صفحات المنتجات والبيانات الوصفية لتعزيز الظهور في نتائج البحث.", "بناء أساس تقني لتحسين محركات البحث، شمل خريطة الموقع والبيانات المنظمة وتحسينات Core Web Vitals."]},
  "measured": {"en": "Verified through Search Console indexation status and live GA4 tracking confirmed active at launch.", "ar": "تم التحقق من ذلك عبر حالة الفهرسة في Search Console وتأكيد عمل تتبع GA4 مباشرة عند الإطلاق."},
  "showed": {"en": "Building tracking and SEO foundations before launch avoids retrofitting work that is far more expensive once a catalog and its indexation are already live.", "ar": "بناء أسس التتبع وتحسين محركات البحث قبل الإطلاق يجنّب إعادة العمل التي تكون أكثر تكلفة بكثير بعد أن يكون الكتالوج وفهرسته قد أصبحا مباشرين بالفعل."},
  "tools": ["Salla", "Google Analytics 4", "Google Tag Manager", "Structured Data"],
  "expertise": {"en": ["Technical SEO", "Store Launch & Catalog Architecture"], "ar": ["تحسين محركات البحث التقني", "إطلاق المتاجر وبنية الكتالوج"]},
  "related": ["corner-filter", "ghodoq-shark"],
 },
]
BY_SLUG = {c["slug"]: c for c in CASES}

EXPERIENCE = [
 {"date": {"en": "Apr 2026 – Present", "ar": "أبريل 2026 – حتى الآن"}, "co": {"en": "Ajlan & Bros Holding", "ar": "مجموعة عجلان وإخوانه القابضة"}, "role": {"en": "Senior E-Commerce Specialist", "ar": "أخصائي تجارة إلكترونية أول"},
  "pts": {"en": ["Leading e-commerce strategy and operations for Ajlan & Bros Holding's enterprise digital transformation initiative.", "Managing and scaling ajstore.com — optimizing product taxonomy, checkout flow, and multi-category conversion rates.", "Architecting unified GA4 and GTM measurement infrastructure to ensure full attribution across marketing channels.", "Directing multi-channel acquisition roadmaps aligned with commercial revenue targets in Saudi Arabia."],
          "ar": ["قيادة استراتيجية وعمليات التجارة الإلكترونية ضمن مبادرة التحول الرقمي لمجموعة عجلان وإخوانه القابضة.", "إدارة وتطوير متجر ajstore.com — تحسين كتالوج المنتجات، وتعزيز تجربة المستخدم، ورفع معدلات التحويل.", "تطبيق أنظمة تحليلات وتتبع لقياس الأداء وتحديد فرص النمو عبر مختلف القنوات.", "تطوير استراتيجيات تسويق رقمي عبر عدة قنوات لدعم ظهور العلامة التجارية واكتساب العملاء في المملكة."]},
  "tags": ["ajstore.com", "E-Commerce Strategy", "Analytics", "CRO", "SEO", "GA4", "GTM"]},
 {"date": {"en": "Feb 2025 – Jan 2026", "ar": "فبراير 2025 – يناير 2026"}, "co": {"en": "Qeyam.sa", "ar": "قيم (qeyam.sa)"}, "role": {"en": "Senior E-Commerce Specialist", "ar": "أخصائي تجارة إلكترونية أول"},
  "pts": {"en": ["Led end-to-end e-commerce operations and growth strategy, owning the commercial roadmap from performance media to on-site UX.", "Managed multi-platform advertising campaigns across Google and Meta, focusing on ROAS and acquisition cost efficiency.", "Implemented systematic CRO testing frameworks — refining checkout flows, product page layouts, and conversion funnels.", "Synchronized multi-channel marketplace integrations to ensure pricing and inventory consistency across platforms."],
          "ar": ["قيادة عمليات التجارة الإلكترونية واستراتيجية النمو بصفتي الأخصائي الأول، وتولي خارطة الطريق من التسويق الأدائي إلى تجربة المستخدم.", "إدارة حملات الإعلانات المدفوعة عبر جوجل ومنصات التواصل الاجتماعي، مع التركيز على نموذج النسب وخفض تكلفة اكتساب العملاء.", "تطبيق أطر عمل منهجية لتحسين معدل التحويل — اختبار مسارات الدفع، وتخطيطات صفحات المنتج، ودعوات اتخاذ الإجراء.", "التنسيق مع شركاء التطوير لدمج قوائم الأسواق الإلكترونية والحفاظ على تناسق بيانات المنتجات عبر القنوات."]},
  "tags": ["Salla", "Google Ads", "Meta Ads", "CRO", "GTM", "GA4", "A/B Testing"]},
 {"date": {"en": "Jan 2023 – Feb 2025", "ar": "يناير 2023 – فبراير 2025"}, "co": {"en": "Taif Almasia Medical Company", "ar": "شركة طيف الماسية الطبية"}, "role": {"en": "E-Commerce Specialist", "ar": "أخصائي تجارة إلكترونية"},
  "pts": {"en": ["Managed online store operations across product catalogs, inventory accuracy, and multi-channel fulfillment.", "Engineered an automated Excel data-pipeline between the company ERP and online store, cutting weekly manual reconciliation effort by 70%.", "Executed technical SEO and organic visibility strategy while monitoring customer acquisition economics.", "Collaborated with clinical and operational teams to align digital store workflows with medical compliance requirements."],
          "ar": ["إدارة عمليات المتجر الإلكتروني من الطلب إلى التسليم — كتالوج المنتجات، ودقة المخزون، وأداء المنصة.", "بناء أداة أتمتة مخصصة عبر Excel لمزامنة بيانات نظام تخطيط الموارد مع المتجر الإلكتروني، ما خفّض جهد التسوية اليدوية بنسبة تقديرية بلغت 70%.", "تطبيق استراتيجية تحسين محركات البحث وتحليلات الأداء لمتابعة تكلفة اكتساب العملاء مع مرور الوقت.", "التعاون مع فرق متعددة الوظائف لمواءمة العمليات الرقمية مع أهداف العمل ومتطلبات التقارير."]},
  "tags": ["Excel (Advanced)", "CRO", "SEO / GEO", "Analytics", "ERP Integration"]},
 {"date": {"en": "2019 – 2022", "ar": "2019 – 2022"}, "co": {"en": "La Secta Beauty", "ar": "لا سيكتا بيوتي (La Secta Beauty)"}, "role": {"en": "E-Commerce Coordinator", "ar": "منسّق تجارة إلكترونية"},
  "pts": {"en": ["Managed daily store operations — catalog updates, promotional campaigns, inventory tracking, and visual merchandising.", "Optimized Shopify applications and store user experience to increase repeat purchase rates.", "Maintained Amazon Marketplace product listings with emphasis on buy-box retention, keyword indexation, and review velocity.", "Coordinated digital media campaigns across social platforms to support product launches."],
          "ar": ["إدارة العمليات اليومية للمتجر — تحديث المنتجات، ونشر المحتوى، ومتابعة المخزون، والحملات الترويجية.", "تحسين تطبيقات Shopify وتجربة المستخدم في المتجر لتقليل الاحتكاك وزيادة معدل الشراء المتكرر.", "إدارة قوائم المنتجات على أمازون مع التركيز على جودة المحتوى وتحسين الكلمات المفتاحية وأداء صندوق الشراء.", "تنسيق حملات التسويق الرقمي عبر منصات التواصل الاجتماعي."]},
  "tags": ["Shopify", "Amazon", "CRM", "Social Media", "Content Marketing"]},
]

CAPS = [
 ("cart", {"en": "E-Commerce Operations", "ar": "عمليات التجارة الإلكترونية"}, {"en": "Managing Salla, Shopify, Zid, and WooCommerce stores end-to-end — catalog architecture, inventory management, and platform migrations.", "ar": "تشغيل متاجر سلة وShopify وZid وWooCommerce من الألف إلى الياء — إدارة الكتالوج، والمخزون، وترحيل المنصات."}, {"en": "Corner Filter · Qeyam · Gmraa · Taif Almasia · La Secta", "ar": "كورنر فلتر · قيم · قمراء · طيف الماسية · La Secta"}),
 ("funnel", {"en": "Conversion Rate Optimization (CRO)", "ar": "تحسين معدل التحويل (CRO)"}, {"en": "Evidence-driven CRO using Microsoft Clarity heatmaps, GA4 drop-off funnels, and structured A/B tests on product pages and checkout flows.", "ar": "تحسين منهجي باستخدام خرائط حرارة Clarity، وتحليل مسار GA4، واختبارات A/B منظمة على مسارات الدفع وصفحات المنتج."}, {"en": "Corner Filter · Qeyam", "ar": "كورنر فلتر · قيم"}),
 ("search", {"en": "SEO & Generative Engine Optimization", "ar": "تحسين محركات البحث وGEO"}, {"en": "Technical SEO combined with Generative Engine Optimization, structuring catalogs for both Google Search and AI answer surfaces.", "ar": "تحسين محركات البحث التقني إلى جانب GEO، تم تطويرهما عبر دورات معتمدة من IBM وSkillUp."}, {"en": "Ghadak Al-Sharq · Gmraa · Altowayan", "ar": "غدق الشرق · قمراء · الطويان"}),
 ("chart", {"en": "Analytics & Measurement Architecture", "ar": "بنية التحليلات والتتبع"}, {"en": "Full GA4 e-commerce implementations, custom GTM container builds, Google Search Console, and Microsoft Clarity integration.", "ar": "أحداث GA4 مخصصة، وبناء حاويات GTM، وSearch Console، وMicrosoft Clarity — بنية قياس من الصفر."}, {"en": "Al-Towayan · Ajlan & Bros / ajstore.com", "ar": "الطويان · عجلان وإخوانه / ajstore.com"}),
 ("target", {"en": "Performance Marketing & Attribution", "ar": "التسويق الأدائي ونماذج النسب"}, {"en": "Google Ads and Meta Ads campaign structure, conversion attribution modeling, and customer acquisition cost optimization.", "ar": "بنية حملات Google Ads وMeta Ads، ونمذجة النسب، والإدارة المرتكزة على عائد الإنفاق الإعلاني."}, {"en": "Ghadak Al-Sharq · Qeyam", "ar": "غدق الشرق · قيم"}),
 ("sync", {"en": "Data & Process Automation", "ar": "البيانات وأتمتة العمليات"}, {"en": "Advanced Excel modeling, ERP-to-store data pipelines, and clear operating documentation for team independence.", "ar": "Excel المتقدم، وأدوات مزامنة بين ERP والمتجر، وسير عمل موثّق لفرق العمليات."}, {"en": "Taif Almasia", "ar": "طيف الماسية"}),
]

STACK = [
 ["Salla", "Shopify", "Zid", "WooCommerce", "WordPress", "Amazon Marketplace"],
 ["Google Analytics 4", "Google Tag Manager", "Search Console", "Microsoft Clarity"],
 ["Semrush", "Ahrefs", "Screaming Frog", "Schema / JSON-LD"],
 ["Excel (Advanced)", "Google Sheets", "ERP Data Pipelines", "Jupyter / Python"]
]

SERVICES = [
 ("layout", {"en": "Store Architecture & Launch", "ar": "بنية وإطلاق المتاجر"}, {"en": "End-to-end architecture and optimization of online stores, from product hierarchy to streamlined checkout.", "ar": "تدقيق شامل وتحسين لبنية المتجر، من صفحات المنتج وحتى الدفع."},
  {"en": ["Platform setup & migration (Salla, Shopify, Zid)", "Catalog taxonomy & navigation structuring", "Page speed & mobile checkout optimization", "Payment gateway & shipping logic setup"], "ar": ["ترحيل المنصة وإعدادها (سلة، Shopify، زد)", "إعادة هيكلة تجربة المستخدم والتنقل", "بنية كتالوج المنتجات وسرعة الصفحات", "إعداد بوابات الدفع والشحن"]},
  {"en": "Typical timeframe: 2–4 weeks for a full audit and prioritized execution plan.", "ar": "المدة المعتادة: 2–4 أسابيع لتدقيق كامل وخطة عمل ذات أولويات."}),
 ("funnel", {"en": "Conversion Rate Optimization", "ar": "تحسين معدل التحويل"}, {"en": "Systematically converting existing store visitors into paying customers by diagnosing and fixing funnel drop-off points.", "ar": "تحويل الزيارات الحالية إلى إيرادات عبر تحسين قائم على الأدلة يحدد نقاط الاحتكاك ويعالجها."},
  {"en": ["Clarity heatmap & session recording analysis", "Hypothesis-driven A/B checkout experiments", "Product page value proposition enhancement", "Cart abandonment reduction workflows"], "ar": ["تحليل خرائط الحرارة والجلسات", "استراتيجية اختبارات A/B لمسار الشراء", "تحسين عرض القيمة في صفحات المنتجات", "معالجة عربات التسوق المتروكة"]},
  {"en": "Evidence-backed methodology with measurable revenue lift.", "ar": "منهجية مستندة إلى الأدلة مع قياس مباشر لأثر الإيرادات."}),
 ("search", {"en": "Technical SEO & GEO", "ar": "تحسين محركات البحث وGEO"}, {"en": "Securing durable organic search rankings while ensuring catalog discoverability across modern AI answer engines.", "ar": "الظهور في نتائج البحث التقليدية مع البقاء قابلًا للاكتشاف مع تنامي البحث بالذكاء الاصطناعي."},
  {"en": ["Technical crawlability & Core Web Vitals audit", "High-intent buyer keyword strategy", "Product schema markup & rich snippets", "Generative Engine Optimization (GEO) principles"], "ar": ["تدقيق تقني لمحركات البحث وسرعة الصفحات", "استراتيجية الكلمات المفتاحية لنية الشراء", "البيانات المنظمة لصفحات المنتجات", "تحسين محركات البحث التوليدية"]},
  {"en": "Built on accredited IBM and SkillUp frameworks.", "ar": "مبنية على أطر عمل معتمدة من IBM وSkillUp."}),
 ("chart", {"en": "Measurement & Analytics Infrastructure", "ar": "بنية القياس والتحليلات"}, {"en": "Building unshakeable tracking infrastructure from the ground up so every business decision is backed by clean data.", "ar": "بنية قياس تُبنى من الصفر، بحيث تستند القرارات إلى بيانات فعلية لا تخمينات."},
  {"en": ["GA4 e-commerce implementation from scratch", "GTM containers with custom event triggers", "Multi-channel conversion attribution", "Executive performance dashboards"], "ar": ["تطبيق GA4 للتجارة الإلكترونية من الصفر", "حاويات GTM بمشغّلات أحداث مخصصة", "نمذجة نسب التحويل متعدد القنوات", "لوحات متابعة تنفيذية لمؤشرات الأداء"]},
  {"en": "Covers view_item, add_to_cart, checkout steps, and purchase.", "ar": "تغطي أحداث مشاهدة المنتج، والإضافة للسلة، وخطوات الدفع، والشراء."}),
 ("compass", {"en": "E-Commerce Growth Advisory", "ar": "استشارات نمو التجارة الإلكترونية"}, {"en": "High-level strategic leadership for established brands seeking senior expertise without full-time agency overhead.", "ar": "دعم استراتيجي رفيع المستوى للعلامات التجارية التي تتطلب خبرة قيادية دون تكاليف إضافية."},
  {"en": ["Growth roadmap planning & channel prioritization", "Marketplace expansion (Amazon, Noon)", "Paid media performance oversight", "Unit economics & retention frameworks"], "ar": ["تخطيط خارطة النمو وترتيب أولويات القنوات", "التوسع في الأسواق الإلكترونية (أمازون، نون)", "الإشراف على كفاءة الإنفاق الإعلاني", "أطر اقتصاديات الوحدة والاحتفاظ بالعملاء"]},
  {"en": "Available on monthly retainer or strategic project scope.", "ar": "متاح عبر تعاقد استشاري شهري أو مشاريع محددة النطاق."}),
 ("sync", {"en": "Operations & ERP Automation", "ar": "العمليات وأتمتة ERP"}, {"en": "Eliminating manual data entry and keeping inventory in sync between enterprise ERPs and digital stores.", "ar": "تقليل العمل اليدوي والحفاظ على تزامن المخزون بين أنظمة ERP والمتاجر الإلكترونية."},
  {"en": ["ERP export data cleaning & mapping", "Automated Excel inventory reconciliation tools", "Sync anomaly detection & error reduction", "Full workflow documentation for internal teams"], "ar": ["تنظيف ومطابقة بيانات تصدير نظام ERP", "أدوات أتمتة عبر Excel لمزامنة المخزون", "رصد التباينات وتجنب أخطاء نفاذ المخزون", "توثيق شامل لسير العمل لصيانة الفريق الداخلي"]},
  {"en": "Proven to reduce weekly manual operational hours by up to 70%.", "ar": "مُثبتة في خفض ساعات العمل اليدوي الأسبوعية بنسبة تصل إلى 70%."}),
]

CERT_TYPES = {
 "professional-cert": {"en": "Professional Cert", "ar": "شهادة احترافية"},
 "specialization": {"en": "Specialization", "ar": "تخصص معتمد"},
 "course": {"en": "Course", "ar": "دورة معتمدة"},
 "project": {"en": "Guided Project", "ar": "مشروع تطبيقي"},
}

CERT_ITEMS = [
 # ── Flagship Multi-Course Programs (3) ──
 {"code": "VQJUO0ZOA8EN", "verify": "professional-cert/VQJUO0ZOA8EN", "issuer": "Google", "issuer_key": "google",
  "type": "professional-cert", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "Google AI Professional Certificate",
  "title_ar": "شهادة Google الاحترافية في الذكاء الاصطناعي",
  "desc": {"en": "7-course Google credential covering AI fundamentals, brainstorming, research, business communication, content creation, data analysis, and AI app building with 20+ artifacts.",
           "ar": "برنامج احترافي من 7 دورات من Google يغطي أساسيات الذكاء الاصطناعي، والعصف الذهني، والبحث، والتواصل، وإنشاء المحتوى، وتحليل البيانات، وبناء التطبيقات بأكثر من 20 مشروعًا عمليًا."},
  "featured": True, "children": ["B2SPRJVN5QWT", "E3OJMLT71NO4", "EZ3MHJFSP6Z1", "4U4ALDBAIOWF", "B7L6NOUHM7BM", "JK6PXZNF5Z0O", "RCFE0MJA5TNO"]},

 {"code": "ZPHYIJVYHDB9", "verify": "specialization/ZPHYIJVYHDB9", "issuer": "IBM & SkillUp", "issuer_key": "ibm",
  "type": "specialization", "cat": "seo", "date": {"en": "Mar 11, 2026", "ar": "11 مارس 2026"},
  "title": "SEO Mastery: From Fundamentals to GenAI and GEO Strategies",
  "title_ar": "إتقان SEO: من الأساسيات إلى استراتيجيات GenAI وGEO",
  "desc": {"en": "4-course specialization by IBM and SkillUp uniting technical SEO, keyword architecture, schema markup, generative AI playbooks, and Generative Engine Optimization (GEO).",
           "ar": "تخصص من 4 دورات من IBM وSkillUp يجمع بين تحسين محركات البحث التقني، وهيكلة الكلمات المفتاحية، والبيانات المنظمة، واستراتيجيات GenAI وGEO مع مشروع تخرج تطبيقي."},
  "featured": True, "children": ["ACG0H1O5GSJB", "KUYFQIQ9YQ8S", "95XGAYYY48HX", "MTD57EZ2YC3A"]},

 {"code": "ZU8R2CZYZTZH", "verify": "specialization/ZU8R2CZYZTZH", "issuer": "IBM", "issuer_key": "ibm",
  "type": "specialization", "cat": "data", "date": {"en": "Mar 19, 2026", "ar": "19 مارس 2026"},
  "title": "Data Analysis and Visualization Foundations",
  "title_ar": "أساسيات تحليل البيانات وتصويرها",
  "desc": {"en": "4-course IBM specialization covering data ecosystems, Excel pivot tables & data wrangling, advanced visual charts, interactive IBM Cognos dashboards, and assessment.",
           "ar": "تخصص من 4 دورات من IBM يغطي منظومة البيانات، ومعالجة البيانات والجداول المحورية في Excel، وتصميم المخططات المتقدمة، وبناء لوحات المعلومات عبر IBM Cognos Analytics."},
  "featured": True, "children": ["IHN6Z2Z7EDNM", "88DR29TLTFOR", "I1JFTVIIAA00", "W8RSSMN95ZXG"]},

 # ── Standalone Courses & Guided Projects (8) ──
 {"code": "7GNJLQHHIU4R", "verify": "7GNJLQHHIU4R", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ecommerce", "date": {"en": "Feb 27, 2026", "ar": "27 فبراير 2026"},
  "title": "Foundations of Digital Marketing and E-commerce",
  "title_ar": "أساسيات التسويق الرقمي والتجارة الإلكترونية",
  "desc": {"en": "Full lifecycle of digital marketing and e-commerce — acquisition funnels, campaign analytics, customer loyalty, and online store optimization.",
           "ar": "دورة حياة التسويق الرقمي والتجارة الإلكترونية بالكامل — مسارات الاستحواذ، وتحليلات الحملات، وولاء العملاء، وتحسين المتجر."},
  "featured": True},

 {"code": "9045Q12FQOAJ", "verify": "9045Q12FQOAJ", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Mar 22, 2026", "ar": "22 مارس 2026"},
  "title": "Python for Data Science & AI: Hands-On Development",
  "title_ar": "Python لعلوم البيانات والذكاء الاصطناعي: تطوير عملي",
  "desc": {"en": "Hands-on Python programming for data science — data structures, pandas, NumPy, REST APIs, and automated data manipulation workflows.",
           "ar": "برمجة Python العملية لعلوم البيانات — هياكل البيانات، ومكتبتا pandas وNumPy، وواجهات البرمجة، ومعالجة البيانات الآلية."},
  "featured": True},

 {"code": "T80ZO4JTMNS5", "verify": "T80ZO4JTMNS5", "issuer": "Meta", "issuer_key": "meta",
  "type": "course", "cat": "data", "date": {"en": "Feb 27, 2026", "ar": "27 فبراير 2026"},
  "title": "Introduction to Data Analytics",
  "title_ar": "مقدمة في تحليلات البيانات",
  "desc": {"en": "A/B testing, statistical thinking, and performance measurement using Meta's advertising and analytics methodology.",
           "ar": "اختبارات A/B، والتفكير الإحصائي، وقياس الأداء باستخدام منهجية التحليلات والإعلانات الخاصة بـ Meta."},
  "featured": True},

 {"code": "UBT00XKO189U", "verify": "UBT00XKO189U", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Mar 23, 2026", "ar": "23 مارس 2026"},
  "title": "Python Project for Data Science",
  "title_ar": "مشروع عملي بـ Python لعلوم البيانات",
  "desc": {"en": "Applied Python data engineering project extracting, cleaning, analyzing, and visualizing real-world market and financial datasets.",
           "ar": "مشروع تطبيقي بـ Python لاستخراج البيانات وتنظيفها وتحليلها وتصويرها عبر سيناريوهات واقعية للأسواق والبيانات المالية."}},

 {"code": "A0UZZGTU7QV8", "verify": "A0UZZGTU7QV8", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "data", "date": {"en": "Mar 2, 2026", "ar": "2 مارس 2026"},
  "title": "Foundations: Data, Data, Everywhere",
  "title_ar": "أساسيات البيانات: البيانات في كل مكان",
  "desc": {"en": "Core data-analytics concepts, structured analytical thinking, spreadsheet fundamentals, and data-driven business strategy.",
           "ar": "مفاهيم أساسية في تحليل البيانات، والتفكير التحليلي المنظم، وأساسيات جداول البيانات، واتخاذ القرار المستند إلى البيانات."}},

 {"code": "E04PR2C0DPXD", "verify": "E04PR2C0DPXD", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "ecommerce", "date": {"en": "Feb 28, 2026", "ar": "28 فبراير 2026"},
  "title": "Generative AI: Accelerate your Digital Marketing Career",
  "title_ar": "الذكاء الاصطناعي التوليدي: تسريع مسيرتك في التسويق الرقمي",
  "desc": {"en": "Applying generative AI tools and workflows to campaign ideation, audience research, content production, and marketing performance.",
           "ar": "توظيف أدوات وسير عمل الذكاء الاصطناعي التوليدي في تخطيط الحملات، وأبحاث الجمهور، وإنشاء المحتوى، ورفع الأداء التسويقي."}},

 {"code": "6M9UIJFN1UTS", "verify": "6M9UIJFN1UTS", "issuer": "Coursera", "issuer_key": "coursera",
  "type": "project", "cat": "ecommerce", "date": {"en": "Mar 2, 2026", "ar": "2 مارس 2026"},
  "title": "Create your e-commerce store with Shopify",
  "title_ar": "إنشاء متجر تجارة إلكترونية عبر Shopify",
  "desc": {"en": "Hands-on guided project covering end-to-end Shopify setup — theme customization, product catalog architecture, and launch configuration.",
           "ar": "مشروع تطبيقي عملي لإعداد متجر Shopify من البداية — تخصيص القالب، وإدارة كتالوج المنتجات، وتجهيز الإطلاق."}},

 {"code": "RXY63RIH5DR8", "verify": "RXY63RIH5DR8", "issuer": "Coursera", "issuer_key": "coursera",
  "type": "project", "cat": "ecommerce", "date": {"en": "Mar 2, 2026", "ar": "2 مارس 2026"},
  "title": "Build a Full Website using WordPress",
  "title_ar": "بناء موقع إلكتروني متكامل عبر WordPress",
  "desc": {"en": "Complete WordPress site building project — page architecture, themes, plugins, navigation structure, and web publishing readiness.",
           "ar": "مشروع بناء موقع متكامل عبر WordPress — هيكلة الصفحات، والقوالب، والإضافات، وتجربة التنقل، وجاهزية النشر."}},

 # ── Google AI Professional Certificate Modules (7) ──
 {"code": "B2SPRJVN5QWT", "verify": "B2SPRJVN5QWT", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 6, 2026", "ar": "6 مارس 2026"},
  "title": "AI Fundamentals",
  "title_ar": "أساسيات الذكاء الاصطناعي",
  "desc": {"en": "Foundational mechanics of generative AI, effective prompting frameworks, output evaluation, and responsible workplace deployment.",
           "ar": "المفاهيم التأسيسية للذكاء الاصطناعي التوليدي، وأطر صياغة الأوامر الفعّالة، وتقييم المخرجات، والاستخدام المسؤول."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "E3OJMLT71NO4", "verify": "E3OJMLT71NO4", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for Brainstorming and Planning",
  "title_ar": "الذكاء الاصطناعي للعصف الذهني والتخطيط",
  "desc": {"en": "Structured ideation, project scoping, strategic roadmapping, and operational planning accelerated by AI workflows.",
           "ar": "توليد الأفكار المنهجي، وتحديد نطاق المشاريع، وبناء خطط العمل وخرائط الطريق باستخدام سير عمل الذكاء الاصطناعي."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "EZ3MHJFSP6Z1", "verify": "EZ3MHJFSP6Z1", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for Research and Insights",
  "title_ar": "الذكاء الاصطناعي للبحث واستخلاص الرؤى",
  "desc": {"en": "Synthesizing market research, validating primary sources, analyzing customer feedback, and surfacing decision-ready insights.",
           "ar": "تلخيص أبحاث السوق، والتحقق من المصادر، وتحليل آراء العملاء، واستخلاص رؤى دقيقة لدعم القرارات التجارية."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "4U4ALDBAIOWF", "verify": "4U4ALDBAIOWF", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for Writing and Communicating",
  "title_ar": "الذكاء الاصطناعي للكتابة والتواصل",
  "desc": {"en": "Drafting executive briefs, stakeholder communications, and persuasive commercial copy with precision and tone consistency.",
           "ar": "صياغة الملخصات التنفيذية، ومراسلات أصحاب المصلحة، والنصوص التجارية بوضوح واتساق في الأسلوب."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "B7L6NOUHM7BM", "verify": "B7L6NOUHM7BM", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for Content Creation",
  "title_ar": "الذكاء الاصطناعي لإنشاء المحتوى",
  "desc": {"en": "Producing creative campaign assets, visual concepts, and scalable content pipelines tailored to commercial channels.",
           "ar": "إنتاج أصول الحملات الإبداعية، والمفاهيم البصرية، ومسارات المحتوى القابلة للتوسع عبر القنوات التجارية."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "JK6PXZNF5Z0O", "verify": "JK6PXZNF5Z0O", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for Data Analysis",
  "title_ar": "الذكاء الاصطناعي لتحليل البيانات",
  "desc": {"en": "Leveraging AI assistants to clean datasets, uncover commercial anomalies, automate formulas, and interpret performance KPIs.",
           "ar": "توظيف مساعدات الذكاء الاصطناعي لتنظيف مجموعات البيانات، واكتشاف الأنماط، وأتمتة المعادلات، وتفسير مؤشرات الأداء."},
  "parent": "VQJUO0ZOA8EN"},

 {"code": "RCFE0MJA5TNO", "verify": "RCFE0MJA5TNO", "issuer": "Google", "issuer_key": "google",
  "type": "course", "cat": "ai", "date": {"en": "Mar 7, 2026", "ar": "7 مارس 2026"},
  "title": "AI for App Building",
  "title_ar": "الذكاء الاصطناعي لبناء التطبيقات",
  "desc": {"en": "Prototyping and vibe-coding custom AI-powered web tools and lightweight operational utilities to solve workplace bottlenecks.",
           "ar": "تصميم وبرمجة نماذج أولية وأدوات ويب مخصصة مدعومة بالذكاء الاصطناعي لمعالجة التحديات التشغيلية."},
  "parent": "VQJUO0ZOA8EN"},

 # ── SEO Mastery Specialization Modules (4) ──
 {"code": "ACG0H1O5GSJB", "verify": "ACG0H1O5GSJB", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "seo", "date": {"en": "Feb 24, 2026", "ar": "24 فبراير 2026"},
  "title": "Search Engine Optimization and Content Marketing",
  "title_ar": "تحسين محركات البحث والتسويق بالمحتوى",
  "desc": {"en": "Technical SEO audits, on-page optimization, commercial keyword research, and structured content marketing methodologies.",
           "ar": "تحسين محركات البحث التقني، وتحسين الصفحات، وبحث الكلمات المفتاحية التجارية، ومنهجيات التسويق بالمحتوى."},
  "parent": "ZPHYIJVYHDB9"},

 {"code": "KUYFQIQ9YQ8S", "verify": "KUYFQIQ9YQ8S", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "seo", "date": {"en": "Feb 25, 2026", "ar": "25 فبراير 2026"},
  "title": "GenAI for SEO: A Hands-On Playbook",
  "title_ar": "دليل عملي لاستخدام GenAI في تحسين محركات البحث",
  "desc": {"en": "Practical AI-assisted workflows for metadata scaling, schema structuring, internal linking, and search visibility improvements.",
           "ar": "تطبيقات عملية للذكاء الاصطناعي في تحسين البيانات الوصفية، والبيانات المنظمة، والربط الداخلي، ورفع الظهور العضوي."},
  "parent": "ZPHYIJVYHDB9"},

 {"code": "95XGAYYY48HX", "verify": "95XGAYYY48HX", "issuer": "SkillUp", "issuer_key": "skillup",
  "type": "course", "cat": "seo", "date": {"en": "Feb 28, 2026", "ar": "28 فبراير 2026"},
  "title": "AI SEO: Mastering Generative Engine Optimization (GEO)",
  "title_ar": "AI SEO: إتقان تحسين محركات البحث التوليدية (GEO)",
  "desc": {"en": "Frameworks for optimizing content and catalog entities to surface inside AI answer engines and Google AI Overviews.",
           "ar": "أطر عمل لتحسين المحتوى وبنية الصفحات للظهور في محركات الإجابة بالذكاء الاصطناعي وملخصات AI Overviews."},
  "parent": "ZPHYIJVYHDB9"},

 {"code": "MTD57EZ2YC3A", "verify": "MTD57EZ2YC3A", "issuer": "SkillUp", "issuer_key": "skillup",
  "type": "course", "cat": "seo", "date": {"en": "Mar 11, 2026", "ar": "11 مارس 2026"},
  "title": "SEO, Generative AI, and GEO Capstone Project",
  "title_ar": "مشروع التخرج في SEO والذكاء الاصطناعي وGEO",
  "desc": {"en": "Comprehensive applied capstone designing and executing a full data-informed SEO and GEO visibility campaign.",
           "ar": "مشروع تخرج تطبيقي متكامل لتصميم وتنفيذ حملة تحسين محركات البحث وGEO مستندة إلى البيانات."},
  "parent": "ZPHYIJVYHDB9"},

 # ── Data Analysis & Visualization Specialization Modules (4) ──
 {"code": "IHN6Z2Z7EDNM", "verify": "IHN6Z2Z7EDNM", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Mar 18, 2026", "ar": "18 مارس 2026"},
  "title": "Data Analytics Foundations: Turn Data into Insights",
  "title_ar": "أساسيات تحليلات البيانات: تحويل البيانات إلى رؤى",
  "desc": {"en": "Modern data ecosystems, data collection and wrangling principles, analytical workflows, and insight storytelling.",
           "ar": "منظومات البيانات الحديثة، ومبادئ جمع البيانات وتنظيفها، وسير العمل التحليلي، وصياغة الرؤى التجارية."},
  "parent": "ZU8R2CZYZTZH"},

 {"code": "88DR29TLTFOR", "verify": "88DR29TLTFOR", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Feb 26, 2026", "ar": "26 فبراير 2026"},
  "title": "Excel for Data Analysis: Essential Skills & Techniques",
  "title_ar": "Excel لتحليل البيانات: المهارات والتقنيات الأساسية",
  "desc": {"en": "Pivot tables, VLOOKUP, data cleaning, summarization, and structured Excel analysis techniques.",
           "ar": "الجداول المحورية، ودالة VLOOKUP، وتنظيف البيانات، وتقنيات التلخيص والتحليل المتقدم عبر Excel."},
  "parent": "ZU8R2CZYZTZH"},

 {"code": "I1JFTVIIAA00", "verify": "I1JFTVIIAA00", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Mar 19, 2026", "ar": "19 مارس 2026"},
  "title": "Data Visualization and Dashboards with Excel and Cognos",
  "title_ar": "تصوير البيانات ولوحات المعلومات عبر Excel وCognos",
  "desc": {"en": "Designing analytical charts (treemaps, scatter, histograms) and interactive executive dashboards with Excel and IBM Cognos.",
           "ar": "تصميم المخططات التحليلية المتقدمة وبناء لوحات المعلومات التفاعلية باستخدام Excel وIBM Cognos Analytics."},
  "parent": "ZU8R2CZYZTZH"},

 {"code": "W8RSSMN95ZXG", "verify": "W8RSSMN95ZXG", "issuer": "IBM", "issuer_key": "ibm",
  "type": "course", "cat": "data", "date": {"en": "Mar 19, 2026", "ar": "19 مارس 2026"},
  "title": "Assessment for Data Analysis and Visualization Foundations",
  "title_ar": "التقييم العملي لأساسيات تحليل البيانات وتصويرها",
  "desc": {"en": "Applied technical assessment verifying practical spreadsheet data analysis and interactive dashboard skills.",
           "ar": "تقييم تطبيقي شامل لإثبات الكفاءة العملية في تحليل البيانات وبناء لوحات المؤشرات التفاعلية."},
  "parent": "ZU8R2CZYZTZH"},
]
CERT_BY_CODE = {c["code"]: c for c in CERT_ITEMS}

def cert_verify_url(c):
    kind = "specialization" if "children" in c else "verify"
    return f"https://www.coursera.org/account/accomplishments/{kind}/{c['code']}"

def cert_pdf_rel(c, r):
    return f"{r}assets/certificates/Coursera-{c['code']}.pdf"

# ─────────────────────────── HELPERS ───────────────────────────
def pick(v, lang):
    return v[lang] if isinstance(v, dict) else v

def rel(depth):
    return "../" * depth

def head(lang, depth, title, desc, path, extra_ld=None, robots="index, follow"):
    r = rel(depth)
    canon = SITE + ("ar/" if lang == "ar" else "") + path
    en_url, ar_url = SITE + path, SITE + "ar/" + path
    ld = json.dumps(extra_ld, ensure_ascii=False, indent=2) if extra_ld else None
    ld_tag = f'\n  <script type="application/ld+json">\n{ld}\n  </script>' if ld else ""
    loc, alt = ("ar_SA", "en_US") if lang == "ar" else ("en_US", "ar_SA")
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {THEME_BOOT}
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Zakaria Fadl">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="ar" href="{ar_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canon}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}assets/images/og-cover.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Zakaria Fadl">
  <meta property="og:locale" content="{loc}">
  <meta property="og:locale:alternate" content="{alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}assets/images/og-cover.jpg">
  <link rel="icon" href="{r}favicon.ico" sizes="any">
  <link rel="icon" href="{r}assets/images/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="{r}assets/images/apple-touch-icon.png">
  <link rel="manifest" href="{r}site.webmanifest">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link rel="stylesheet" href="{r}assets/css/styles.css?v={CSS_V}">{ld_tag}
</head>
<body>
<a href="#main" class="skip-link">{T[lang]['skip']}</a>
"""

def nav(lang, depth, path, is_home=False):
    t = T[lang]; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    home = lroot or "./"
    items = []
    for i, (anchor, label) in enumerate(t["nav"]):
        if anchor.startswith("#"):
            href = anchor if is_home else home + anchor
            cur = ""
        else:
            href = lroot + anchor
            cur = ' aria-current="page"' if path.startswith(anchor) else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        if i == 0:
            cs_cur = ' aria-current="page"' if path.startswith("case-studies/") else ""
            items.append(f'<li><a href="{lroot}case-studies/"{cs_cur}>{t["nav_cs"]}</a></li>')
    en_href = (r + path) or "./"
    ar_href = r + "ar/" + path
    return f"""<nav class="site-nav" id="site-nav">
  <div class="nav-inner">
    <a href="{home}" class="nav-brand">
      <span class="brand-mark"><img class="logo-dark" src="{r}assets/images/brand-icon-on-dark.png" alt="Zakaria Fadl" width="30" height="30"><img class="logo-light" src="{r}assets/images/brand-icon-on-light.png" alt="" width="30" height="30"></span>
      <span class="nav-name">Zakaria Fadl<span>{t['role']}</span></span>
    </a>
    <ul class="nav-links" id="navLinks" data-open="false">
      {''.join(items)}
    </ul>
    <div class="nav-controls">
      <div class="lang-switch">
        <a href="{en_href}" aria-current="{'true' if lang == 'en' else 'false'}" lang="en" hreflang="en">EN</a>
        <a href="{ar_href}" aria-current="{'true' if lang == 'ar' else 'false'}" lang="ar" hreflang="ar">ع</a>
      </div>
      <button class="theme-toggle" id="themeToggle" type="button" aria-label="{t['theme']}">{ICON['sun']}{ICON['moon']}</button>
      <button class="nav-toggle" id="navToggle" type="button" aria-label="{t['menu']}" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
"""

def footer(lang, depth, extra_scripts=""):
    t = T[lang]; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    home = lroot or "./"
    name = "زكريا فضل" if lang == "ar" else "Zakaria Fadl"
    return f"""<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand">
      <span class="brand-mark"><img class="logo-dark" src="{r}assets/images/brand-icon-on-dark.png" alt="" width="30" height="30"><img class="logo-light" src="{r}assets/images/brand-icon-on-light.png" alt="" width="30" height="30"></span>
      <span class="footer-brand-name">{name} — {t['role']}</span>
    </div>
    <div class="footer-links">
      <a href="{home}">berrizak.com</a>
      <a href="{lroot}case-studies/">{t['nav_cs']}</a>
      <a href="{lroot}certificates/">{t['certs_h']}</a>
      <a href="mailto:zak@berrizak.com">zak@berrizak.com</a>
      <a href="{LI}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      <a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
    <div class="footer-copy">© <span id="year">2026</span> {name} · {t['footer']}</div>
  </div>
</footer>
<script src="{r}assets/js/main.js?v={MAIN_JS_V}" defer></script>{extra_scripts}
</body>
</html>
"""

def bp_node(n):
    label, sub, status = n
    s = f'<span class="bp-node-sub">{sub}</span>' if sub else ""
    return f'<div class="bp-node bp-{status}"><span class="bp-node-label">{label}</span>{s}</div>'

def bp_flow(nodes):
    parts = []
    for i, n in enumerate(nodes):
        if i:
            parts.append('<span class="bp-arrow" aria-hidden="true">→</span>')
        if isinstance(n, list):
            parts.append('<div class="bp-stack">' + "".join(bp_node(x) for x in n) + "</div>")
        else:
            parts.append(bp_node(n))
    return '<div class="bp-flow">' + "".join(parts) + "</div>"

def blueprint(c, lang):
    t = T[lang]; bp = c["bp"]
    before = bp["before_ar"] if lang == "ar" else bp["before"]
    after = bp["after_ar"] if lang == "ar" else bp["after"]
    return f"""<div class="blueprint-card js-states" data-current="after">
  <div class="blueprint-head">
    <div class="blueprint-title">{pick(bp['title'], lang)}</div>
    <div class="state-switch--compact" role="group">
      <button type="button" class="state-btn" data-state="before">{'قبل' if lang == 'ar' else 'Before'}</button>
      <button type="button" class="state-btn is-active" data-state="after">{'بعد' if lang == 'ar' else 'After'}</button>
    </div>
  </div>
  <div class="bp-stage" data-show="before" hidden>{bp_flow(before)}</div>
  <div class="bp-stage" data-show="after">{bp_flow(after)}</div>
  <p class="bp-caption">{t['bp_caption']}</p>
</div>"""

def cs_card(c, lang, prefix, index_num):
    t = T[lang]; cd = c["card"]
    idx_str = f"0{index_num}"
    return f"""<a class="cs-card reveal" href="{prefix}{c['slug']}/">
  <div class="cs-card-top">
    <span class="cs-card-index">{idx_str}</span>
    <span class="cs-sector">{pick(c['sector'], lang)}</span>
    <span class="cs-platform-pill">{c['platform']}</span>
  </div>
  <span class="cs-name">{pick(c['name'], lang)}</span>
  <div class="cs-visual-preview">
    <div class="cs-mini-metric-row">
      <span class="cs-mini-kpi">{cd['kpi']}</span>
      <span class="cs-mini-tag">{pick(cd['kpi_lbl'], lang)}</span>
    </div>
    <div class="cs-transition">
      <span class="pill pill-bad">{pick(cd['from'], lang)}</span>
      <span class="cs-trans-arrow" aria-hidden="true">→</span>
      <span class="pill pill-ok">{pick(cd['to'], lang)}</span>
    </div>
  </div>
  <p class="cs-snippet">{pick(c['lede'], lang)}</p>
  <span class="cs-link">{t['read_cs']}</span>
</a>"""

def section_head(tag, title, desc=None):
    d = f'<p class="section-desc">{desc}</p>' if desc else ""
    return f'<div class="section-header"><span class="eyebrow"><span class="eyebrow-dot"></span>{tag}</span><h2 class="section-title">{title}</h2>{d}</div>'

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", path)

PERSON = {"@type": "Person", "@id": SITE + "#person", "name": "Zakaria Fadl", "jobTitle": "Senior E-Commerce Specialist",
          "url": SITE, "email": "mailto:zak@berrizak.com", "telephone": "+966570674043", "sameAs": [LI],
          "knowsAbout": ["E-Commerce Operations", "Conversion Rate Optimization", "Search Engine Optimization", "Generative Engine Optimization", "Google Analytics 4", "Digital Marketing", "Salla", "Shopify"],
          "address": {"@type": "PostalAddress", "addressCountry": "SA"}}

def cert_title(c, lang):
    return c["title_ar"] if lang == "ar" else c["title"]

def cert_card_html(c, lang, r, lroot, for_home=False):
    t = T[lang]
    code = c["code"]
    vurl = cert_verify_url(c)
    pdf_href = f"{lroot}certificates/?cert={code}" if for_home else cert_pdf_rel(c, r)
    open_attr = "" if for_home else f' data-open-cert="{code}"'
    type_lbl = CERT_TYPES[c["type"]][lang]
    badge_extra = f' · {len(c["children"])}' if "children" in c else ""
    title = cert_title(c, lang)
    sub_en = f'<div class="cert-sub-en" dir="ltr">{c["title"]}</div>' if lang == "ar" and c["title_ar"] != c["title"] else ""
    parent_tag = ""
    if not for_home and c.get("parent") and c["parent"] in CERT_BY_CODE:
        p = CERT_BY_CODE[c["parent"]]
        parent_tag = f'<div class="cert-parent-tag">{t["certs_part_of"]}: {cert_title(p, lang)}</div>'
    dl_btn = "" if for_home else f'<a class="cert-btn-link" href="{cert_pdf_rel(c, r)}" download="Coursera-{code}.pdf" title="{t["cert_dl_btn"]}" aria-label="{t["cert_dl_btn"]}">↓</a>'
    return f"""<article class="cert-card reveal" data-cert-code="{code}" data-cat="{c['cat']}">
  <div class="cert-top">
    <span class="cert-issuer">{c['issuer']}</span>
    <span class="cert-badge-verified">{t['cert_verified']}</span>
  </div>
  <div>
    <h3 class="cert-name">{title}</h3>
    {sub_en}
  </div>
  <p class="cert-desc">{pick(c['desc'], lang)}</p>
  {parent_tag}
  <div class="cert-meta-row">
    <span class="cert-type-pill">{type_lbl}{badge_extra}</span>
    <span>{pick(c['date'], lang)} · {code}</span>
  </div>
  <div class="cert-card-actions">
    <a class="cert-btn-preview" href="{pdf_href}"{open_attr}>{ICON['doc']}<span>{t['cert_preview']}</span></a>
    <div class="cert-action-group">
      <a class="cert-btn-link" href="{vurl}" target="_blank" rel="noopener noreferrer">{t['cert_verify_btn']}</a>
      {dl_btn}
    </div>
  </div>
</article>"""

# ─────────────────────────── HOME ───────────────────────────
def home(lang):
    t = T[lang]; depth = 1 if lang == "ar" else 0; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Zakaria Fadl", "inLanguage": lang, "publisher": {"@id": SITE + "#person"}},
        {"@type": "ProfilePage", "url": SITE + ("ar/" if lang == "ar" else ""), "inLanguage": lang, "mainEntity": {"@id": SITE + "#person"}}, PERSON]}
    h = head(lang, depth, t["home_title"], t["home_desc"], "", ld) + nav(lang, depth, "", is_home=True)

    tele = "".join(f'<div class="telemetry-item"><div class="telemetry-val">{v}<span>{s}</span></div><div class="telemetry-lbl">{l}</div></div>' for v, s, l in t["tele"])

    # Executive Dossier Rows
    dossier_rows = [
        {"client": {"en": "Corner Filter · Salla", "ar": "كورنر فلتر · سلة"},
         "detail": {"en": "Automotive fitment-first navigation", "ar": "فلترة حسب توافق المركبة للقطع"},
         "metric": "+35% Eng."},
        {"client": {"en": "Ghadak Al-Sharq · Shopify", "ar": "غدق الشرق · Shopify"},
         "detail": {"en": "Intent-led SEO & campaign attribution", "ar": "SEO نية الشراء ونسب الحملات"},
         "metric": "+40% Org."},
        {"client": {"en": "Taif Almasia · Medical", "ar": "طيف الماسية · طبي"},
         "detail": {"en": "Automated ERP inventory sync tool", "ar": "أتمتة مزامنة المخزون مع ERP"},
         "metric": "−70% Sync"},
        {"client": {"en": "Al-Towayan · Multi-platform", "ar": "الطويان · متعدد المنصات"},
         "detail": {"en": "Full GA4/GTM purchase funnel build", "ar": "تتبع كامل لمسار الشراء GA4/GTM"},
         "metric": "Week 1 Live"},
    ]
    rows_html = "".join(f"""<div class="dossier-row">
  <div class="dossier-row-left">
    <span class="dossier-client">{pick(dr['client'], lang)}</span>
    <span class="dossier-detail">{pick(dr['detail'], lang)}</span>
  </div>
  <span class="dossier-metric">{dr['metric']}</span>
</div>""" for dr in dossier_rows)

    dossier_card = f"""<div class="dossier-card" aria-label="{t['dossier_label']}">
  <div class="dossier-head">
    <span class="dossier-label">{t['dossier_label']}</span>
    <span class="dossier-badge">{t['dossier_badge']}</span>
  </div>
  <div class="dossier-appointment">
    <div class="dossier-co-title">{t['dossier_co']}</div>
    <div class="dossier-role">{t['dossier_role']}</div>
    <p class="dossier-scope">{t['dossier_scope']}</p>
  </div>
  <div class="dossier-impact-list">
    {rows_html}
  </div>
  <div class="dossier-foot">
    <span>{t['dossier_foot_label']}</span>
    <a href="{lroot}case-studies/">{t['dossier_view_all']}</a>
  </div>
</div>"""

    plats = "".join(f'<span class="platform-badge"><span class="dot"></span>{p}</span>' for p in ["Salla", "Shopify", "Zid", "WooCommerce", "GA4", "GTM", "Clarity", "Google Ads", "Meta Ads", "Search Console"])
    cards = "".join(cs_card(c, lang, lroot + "case-studies/", i + 1) for i, c in enumerate(CASES))
    principles = "".join(f'<div class="principle-card reveal"><span class="principle-num">0{i+1}</span><div class="principle-title">{a}</div><div class="principle-desc">{b}</div></div>' for i, (a, b) in enumerate(t["principles"]))
    about_p = "".join(f"<p>{p}</p>" for p in t["about_p"])

    exp = []
    for e in EXPERIENCE:
        pts = "".join(f"<li>{x}</li>" for x in e["pts"][lang])
        tags = "".join(f'<span class="tl-tag">{x}</span>' for x in e["tags"])
        exp.append(f"""<div class="tl-item reveal">
  <div class="tl-meta">
    <span class="tl-date">{e['date'][lang]}</span>
    <span class="tl-location">{'السعودية' if lang == 'ar' else 'Saudi Arabia'}</span>
  </div>
  <div>
    <div class="tl-company">{e['co'][lang] if isinstance(e['co'], dict) else e['co']}</div>
    <div class="tl-role">{e['role'][lang]}</div>
    <ul class="tl-points">{pts}</ul>
    <div class="tl-tags">{tags}</div>
  </div>
</div>""")

    caps = "".join(f'<div class="cap-card reveal"><div class="card-icon">{ICON[ic]}</div><div class="cap-title">{ti[lang]}</div><div class="cap-desc">{de[lang]}</div><div class="cap-evidence">{ev[lang]}</div></div>' for ic, ti, de, ev in CAPS)
    stack = "".join(f'<div><div class="stack-col-title">{t["stack_cols"][i]}</div><div class="stack-wrap">{"".join(f"<span class=stack-pill>{x}</span>" for x in col)}</div></div>' for i, col in enumerate(STACK))
    svcs = "".join(f'<div class="service-card reveal"><div class="card-icon">{ICON[ic]}</div><div class="service-title">{ti[lang]}</div><div class="service-desc">{de[lang]}</div><ul class="service-list">{"".join(f"<li>{x}</li>" for x in li[lang])}</ul><div class="service-note">{no[lang]}</div></div>' for ic, ti, de, li, no in SERVICES)

    def cert_card(c):
        return cert_card_html(c, lang, r, lroot, for_home=True)

    featured_certs = [c for c in CERT_ITEMS if c.get("featured")]
    certs_html = "".join(cert_card(c) for c in featured_certs)

    body = f"""<main id="main">
<header class="hero" id="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow"><span class="eyebrow-dot"></span>{t['eyebrow']}</span>
      <h1 class="hero-title"><span class="hero-name">{t['h1_name']}</span>{t['h1a']}<br><span class="hero-highlight">{t['h1b']}</span></h1>
      <p class="hero-sub">{t['hero_sub']}</p>
      <div class="hero-ctas">
        <a href="#work" class="btn btn-primary">{t['cta_work']}</a>
        <a href="{CV}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">{t['cta_cv']}</a>
        <a href="{WA}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">{t['cta_wa']}</a>
      </div>
      <div class="hero-telemetry">{tele}</div>
    </div>
    <div class="hero-dossier-wrapper">
      {dossier_card}
    </div>
  </div>
</header>

<section class="platform-bar" aria-label="{t['platforms']}"><div class="container platform-inner"><span class="platform-label">{t['platforms']}</span><div class="platform-badges">{plats}</div></div></section>

<section class="section" id="work">
  <div class="container">
    <div class="section-header-row">{section_head(t['work_tag'], t['work_title'], t['work_desc'])}<a href="{lroot}case-studies/" class="btn btn-secondary">{t['all_cs']}</a></div>
    <div class="cs-bento">{cards}</div>
  </div>
</section>

<section class="section section-alt" id="approach">
  <div class="container about-grid">
    <div class="about-copy">
      {section_head(t['approach_tag'], t['approach_title'])}
      <p class="about-lead">{t['approach_lead']}</p>
      {about_p}
    </div>
    <div class="principle-grid">{principles}</div>
  </div>
</section>

<section class="section" id="experience">
  <div class="container">{section_head(t['exp_tag'], t['exp_title'], t['exp_desc'])}<div class="timeline">{''.join(exp)}</div></div>
</section>

<section class="section section-alt" id="capabilities">
  <div class="container">{section_head(t['cap_tag'], t['cap_title'], t['cap_desc'])}<div class="cap-grid">{caps}</div><div class="stack-matrix">{stack}</div></div>
</section>

<section class="section" id="services">
  <div class="container">{section_head(t['svc_tag'], t['svc_title'], t['svc_desc'])}<div class="services-grid">{svcs}</div></div>
</section>

<section class="section section-alt" id="certifications">
  <div class="container">
    <div class="section-header-row">{section_head(t['cert_tag'], t['cert_title'], t['cert_desc'])}<a href="{lroot}certificates/" class="btn btn-secondary">{t['all_certs']}</a></div>
    <div class="certs-grid">{certs_html}</div>
    <div class="certs-archive-banner reveal">
      <div class="certs-archive-copy">
        <div class="certs-archive-title">{t['cert_archive_h']}</div>
        <div class="certs-archive-sub">{t['cert_archive_sub']}</div>
      </div>
      <a href="{lroot}certificates/" class="btn btn-primary">{t['cert_archive_cta']}</a>
    </div>
  </div>
</section>

<section class="section" id="contact">
  <div class="container contact-grid">
    <div>
      <span class="eyebrow"><span class="eyebrow-dot"></span>{t['ct_tag']}</span>
      <h2 class="contact-headline">{t['ct_title']}</h2>
      <p class="contact-sub">{t['ct_sub']}</p>
      <div class="contact-methods">
        <a href="{WA}" class="contact-method" target="_blank" rel="noopener noreferrer"><div><div class="contact-method-label">{t['ct_phone']}</div><div class="contact-method-value" dir="ltr">+966 570 674 043</div></div><span aria-hidden="true">↗</span></a>
        <a href="mailto:zak@berrizak.com" class="contact-method"><div><div class="contact-method-label">{t['ct_email']}</div><div class="contact-method-value">zak@berrizak.com</div></div><span aria-hidden="true">↗</span></a>
        <a href="{LI}" class="contact-method" target="_blank" rel="noopener noreferrer"><div><div class="contact-method-label">{t['ct_li']}</div><div class="contact-method-value">Zakaria Fadl</div></div><span aria-hidden="true">↗</span></a>
      </div>
    </div>
    <div class="contact-form-card">
      <h3>{t['form_h']}</h3>
      <form action="{FORM}" method="POST" id="contactForm" data-sending-label="{t['form_sending']}" data-success-msg="{t['form_ok']}" data-error-msg="{t['form_err']}">
        <div class="honeypot-field" aria-hidden="true"><label for="_gotcha">Leave empty</label><input type="text" id="_gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
        <div class="form-group"><label class="form-label" for="name">{t['form_name']}</label><input class="form-input" type="text" id="name" name="name" autocomplete="name" required></div>
        <div class="form-group"><label class="form-label" for="email">{t['form_email']}</label><input class="form-input" type="email" id="email" name="email" autocomplete="email" required></div>
        <div class="form-group"><label class="form-label" for="message">{t['form_msg']}</label><textarea class="form-textarea" id="message" name="message" required></textarea></div>
        <p class="form-privacy">{t['form_priv']}</p>
        <button class="form-submit" type="submit" id="formSubmit">{t['form_send']}</button>
        <div id="formMsg" class="form-msg" role="status" aria-live="polite" hidden></div>
      </form>
      <p class="form-fallback">{t['form_fb']} <a href="mailto:zakfdl22@gmail.com">zakfdl22@gmail.com</a></p>
    </div>
  </div>
</section>
</main>
"""
    write(("ar/" if lang == "ar" else "") + "index.html", h + body + footer(lang, depth))

# ─────────────────────────── CASE STUDY INDEX ───────────────────────────
def cs_index(lang):
    t = T[lang]; depth = 2 if lang == "ar" else 1; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    base = SITE + ("ar/" if lang == "ar" else "")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "url": base + "case-studies/", "name": t["cs_index_title"], "inLanguage": lang, "isPartOf": {"@id": SITE + "#website"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": t["home"], "item": base}, {"@type": "ListItem", "position": 2, "name": t["cs_index_h"], "item": base + "case-studies/"}]}]}
    h = head(lang, depth, t["cs_index_title"], t["cs_index_desc"], "case-studies/", ld) + nav(lang, depth, "case-studies/")
    cards = "".join(cs_card(c, lang, "", i + 1) for i, c in enumerate(CASES))
    body = f"""<main id="main">
<header class="cs-hero"><div class="container">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="{lroot or './'}">{t['home']}</a> / {t['cs_index_h']}</nav>
  <span class="eyebrow"><span class="eyebrow-dot"></span>{t['work_tag']}</span>
  <h1 style="margin-top:18px">{t['work_title']}</h1>
  <p class="cs-hero-lede">{t['cs_index_desc']}</p>
</div></header>
<section class="section"><div class="container"><div class="cs-bento">{cards}</div></div></section>
</main>
"""
    write(("ar/" if lang == "ar" else "") + "case-studies/index.html", h + body + footer(lang, depth))

# ─────────────────────────── CASE STUDY DETAIL ───────────────────────────
def cs_detail(c, lang):
    t = T[lang]; depth = 3 if lang == "ar" else 2; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    path = f"case-studies/{c['slug']}/"
    base = SITE + ("ar/" if lang == "ar" else "")
    name = pick(c["name"], lang)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CreativeWork", "headline": name, "description": pick(c["lede"], lang), "url": base + path, "inLanguage": lang, "author": {"@id": SITE + "#person"}, "about": name},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["home"], "item": base},
            {"@type": "ListItem", "position": 2, "name": t["cs_index_h"], "item": base + "case-studies/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": base + path}]}]}
    h = head(lang, depth, pick(c["seo_title"], lang), pick(c["lede"], lang), path, ld) + nav(lang, depth, path)
    s = t["cs_sections"]
    kpis = "".join(f'<div class="cs-kpi-box"><div class="cs-kpi-val">{v}</div><div class="cs-kpi-lbl">{pick(l, lang)}</div></div>' for v, l in c["kpis"])
    done = "".join(f"<li>{x}</li>" for x in c["done"][lang])
    tools = "".join(f'<span class="tl-tag">{x}</span>' for x in c["tools"])
    exp = "".join(f"<li>{x}</li>" for x in c["expertise"][lang])
    rel_links = "".join(f'<a href="../{x}/">{pick(BY_SLUG[x]["name"], lang)}<span>{pick(BY_SLUG[x]["sector"], lang)}</span></a>' for x in c["related"])
    body = f"""<main id="main">
<header class="cs-hero"><div class="container">
  <nav class="breadcrumb" aria-label="Breadcrumb"><a href="{lroot}">{t['home']}</a> / <a href="../">{t['cs_index_h']}</a> / {name}</nav>
  <div class="cs-hero-meta"><span class="cs-hero-tag">{pick(c['sector'], lang)}</span><span class="cs-hero-tag">{c['platform']}</span></div>
  <h1>{name}</h1>
  <p class="cs-hero-lede">{pick(c['lede'], lang)}</p>
  <a class="cs-hero-url" href="https://{c['url']}" target="_blank" rel="noopener noreferrer">{t['visit']}: {c['url']} ↗</a>
  <div class="cs-kpi-strip">{kpis}</div>
</div></header>

<section class="section"><div class="container">
  {blueprint(c, lang)}
  <div class="cs-body-grid">
    <div>
      <div class="cs-block"><h2>{s[0]}</h2><p>{pick(c['context'], lang)}</p></div>
      <div class="cs-block"><h2>{s[1]}</h2><p>{pick(c['problem'], lang)}</p></div>
      <div class="cs-block"><h2>{s[2]}</h2><p>{pick(c['resp'], lang)}</p></div>
      <div class="cs-block"><h2>{s[3]}</h2><ul class="tl-points">{done}</ul></div>
      <div class="cs-block"><h2>{s[4]}</h2><div class="cs-result-callout">{pick(c['result'], lang)}</div></div>
      <div class="cs-block"><h2>{s[5]}</h2><p>{pick(c['measured'], lang)}</p></div>
      <div class="cs-block"><h2>{s[6]}</h2><p>{pick(c['showed'], lang)}</p></div>
    </div>
    <aside class="cs-sidebar">
      <div class="cs-side-block"><div class="cs-side-title">{t['side_tools']}</div><div class="cs-tool-tags">{tools}</div></div>
      <div class="cs-side-block"><div class="cs-side-title">{t['side_exp']}</div><ul class="cs-side-list">{exp}</ul></div>
      <div class="cs-side-block cs-related"><div class="cs-side-title">{t['side_rel']}</div>{rel_links}</div>
      <div class="cs-side-block cs-side-cta"><div class="cs-side-title">{t['cs_cta_h']}</div><a class="btn btn-primary" href="{lroot}#contact">{t['cs_cta_btn']}</a></div>
    </aside>
  </div>
</div></section>
<div class="container cs-back"><a href="../">{t['back']}</a></div>
</main>
"""
    write(("ar/" if lang == "ar" else "") + path + "index.html", h + body + footer(lang, depth))

def pdf_stage_html(t):
    return f"""<div class="pdf-stage" dir="ltr" data-pdf-stage>
  <div class="pdf-loading" data-pdf-loading hidden>
    <div class="pdf-spinner" aria-hidden="true"></div>
    <span class="pdf-loading-text">{t['pdf_loading']}</span>
  </div>
  <div class="pdf-canvas-wrap" data-pdf-canvas-wrap hidden>
    <canvas data-pdf-canvas></canvas>
  </div>
  <div class="pdf-fallback-wrap" data-pdf-fallback hidden>
    <iframe class="pdf-fallback-frame" data-pdf-iframe src="about:blank" title="Certificate PDF"></iframe>
  </div>
</div>"""

def pdf_zoom_controls_html(t):
    return f"""<div class="pdf-controls-group" data-pdf-zoom-group>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="zoom-out" aria-label="{t['pdf_zoom_out']}">−</button>
  <span class="pdf-zoom-readout" data-pdf-zoom-val>100%</span>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="zoom-in" aria-label="{t['pdf_zoom_in']}">+</button>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="fit-page">{t['pdf_fit_page']}</button>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="fit-width">{t['pdf_fit_width']}</button>
</div>
<div class="pdf-controls-group" data-pdf-page-controls hidden>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="prev-page">‹</button>
  <span class="pdf-zoom-readout" data-pdf-page-val>1 / 1</span>
  <button type="button" class="pdf-ctrl-btn" data-pdf-action="next-page">›</button>
</div>"""

# ─────────────────────────── CERTIFICATES ARCHIVE ───────────────────────────
def certs_page(lang):
    t = T[lang]; depth = 2 if lang == "ar" else 1; r = rel(depth)
    lroot = r + ("ar/" if lang == "ar" else "")
    path = "certificates/"
    base = SITE + ("ar/" if lang == "ar" else "")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "url": base + path, "name": t["certs_page_title"], "description": t["certs_page_desc"], "inLanguage": lang, "isPartOf": {"@id": SITE + "#website"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["home"], "item": base},
            {"@type": "ListItem", "position": 2, "name": t["certs_h"], "item": base + path}]}]}
    h = head(lang, depth, t["certs_page_title"], t["certs_page_desc"], path, ld) + nav(lang, depth, path)

    kpis = "".join(f'<div class="cs-kpi-box"><div class="cs-kpi-val">{v}</div><div class="cs-kpi-lbl">{lbl}</div></div>' for v, lbl in t["certs_kpis"])

    programs = [c for c in CERT_ITEMS if "children" in c]
    prog_cards = []
    for p in programs:
        p_code = p["code"]
        p_pdf = cert_pdf_rel(p, r)
        p_vurl = cert_verify_url(p)
        p_type = CERT_TYPES[p["type"]][lang]
        child_rows = []
        for idx, ch_code in enumerate(p["children"], 1):
            ch = CERT_BY_CODE[ch_code]
            ch_pdf = cert_pdf_rel(ch, r)
            ch_vurl = cert_verify_url(ch)
            child_rows.append(f"""<div class="program-course-item">
  <div class="program-course-left">
    <span class="program-course-num">{idx:02d}</span>
    <div>
      <div class="program-course-title">{cert_title(ch, lang)}</div>
      <div class="program-course-date">{ch['issuer']} · {pick(ch['date'], lang)}</div>
    </div>
  </div>
  <div class="program-course-btns">
    <a class="mini-icon-btn mini-icon-btn--accent" href="{ch_pdf}" data-open-cert="{ch_code}">PDF</a>
    <a class="mini-icon-btn" href="{ch_vurl}" target="_blank" rel="noopener noreferrer" aria-label="{t['cert_verify_btn']}">↗</a>
  </div>
</div>""")
        prog_cards.append(f"""<article class="program-card reveal">
  <div class="program-overview">
    <div class="program-badges">
      <span class="program-pill-accent">{p_type} · {len(p['children'])} {'دورات' if lang == 'ar' else 'Courses'}</span>
      <span class="cert-badge-verified">{t['cert_verified']}</span>
    </div>
    <h3 class="program-title">{cert_title(p, lang)}</h3>
    <p class="program-desc">{pick(p['desc'], lang)}</p>
    <div class="program-meta">{p['issuer']} · {pick(p['date'], lang)} · {p_code}</div>
    <div class="program-actions">
      <a class="btn btn-primary btn-sm" href="{p_pdf}" data-open-cert="{p_code}">{t['certs_preview_prog']}</a>
      <a class="btn btn-secondary btn-sm" href="{p_pdf}" download="Coursera-{p_code}.pdf">{t['cert_dl_btn']} ↓</a>
      <a class="btn-ghost" href="{p_vurl}" target="_blank" rel="noopener noreferrer">{t['cert_verify_btn']}</a>
    </div>
  </div>
  <div class="program-courses">
    <div class="program-courses-head">{t['certs_included']} ({len(p['children'])})</div>
    <div class="program-course-list">{''.join(child_rows)}</div>
  </div>
</article>""")

    cat_counts = {"all": len(CERT_ITEMS)}
    for c in CERT_ITEMS:
        cat_counts[c["cat"]] = cat_counts.get(c["cat"], 0) + 1
    cat_tabs = "".join(
        f'<button type="button" class="filter-pill{" is-active" if key == "all" else ""}" role="tab" aria-selected="{"true" if key == "all" else "false"}" data-filter-cat="{key}"><span>{lbl}</span><span class="filter-pill-count">{cat_counts.get(key, 0)}</span></button>'
        for key, lbl in t["certs_cats"]
    )
    issuer_chips = "".join(
        f'<button type="button" class="issuer-chip{" is-active" if key == "all" else ""}" aria-pressed="{"true" if key == "all" else "false"}" data-filter-issuer="{key}">{lbl}</button>'
        for key, lbl in t["certs_issuers"]
    )
    all_cards = "".join(cert_card_html(c, lang, r, lroot, for_home=False) for c in CERT_ITEMS)

    json_certs = []
    for c in CERT_ITEMS:
        ik = [k.strip().lower() for k in c["issuer"].replace("&", ",").split(",")]
        parent_title = cert_title(CERT_BY_CODE[c["parent"]], lang) if c.get("parent") in CERT_BY_CODE else ""
        json_certs.append({
            "code": c["code"],
            "filename": f"Coursera-{c['code']}.pdf",
            "pdf": cert_pdf_rel(c, r),
            "verifyUrl": cert_verify_url(c),
            "issuer": c["issuer"],
            "issuerKey": c["issuer_key"],
            "issuerKeys": list(dict.fromkeys([c["issuer_key"]] + ik)),
            "type": c["type"],
            "typeLabel": CERT_TYPES[c["type"]][lang],
            "cat": c["cat"],
            "date": pick(c["date"], lang),
            "title": cert_title(c, lang),
            "titleAr": c["title_ar"],
            "desc": pick(c["desc"], lang),
            "parentCode": c.get("parent", ""),
            "parentTitle": parent_title,
        })
    json_programs = [
        {"code": c["code"], "title": cert_title(c, lang)}
        for c in programs
    ]
    payload = {
        "lang": lang,
        "certs": json_certs,
        "programs": json_programs,
        "ui": {
            "countTemplate": t["certs_count_tpl"],
            "noResults": t["certs_empty"],
            "partOf": t["certs_part_of"],
        }
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    body = f"""<main id="main">
<header class="cs-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="{lroot or './'}">{t['home']}</a> / {t['certs_h']}</nav>
    <span class="eyebrow"><span class="eyebrow-dot"></span>{t['certs_page_tag']}</span>
    <h1 style="margin-top:18px">{t['certs_page_h1']}</h1>
    <p class="cs-hero-lede">{t['certs_page_lede']}</p>
    <div class="certs-hero-actions">
      <button type="button" class="btn btn-primary" id="openReaderModeBtn">{t['certs_cta_reader']}</button>
      <a href="#certsDirectory" class="btn btn-secondary">{t['certs_cta_browse']}</a>
    </div>
    <div class="cs-kpi-strip">{kpis}</div>
  </div>
</header>

<section class="section" id="flagshipPrograms">
  <div class="container">
    {section_head(t['certs_prog_tag'], t['certs_prog_title'], t['certs_prog_desc'])}
    <div class="programs-stack">{''.join(prog_cards)}</div>
  </div>
</section>

<section class="section section-alt" id="certsDirectory">
  <div class="container">
    <div class="section-header-row">
      {section_head(t['certs_dir_tag'], t['certs_dir_title'], t['certs_dir_desc'])}
      <div class="certs-view-switch" role="group" aria-label="View mode">
        <button type="button" class="state-btn is-active" data-view-mode="cards" aria-pressed="true">{t['certs_view_cards']}</button>
        <button type="button" class="state-btn" data-view-mode="split" aria-pressed="false">{t['certs_view_split']}</button>
      </div>
    </div>

    <div class="certs-toolbar">
      <div class="certs-toolbar-top">
        <div class="certs-tabs" role="tablist">{cat_tabs}</div>
        <div class="cert-search-wrap">
          <svg class="cert-search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/></svg>
          <input type="search" id="certSearch" class="cert-search-input" placeholder="{t['certs_search_ph']}" autocomplete="off">
          <button type="button" id="certSearchClear" class="cert-search-clear" aria-label="Clear search" hidden>×</button>
        </div>
      </div>
      <div class="certs-toolbar-bottom">
        <div class="certs-issuer-bar">
          <span class="certs-issuer-label">{t['certs_issuer_lbl']}</span>
          {issuer_chips}
        </div>
        <div class="certs-count" id="certsCount" aria-live="polite"></div>
      </div>
    </div>

    <div class="certs-grid" id="certsGrid">{all_cards}</div>

    <div class="certs-empty" id="certsEmpty" hidden>
      <p>{t['certs_empty']}</p>
      <button type="button" class="btn btn-secondary btn-sm" id="certsReset">{t['certs_reset']}</button>
    </div>

    <div class="certs-split-shell" id="certsSplitShell" hidden>
      <div class="split-list" id="splitReaderList" role="list"></div>
      <div class="split-reader-pane" id="splitReaderViewport">
        <div class="pdf-toolbar">
          <div class="pdf-toolbar-info">
            <div class="pdf-toolbar-meta" data-pdf-meta></div>
            <div class="pdf-toolbar-title" data-pdf-title></div>
          </div>
          {pdf_zoom_controls_html(t)}
          <div class="pdf-actions-group">
            <a class="pdf-tool-link" data-pdf-verify href="#" target="_blank" rel="noopener noreferrer">{t['cert_verify_btn']}</a>
            <a class="pdf-tool-link" data-pdf-download href="#" download>↓</a>
            <a class="pdf-tool-link" data-pdf-newtab href="#" target="_blank" rel="noopener noreferrer">{t['pdf_new_tab']}</a>
            <button type="button" class="pdf-tool-link pdf-tool-link--primary" data-pdf-expand data-open-cert="">{t['pdf_expand']}</button>
          </div>
        </div>
        {pdf_stage_html(t)}
      </div>
    </div>
  </div>
</section>
</main>

<div class="pdf-modal" id="pdfModal" hidden>
  <div class="pdf-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="pdfModalTitle">
    <div class="pdf-modal-bar">
      <div class="pdf-modal-title-group">
        <button type="button" class="pdf-tool-link" id="pdfToggleRail" aria-expanded="true" aria-controls="pdfModalRail">{t['pdf_rail']}</button>
        <div style="min-width:0">
          <div class="pdf-modal-badge" data-modal-badge></div>
          <h2 class="pdf-modal-title" id="pdfModalTitle" data-modal-title></h2>
          <div class="pdf-modal-sub" data-modal-sub></div>
        </div>
      </div>
      {pdf_zoom_controls_html(t)}
      <div class="pdf-actions-group">
        <a class="pdf-tool-link" data-pdf-verify href="#" target="_blank" rel="noopener noreferrer">{t['cert_verify_btn']}</a>
        <a class="pdf-tool-link" data-pdf-download href="#" download><span class="pdf-tool-link-lbl">PDF</span> ↓</a>
        <a class="pdf-tool-link" data-pdf-newtab href="#" target="_blank" rel="noopener noreferrer"><span class="pdf-tool-link-lbl">{t['pdf_new_tab']}</span></a>
        <button type="button" class="pdf-tool-link" data-modal-fullscreen aria-label="Fullscreen">⤢</button>
        <button type="button" class="pdf-close-btn" data-modal-close aria-label="{t['pdf_close']}">×</button>
      </div>
    </div>
    <div class="pdf-modal-body">
      <aside class="pdf-modal-rail" id="pdfModalRail"></aside>
      <div class="pdf-modal-main">
        <button type="button" class="pdf-nav-float pdf-nav-float--prev" data-modal-nav="prev" aria-label="{t['pdf_prev_cert']}"><span>‹</span></button>
        <button type="button" class="pdf-nav-float pdf-nav-float--next" data-modal-nav="next" aria-label="{t['pdf_next_cert']}"><span>›</span></button>
        {pdf_stage_html(t)}
      </div>
    </div>
    <div class="pdf-modal-foot">
      <div class="pdf-foot-left">
        <span class="pdf-code-chip" data-modal-code></span>
        <button type="button" class="pdf-parent-jump" data-modal-parent hidden></button>
      </div>
      <span class="pdf-foot-hints">{t['pdf_hints']}</span>
      <span class="pdf-foot-counter" data-modal-counter></span>
    </div>
  </div>
</div>
<script id="certsData" type="application/json">{payload_json}</script>
"""
    extra = f'\n<script src="{r}assets/js/certs.js?v={CERTS_JS_V}" defer></script>'
    write(("ar/" if lang == "ar" else "") + path + "index.html", h + body + footer(lang, depth, extra))

def write_sitemap():
    urls = [("", "1.0"), ("case-studies/", "0.8"), ("certificates/", "0.8")]
    urls += [(f"case-studies/{c['slug']}/", "0.7") for c in CASES]
    entries = []
    for p, prio in urls:
        en_u, ar_u = SITE + p, SITE + "ar/" + p
        for loc in (en_u, ar_u):
            entries.append(f"""  <url>
    <loc>{loc}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{en_u}"/>
    <xhtml:link rel="alternate" hreflang="ar" href="{ar_u}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{en_u}"/>
    <priority>{prio}</priority>
  </url>""")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n"
    write("sitemap.xml", xml)

def page_404():
    t = T["en"]
    h = head("en", 0, "Page Not Found — Zakaria Fadl", "The page you are looking for could not be found.", "404.html", None, "noindex, follow")
    h = h.replace('href="favicon.ico"', 'href="/favicon.ico"').replace('href="assets/', 'href="/assets/').replace('href="site.webmanifest"', 'href="/site.webmanifest"')
    body = f"""<main id="main"><section class="error-page"><div class="container">
<div class="error-code" aria-hidden="true">404</div><h1>{t['e404_t']}</h1><p>{t['e404_p']}</p>
<a href="/" class="btn btn-primary">{t['e404_b']}</a> <a href="/ar/" class="btn btn-secondary">العربية</a>
</div></section></main>
<script src="/assets/js/main.js?v={MAIN_JS_V}" defer></script></body></html>
"""
    write("404.html", h + body)

if __name__ == "__main__":
    for lang in ("en", "ar"):
        home(lang)
        cs_index(lang)
        certs_page(lang)
        for c in CASES:
            cs_detail(c, lang)
    page_404()
    write_sitemap()
