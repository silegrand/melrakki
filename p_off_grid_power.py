from common import *

SLUG = "off-grid-power"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="/bespoke/#brief">Develop a requirement</a>
      <a class="btn btn-secondary" href="#applications">See where it applies</a>
    </div>
    <div class="spec-strip">
      <div><div class="n">2.4 kWh</div><div class="l">A day at 100 W</div></div>
      <div><div class="n">~25 W</div><div class="l">Solar-only, southern UK, December</div></div>
      <div><div class="n">75 h / 41 h</div><div class="l">Battery reserve at 100 W</div></div>
      <div><div class="n">1,840 h</div><div class="l">Before refuelling, Hybrid</div></div>
    </div>'''

ARCH_SVG = '''<figure class="fig">
<svg viewBox="0 0 760 300" role="img" aria-labelledby="arch-t arch-d">
<title id="arch-t">Autonomous off-grid power architecture</title>
<desc id="arch-d">Solar generation feeds a charge and power controller, which charges battery storage and supplies the load. An optional generator recharges storage only when needed. Optional remote monitoring reports the system's health over the site's communications link.</desc>
<defs><marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah-hi"/></marker>
<marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker></defs>
<rect x="20" y="40" width="150" height="70" rx="6" class="box-hi"/><text x="95" y="70" text-anchor="middle" class="t">Generation</text><text x="95" y="92" text-anchor="middle" class="ts">solar array</text>
<rect x="225" y="40" width="150" height="70" rx="6" class="box-hi"/><text x="300" y="70" text-anchor="middle" class="t">Control</text><text x="300" y="92" text-anchor="middle" class="ts">charge, protect</text>
<rect x="430" y="40" width="150" height="70" rx="6" class="box-hi"/><text x="505" y="70" text-anchor="middle" class="t">Storage</text><text x="505" y="92" text-anchor="middle" class="ts">battery pack</text>
<rect x="620" y="40" width="120" height="70" rx="6" class="box"/><text x="680" y="70" text-anchor="middle" class="t">Load</text><text x="680" y="92" text-anchor="middle" class="ts">your equipment</text>
<line x1="170" y1="75" x2="221" y2="75" class="ln-hi" marker-end="url(#a1)"/>
<line x1="375" y1="75" x2="426" y2="75" class="ln-hi" marker-end="url(#a1)"/>
<line x1="580" y1="75" x2="616" y2="75" class="ln-hi" marker-end="url(#a1)"/>
<rect x="210" y="190" width="180" height="70" rx="6" class="box-opt"/><text x="300" y="220" text-anchor="middle" class="t">Backup</text><text x="300" y="242" text-anchor="middle" class="ts">generator, optional</text>
<line x1="300" y1="190" x2="300" y2="114" class="ln-dash" marker-end="url(#a2)"/>
<text x="312" y="160" class="ts">recharges only</text>
<rect x="545" y="190" width="200" height="70" rx="6" class="box-opt"/><text x="645" y="220" text-anchor="middle" class="t">Monitoring</text><text x="645" y="242" text-anchor="middle" class="ts">optional, via site link</text>
<line x1="650" y1="190" x2="650" y2="114" class="ln-dash" marker-end="url(#a2)"/>
<text x="20" y="24" class="tc">ON SITE, UNDER YOUR CONTROL</text>
<text x="20" y="290" class="ts">Dashed: added where the site needs it. Solid: always present.</text>
</svg>
<figcaption>Conceptual architecture. Everything shown sits on the site; nothing depends on a grid connection. A generator is only present where the worst month demands it, and then it recharges storage rather than running the load directly.</figcaption>
</figure>'''

ENDURE_SVG = '''<figure class="fig">
<svg viewBox="0 0 760 250" role="img" aria-labelledby="en-t en-d">
<title id="en-t">Autonomy versus endurance at a 100 W load</title>
<desc id="en-d">Harka Solar holds 75 hours on battery alone, then continues indefinitely wherever the worst-month solar resource covers the load. Harka Hybrid holds 41 hours on battery alone, then its generator recharges the pack, giving up to 1,840 hours before refuelling. Not to scale.</desc>
<text x="20" y="30" class="tc">HARKA SOLAR</text>
<rect x="20" y="44" width="170" height="36" rx="4" class="area"/><text x="105" y="67" text-anchor="middle" class="t">75 h battery</text>
<rect x="190" y="44" width="550" height="36" rx="4" class="box"/><text x="465" y="67" text-anchor="middle" class="ts">then indefinitely, if the worst month's sun covers the load</text>
<text x="20" y="130" class="tc">HARKA HYBRID</text>
<rect x="20" y="144" width="110" height="36" rx="4" class="area"/><text x="75" y="167" text-anchor="middle" class="t">41 h</text>
<rect x="130" y="144" width="560" height="36" rx="4" class="area2"/><text x="410" y="167" text-anchor="middle" class="t">up to 1,840 h before refuelling</text>
<line x1="690" y1="136" x2="690" y2="190" class="ln" /><text x="690" y="208" text-anchor="middle" class="ts">refuel</text>
<text x="20" y="238" class="ts">Autonomy (cyan): hours with no input at all. Endurance (amber): hours until someone has to bring something. Not to scale.</text>
</svg>
<figcaption>Published figures at a 100 W continuous reference load, battery reserve to 80% depth of discharge. Halve the load and both battery figures roughly double.</figcaption>
</figure>'''

body = section(f'''<div class="measure">
  <p class="lede">An off-grid system is not simply equipment without a cable. It is a small power station that has to generate, store and manage its own energy, and decide what happens when it runs short, with nobody there to intervene.</p>
  <p>That makes three questions unavoidable, and every good design answers them in this order. How much energy does the equipment need in a day, in the worst month of the year? How long must it keep running with no input at all? And what is allowed to refill it: the sun alone, or fuel as well?</p>
  <p>Beneath all three sits a fourth, which is the one that decides resilience. <strong>What does the system depend on that it does not control?</strong> A grid connection, a fuel delivery, a site visit and a clear sky are all dependencies. The job is to remove the ones whose failure would stop the mission, and to size honestly for the ones that remain.</p>
