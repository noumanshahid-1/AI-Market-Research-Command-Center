"""
core.py
-------
Main Super-Agent Orchestrator.
"""

from orchestrator.planner import Planner
from orchestrator.aggregator import Aggregator
from orchestrator.async_runner import AsyncAgentRunner

from agents.stock_agent import StockAgent
from agents.news_agent import NewsAgent
from agents.product_agent import ProductAgent
from agents.comparison_agent import ComparisonAgent
from agents.screener_agent import ScreenerAgent
from agents.heatmap_agent import HeatmapAgent
from agents.multi_asset_agent import MultiAssetAgent


class Orchestrator:
    """
    Main system controller.
    """

    AGENT_MAP = {
        "heatmap": HeatmapAgent,
        "screener": ScreenerAgent,
        "comparison": ComparisonAgent,
        "multi_asset": MultiAssetAgent,
        "stock": StockAgent,
        "news": NewsAgent,
        "product": ProductAgent
    }

    def __init__(self, query: str):
        self.query = query
        self.planner = Planner(query)

    def execute(self) -> dict:
        """
        Execute selected agents and aggregate outputs.
        """

        selected_agents = self.planner.create_plan()

        if not selected_agents:
            selected_agents = ["news"]

        results = AsyncAgentRunner.run(
            agent_plan=selected_agents,
            agent_map=self.AGENT_MAP,
            query=self.query
        )

        return Aggregator.aggregate(results)