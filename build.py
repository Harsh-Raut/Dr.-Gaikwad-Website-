#!/usr/bin/env python3
"""
Dr. Gaikwad's Institute — static site generator.

Writes plain .html files to the project root. There is no runtime dependency:
the output is pure static HTML/CSS/JS and deploys to Netlify as-is. This script
exists only so the shared header, navigation and footer live in one place
instead of being copy-pasted across fourteen pages.

    python3 build.py
"""

import os, re, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))


def _asset_version():
    """Short hash of the CSS+JS so browsers pick up changes immediately
    instead of serving a stale cached stylesheet."""
    h = hashlib.sha256()
    for rel in ("assets/css/site.css", "assets/js/site.js"):
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    return h.hexdigest()[:8]


ASSET_VER = _asset_version()

PHONE1, PHONE1_H = "+918691973874", "+91 86919 73874"
PHONE2, PHONE2_H = "+919321690625", "+91 93216 90625"
EMAIL = "drgaikwadinstitute@gmail.com"
ADDR_H = "203 Akanksha, Opp. Plaza, Dadar (W), Mumbai 400 028"
WA = "https://wa.me/918691973874"

# Google Maps — the institute's own verified listing.
MAP_LAT, MAP_LNG = "19.0216642", "72.8420722"
MAP_LINK = "https://maps.app.goo.gl/RrdZxm7pzS1dAvXf8"
MAP_EMBED = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}&z=17&hl=en&output=embed"
MAP_DIRECTIONS = f"https://www.google.com/maps/dir/?api=1&destination={MAP_LAT},{MAP_LNG}"

NAV = [
    ("index.html",       "Home"),
    ("about.html",       "About"),
    ("courses.html",     "Courses"),
    ("fees.html",        "Fees"),
    ("admissions.html",  "Admissions"),
    ("placements.html",  "Placements"),
    ("gallery.html",     "Gallery"),
    ("contact.html",     "Contact"),
]

# Course data — single source of truth for tables and detail pages.
COURSES = [
    dict(slug="patient-care", abbr="DPC · DPCA", fee=60000, adm=12000, icon="stethoscope",
         name="Diploma in Patient Care / Patient Care Assistant",
         short="Patient Care", elig="10th pass or fail"),
    dict(slug="medical-lab-technology", abbr="DMLT", fee=68000, adm=14000, icon="microscope",
         name="Diploma in Medical Laboratory Technology",
         short="Medical Lab Technology", elig="12th pass or fail"),
    dict(slug="operation-theatre", abbr="DOTT", fee=60000, adm=12000, icon="ot",
         name="Diploma in Operation Theatre Technician",
         short="Operation Theatre", elig="10th pass or fail"),
    dict(slug="optometry", abbr="DOPTO", fee=37500, adm=15000, icon="eye",
         name="Diploma in Optometry",
         short="Optometry", elig="10th pass or fail"),
]

MONOGRAM = ('<svg width="46" height="46" viewBox="0 0 46 46" role="img" aria-label="Institute monogram">'
            '<circle cx="23" cy="23" r="21.2" fill="none" stroke="var(--navy)" stroke-width="1.6"/>'
            '<circle cx="23" cy="23" r="17.6" fill="none" stroke="var(--brass)" stroke-width="1"/>'
            '<circle cx="23" cy="23" r="15.4" fill="var(--navy)"/>'
            '<text x="23" y="28.4" text-anchor="middle" font-family="Georgia, serif" font-size="13.5" '
            'font-weight="700" fill="#E8D3A0">DGI</text></svg>')

# Hand-drawn line icons, 64x64 viewBox, stroke/fill via currentColor so each
# call site sets its own colour context. No stock photography is used on this
# build — see the note in gallery.html for why.
ICONS = {
    "stethoscope": (
        '<path d="M20 14v10c0 6 5 9 12 9s12-3 12-9V14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'
        '<line x1="32" y1="33" x2="32" y2="40" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'
        '<circle cx="32" cy="46" r="6" fill="none" stroke="currentColor" stroke-width="2.2"/>'
        '<circle cx="32" cy="46" r="2" fill="currentColor"/>'
        '<circle cx="20" cy="13" r="2" fill="currentColor"/><circle cx="44" cy="13" r="2" fill="currentColor"/>'),
    "microscope": (
        '<rect x="20" y="47" width="24" height="4" rx="2" fill="currentColor"/>'
        '<path d="M32 47V38" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
        '<path d="M32 38c0-10 4-14 10-16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
        '<line x1="41" y1="23" x2="45" y2="17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
        '<circle cx="46" cy="15" r="2.4" fill="currentColor"/>'
        '<line x1="21" y1="38" x2="41" y2="38" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
        '<circle cx="31" cy="38" r="3" fill="none" stroke="currentColor" stroke-width="1.6"/>'),
    "ot": (
        '<path d="M32 13l15 5.5v11.5c0 11.5-6.5 18.5-15 22-8.5-3.5-15-10.5-15-22V18.5z" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<line x1="32" y1="25" x2="32" y2="41" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
        '<line x1="24" y1="33" x2="40" y2="33" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'),
    "eye": (
        '<path d="M12 32C18 21 26 17 32 17s14 4 20 15c-6 11-14 15-20 15s-14-4-20-15z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>'
        '<circle cx="32" cy="32" r="7.5" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<circle cx="32" cy="32" r="3" fill="currentColor"/>'),
    "book": (
        '<path d="M32 18c-4-3-11-4-16-3v28c5-1 12 0 16 3 4-3 11-4 16-3V15c-5-1-12 0-16 3z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'
        '<line x1="32" y1="18" x2="32" y2="46" stroke="currentColor" stroke-width="1.6"/>'),
    "cap": (
        '<path d="M32 16L10 26l22 10 22-10z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'
        '<path d="M19 30v9c0 3 6 6 13 6s13-3 13-6v-9" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<line x1="48" y1="27" x2="48" y2="40" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'),
    "star": (
        '<path d="M32 14l5.6 12.2L50 28l-9 8.8L43.2 50 32 43.4 20.8 50 23 36.8 14 28l12.4-1.8z" '
        'fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'),
    "medal": (
        '<circle cx="32" cy="36" r="12" fill="none" stroke="currentColor" stroke-width="2.2"/>'
        '<circle cx="32" cy="36" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
        '<path d="M24 26L17 12l9 3 4-8 4 8 9-3-7 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'),
    "camera": (
        '<rect x="12" y="22" width="40" height="26" rx="3" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<path d="M24 22l3-5h10l3 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'
        '<circle cx="32" cy="35" r="8" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<circle cx="45" cy="27" r="1.6" fill="currentColor"/>'),
}


def medallion(key, size=64, ring=True):
    """A solid navy medallion carrying a line icon — the same seal language as
    the BSS emblem, used to mark each course rather than a stock photograph."""
    stroke = 'stroke="var(--brass)" stroke-width="1.3"' if ring else 'stroke="none"'
    dashed = ('<circle cx="32" cy="32" r="25.5" fill="none" stroke="rgba(201,162,78,.35)" '
              'stroke-width=".7" stroke-dasharray="2 3"/>') if ring else ""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-hidden="true" '
            f'style="flex:0 0 auto;">'
            f'<circle cx="32" cy="32" r="30" fill="var(--navy)" {stroke}/>{dashed}'
            f'<g style="color:#E8D3A0;">{ICONS[key]}</g></svg>')


def photo_img(name, alt, kind, cap, tall=False):
    """A real photograph from the institute's archive (extracted from the
    printed prospectus). `name` is the file stem in assets/img/."""
    cls = "photo photo-real photo-tall" if tall else "photo photo-real"
    return (f'<figure class="{cls}">'
            f'<img src="assets/img/{name}.jpg" alt="{alt}" loading="lazy" decoding="async">'
            f'<figcaption><b>{kind}</b>{cap}</figcaption></figure>')


def ghost_icon(key, size=44):
    """A faint watermark icon centred in a placeholder photo panel — signals
    'a photograph belongs here' without pretending one already does."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-hidden="true" '
            f'style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);'
            f'color:rgba(255,255,255,.30);z-index:1;">{ICONS[key]}</svg>')


DISCLOSURE = (
    "<b>Important disclosures.</b> Placement assistance offered by the institute covers private hospitals, "
    "clinics and diagnostic laboratories only, and does not extend to appointments in Government hospitals. "
    "The Diploma in Patient Care (DPC) and Diploma in Patient Care Assistant (DPCA) have no affiliation with "
    "the Indian Nursing Council. Certificate courses for working technicians are non-stipendiary and are not "
    "covered by placement assistance. Stipend amounts are paid by the host nursing home, laboratory or clinic "
    "and may vary according to the student's work. Fees, instalment dates and refund terms are as stated in "
    "the printed prospectus, which forms the binding record."
)


def rupee(n):
    """Indian digit grouping: 68000 -> 68,000; 150000 -> 1,50,000."""
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


def nav_html(active):
    out = []
    for href, label in NAV:
        cls = ' class="on"' if href == active else ""
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n        ".join(out)


def shell(page_file, title, description, body, active=None, head_extra="", robots=""):
    active = active or page_file
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{head_extra}<title>{title}</title>
<meta name="description" content="{description}">
{robots}<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="assets/css/site.css?v={ASSET_VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="util">
  <div class="wrap">
    <div class="util-l">
      <a href="tel:{PHONE1}">{PHONE1_H}</a>
      <span class="sep">/</span>
      <a href="tel:{PHONE2}">{PHONE2_H}</a>
      <span class="sep">|</span>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    <div class="util-note">{ADDR_H}</div>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Dr. Gaikwad's Institute — home">
      <span class="mark">{MONOGRAM}</span>
      <span class="brand-txt">
        <span class="brand-name">Dr. Gaikwad's Institute<sup>&reg;</sup></span>
        <span class="brand-sub">Paramedical Training &middot; Dadar, Mumbai</span>
      </span>
    </a>
    <nav class="main" aria-label="Main">
        {nav_html(active)}
    </nav>
    <a class="btn btn-brass btn-sm" href="contact.html">Apply Now</a>
    <button class="nav-toggle" aria-label="Open menu">Menu</button>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
          <svg width="40" height="40" viewBox="0 0 46 46" role="img" aria-label="Institute monogram">
            <circle cx="23" cy="23" r="21.2" fill="none" stroke="#C9A24E" stroke-width="1.4"/>
            <circle cx="23" cy="23" r="15.4" fill="rgba(255,255,255,.07)"/>
            <text x="23" y="28.4" text-anchor="middle" font-family="Georgia, serif" font-size="13.5"
                  font-weight="700" fill="#E8D3A0">DGI</text>
          </svg>
          <span style="font-family:var(--serif);font-size:17px;color:#E4EBF5;">Dr. Gaikwad's Institute<sup style="font-size:8px;color:#C9A24E;">&reg;</sup></span>
        </div>
        <p class="foot-addr">203 Akanksha, Opposite Plaza,<br>Dadar (West), Mumbai 400 028<br>Maharashtra, India</p>
        <p class="foot-addr" style="margin-top:14px;">
          <a href="tel:{PHONE1}">{PHONE1_H}</a><br>
          <a href="tel:{PHONE2}">{PHONE2_H}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </p>
      </div>
      <div>
        <h5>Diploma Courses</h5>
        <ul>
          <li><a href="course-patient-care.html">Patient Care (DPC / DPCA)</a></li>
          <li><a href="course-medical-lab-technology.html">Medical Lab Technology (DMLT)</a></li>
          <li><a href="course-operation-theatre.html">Operation Theatre (DOTT)</a></li>
          <li><a href="course-optometry.html">Optometry (DOPTO)</a></li>
          <li><a href="certificate-courses.html">Certificate Courses</a></li>
          <li><a href="bvoc.html">B.Voc &amp; ADMLT</a></li>
        </ul>
      </div>
      <div>
        <h5>Institute</h5>
        <ul>
          <li><a href="about.html">About &amp; BSS Certification</a></li>
          <li><a href="fees.html">Fees &amp; Stipend</a></li>
          <li><a href="admissions.html">Admission Process</a></li>
          <li><a href="placements.html">Placements &amp; Postings</a></li>
          <li><a href="gallery.html">Gallery &amp; Campus Life</a></li>
          <li><a href="refund-policy.html">Refund Policy</a></li>
          <li><a href="contact.html">Contact &amp; Directions</a></li>
        </ul>
      </div>
      <div>
        <h5>Admissions Enquiry</h5>
        <p style="line-height:1.7;color:#A8BCD8;">Counselling hours are best confirmed by telephone before
          visiting. Parents and guardians are encouraged to attend.</p>
        <div style="display:flex;flex-direction:column;gap:10px;margin-top:18px;">
          <a class="btn btn-brass btn-sm" href="{WA}">WhatsApp Us</a>
          <a class="btn btn-on-dark btn-sm" href="tel:{PHONE1}">Call the Institute</a>
        </div>
      </div>
    </div>
    <div class="disclose">{DISCLOSURE}</div>
    <div class="foot-btm">
      <span>&copy; 2026 Dr. Gaikwad's Institute. All rights reserved.</span>
      <span>Certified by Bharat Sevak Samaj &middot; Dadar, Mumbai</span>
    </div>
  </div>
</footer>

<a class="wa" href="{WA}" aria-label="Chat with us on WhatsApp">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 20zm4.4-5.9c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5.2-.4v-.4l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.5.6 2.1.7 2.9.6a2.5 2.5 0 0 0 1.6-1.2 2 2 0 0 0 .1-1.2l-.4-.2z"/>
  </svg>
  Chat on WhatsApp
</a>

<script src="assets/js/site.js?v={ASSET_VER}"></script>
</body>
</html>
"""


