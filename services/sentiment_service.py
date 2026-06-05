"""
sentiment_service.py
--------------------
Rule-assisted sentiment engine.
"""

from textblob.sentiments import PatternAnalyzer


class SentimentService:
    analyzer = PatternAnalyzer()

    POSITIVE_WORDS = [
        "growth", "rises", "surge", "record", "strong", "beats",
        "expansion", "profit", "demand", "innovation", "launch",
        "partnership", "approval", "upgrade", "bullish", "gain",
        "wins", "accelerates", "raises"
    ]

    NEGATIVE_WORDS = [
        "loss", "lawsuit", "decline", "falls", "risk", "layoff",
        "cut", "warning", "delay", "probe", "penalty", "miss",
        "bearish", "drop", "weak", "concern", "tension",
        "slows", "investigation", "ban"
    ]

    @staticmethod
    def analyze_text(text: str) -> dict:
        """
        Analyze sentiment of one text block.
        """

        text = text.lower().strip()

        if not text:
            return {"score": 0.0, "label": "neutral"}

        sentiment_result = SentimentService.analyzer.analyze(text)
        polarity_score = float(sentiment_result[0])

        positive_hits = sum(
            word in text for word in SentimentService.POSITIVE_WORDS
        )

        negative_hits = sum(
            word in text for word in SentimentService.NEGATIVE_WORDS
        )

        polarity_score += positive_hits * 0.08
        polarity_score -= negative_hits * 0.08

        if polarity_score > 0.08:
            label = "bullish"
        elif polarity_score < -0.08:
            label = "bearish"
        else:
            label = "neutral"

        return {
            "score": round(polarity_score, 2),
            "label": label
        }

    @staticmethod
    def analyze_articles(articles: list) -> dict:
        """
        Analyze all articles and attach per-article sentiment.
        """

        if not articles:
            return {"score": 0.0, "label": "neutral"}

        total_score = 0.0

        for article in articles:
            text = (
                f"{article.get('title', '')} "
                f"{article.get('description', '')}"
            )

            sentiment = SentimentService.analyze_text(text)

            article["sentiment"] = sentiment

            total_score += sentiment["score"]

        avg_score = total_score / len(articles)

        if avg_score > 0.08:
            label = "bullish"
        elif avg_score < -0.08:
            label = "bearish"
        else:
            label = "neutral"

        return {
            "score": round(avg_score, 2),
            "label": label
        }