import json
import random
import re
import feedparser
import trafilatura
import requests
from datetime import datetime
from pathlib import Path

# ==========================================
# PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
FEEDS_FILE = BASE_DIR / "feeds.json"
CONTENT_DIR = BASE_DIR / "content" / "posts"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# QUOTES
# ==========================================

QUOTES = [
    "Trust arrives on foot and leaves on horseback. — Dutch proverb",
    "When the winds of change blow, some build walls, others build windmills. — Chinese proverb",
    "Fall seven times, stand up eight. — Japanese proverb",
    "Vision without action is a daydream. Action without vision is a nightmare. — Japanese proverb",
    "The bamboo that bends is stronger than the oak that resists. — Japanese saying"
]

# ==========================================
# TEXT CLEANING
# ==========================================

def rewrite_text(text):
    paragraphs = text.split("\n")

    cleaned = []

    for p in paragraphs:
        p = p.strip()

        if len(p) > 60:
            cleaned.append(p)

    return "\n\n".join(cleaned[:6])


def clean_slug(title):
    slug = title.lower()

    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = slug.replace(" ", "-")
    slug = re.sub(r"-+", "-", slug)

    return slug[:80]


# ==========================================
# LOAD FEEDS
# ==========================================

with open(FEEDS_FILE, "r", encoding="utf-8") as f:
    feeds = json.load(f)

# ==========================================
# PROCESS FEEDS
# ==========================================

for category, urls in feeds.items():

    print(f"\nProcessing category: {category}")

    for url in urls:

        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:

            title = entry.get("title", "Untitled")
            article_url = entry.link

            try:
                response = requests.get(
                    article_url,
                    timeout=20,
                    headers={
                        "User-Agent":
                        "Mozilla/5.0"
                    }
                )

                downloaded = trafilatura.extract(
                    response.text,
                    include_comments=False,
                    include_links=False
                )

                text = rewrite_text(downloaded or "")

                if len(text) < 100:
                    print(f"Skipped: {title}")
                    continue

                slug = clean_slug(title)

                filename = CONTENT_DIR / f"{slug}.md"

                if filename.exists():
                    print(f"Already exists: {title}")
                    continue

                source_name = feed.feed.get(
                    "title",
                    "Source"
                )

                quote = random.choice(QUOTES)

                content = f"""---
title: "{title.replace('"', "'")}"
date: {datetime.today().strftime("%Y-%m-%d")}
draft: false
categories:
  - {category}
author: "DedSec-Terminal"
---

{text}

*{quote}*

Source: [{source_name}]({article_url}) · [Read Original →]({article_url})
"""

                with open(
                    filename,
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write(content)

                print(f"Created: {filename.name}")

            except Exception as e:
                print(f"Error processing '{title}': {e}")

print("\nRSS update complete.")