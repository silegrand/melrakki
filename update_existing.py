"""Apply nav, footer, asset includes and contextual inbound links to the existing pages. Idempotent."""
import re, os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import nav_html, apps_footer_col, explore_list

ROOT = "/home/claude/site/melrakki-main"
os.chdir(ROOT)

PAGES = {
    "index.html": dict(current=None, home=True),
    "about/index.html": dict(current="about"),
    "bespoke/index.html": dict(current="bespoke"),
    "greni/index.html": dict(current=None),
    "harka/index.html": dict(current=None),
    "resilience/index.html": dict(current="notes"),
}
for d in sorted(os.listdir("resilience")):
    p = f"resilience/{d}/index.html"
    if os.path.exists(p):
        PAGES[p] = dict(current="notes")

report = []

def must(cond, msg):
    if not cond:
        report.append("MISSED: " + msg)

def append_after_h2(s, h2, sentence, nth=1, f=""):
    """Append a sentence to the nth paragraph after the given H2."""
    if sentence in s:
        return s
    i = s.find(f"<h2>{h2}</h2>")
    must(i >= 0, f"{f}: h2 {h2}")
    if i < 0:
        return s
    j = i
    for _ in range(nth):
        j = s.find("</p>", j + 1)
    return s[:j] + " " + sentence + s[j:]

for f, opt in PAGES.items():
    s = open(f).read(); o = s
    # 1. nav
    s, n = re.subn(r'<ul class="nav-links" id="navLinks">.*?</ul>\s*(?=</nav>|\s*<button)', nav_html(opt["current"], home=opt.get("home", False)) + "\n      ", s, count=1, flags=re.S)
    if n == 0:
        # nav-links ul containing nested lists (already converted): replace up to the details block end
        s, n = re.subn(r'<ul class="nav-links" id="navLinks">.*?<li class="nav-cta">.*?</li>\s*</ul>', nav_html(opt["current"], home=opt.get("home", False)), s, count=1, flags=re.S)
    must(n == 1, f"{f}: nav")
    # 2. assets
    if "/assets/nav.css" not in s:
        s = s.replace("</head>", '<link rel="stylesheet" href="/assets/nav.css">\n</head>', 1)
    if "/assets/nav.js" not in s:
        s = s.replace("</body>", '<script src="/assets/nav.js" defer></script>\n</body>', 1)
    # 3. footer: Explore list + Applications column
    m = re.search(r'<div class="foot-col">\s*<(h[24])>Explore</\1>\s*<ul>.*?</ul>\s*</div>', s, re.S)
    must(m is not None, f"{f}: footer explore")
    if m:
        tag = m.group(1)
        new_explore = f'<div class="foot-col">\n        <{tag}>Explore</{tag}>\n        <ul>{explore_list()}</ul>\n      </div>'
        block = new_explore if ">Applications<" in s else new_explore + "\n      " + apps_footer_col(tag)
        s = s[:m.start()] + block + s[m.end():]
    if s != o:
        open(f, "w").write(s)

# ---- contextual inbound links ----
def edit(f, fn):
    s = open(f).read(); o = s
    s = fn(s)
    if s != o:
        open(f, "w").write(s)

def home(s):
    links = {
        "<h3>Critical infrastructure</h3>": ("/critical-infrastructure/", "Critical infrastructure power"),
        "<h3>Remote security</h3>": ("/solar-powered-surveillance/", "Solar-powered surveillance"),
        "<h3>Autonomous systems</h3>": ("/drone-dock-power/", "Drone dock power"),
        "<h3>Remote industrial</h3>": ("/oil-and-gas/", "Oil and gas sites"),
    }
    for h3, (u, t) in links.items():
        pat = re.compile(re.escape(h3) + r"(<p>.*?</p>)(</div>)", re.S)
        if f'sector-link"><a href="{u}"' not in s:
            s, n = pat.subn(lambda m: h3 + m.group(1)[:-4] + f' <span class="sector-link"><a href="{u}">{t} &rarr;</a></span></p>' + m.group(2), s, count=1)
            must(n == 1, f"home sector {h3}")
    s = s.replace("<li>Oil and gas</li><li>Defence and public sector</li>",
                  '<li><a href="/oil-and-gas/">Oil and gas</a></li><li><a href="/defence-and-security/">Defence and public sector</a></li>')
    return s
edit("index.html", home)

