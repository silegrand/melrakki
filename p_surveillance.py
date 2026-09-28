from common import *

SLUG = "solar-powered-surveillance"

hero_extra = '''<div class="cta-row">
      <a class="btn btn-primary" href="#worksheet">Work out your load</a>
      <a class="btn btn-secondary" href="mailto:hello@melrakki.systems?subject=Surveillance%20power%20specification">Request a specification</a>
    </div>
    <div class="spec-strip">
      <div><div class="n">13 years</div><div class="l">Building off-grid surveillance and power</div></div>
      <div><div class="n">58 sites</div><div class="l">Solar CCTV infrastructure, Kazakhstan</div></div>
      <div><div class="n">~16 h</div><div class="l">Of darkness, southern UK, December</div></div>
      <div><div class="n">~25 W</div><div class="l">Solar-only average, same month</div></div>
    </div>'''

PROFILE_SVG = '''<figure class="fig">
<svg viewBox="0 0 760 290" role="img" aria-labelledby="pr-t pr-d">
<title id="pr-t">A December day for a solar surveillance mast</title>
<desc id="pr-d">Over 24 hours in December, solar generation is a short, low hump between late morning and mid-afternoon. The load has a constant baseline for cameras and communications, and a large additional block through the long night when infrared illumination is on. The night-time block is far larger than the daytime generation.</desc>
<line x1="60" y1="230" x2="740" y2="230" class="grid"/>
<line x1="60" y1="40" x2="60" y2="230" class="grid"/>
<text x="60" y="252" text-anchor="middle" class="ts">00:00</text><text x="230" y="252" text-anchor="middle" class="ts">06:00</text><text x="400" y="252" text-anchor="middle" class="ts">12:00</text><text x="570" y="252" text-anchor="middle" class="ts">18:00</text><text x="740" y="252" text-anchor="middle" class="ts">24:00</text>
<path d="M60,230 L60,120 L292,120 L292,190 L512,190 L512,120 L740,120 L740,230 Z" class="area2"/>
<path d="M292,230 C330,230 350,160 400,150 C450,160 470,230 512,230 Z" class="area"/>
<text x="176" y="112" text-anchor="middle" class="t">Infrared on</text>
<text x="626" y="112" text-anchor="middle" class="t">Infrared on</text>
<text x="400" y="140" text-anchor="middle" class="t">Solar harvest</text>
<text x="400" y="214" text-anchor="middle" class="ts">baseline: cameras, router, analytics</text>
<text x="20" y="30" class="tc">POWER (ILLUSTRATIVE)</text>
<text x="60" y="280" class="ts">Amber: load. Cyan: December solar generation. Shapes illustrative, not to scale.</text>
</svg>
<figcaption>Winter works against a surveillance mast from three directions at once: the longest nights keep infrared on for around 16 hours, the shortest days give the least generation, and the cold reduces what the battery can deliver.</figcaption>
</figure>'''

