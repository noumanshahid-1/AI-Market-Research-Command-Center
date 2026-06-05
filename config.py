"""
config.py
----------
Central configuration file for:
- API keys
- Constants
- Query categories
- UI settings

Keep this file simple and centralized so the whole project
can scale without scattered hardcoded values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# =========================
# API CONFIGURATION
# =========================

# News API Key (Get from https://newsapi.org/)
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")


# =========================
# APPLICATION SETTINGS
# =========================

APP_NAME = "AI Market Research Command Center"

DEFAULT_NEWS_LIMIT = 5
DEFAULT_PRODUCT_LIMIT = 5


# =========================
# INTENT KEYWORDS
# These keywords help classify user queries.
# Keep transparent and editable.
# =========================

INTENT_KEYWORDS = {
    "stock": [
        "stock",
        "stocks",
        "share",
        "shares",
        "investment",
        "invest",
        "price",
        "market",
        "crypto",
        "bitcoin",
        "etf",
        "nasdaq",
        "s&p",
        "finance"
    ],

    "news": [
        "news",
        "latest",
        "headline",
        "headlines",
        "updates",
        "breaking",
        "current",
        "happening"
    ],

    "product": [
        "product",
        "products",
        "trend",
        "trending",
        "popular",
        "gadgets",
        "best selling",
        "market demand"
    ]
}


# =========================
# UI SETTINGS
# =========================

THEME = {
    "primary_color": "#4CAF50",
    "background_color": "#0E1117",
    "secondary_background": "#262730",
    "text_color": "#FAFAFA"
}