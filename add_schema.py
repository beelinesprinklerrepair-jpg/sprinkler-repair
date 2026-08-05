import re
import json
import os

BASE = "/sessions/charming-confident-dirac/mnt/Building Beeline Website"

AGGREGATE_RATING = {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "reviewCount": "136",
    "bestRating": "5"
}

REVIEWS = [
    {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Jake R."},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "We just moved into our new home in Meridian and had Beeline install the sprinkler system before sod went in. The whole thing was done in a day and a half and the crew did great work. System has been running perfectly ever since.",
        "datePublished": "2024-03-01"
    },
    {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Mike T."},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "Got quotes from a couple of companies. Beeline was competitive on price and actually took the time to explain the zone layout to me before they started. Install went smooth and everything works great. Highly recommend.",
        "datePublished": "2024-04-15"
    },
    {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Sarah W."},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "Called Beeline for a repair and they came out the next day. Diagnosed the problem fast, fixed it clean, and walked me through what was wrong. Fair price and great service.",
        "datePublished": "2024-05-10"
    },
    {
        "@type": "Review",
        "author": {"@type": "Person", "name": "Derek L."},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
        "reviewBody": "Beeline has taken care of our system for three seasons now. Reliable, honest, and they always show up when they say they will. Wouldn't use anyone else.",
        "datePublished": "2024-07-20"
    }
]

LOCAL_BUSINESS_OBJECT = {
    "@type": "LocalBusiness",
    "name": "Beeline Sprinkler Repair",
    "telephone": "(208) 880-2712",
    "url": "https://www.beelinesprinklerrepair.com",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "5606 W Amity Rd",
        "addressLocality": "Nampa",
        "addressRegion": "ID",
        "postalCode": "83687",
        "addressCountry": "US"
    },
    "aggregateRating": AGGREGATE_RATING,
    "review": REVIEWS
}

# Files that already have aggregateRating - skip
already_done = {
    "sprinkler-installation.html", "boise-sprinkler-repair.html", "index.html",
    "plans.html", "valve-repair-treasure-valley.html", "reviews.html",
    "caldwell-sprinkler-repair.html", "backflow.html", "controller-replacement.html",
    "sprinkler-head-replacement-treasure-valley.html", "middleton-sprinkler-repair.html",
    "star-sprinkler-repair.html", "eagle-sprinkler-repair.html", "kuna-sprinkler-repair.html",
    "nampa-sprinkler-repair.html", "meridian-sprinkler-repair.html",
    "winterization.html", "emergency.html", "sprinkler-repair.html"
}

html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and f not in already_done]

results = []

for fname in sorted(html_files):
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the JSON-LD script block
    pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if not matches:
        results.append(f"SKIP (no schema): {fname}")
        continue

    # Use the first (main) JSON-LD block
    m = matches[0]
    json_str = m.group(2)
    
    try:
        schema = json.loads(json_str)
    except json.JSONDecodeError as e:
        results.append(f"ERROR parsing {fname}: {e}")
        continue

    graph = schema.get("@graph", [])
    modified = False

    # Check if any object already has aggregateRating
    has_rating = any("aggregateRating" in obj for obj in graph)
    if has_rating:
        results.append(f"SKIP (already has aggregateRating): {fname}")
        continue

    # Find a Service or LocalBusiness to inject into
    injectable = None
    for obj in graph:
        if obj.get("@type") in ("Service", "LocalBusiness", "Plumber", "HomeAndConstructionBusiness", "ProfessionalService"):
            injectable = obj
            break

    if injectable is not None:
        injectable["aggregateRating"] = AGGREGATE_RATING
        injectable["review"] = REVIEWS
        modified = True
        method = f"injected into @type:{injectable['@type']}"
    else:
        # No injectable type — add a LocalBusiness object
        graph.append(LOCAL_BUSINESS_OBJECT)
        schema["@graph"] = graph
        modified = True
        method = "added LocalBusiness object"

    if modified:
        new_json = json.dumps(schema, ensure_ascii=False, separators=(',', ':'))
        new_content = content[:m.start()] + m.group(1) + new_json + m.group(3) + content[m.end():]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        results.append(f"OK ({method}): {fname}")

for r in results:
    print(r)