</div>
{ARCH_SVG}''', eyebrow="What off-grid actually means", h2="Keeping equipment alive where the grid does not reach, or cannot be trusted.", tight_top=False)

body += section(table(
    ["Architecture", "It depends on", "Where it is strong", "Where it struggles"],
    [
        ["Grid extension", "The network, the cable route and the local supply", "Heavy, continuous loads close to a reliable supply", "Distance, civil works and lead time; fails with the local network, often in the same storm that makes the site hard to reach"],
        ["Diesel generator only", "Fuel deliveries, servicing and someone to do both", "Short jobs on accessible sites; loads in the kilowatts", "Runs continuously for a small load; fuel logistics, theft, noise, heat and exhaust. See <a class=\"inline-link\" href=\"/resilience/the-true-cost-of-a-diesel-generator/\">what a remote generator really costs</a>"],
        ["Solar and battery", "The site's worst-month sun", "Low to moderate loads where winter sun covers the draw; nothing to deliver, nothing to steal, no noise", "High latitudes in winter, heavy or growing loads, persistent shade or snow"],
        ["Solar hybrid", "The sun most of the time, and a small, infrequent fuel resupply", "Year-round uptime where solar alone cannot close the winter gap", "Still carries a fuel store and a generator to service, though far less of both"],
        ["Fuel cell hybrid", "Delivered methanol or hydrogen cartridges", "Quiet, low-emission backup with a compact footprint", "A delivered fuel all the same, with its own supply chain. Harka does not use fuel cells"],
    ]), eyebrow="The architectures", h2="Compare them by what they depend on, not what they cost to buy.",
    lead="Each of these is the right answer somewhere. The question is which dependency your site can live with in its worst week.")

body += section(f'''<div class="measure">
  <p>These two words get used interchangeably, and they describe different promises. <strong>Autonomy</strong> is how long the system holds with no input whatsoever: the battery reserve that covers a run of dark days, a snow-covered array or a failed generator. <strong>Endurance</strong> is how long the site runs before someone has to bring something to it.</p>
  <p>A solar-only platform has modest autonomy and, where the worst month's sun covers the load, effectively unlimited endurance: there is nothing to deliver. A hybrid has less battery autonomy but very long endurance, because the generator refills the battery from a 125-litre HVO tank: up to 1,840 hours, about eleven weeks, at the 100 W reference load.</p>
  <p>Both figures scale with the load. The published Harka numbers are stated at a 100 W reference draw, which is 2.4 kWh a day. Run 50 W and the battery figures roughly double; run 200 W and they roughly halve. That is why the load has to be measured before anything else is decided.</p>