WORKSHEET = '''<div class="ws" id="worksheet">
  <div class="calc-head">
    <p class="k">Surveillance load worksheet</p>
    <h3>Build your daily energy figure</h3>
    <p class="calc-sub">Replace the illustrative rows with your own devices. Use each datasheet's typical power, not its maximum or its PoE class, and the hours a day it actually draws. The result compares your load with what the Harka array can harvest in your worst month.</p>
  </div>
  <table>
    <thead><tr><th>Device</th><th>Watts</th><th>Hours a day</th><th style="text-align:right">Wh a day</th></tr></thead>
    <tbody id="wsRows">
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 1" value="Fixed camera"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 1 watts" value="6"></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 1 hours" value="24"></td><td class="out" data-l="Wh a day">0</td></tr>
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 2" value="PTZ camera, average"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 2 watts" value="12"></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 2 hours" value="24"></td><td class="out" data-l="Wh a day">0</td></tr>
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 3" value="Infrared illuminator"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 3 watts" value="20"></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 3 hours" value="16"></td><td class="out" data-l="Wh a day">0</td></tr>
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 4" value="4G router"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 4 watts" value="6"></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 4 hours" value="24"></td><td class="out" data-l="Wh a day">0</td></tr>
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 5" value="Enclosure heater"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 5 watts" value="10"></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 5 hours" value="8"></td><td class="out" data-l="Wh a day">0</td></tr>
      <tr><td class="nm" data-l="Device"><input class="row-name" aria-label="Device 6" value="" placeholder="Add a device"></td><td data-l="Watts"><input class="num" type="number" min="0" step="0.5" inputmode="decimal" aria-label="Device 6 watts" value=""></td><td data-l="Hours a day"><input class="num" type="number" min="0" max="24" step="0.5" inputmode="decimal" aria-label="Device 6 hours" value=""></td><td class="out" data-l="Wh a day">0</td></tr>
    </tbody>
  </table>
  <div class="ws-foot">
    <label class="ws-psh" for="wsPsh">Worst-month peak sun hours <input id="wsPsh" class="num" type="number" min="0.1" max="8" step="0.1" value="0.8" inputmode="decimal"></label>
    <div class="presets" role="group" aria-label="Rough December starting points">
      <button type="button" data-psh="0.8">Southern UK ~0.8</button>
      <button type="button" data-psh="0.5">Scotland ~0.5</button>
      <button type="button" data-psh="1.8">S. Europe ~1.8</button>
    </div>
  </div>
  <div class="calc-out" id="wsOut" aria-live="polite"></div>
  <p class="calc-note">Illustrative starting rows only, not measurements of any product. Harvest uses the 1,080 W Harka array and a 0.7 performance ratio. Reserves use about 7.5 kWh usable on Harka Solar and 4.1 kWh on Harka Hybrid, to 80% depth of discharge. Indicative only; the real answer comes from a full assessment.</p>
</div>
<script>
(function(){
  var rows=document.querySelectorAll('#wsRows tr'), psh=document.getElementById('wsPsh'), out=document.getElementById('wsOut');
  if(!rows.length||!psh||!out) return;
  function f(n){return Math.round(n).toLocaleString('en-GB');}
  function hrs(h){return h>=48?(h/24).toFixed(1)+' days':f(h)+' h';}
  function calc(){
    var wh=0, list=[];
    rows.forEach(function(r){var i=r.querySelectorAll('input'),w=parseFloat(i[1].value)||0,h=Math.min(24,parseFloat(i[2].value)||0),e=w*h;r.querySelector('.out').textContent=f(e);wh+=e;if(e>0)list.push((i[0].value||'Device')+': '+w+' W x '+h+' h');});
    var P=Math.max(0.1,parseFloat(psh.value)||0.1), harvest=1080*P*0.7, avg=wh/24, ratio=wh>0?harvest/wh:99, cls, v, d;
    if(ratio>=1.15){cls='v-good';v='Solar-only looks viable in your worst month';d='The estimated worst-month harvest covers this load with margin. Harka Solar, with no fuel on site, is the likely answer.';}
    else if(ratio>=1){cls='v-borderline';v='Borderline. Worth a proper assessment';d='The harvest only just covers the load. One hard week could close the margin; reducing the night load or adding hybrid backup removes the risk.';}
    else{cls='v-hybrid';v='Solar alone falls short in the worst month';d='At this load the array cannot refill the battery in the worst month. Harka Hybrid, a lower night load, or a larger bespoke system are the honest routes.';}
    var body=encodeURIComponent('Surveillance load worksheet\\n\\n'+list.join('\\n')+'\\n\\nDaily energy: '+f(wh)+' Wh (average '+avg.toFixed(1)+' W)\\nWorst-month peak sun hours: '+P+'\\nIndicative result: '+v+'\\n\\nSite location:\\nAccess:\\nConditions:');
    out.innerHTML='<div class="verdict '+cls+'"><strong>'+v+'</strong><p>'+d+'</p></div><div class="nums"><div><span class="nl">Daily energy</span><span class="nv">'+f(wh)+' Wh</span></div><div><span class="nl">Average load</span><span class="nv">'+avg.toFixed(1)+' W</span></div><div><span class="nl">Worst-month harvest, est.</span><span class="nv">~'+f(harvest)+' Wh</span></div><div><span class="nl">Battery reserve, Harka Solar</span><span class="nv">'+(avg>0?hrs(7500/avg):'n/a')+'</span></div><div><span class="nl">Battery reserve, Harka Hybrid</span><span class="nv">'+(avg>0?hrs(4100/avg):'n/a')+'</span></div><div><span class="nl">Solar-only capacity here</span><span class="nv">~'+(harvest/24).toFixed(0)+' W avg</span></div></div><a class="btn btn-primary calc-cta" href="mailto:hello@melrakki.systems?subject=Surveillance%20load%20worksheet&body='+body+'">Send this to an engineer</a>';
  }
  document.getElementById('worksheet').addEventListener('input',calc);
  document.querySelectorAll('#worksheet .presets button').forEach(function(b){b.addEventListener('click',function(){psh.value=b.getAttribute('data-psh');calc();});});
  calc();
})();
</script>'''

body = section(f'''<div class="measure">
  <p class="lede">Remote CCTV rarely fails because a camera breaks. It fails because the power was sized for a summer day and asked to survive a winter night.</p>
  <p>A surveillance mast is not a constant load. Fixed cameras draw steadily. PTZ cameras draw more when they move and when their housings heat. Infrared illumination draws nothing by day and a great deal by night. A cellular router idles, then draws hard while it uploads. An enclosure heater does its heaviest work on the coldest night of the year.</p>
  <p>In a UK December all of that lines up against you. The nights are around sixteen hours long, so infrared runs for most of the day. The sun is lowest, so the array returns the least. And the cold reduces how much the battery can deliver. Size to the annual average and the system is fine for nine months and dark for the three that matter most.</p>
</div>
{PROFILE_SVG}''', eyebrow="The problem", h2="Most solar CCTV is sized for the brochure, not the night.", tight_top=False)

