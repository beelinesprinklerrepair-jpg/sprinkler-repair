import os, re

BASE = '/sessions/charming-confident-dirac/mnt/Building Beeline Website/'

# ─── Page groups ─────────────────────────────────────────────────────────────
CITY_REPAIR = [
    'nampa-sprinkler-repair.html','meridian-sprinkler-repair.html',
    'boise-sprinkler-repair.html','eagle-sprinkler-repair.html',
    'caldwell-sprinkler-repair.html','kuna-sprinkler-repair.html',
    'star-sprinkler-repair.html','middleton-sprinkler-repair.html',
]
SERVICE_PAGES = [
    'sprinkler-repair.html','sprinkler-installation.html','spring-turn-on.html',
    'winterization.html','backflow.html','valve-repair-treasure-valley.html',
    'sprinkler-head-replacement-treasure-valley.html','controller-replacement.html',
    'broken-sprinkler-line-repair.html','sprinkler-manifold-repair.html',
    'drip-irrigation-installation.html',
]
BOISE_SUB = [
    'boise-sprinkler-valve-repair.html','boise-sprinkler-leak-repair.html',
    'boise-sprinkler-head-replacement.html','boise-sprinkler-turn-on.html',
    'boise-backflow-repair.html','boise-sprinkler-installation.html',
]
MERIDIAN_VALVE = ['meridian-sprinkler-valve-repair.html']
BLOWOUT = [
    'nampa-sprinkler-blowouts.html','meridian-sprinkler-blowouts.html',
    'boise-sprinkler-blowouts.html','eagle-sprinkler-blowouts.html',
    'caldwell-sprinkler-blowouts.html','kuna-sprinkler-blowouts.html',
    'star-sprinkler-blowouts.html','middleton-sprinkler-blowouts.html',
]

# ─── Snippets ────────────────────────────────────────────────────────────────
FORM_CSS = """
/* Hero quote form card */
.hero-quote-card{width:100%;max-width:360px;background:rgba(0,0,0,.55);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.18);border-radius:16px;padding:28px 26px 24px;flex-shrink:0}
.hqc-eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--yellow);margin-bottom:8px}
.hqc-title{font-size:1.15rem;font-weight:800;color:#fff;line-height:1.3;margin-bottom:18px}
.hqc-field{display:flex;flex-direction:column;gap:4px;margin-bottom:10px}
.hqc-field label{font-size:.75rem;font-weight:600;color:rgba(255,255,255,.6);letter-spacing:.04em}
.hqc-field input,.hqc-field select{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:9px 13px;color:#fff;font-size:.95rem;font-family:inherit;outline:none;transition:border-color .15s;width:100%;-webkit-appearance:none;appearance:none}
.hqc-field input::placeholder{color:rgba(255,255,255,.35)}
.hqc-field input:focus,.hqc-field select:focus{border-color:var(--yellow)}
.hqc-field select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='rgba(255,255,255,.5)' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 13px center;padding-right:36px;cursor:pointer}
.hqc-field select option{background:#1a3a1a;color:#fff}
.hqc-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.hqc-submit{display:block;width:100%;background:var(--yellow);color:var(--ink);font-weight:900;font-size:1rem;padding:14px;border:none;border-radius:10px;cursor:pointer;margin-top:16px;transition:opacity .15s}
.hqc-submit:hover{opacity:.88}
.hqc-phone{display:block;text-align:center;color:rgba(255,255,255,.55);font-size:.8rem;margin-top:12px}
.hqc-phone a{color:rgba(255,255,255,.8);text-decoration:none;font-weight:600}
.hqc-phone a:hover{color:#fff}
.hqc-success{text-align:center;padding:20px 0}
.hqc-success .check{font-size:2.5rem;margin-bottom:10px}
.hqc-success p{color:#fff;font-size:1rem;font-weight:600;line-height:1.5}
.hqc-success span{color:rgba(255,255,255,.6);font-size:.85rem}
.hero-right-form{flex-shrink:0}
@media(max-width:860px){.city-hero-content,.svc-hero-content{flex-direction:column!important}.hero-quote-card{max-width:100%}}
"""

FORM_HTML = """<div class="hero-quote-card">
  <div class="hqc-eyebrow">Free Quote · Fast Response</div>
  <div class="hqc-title">What can we fix for you?</div>
  <div class="hqc-success" id="hqcSuccess" style="display:none">
    <div class="check">✅</div>
    <p>Got it! We'll call you shortly.</p>
    <span>Most calls back within 1 hour</span>
  </div>
  <form id="hqcForm" action="https://formspree.io/f/xwvdqvlb" method="POST">
    <div class="hqc-field">
      <label for="fname">First Name</label>
      <input type="text" id="fname" name="name" placeholder="Calvin" required>
    </div>
    <div class="hqc-row">
      <div class="hqc-field">
        <label for="fphone">Phone</label>
        <input type="tel" id="fphone" name="phone" placeholder="(208) 555-0100">
      </div>
      <div class="hqc-field">
        <label for="femail">Email</label>
        <input type="email" id="femail" name="email" placeholder="you@email.com">
      </div>
    </div>
    <div id="contactError" style="display:none;font-size:.75rem;color:#ff8a8a;margin-top:-8px;margin-bottom:10px;">Please enter a phone number or email.</div>
    <div class="hqc-field">
      <label for="fservice">What do you need?</label>
      <select id="fservice" name="service">
        <option value="" disabled selected>Choose a service…</option>
        <option>Sprinkler Repair</option>
        <option>Fall Blowout / Winterization</option>
        <option>Sprinkler Installation</option>
        <option>Spring Turn-On</option>
        <option>Backflow Testing / Repair</option>
        <option>Valve Repair</option>
        <option>Sprinkler Head Replacement</option>
        <option>Controller / Timer Replacement</option>
        <option>Other / Not Sure</option>
      </select>
    </div>
    <div class="hqc-field">
      <select id="fcity" name="city">
        <option value="" disabled selected>Your city…</option>
        <option>Nampa</option>
        <option>Meridian</option>
        <option>Boise</option>
        <option>Caldwell</option>
        <option>Eagle</option>
        <option>Kuna</option>
        <option>Star</option>
        <option>Middleton</option>
        <option>Other</option>
      </select>
    </div>
    <button type="submit" class="hqc-submit">Get My Free Quote →</button>
  </form>
  <p class="hqc-phone">Or call / text: <a href="tel:2088802712">(208) 880-2712</a></p>
</div>"""