</div>
{ENDURE_SVG}''', eyebrow="Autonomy and endurance", h2="How long it holds, and how long until someone has to visit, are different questions.")

body += section(f'''<div class="measure">
  <p>Solar output is a season, not a number. The figure that matters is peak sun hours in the worst month, and in the UK that month is December. Taking the 1,080 W Harka array, a conservative 0.7 performance ratio for tilt, temperature, soiling and charge losses, and typical December peak sun hours, the average continuous load that solar alone can sustain is:</p>
</div>
{table(["Location (December)", "Peak sun hours per day", "Daily solar yield", "Sustainable average load"],
  [["Southern UK", "~0.8", "~605 Wh", "<strong>~25 W</strong>"],
   ["Scotland", "~0.5", "~380 Wh", "<strong>~16 W</strong>"],
   ["Southern Europe", "~1.8", "~1,360 Wh", "<strong>~57 W</strong>"]],
  caption="Solar-only capacity of a 1,080 W array in the worst month. Indicative, before site-specific shading and snow.")}
<div class="measure" style="margin-top:1.6rem;">
  <p>This is the most useful number to know before specifying solar-only power in the UK, and it is rarely published. A camera mast with infrared, a router and an enclosure heater commonly averages more than 25 W across a December day and night. Solar-only power will run it beautifully from spring to autumn and fall short in midwinter, exactly when nights are longest and the battery is coldest.</p>
  <p>There are three honest routes when the worst month does not close: reduce the load, enlarge the array and battery until it does (which buys one hard month with a lot of idle capacity for the other eleven), or add a generator that runs only in the deficit window. The <a href="/harka/#calc">Harka viability check</a> runs this arithmetic for your load and location. Take your site's own figure from <a href="https://re.jrc.ec.europa.eu/pvg_tools/en/" rel="noopener">PVGIS</a>.</p>
</div>''', eyebrow="The winter number", h2="What solar alone can carry in a UK December.")

body += section(f'''<div class="measure">
  <p class="lede">The further critical equipment moves from reliable infrastructure, the more autonomous the infrastructure supporting it needs to become.</p>
  <p>On an accessible site a flat battery is an inconvenience. On a site reached by a weekly convoy, a seasonal window or a helicopter, it is an outage that lasts until the next visit. Access is therefore not a logistics detail to sort out after the design. It is a design input, and it sets two numbers directly: the battery reserve, which has to cover the time it takes someone to get there in bad weather, and the fuel endurance, which has to outlast the resupply interval with margin.</p>
</div>
{table(["How the site is reached", "What it means for the design"],
  [["By road, any day", "Moderate reserve is enough. Fuel, if any, is a routine delivery. The case for autonomy is cost and signature more than survival."],
   ["Scheduled visits, weekly or monthly", "Reserve must bridge the gap between visits in the worst week. Remote monitoring earns its place, so a visit is triggered by condition rather than by calendar."],
   ["Seasonal access only", "Solar-only power must hold the whole closed season on the worst-month figure, or the tank must outlast it. Design for the winter the site will actually get."],
   ["Convoy or helicopter", "Every visit is expensive and exposed. Minimise anything that has to be delivered or serviced, and size reserve for the longest credible delay, not the planned one."]])}
<div class="measure" style="margin-top:1.6rem;">
  <p>Three physical factors complete the picture. <strong>Wind loading</strong> on the mast and array is engineered to each site's requirement. <strong>Insulation and ventilation</strong> of the battery and equipment enclosures are specified to the site's temperature range, because cold cuts battery capacity and heat shortens battery life. And <strong>transport</strong> matters more than it looks: Harka platforms are skid-mounted with forklift pockets, ten to a truck, with a manual mast one person raises without tools and a solar array that opens by hand.</p>
