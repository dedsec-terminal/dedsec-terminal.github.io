import os
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import feedparser
import requests
import trafilatura

from quote import get_random_quote

# ==========================================================
# OPTIONAL GROQ
# ==========================================================

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
        print("Groq enabled")
    except Exception:
        client = None
        print("Groq initialization failed")
else:
    print("Groq disabled")

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CONTENT_DIR = BASE_DIR / "content" / "posts"
SEEN_FILE = BASE_DIR / ".seen_posts.json"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# CONFIG
# ==========================================================

MIN_POSTS_PER_CATEGORY = 3
MAX_FEED_ENTRIES = 50

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

CATEGORIES = [
    "threat-intel",
    "data-breaches",
    "cves",
    "malware",
    "research"
]

FEED_WEIGHTS = {
    "cisa.gov": {"cves": 10},
    "zerodayinitiative.com": {"cves": 8},
    "securelist.com": {"malware": 6},
    "databreaches.net": {"data-breaches": 8},
    "krebsonsecurity.com": {"threat-intel": 4},
    "thehackernews": {"threat-intel": 3, "malware": 2},
}

CATEGORY_KEYWORDS = {
    "threat-intel": [
        "apt", "campaign", "espionage", "threat actor",
        "nation-state", "targeted attack", "phishing",
        "credential theft", "cyber operation", "hacking group",
        "identity attack", "adversary"
    ],

    "data-breaches": [
        "breach", "data leak", "leak", "compromised",
        "database exposed", "stolen", "exposed",
        "security incident", "data exposure"
    ],

    "cves": [
        "cve-", "vulnerability", "exploit", "zero-day",
        "rce", "security flaw", "patch", "kev",
        "privilege escalation", "remote code execution"
    ],

    "malware": [
        "malware", "ransomware", "trojan", "botnet",
        "rootkit", "worm", "loader", "payload",
        "backdoor", "dropper"
    ],

    "research": [
        "research", "analysis", "study",
        "report", "whitepaper", "deep dive",
        "technical analysis", "guide"
    ]
}

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


# ==========================================================
# CHECKPOINT MEMORY
# ==========================================================

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


# ==========================================================
# HELPERS
# ==========================================================

def clean_slug(title):
    slug = title.lower()

    slug = re.sub(
        r"[^\\w\\s-]",
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
        response = session.get(
            url,
            timeout=25
        )

        response.raise_for_status()

        extracted = trafilatura.extract(
            response.text,
            include_comments=False,
            include_links=False,
            include_tables=False
        )

        if extracted and len(extracted) > 250:
            return extracted

    except Exception:
        pass

    return None


# ==========================================================
# SMART CLASSIFIER V3
# ==========================================================

def score_article(
    title,
    text,
    link,
    metadata=""
):

    content = (
        f"{title} {text} {metadata}"
    ).lower()

    scores = {
        category: 0
        for category in CATEGORY_KEYWORDS
    }

    # Keyword scoring
    for category, words in CATEGORY_KEYWORDS.items():

        for word in words:

            if word in content:
                scores[category] += 2

    # Feed reputation weighting
    for domain, weights in FEED_WEIGHTS.items():

        if domain in link.lower():

            for cat, value in weights.items():
                scores[cat] += value

    # Strong pattern boosts
    if re.search(
        r"cve-\\d{4}-\\d+",
        content
    ):
        scores["cves"] += 10

    if "ransomware" in content:
        scores["malware"] += 5

    if (
        "breach" in content
        or "leak" in content
        or "exposed" in content
    ):
        scores["data-breaches"] += 5

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    category, confidence = ranked[0]

    return (
        category,
        confidence,
        scores
    )


# ==========================================================
# OPTIONAL GROQ FALLBACK
# ==========================================================

def groq_classify(
    title,
    text
):

    if not client:
        return "research"

    try:

        prompt = f'''
Classify this cybersecurity article into exactly ONE category:

threat-intel
data-breaches
cves
malware
research

Title:
{title}

Article:
{text[:4000]}
'''.strip()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=20
        )

        result = (
            response
            .choices[0]
            .message
            .content
            .strip()
            .lower()
        )

        if result in CATEGORIES:
            return result

    except Exception:
        pass

    return "research"


