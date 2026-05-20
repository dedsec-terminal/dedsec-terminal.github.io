import os
import json
import random
import re
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import requests
import trafilatura

from quote import get_random_quote

# =========================
# GROQ SETUP (GITHUB SAFE)
# =========================

try:
    from groq import Groq
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
except:
    client = None

# =========================
# PATHS
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

CONTENT_DIR = BASE_DIR / "content" / "posts"
DATA_DIR = BASE_DIR / "data"

SEEN_FILE = DATA_DIR / "seen.json"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# =========================
# FEEDS (GLOBAL INTAKE LAYER)
# =========================

FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://krebsonsecurity.com/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://securelist.com/feed/",
    "https://www.schneier.com/feed/atom/",
    "https://www.wired.com/feed/category/security/rss",
    "https://www.microsoft.com/en-us/security/blog/feed/",
    "https://databreaches.net/feed/",
    "https://torrents.ddosecrets.org/releases.xml"
]

# =========================
# CATEGORY QUOTA (KEY FIX)
# =========================

CATEGORY_MIN = {
    "threat-intel": 3,
    "data-breaches": 3,
    "cves": 3,
    "malware": 3,
    "research": 3
}

CATEGORIES = {k: [] for k in CATEGORY_MIN}
OVERFLOW = []

# =========================
# UTILS
# =========================

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})


def hash_id(x):
    return hashlib.sha256(x.encode()).hexdigest()


def slugify(title):
    title = title.lower()
    title = re.sub(r"[^\w\s-]", "", title)
    title = title.replace(" ", "-")
    return title[:90]


def get_time(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)

# =========================
# CLASSIFIER (CORE ENGINE)
# =========================

def classify(text, title, feed_url):

    t = (text + " " + title).lower()

    if "cve" in t or "vulnerability" in t or "exploit" in t:
        return "cves"

    if "ransomware" in t or "malware" in t or "trojan" in t:
        return "malware"

    if "breach" in t or "leak" in t or "stolen" in t:
        return "data-breaches"

    if "research" in feed_url or "schneier" in feed_url:
        return "research"

    return "threat-intel"

# =========================
# FETCH ARTICLE
# =========================

def fetch(url):
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        return trafilatura.extract(r.text)
    except:
        return None

# =========================
# GROQ SUMMARY
# =========================

def summarize(title, text):
    if not text:
        return None

    if not client:
        return text[:900]

    try:
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"Summarize cybersecurity article:\n{title}\n\n{text[:12000]}"
            }],
            temperature=0.2,
            max_tokens=500
        )
        return res.choices[0].message.content
    except:
        return text[:900]

# =========================
# MAIN ENGINE
# =========================

def main():

    seen = set()
    if SEEN_FILE.exists():
        seen = set(json.load(open(SEEN_FILE)))

    print("🚀 Intel Balancer v2 Running...\n")

    pool = []

    # STEP 1: COLLECT ALL ARTICLES
    for feed_url in FEEDS:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:10]:

            link = entry.get("link")
            title = entry.get("title", "Untitled")

            if not link:
                continue

            uid = hash_id(link)
            if uid in seen:
                continue

            raw = fetch(link)
            if not raw:
                continue

            category = classify(raw, title, feed_url)

            pool.append({
                "uid": uid,
                "title": title,
                "link": link,
                "text": raw,
                "category": category,
                "time": get_time(entry)
            })

    # STEP 2: SORT BY RELEVANCE (simple: newest first)
    pool.sort(key=lambda x: x["time"], reverse=True)

    # STEP 3: DISTRIBUTE WITH QUOTA ENFORCEMENT
    for item in pool:

        cat = item["category"]

        if len(CATEGORIES[cat]) >= CATEGORY_MIN[cat]:
            OVERFLOW.append(item)
            continue

        summary = summarize(item["title"], item["text"])
        if not summary:
            continue

        quote = get_random_quote()

        slug = slugify(item["title"])
        file_path = CONTENT_DIR / f"{slug}.md"

        content = f"""---
title: "{item['title'].replace('"','')}"
date: {item['time'].isoformat()}
draft: false
categories:
  - {cat}
---

{summary}

---

> *{quote}*

Source: [{item['title']}]({item['link']})
"""

        file_path.write_text(content, encoding="utf-8")

        CATEGORIES[cat].append(file_path.name)
        seen.add(item["uid"])

        print(f"[{cat}] {file_path.name}")

    # STEP 4: FILL EMPTY CATEGORIES FROM OVERFLOW
    for item in OVERFLOW:

        for cat in CATEGORIES:

            if len(CATEGORIES[cat]) >= CATEGORY_MIN[cat]:
                continue

            summary = summarize(item["title"], item["text"])
            if not summary:
                continue

            quote = get_random_quote()

            slug = slugify(item["title"])
            file_path = CONTENT_DIR / f"{slug}.md"

            content = f"""---
title: "{item['title'].replace('"','')}"
date: {item['time'].isoformat()}
draft: false
categories:
  - {cat}
---

{summary}

---

> *{quote}*

Source: [{item['title']}]({item['link']})
"""

            file_path.write_text(content, encoding="utf-8")

            CATEGORIES[cat].append(file_path.name)
            seen.add(item["uid"])

            print(f"[FILL {cat}] {file_path.name}")

    # STEP 5: SAVE STATE
    json.dump(list(seen), open(SEEN_FILE, "w"), indent=2)

    print("\n📊 FINAL CATEGORY BALANCE:")
    for k, v in CATEGORIES.items():
        print(k, len(v))


if __name__ == "__main__":
    main()  