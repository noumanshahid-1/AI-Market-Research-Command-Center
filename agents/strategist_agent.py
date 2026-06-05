"""
strategist_agent.py
-------------------
Advanced strategic synthesis agent.

Purpose:
- Interpret stock momentum
- Interpret news sentiment
- Interpret product demand
- Generate contextual executive insight
"""


class StrategistAgent:
    """
    Converts raw agent outputs into strategic market intelligence.
    """

    @staticmethod
    def _stock_signal(stock_data):
        if not stock_data or stock_data.get("status") != "success":
            return None

        ticker = stock_data.get("ticker", "This asset")
        trend = stock_data.get("trend", "neutral")
        change = float(stock_data.get("price_change", 0))

        if trend == "up":
            return (
                f"{ticker} is showing positive price momentum, "
                f"with a daily gain of ${abs(change)}."
            )

        if trend == "down":
            return (
                f"{ticker} is showing short-term weakness, "
                f"with a daily decline of ${abs(change)}."
            )

        return (
            f"{ticker} is trading in a relatively stable pattern."
        )

    @staticmethod
    def _news_signal(news_data):
        if not news_data or news_data.get("status") != "success":
            return None

        sentiment = (
            news_data.get("sentiment", {})
            .get("label", "neutral")
        )

        articles = news_data.get("articles", [])
        article_count = len(articles)

        if sentiment == "bullish":
            return (
                f"News sentiment is bullish across {article_count} relevant articles, "
                f"suggesting supportive market narrative."
            )

        if sentiment == "bearish":
            return (
                f"News sentiment is bearish across {article_count} relevant articles, "
                f"indicating elevated headline risk."
            )

        return (
            f"News sentiment is mixed across {article_count} relevant articles, "
            f"so the external narrative remains balanced."
        )

    @staticmethod
    def _product_signal(product_data):
        if not product_data or product_data.get("status") != "success":
            return None

        trend = product_data.get("trend", "stable")
        score = float(product_data.get("average_interest", 0))
        products = product_data.get("top_products", [])

        product_text = (
            ", ".join(products[:3])
            if products
            else "leading products"
        )

        if trend == "growing":
            return (
                f"Product demand appears strong with an interest score of {score}. "
                f"Top market movers include {product_text}."
            )

        if trend == "declining":
            return (
                f"Product demand appears to be weakening with an interest score of {score}. "
                f"This category may need closer monitoring."
            )

        return (
            f"Product demand looks stable with an interest score of {score}. "
            f"Key tracked products include {product_text}."
        )

    @staticmethod
    def _risk_signal(stock_data, news_data, product_data):
        """
        Generate simple risk interpretation.
        """

        risks = []

        if stock_data and stock_data.get("trend") == "down":
            risks.append("short-term price pressure")

        if news_data:
            sentiment = (
                news_data.get("sentiment", {})
                .get("label", "neutral")
            )

            if sentiment == "bearish":
                risks.append("negative media sentiment")

            elif sentiment == "neutral":
                risks.append("mixed external news signals")

        if product_data and product_data.get("trend") == "declining":
            risks.append("weakening demand indicators")

        if not risks:
            return (
                "Risk level appears manageable based on the current available signals."
            )

        return (
            "Key risks include "
            + ", ".join(risks)
            + "."
        )

    @staticmethod
    def generate(
        stock_data=None,
        news_data=None,
        product_data=None
    ) -> str:
        """
        Generate advanced executive strategic insight.
        """

        signals = []

        stock_signal = StrategistAgent._stock_signal(stock_data)
        news_signal = StrategistAgent._news_signal(news_data)
        product_signal = StrategistAgent._product_signal(product_data)

        if stock_signal:
            signals.append(stock_signal)

        if news_signal:
            signals.append(news_signal)

        if product_signal:
            signals.append(product_signal)

        if not signals:
            return (
                "Insufficient strategic signals detected. "
                "Try asking about a stock, market trend, product category, or recent news."
            )

        risk_signal = StrategistAgent._risk_signal(
            stock_data,
            news_data,
            product_data
        )

        final_view = (
            "Executive View: "
            + " ".join(signals)
            + " "
            + risk_signal
        )

        return final_view