from common import *

SLUG = "defence-and-security"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="mailto:hello@melrakki.systems?subject=Defence%20and%20security%20power">Talk to an engineer</a>
      <a class="btn btn-secondary" href="#signature">The signature ledger</a>
    </div>'''

body = section('''<div class="measure">
  <p class="lede">Persistent surveillance and communications at a perimeter, a border or a temporary compound depend on power, and the way that power is delivered has consequences beyond uptime.</p>
  <p>A generator can be heard, seen on a thermal camera and smelt downwind. Its fuel has to be delivered, and every delivery is a vehicle on a predictable route to a known point. Its fuel store is worth stealing. None of this matters much on a secure, accessible site. At the edge, it can matter more than the equipment the generator is powering.</p>
  <p>Military analysis has made the same point about logistics for years. A <a href="https://www.rusi.org/explore-our-research/publications/commentary/achieving-military-advantage-british-army-through-energy-transition" rel="noopener">2025 RUSI commentary</a> on energy in the British Army recalls estimates that it took around 27 litres of fuel to deliver one litre to a patrol base in southern Afghanistan, and that 52% of casualties in that campaign were sustained maintaining lines of communication and resupply. It also notes that vehicle acoustic signatures can be detected and identified at 10 km. The scale of a fixed security site is different. The principle is not: <strong>every delivery is an exposure, and every running engine is a signature.</strong></p>
</div>''', eyebrow="The problem", h2="Power that adds a logistics chain and a signature to the site it protects.", tight_top=False)

body += section(f'''{table(["Signature", "Diesel generator site", "Harka Hybrid", "Harka Solar"], [
    ["Acoustic", "An engine running continuously", "Silent on battery. A low-rpm, noise-insulated generator runs only to recharge", "Silent. No engine"],
    ["Thermal", "Engine block and exhaust heat", "No engine heat on battery; generator heat while recharging", "No engine heat or exhaust. With appropriate insulation, the electronics' heat signature is extremely low"],
    ["Exhaust", "Continuous", "Only while recharging, on HVO", "None"],
    ["Resupply pattern", "Regular fuel runs to a known point", "Up to 1,840 h between refuelling at 100 W", "None: nothing to deliver"],
    ["Visual", "Generator, fuel store, vehicle tracks", "Mast, array and generator housing", "Mast and array"],
])}
<div class="measure" style="margin-top:1.6rem;">
  <p>Two honest limits. First, a 6 m mast and a solar array are visible: lowering the acoustic, thermal and logistic signature is not concealment, and siting still matters. Second, the Hybrid is only silent while the sun and battery are carrying the load. Its generator runs only when the battery falls to 40% state of charge, which from a full battery at 100 W is roughly 31 hours of silent running before any solar top-up. Where signature is the overriding requirement, the load and the array are sized so the generator runs as rarely as possible, or the clean tier is used.</p>
</div>''', eyebrow="The signature ledger", h2="What each architecture gives away.", sid="signature")

body += section('''<div class="measure">
  <p>For a security site, the number of times someone must visit is a design input, not an operating detail. It sets the battery reserve, the fuel endurance and whether remote monitoring is essential or optional.</p>
  <ul>
    <li><strong>Reserve</strong> should cover the longest credible interval before anyone can attend, in the worst week of the year. Harka holds 75 h (Solar) and 41 h (Hybrid) on battery at 100 W; lighter loads hold proportionally longer.</li>
    <li><strong>Endurance</strong> is unlimited on Harka Solar wherever the worst month's sun covers the load, and up to 1,840 h before refuelling on Harka Hybrid at 100 W, from a 125-litre HVO tank.</li>
    <li><strong>Knowing the site is healthy</strong> without going there takes remote monitoring, which is optional on Harka and usually worth specifying where visits are costly or exposed.</li>
    <li><strong>Deployment</strong> is deliberately simple: skid-mounted platforms with forklift pockets, ten to a truck, a manual mast one person raises in minutes without tools, and an array that opens by hand.</li>
  </ul>
