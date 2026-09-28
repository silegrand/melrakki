from common import *

SLUG = "oil-and-gas"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="mailto:hello@melrakki.systems?subject=Oil%20and%20gas%20site%20power">Talk to an engineer</a>
      <a class="btn btn-secondary" href="#hazardous-areas">The hazardous-area boundary</a>
    </div>
    <div class="spec-strip">
      <div><div class="n">58 sites</div><div class="l">Solar CCTV infrastructure, Kazakhstan</div></div>
      <div><div class="n">13 years</div><div class="l">Off-grid surveillance and power</div></div>
      <div><div class="n">0 L</div><div class="l">Fuel on site, Harka Solar</div></div>
    </div>'''

body = section('''<div class="measure">
  <p class="lede">Oil and gas assets are spread across the places the grid never reached: wellsites, pipeline routes, gathering stations, laydown yards and camp perimeters, often hours from the nearest dependable supply.</p>
  <p>They still need watching, connecting and monitoring. The usual answer is a generator at each point, and on an oil and gas site that answer carries costs a spreadsheet tends to miss. Every fuel run is a vehicle journey on remote roads, which is an exposure in its own right. Every fuel store is something to be stolen or diverted. Every running engine is noise, heat and exhaust at a site where people may be trying to see or hear what is happening.</p>
  <p>The climate adds its own pressure: long, deep winters and extreme summer heat, dust and wind, and service intervals set by access rather than convenience.</p>
</div>''', eyebrow="The problem", h2="Watching remote assets without a convoy to keep them powered.", tight_top=False)

body += section(table(["Where power is needed", "What it carries", "What matters most"], [
    ["Wellsite and pad perimeters", "Cameras, infrared, detection, a cellular or satellite link", "Continuous recording through winter nights; nothing on site worth stealing"],
    ["Pipeline routes and points of interest", "Surveillance at crossings, valves and access points; sensing", "No supply for kilometres; long unattended intervals"],
    ["Laydown yards and construction compounds", "Perimeter cameras, lighting, access monitoring", "Rapid deployment before permanent power exists; relocation as work moves"],
    ["Gates, camps and access roads", "Surveillance, communications relays", "Dependable uptime without adding to the fuel logistics"],
    ["Instrumentation and monitoring", "Low-power sensing and telemetry", "Power and communications designed together"],
]), eyebrow="Applications", h2="Where autonomous power earns its place on an oil and gas site.",
    lead="Melrakki's experience in the sector is surveillance-led. The same load-backwards method applies to any remote load on the site.")

body += section('''<div class="callout warn">
  <span class="k">Hazardous areas</span>
  <p>Harka platforms are not certified for use inside hazardous areas. A solar array, a battery and, on the Hybrid, a generator are all potential ignition sources, and none of them is rated for an explosive atmosphere.</p>
  <p>Platforms must be sited outside classified zones, as defined by the operator's hazardous area classification. In Great Britain that falls under DSEAR, with equipment for explosive atmospheres covered by ATEX and UKEX; internationally, IECEx. Where monitoring is needed inside a zone, certified equipment in the zone can be powered from a platform sited safely outside it, subject to the operator's own design and approval.</p>
</div>
<div class="measure">
  <p>The zone drawing is therefore one of the first documents we ask for. It decides where power can stand, how far cable runs to certified equipment have to go, and sometimes whether a camera can see what it needs to from outside the boundary. For the regulatory background, see HSE's guidance on <a href="https://www.hse.gov.uk/fireandexplosion/atex.htm" rel="noopener">ATEX and explosive atmospheres</a> and on <a href="https://www.hse.gov.uk/comah/sragtech/techmeasareaclas.htm" rel="noopener">hazardous area classification</a>.</p>
</div>''', eyebrow="The hazardous-area boundary", h2="Power stands outside the zone.", sid="hazardous-areas")

body += section('''<div class="measure">
  <p>Oil and gas sites tend to sit at the extremes, and the power system feels every one of them.</p>
  <ul>
    <li><strong>Cold</strong> cuts what a battery can deliver. EnerSys data for pure-lead AGM shows available capacity falling to about 84% at 0 °C and 65% at −20 °C at high discharge rates. Battery enclosures are insulated to the site's winter.</li>
    <li><strong>Heat</strong> shortens battery life: EnerSys gives lead-acid life halving for roughly every 8 to 10 °C above 20 to 25 °C. Enclosures are ventilated and shaded to the site's summer.</li>
    <li><strong>Dust and soiling</strong> quietly reduce solar yield. The cleaning interval belongs in the design, alongside the worst-month sun figure.</li>
    <li><strong>Wind</strong> loading on the mast and array is engineered to each site's requirement.</li>
    <li><strong>Winter sun</strong> at northern latitudes may not cover the load at all. That is what the Hybrid tier is for.</li>
  </ul>
  <p>We do not publish a single operating temperature range for Harka because the thermal design is specified per site: insulated, ventilated, or both, to the conditions the customer needs it to survive.</p>