# ==========================================================
# GROQ SUMMARY
# ==========================================================

def generate_summary(
    title,
    text
):

    fallback = text[:1200]

    if not client:
        return fallback

    try:

        prompt = f'''
Summarize this cybersecurity article.

Rules:
- 3 to 5 paragraphs
- concise
- technical but readable
- no headings
- professional tone

Title:
{title}

Article:
{text[:12000]}
'''.strip()

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


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("Intel Balancer v3 Running")

    seen = load_seen()

    category_count = {
        category: 0
        for category in CATEGORIES
    }

    candidate_pool = []

    # ------------------------------------------------------
    # COLLECT ARTICLES
    # ------------------------------------------------------

    for feed_url in RSS_FEEDS:

        try:
            feed = feedparser.parse(feed_url)
        except Exception:
            continue

        for entry in feed.entries[:MAX_FEED_ENTRIES]:

            title = (
                entry.get("title", "")
                .strip()
            )

            link = entry.get("link")

            if not title or not link:
                continue

            article_hash = get_hash(link)

            if article_hash in seen:
                continue

            slug = clean_slug(title)

            file_path = (
                CONTENT_DIR /
                f"{slug}.md"
            )

            if file_path.exists():
                seen.add(article_hash)
                continue

            raw = fetch_article(link)

            if not raw:
                continue

            metadata = ""

            if entry.get("tags"):
                try:
                    metadata = " ".join(
                        str(x.get("term", ""))
                        for x in entry.tags
                    )
                except Exception:
                    pass

            (
                category,
                confidence,
                _
            ) = score_article(
                title,
                raw,
                link,
                metadata
            )

            # Low confidence → Groq classifier
            if confidence <= 2:
                category = groq_classify(
                    title,
                    raw
                )

            candidate_pool.append({
                "title": title,
                "slug": slug,
                "raw": raw,
                "link": link,
                "category": category,
                "score": confidence,
                "hash": article_hash,
                "published": (
                    get_published_date(entry)
                )
            })

    # ------------------------------------------------------
    # SORT BY QUALITY
    # ------------------------------------------------------

    candidate_pool = sorted(
        candidate_pool,
        key=lambda x: x["score"],
        reverse=True
    )

    used_hashes = set()

    # ------------------------------------------------------
    # GUARANTEED CATEGORY FILL
    # ------------------------------------------------------

    for category in CATEGORIES:

        category_posts = [
            x for x in candidate_pool
            if (
                x["category"] == category
                and x["hash"]
                not in used_hashes
            )
        ]

        while (
            category_count[category]
            < MIN_POSTS_PER_CATEGORY
        ):

            if category_posts:
                article = category_posts.pop(0)

            else:
                # Smart rebalance
                fallback = [
                    x for x in candidate_pool
                    if x["hash"]
                    not in used_hashes
                ]

                if not fallback:
                    break

                article = fallback[0]

            summary = generate_summary(
                article["title"],
                article["raw"]
            )

            if (
                not summary
                or len(summary) < 120
            ):
                continue

            quote = get_random_quote()

            safe_title = (
                article["title"]
                .replace('"', "'")
            )

            markdown = f'''---
title: "{safe_title}"
date: {article["published"].isoformat()}
draft: false
categories:
  - {category}
author: "DedSec-Terminal"
---

{summary}

---

> *{quote}*

Source: [{safe_title}]({article["link"]})
'''

            file_path = (
                CONTENT_DIR /
                f'{article["slug"]}.md'
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:
                f.write(markdown)

            used_hashes.add(
                article["hash"]
            )

            seen.add(
                article["hash"]
            )

            category_count[
                category
            ] += 1

            print(
                f'[{category}] '
                f'{file_path.name}'
            )

    save_seen(seen)

    print("\\nFinal Category Balance:")

    for k, v in category_count.items():
        print(k, v)


if __name__ == "__main__":
    main()
