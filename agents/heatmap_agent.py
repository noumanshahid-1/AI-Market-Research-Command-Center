"""
heatmap_agent.py
----------------
Sector heatmap intelligence agent.

Purpose:
- AI sector heatmap
- Semiconductor heatmap
- EV heatmap
- Crypto heatmap
"""

from agents.base_agent import BaseAgent
from services.yahoo_finance_service import YahooFinanceService


class HeatmapAgent(BaseAgent):
    """
    Builds sector-level heatmap data.
    """

    SECTORS = {
        "ai": {
            "title": "AI Sector Heatmap",
            "assets": {
                "NVDA": 35,
                "MSFT": 25,
                "GOOGL": 20,
                "META": 15,
                "AMD": 12
            }
        },
        "semiconductor": {
            "title": "Semiconductor Market Heatmap",
            "assets": {
                "NVDA": 35,
                "AMD": 20,
                "AVGO": 20,
                "TSM": 18,
                "INTC": 12
            }
        },
        "ev": {
            "title": "EV Market Heatmap",
            "assets": {
                "TSLA": 35,
                "RIVN": 14,
                "LCID": 10,
                "NIO": 12,
                "BYDDF": 20
            }
        },
        "crypto": {
            "title": "Crypto Market Heatmap",
            "assets": {
                "BTC-USD": 35,
                "ETH-USD": 28,
                "SOL-USD": 18,
                "BNB-USD": 16,
                "DOGE-USD": 10
            }
        }
    }

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def detect_sector(self) -> dict:
        """
        Detect target sector from query.
        """

        query = self.query.lower()

        if "semiconductor" in query or "chip" in query:
            return self.SECTORS["semiconductor"]

        if "ev" in query or "electric vehicle" in query:
            return self.SECTORS["ev"]

        if "crypto" in query or "bitcoin" in query:
            return self.SECTORS["crypto"]

        return self.SECTORS["ai"]

    def fetch_data(self) -> dict:
        """
        Fetch heatmap assets.
        """

        sector = self.detect_sector()
        assets = []

        for ticker, weight in sector["assets"].items():

            data = YahooFinanceService.get_stock_data(ticker)

            if data.get("status") == "success":

                daily_percent = float(
                    data.get("daily_change_percent", 0)
                )

                if daily_percent > 1:
                    signal = "strong"
                elif daily_percent > 0:
                    signal = "positive"
                elif daily_percent < -1:
                    signal = "weak"
                else:
                    signal = "neutral"

                assets.append(
                    {
                        "ticker": ticker,
                        "weight": weight,
                        "current_price": data.get("current_price"),
                        "daily_change_percent": daily_percent,
                        "weekly_change_percent": data.get(
                            "weekly_change_percent",
                            0
                        ),
                        "trend": data.get("trend"),
                        "signal": signal
                    }
                )

        return {
            "status": "success",
            "sector_title": sector["title"],
            "assets": assets
        }

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "heatmap",
                "status": "error",
                "message": "Invalid heatmap query."
            }

        result = self.fetch_data()
        result["agent"] = "heatmap"

        return result