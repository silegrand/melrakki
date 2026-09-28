"""Shared template for Melrakki application and sector pages.
Generates head, nav, breadcrumb, CTA band, footer and JSON-LD so every page is consistent."""
import json, re, html

SITE = "https://www.melrakki.systems"

APPS = [
    # (url, short label, group)
    ("/solar-powered-surveillance/", "Surveillance", "equipment"),
    ("/telecommunications/", "Communications", "equipment"),
    ("/drone-dock-power/", "Drone docks", "equipment"),
    ("/critical-infrastructure/", "Critical infrastructure", "sector"),
    ("/oil-and-gas/", "Oil and gas", "sector"),
    ("/defence-and-security/", "Defence and security", "sector"),
]


def nav_html(current=None, home=False, current_url=None):
    """current: one of approach, platforms, bespoke, applications, notes, about."""
    pre = "" if home else "/"
    def cur(key):
        return ' aria-current="page"' if current == key else ""
    def app_link(url, label):
        ac = ' aria-current="page"' if current_url == url else ""
        return f'<li><a href="{url}"{ac}>{label}</a></li>'
    eq = "".join(app_link(u, l) for u, l, g in APPS if g == "equipment")
    se = "".join(app_link(u, l) for u, l, g in APPS if g == "sector")
    lead_ac = ' aria-current="page"' if current_url == "/off-grid-power/" else ""
    drop_cls = "nav-drop current" if current == "applications" else "nav-drop"
    return f'''<ul class="nav-links" id="navLinks">
        <li><a href="{pre}#approach">Approach</a></li>
        <li><a href="{pre}#platforms">Platforms</a></li>
        <li><a href="/bespoke/"{cur("bespoke")}>Bespoke</a></li>
        <li class="{drop_cls}"><details><summary>Applications</summary>
          <div class="drop">
            <a class="drop-lead" href="/off-grid-power/"{lead_ac}>Off-grid power<span>How it works, and which architecture fits</span></a>
            <div class="drop-cols">
              <div><p class="drop-h">By equipment</p><ul>{eq}</ul></div>
              <div><p class="drop-h">By sector</p><ul>{se}</ul></div>
            </div>
          </div>
        </details></li>
        <li><a href="/resilience/"{cur("notes")}>Field notes</a></li>
        <li><a href="/about/"{cur("about")}>About</a></li>
        <li class="nav-cta"><a class="btn btn-primary" href="mailto:hello@melrakki.systems">Talk to an engineer</a></li>
      </ul>'''


def apps_footer_col(tag="h4"):
    items = '<li><a href="/off-grid-power/">Off-grid power</a></li>' + "".join(
        f'<li><a href="{u}">{l}</a></li>' for u, l, g in APPS)
    return f'''<div class="foot-col">
        <{tag}>Applications</{tag}>
        <ul>{items}</ul>
      </div>'''


def explore_list():
    return ('<li><a href="/bespoke/">Bespoke</a></li><li><a href="/harka/">Harka platforms</a></li>'
            '<li><a href="/greni/">Greni</a></li><li><a href="/#approach">Approach</a></li>'
            '<li><a href="/resilience/">Field notes</a></li><li><a href="/about/">About</a></li>')


def footer_html():
    return f'''<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/logo-lockup.png" width="480" height="135" loading="lazy" decoding="async" alt="Melrakki Systems">
        <p>Autonomous off-grid power platforms, solar and battery towers and masts, engineered from the load backwards and built around proven hardware.</p>
        <p class="foot-strap">Power that holds.</p>
      </div>
      <div class="foot-col">
        <h4>Explore</h4>
        <ul>{explore_list()}</ul>
      </div>
      {apps_footer_col()}
      <div class="foot-col">
        <h4>Platforms</h4>
        <ul>
          <li><a href="/Melrakki-Harka-Hybrid.pdf">Harka Hybrid brochure</a></li>
          <li><a href="/Melrakki-Harka-Solar.pdf">Harka Solar brochure</a></li>
          <li><a href="/greni/#interest">Greni early interest</a></li>
          <li><a href="/bespoke/#brief">Build a requirement brief</a></li>
          <li><a href="mailto:hello@melrakki.systems">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <p>hello@melrakki.systems &nbsp;|&nbsp; &copy; 2026 Melrakki Systems.</p>
      <p class="foot-desc">Autonomous power for the hardest places on earth.</p>
    </div>
  </div>
</footer>'''


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def cta_html(sub, subject, secondary=None):
    sec = secondary or (f"mailto:hello@melrakki.systems?subject={subject}", "Talk to an engineer")
    return f'''<section class="section-tight cta">
  <div class="wrap">
    <p class="cta-four">Load. Location. Conditions. Mission.</p>
    <h2>Tell us what needs to keep running.</h2>
    <p>{sub}</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="/bespoke/#brief">Develop a requirement</a>
      <a class="btn btn-secondary" href="{sec[0]}">{sec[1]}</a>
    </div>
  </div>
</section>'''


def faq_html(faqs, heading="Common questions."):
    items = "\n      ".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'''<section class="section" id="questions" style="padding-top:0;">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">What people ask</p>
      <h2>{heading}</h2>
    </div>
    <div class="faq measure" style="max-width:52rem;">
      {items}
    </div>
  </div>
</section>'''