</div>''', eyebrow="Remote sites", h2="Designing for a site you cannot easily reach.")

body += section('''<div class="measure">
  <p>Harka platforms use AGM lead-acid batteries: four in Harka Solar (24 V, 400 Ah) and two in Harka Hybrid (24 V, 220 Ah). Lead-acid is heavy, robust and well understood, and like every battery it wears according to how deeply and how hot it is cycled.</p>
  <ul>
    <li><strong>Depth of discharge drives cycle life.</strong> Harka's published expected life is 500 cycles. For comparison, EnerSys rates its own pure-lead AGM at up to 400 cycles at 80% depth of discharge, with many more at shallower depths. A well-sized solar platform cycles shallowly on most days: at a 25 W load, a 16-hour winter night uses about 4% of the Harka Solar pack. Deep cycles only come in long runs of low sun.</li>
    <li><strong>Cold reduces what you can draw.</strong> EnerSys data shows available capacity falling to about 84% at 0 °C and 65% at −20 °C at high discharge rates. Slower remote loads fare better, but the effect arrives in the same weeks as the weakest sun.</li>
    <li><strong>Heat shortens life.</strong> EnerSys gives lead-acid life halving for roughly every 8 to 10 °C above 20 to 25 °C. In hot climates, ventilation and shading of the battery enclosure are part of the design, not an accessory.</li>
  </ul>
  <p>The practical conclusion: plan the battery as a lifecycle replacement, sized so that normal days cycle it lightly, and protected from the temperature extremes of the site. Published Harka reserve figures are taken to 80% depth of discharge, the same deep-cycle point the manufacturers rate against. In normal running the Hybrid's generator starts much earlier, at 40% state of charge, so its battery is rarely cycled that deeply.</p>
</div>''', eyebrow="Lifecycle", h2="Batteries are a lifecycle, not a component.")

body += section(f'''<div class="measure">
  <p>We design every system in the same order, and the order is the method. The requirement comes first: the <strong>mission</strong>, the <strong>load</strong> and its <strong>duty cycle</strong>. Then the site: its <strong>location</strong>, with its worst-month sun, and the <strong>conditions</strong> it has to survive. Only then the architecture: <strong>generation</strong>, <strong>storage</strong>, <strong>backup</strong> if the worst month demands it, and finally the <strong>platform</strong> that carries it all.</p>
  <p>Working the other way round, from a panel on a datasheet, is how systems end up running beautifully all summer and going dark in February. The full sizing method, with the numbers to bring to the first conversation, is in <a href="/resilience/designing-power-from-the-load-backwards/">designing power from the load backwards</a>. The resilience thinking behind it is in <a href="/resilience/when-the-grid-goes-away/">when the grid goes away</a>.</p>
