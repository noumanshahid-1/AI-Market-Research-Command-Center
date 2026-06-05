"""
news_agent.py
-------------
Specialized news intelligence agent.
"""

from agents.base_agent import BaseAgent
from services.news_api_service import NewsAPIService
from services.sentiment_service import SentimentService


class NewsAgent(BaseAgent):
    """
    News intelligence agent.
    """

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def clean_query(self) -> str:
        cleaned = self.query.lower()

        remove_words = [
            "latest", "news", "today", "recent", "current",
            "stock", "price", "share", "ticker", "and"
        ]

        for word in remove_words:
            cleaned = cleaned.replace(word, "")

        cleaned = cleaned.strip()

        return cleaned if cleaned else "technology"

    def fetch_data(self) -> dict:
        news_service = NewsAPIService()
        cleaned_query = self.clean_query()

        news_result = news_service.get_news(cleaned_query)

        if news_result.get("status") == "success":
            sentiment = SentimentService.analyze_articles(
                news_result.get("articles", [])
            )

            news_result["sentiment"] = sentiment

            # Add simple relevance rank
            for index, article in enumerate(
                news_result.get("articles", []),
                start=1
            ):
                article["rank"] = index
                article["relevance"] = max(100 - ((index - 1) * 8), 60)

        return news_result

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "news",
                "status": "error",
                "message": "Invalid news query."
            }

        result = self.fetch_data()
        result["agent"] = "news"

        return result