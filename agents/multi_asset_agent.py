"""
multi_asset_agent.py
--------------------
Handles queries containing multiple assets without explicit comparison.

Example:
- Apple stock and Bitcoin price today
- Tesla and Nvidia stock
"""

from agents.base_agent import BaseAgent
from services.yahoo_finance_service import YahooFinanceService
from services.entity_parser import EntityParser


class MultiAssetAgent(BaseAgent):
    """
    Multi-asset intelligence agent.
    """

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def fetch_data(self) -> dict:
        """
        Fetch multiple detected assets.
        """

        tickers = EntityParser.extract_assets(
            self.query
        )

        tickers = list(dict.fromkeys(tickers))

        if len(tickers) < 2:
            return {
                "status": "error",
                "message": "Could not detect multiple assets."
            }

        results = []

        for ticker in tickers[:4]:
            data = YahooFinanceService.get_stock_data(
                ticker
            )

            if data.get("status") == "success":
                results.append(data)

        if not results:
            return {
                "status": "error",
                "message": "No valid asset data found."
            }

        return {
            "status": "success",
            "assets": results
        }

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "multi_asset",
                "status": "error",
                "message": "Invalid multi-asset query."
            }

        result = self.fetch_data()
        result["agent"] = "multi_asset"

        return result