def pagehead(crumbs, h1, dek, meta=None, icon=None):
    """crumbs: list of (label, href|None). meta: list of (value, label).
    icon: optional ICONS key, drawn as a large medallion beside the heading."""
    parts = []
    for i, (label, href) in enumerate(crumbs):
        if i:
            parts.append('<span class="sep">/</span>')
        parts.append(f'<a href="{href}">{label}</a>' if href else label)
    meta_html = ""
    if meta:
        cells = "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v, l in meta)
        meta_html = f'<div class="head-meta">{cells}</div>'
    heading = (f'<div style="display:flex;align-items:flex-start;gap:22px;">'
               f'{medallion(icon, 84)}<div><h1>{h1}</h1></div></div>' if icon else f'<h1>{h1}</h1>')
    return f"""<section class="pagehead">
  <div class="wrap">
    <div class="crumb">{''.join(parts)}</div>
    {heading}
    <p class="dek">{dek}</p>
    {meta_html}
  </div>
</section>"""


def cta_band(heading, copy):
    return f"""<section class="cta-band">
  <div class="wrap">
    <div class="cta-inner">
      <div>
        <span class="label" style="color:var(--brass-lt);">Admissions 2026&ndash;27</span>
        <h2 style="margin-top:14px;">{heading}</h2>
        <p>{copy}</p>
        <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;">
          <a class="btn btn-brass" href="{WA}">Message on WhatsApp</a>
          <a class="btn btn-on-dark" href="tel:{PHONE1}">Call {PHONE1_H}</a>
        </div>
      </div>
      <aside class="cta-box">
        <span class="label" style="color:var(--brass-lt);">Visit us</span>
        <div style="margin-top:16px;">
          <div class="cta-line"><span>Address</span><b>203 Akanksha, Opp. Plaza,<br>Dadar (W), Mumbai 400 028</b></div>
          <div class="cta-line"><span>Telephone</span><b>{PHONE1_H}</b></div>
          <div class="cta-line"><span>Alternate</span><b>{PHONE2_H}</b></div>
          <div class="cta-line"><span>Nearest station</span><b>Dadar</b></div>
        </div>
        <a class="btn btn-primary" style="width:100%;margin-top:20px;background:#F4F8FD;color:#0E2A4E;border-color:#F4F8FD;"
           href="prospectus.pdf">Download Prospectus (PDF)</a>
      </aside>
    </div>
  </div>
</section>"""


def course_table(link=True):
    rows = []
    for c in COURSES:
        name = (f'<a href="course-{c["slug"]}.html">{c["name"]}</a>' if link else c["name"])
        rows.append(f"""          <tr>
            <td>
              <div class="c-name">{name}</div>
              <span class="c-abbr">{c['abbr']}</span>
            </td>
            <td>{c['elig']}</td>
            <td class="num">4 + 20 months</td>
            <td class="money">&#8377;{rupee(c['fee'])}<small>&#8377;{rupee(c['adm'])} at admission</small></td>
            <td class="money">&#8377;70,000&ndash;75,000</td>
            <td><span class="tag g"><span class="dot"></span>Assured</span></td>
          </tr>""")
    return f"""<div class="tbl-wrap rise">
      <table class="reg">
        <thead>
          <tr>
            <th style="width:30%">Diploma</th><th>Eligibility</th><th>Duration</th>
            <th>Course Fee</th><th>Stipend (approx.)</th><th>Placement</th>
          </tr>
        </thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
    </div>"""


LADDER = """<div class="ladder rise">
      <div class="rung"><span class="label-q">Months 1&ndash;5</span><b>&#8377;2,000</b><span>per month</span></div>
      <div class="rung"><span class="label-q">Months 6&ndash;10</span><b>&#8377;3,000</b><span>per month</span></div>
      <div class="rung"><span class="label-q">Months 11&ndash;15</span><b>&#8377;4,000</b><span>per month</span></div>
      <div class="rung"><span class="label-q">Months 16&ndash;20</span><b>&#8377;5,000</b><span>per month</span></div>
    </div>"""

CERTS = ["Blood Banking", "Medical Lab Technician", "Nutrition", "Operation Theatre Technician",
         "Dietician", "X-Ray Technician", "Optometry", "ECG Technician",
         "Medical Records", "Hospital Management", "Ayurvedic Massage", "Ayurvedic Panchakarma"]

PAGES = {}

# ============================================================ HOME
PAGES["index.html"] = dict(
    title="Dr. Gaikwad's Institute — Paramedical Diplomas in Dadar, Mumbai",
    description="Two-year BSS-certified paramedical diplomas in Dadar, Mumbai — DMLT, Patient Care, "
                "Operation Theatre and Optometry. Hospital postings with a monthly stipend.",
    body=f"""<section class="hero">
  <div class="wrap">
    <div>
      <span class="hero-eyebrow">Admissions open &middot; 2026&ndash;27 batch</span>
      <h1>Train for a hospital job.<br><em>Earn while you train.</em></h1>
      <p class="hero-dek">Two-year paramedical diplomas in Dadar, certified by Bharat Sevak Samaj &mdash;
        a national development agency promoted by the Government of India since 1952. Full-time hospital and
        laboratory postings from the fifth month, with a monthly stipend that rises as you qualify.</p>
      <div class="hero-cta">
        <a class="btn btn-brass" href="courses.html">View Courses &amp; Fees</a>
        <a class="btn btn-on-dark" href="contact.html">Talk to a Counsellor</a>
      </div>
      <p class="hero-fine">Placement assistance covers private hospitals, clinics and diagnostic laboratories.
        It does not extend to Government hospital appointments. DPC &amp; DPCA are not affiliated to the
        Indian Nursing Council.</p>
    </div>
    <aside class="cred">
      <div class="cred-inner">
        <svg width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="Certification seal" style="margin:0 auto;display:block;">
          <circle cx="32" cy="32" r="30" fill="none" stroke="#C9A24E" stroke-width="1.2"/>
          <circle cx="32" cy="32" r="26" fill="none" stroke="#C9A24E" stroke-width=".7" stroke-dasharray="2 3"/>
          <circle cx="32" cy="32" r="21" fill="#0E2A4E"/>
          <text x="32" y="30" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#E8D3A0" font-weight="700">B.S.S</text>
          <text x="32" y="41" text-anchor="middle" font-family="Georgia, serif" font-size="7.5" fill="#B9C9E0">1952</text>
        </svg>
        <p class="label" style="margin-top:14px;">Certification Authority</p>
        <h3>Bharat Sevak Samaj</h3>
        <p>National Development Agency promoted by the Government of India. Founder President:
           Pandit Jawaharlal Nehru. Constitution approved unanimously by the Indian Parliament.</p>
        <div class="cred-rule"></div>
        <div class="cred-facts">
          <div class="cred-fact"><b>30</b><span>Years<br>Teaching</span></div>
          <div class="cred-fact"><b>10,000+</b><span>Students<br>Placed</span></div>
          <div class="cred-fact"><b>100%</b><span>Stipendiary<br>Diplomas</span></div>
        </div>
      </div>
    </aside>
  </div>
</section>

<div class="trust">
  <div class="wrap">
    <div class="trust-i"><b>4 + 20</b><span>Months &mdash; classroom training followed by full-time hospital posting</span></div>
    <div class="trust-i"><b>&#8377;70,000+</b><span>Typical total stipend earned over the two-year diploma</span></div>
    <div class="trust-i"><b>10th / 12th</b><span>Pass or fail &mdash; eligible to apply for the diploma courses</span></div>
    <div class="trust-i"><b>50%</b><span>Railway concession for students during classroom training</span></div>
  </div>
</div>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Programmes</span>
      <h2>Four stipendiary diplomas</h2>
      <p>Each runs four months of classroom training followed by twenty months of supervised posting in a
         Mumbai hospital, nursing home, laboratory or optician's practice.</p>
    </div>
    <div class="grid-4 rise">
      {''.join(f'''<article class="ccard">
        <div class="ccard-top">
          {medallion(c['icon'], 52)}
          <span class="c-abbr">{c['abbr']}</span>
          <h3>{c['short']}</h3>
        </div>
        <div class="ccard-body">
          <div class="row"><span>Eligibility</span><b style="font-family:var(--sans);font-weight:600;">{c['elig'].split(' pass')[0]}</b></div>
          <div class="row"><span>Duration</span><b>4 + 20 mo</b></div>
          <div class="row"><span>Course fee</span><b>&#8377;{rupee(c['fee'])}</b></div>
          <div class="row"><span>Stipend</span><b>&#8377;70&ndash;75k</b></div>
          <div class="ccard-foot">
            <a class="btn btn-ghost btn-sm" style="width:100%;" href="course-{c['slug']}.html">Course details</a>
          </div>
        </div>
      </article>''' for c in COURSES)}
    </div>
    <div class="grid-2 rise" style="margin-top:22px;">
      <div class="card">
        <span class="label">For working technicians</span>
        <h4>One-year certificate courses</h4>
        <p>Twelve programmes for in-service candidates with three or more years of experience. Study alongside
           your job; direct examination available for experienced candidates.</p>
        <a class="card-link" href="certificate-courses.html">See all twelve courses &rarr;</a>
      </div>
      <div class="card">
        <span class="label">Degree pathway</span>
        <h4>B.Voc &amp; Advanced Diploma</h4>
        <p>Graduates of our two-year diplomas can enter a Bachelor of Vocation by lateral entry, or take the
           Advanced Diploma in Medical Laboratory Technology.</p>
        <a class="card-link" href="bvoc.html">See the degree pathway &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Fees &amp; Stipend</span>
      <h2>Most of the fee comes back as stipend.</h2>
      <p>Families rightly ask what a two-year diploma really costs. Here is the arithmetic in full, using the
         Diploma in Medical Laboratory Technology as the worked example &mdash; nothing withheld for a
         counselling call.</p>
    </div>
    <div class="math rise">
      <div class="math-col">
        <h4>What you pay &mdash; D.M.L.T.</h4>
        <div class="math-row"><span>Admission instalment</span><b>&#8377;14,000</b></div>
        <div class="math-row"><span>First three monthly instalments</span><b>&#8377;24,000</b></div>
        <div class="math-row"><span>Balance, staged to April 2028</span><b>&#8377;30,000</b></div>
        <div class="math-total"><span>Total course fee</span><b>&#8377;68,000</b></div>
        <p class="math-note">Inclusive of textbooks, workbooks, notes, equipment, examination fee,
           registration and identity card.</p>
      </div>
      <div class="math-col">
        <h4>What you earn back</h4>
        <div class="math-row"><span>Months 1&ndash;5 &mdash; &#8377;2,000/month</span><b>&#8377;10,000</b></div>
        <div class="math-row"><span>Months 6&ndash;10 &mdash; &#8377;3,000/month</span><b>&#8377;15,000</b></div>
        <div class="math-row"><span>Months 11&ndash;15 &mdash; &#8377;4,000/month</span><b>&#8377;20,000</b></div>
        <div class="math-row"><span>Months 16&ndash;20 &mdash; &#8377;5,000/month</span><b>&#8377;25,000</b></div>
        <div class="math-total"><span>Typical stipend earned</span><b class="pos">&#8377;70,000</b></div>
        <p class="math-note">Paid by the nursing home, laboratory or clinic where you are posted, and may vary
           according to your work.</p>
      </div>
    </div>
    <div style="margin-top:26px;">
      <a class="btn btn-primary" href="fees.html">Full fee schedule for every course</a>
    </div>
  </div>
</section>

<section class="band ink">
  <div class="wrap">
    <div class="bss">
      <div>
        <svg width="180" height="180" viewBox="0 0 180 180" role="img" aria-label="Bharat Sevak Samaj certification emblem" style="display:block;">
          <circle cx="90" cy="90" r="86" fill="none" stroke="#C9A24E" stroke-width="1.4"/>
          <circle cx="90" cy="90" r="78" fill="none" stroke="rgba(201,162,78,.5)" stroke-width=".8" stroke-dasharray="3 4"/>
          <circle cx="90" cy="90" r="68" fill="rgba(255,255,255,.05)" stroke="rgba(201,162,78,.7)" stroke-width="1"/>
          <circle cx="90" cy="90" r="54" fill="none" stroke="rgba(201,162,78,.35)" stroke-width=".8"/>
          <text x="90" y="76" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#E8D3A0" font-weight="700">B.S.S</text>
          <line x1="60" y1="86" x2="120" y2="86" stroke="#C9A24E" stroke-width=".8"/>
          <text x="90" y="104" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">NATIONAL</text>
          <text x="90" y="117" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">DEVELOPMENT</text>
          <text x="90" y="130" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">AGENCY</text>
          <text x="90" y="150" text-anchor="middle" font-family="Georgia, serif" font-size="13" fill="#E8D3A0" font-weight="700">1952</text>
        </svg>
      </div>
      <div class="bss-copy">
        <span class="label">The certification behind your diploma</span>
        <h2 style="font-size:clamp(25px,2.9vw,33px);line-height:1.15;margin:14px 0 18px;">A credential with a constitutional record.</h2>
        <p>Bharat Sevak Samaj is a national development agency promoted by the Government of India in 1952 to
           secure public co-operation in implementing government plans. Pandit Jawaharlal Nehru was its founder
           President, and its constitution and functioning were approved unanimously by the Indian Parliament.</p>
        <p>Every diploma awarded at this institute is issued under that certification.</p>
        <div style="display:flex;gap:12px;margin-top:26px;flex-wrap:wrap;">
          <a class="btn btn-brass" href="about.html">About the Institute</a>
          <a class="btn btn-on-dark" href="placements.html">See Our Placements</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Admissions</span>
      <h2>How to join</h2>
      <p>Four steps from first enquiry to your first day of classroom training. Our counsellors confirm your
         eligibility before you pay anything.</p>
    </div>
    <div class="steps rise">
      <div class="step"><span class="n">STEP 01</span><h4>Enquire</h4>
        <p>Call or message us on WhatsApp with your name, the course you are considering, and your last
           examination result. We reply the same working day.</p></div>
      <div class="step"><span class="n">STEP 02</span><h4>Counselling</h4>
        <p>Meet us at Dadar with a parent or guardian. We explain the course, the posting system and the full
           fee and stipend schedule before you commit.</p></div>
      <div class="step"><span class="n">STEP 03</span><h4>Submit documents</h4>
        <p>Mark sheets, Aadhaar, leaving certificate, domicile, medical fitness certificate and photographs.</p></div>
      <div class="step"><span class="n">STEP 04</span><h4>Confirm admission</h4>
        <p>Pay the first instalment to reserve your seat. Hospital posting follows in the fifth month.</p></div>
    </div>
    <div style="margin-top:34px;">
      <a class="btn btn-primary" href="admissions.html">Full admission process &amp; document checklist</a>
    </div>
  </div>
</section>

{cta_band("Seats are limited, and the batch fills before September.",
          "Speak to a counsellor about which diploma fits your marks, your budget and the hospital you want to "
          "work in. Bring a parent or guardian &mdash; we would rather answer every question now than after you "
          "have paid.")}""")

