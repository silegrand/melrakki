from common import *

SLUG = "telecommunications"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="mailto:hello@melrakki.systems?subject=Remote%20communications%20power">Talk to an engineer</a>
      <a class="btn btn-secondary" href="#scale">What a small platform can carry</a>
    </div>
    <div class="spec-strip">
      <div><div class="n">25.3%</div><div class="l">Of reported UK network incidents, 2020 to 2022, were power-related</div></div>
      <div><div class="n">~5%</div><div class="l">Of UK mast sites had 6 h or more of backup</div></div>
    </div>'''

body = section('''<div class="measure">
  <p class="lede">On most remote sites the communications equipment is the smallest load and the one everything else depends on.</p>
  <p>The camera's footage, the sensor's alarm, the telemetry reading and the power system's own health report all leave the site through the same link. When the link loses power, the site does not just lose communications. It goes silent, and nobody knows whether anything else is still working.</p>
  <p>Communications power also tends to fail at the worst time. The storm that takes out the local supply is the same storm that makes the site hard to reach. Ofcom's technical work found that between 2020 and 2022, 25.3% of reported incidents on UK fixed and mobile networks were caused by power-related issues, and that only around 20% of mast sites had backup of at least an hour, and around 5% of at least six hours.</p>
</div>''', eyebrow="The problem", h2="Everything on a remote site reaches the world through one link.", tight_top=False)

body += section(f'''{table(["", "Backup", "Autonomy"], [
    ["Assumes", "Mains will return soon", "Mains may not exist, or may not return for days"],
    ["Measured in", "Minutes to hours", "Days, in the worst month"],
    ["Refilled by", "The grid, once restored", "Generation on site: solar, and a generator if the worst month demands it"],
    ["Fails when", "The outage outlasts the battery", "The design underestimated the load or the winter"],
    ["Right for", "Sites with a dependable supply and brief interruptions", "Sites with no supply, an unreliable one, or recovery measured in days"],
])}
<div class="measure" style="margin-top:1.6rem;">
  <p>Ofcom's revised <a href="https://www.ofcom.org.uk/internet-based-services/network-security/resilience-guidance" rel="noopener">network and service resilience guidance</a>, published in June 2026, asks communications providers to seek to eliminate loss of key dependencies, including mains power, "for a significant period of time", and leaves the duration to risk assessment. For a remote node, a realistic risk assessment usually ends with the same answer: the time it takes someone to reach the site in the weather that caused the outage.</p>
</div>''', eyebrow="Backup or autonomy", h2="Two different promises, often confused.")

body += section(f'''<div class="measure">
  <p>Communications loads span three orders of magnitude, and the honest answer depends on where yours sits. The Harka platforms carry a 1,080 W solar array on a 24 V DC system. In a southern UK December, that array alone sustains roughly a 25 W average load.</p>
</div>
{table(["Communications load", "Typical character", "What fits"], [
    ["Telemetry gateways, IoT and sensor links", "Small, steady draw with brief transmissions", "Harka Solar, comfortably, including in a UK winter"],
    ["4G or 5G routers, point-to-point links, small repeaters", "Modest continuous draw that rises with traffic", "Harka Solar where the winter average stays inside solar capacity; Harka Hybrid where it does not"],
    ["Multi-radio nodes and small cells", "Several radios, backhaul and some cooling", "Harka Hybrid, or a bespoke system sized to the node"],
    ["Macro mobile base stations", "Multi-band radio and cooling, commonly drawing kilowatts", "Beyond a single mast platform. A bespoke hybrid at a very different scale, and a conversation about whether autonomy or long-duration backup is the real requirement"],
])}
<p class="tbl-note">Take the actual figure from each device's datasheet in the configuration you will run it, averaged over a day at your real traffic pattern.</p>''',
    eyebrow="Scale", h2="What a small autonomous platform can honestly carry.", sid="scale")

body += section('''<div class="measure">
  <ul>
    <li><strong>Stay on DC where you can.</strong> Much communications equipment runs natively on DC. Every conversion to AC and back costs energy that a small solar system has to generate in December.</li>
    <li><strong>Measure the duty cycle, not the nameplate.</strong> Radios idle and burst. The daily average at your real traffic pattern is the number that sizes the system; the peak sizes the conversion.</li>
    <li><strong>Power and monitoring share a link.</strong> Optional remote monitoring reports the power system's health over the same connection it keeps alive. Design the two together, so the link is the last thing to go and the first warning arrives in time.</li>
    <li><strong>Siting pulls two ways.</strong> The antenna wants height and line of sight; the array wants an unshaded southern aspect. On a hillside or in a cutting those are not always the same spot. The Harka mast raises equipment to 6 m.</li>
    <li><strong>The failures correlate.</strong> Storms remove the supply and the access together. Size autonomy for how long it takes to reach the site in bad weather, not on a normal day.</li>
    <li><strong>Winter is the design case.</strong> Longest nights, lowest sun, coldest batteries. Insulation and ventilation of the enclosures are specified to each site's temperature range.</li>
  </ul>
</div>''', eyebrow="Engineering considerations", h2="Designing power for a communications node.")

