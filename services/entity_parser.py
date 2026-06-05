"""
entity_parser.py
----------------
Central asset/entity parser.

Purpose:
- Resolve company/crypto names to tickers
- Extract multiple assets from mixed queries
- Reduce bad ticker extraction
"""

import re


class EntityParser:
    """
    Shared entity parser for stocks, crypto, comparison, and multi-asset queries.
    """

    COMPANY_TICKERS = {
        "apple": "AAPL",
        "aapl": "AAPL",

        "tesla": "TSLA",
        "tsla": "TSLA",

        "nvidia": "NVDA",
        "nvda": "NVDA",

        "microsoft": "MSFT",
        "msft": "MSFT",

        "google": "GOOGL",
        "alphabet": "GOOGL",
        "googl": "GOOGL",

        "meta": "META",
        "facebook": "META",

        "amazon": "AMZN",
        "amzn": "AMZN",

        "amd": "AMD",
        "intel": "INTC",
        "intc": "INTC",
        "tsmc": "TSM",
        "broadcom": "AVGO",

        "bitcoin": "BTC-USD",
        "btc": "BTC-USD",

        "ethereum": "ETH-USD",
        "eth": "ETH-USD",

        "solana": "SOL-USD",
        "sol": "SOL-USD",

        "dogecoin": "DOGE-USD",
        "doge": "DOGE-USD",
    }

    STOPWORDS = {
        "stock", "stocks", "price", "prices", "latest", "current",
        "today", "share", "shares", "ticker", "news", "recent",
        "market", "markets", "please", "show", "tell", "me",
        "and", "with", "about", "for", "of", "the", "a", "an",
        "best", "top", "leading", "trend", "trending", "heatmap",
        "sector", "compare", "comparison", "versus", "vs"
    }

    @staticmethod
    def normalize(query: str) -> str:
        """
        Normalize query text.
        """

        return re.sub(
            r"[^a-zA-Z0-9\s&-]",
            " ",
            query.lower()
        )

    @classmethod
    def extract_assets(cls, query: str) -> list:
        """
        Extract all recognizable assets from query.
        """

        clean_query = cls.normalize(query)
        found = []

        # Phrase/name matching first
        for name, ticker in cls.COMPANY_TICKERS.items():
            pattern = rf"\b{re.escape(name)}\b"

            if re.search(pattern, clean_query):
                if ticker not in found:
                    found.append(ticker)

        # Uppercase ticker fallback from original query
        raw_tokens = re.findall(
            r"\b[A-Z]{2,6}(?:-USD)?\b",
            query
        )

        for token in raw_tokens:
            if token not in found:
                found.append(token)

        return found

    @classmethod
    def extract_primary_asset(cls, query: str) -> str:
        """
        Extract first asset from query.
        """

        assets = cls.extract_assets(query)

        if assets:
            return assets[0]

        clean_query = cls.normalize(query)
        words = [
            word for word in clean_query.split()
            if word not in cls.STOPWORDS
        ]

        for word in words:
            if len(word) <= 5 and word.isalpha():
                return word.upper()

        return "AAPL"

    @classmethod
    def extract_comparison_assets(cls, query: str) -> list:
        """
        Extract two assets for comparison query.
        """

        assets = cls.extract_assets(query)

        if len(assets) >= 2:
            return assets[:2]

        return []