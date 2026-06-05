"""
news_api_service.py
-------------------
Handles NewsAPI requests.

Purpose:
- Fetch relevant news
- Improve source quality
- Filter noisy sources
- Reduce duplicate headlines
"""

from newsapi import NewsApiClient
from config import NEWS_API_KEY


class NewsAPIService:
    """
    News intelligence service.
    """

    def __init__(self):
        """
        Initialize NewsAPI client.
        """
        self.client = NewsApiClient(api_key=NEWS_API_KEY)

    def get_news(self, query: str) -> dict:
        """
        Fetch cleaner, more relevant news articles.
        """

        try:
            response = self.client.get_everything(
                q=query,
                language="en",
                sort_by="relevancy",
                page_size=15
            )

            # Lower-quality / noisy domains to exclude
            blocked_sources = [
                "pypi.org",
                "slickdeals.net",
                "github.com",
                "reddit.com"
            ]

            articles = []

            # Track duplicate-like headlines
            seen_titles = set()

            # Track overused major themes
            keyword_frequency = {}

            for article in response.get("articles", []):

                if not article.get("title") or not article.get("source"):
                    continue

                source_name = article["source"]["name"].lower()
                title = article["title"].strip()

                # Skip blocked sources
                if any(
                    blocked in source_name
                    for blocked in blocked_sources
                ):
                    continue

                # Exact-ish duplicate prevention
                simplified_title = title.lower()

                if simplified_title in seen_titles:
                    continue

                # Major keyword diversity filter
                major_keywords = [
                    word for word in title.lower().split()
                    if word in [
                        "apple",
                        "tim",
                        "cook",
                        "ceo",
                        "vision",
                        "iphone"
                    ]
                ]

                repetitive = False

                for keyword in major_keywords:
                    if keyword_frequency.get(keyword, 0) >= 2:
                        repetitive = True
                        break

                if repetitive:
                    continue

                # Update trackers
                seen_titles.add(simplified_title)

                for keyword in major_keywords:
                    keyword_frequency[keyword] = (
                        keyword_frequency.get(keyword, 0) + 1
                    )

                articles.append(
                    {
                        "title": title,
                        "source": article["source"]["name"],
                        "url": article.get("url", ""),
                        "description": article.get(
                            "description",
                            "No description available."
                        )
                    }
                )

                if len(articles) == 5:
                    break

            # If nothing useful found
            if not articles:
                return {
                    "status": "error",
                    "message": "No relevant news found."
                }

            return {
                "status": "success",
                "query": query,
                "articles": articles
            }

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }