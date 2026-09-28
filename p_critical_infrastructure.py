from common import *

SLUG = "critical-infrastructure"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="mailto:hello@melrakki.systems?subject=Critical%20infrastructure%20dependency%20review">Map one site with us</a>
      <a class="btn btn-secondary" href="#questions-to-ask">Questions to ask of any remote system</a>
    </div>'''

DEP_SVG = '''<figure class="fig">
<svg viewBox="0 0 760 300" role="img" aria-labelledby="dp-t dp-d">
<title id="dp-t">Shared dependency versus independent power at the edge</title>
<desc id="dp-d">Left: an asset and the camera protecting it both draw from the same local supply, so a single supply failure takes out the asset and its protection together. Right: the camera runs on autonomous power on site, so it keeps watching when the local supply fails.</desc>
<defs><marker id="b1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker>
<marker id="b2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah-hi"/></marker></defs>
<text x="20" y="26" class="tc">SHARED DEPENDENCY</text>
<rect x="110" y="44" width="160" height="56" rx="6" class="box"/><text x="190" y="70" text-anchor="middle" class="t">Local supply</text><text x="190" y="89" text-anchor="middle" class="ts">one point of failure</text>
<rect x="20" y="190" width="150" height="56" rx="6" class="box"/><text x="95" y="222" text-anchor="middle" class="t">Asset</text>
<rect x="210" y="190" width="150" height="56" rx="6" class="box"/><text x="285" y="216" text-anchor="middle" class="t">Camera</text><text x="285" y="235" text-anchor="middle" class="ts">goes dark with it</text>
<line x1="170" y1="100" x2="105" y2="186" class="ln" marker-end="url(#b1)"/>
<line x1="210" y1="100" x2="275" y2="186" class="ln" marker-end="url(#b1)"/>
<line x1="385" y1="30" x2="385" y2="270" class="grid"/>
<text x="410" y="26" class="tc">INDEPENDENT AT THE EDGE</text>
<rect x="490" y="44" width="160" height="56" rx="6" class="box"/><text x="570" y="70" text-anchor="middle" class="t">Local supply</text><text x="570" y="89" text-anchor="middle" class="ts">feeds the asset only</text>
<rect x="410" y="190" width="150" height="56" rx="6" class="box"/><text x="485" y="222" text-anchor="middle" class="t">Asset</text>
<rect x="600" y="190" width="150" height="56" rx="6" class="box-hi"/><text x="675" y="216" text-anchor="middle" class="t">Camera</text><text x="675" y="235" text-anchor="middle" class="ts">keeps watching</text>
<line x1="550" y1="100" x2="495" y2="186" class="ln" marker-end="url(#b1)"/>
<rect x="600" y="128" width="150" height="34" rx="6" class="box-hi"/><text x="675" y="150" text-anchor="middle" class="ts">autonomous power</text>
<line x1="675" y1="162" x2="675" y2="186" class="ln-hi" marker-end="url(#b2)"/>
<text x="20" y="290" class="ts">Conceptual. The same applies to sensors, telemetry and comms links.</text>
</svg>
<figcaption>Redundancy adds a second copy of something. Independence removes the shared dependency. At remote assets the second is usually cheaper, and it is the one that survives the event that takes out the first.</figcaption>
</figure>'''

body = section(f'''<div class="measure">
  <p class="lede">Critical infrastructure does not end at the control room. It ends where the equipment has to work: the far fence of a substation, a valve on a pipeline route, a roadside cabinet, a radio link on a hill.</p>
  <p>That edge is often powered by whatever is nearest. Very often that is the same local supply that feeds the asset being protected or monitored. When it fails, through a fault, a storm, a fire or deliberate interference, the protection fails with it, at exactly the moment it is needed. Restoring it means a site visit, in the same conditions that caused the outage.</p>
  <p>We have written about this at length. <a href="/resilience/the-last-mile-of-resilience/">The last mile of resilience</a> sets out why the edge behaves differently from the centre. <a href="/resilience/when-the-infrastructure-becomes-the-vulnerability/">When the infrastructure becomes the vulnerability</a> looks at the dependency chain beneath protective security. <a href="/resilience/the-sabotage-problem/">The sabotage problem</a> asks what happens when someone is trying to make it fail. This page is the practical version: where independent power belongs, and how to decide.</p>
</div>
{DEP_SVG}''', eyebrow="The problem", h2="The edge often depends on the power it is meant to protect.", tight_top=False)

body += section(table(["Remote asset", "What it usually runs on", "What takes it down", "What autonomous power changes"], [
    ["Substation and switching-site perimeter", "The site's own auxiliary or a nearby low-voltage supply", "The fault, fire or outage the security is there to watch", "Cameras and detection keep recording through the event and report it"],
    ["Pipeline and linear routes", "Nothing, or a generator at points of interest", "Distance: no supply for kilometres, and fuel that has to be driven out", "Surveillance and sensing at the points that matter, with nothing to deliver"],
    ["Rail and highway roadside systems", "Roadside supply along the route", "Cable faults, damage and theft; supply works that take months to programme", "Temporary or permanent monitoring without civil works or a supply application"],
    ["Telemetry and monitoring outstations", "Small local supply or a solar panel", "Undersized winter power, and a communications link on a different supply", "Power and link designed as one system, sized for the worst month"],
    ["Remote communications nodes", "Local mains with short battery backup", "A prolonged outage that outlasts the backup", "Days of autonomy rather than hours. See <a class=\"inline-link\" href=\"/telecommunications/\">remote communications power</a>"],
    ["Water, reservoir and remote utility compounds", "Site supply, often single feed", "Storms that take out supply and access together", "Protection that does not share the asset's single point of failure"],
]), eyebrow="Asset by asset", h2="What the edge depends on, and what fails first.",
    lead="The pattern repeats across sectors. The question to ask of every remote asset is the same: if its supply went tonight, what would still be watching it?")

body += section('''<ul class="checklist">
  <li>What does this system draw power from, and does that supply fail with the asset it protects?</li>
  <li>How long does it keep working if that supply goes, measured in the worst week of the year rather than the best?</li>
  <li>Is the communications link that carries its alarms powered independently, or does it share the same point of failure?</li>
  <li>Who has to travel for it to recover, and how long would that take in the weather that caused the outage?</li>
  <li>Does it report that it is failing before it fails, or do you find out when it is already dark?</li>
  <li>If fuel is involved, who delivers it, how often, and is the fuel store itself a target?</li>
  <li>Could someone disconnect it deliberately, and how visible and reachable is the thing they would cut?</li>
</ul>''', eyebrow="Questions to ask", h2="Seven questions for any remote security or monitoring system.", sid="questions-to-ask",
    lead="These apply whoever supplies the equipment. If the answers are uncomfortable, the edge is where to start.")

body += section('''<div class="measure">
  <p>UK government and regulators have moved steadily towards the same concern. The <a href="https://www.gov.uk/government/publications/uk-government-resilience-action-plan/uk-government-resilience-action-plan-html" rel="noopener">UK Government Resilience Action Plan</a> commits to mapping vulnerabilities and interdependencies across critical national infrastructure. The <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1081116/storm-arwen-review-final-report.pdf" rel="noopener">Storm Arwen review</a> recorded supply disruption to just over a million customers in November 2021: most were restored within a day, and a small but significant number were without power for up to 13 days. The <a href="https://assets.publishing.service.gov.uk/media/62828be08fa8f556165a1dec/GOV.UK_ECRRG_Post_Incident_Report_-_2021_2022_Severe_Storms.pdf" rel="noopener">communications industry's post-incident report</a> found battery backup at mobile sites depleted after a number of hours, because it had been designed for brief outages rather than prolonged ones.</p>
  <p>In June 2026 Ofcom's revised <a href="https://www.ofcom.org.uk/internet-based-services/network-security/resilience-guidance" rel="noopener">network and service resilience guidance</a> asked communications providers to seek to eliminate loss of key dependencies, including mains power, for a significant period of time, leaving the duration to risk assessment. The direction is consistent: the edge is expected to keep working when the supply around it does not.</p>
</div>''', eyebrow="Context", h2="Why the edge is now a resilience question, not a maintenance one.")

body += section(f'''<div class="measure">
  <p>We start with the asset and its worst credible week, then engineer the power from the load backwards: what has to keep running, for how long, with what access, in which conditions. Where a remote supply exists but is shared with the asset, the case for independence is usually stronger than the case for a bigger backup on the same feed.</p>
  <p>Melrakki provides the power infrastructure. The platforms are delivered open for the operator's own cameras, sensors and radios, or we specify them.</p>
</div>
{cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "Where the worst month covers the load and nothing should be delivered to site. Silent, no fuel, no engine.", "Harka Solar"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "Where uptime must hold through midwinter. Solar first, with an HVO generator that only recharges the battery.", "Harka Hybrid"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "Multiple loads, unusual voltages, integration onto an existing asset, or conditions no standard platform was sized for.", "Bespoke engineering"),
])}
<p class="tbl-note" style="margin-top:1.4rem;"><span class="status">In development</span>&nbsp; For linear assets that need an aerial look on demand, <a class="inline-link" href="/greni/">Greni</a>, our autonomous drone node, is a working prototype in field test.</p>''',
    eyebrow="Our approach", h2="Power that does not share the asset's point of failure.")

body += sources([
    ("Cabinet Office, UK Government Resilience Action Plan, July 2025", "https://www.gov.uk/government/publications/uk-government-resilience-action-plan/uk-government-resilience-action-plan-html"),
    ("Energy Emergencies Executive Committee, Storm Arwen Review: Final Report, June 2022", "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1081116/storm-arwen-review-final-report.pdf"),
    ("Electronic Communications Resilience and Response Group, Post Incident Report: 2021/2022 Severe Storms", "https://assets.publishing.service.gov.uk/media/62828be08fa8f556165a1dec/GOV.UK_ECRRG_Post_Incident_Report_-_2021_2022_Severe_Storms.pdf"),
    ("Ofcom, Network and Service Resilience Guidance, June 2026", "https://www.ofcom.org.uk/internet-based-services/network-security/resilience-guidance"),
    ("NPSA, Critical National Infrastructure", "https://www.npsa.gov.uk/about-npsa/critical-national-infrastructure"),
])

faqs = [
    ("Is a UPS enough for remote security equipment?",
     "A UPS bridges a short interruption on the same supply. It does not remove the dependency: if the outage lasts longer than the battery, or the fault is on the feed the UPS sits behind, the equipment goes dark. At remote assets, independent generation and storage sized for the worst week is usually the stronger answer."),
    ("Which remote assets are the best candidates for autonomous power?",
     "Assets where mains is absent or unreliable, where the security or monitoring shares a supply with the asset it protects, and where restoring a failed system means an expensive or slow site visit. Perimeter security, linear routes, roadside systems, telemetry and remote communications nodes are the common cases."),
    ("Does Melrakki supply the cameras and sensors?",
     "Melrakki provides the power infrastructure. The platforms are delivered open so operators can fit their own cameras, sensors and radios, and we can specify the payload where that helps."),
    ("How do you decide between solar-only and hybrid power for an infrastructure site?",
     "By the worst month. If the site's worst-month sun covers the load with margin, solar-only removes fuel entirely. If not, a hybrid carries the load on solar and battery and runs a generator only to recharge in the deficit window. Our <a href=\"/off-grid-power/\">guide to off-grid architectures</a> sets out the numbers."),
]

META = dict(
    slug=SLUG,
    title="Off-Grid Power for Critical Infrastructure | Melrakki",
    desc="Remote substations, pipelines, roadside and telemetry assets often depend on the power they protect. Where autonomous power removes that dependency.",
    og_title="Power for the edge of critical infrastructure",
    og_desc="Asset by asset: what the remote edge of critical infrastructure depends on, what fails first, and where independent power belongs.",
    h1="Power for the edge of critical infrastructure.",
    eyebrow="Critical infrastructure",
    standfirst="The control room has resilient supplies. The camera on the far fence, the telemetry outstation and the radio on the hill often run from the same local supply as the asset they protect. When it fails, they fail with it.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Pick one remote asset. We will map what it depends on with you, and engineer the power that removes the dependency that matters.",
    cta_subject="Critical%20infrastructure%20enquiry", crumb_name="Critical infrastructure",
)