</div>''', eyebrow="Logistics", h2="Fewer visits, by design.")

body += section('''<div class="measure">
  <p>Independent power is also a resilience measure. A camera that runs from the same supply as the site it protects can be switched off by anyone who can reach that supply. One that generates and stores its own power, with no external cable to cut and its sensitive components in a lockable steel bay, is harder to disconnect.</p>
  <p>That does not make it invulnerable, and we do not claim it does. It removes one dependency, which is usually the cheapest one to remove. The fuller argument is in <a href="/resilience/the-sabotage-problem/">the sabotage problem</a> and <a href="/resilience/when-the-infrastructure-becomes-the-vulnerability/">when the infrastructure becomes the vulnerability</a>.</p>
</div>''', eyebrow="Resilience", h2="Harder to disconnect.")

body += section(f'''{cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "The lowest signature in the range: no engine, no fuel, no exhaust. For sites where the worst month's sun covers the load.", "Harka Solar"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "For higher latitudes, winter and heavier loads, with a generator that runs only to recharge and long intervals between refuelling.", "Harka Hybrid"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "Constraints on size, weight, portability, signature or mounting that the design has to be built around.", "Bespoke engineering"),
])}
<div class="measure" style="margin-top:1.8rem;">
  <p>Wind loading, insulation and ventilation are engineered to each site's requirement. For camera load budgets and winter sizing, see <a href="/solar-powered-surveillance/">solar-powered surveillance</a>; for the architecture choices in general, <a href="/off-grid-power/">off-grid power systems for remote sites</a>.</p>
  <p>Melrakki does not publish customer or programme information, and nothing on this page implies a defence approval, accreditation or contract. We engineer to the requirement and say plainly what is proven and what is not.</p>
</div>''', eyebrow="Platforms", h2="Power specified by the mission, not the catalogue.")

body += sources([
    ("Goodall, P., Achieving military advantage for the British Army through energy transition, RUSI commentary, February 2025", "https://www.rusi.org/explore-our-research/publications/commentary/achieving-military-advantage-british-army-through-energy-transition"),
])

faqs = [
    ("Is solar power silent?",
     "Harka Solar has no engine and makes no operating noise. Harka Hybrid is silent while the sun and battery carry the load; its low-rpm, noise-insulated generator runs only to recharge the battery when it reaches 40% state of charge."),
    ("Does a solar platform have a thermal signature?",
     "There is no engine heat or exhaust. The electronics still produce some heat, and with appropriate insulation that signature is extremely low. The mast and array remain visible, so siting still matters."),
    ("How long can a site run without resupply?",
     "Harka Solar needs no resupply wherever the worst month's sun covers the load, and holds 75 hours on battery alone at 100 W. Harka Hybrid holds 41 hours on battery and runs up to 1,840 hours before refuelling at 100 W. Lighter loads extend all three figures."),
    ("How quickly can a platform be deployed?",
     "Harka platforms are skid-mounted, travel ten to a truck and are moved by forklift. One person raises the mast manually in minutes without tools, and the solar array opens by hand."),
    ("Does Melrakki hold defence approvals?",
     "We do not publish customer or programme information and make no claim to defence approvals or accreditations on this site. Tell us the requirement and we will be straight about what is proven and what would need to be established."),
]

META = dict(
    slug=SLUG,
    title="Low-Signature Power for Defence and Security | Melrakki",
    desc="Off-grid power for surveillance and communications that reduces fuel logistics and signature: acoustic, thermal, exhaust, and the resupply pattern itself.",
    og_title="Autonomous power for defence and security sites",
    og_desc="What each power architecture gives away, and how to design a security site that needs fewer visits and is harder to disconnect.",
    h1="Autonomous power for defence and security sites.",
    eyebrow="Defence and security",
    standfirst="For surveillance and communications at a perimeter, a border or a temporary compound, the power system decides more than uptime. It decides what the site sounds like, how it looks to a thermal camera, and how often someone has to drive to it.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Tell us what has to keep running, where, and how often anyone can reach it. We will engineer the power around the mission and its constraints.",
    cta_subject="Defence%20and%20security%20enquiry", crumb_name="Defence and security",
)
