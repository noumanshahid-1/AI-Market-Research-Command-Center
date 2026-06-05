"""
screener_agent.py
-----------------
Market screener agent for grouped stock intelligence.

Purpose:
- Top AI stocks
- Semiconductor stocks
- EV stocks
- Crypto assets
"""

from agents.base_agent import BaseAgent
from services.yahoo_finance_service import YahooFinanceService


class ScreenerAgent(BaseAgent):
    """
    Screens predefined market baskets.
    """

    BASKETS = {
        "ai": {
            "title": "Top AI Stocks",
            "tickers": ["NVDA", "MSFT", "GOOGL", "META", "AMD"]
        },
        "semiconductor": {
            "title": "Top Semiconductor Stocks",
            "tickers": ["NVDA", "AMD", "INTC", "TSM", "AVGO"]
        },
        "ev": {
            "title": "Top EV Stocks",
            "tickers": ["TSLA", "RIVN", "LCID", "NIO", "BYDDF"]
        },
        "crypto": {
            "title": "Top Crypto Assets",
            "tickers": ["BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "DOGE-USD"]
        }
    }

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def detect_basket(self) -> dict:
        """
        Detect which basket should be screened.
        """

        query = self.query.lower()

        if "semiconductor" in query or "chip" in query:
            return self.BASKETS["semiconductor"]

        if "ev" in query or "electric vehicle" in query:
            return self.BASKETS["ev"]

        if "crypto" in query or "bitcoin" in query:
            return self.BASKETS["crypto"]

        return self.BASKETS["ai"]

    def score_asset(self, asset_data: dict) -> int:
        """
        Smarter momentum score using daily and weekly movement.
        """

        if asset_data.get("status") != "success":
            return 0

        score = 50

        trend = asset_data.get("trend", "neutral")
        daily_percent = float(asset_data.get("daily_change_percent", 0))
        weekly_percent = float(asset_data.get("weekly_change_percent", 0))

        # Daily movement signal
        if daily_percent > 2:
            score += 18
        elif daily_percent > 0.5:
            score += 12
        elif daily_percent > 0:
            score += 6
        elif daily_percent < -2:
            score -= 18
        elif daily_percent < -0.5:
            score -= 12
        elif daily_percent < 0:
            score -= 6

        # Weekly movement signal
        if weekly_percent > 5:
            score += 20
        elif weekly_percent > 2:
            score += 14
        elif weekly_percent > 0:
            score += 7
        elif weekly_percent < -5:
            score -= 20
        elif weekly_percent < -2:
            score -= 14
        elif weekly_percent < 0:
            score -= 7

        # Trend confirmation
        if trend == "up":
            score += 5
        elif trend == "down":
            score -= 5

        return max(0, min(100, round(score)))

    def fetch_data(self) -> dict:
        """
        Fetch all basket assets and rank by momentum score.
        """

        basket = self.detect_basket()
        results = []

        for ticker in basket["tickers"]:
            data = YahooFinanceService.get_stock_data(ticker)

            if data.get("status") == "success":
                data["momentum_score"] = self.score_asset(data)
                results.append(data)

        results = sorted(
            results,
            key=lambda item: item.get("momentum_score", 0),
            reverse=True
        )

        return {
            "status": "success",
            "basket_title": basket["title"],
            "assets": results
        }

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "screener",
                "status": "error",
                "message": "Invalid screener query."
            }

        result = self.fetch_data()
        result["agent"] = "screener"

        return result