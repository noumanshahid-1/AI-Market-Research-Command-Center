"""
comparison_agent.py
-------------------
Compares two stocks / crypto assets side-by-side.
"""

from agents.base_agent import BaseAgent
from services.yahoo_finance_service import YahooFinanceService
from services.entity_parser import EntityParser


class ComparisonAgent(BaseAgent):
    """
    Comparison intelligence agent.
    """

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def fetch_data(self) -> dict:
        """
        Fetch two comparison assets.
        """

        assets = EntityParser.extract_comparison_assets(
            self.query
        )

        if len(assets) != 2:
            return {
                "status": "error",
                "message": "Could not detect two assets for comparison."
            }

        left_data = YahooFinanceService.get_stock_data(
            assets[0]
        )

        right_data = YahooFinanceService.get_stock_data(
            assets[1]
        )

        return {
            "status": "success",
            "assets": [
                left_data,
                right_data
            ]
        }

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "comparison",
                "status": "error",
                "message": "Invalid comparison query."
            }

        result = self.fetch_data()
        result["agent"] = "comparison"

        return result