</div>''', eyebrow="Climate", h2="Designing for the extremes the site will actually see.")

body += section('''<div class="measure">
  <p>On a remote oil and gas site, fuel is not just an operating cost. It is a logistics chain, a security problem and a safety exposure.</p>
  <p><strong>Harka Solar</strong> removes it entirely: no fuel, no engine, nothing to deliver, nothing to steal. Where the worst month's sun covers the load, it runs with no resupply at all.</p>
  <p><strong>Harka Hybrid</strong> minimises it. Solar and battery carry the load; a Stage V generator running on HVO renewable diesel starts only when the battery reaches 40% state of charge, recharges it and stops. From a 125-litre HVO tank, at the 100 W reference load, it runs up to 1,840 hours, around eleven weeks, before refuelling, with most of the fuel burned in the weeks the sun cannot cover.</p>
  <p>The full argument, including when a generator is still the right answer, is in <a href="/resilience/the-true-cost-of-a-diesel-generator/">the true cost of a diesel generator on a remote site</a>.</p>
</div>''', eyebrow="Fuel", h2="Less fuel to deliver, store and protect.")

body += section('''<div class="proof">
  <p class="eyebrow">Experience</p>
  <p class="big">Solar surveillance infrastructure across 58 oil and gas sites in Kazakhstan.</p>
  <p>The team behind Melrakki has spent more than a decade designing and deploying off-grid solar surveillance into demanding sectors, and oil and gas is where much of that experience was earned: solar CCTV infrastructure co-designed for 58 sites in Kazakhstan, where continental winters and summers are both severe, alongside work in highways, construction and critical infrastructure. It is the reason we size for the worst credible week, not the best day.</p>
  <p><a href="/about/">More about Melrakki</a>.</p>
</div>''')

body += section(f'''{cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "No fuel on site. For perimeters and points of interest where the worst month's sun covers the load.", "Harka Solar"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "For northern winters and heavier loads. Up to 1,840 h before refuelling at 100 W.", "Harka Hybrid"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "Unusual loads, integration with existing site systems, or conditions a standard platform was not sized for.", "Bespoke engineering"),
])}
<div class="measure" style="margin-top:1.8rem;">
  <p>Platforms are skid-mounted with forklift pockets and travel ten to a truck. One person raises the manual mast without tools, and the array opens by hand. For camera load budgets and winter sizing in detail, see <a href="/solar-powered-surveillance/">solar-powered surveillance</a>. For the resilience argument behind independent power at remote assets, see <a href="/resilience/the-sabotage-problem/">the sabotage problem</a>.</p>
  <p style="margin-top:1rem;"><span class="status">In development</span>&nbsp; For an aerial look on demand at remote wellsites and pipeline routes, <a href="/greni/">Greni</a>, our autonomous drone node, is a working prototype in field test. See also <a href="/drone-dock-power/">powering a drone dock off-grid</a>.</p>
</div>''', eyebrow="Platforms", h2="Autonomous power for the remote edge of the field.")

body += sources([
    ("HSE, ATEX equipment and explosive atmospheres", "https://www.hse.gov.uk/fireandexplosion/atex.htm"),
    ("HSE, Hazardous area classification and control of ignition sources", "https://www.hse.gov.uk/comah/sragtech/techmeasareaclas.htm"),
    ("EnerSys, Genesis XE and EP application manual: capacity versus temperature", "https://www.enersys.com/493bb4/globalassets/documents/product-documentation/genesis/ep/emea/en-gpl-am-005_0911.pdf"),
    ("EnerSys, PowerSafe SBS application guide: temperature and service life", "https://www.enersys.com/4b05c9/globalassets/documents/product-documentation/powersafe/sbs/amer/amer-en-am-ps-sbs-1222_powersafe_sbs_application_guide.pdf"),
])

faqs = [
    ("Can a Harka platform be installed inside an ATEX zone?",
     "No. Harka platforms are not certified for hazardous areas and must be sited outside classified zones, as set by the operator's hazardous area classification. Certified equipment inside a zone can be powered from a platform outside it, subject to the operator's design and approval."),
    ("Will solar power work in extreme heat and cold?",
     "Yes, when the system is designed for it. Cold reduces battery capacity and winter reduces solar yield, so the system is sized for the worst month; heat shortens battery life, so enclosures are ventilated and shaded. Insulation and ventilation are specified to each site's conditions rather than to a single published range."),
    ("Solar only or hybrid for a remote wellsite?",
     "Let the worst month decide. If the site's worst-month sun covers the load with margin, Harka Solar removes fuel from the site entirely. If not, Harka Hybrid carries the load on solar and battery and runs its HVO generator only to recharge the battery when it reaches 40% state of charge."),
    ("How are the platforms transported to remote sites?",
     "Harka platforms are skid-mounted with forklift pockets, travel ten to a truck and are built for all-terrain transport. One person raises the mast manually without tools, and the solar array opens by hand."),
]

META = dict(
    slug=SLUG,
    title="Off-Grid Power for Oil and Gas Sites | Melrakki Systems",
    desc="Autonomous solar and hybrid power for surveillance, monitoring and communications on remote oil and gas sites, from a team with over a decade in the sector.",
    og_title="Power for oil and gas sites the grid never reached",
    og_desc="Surveillance and monitoring power for wellsites and pipeline routes: the hazardous-area boundary, extreme climates and less fuel to protect.",
    h1="Power for oil and gas sites the grid never reached.",
    eyebrow="Oil and gas",
    standfirst="Wellsites, pipeline routes, laydown areas and remote perimeters need watching and connecting, often far from dependable power. The team behind Melrakki has been putting autonomous solar power into that environment for more than a decade.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Send us the site, the zone drawing and what has to stay live. We will engineer the power that holds there, outside the zone and through the worst week.",
    cta_subject="Oil%20and%20gas%20enquiry", crumb_name="Oil and gas",
)
