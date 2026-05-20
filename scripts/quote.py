import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_QUOTES_FILE = BASE_DIR / "raw.json"

DEFAULT_QUOTE = (
    "Vision without action is a daydream. Action without vision is a nightmare.\n"
    "Author: Japanese proverb"
)


# ------------------------------------------
# LOAD QUOTES
# ------------------------------------------
def load_quotes():
    try:
        with open(RAW_QUOTES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        quotes = []

        if isinstance(data, list):
            for item in data:

                # -------------------------
                # STRING FORMAT
                # -------------------------
                if isinstance(item, str):
                    item = item.strip()
                    if item:
                        quotes.append(item)

                # -------------------------
                # DICT FORMAT
                # -------------------------
                elif isinstance(item, dict):

                    quote = (
                        item.get("quote")
                        or item.get("text")
                        or item.get("content")
                        or item.get("quoteText")   # FIXED
                    )

                    author = (
                        item.get("author")
                        or item.get("by")
                        or item.get("source")
                        or item.get("quoteAuthor")  # FIXED
                    )

                    if quote and author:
                        # SAFE FORMAT (NO EM DASH)
                        quotes.append(
                            f"{quote}\nAuthor: {author}"
                        )

                    elif quote:
                        quotes.append(quote)

        if quotes:
            print(f"Loaded {len(quotes)} quotes")
            return quotes

    except Exception as e:
        print(f"Quote load error: {e}")

    return [DEFAULT_QUOTE]


# ------------------------------------------
# GLOBAL QUOTES CACHE
# ------------------------------------------
QUOTES = load_quotes()


# ------------------------------------------
# GET RANDOM QUOTE
# ------------------------------------------
def get_random_quote():
    return random.choice(QUOTES)


# ------------------------------------------
# TEST OUTPUT
# ------------------------------------------
if __name__ == "__main__":
    print("\nRandom Quote:\n")
    print(get_random_quote())