</div>''', eyebrow="Our approach", h2="Engineered from the load backwards.")

body += section(cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "Solar and battery only. No fuel, no engine, no emissions. 1,080 W array, 24 V 400 Ah AGM, 75 h reserve at 100 W. For sites where the worst month covers the load.", "The Harka platforms"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "Solar and battery carry the load; a Stage V generator on HVO recharges the pack only when the sun cannot. 41 h battery reserve, up to 1,840 h before refuelling at 100 W.", "Compare the specifications"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "For loads, sites and constraints no standard platform was sized for: an unusual device, a harder winter, a hotter climate or a limit on size, weight or signature.", "Bespoke engineering"),
]), eyebrow="Platforms", h2="Two standard architectures, and engineering beyond them.",
    lead="Harka covers the common cases for surveillance, communications and sensors. Greni, for autonomous drones, is <a class=\"inline-link\" href=\"/greni/\">in development, with a prototype in field test</a>.")

body += section(cards([
    ("/solar-powered-surveillance/", "By equipment", "Surveillance", "CCTV, infrared, thermal and analytics on a remote mast, and what winter does to their power budget.", "Solar-powered surveillance"),
    ("/telecommunications/", "By equipment", "Communications", "Radio links, routers and telemetry gateways that everything else on the site depends on.", "Remote communications power"),
    ("/drone-dock-power/", "By equipment", "Drone docks", "Why a dock is a harder load than a camera, and what it takes to power one with no grid.", "Drone dock power"),
    ("/critical-infrastructure/", "By sector", "Critical infrastructure", "The remote edge of energy, transport, water and communications networks, where power often fails with the asset it protects.", "Critical infrastructure"),
    ("/oil-and-gas/", "By sector", "Oil and gas", "Wellsites, pipeline routes and remote perimeters, extreme climates and the hazardous-area boundary.", "Oil and gas sites"),
    ("/defence-and-security/", "By sector", "Defence and security", "Perimeters, borders and compounds, where fuel logistics and signature are design inputs.", "Defence and security"),
]), eyebrow="Where this applies", h2="Applications and sectors.", sid="applications")

body += sources([
    ("EU Joint Research Centre, PVGIS: Photovoltaic Geographical Information System", "https://re.jrc.ec.europa.eu/pvg_tools/en/"),
    ("EnerSys, Genesis XE and EP application manual: cycle life, capacity and temperature", "https://www.enersys.com/493bb4/globalassets/documents/product-documentation/genesis/ep/emea/en-gpl-am-005_0911.pdf"),
    ("EnerSys, Genesis EP battery range summary", "https://www.enersys.com.cn/493bb4/globalassets/documents/product-documentation/genesis/ep/emea/en-ep-rs-003-sept-20.pdf"),
    ("EnerSys, PowerSafe SBS application guide: temperature and service life", "https://www.enersys.com/4b05c9/globalassets/documents/product-documentation/powersafe/sbs/amer/amer-en-am-ps-sbs-1222_powersafe_sbs_application_guide.pdf"),
])

faqs = [
    ("How do you size an off-grid power system for remote equipment?",
     "Start with the load, not the panel. Work out the equipment's realistic daily energy in watt-hours for the worst month, decide how many hours it must hold with no input, then size the solar array to the worst month's peak sun hours after losses, and the battery to the reserve. If the worst month does not close, add backup generation or reduce the load. The full method is in <a href=\"/resilience/designing-power-from-the-load-backwards/\">designing power from the load backwards</a>."),
    ("Can solar alone power remote equipment through a UK winter?",
     "Only at low loads. With a 1,080 W array, a southern UK December supports roughly a 25 W average continuous load, and Scotland roughly 16 W. Above that, solar-only power will fall short in midwinter unless the array and battery are made much larger. A hybrid with a generator that runs only in the deficit window is usually the more honest answer."),
    ("What is the difference between battery autonomy and endurance?",
     "Autonomy is how long the system runs with no input at all, from the battery alone. Endurance is how long it runs before someone has to deliver something, such as fuel. At 100 W, Harka Solar has 75 hours of autonomy and unlimited endurance where the worst month's sun covers the load; Harka Hybrid has 41 hours of autonomy and up to 1,840 hours of endurance before refuelling."),
    ("When is a diesel generator still the right answer?",
     "On an accessible site, for a short job, or for loads in the kilowatts. A generator is a capable machine. Its cost on a remote site is rarely the fuel price; it is the deliveries, servicing, visits, theft risk and signature that come with running an engine continuously for a small load."),
    ("How often does an off-grid power system need a site visit?",
     "It depends on the architecture and the site. Solar-only platforms have nothing to refuel, but panels, batteries and fixings still need periodic inspection. A hybrid needs refuelling and generator servicing on an interval set by the load and the season. Optional remote monitoring lets visits be triggered by the system's condition rather than by the calendar."),
]

META = dict(
    slug=SLUG,
    title="Off-Grid Power Systems for Remote Sites | Melrakki",
    desc="How to power surveillance, communications and sensors where there is no reliable grid: solar, battery and hybrid architectures, sized from the load backwards.",
    og_title="Off-grid power for equipment that has to keep running",
    og_desc="Solar, battery and hybrid architectures compared by what they depend on, with the winter numbers most suppliers leave out.",
    h1="Off-grid power for equipment that has to keep running.",
    eyebrow="Off-grid power systems",
    standfirst="Cameras, radios, sensors and drones increasingly sit where mains power is unavailable, unreliable or too expensive to bring in. This is how to decide what should power them: by the load, the site, and what the mission can afford to depend on.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Bring us the load, the location, the conditions and the mission. We will size the system, choose the architecture honestly and tell you where solar alone will not hold.",
    cta_subject="Off-grid%20power%20enquiry", crumb_name="Off-grid power", parent=False,
)