body += section(table(["Device", "How it behaves", "What to measure"], [
    ["Fixed IP camera", "A steady draw around the clock; higher with on-board analytics or a heated housing", "Typical power from the datasheet, with analytics and heater states as used"],
    ["PTZ camera", "Idle between moves, higher when panning and zooming, highest with heaters and wipers", "An average over a realistic patrol pattern, not the peak"],
    ["Infrared illuminator", "Nothing by day, full draw through the night", "Watts multiplied by the longest night of the year, not the average"],
    ["Thermal camera", "Steady and often higher than a visible camera", "Typical power, including any housing heater"],
    ["Router or radio link", "Idle, then bursts while transmitting; average rises with how much video leaves the site", "Average over a day at your real upload pattern"],
    ["Recorder, analytics, detectors", "Steady; edge analytics can dominate a small budget", "Typical power in the configuration you will actually run"],
    ["Enclosure heating and cooling", "Seasonal, and at its worst in the same weeks as the weakest sun", "Worst-month duty cycle for your site"],
]), eyebrow="The load budget", h2="Every device, how it behaves across a day, and what to measure.",
    lead="A PoE class tells you the budget a switch reserves for a device, not what it draws. Power budgets built from PoE classes or nameplate maxima oversize the system; budgets built from optimistic averages leave it dark. Measure or take the datasheet's typical figure, and count the switch or injector losses too.")

body += section(WORKSHEET, eyebrow="Try it", h2="What does your mast really draw?",
    lead="Six rows are enough for most masts. Change a figure and the result updates.")

body += section(f'''<div class="measure">
  <p>Using the Harka array's own figures, solar alone sustains an average load of roughly <strong>25 W in a southern UK December</strong> and <strong>16 W in Scotland</strong>. Most multi-camera masts with infrared and a cellular link average more than that through the winter. That does not rule solar out. It means choosing, deliberately, between three routes.</p>
</div>
{table(["Route", "What it involves", "When it is right"], [
    ["Lower the winter load", "Infrared or white light only on detection; event-based upload rather than continuous streaming; cameras chosen on measured draw; analytics placed where the power is", "The mission tolerates it, and the saving brings the worst month inside solar capacity"],
    ["Solar only, larger", "A bigger array and battery than the standard platform, engineered as a bespoke system", "Fuel on site is unacceptable, and the footprint, weight and cost are justified"],
    ["Solar hybrid", "Solar and battery carry the load; a generator recharges the pack only in the deficit window", "Uptime cannot be risked through midwinter and a small, infrequent fuel resupply is acceptable"],
])}
<div class="callout"><span class="k">Why the hybrid burns so little</span><p>In a hybrid, the generator is not the power source. It is a charger for the battery. It runs only when the pack falls to 40% state of charge, refills it, and stops. Starting at 40% rather than lower keeps each battery cycle shallow, which is what makes lead-acid last; if the generator were ever unavailable, the battery still holds 41 hours at 100 W. Through spring, summer and autumn the sun usually covers the load and the generator barely runs. The fuel it does burn is concentrated in the weeks when solar genuinely cannot keep up.</p></div>''',
    eyebrow="Winter", h2="Solar only, or hybrid: let the worst month decide.")

body += section(f'''<div class="measure">
  <p>Power is only half of a working surveillance mast. The rest is where it stands, what it carries and who has to look after it.</p>
  <ul>
    <li><strong>Your equipment, on an open platform.</strong> Harka is delivered with a universal head mount and a lockable steel equipment bay (370 &times; 200 &times; 470 mm) that accept the operator's own cameras, lighting, sensors and radios. We can also specify them.</li>
    <li><strong>Height and field of view.</strong> The Harka mast raises the head to 6 m. Camera choice and siting do the rest.</li>
    <li><strong>Communications are part of the load.</strong> A 4G, 5G or satellite link is often the largest continuous draw after infrared. How much video leaves the site decides how much energy the link needs.</li>
    <li><strong>Knowing it is healthy.</strong> Optional remote monitoring reports the power system's condition over the site's link, so a visit is triggered by need rather than by schedule.</li>
    <li><strong>Theft and tampering.</strong> Sensitive components sit in the lockable bay. Harka Solar carries no fuel, so there is nothing on site worth siphoning.</li>
    <li><strong>The site itself.</strong> Wind loading, insulation and ventilation are engineered to each site's requirement. Platforms travel ten to a truck, with forklift pockets, and one person raises the mast without tools.</li>
  </ul>
  <p>For the wider question of what a protective system depends on, and why a robust camera can still be an operationally fragile one, read <a href="/resilience/when-the-infrastructure-becomes-the-vulnerability/">when the infrastructure becomes the vulnerability</a>.</p>
</div>''', eyebrow="Deployment", h2="Engineering the mast, not just the power.")

