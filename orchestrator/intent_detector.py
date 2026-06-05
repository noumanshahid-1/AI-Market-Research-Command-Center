"""
intent_detector.py
------------------
Advanced market query intent detector.
"""

import re
from services.entity_parser import EntityParser


class IntentDetector:
    """
    Detects market research intent with priority-aware logic.
    """

    NEWS_KEYWORDS = [
        "news", "latest", "headline", "headlines", "update",
        "updates", "recent", "current", "breaking"
    ]

    PRODUCT_KEYWORDS = [
        "product", "products", "trend", "trending", "gadgets",
        "smartphones", "laptops", "electric vehicles", "gaming",
        "wearables", "devices"
    ]

    STOCK_KEYWORDS = [
        "stock", "stocks", "price", "share", "shares", "ticker",
        "investment", "invest", "market price", "crypto", "bitcoin",
        "ethereum", "btc", "eth"
    ]

    COMPARISON_KEYWORDS = [
        " vs ",
        " versus ",
        " compare ",
        " comparison "
    ]

    SCREENER_KEYWORDS = [
        "top ai stocks",
        "best ai stocks",
        "leading ai stocks",
        "top semiconductor stocks",
        "best semiconductor stocks",
        "chip stocks",
        "top ev stocks",
        "best ev stocks",
        "leading ev stocks",
        "top crypto assets",
        "top crypto",
        "best crypto"
    ]

    HEATMAP_KEYWORDS = [
        "heatmap",
        "sector heatmap",
        "market heatmap",
        "ai sector",
        "semiconductor heatmap",
        "ev heatmap",
        "crypto heatmap"
    ]

    def __init__(self, query: str):
        self.original_query = query
        self.query = re.sub(
            r"[^a-zA-Z0-9\s&-]",
            " ",
            query.lower()
        )

    def detect(self) -> dict:
        """
        Return detected intent dictionary.
        """

        query_with_spaces = f" {self.query} "

        assets = EntityParser.extract_assets(
            self.original_query
        )

        comparison_detected = any(
            keyword in query_with_spaces
            for keyword in self.COMPARISON_KEYWORDS
        )

        screener_detected = any(
            keyword in self.query
            for keyword in self.SCREENER_KEYWORDS
        )

        heatmap_detected = any(
            keyword in self.query
            for keyword in self.HEATMAP_KEYWORDS
        )

        product_detected = any(
            keyword in self.query
            for keyword in self.PRODUCT_KEYWORDS
        )

        news_detected = any(
            keyword in self.query
            for keyword in self.NEWS_KEYWORDS
        )

        stock_detected = (
            any(keyword in self.query for keyword in self.STOCK_KEYWORDS)
            or bool(assets)
        )

        multi_asset_detected = (
            len(assets) >= 2
            and not comparison_detected
            and not screener_detected
            and not heatmap_detected
        )

        return {
            "heatmap": heatmap_detected,
            "screener": screener_detected,
            "comparison": comparison_detected,
            "multi_asset": multi_asset_detected,
            "stock": stock_detected,
            "news": news_detected,
            "product": product_detected,
        }