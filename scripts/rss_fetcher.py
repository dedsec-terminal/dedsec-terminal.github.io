import os
import json
import random
import re
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import feedparser
import requests
import trafilatura

from quote import get_random_quote

# ==========================================
# OPTIONAL GROQ
# ==========================================

USE_GROQ = True

try:
    from groq import Groq
except Exception:
    USE_GROQ = False

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = None
if USE_GROQ and GROQ_API_KEY:
    try:
        client = Groq(api_key=GROQ_API_KEY)
        print("✓ Groq enabled")
    except Exception:
        client = None
        print("⚠ Groq failed to initialize")
else:
    print("⚠ Groq disabled")

# ==========================================
# PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

CONTENT_DIR = BASE_DIR / "content" / "posts"
SEEN_FILE = BASE_DIR / ".seen_posts.json"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# SESSION
# ==========================================

session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/124 Safari/537.36"
    )
})

# ==========================================
# RSS SOURCES
# ==========================================

RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://krebsonsecurity.com/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://securelist.com/feed/",
    "https://www.schneier.com/feed/atom/",
    "https://www.wired.com/feed/category/security/rss",
    "https://databreaches.net/feed/",
    "https://torrents.ddosecrets.org/releases.xml",
    "https://www.cisa.gov/cybersecurity-advisories/all.xml",
    "https://www.zerodayinitiative.com/rss/published/",
]

# ==========================================
# CATEGORY KEYWORDS
# ==========================================

CATEGORY_KEYWORDS = {
    "threat-intel": [
        "apt", "threat", "espionage",
        "hack", "attacker", "campaign",
        "nation-state", "intelligence"
    ],

    "data-breaches": [
        "breach", "leak", "exposed",
        "database", "compromised",
        "stolen", "data leak"
    ],

    "cves": [
        "cve-", "vulnerability",
        "exploit", "rce",
        "security flaw", "kev"
    ],

    "malware": [
        "malware", "ransomware",
        "trojan", "botnet",
        "payload", "rootkit",
        "loader", "worm"
    ],

    "research": [
        "research", "analysis",
        "report", "study",
        "deep dive", "security research"
    ]
}

MIN_POSTS_PER_CATEGORY = 3

# ==========================================
# CHECKPOINT SYSTEM
# ==========================================

def load_seen():
    if SEEN_FILE.exists():
        try:
            with open(SEEN_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                return set(data)

        except Exception:
            pass

    return set()


def save_seen(seen):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(
            sorted(list(seen)),
            f,
            indent=2
        )


def get_hash(link):
    return hashlib.sha256(
        link.strip().encode("utf-8")
    ).hexdigest()

# ==========================================
# HELPERS
# ==========================================

def clean_slug(title):
    slug = title.lower()

    slug = re.sub(
        r"[^\w\s-]",
        "",
        slug
    )

    slug = slug.replace(" ", "-")
    slug = re.sub(r"-+", "-", slug)

    return slug[:100].strip("-")


def get_published_date(entry):

    if entry.get("published_parsed"):
        return datetime(
            *entry.published_parsed[:6],
            tzinfo=timezone.utc
        )

    if entry.get("updated_parsed"):
        return datetime(
            *entry.updated_parsed[:6],
            tzinfo=timezone.utc
        )

    return datetime.now(timezone.utc)


def fetch_article(url):

    try:
        r = session.get(
            url,
            timeout=20
        )

        r.raise_for_status()

        extracted = trafilatura.extract(
            r.text,
            include_comments=False,
            include_links=False,
            include_tables=False
        )

        if extracted and len(extracted) > 250:
            return extracted

    except Exception:
        pass

    return None


# ==========================================
# CLASSIFIER
# ==========================================

def classify_article(title, text):

    content = f"{title} {text}".lower()

    scores = {
        category: 0
        for category in CATEGORY_KEYWORDS
    }

    for category, words in CATEGORY_KEYWORDS.items():

        for word in words:
            if word in content:
                scores[category] += 1

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "research"

    return best


# ==========================================
# GROQ SUMMARY
# ==========================================

def generate_summary(title, text):

    if not text:
        return None

    fallback = text[:1000]

    if not client:
        return fallback

    try:
        prompt = f"""
Summarize this cybersecurity article.

Rules:
- 3 to 5 paragraphs
- concise
- technical but readable
- no fluff
- no headings

Title:
{title}

Article:
{text[:12000]}
""".strip()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=500
        )

        summary = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        return summary

    except Exception:
        return fallback


# ==========================================
# MAIN
# ==========================================

def main():

    seen = load_seen()

    print("🚀 Intel Balancer v2 Running...")

    category_count = {
        "threat-intel": 0,
        "data-breaches": 0,
        "cves": 0,
        "malware": 0,
        "research": 0
    }

    for feed_url in RSS_FEEDS:

        try:
            feed = feedparser.parse(feed_url)
        except Exception:
            continue

        for entry in feed.entries[:20]:

            title = (
                entry.get("title", "")
                .strip()
            )

            link = entry.get("link")

            if not title or not link:
                continue

            article_hash = get_hash(link)

            # hard skip already processed
            if article_hash in seen:
                continue

            slug = clean_slug(title)

            file_path = (
                CONTENT_DIR /
                f"{slug}.md"
            )

            # if file exists but hash missing
            if file_path.exists():
                seen.add(article_hash)
                continue

            raw = fetch_article(link)

            if not raw:
                continue

            category = classify_article(
                title,
                raw
            )

            if (
                category_count[category]
                >= MIN_POSTS_PER_CATEGORY
            ):
                continue

            summary = generate_summary(
                title,
                raw
            )

            if (
                not summary or
                len(summary) < 120
            ):
                continue

            quote = get_random_quote()

            published_date = (
                get_published_date(entry)
            )

            markdown = f"""---
title: "{title.replace('"', "'")}"
date: {published_date.isoformat()}
draft: false
categories:
  - {category}
author: "DedSec-Terminal"
---

{summary}

---

> *{quote}*

Source: [{title}]({link})
"""

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:
                f.write(markdown)

            seen.add(article_hash)

            category_count[
                category
            ] += 1

            print(
                f"[{category}] "
                f"{file_path.name}"
            )

    save_seen(seen)

    print("\n📊 FINAL CATEGORY BALANCE:")

    for k, v in category_count.items():
        print(k, v)


if __name__ == "__main__":
    main()