def page(slug, title, desc, og_title, og_desc, h1, eyebrow, standfirst, hero_extra, body,
         faqs, cta_sub, cta_subject, crumb_name, parent=True, cta_secondary=None, about_mentions=None):
    url = f"{SITE}/{slug}/"
    crumbs_ld = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    crumbs_vis = '<a href="/">Home</a><span class="sep">/</span>'
    if parent:
        crumbs_ld.append({"@type": "ListItem", "position": 2, "name": "Off-grid power", "item": SITE + "/off-grid-power/"})
        crumbs_vis += '<a href="/off-grid-power/">Off-grid power</a><span class="sep">/</span>'
    crumbs_ld.append({"@type": "ListItem", "position": len(crumbs_ld) + 1, "name": crumb_name, "item": url})
    crumbs_vis += f'<span aria-current="page">{crumb_name}</span>'
    webpage = {
        "@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title,
        "description": desc, "inLanguage": "en-GB",
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": SITE + "/#org"},
        "publisher": {"@id": SITE + "/#org"},
        "breadcrumb": {"@id": url + "#breadcrumb"},
    }
    if about_mentions:
        webpage["mentions"] = [{"@id": m} for m in about_mentions]
    graph = [webpage, {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": crumbs_ld}]
    if faqs:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faqs]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)
    current_url = f"/{slug}/"
    tail = ""
    if "<!--src-->" in body:
        body, tail = body.split("<!--src-->", 1)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#071A2B">
<link rel="icon" href="/favicon.ico?v=3" sizes="any">
<link rel="icon" type="image/svg+xml" href="/favicon.svg?v=3">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Melrakki Systems">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{html.escape(og_title)}">
<meta property="og:description" content="{html.escape(og_desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/social-preview.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:image:alt" content="Melrakki Systems. Power that holds.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(og_title)}">
<meta name="twitter:description" content="{html.escape(og_desc)}">
<meta name="twitter:image" content="{SITE}/social-preview.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/solutions.css">
<link rel="stylesheet" href="/assets/nav.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Melrakki Systems home"><img src="/logo-lockup.png" width="480" height="135" alt="Melrakki Systems"></a>
    <nav class="primary" aria-label="Primary">
      {nav_html("applications", current_url=current_url)}
      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
    </nav>
  </div>
</header>

<main id="main">

<section class="deep phero">
  <div class="wrap">
    <div class="head">
      <nav class="crumbs" aria-label="Breadcrumb">{crumbs_vis}</nav>
      <p class="eyebrow" style="margin-top:1.6rem;">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="standfirst">{standfirst}</p>
    </div>
    {hero_extra}
  </div>
</section>

{body}

{faq_html(faqs) if faqs else ""}

{tail}

</main>

{cta_html(cta_sub, cta_subject, cta_secondary)}

{footer_html()}

<script>
(function(){{
  var t=document.getElementById('navToggle'),l=document.getElementById('navLinks');
  if(!t||!l)return;
  function close(){{l.classList.remove('open');t.setAttribute('aria-expanded','false');t.setAttribute('aria-label','Open menu');}}
  t.addEventListener('click',function(){{var o=l.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');t.setAttribute('aria-label',o?'Close menu':'Open menu');}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&l.classList.contains('open')){{close();t.focus();}}}});
}})();
</script>
<script src="/assets/nav.js" defer></script>
</body>
</html>
'''


def section(inner, eyebrow=None, h2=None, lead=None, sid=None, cls="section", tight_top=True):
    head = ""
    if h2:
        head = '<div class="section-head">'
        if eyebrow:
            head += f'<p class="eyebrow">{eyebrow}</p>'
        head += f"<h2>{h2}</h2>"
        if lead:
            head += f"<p>{lead}</p>"
        head += "</div>"
    idattr = f' id="{sid}"' if sid else ""
    style = ' style="padding-top:0;"' if tight_top else ""
    return f'''<section class="{cls}"{idattr}{style}>
  <div class="wrap">
    {head}
    {inner}
  </div>
</section>'''


def cards(items):
    """items: (href, kicker, title, text, go)"""
    out = []
    for href, k, t, p, go in items:
        tag_open = f'<a class="card" href="{href}">' if href else '<div class="card">'
        tag_close = "</a>" if href else "</div>"
        go_html = f'<span class="go">{go} &rarr;</span>' if go else ""
        out.append(f'{tag_open}<p class="k">{k}</p><h3>{t}</h3><p>{p}</p>{go_html}{tag_close}')
    return '<div class="cards">' + "".join(out) + "</div>"


def table(headers, rows, caption=None, txt=True):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ""
    for r in rows:
        cells = f'<th scope="row">{r[0]}</th>' + "".join(
            f'<td class="txt">{c}</td>' if txt else f"<td>{c}</td>" for c in r[1:])
        body += f"<tr>{cells}</tr>"
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="tbl-wrap"><table class="spec">{cap}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def sources(items):
    lis = "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in items)
    return "<!--src-->" + section(f'<ol class="srcs">{lis}</ol>', eyebrow="Sources", h2="Where the external figures come from.")