FORM_JS = """
<script>
(function(){
  var form=document.getElementById('hqcForm');
  if(!form)return;
  var success=document.getElementById('hqcSuccess');
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var phone=document.getElementById('fphone').value.trim();
    var email=document.getElementById('femail').value.trim();
    var err=document.getElementById('contactError');
    if(!phone&&!email){err.style.display='block';return;}
    err.style.display='none';
    fetch(form.action,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'}})
      .then(function(r){if(r.ok){window.location.href='thank-you.html';}else{alert('Something went wrong. Please call us at (208) 880-2712.');}})
      .catch(function(){alert('Something went wrong. Please call us at (208) 880-2712.');});
  });
})();
</script>
"""

# ─── Helpers ─────────────────────────────────────────────────────────────────
def find_div_end(html, start):
    """Find the closing </div> for the div opening that starts at `start`."""
    depth = 0
    pos = start
    while pos < len(html):
        o = html.find('<div', pos)
        c = html.find('</div>', pos)
        if o == -1 and c == -1:
            break
        if o != -1 and (c == -1 or o < c):
            depth += 1
            pos = o + 4
        else:
            depth -= 1
            if depth == 0:
                return c  # position of </div>
            pos = c + 6
    return -1

def inject_css(html):
    return html.replace('</style>', FORM_CSS + '</style>', 1)

def inject_js(html):
    # Insert our script block right before </body>
    return html.replace('</body>', FORM_JS + '\n</body>', 1)

# ─── City-hero-content pages (city repair + service pages) ───────────────────
def process_city_hero(html, fname):
    marker = '<div class="city-hero-content">'
    idx = html.find(marker)
    if idx == -1:
        print(f'  SKIP: no city-hero-content in {fname}')
        return html
    inner_start = idx + len(marker)
    div_end = find_div_end(html, idx)
    if div_end == -1:
        print(f'  ERROR: could not find end of city-hero-content in {fname}')
        return html
    inner = html[inner_start:div_end]
    # Build new content: hero-left wrapping original + hero-right with form
    new_inner = f'\n  <div class="hero-left">{inner}  </div>\n  <div class="hero-right-form">\n{FORM_HTML}\n  </div>\n'
    new_html = html[:idx] + '<div class="city-hero-content" style="display:flex;gap:40px;align-items:flex-start">' + new_inner + html[div_end:]
    return new_html

# ─── svc-hero-content single-column pages (boise sub + meridian valve) ───────
def process_svc_hero(html, fname):
    marker = '<div class="svc-hero-content">'
    idx = html.find(marker)
    if idx == -1:
        print(f'  SKIP: no svc-hero-content in {fname}')
        return html
    inner_start = idx + len(marker)
    div_end = find_div_end(html, idx)
    if div_end == -1:
        print(f'  ERROR: could not find end of svc-hero-content in {fname}')
        return html
    inner = html[inner_start:div_end]
    new_inner = f'\n  <div class="hero-left">{inner}  </div>\n  <div class="hero-right-form">\n{FORM_HTML}\n  </div>\n'
    new_html = html[:idx] + '<div class="svc-hero-content" style="display:flex;gap:40px;align-items:flex-start">' + new_inner + html[div_end:]
    return new_html

# ─── Blowout pages: replace hero-right-cta div ───────────────────────────────
def process_blowout(html, fname):
    marker = '<div class="hero-right-cta">'
    idx = html.find(marker)
    if idx == -1:
        print(f'  SKIP: no hero-right-cta in {fname}')
        return html
    div_end = find_div_end(html, idx)
    if div_end == -1:
        print(f'  ERROR: could not find end of hero-right-cta in {fname}')
        return html
    # Replace from idx to div_end + len('</div>') with form card
    new_html = html[:idx] + FORM_HTML + html[div_end + len('</div>'):]
    return new_html

# ─── Main ─────────────────────────────────────────────────────────────────────
SKIP_MARKER = 'hqcForm'  # already processed if this exists

def process_file(fname, processor):
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'  NOT FOUND: {fname}')
        return
    html = open(path, 'rb').read().decode('utf-8', 'replace')
    if SKIP_MARKER in html:
        print(f'  SKIP (already done): {fname}')
        return
    html = inject_css(html)
    html = processor(html, fname)
    html = inject_js(html)
    open(path, 'wb').write(html.encode('utf-8'))
    print(f'  OK: {fname}')

print('=== City repair pages ===')
for f in CITY_REPAIR:
    process_file(f, process_city_hero)

print('\n=== Service pages ===')
for f in SERVICE_PAGES:
    process_file(f, process_city_hero)

print('\n=== Boise sub-pages ===')
for f in BOISE_SUB:
    process_file(f, process_svc_hero)

print('\n=== Meridian valve ===')
for f in MERIDIAN_VALVE:
    process_file(f, process_svc_hero)

print('\n=== Blowout pages ===')
for f in BLOWOUT:
    process_file(f, process_blowout)

print('\nDone.')