# ============================================================ ABOUT
PAGES["about.html"] = dict(
    title="About the Institute & BSS Certification — Dr. Gaikwad's Institute",
    description="Three decades of paramedical training in Dadar, Mumbai, certified by Bharat Sevak Samaj — "
                "a national development agency promoted by the Government of India since 1952.",
    body=f"""{pagehead([("Home","index.html"),("About &amp; BSS",None)],
    "Three decades of training technicians for Mumbai's hospitals.",
    "We are a paramedical training institute in Dadar West. We teach four stipendiary diplomas, place our "
    "graduates in private hospitals, laboratories and clinics across the city, and certify them under Bharat "
    "Sevak Samaj.",
    [("30","Years teaching"),("10,000+","Students placed"),("1952","BSS established")])}

<section class="band">
  <div class="wrap">
    <div class="split">
      <div class="prose rise">
        <span class="label">Who we are</span>
        <h2 style="font-size:clamp(24px,2.8vw,32px);margin:14px 0 20px;">An institute built around the posting, not the classroom.</h2>
        <p>Most paramedical courses in Mumbai teach theory and leave the student to find work afterwards. We
           built ours the other way round. Four months of classroom training establish the fundamentals; the
           remaining twenty months are spent on a full-time posting in a working nursing home, diagnostic
           laboratory, operation theatre or optician's practice, under a practising doctor.</p>
        <p>That posting is where the diploma stops being theoretical. It is also where most of our placements
           originate &mdash; the laboratory or nursing home that trains a student for twenty months is very
           often the one that hires them.</p>

        <h3>What we expect</h3>
        <p>We are a strict institute, and we say so plainly. Ninety per cent attendance is compulsory. Uniforms
           are required on duty. Night duty is part of the Patient Care course, and laboratory students work
           two shifts. Students who cannot commit to this will not do well here, and we would rather say that
           at the counselling stage than after a fee has been paid.</p>

        <h3>What we do not claim</h3>
        <p>Our placement assistance covers private hospitals, clinics and diagnostic laboratories. It does not
           extend to Government hospital appointments, and we will not suggest otherwise. The Diploma in
           Patient Care and Diploma in Patient Care Assistant have no affiliation with the Indian Nursing
           Council. Our certificate courses for working technicians carry neither stipend nor placement
           assistance.</p>

        <div class="callout">
          <span class="tag-l">Before you enrol</span>
          <p>Ask us for the fee schedule, the refund rules and the posting terms in writing at your first
             visit. We give them to every family as a printed prospectus, and everything in it is also
             published on this website.</p>
        </div>
      </div>

      <aside class="side-card rise">
        <span class="label">At a glance</span>
        <h4>Dr. Gaikwad's Institute</h4>
        <div class="row"><span>Location</span><b style="font-family:var(--sans);font-weight:600;">Dadar (W)</b></div>
        <div class="row"><span>Certification</span><b style="font-family:var(--sans);font-weight:600;">B.S.S.</b></div>
        <div class="row"><span>Diploma courses</span><b>4</b></div>
        <div class="row"><span>Certificate courses</span><b>12</b></div>
        <div class="row"><span>Diploma duration</span><b>4 + 20 mo</b></div>
        <div class="row"><span>Posting radius</span><b style="font-family:var(--sans);font-weight:600;">Virar&ndash;Kalyan&ndash;Chembur</b></div>
        <a class="btn btn-brass" href="contact.html">Arrange a visit</a>
        <a class="btn btn-ghost" href="courses.html">Browse courses</a>
      </aside>
    </div>
  </div>
</section>

<section class="band ink">
  <div class="wrap">
    <div class="bss">
      <div>
        <svg width="180" height="180" viewBox="0 0 180 180" role="img" aria-label="Bharat Sevak Samaj certification emblem" style="display:block;">
          <circle cx="90" cy="90" r="86" fill="none" stroke="#C9A24E" stroke-width="1.4"/>
          <circle cx="90" cy="90" r="78" fill="none" stroke="rgba(201,162,78,.5)" stroke-width=".8" stroke-dasharray="3 4"/>
          <circle cx="90" cy="90" r="68" fill="rgba(255,255,255,.05)" stroke="rgba(201,162,78,.7)" stroke-width="1"/>
          <text x="90" y="76" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#E8D3A0" font-weight="700">B.S.S</text>
          <line x1="60" y1="86" x2="120" y2="86" stroke="#C9A24E" stroke-width=".8"/>
          <text x="90" y="104" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">NATIONAL</text>
          <text x="90" y="117" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">DEVELOPMENT</text>
          <text x="90" y="130" text-anchor="middle" font-family="Georgia, serif" font-size="10.5" fill="#C4D3E8">AGENCY</text>
          <text x="90" y="150" text-anchor="middle" font-family="Georgia, serif" font-size="13" fill="#E8D3A0" font-weight="700">1952</text>
        </svg>
      </div>
      <div class="bss-copy">
        <span class="label">Certification</span>
        <h2 style="font-size:clamp(25px,2.9vw,33px);line-height:1.15;margin:14px 0 18px;">Bharat Sevak Samaj</h2>
        <p>B.S.S. is a national development agency promoted by the Government of India in 1952 to secure public
           co-operation in implementing government plans. Pandit Jawaharlal Nehru was its founder President.</p>
        <p>Its constitution and functioning were approved unanimously by the Indian Parliament &mdash; recorded
           in the First Five Year Plan, in the chapter on public co-operation in national development. Every
           diploma awarded at this institute is issued under that certification.</p>
      </div>
    </div>

    <div class="cert-block">
      <figure>
        <img src="assets/img/bss-certificate.jpg" loading="lazy" decoding="async"
             alt="Specimen Bharat Sevak Samaj diploma certificate awarded by the institute, with the holder's personal details redacted">
      </figure>
      <div>
        <span class="label">The certificate itself</span>
        <h3 style="font-size:24px;margin:12px 0 14px;">What you are awarded</h3>
        <p class="lede-c">A specimen of the certificate issued on successful completion, carrying the Bharat
           Sevak Samaj seal, your register number, the course and year, and the division obtained in theory
           and practicals. It is signed by the Director and by the Chairman of the Board of Examinations.</p>
        <p class="fine-c">Specimen shown for illustration. The holder's name, register number, photograph and
           QR code have been redacted from this scan. Certificates are collected within one month of
           convocation.</p>
      </div>
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">The institute</span>
      <h2>Our students on posting</h2>
      <p>Photographs from the institute's own archive, taken at the nursing homes, laboratories and clinics
         where our students train.</p>
    </div>
    <div class="grid-3 rise">
      {photo_img("posting-with-doctor-02", "Two students in uniform with a doctor at his practice",
                 "Our students", "Students with the doctor supervising their posting")}
      {photo_img("posting-examination", "Student examining a patient with a stethoscope",
                 "Our students", "Patient examination during a ward shift")}
      {photo_img("posting-equipment", "Student operating bedside equipment beside a patient and doctor",
                 "Our students", "Operating bedside equipment on posting")}
    </div>
  </div>
</section>

{cta_band("Come and see the institute before you decide.",
          "We would rather you visit, meet the staff and ask difficult questions than enrol on the strength of "
          "a website. Telephone first to confirm counselling hours.")}""")

