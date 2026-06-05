"""
product_agent.py
----------------
Specialized product trend intelligence agent.

Purpose:
- Validate query
- Normalize product search terms
- Fetch trend insights
"""

from agents.base_agent import BaseAgent
from services.google_trends_service import GoogleTrendsService


class ProductAgent(BaseAgent):
    """
    Product trend intelligence agent.
    """

    PRODUCT_MAP = {
        "smartphones": "smartphones",
        "phones": "smartphones",
        "ai gadgets": "artificial intelligence",
        "gadgets": "gadgets",
        "laptops": "laptops",
        "gaming consoles": "gaming",
        "electric vehicles": "electric cars",
        "electric cars": "electric cars",
        "cars": "cars"
    }

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def clean_query(self) -> str:
        """
        Normalize product queries.
        """

        lower_query = self.query.lower()

        for keyword, normalized in self.PRODUCT_MAP.items():
            if keyword in lower_query:
                return normalized

        # Remove generic filler
        remove_words = [
            "trending",
            "trend",
            "products",
            "product"
        ]

        for word in remove_words:
            lower_query = lower_query.replace(word, "")

        cleaned = lower_query.strip()

        return cleaned if cleaned else "technology"

    def fetch_data(self) -> dict:
        trends_service = GoogleTrendsService()

        cleaned_query = self.clean_query()

        return trends_service.get_trends(cleaned_query)

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "product",
                "status": "error",
                "message": "Invalid product query."
            }

        result = self.fetch_data()

        result["agent"] = "product"

        return result