from common import *

SLUG = "drone-dock-power"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="/greni/#interest">Register interest in Greni</a>
      <a class="btn btn-secondary" href="/resilience/off-grid-drone-infrastructure/">Read the thinking behind it</a>
    </div>
    <div class="spec-strip">
      <div><div class="n">24 h</div><div class="l">A dock's baseline never stops</div></div>
      <div><div class="n">Peaks</div><div class="l">Every sortie ends in a fast charge</div></div>
      <div><div class="n">Tested</div><div class="l">Compatibility proven, not assumed</div></div>
    </div>'''

LOAD_SVG = '''<figure class="fig">
<svg viewBox="0 0 760 280" role="img" aria-labelledby="dk-t dk-d">
<title id="dk-t">The load profile of a drone dock over a day</title>
<desc id="dk-d">A drone dock draws a continuous baseline for its electronics, communications and thermal management, all day and night. Each sortie ends with a short, tall charging peak as the aircraft recharges. The peaks set the power the system must deliver; the baseline usually dominates the energy over a day.</desc>
<line x1="60" y1="220" x2="740" y2="220" class="grid"/>
<line x1="60" y1="40" x2="60" y2="220" class="grid"/>
<text x="60" y="242" text-anchor="middle" class="ts">00:00</text><text x="230" y="242" text-anchor="middle" class="ts">06:00</text><text x="400" y="242" text-anchor="middle" class="ts">12:00</text><text x="570" y="242" text-anchor="middle" class="ts">18:00</text><text x="740" y="242" text-anchor="middle" class="ts">24:00</text>
<rect x="60" y="180" width="680" height="40" class="area"/>
<rect x="196" y="70" width="18" height="110" class="area2"/>
<rect x="326" y="70" width="18" height="110" class="area2"/>
<rect x="440" y="70" width="18" height="110" class="area2"/>
<rect x="560" y="70" width="18" height="110" class="area2"/>
<rect x="680" y="70" width="18" height="110" class="area2"/>
<text x="400" y="205" text-anchor="middle" class="ts">baseline: electronics, comms, heating or cooling, standby</text>
<text x="370" y="58" text-anchor="middle" class="t">charge peak after each sortie</text>
<text x="20" y="28" class="tc">POWER (ILLUSTRATIVE)</text>
<text x="60" y="270" class="ts">Cyan: continuous baseline. Amber: aircraft charging. Illustrative shapes, not measurements of any product.</text>
</svg>
<figcaption>The peaks decide how much power the storage and conversion must deliver, in the cold, at night. The baseline, running 24 hours a day, usually decides how much energy the site has to generate.</figcaption>
</figure>'''

body = section(f'''<div class="measure">
  <p class="lede">Drone-in-a-box systems can launch, land, recharge and re-task an aircraft with no one present. Almost all of them assume a mains connection at the landing site.</p>
  <p>That assumption holds on a depot roof. It does not hold on a pipeline route, a remote perimeter, a border or a disaster zone, which are often the places an autonomous aircraft would be most useful. However capable the aircraft, the capability stops at the landing zone if nothing there can recharge it.</p>
  <p>Replacing the mains connection is an off-grid power problem, and a harder one than powering a camera. It is worth understanding why before anyone specifies panels or batteries.</p>
</div>''', eyebrow="The missing layer", h2="The aircraft is autonomous. The power behind it usually is not.", tight_top=False)

body += section(f'''<div class="measure">
  <p>A dock has two loads layered on top of each other.</p>
  <p><strong>The baseline</strong> runs all day and all night: the dock's control electronics, its communications link, its own backup battery, and the heating or cooling that keeps the aircraft battery and mechanism within temperature. On a cold or hot day the thermal part can grow substantially, and it runs whether or not anything flies.</p>
  <p><strong>The charging peaks</strong> arrive after every sortie. Docks are designed to turn the aircraft round quickly, so they recharge fast, which means a short, high draw.</p>
  <p>Published specifications show the scale. One widely deployed commercial dock, for example, takes a 100 to 240 V AC mains supply with a maximum input of 800 W, and recharges its aircraft's roughly 150 Wh battery from 15% to 95% in under half an hour. It is rated to operate from −30 to 50 °C. Other docks differ, which is exactly why the real figures have to come from the dock you intend to use.</p>
</div>
{LOAD_SVG}
<div class="callout"><span class="k">Why this is harder than a camera</span><p>A camera mast is sized mostly for energy. A dock has to be sized for energy <em>and</em> for peak power: the storage and conversion must deliver the charge peak on a winter night with the battery cold and the sun long gone. It usually needs an AC supply as well, which adds conversion losses a DC camera system does not have.</p></div>''',
    eyebrow="The dock as a load", h2="A continuous baseline with a spike after every sortie.")

body += section(f'''<div class="measure">
  <p>The daily energy a dock site needs comes from three terms, and each has to be taken for the worst month rather than the average:</p>
  <ol>
    <li><strong>Baseline</strong>: the dock's standby draw, including thermal management in the site's winter or summer extreme, multiplied by 24 hours.</li>
    <li><strong>Sorties</strong>: the number of flights a day, multiplied by the energy to recharge the aircraft each time, grossed up for charger and conversion losses.</li>
    <li><strong>Everything else on the node</strong>: cameras, sensors or radios sharing the site.</li>
  </ol>
  <p>The standby figure is the one most often missing from datasheets, and it is frequently the largest term because it never stops. As an illustration only, using assumed rather than measured figures: a dock idling at 50 W uses 1.2 kWh a day before anything flies, while six recharges of a battery the size of the one above add less than 1 kWh. Double the standby in a hard winter and it dominates completely. That is why compatibility has to be established by measurement on the actual dock, not by reading its maximum input.</p>
  <p>Weather cuts both ways. The coldest weeks raise the baseline, reduce battery capacity and weaken the sun at the same time. In a northern winter, a hybrid architecture with fuelled backup is often the honest answer for a dock, the same logic that separates <a href="/harka/">Harka Solar and Harka Hybrid</a>.</p>