# ============================================================ COURSES HUB
PAGES["courses.html"] = dict(
    title="Courses — Paramedical Diplomas & Certificates | Dr. Gaikwad's Institute",
    description="Four two-year stipendiary paramedical diplomas, twelve one-year certificate courses for "
                "working technicians, and a B.Voc degree pathway. Fees and eligibility in full.",
    body=f"""{pagehead([("Home","index.html"),("Courses",None)],
    "Every course we teach, with the fee printed.",
    "Three tracks: two-year stipendiary diplomas for school leavers, one-year certificates for technicians "
    "already in service, and a degree pathway for diploma holders who want to go further.",
    [("4","Diploma courses"),("12","Certificate courses"),("3","Degree pathways")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Track one</span>
      <h2>Two-year stipendiary diplomas</h2>
      <p>Four months of classroom training followed by twenty months of full-time supervised posting. These four
         courses carry a written stipend and placement assistance.</p>
    </div>
    {course_table()}
    <p style="margin-top:16px;font-size:13px;color:var(--muted);max-width:70ch;">
      Placement assistance covers private hospitals, clinics and diagnostic laboratories only. DPC and DPCA
      have no affiliation with the Indian Nursing Council. The X-Ray Technician course is open to male
      candidates only.</p>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Track two</span>
      <h2>One-year certificates for working technicians</h2>
      <p>For candidates already in service with three or more years of experience. Study alongside your job.
         These courses are non-stipendiary and are not covered by placement assistance.</p>
    </div>
    <div class="grid-4 rise">
      {''.join(f'''<div class="card"><span class="label">1 Year</span><h4 style="font-size:16px;">{n}</h4>
        <p style="font-size:13px;">&#8377;30,000 &mdash; payable as &#8377;6,000 + &#8377;3,000 &times; 8.</p></div>''' for n in CERTS)}
    </div>
    <div style="margin-top:26px;">
      <a class="btn btn-primary" href="certificate-courses.html">Eligibility and full details</a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Track three</span>
      <h2>Degree pathway</h2>
      <p>Diploma holders can continue to a Bachelor of Vocation by lateral entry, or take the Advanced Diploma
         in Medical Laboratory Technology.</p>
    </div>
    <div class="grid-3 rise">
      <div class="card"><span class="label">3 years &middot; 6 semesters</span><h4>B.Voc &mdash; regular entry</h4>
        <p>Medical Lab Technology or Patient Care Management. Eligibility: 12th pass with 60% or above.</p>
        <ul><li><span>Total fee</span><b>&#8377;1,50,000</b></li></ul></div>
      <div class="card"><span class="label">2 years &middot; 4 semesters</span><h4>B.Voc &mdash; lateral entry</h4>
        <p>For holders of a two-year BSS diploma. Enter directly in the third semester.</p>
        <ul><li><span>Total fee</span><b>&#8377;92,000</b></li></ul></div>
      <div class="card"><span class="label">1 year</span><h4>Advanced Diploma (ADMLT)</h4>
        <p>Advanced Diploma in Medical Laboratory Technology, after a BSS diploma.</p>
        <ul><li><span>Total fee</span><b>&#8377;40,000</b></li></ul></div>
    </div>
    <div style="margin-top:26px;">
      <a class="btn btn-primary" href="bvoc.html">About the degree pathway</a>
    </div>
  </div>
</section>

{cta_band("Not sure which course fits?",
          "Tell a counsellor your last examination result and what you would like to do, and we will tell you "
          "honestly which of these courses you are eligible for.")}""")

# ============================================================ COURSE DETAIL PAGES
COURSE_DETAIL = {
    "patient-care": dict(
        dek="Trains you to care for admitted patients in nursing homes and hospitals — vital signs, ward "
            "procedure, patient hygiene, mobility, and assisting nursing and medical staff on duty.",
        learn=["Recording and charting vital signs — temperature, pulse, respiration, blood pressure",
               "Bed-making, patient positioning, hygiene and pressure-sore prevention",
               "Assisting with feeding, mobility and personal care of admitted patients",
               "Ward procedure, infection control and handling of medical waste",
               "Basic first aid, oxygen administration and emergency response",
               "Maintaining patient records and handing over between shifts"],
        careers=["Patient care assistant in a private nursing home or hospital",
                 "Ward assistant / ward attendant", "Home-care attendant for post-operative patients",
                 "Assistant in a day-care or dialysis unit"],
        note="Night duty is compulsory for this course. This diploma has no affiliation with the Indian "
             "Nursing Council, and does not qualify the holder as a registered nurse."),
    "medical-lab-technology": dict(
        dek="Trains you to run the routine tests a diagnostic laboratory depends on — haematology, "
            "biochemistry, microbiology and sample handling, on real equipment under a pathologist.",
        learn=["Blood collection (venepuncture), sample labelling, transport and storage",
               "Haematology — haemoglobin, cell counts, ESR, blood grouping and cross-matching",
               "Clinical biochemistry — blood sugar, lipid profile, liver and kidney function tests",
               "Microbiology — staining, culture technique, and basic identification",
               "Urine, stool and body-fluid analysis",
               "Laboratory safety, quality control, reagent preparation and equipment maintenance"],
        careers=["Laboratory technician in a diagnostic centre or pathology laboratory",
                 "Phlebotomist / sample collection technician", "Hospital laboratory assistant",
                 "Blood bank technician (with the additional certificate)"],
        note="This is our most subscribed course, and requires 12th pass or fail. Students are expected to "
             "work in two shifts or on break duty during the posting."),
    "operation-theatre": dict(
        dek="Trains you to prepare and run an operation theatre — sterilisation, instrument handling, "
            "theatre discipline and assisting the surgical team during procedures.",
        learn=["Sterilisation technique, autoclaving and maintaining the sterile field",
               "Identification, handling and counting of surgical instruments",
               "Theatre preparation, positioning and draping of the patient",
               "Assisting the surgeon and anaesthetist during procedures",
               "Handling of specimens, sharps and biomedical waste",
               "Post-operative theatre cleaning and turnaround"],
        careers=["Operation theatre technician in a private hospital or nursing home",
                 "OT assistant in a day-surgery or maternity centre",
                 "CSSD (sterile supply) technician", "Endoscopy or minor-procedure room assistant"],
        note="Requires the ability to stand for extended periods and to work at short notice when emergency "
             "procedures are scheduled."),
    "optometry": dict(
        dek="Trains you to test vision and dispense spectacles — refraction, use of optical instruments, "
            "lens fitting and patient handling in an optician's practice or eye clinic.",
        learn=["Vision testing and refraction using trial lens sets and the retinoscope",
               "Use of the auto-refractometer, slit lamp and lensmeter",
               "Spectacle prescription reading, lens selection and frame fitting",
               "Contact lens basics, insertion, removal and hygiene counselling",
               "Recognising common eye conditions for referral to an ophthalmologist",
               "Shop practice — dispensing, edging, and patient follow-up"],
        careers=["Optometrist assistant / refractionist in an optician's practice",
                 "Vision technician in an eye hospital or clinic",
                 "Optical retail dispensing", "Assistant in a community eye-screening programme"],
        note="This is our lowest-fee diploma at ₹37,500. Postings are with opticians and eye clinics rather "
             "than general hospitals."),
}

for c in COURSES:
    d = COURSE_DETAIL[c["slug"]]
    others = "".join(
        f'<li style="display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px solid var(--rule);">'
        f'<a href="course-{o["slug"]}.html" style="color:var(--navy-mid);font-weight:600;font-size:13.5px;">{o["short"]}</a>'
        f'<b style="font-family:var(--mono);font-variant-numeric:tabular-nums;color:var(--ink);font-size:13px;">&#8377;{rupee(o["fee"])}</b></li>'
        for o in COURSES if o["slug"] != c["slug"])
    monthly = 6000 if c["fee"] == 60000 else (8000 if c["fee"] == 68000 else 1500)
    PAGES[f"course-{c['slug']}.html"] = dict(
        title=f"{c['name']} ({c['abbr'].replace(' · ', ' / ')}) — Dr. Gaikwad's Institute",
        description=f"{c['name']} in Dadar, Mumbai. {c['elig'].capitalize()}. 4 + 20 months, "
                    f"fee ₹{rupee(c['fee'])}, with a monthly stipend and placement assistance.",
        active="courses.html",
        body=f"""{pagehead([("Home","index.html"),("Courses","courses.html"),(c['short'],None)],
        c['name'], d['dek'],
        [(c['elig'].split(' pass')[0], "Eligibility"),("4 + 20", "Months"),
         (f"&#8377;{rupee(c['fee'])}", "Course fee"),("&#8377;70&ndash;75k", "Typical stipend")],
        icon=c['icon'])}

<section class="band">
  <div class="wrap">
    <div class="split">
      <div class="rise">
        <div class="prose">
          <span class="label">The course</span>
          <h2 style="font-size:clamp(23px,2.6vw,30px);margin:14px 0 18px;">What you will learn</h2>
          <ul>{''.join(f'<li>{x}</li>' for x in d['learn'])}</ul>

          <h3>How the two years run</h3>
          <p>The first four months are classroom training at our Dadar premises, with a compulsory test after
             every chapter that counts towards your internal assessment. From the fifth month you move to a
             full-time posting in a working {'laboratory' if c['slug']=='medical-lab-technology' else ('nursing home or hospital' if c['slug']=='patient-care' else ('hospital operation theatre' if c['slug']=='operation-theatre' else "optician's practice or eye clinic"))},
             where you work under a practising doctor and draw a monthly stipend.</p>

          <h3>Where graduates work</h3>
          <ul>{''.join(f'<li>{x}</li>' for x in d['careers'])}</ul>

          <div class="callout">
            <span class="tag-l">Please note</span>
            <p>{d['note']}</p>
          </div>

          <h3>The fee, and what comes back</h3>
          <p>The course fee is &#8377;{rupee(c['fee'])}, inclusive of textbooks, workbooks, notes, equipment,
             examination fee, registration and identity card. &#8377;{rupee(c['adm'])} is payable at admission;
             the balance is staged in instalments, and once your posting begins the monthly instalment is
             deducted from your stipend and remitted to the institute directly by the doctor.</p>
        </div>

        <div style="margin-top:30px;">
          <span class="label">Stipend ladder</span>
          <h3 style="font-size:20px;margin:12px 0 0;">Your monthly stipend rises as you qualify</h3>
        </div>
        {LADDER}
        <p style="margin-top:14px;font-size:13px;color:var(--muted);max-width:66ch;">
          Stipend is paid by the host {'laboratory' if c['slug']=='medical-lab-technology' else 'nursing home, laboratory or clinic'}
          and may vary above or below these figures according to your work. Uniform and apron are purchased by
          the student, and entry to duty is refused without them.</p>
      </div>

      <aside class="side-card rise">
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
          {medallion(c['icon'], 56)}
          <div><span class="label">{c['abbr']}</span><h4 style="margin:4px 0 0;">{c['short']}</h4></div>
        </div>
        <div class="row"><span>Eligibility</span><b style="font-family:var(--sans);font-weight:600;">{c['elig']}</b></div>
        <div class="row"><span>Duration</span><b>4 + 20 months</b></div>
        <div class="row"><span>Course fee</span><b>&#8377;{rupee(c['fee'])}</b></div>
        <div class="row"><span>At admission</span><b>&#8377;{rupee(c['adm'])}</b></div>
        <div class="row"><span>Then monthly</span><b>&#8377;{rupee(monthly)}</b></div>
        <div class="row"><span>Stipend</span><b>&#8377;70,000&ndash;75,000</b></div>
        <div class="row"><span>Placement</span><b style="font-family:var(--sans);font-weight:600;color:var(--green);">Assured</b></div>
        <a class="btn btn-brass" href="{WA}">Ask about this course</a>
        <a class="btn btn-ghost" href="admissions.html">How to apply</a>

        <div style="margin-top:24px;padding-top:20px;border-top:1px solid var(--rule);">
          <span class="label">Other diplomas</span>
          <ul style="list-style:none;padding:0;margin:12px 0 0;">{others}</ul>
        </div>
      </aside>
    </div>
  </div>
</section>

{cta_band(f"Apply for the {c['short']} diploma.",
          "Message us with your last examination result and we will confirm your eligibility the same working "
          "day. Counselling is free, and we will show you the full fee and refund terms before you pay.")}""")