def harka(s):
    m = {"Oil and gas": "/oil-and-gas/", "Defence and public sector": "/defence-and-security/",
         "Critical national infrastructure": "/critical-infrastructure/", "Security and surveillance": "/solar-powered-surveillance/",
         "Telecoms and remote networks": "/telecommunications/", "Border and perimeter security": "/defence-and-security/"}
    for name, u in m.items():
        s = re.sub(r'<div class="sector">' + re.escape(name) + r'(<span>[^<]*</span>)</div>', f'<a class="sector" href="{u}">{name}\\1</a>', s)
    s = append_after_h2(s, "A power system, engineered from the load backwards.",
        'For how Harka compares with grid extension, generators and fuel cells, see <a href="/off-grid-power/">off-grid power systems for remote sites</a>.', 2, "harka")
    return s
edit("harka/index.html", harka)

def bespoke(s):
    return append_after_h2(s, "We don&#39;t start from a catalogue. We start from the load." if "We don&#39;t start" in s else "We don't start from a catalogue. We start from the load.",
        'The architecture choices themselves, from solar-only to hybrid, are compared in <a href="/off-grid-power/">off-grid power systems for remote sites</a>.', 1, "bespoke")
edit("bespoke/index.html", bespoke)

N = "resilience/"
edit(N + "designing-power-from-the-load-backwards/index.html", lambda s: append_after_h2(append_after_h2(s,
    "Start with the load, not the panel",
    'For a surveillance mast, the <a href="/solar-powered-surveillance/#worksheet">surveillance load worksheet</a> turns this into a daily energy figure.', 2, "designing"),
    "Match generation to the worst month, not the average",
    'What that means for solar-only power in a UK December is set out in <a href="/off-grid-power/">off-grid power systems for remote sites</a>.', 2, "designing"))
edit(N + "the-true-cost-of-a-diesel-generator/index.html", lambda s: append_after_h2(append_after_h2(append_after_h2(s,
    "The cost of a site visit", 'How access shapes the design itself is covered in <a href="/off-grid-power/">off-grid power systems for remote sites</a>.', 1, "diesel"),
    "Fuel is worth stealing", 'On remote oil and gas sites the problem is sharper; see <a href="/oil-and-gas/">off-grid power for oil and gas sites</a>.', 1, "diesel"),
    "The energy signature", 'What each power architecture gives away is set out in <a href="/defence-and-security/#signature">the signature ledger</a>.', 1, "diesel"))
edit(N + "the-last-mile-of-resilience/index.html", lambda s: append_after_h2(append_after_h2(s,
    "Why the edge is different", 'The asset-by-asset version is in <a href="/critical-infrastructure/">off-grid power for critical infrastructure</a>.', 1, "lastmile"),
    "What happened at the edge during Storm Arwen", 'What that means for powering remote communications is covered in <a href="/telecommunications/">off-grid power for remote communications</a>.', 3, "lastmile"))
edit(N + "when-the-infrastructure-becomes-the-vulnerability/index.html", lambda s: append_after_h2(s,
    "Why remote sites change the equation", 'Where independent power belongs, asset by asset, is set out in <a href="/critical-infrastructure/">off-grid power for critical infrastructure</a>.', 1, "vuln"))
edit(N + "off-grid-drone-infrastructure/index.html", lambda s: append_after_h2(s,
    "Why off-grid changes the problem", 'The dock&#39;s load profile, and how to size for it, is set out in <a href="/drone-dock-power/">powering a drone dock where there is no grid</a>.', 1, "drone"))

# ---- notes index schema: list all seven notes ----
def notes_schema(s):
    m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
    d = json.loads(m.group(2))
    have = {p["url"] for p in d["hasPart"]}
    for slug, head in [("the-sabotage-problem", "The sabotage problem"), ("the-last-mile-of-resilience", "The last mile of resilience"),
                       ("when-the-infrastructure-becomes-the-vulnerability", "When the infrastructure becomes the vulnerability")]:
        u = f"https://www.melrakki.systems/resilience/{slug}/"
        if u not in have:
            d["hasPart"].insert(0, {"@type": "BlogPosting", "headline": head, "url": u})
    return s[:m.start(2)] + "\n" + json.dumps(d, indent=2, ensure_ascii=False) + "\n" + s[m.end(2):]
edit("resilience/index.html", notes_schema)

print("\n".join(report) or "all edits applied")

# ---- identical footer on every page (mirrors the application pages) ----
from common import footer_html
FOOT = footer_html()
for f in PAGES:
    s = open(f).read()
    s2, n = re.subn(r"<footer[^>]*>.*?</footer>", lambda m: FOOT, s, count=1, flags=re.S)
    must(n == 1, f"{f}: footer replace")
    if s2 != s:
        open(f, "w").write(s2)
print("\n".join(report) or "footers done")
