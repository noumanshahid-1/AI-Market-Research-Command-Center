"""
planner.py
----------
Creates execution plan based on detected intents.
"""

from orchestrator.intent_detector import IntentDetector


class Planner:
    """
    Converts detected intents into agent plan.
    """

    def __init__(self, query: str):
        self.query = query
        self.intent_detector = IntentDetector(query)

    def create_plan(self) -> list:
        detected = self.intent_detector.detect()

        selected_agents = []

        # Priority order matters
        if detected.get("heatmap"):
            selected_agents.append("heatmap")
            return selected_agents

        if detected.get("screener"):
            selected_agents.append("screener")
            return selected_agents

        if detected.get("comparison"):
            selected_agents.append("comparison")

            if detected.get("news"):
                selected_agents.append("news")

            return selected_agents

        if detected.get("multi_asset"):
            selected_agents.append("multi_asset")

            if detected.get("news"):
                selected_agents.append("news")

            return selected_agents

        if detected.get("stock"):
            selected_agents.append("stock")

        if detected.get("news"):
            selected_agents.append("news")

        if detected.get("product"):
            selected_agents.append("product")

        return selected_agents