body += section(f'''<div class="measure">
  <p>Melrakki provides the power infrastructure. We do not supply radios or network services. The platforms are delivered open, with a universal head mount and a lockable equipment bay for the operator's own equipment, and we can specify it where that helps.</p>
  <p>For the wider argument about why the edge of a network needs resilience engineered differently, read <a href="/resilience/the-last-mile-of-resilience/">the last mile of resilience</a>. For communications nodes that form part of a critical network, see <a href="/critical-infrastructure/">critical infrastructure</a>. For the architecture choices in more depth, see <a href="/off-grid-power/">off-grid power systems for remote sites</a>.</p>
</div>
{cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "For telemetry, gateways and low-power links whose winter average sits inside the site's solar capacity. No fuel, nothing to service but the site.", "Harka Solar"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "For routers, repeaters and multi-radio nodes that must stay on air through midwinter. HVO generator recharges only when needed.", "Harka Hybrid"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "Larger nodes, unusual voltages, several radios from one power system, or a site no standard platform was sized for.", "Bespoke engineering"),
])}''', eyebrow="Our approach", h2="The power layer beneath the network.")

body += sources([
    ("Ofcom, Network and Service Resilience Guidance, June 2026", "https://www.ofcom.org.uk/internet-based-services/network-security/resilience-guidance"),
    ("Ofcom, Mobile RAN power resilience: technical report, February 2025", "https://www.ofcom.org.uk/siteassets/resources/documents/consultations/category-1-10-weeks/272921-resilience-guidance-and-mobile-ran-power-back-up/associated-documents/mobile-ran-power-resilience-technical-report-cfi-update.pdf?v=390945"),
    ("Electronic Communications Resilience and Response Group, Post Incident Report: 2021/2022 Severe Storms", "https://assets.publishing.service.gov.uk/media/62828be08fa8f556165a1dec/GOV.UK_ECRRG_Post_Incident_Report_-_2021_2022_Severe_Storms.pdf"),
])

faqs = [
    ("Can a 4G router run on solar power all year in the UK?",
     "Usually, if the whole node's average draw stays well inside what the array can harvest in December. A 1,080 W array supports roughly a 25 W average load in southern England and about 16 W in Scotland in the worst month. Add cameras or heaters to the same system and a hybrid may be needed."),
    ("How long should battery backup last at a remote communications site?",
     "As long as it takes to restore the site in the conditions that caused the outage, which at a remote site is often days rather than hours. Ofcom's 2026 guidance leaves the duration to risk assessment. Where recovery depends on access in bad weather, autonomy with on-site generation is usually a better answer than a larger backup battery."),
    ("Can Melrakki power a mobile phone mast?",
     "Macro mobile base stations commonly draw kilowatts, which is beyond a single mast platform. That is a bespoke conversation at a different scale, and we will be straight about whether autonomous power or longer-duration backup is the right requirement."),
    ("Does Melrakki supply radios or connectivity?",
     "No. Melrakki provides the power infrastructure. You supply the radios, routers and network services, or we specify the equipment with you."),
]

META = dict(
    slug=SLUG,
    title="Off-Grid Power for Remote Communications | Melrakki",
    desc="Solar and hybrid power for radio, telemetry and network nodes where mains is absent or unreliable, and where a small autonomous platform stops being enough.",
    og_title="Keeping remote communications on air without the grid",
    og_desc="Backup versus autonomy, what a small solar platform can honestly carry, and how to power the link everything else depends on.",
    h1="Keeping remote communications on air without the grid.",
    eyebrow="Remote communications power",
    standfirst="A radio link, a router or a telemetry gateway is usually the smallest load on a site and the one everything else depends on. Powering it independently of the grid is a small engineering problem with large consequences.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Tell us the radio, the duty cycle, the site and how long it takes to reach in bad weather. We will engineer the power that keeps it on air.",
    cta_subject="Remote%20communications%20enquiry", crumb_name="Communications",
)