body += section('''<div class="proof">
  <p class="eyebrow">Experience</p>
  <p class="big">Thirteen years of putting surveillance where the grid does not go.</p>
  <p>The team behind Melrakki has spent more than a decade designing and deploying off-grid solar surveillance, long before the work carried this name. That includes solar CCTV infrastructure across 58 oil and gas sites in Kazakhstan, and deployments across highways, construction and critical infrastructure. It is where the load-backwards method comes from: remote power rarely looks the same on a drawing as it does when someone has to keep it running through a winter.</p>
  <p><a href="/about/">More about Melrakki and its founder</a>.</p>
</div>''')

body += section(cards([
    ("/harka/", "Clean tier · MK-HK-S6", "Harka Solar", "For masts whose winter load sits within the site's worst-month sun. No fuel, no engine, no emissions, 75 h battery reserve at 100 W.", "Harka Solar"),
    ("/harka/#specifications", "Endurance tier · MK-HK-H6", "Harka Hybrid", "For typical UK surveillance loads through midwinter. Silent on battery; the HVO generator recharges only when the sun cannot.", "Harka Hybrid"),
    ("/bespoke/", "Engineered to your application", "Bespoke", "Heavier payloads, multiple masts from one power source, unusual voltages, or a site no standard platform was sized for.", "Bespoke engineering"),
]), eyebrow="Platforms", h2="Surveillance power, specified by the load.",
    lead="The full sizing method is in <a class=\"inline-link\" href=\"/resilience/designing-power-from-the-load-backwards/\">designing power from the load backwards</a>. Surveillance on sites with more demanding conditions is covered under <a class=\"inline-link\" href=\"/oil-and-gas/\">oil and gas</a>, <a class=\"inline-link\" href=\"/critical-infrastructure/\">critical infrastructure</a> and <a class=\"inline-link\" href=\"/defence-and-security/\">defence and security</a>.")

faqs = [
    ("How long will a solar CCTV tower run without sun?",
     "It depends on the load. Harka Solar holds about 7.5 kWh usable, which is 75 hours at 100 W, around 150 hours at 50 W and around 300 hours at 25 W, with no solar input at all, at 25 °C. Cold reduces these figures. Harka Hybrid holds 41 hours at 100 W on battery, after which its generator recharges the pack."),
    ("Does solar CCTV work in a UK winter?",
     "At low loads, yes. With a 1,080 W array, a southern UK December supports roughly a 25 W average load and Scotland roughly 16 W. Masts with infrared, several cameras and a cellular link usually average more than that in winter, which is why a hybrid, a lower night load or a larger bespoke system is often the honest answer."),
    ("How much power does a CCTV camera use?",
     "Take the typical figure from the camera's datasheet in the configuration you will run it, including any housing heater and analytics. Do not use the PoE class, which is the budget the switch reserves rather than the camera's consumption. Infrared illumination is usually the largest single night-time load, so size it against the longest night of the year."),
    ("Can I use my own cameras and radios?",
     "Yes. Harka is delivered as an open platform with a universal head mount and a lockable internal equipment bay that accept the operator's own cameras, lighting, sensors and radios. Melrakki can also specify the payload if you prefer."),
    ("Is a solar CCTV tower secure against theft and tampering?",
     "Sensitive components sit in a lockable steel compartment, and Harka Solar carries no fuel, which removes one of the most common reasons remote sites are targeted. The physical security of the mast itself is part of the site design."),
]

META = dict(
    slug=SLUG,
    title="Solar-Powered CCTV and Surveillance Power | Melrakki",
    desc="What it takes to keep remote CCTV running on solar: camera load, infrared at night, winter sun, battery reserve, and when a hybrid backup is the honest answer.",
    og_title="Solar power for surveillance that holds through winter",
    og_desc="The camera load budget, the UK winter numbers and the honest choice between solar-only and hybrid power for remote CCTV.",
    h1="Solar power for surveillance that holds through winter.",
    eyebrow="Solar-powered surveillance",
    standfirst="This is about the part of a solar CCTV system that decides whether the cameras are still recording in February: the load, the longest night, the weakest sun and the battery that has to bridge them.",
    hero_extra=hero_extra, body=body, faqs=faqs,
    cta_sub="Send us the camera schedule, the site and its access. We will tell you whether solar alone will hold, and what will if it will not.",
    cta_subject="Surveillance%20power%20enquiry", crumb_name="Surveillance",
)