# ============================================================ CERTIFICATE COURSES
cert_rows = "".join(f"""          <tr>
            <td><div class="c-name">Certificate / Diploma in {n}</div></td>
            <td>{'12th pass' if n == 'Nutrition' else '10th pass'}</td>
            <td class="num">1 year</td>
            <td class="money">&#8377;30,000<small>&#8377;6,000 + &#8377;3,000 &times; 8</small></td>
            <td><span class="tag n">Non-stipendiary</span></td>
          </tr>""" for n in CERTS)

PAGES["certificate-courses.html"] = dict(
    title="One-Year Certificate Courses for Working Technicians — Dr. Gaikwad's Institute",
    description="Twelve one-year certificate and diploma courses for in-service technicians with three or "
                "more years of experience. ₹30,000 each, payable in instalments.",
    active="courses.html",
    body=f"""{pagehead([("Home","index.html"),("Courses","courses.html"),("Certificate Courses",None)],
    "One-year certificates for technicians already in service.",
    "Twelve programmes for candidates with three or more years of work experience who want a formal "
    "qualification without leaving their job. Direct examination is available for experienced candidates.",
    [("12","Courses"),("1","Year each"),("&#8377;30,000","Fee each")])}

<section class="band">
  <div class="wrap">
    <div class="callout rise" style="max-width:none;margin-top:0;">
      <span class="tag-l">Before you read further</span>
      <p>These courses are <b>non-stipendiary</b> and are <b>not covered by placement assistance</b>. They are
         designed as a formal qualification for people already working in a hospital, laboratory or clinic.
         If you are a school leaver looking to start a career with a stipend and placement,
         see the <a href="courses.html" style="color:var(--navy-mid);font-weight:700;">two-year diploma courses</a> instead.</p>
    </div>

    <div class="tbl-wrap rise" style="margin-top:30px;">
      <table class="reg">
        <thead><tr><th style="width:36%">Certificate / Diploma</th><th>Eligibility</th><th>Duration</th>
          <th>Fee &amp; instalments</th><th>Stipend</th></tr></thead>
        <tbody>
{cert_rows}
        </tbody>
      </table>
    </div>

    <div class="grid-3 rise" style="margin-top:30px;">
      <div class="card"><span class="label">Requirement</span><h4>Three years in service</h4>
        <p>All twelve courses are for in-service candidates with a minimum of three years of relevant work
           experience. Bring evidence of employment to your counselling visit.</p></div>
      <div class="card"><span class="label">Flexibility</span><h4>Study alongside your job</h4>
        <p>Teaching is arranged so that working technicians can attend without leaving employment. Direct
           examination is available for suitably experienced candidates.</p></div>
      <div class="card"><span class="label">Payment</span><h4>&#8377;6,000 then &#8377;3,000 &times; 8</h4>
        <p>&#8377;6,000 at admission followed by eight monthly instalments of &#8377;3,000. Late instalments
           attract the standard penalty set out in the prospectus.</p></div>
    </div>
  </div>
</section>

{cta_band("Already working, and want the qualification on paper?",
          "Tell us your current role and how long you have been in it, and we will confirm which of the twelve "
          "certificates you are eligible for.")}""")

# ============================================================ B.VOC
PAGES["bvoc.html"] = dict(
    title="B.Voc Degree & Advanced Diploma (ADMLT) — Dr. Gaikwad's Institute",
    description="Bachelor of Vocation in Medical Lab Technology or Patient Care Management, with lateral "
                "entry for BSS diploma holders, plus the one-year Advanced Diploma (ADMLT).",
    active="courses.html",
    body=f"""{pagehead([("Home","index.html"),("Courses","courses.html"),("B.Voc &amp; ADMLT",None)],
    "From diploma to degree.",
    "A Bachelor of Vocation under the UGC B.Voc scheme, offered in association with Shri Venkateshwara "
    "University. Holders of our two-year diploma enter laterally and finish the degree in two years instead "
    "of three.",
    [("3 yrs","Regular entry"),("2 yrs","Lateral entry"),("1 yr","Advanced Diploma")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Degree programmes</span>
      <h2>Bachelor of Vocation (B.Voc)</h2>
      <p>The UGC Bachelor of Vocation scheme is a skills-based undergraduate degree with multiple entry and
         exit points, mapped to industry job roles under the National Skills Qualification Framework.</p>
    </div>

    <div class="tbl-wrap rise">
      <table class="reg">
        <thead><tr><th style="width:32%">Programme</th><th>Eligibility</th><th>Duration</th>
          <th>Total fee</th><th>Payment</th></tr></thead>
        <tbody>
          <tr><td><div class="c-name">B.Voc in Medical Lab Technology</div><span class="c-abbr">REGULAR ENTRY</span></td>
            <td>12th pass (60% and above)</td><td class="num">3 years &middot; 6 sem.</td>
            <td class="money">&#8377;1,50,000</td>
            <td class="money">&#8377;12,000<small>then 30 &times; &#8377;4,600</small></td></tr>
          <tr><td><div class="c-name">B.Voc in Patient Care Management</div><span class="c-abbr">REGULAR ENTRY</span></td>
            <td>12th pass (60% and above)</td><td class="num">3 years &middot; 6 sem.</td>
            <td class="money">&#8377;1,50,000</td>
            <td class="money">&#8377;12,000<small>then 30 &times; &#8377;4,600</small></td></tr>
          <tr><td><div class="c-name">B.Voc in Medical Lab Technology</div><span class="c-abbr">LATERAL ENTRY</span></td>
            <td>12th pass + BSS diploma</td><td class="num">2 years &middot; 4 sem.</td>
            <td class="money">&#8377;92,000</td>
            <td class="money">&#8377;12,000<small>then 20 &times; &#8377;4,000</small></td></tr>
          <tr><td><div class="c-name">B.Voc in Patient Care Management</div><span class="c-abbr">LATERAL ENTRY</span></td>
            <td>12th pass + BSS diploma</td><td class="num">2 years &middot; 4 sem.</td>
            <td class="money">&#8377;92,000</td>
            <td class="money">&#8377;12,000<small>then 20 &times; &#8377;4,000</small></td></tr>
          <tr><td><div class="c-name">Advanced Diploma in Medical Laboratory Technology</div><span class="c-abbr">ADMLT</span></td>
            <td>12th pass + BSS diploma</td><td class="num">1 year</td>
            <td class="money">&#8377;40,000</td>
            <td class="money">&#8377;7,000<small>then 11 &times; &#8377;3,000</small></td></tr>
        </tbody>
      </table>
    </div>

    <div class="grid-2 rise" style="margin-top:30px;">
      <div class="card">
        <span class="label">Why lateral entry matters</span>
        <h4>Two years saved, and &#8377;58,000</h4>
        <p>A student who completes our two-year DMLT diploma and then enters the B.Voc laterally pays
           &#8377;92,000 for the degree instead of &#8377;1,50,000, and finishes in two years instead of three
           &mdash; while having earned a stipend throughout the diploma.</p>
      </div>
      <div class="card">
        <span class="label">Recommended route</span>
        <h4>12th Science pass students</h4>
        <p>Students who have passed 12th in the Science stream are advised to consider B.Voc or the Advanced
           Diploma directly. Speak to a counsellor about which is the better fit for your marks and your
           intended career.</p>
      </div>
    </div>

    <p style="margin-top:24px;font-size:13px;color:var(--muted);max-width:74ch;">
      Offered in association with Shri Venkateshwara University under the UGC Bachelor of Vocation scheme.
      Confirm current affiliation status and approvals with the institute at your counselling visit.</p>
  </div>
</section>

{cta_band("Ask about the degree pathway.",
          "Whether B.Voc, ADMLT or a two-year diploma first is the better route depends on your marks and how "
          "soon you need to be earning. A counsellor will walk you through both.")}""")