</div>''', eyebrow="Sizing", h2="The sortie arithmetic.")

body += section('''<div class="measure">
  <p>Persistent drone operations beyond visual line of sight (BVLOS) need regulatory approval as well as power. In the UK the Civil Aviation Authority is working towards <a href="https://www.caa.co.uk/drones/drone-regulations/policy-programmes/beyond-visual-line-of-sight-bvlos/" rel="noopener">routine BVLOS operations by 2027</a>, and remotely operated dock deployments are already being approved case by case. In June 2026, for example, <a href="https://www.dronewatch.eu/network-rail-obtains-uk-approval-for-bvlos-dji-dock-operations/" rel="noopener">Network Rail was reported to have received CAA approval</a> for BVLOS dock operations at two sites, flown from a remote operations centre.</p>
  <p>Power does not grant any permission. What it changes is where a dock can go and how dependable it is once there. As approvals become routine, the constraint on where docks can be placed shifts from regulation towards infrastructure: a landing zone needs power, a communications link and protection from the weather, and a remote landing zone needs all three without a grid.</p>
</div>''', eyebrow="Operations", h2="Where the rules sit, and what power changes.")

body += section(f'''<div class="measure">
  <p><strong>Compatibility is proven by test, not assumed.</strong> Melrakki powers only dock and aircraft combinations it has tested and passed. A datasheet's maximum input tells us very little about how a dock behaves at −10 °C at three in the morning, which is the condition the power system actually has to survive. Tell us the dock you use or are considering, and we will tell you plainly where it stands.</p>
  <p>That discipline is also why Greni exists.</p>
</div>
<div class="proof" style="margin-top:2rem;">
  <p><span class="status">In development. Prototype in field test</span></p>
  <p class="big" style="margin-top:1.2rem;">Melrakki Greni, MK-GR-01: an autonomous edge node for drones.</p>
  <p>Greni is an off-grid charging and docking station built on skid-mounted solar hybrid power, with a tilting solar array and lithium storage, designed around the dock's full load: the charge peaks and the baseline that runs day and night. A working prototype is in field test with a leading UK organisation. That evaluation is confidential, and we will not publish figures or compatibilities until testing lets us stand behind them.</p>
  <p><a href="/greni/">Explore Greni</a> or <a href="/greni/#interest">register early interest</a> to help shape how it is specified.</p>
</div>''', eyebrow="How we approach it", h2="Tested combinations only.")

faqs = [
    ("Can a drone dock run on solar power?",
     "In principle, yes, if generation and storage cover the dock's daily energy in the worst month and the storage can deliver the charging peak on a cold night. In a northern winter, solar alone often cannot, and a hybrid architecture with fuelled backup is the more honest design."),
    ("How much power does a drone dock need?",
     "Two figures matter. The peak is set by fast charging after each sortie; one widely deployed commercial dock, for example, lists a maximum input of 800 W. The daily energy is set mostly by the standby baseline, including heating or cooling, which runs 24 hours a day. The baseline is rarely published and has to be measured."),
    ("Will Melrakki power the drone dock we already have?",
     "Only if that dock and aircraft combination has been tested and passed by Melrakki. We do not assume compatibility from a datasheet. Tell us the dock and aircraft you use and we will tell you where it stands."),
    ("When will Greni be available?",
     "Greni is a working prototype in field test. We are not publishing dates, figures or compatibilities until testing lets us stand behind them. Registering interest puts your requirement in front of us while the specification is being finalised."),
    ("Does off-grid power affect BVLOS approval?",
     "No. Approval concerns the operation, the airspace and the operator. Power affects where a dock can be placed and how dependable it is. The two need planning together, but one does not grant the other."),
]

META = dict(
    slug=SLUG,
    title="Off-Grid Power for Drone Docks | Melrakki Systems",
    desc="Drone-in-a-box systems assume mains at the landing zone. How to engineer off-grid power for a dock: standby load, charge peaks, weather and sortie rate.",
    og_title="Powering a drone dock where there is no grid",
    og_desc="Why a drone dock is a harder load than a camera, the sortie arithmetic, and why compatibility has to be proven by test.",
    h1="Powering a drone dock where there is no grid.",
    eyebrow="Drone dock power",
    standfirst="What it takes to replace the mains connection a dock assumes with energy generated and stored on site, and why the answer depends on the dock's baseline as much as its charge peaks.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Tell us the dock, the aircraft, the site and how often it has to fly. We will be straight about what is tested, what is not, and where Greni fits.",
    cta_subject="Drone%20dock%20power%20enquiry", crumb_name="Drone docks",
    cta_secondary=("/greni/#interest", "Register interest in Greni"),
)
