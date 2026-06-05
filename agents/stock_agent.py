"""
stock_agent.py
--------------
Smart stock / crypto agent.
"""

from agents.base_agent import BaseAgent
from services.yahoo_finance_service import YahooFinanceService
from services.entity_parser import EntityParser


class StockAgent(BaseAgent):
    """
    Stock intelligence agent.
    """

    def validate_input(self) -> bool:
        return bool(self.query.strip())

    def extract_ticker(self) -> str:
        """
        Extract ticker using shared entity parser.
        """

        return EntityParser.extract_primary_asset(
            self.query
        )

    def fetch_data(self) -> dict:
        """
        Fetch stock/crypto data.
        """

        ticker = self.extract_ticker()

        return YahooFinanceService.get_stock_data(
            ticker
        )

    def process(self) -> dict:
        if not self.validate_input():
            return {
                "agent": "stock",
                "status": "error",
                "message": "Invalid stock query."
            }

        result = self.fetch_data()
        result["agent"] = "stock"

        return result