# ============================================================ FEES
PAGES["fees.html"] = dict(
    title="Fees & Stipend — Every Course, In Full | Dr. Gaikwad's Institute",
    description="Complete fee schedule for all diploma, certificate and degree courses at Dr. Gaikwad's "
                "Institute, with the stipend ladder, instalment dates and refund rules.",
    body=f"""{pagehead([("Home","index.html"),("Fees &amp; Stipend",None)],
    "The whole fee schedule, published.",
    "Every fee we charge, every instalment date, the stipend you can expect against it, and the refund terms "
    "if you leave. Nothing is held back for a counselling call.",
    [("&#8377;37,500","Lowest diploma fee"),("&#8377;68,000","Highest diploma fee"),("&#8377;70,000+","Typical stipend")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">The arithmetic</span>
      <h2>Most of the fee comes back as stipend.</h2>
      <p>Worked in full for the Diploma in Medical Laboratory Technology, our highest-fee course. The other
         diplomas follow the same pattern at a lower fee.</p>
    </div>
    <div class="math rise">
      <div class="math-col">
        <h4>What you pay &mdash; D.M.L.T.</h4>
        <div class="math-row"><span>Admission instalment</span><b>&#8377;14,000</b></div>
        <div class="math-row"><span>First three monthly instalments</span><b>&#8377;24,000</b></div>
        <div class="math-row"><span>Balance, staged to April 2028</span><b>&#8377;30,000</b></div>
        <div class="math-total"><span>Total course fee</span><b>&#8377;68,000</b></div>
        <p class="math-note">Inclusive of textbooks, workbooks, notes, equipment, examination fee,
           registration, identity card and record note fees.</p>
      </div>
      <div class="math-col">
        <h4>What you earn back</h4>
        <div class="math-row"><span>Months 1&ndash;5 &mdash; &#8377;2,000/month</span><b>&#8377;10,000</b></div>
        <div class="math-row"><span>Months 6&ndash;10 &mdash; &#8377;3,000/month</span><b>&#8377;15,000</b></div>
        <div class="math-row"><span>Months 11&ndash;15 &mdash; &#8377;4,000/month</span><b>&#8377;20,000</b></div>
        <div class="math-row"><span>Months 16&ndash;20 &mdash; &#8377;5,000/month</span><b>&#8377;25,000</b></div>
        <div class="math-total"><span>Typical stipend earned</span><b class="pos">&#8377;70,000</b></div>
        <p class="math-note">Paid by the host nursing home, laboratory or clinic, and may vary according to
           your work.</p>
      </div>
    </div>
    {LADDER}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Diploma courses</span>
      <h2>Fee schedule &mdash; two-year diplomas</h2>
    </div>
    {course_table()}

    <div class="sec-head rise" style="margin-top:54px;">
      <span class="label">Instalment dates</span>
      <h2 style="font-size:26px;">When each stage falls due</h2>
      <p>For the current admission cycle. Confirm the dates applicable to your batch at admission.</p>
    </div>
    <div class="tbl-wrap rise">
      <table class="reg" style="min-width:620px;">
        <thead><tr><th>Stage</th><th>Due by</th>
          <th>DPC / DPCA / DOTT / DOPTO</th><th>DMLT</th></tr></thead>
        <tbody>
          <tr><td>At admission</td><td>On the day</td><td class="money">&#8377;12,000</td><td class="money">&#8377;14,000</td></tr>
          <tr><td>Cumulative total</td><td>25 September 2026</td><td class="money">&#8377;30,000</td><td class="money">&#8377;38,000</td></tr>
          <tr><td>Cumulative total</td><td>1 March 2027</td><td class="money">&#8377;39,000</td><td class="money">&#8377;47,000</td></tr>
          <tr><td>Cumulative total</td><td>25 September 2027</td><td class="money">&#8377;49,500</td><td class="money">&#8377;57,500</td></tr>
          <tr><td>Full fee complete</td><td>1 April 2028</td><td class="money">&#8377;60,000</td><td class="money">&#8377;68,000</td></tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:14px;font-size:13px;color:var(--muted);max-width:74ch;">
      The first instalment is payable in cash. Once your posting begins, the monthly instalment is deducted
      from your stipend and remitted to the institute directly by the doctor. Instalments are due before the
      10th of each month; a 10% penalty applies to late instalments, and a student two instalments in arrears
      may not attend class. Convocation fee of &#8377;1,000 is payable in April 2028.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="grid-2 rise">
      <div class="card">
        <span class="label">Certificate courses</span>
        <h4>One year, for working technicians</h4>
        <ul>
          <li><span>All twelve certificate courses</span><b>&#8377;30,000</b></li>
          <li><span>At admission</span><b>&#8377;6,000</b></li>
          <li><span>Then eight monthly instalments</span><b>&#8377;3,000</b></li>
        </ul>
        <a class="card-link" href="certificate-courses.html">See the twelve courses &rarr;</a>
      </div>
      <div class="card">
        <span class="label">Degree pathway</span>
        <h4>B.Voc and Advanced Diploma</h4>
        <ul>
          <li><span>B.Voc &mdash; regular, 3 years</span><b>&#8377;1,50,000</b></li>
          <li><span>B.Voc &mdash; lateral entry, 2 years</span><b>&#8377;92,000</b></li>
          <li><span>ADMLT &mdash; 1 year</span><b>&#8377;40,000</b></li>
        </ul>
        <a class="card-link" href="bvoc.html">About the degree pathway &rarr;</a>
      </div>
    </div>

    <div class="sec-head rise" style="margin-top:54px;">
      <span class="label">Included in the fee</span>
      <h2 style="font-size:26px;">What you do not pay extra for</h2>
    </div>
    <div class="grid-4 rise">
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Textbooks &amp; workbooks</h4>
        <p style="font-size:13px;">Text books, notes, workbooks and equipment.</p></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Examination &amp; registration</h4>
        <p style="font-size:13px;">Registration, examination, record note and identity card fees.</p></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Computer &amp; English</h4>
        <p style="font-size:13px;">Computer course and English speaking course as per syllabus (courses 1&ndash;4).</p></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Campus life</h4>
        <p style="font-size:13px;">Sports day, Ganeshotsav, Republic Day, cultural events and competitions.</p></div>
    </div>
    <p style="margin-top:18px;font-size:13px;color:var(--muted);max-width:74ch;">
      Not included: uniform and apron, which are purchased by the student and are compulsory for duty; and the
      &#8377;2,000 examination and certificate fee for the supplementary DGI certificates awarded in the final year.</p>

    <div style="margin-top:34px;">
      <a class="btn btn-primary" href="refund-policy.html">Read the refund policy in full</a>
    </div>
  </div>
</section>

{cta_band("Want this in writing before you decide?",
          "Ask us for the printed prospectus. It carries the same fee schedule, instalment dates and refund "
          "rules published on this page, and it is the binding record.")}""")

# ============================================================ REFUND POLICY
PAGES["refund-policy.html"] = dict(
    title="Refund Policy — Dr. Gaikwad's Institute",
    description="Refund rules for all courses at Dr. Gaikwad's Institute: deduction slabs by date of "
                "withdrawal, application process and payment method.",
    active="fees.html",
    body=f"""{pagehead([("Home","index.html"),("Fees &amp; Stipend","fees.html"),("Refund Policy",None)],
    "Refund policy",
    "Our refund terms are strict, and we publish them so that no family is surprised by them later. Read this "
    "page before you pay the first instalment.")}

<section class="band">
  <div class="wrap">
    <div class="callout rise" style="max-width:none;margin-top:0;border-left-color:var(--clay);">
      <span class="tag-l" style="color:var(--clay);">The two rules that matter most</span>
      <p><b>No refund is given once one month has passed from the commencement of the course</b>, under any
         condition whatsoever. And <b>no refund is given at all where admission is taken after 25 September.</b>
         If either of these could apply to you, raise it with a counsellor before paying.</p>
    </div>

    <div class="tbl-wrap rise" style="margin-top:30px;">
      <table class="reg" style="min-width:680px;">
        <thead><tr><th style="width:34%">Course</th>
          <th>Withdrawal before<br>course commences</th>
          <th>Within 7 days of<br>commencement</th>
          <th>Within 1 month of<br>commencement</th></tr></thead>
        <tbody>
          <tr><td><div class="c-name">Patient Care / Patient Care Assistant</div><span class="c-abbr">TOTAL FEE &#8377;60,000</span></td>
            <td class="money">&#8377;3,000<small>5% deducted</small></td>
            <td class="money">&#8377;6,000<small>10% deducted</small></td>
            <td class="money">&#8377;15,000<small>25% deducted</small></td></tr>
          <tr><td><div class="c-name">Medical Laboratory Technology</div><span class="c-abbr">TOTAL FEE &#8377;68,000</span></td>
            <td class="money">&#8377;3,400<small>5% deducted</small></td>
            <td class="money">&#8377;6,800<small>10% deducted</small></td>
            <td class="money">&#8377;17,000<small>25% deducted</small></td></tr>
          <tr><td><div class="c-name">Operation Theatre / X-Ray / Optometry</div><span class="c-abbr">TOTAL FEE &#8377;60,000</span></td>
            <td class="money">&#8377;3,000<small>5% deducted</small></td>
            <td class="money">&#8377;6,000<small>10% deducted</small></td>
            <td class="money">&#8377;15,000<small>25% deducted</small></td></tr>
          <tr><td><div class="c-name">All other courses</div><span class="c-abbr">TOTAL FEE &#8377;20,000</span></td>
            <td class="money">&#8377;1,000<small>5% deducted</small></td>
            <td class="money">&#8377;2,000<small>10% deducted</small></td>
            <td class="money">&#8377;5,000<small>25% deducted</small></td></tr>
        </tbody>
      </table>
    </div>
    <p style="margin-top:14px;font-size:13px;color:var(--muted);max-width:74ch;">
      Figures shown are the amount <b>deducted</b> from the fee already paid. The remaining amount is returned
      by cheque.</p>

    <div class="split" style="margin-top:54px;">
      <div class="prose rise">
        <span class="label">Process</span>
        <h2 style="font-size:26px;margin:14px 0 18px;">How to claim a refund</h2>
        <ul>
          <li>Submit a written application to the institute.</li>
          <li>State clearly the name in whose favour the cheque should be drawn.</li>
          <li>The cheque is issued fifteen days after the application is received.</li>
          <li>All refunds are made by cheque only, sent by speed post at the student's cost.</li>
        </ul>
        <h3>Related charges</h3>
        <ul>
          <li>Change of course before the course begins: &#8377;500. After it begins: &#8377;1,000 per month.</li>
          <li>Failure to appear for the yearly final examination: 40% extra fee to re-register and re-examine.</li>
          <li>Late instalment: 10% penalty per month; 12% interest applies on late fees.</li>
          <li>Cheque returned unpaid by the bank: &#8377;500.</li>
        </ul>
      </div>
      <aside class="side-card rise">
        <span class="label">Need to discuss this?</span>
        <h4>Speak to us first</h4>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">If circumstances have changed and you are
          thinking of withdrawing, contact the institute before the deadline passes rather than after. The
          slabs above are date-based and cannot be applied retrospectively.</p>
        <a class="btn btn-brass" href="{WA}" style="margin-top:16px;">Message the institute</a>
        <a class="btn btn-ghost" href="tel:{PHONE1}">Call {PHONE1_H}</a>
      </aside>
    </div>
  </div>
</section>""")

# ============================================================ ADMISSIONS
PAGES["admissions.html"] = dict(
    title="Admissions — Process, Documents & Rules | Dr. Gaikwad's Institute",
    description="How to apply to Dr. Gaikwad's Institute: the four-step admission process, required "
                "documents, key dates and the institute rules you agree to on admission.",
    body=f"""{pagehead([("Home","index.html"),("Admissions",None)],
    "How to join the institute.",
    "Four steps, one document checklist, and a set of rules we ask you to read before you sign rather than "
    "after. Counselling is free and carries no obligation.",
    [("Same day","Enquiry response"),("25 Sept","Late admission cutoff"),("90%","Attendance required")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">The process</span>
      <h2>Four steps to admission</h2>
    </div>
    <div class="steps rise">
      <div class="step"><span class="n">STEP 01</span><h4>Enquire</h4>
        <p>Call or message us on WhatsApp with your name, the course you are considering, and your last
           examination result. We reply the same working day and tell you honestly whether you are eligible.</p></div>
      <div class="step"><span class="n">STEP 02</span><h4>Counselling</h4>
        <p>Meet us at Dadar with a parent or guardian. We explain the course, the posting system, the full fee
           and stipend schedule and the refund terms, and answer every question before you commit.</p></div>
      <div class="step"><span class="n">STEP 03</span><h4>Submit documents</h4>
        <p>Bring the checklist below. Photographs must be in white uniform or dress against a white
           background.</p></div>
      <div class="step"><span class="n">STEP 04</span><h4>Confirm admission</h4>
        <p>Pay the first instalment in cash to reserve your seat. Classroom training begins with your batch,
           and hospital posting follows in the fifth month.</p></div>
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="split">
      <div class="rise">
        <span class="label">Checklist</span>
        <h2 style="font-size:clamp(23px,2.6vw,30px);margin:14px 0 20px;">Documents required at admission</h2>
        <div class="tbl-wrap">
          <table class="reg" style="min-width:420px;">
            <thead><tr><th style="width:70%">Document</th><th>Copies</th></tr></thead>
            <tbody>
              <tr><td>10th / 12th mark sheet (photocopy)</td><td class="num">3</td></tr>
              <tr><td>Aadhaar card (photocopy)</td><td class="num">1</td></tr>
              <tr><td>Marriage certificate, if applicable (photocopy)</td><td class="num">3</td></tr>
              <tr><td>Caste certificate, if applicable (photocopy)</td><td class="num">2</td></tr>
              <tr><td>School / college leaving certificate</td><td class="num">2</td></tr>
              <tr><td>Domicile certificate</td><td class="num">1</td></tr>
              <tr><td>Medical fitness certificate</td><td class="num">1</td></tr>
              <tr><td>Colour photographs &mdash; white dress, white background</td><td class="num">10</td></tr>
            </tbody>
          </table>
        </div>
        <p style="margin-top:14px;font-size:13px;color:var(--muted);max-width:66ch;">
          Parents' signature on the admission form is not compulsory for students above 18 years, though we
          strongly encourage a parent or guardian to attend the counselling visit regardless.</p>
      </div>

      <aside class="side-card rise">
        <span class="label">Key dates</span>
        <h4>Admission cycle</h4>
        <div class="row"><span>Enquiries open</span><b style="font-family:var(--sans);font-weight:600;">Year round</b></div>
        <div class="row"><span>Main intake</span><b style="font-family:var(--sans);font-weight:600;">June&ndash;July</b></div>
        <div class="row"><span>Late admission cutoff</span><b style="font-family:var(--sans);font-weight:600;">25 September</b></div>
        <div class="row"><span>Posting begins</span><b style="font-family:var(--sans);font-weight:600;">Month 5</b></div>
        <div class="row"><span>Convocation</span><b style="font-family:var(--sans);font-weight:600;">Aug / Sept</b></div>
        <a class="btn btn-brass" href="{WA}">Start your enquiry</a>
        <a class="btn btn-ghost" href="fees.html">See the fee schedule</a>
      </aside>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Before you sign</span>
      <h2>The rules you are agreeing to</h2>
      <p>We are a strict institute and we would rather you knew that now. These are the terms every student
         and parent signs at admission, summarised.</p>
    </div>
    <div class="faq rise">
      <details><summary>What attendance is required?</summary>
        <p>Ninety per cent attendance is compulsory. Absence due to illness must be notified to the institute
           in writing. A student absent for more than eight days may be given a repeat, particularly where
           examination marks are poor.</p></details>
      <details><summary>What are the dress and conduct rules?</summary>
        <p>Indecent clothing, sleeveless tops, T-shirts, make-up, jewellery and excessive cash are not
           permitted. Uniform and apron are compulsory on duty and entry is refused without them. Mobile
           phones must be kept on vibrate in class and on posting &mdash; a &#8377;500 fine applies on first
           use, and confiscation on the second.</p></details>
      <details><summary>How are postings allocated?</summary>
        <p>We try to place you near your residence, and postings are available up to Virar, Kalyan and
           Chembur &mdash; but not in Navi Mumbai or beyond. You may arrange your own posting, for which a
           request letter is issued one month in advance; if you do, the institute is not responsible for the
           teaching or stipend at that posting. Once a posting has been allocated by the institute, changing to
           one of your own attracts a &#8377;5,000 posting fee.</p></details>
      <details><summary>What happens if there is a problem on posting?</summary>
        <p>Report it to the institute by email immediately and we will act on it; you will receive a reply by
           email. Leaving a posting without informing us in writing is treated as the student's fault and
           attracts a &#8377;5,000 posting fee before a new posting is allocated.</p></details>
      <details><summary>Who may contact the institute about a student?</summary>
        <p>Only the parent or guardian who signed the admission form. Contact by any other person attracts a
           &#8377;1,000 fine on the first occasion and &#8377;3,000 on the second. Please make appointments by
           email and bring your daily diary.</p></details>
      <details><summary>What are fines used for?</summary>
        <p>Fine collections are not used by the institute for itself. They fund student activities &mdash;
           snacks, saree day, colour day, Ganeshotsav, Dassehra, Diwali, New Year, sports day, Republic Day and
           competitions.</p></details>
      <details><summary>Can I take another course at the same time?</summary>
        <p>Only with written permission from the institute, obtained in advance.</p></details>
      <details><summary>When do I collect my certificate?</summary>
        <p>Within one month of convocation. After that the institute is not responsible for damage to the
           certificate, and a late fee of &#8377;500 per year applies.</p></details>
    </div>
  </div>
</section>

{cta_band("Ready to start your enquiry?",
          "Message us with your last examination result and the course you are considering. We will confirm "
          "your eligibility and arrange a counselling appointment.")}""")

# ============================================================ PLACEMENTS
PAGES["placements.html"] = dict(
    title="Placements & Hospital Postings — Dr. Gaikwad's Institute",
    description="Twenty months of supervised posting in Mumbai hospitals, nursing homes and laboratories, "
                "with placement assistance in private healthcare on completion.",
    body=f"""{pagehead([("Home","index.html"),("Placements",None)],
    "Trained on the floor, not only in the classroom.",
    "From the fifth month, students work full shifts under practising doctors in real nursing homes, "
    "laboratories and operation theatres. It is where the diploma stops being theoretical — and where most of "
    "our placements originate.",
    [("20","Months on posting"),("10,000+","Students placed"),("30","Years of practice")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">How the posting works</span>
      <h2>Twenty months inside a working practice</h2>
      <p>The posting is not an observership. Students work full duty &mdash; two shifts or break duty for
         laboratory students, night duty for patient care students &mdash; under the supervision of the doctor
         running the practice.</p>
    </div>
    <div class="grid-3 rise">
      {photo_img("posting-with-doctor-01", "Student in white uniform on posting alongside the supervising doctor",
                 "On posting", "A student with the doctor supervising her posting")}
      {photo_img("posting-venepuncture-01", "Student drawing a blood sample from a seated patient",
                 "On posting", "Drawing a blood sample under supervision")}
      {photo_img("posting-patient-monitoring", "Two students monitoring a patient's blood pressure at the bedside",
                 "On posting", "Bedside monitoring during a ward shift")}
      {photo_img("posting-consulting-room", "Student standing with a senior doctor in a consulting room",
                 "On posting", "In the consulting room of a partner practice")}
      {photo_img("posting-injection-prep", "Student preparing an injection while the supervising doctor observes",
                 "On posting", "Preparing an injection under a doctor's eye")}
      {photo_img("posting-with-doctor-03", "Student in uniform with the doctor at a partner clinic",
                 "On posting", "At a partner clinic in Mumbai")}
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="grid-3 rise">
      <div class="card"><span class="label">Where</span><h4>Across Mumbai</h4>
        <p>Nursing homes, diagnostic laboratories, clinics and opticians. We place you as near your residence
           as we can, up to Virar, Kalyan and Chembur. Postings are not available in Navi Mumbai or beyond.</p></div>
      <div class="card"><span class="label">Supervision</span><h4>Under a practising doctor</h4>
        <p>Parents are welcome to visit the posting with the student after 8:00 pm. We advise against a
           posting more than forty minutes' walk from the station.</p></div>
      <div class="card"><span class="label">On completion</span><h4>Placement assistance</h4>
        <p>Covers private hospitals, clinics and diagnostic laboratories. Very often the practice that trained
           a student for twenty months is the one that hires them.</p></div>
    </div>

    <div class="callout rise" style="max-width:none;margin-top:30px;">
      <span class="tag-l">Scope of our placement assistance</span>
      <p>Placement assistance applies to the four two-year diploma courses only, and covers private hospitals,
         clinics and diagnostic laboratories. <b>It does not extend to appointments in Government hospitals.</b>
         The twelve one-year certificate courses are non-stipendiary and carry no placement assistance.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">In their words</span>
      <h2>Students and parents</h2>
    </div>
    <div class="quotes rise">
      <div class="quote"><span class="qm">&ldquo;</span>
        <blockquote>I failed my 12th and thought that was the end of it. Two years later I was drawing a
          salary in a pathology lab in Mahim. The posting is what got me the job &mdash; the lab I trained at
          kept me on.</blockquote>
        <cite><b>Alumni testimonial &mdash; to be supplied</b>DMLT &middot; placed at a diagnostic laboratory, Mumbai</cite></div>
      <div class="quote"><span class="qm">&ldquo;</span>
        <blockquote>What convinced us as parents was that they showed us the fee schedule and the refund rules
          in writing on the first visit, before asking for a single rupee. Nobody else did that.</blockquote>
        <cite><b>Parent testimonial &mdash; to be supplied</b>Parent of a Patient Care diploma student</cite></div>
    </div>
  </div>
</section>

{cta_band("Ask us about placement before you enrol.",
          "Ask which practices our students are currently posted to, and what our recent graduates are doing "
          "now. We would rather answer that at counselling than have you take it on trust.")}""")

# ============================================================ CONTACT
PAGES["contact.html"] = dict(
    title="Contact & Directions — Dr. Gaikwad's Institute, Dadar West, Mumbai",
    description="Visit Dr. Gaikwad's Institute at 203 Akanksha, Opposite Plaza, Dadar West, Mumbai 400 028. "
                "Telephone, WhatsApp and admission enquiry form.",
    body=f"""{pagehead([("Home","index.html"),("Contact",None)],
    "Come and see us in Dadar.",
    "Telephone first to confirm counselling hours, then visit with a parent or guardian. We are a short walk "
    "from Dadar station, opposite Plaza.")}

<section class="band">
  <div class="wrap">
    <div class="split">
      <div class="rise">
        <span class="label">Admission enquiry</span>
        <h2 style="font-size:clamp(23px,2.6vw,30px);margin:14px 0 8px;">Send us your details</h2>
        <p style="color:var(--muted);margin-bottom:26px;max-width:60ch;">Tell us your last examination result
          and the course you are considering. A counsellor will reply the same working day and confirm whether
          you are eligible.</p>

        <form data-enquiry novalidate>
          <div class="form-grid">
            <div class="field"><label for="f-name">Student name</label>
              <input id="f-name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="f-phone">Mobile number</label>
              <input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
            <div class="field"><label for="f-email">Email address</label>
              <input id="f-email" name="email" type="email" autocomplete="email"></div>
            <div class="field"><label for="f-course">Course of interest</label>
              <select id="f-course" name="course">
                <option>Diploma in Patient Care (DPC / DPCA)</option>
                <option>Diploma in Medical Lab Technology (DMLT)</option>
                <option>Diploma in Operation Theatre Technician (DOTT)</option>
                <option>Diploma in Optometry (DOPTO)</option>
                <option>One-year certificate course</option>
                <option>B.Voc / Advanced Diploma</option>
                <option>Not sure &mdash; please advise</option>
              </select></div>
            <div class="field"><label for="f-qual">Last examination passed</label>
              <select id="f-qual" name="qualification">
                <option>10th &mdash; passed</option><option>10th &mdash; failed</option>
                <option>12th &mdash; passed</option><option>12th &mdash; failed</option>
                <option>Graduate</option><option>Currently working in healthcare</option>
              </select></div>
            <div class="field"><label for="f-area">Area of residence</label>
              <input id="f-area" name="area" type="text" placeholder="e.g. Kurla, Thane, Vasai"></div>
            <div class="field full"><label for="f-msg">Anything you would like to ask</label>
              <textarea id="f-msg" name="message"></textarea></div>
          </div>
          <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px;align-items:center;">
            <button class="btn btn-brass" type="submit">Send enquiry</button>
            <a class="btn btn-ghost" href="{WA}">Or message on WhatsApp</a>
          </div>
          <p class="form-note" data-form-status>We use your details only to respond to this enquiry.</p>
        </form>
      </div>

      <aside class="side-card rise">
        <span class="label">Visit the institute</span>
        <h4>Dadar (West)</h4>
        <p style="font-size:14.5px;line-height:1.7;color:var(--body);margin-bottom:16px;">
          203 Akanksha, Opposite Plaza,<br>Dadar (West), Mumbai 400 028,<br>Maharashtra, India</p>
        <div class="row"><span>Telephone</span><b>{PHONE1_H}</b></div>
        <div class="row"><span>Alternate</span><b>{PHONE2_H}</b></div>
        <div class="row"><span>Nearest station</span><b style="font-family:var(--sans);font-weight:600;">Dadar</b></div>
        <div class="row"><span>Email</span><b style="font-family:var(--sans);font-weight:600;font-size:12.5px;">{EMAIL}</b></div>
        <a class="btn btn-brass" href="{WA}">WhatsApp us</a>
        <a class="btn btn-ghost" href="tel:{PHONE1}">Call the institute</a>

        <div style="margin-top:22px;padding-top:18px;border-top:1px solid var(--rule);">
          <p style="font-size:12.5px;color:var(--muted);line-height:1.6;">Please telephone before visiting to
            confirm counselling hours. Correspondence is by email and WhatsApp; important correspondence is
            sent by speed post.</p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Finding us</span>
      <h2 style="font-size:26px;">Opposite Plaza, a short walk from Dadar station</h2>
    </div>
    <div class="map-embed rise">
      <iframe src="{MAP_EMBED}" title="Map showing Dr. Gaikwad's Institute, Dadar West, Mumbai"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen width="600" height="450"></iframe>
    </div>
    <div class="map-actions rise">
      <a class="btn btn-primary" href="{MAP_LINK}" target="_blank" rel="noopener">Open in Google Maps</a>
      <a class="btn btn-ghost" href="{MAP_DIRECTIONS}" target="_blank" rel="noopener">Get directions</a>
      <p class="map-note">203 Akanksha, Opposite Plaza, Dadar (West), Mumbai 400 028 &middot;
         nearest station Dadar.</p>
    </div>
  </div>
</section>""")


# ============================================================ GALLERY
def photo_grid(items):
    """items: (kind, caption) or (kind, caption, icon_key). Defaults to the
    camera watermark when no icon is given."""
    out = []
    for item in items:
        kind, cap, icon = (*item, "camera")[:3] if len(item) == 2 else item
        out.append(f'<figure class="photo">{ghost_icon(icon)}<figcaption><b>{kind}</b>{cap}</figcaption></figure>')
    return "".join(out)

PAGES["gallery.html"] = dict(
    title="Gallery & Campus Life — Dr. Gaikwad's Institute, Dadar",
    description="Photographs of training, hospital postings, festivals, competitions and convocation at "
                "Dr. Gaikwad's Institute, Dadar West, Mumbai.",
    body=f"""{pagehead([("Home","index.html"),("Gallery",None)],
    "There is a life here beyond the attendance register.",
    "We ask a great deal of our students — ninety per cent attendance, uniform on duty, night shifts. We also "
    "make room for Ganeshotsav, sports day, cooking competitions and a proper convocation. Both are true, and "
    "both belong on this page.",
    [("16","Events a year"),("2","Days of convocation"),("30","Years of batches")])}

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Training</span>
      <h2>Classroom and practical work</h2>
      <p>The first four months at the Dadar premises: lectures, practical laboratory sessions and the
         chapter-end tests that count towards internal assessment.</p>
    </div>
    <div class="grid-3 rise">
      {photo_img("posting-sample-collection-ppe", "Student in gown, mask and face shield collecting a blood sample",
                 "Practical", "Sample collection in full protective equipment")}
      {photo_img("posting-venepuncture-02", "Student drawing a blood sample from a seated patient",
                 "Practical", "Venepuncture practice under supervision")}
      {photo_img("posting-ppe-full", "Student wearing a full protective gown, face shield and mask",
                 "Practical", "Protective equipment drill")}
      {photo_img("posting-injection-prep", "Student preparing an injection with the doctor observing",
                 "Practical", "Injection preparation, checked by the doctor")}
      {photo_img("posting-equipment", "Student operating bedside equipment beside a patient",
                 "Practical", "Bedside equipment handling")}
      {photo_img("posting-examination", "Student examining a patient using a stethoscope",
                 "Practical", "Examination technique on the ward")}
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Hospital postings</span>
      <h2>On duty across Mumbai</h2>
      <p>From the fifth month, students work full shifts in nursing homes, diagnostic laboratories, operation
         theatres and opticians' practices under a practising doctor.</p>
    </div>
    <div class="grid-3 rise">
      {photo_img("posting-with-doctor-01", "Student on posting with the supervising doctor",
                 "On duty", "With the doctor supervising her posting")}
      {photo_img("posting-consulting-room", "Student standing with a senior doctor in his consulting room",
                 "On duty", "In the consulting room of a partner practice")}
      {photo_img("posting-with-doctor-02", "Two students in uniform with a doctor at his practice",
                 "On duty", "Two students at their posting practice")}
      {photo_img("posting-with-doctor-03", "Student in uniform with a doctor at a partner clinic",
                 "On duty", "At a partner clinic in Mumbai")}
      {photo_img("posting-with-doctor-04", "Student in uniform with a doctor at the practice desk",
                 "On duty", "At the practice where she trained")}
      {photo_img("posting-ward-patient", "Student in white uniform beside an elderly patient",
                 "On duty", "Patient care during a ward shift")}
    </div>
    <div style="margin-top:26px;">
      <a class="btn btn-primary" href="placements.html">More about postings and placement</a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Campus life</span>
      <h2>Festivals, competitions and celebration</h2>
      <p>Funded entirely from fine collections — not one rupee of it is used by the institute for itself.
         Ganeshotsav, Dassehra, Diwali, Eid, Christmas, New Year, Republic Day and Gurupurnima are all marked
         here.</p>
    </div>
    <div class="grid-4 rise">
      {photo_grid([
        ("Ganeshotsav", "Ganpati celebration at the institute", "star"),
        ("Republic Day", "Flag hoisting and prize distribution", "star"),
        ("Sports Day", "Annual athletics and team events", "medal"),
        ("Gurupurnima", "Students with the teaching staff", "book"),
        ("Dassehra & Diwali", "Festival celebration with the batch", "star"),
        ("Eid & Christmas", "Festivals marked across the batch", "star"),
        ("Saree Day", "Saree day and colour day", "camera"),
        ("New Year", "New year celebration with the batch", "star"),
      ])}
    </div>

    <div class="sec-head rise" style="margin-top:54px;">
      <span class="label">Competitions</span>
      <h2 style="font-size:26px;">Beyond the syllabus</h2>
      <p>Activities run alongside the course and included in the fee — no separate charge.</p>
    </div>
    <div class="grid-4 rise">
      {photo_grid([
        ("Cooking", "Cooking competition", "medal"),
        ("Mehendi", "Mehendi competition", "medal"),
        ("Hair styling", "Hair styling competition", "medal"),
        ("Yoga", "Yoga and fitness sessions", "star"),
      ])}
    </div>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Convocation</span>
      <h2>The day the diploma is awarded</h2>
      <p>Held in August or September each year, subject to results and hall availability. Certificates are
         awarded under Bharat Sevak Samaj certification, and families are welcome.</p>
    </div>
    <div class="grid-3 rise">
      {photo_grid([
        ("Convocation", "Certificates awarded to the graduating batch", "cap"),
        ("Convocation", "Distinction holders with the teaching staff", "cap"),
        ("Convocation", "Families at the annual convocation", "cap"),
      ])}
    </div>
    <div class="callout rise" style="max-width:none;margin-top:30px;">
      <span class="tag-l">A note on these photographs</span>
      <p>The practical and posting photographs on this page are from the institute's own archive, taken at the
         practices where our students train. Panels still marked with an icon are awaiting a photograph
         &mdash; they are drawn that way on purpose, so nothing here is mistaken for a picture of an event we
         have not photographed. If you appear in any image on this page and would like it removed, write to
         <a href="mailto:{EMAIL}" style="color:var(--navy-mid);font-weight:600;">{EMAIL}</a> and we will take
         it down.</p>
    </div>
  </div>
</section>

{cta_band("Come and see it for yourself.",
          "Photographs only go so far. Telephone to arrange a counselling visit and see the premises, meet the "
          "staff and ask whatever you like.")}""")

# ============================================================ 404
PAGES["404.html"] = dict(
    title="Page not found — Dr. Gaikwad's Institute",
    description="The page you were looking for could not be found. Browse our courses, fees and admission "
                "information, or contact the institute directly.",
    active="none",
    head_extra='<base href="/">\n',
    robots='<meta name="robots" content="noindex">\n',
    body=f"""<section class="pagehead">
  <div class="wrap" style="padding-top:64px;padding-bottom:72px;">
    <div class="crumb"><a href="index.html">Home</a><span class="sep">/</span>Page not found</div>
    <p style="font-family:var(--mono);font-size:13px;letter-spacing:.14em;color:var(--brass-lt);
              text-transform:uppercase;font-weight:700;">Error 404</p>
    <h1 style="margin-top:14px;">This page has moved, or never existed.</h1>
    <p class="dek">That happens when a link is out of date or an address is mistyped. Everything on the site
      is reachable from the links below &mdash; or telephone the institute and we will point you to it.</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:30px;">
      <a class="btn btn-brass" href="index.html">Back to the home page</a>
      <a class="btn btn-on-dark" href="tel:{PHONE1}">Call {PHONE1_H}</a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head rise">
      <span class="label">Where you may have been going</span>
      <h2>The pages people look for most</h2>
    </div>
    <div class="grid-3 rise">
      <div class="card">
        <span class="label">Courses</span>
        <h4>What we teach</h4>
        <p>Four two-year stipendiary diplomas, twelve one-year certificates for working technicians, and a
           B.Voc degree pathway.</p>
        <a class="card-link" href="courses.html">Browse all courses &rarr;</a>
      </div>
      <div class="card">
        <span class="label">Fees &amp; Stipend</span>
        <h4>What it costs</h4>
        <p>The full fee schedule for every course, the stipend ladder against it, instalment dates and the
           refund policy.</p>
        <a class="card-link" href="fees.html">See the fee schedule &rarr;</a>
      </div>
      <div class="card">
        <span class="label">Admissions</span>
        <h4>How to join</h4>
        <p>The four-step admission process, the document checklist and the institute rules you agree to on
           admission.</p>
        <a class="card-link" href="admissions.html">Read the process &rarr;</a>
      </div>
    </div>

    <div class="grid-4 rise" style="margin-top:22px;">
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Diploma pages</h4>
        <ul style="margin-top:10px;">
          <li><a href="course-patient-care.html" style="color:var(--navy-mid);font-weight:600;">Patient Care</a></li>
          <li><a href="course-medical-lab-technology.html" style="color:var(--navy-mid);font-weight:600;">Medical Lab Technology</a></li>
          <li><a href="course-operation-theatre.html" style="color:var(--navy-mid);font-weight:600;">Operation Theatre</a></li>
          <li><a href="course-optometry.html" style="color:var(--navy-mid);font-weight:600;">Optometry</a></li>
        </ul></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">The institute</h4>
        <ul style="margin-top:10px;">
          <li><a href="about.html" style="color:var(--navy-mid);font-weight:600;">About &amp; BSS</a></li>
          <li><a href="placements.html" style="color:var(--navy-mid);font-weight:600;">Placements</a></li>
          <li><a href="gallery.html" style="color:var(--navy-mid);font-weight:600;">Gallery</a></li>
        </ul></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Other courses</h4>
        <ul style="margin-top:10px;">
          <li><a href="certificate-courses.html" style="color:var(--navy-mid);font-weight:600;">Certificate courses</a></li>
          <li><a href="bvoc.html" style="color:var(--navy-mid);font-weight:600;">B.Voc &amp; ADMLT</a></li>
          <li><a href="refund-policy.html" style="color:var(--navy-mid);font-weight:600;">Refund policy</a></li>
        </ul></div>
      <div class="card"><h4 style="font-size:15px;margin-top:0;">Speak to us</h4>
        <p style="font-size:13px;">Counselling is free and carries no obligation.</p>
        <a class="btn btn-brass btn-sm" style="width:100%;margin-top:12px;" href="{WA}">WhatsApp us</a>
        <a class="btn btn-ghost btn-sm" style="width:100%;margin-top:8px;" href="contact.html">Contact page</a></div>
    </div>
  </div>
</section>""")


def build():
    written = []
    for filename, cfg in PAGES.items():
        html = shell(filename, cfg["title"], cfg["description"], cfg["body"], cfg.get("active"),
                     cfg.get("head_extra", ""), cfg.get("robots", ""))
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as fh:
            fh.write(html)
        written.append((filename, len(html)))
    return written


if __name__ == "__main__":
    pages = build()
    print(f"Built {len(pages)} pages:\n")
    for name, size in sorted(pages):
        print(f"  {name:<42} {size/1024:6.1f} KB")
