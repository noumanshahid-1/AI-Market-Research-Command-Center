"""
aggregator.py
-------------
Combines outputs into structured response.
"""

from typing import List, Dict
from agents.strategist_agent import StrategistAgent


class Aggregator:
    """
    Aggregates multiple agent outputs.
    """

    @staticmethod
    def aggregate(results: List[Dict]) -> dict:
        final_response = {
            "status": "success",
            "stock": None,
            "news": None,
            "product": None,
            "comparison": None,
            "multi_asset": None,
            "screener": None,
            "heatmap": None,
            "summary": "",
            "strategy": ""
        }

        summary_parts = []

        for result in results:
            agent_type = result.get("agent")

            if agent_type == "multi_asset":
                final_response["multi_asset"] = result

                if result.get("status") == "success":
                    assets = result.get("assets", [])

                    asset_text = ", ".join(
                        [
                            f"{asset['ticker']} at ${asset['current_price']}"
                            for asset in assets
                        ]
                    )

                    summary_parts.append(
                        f"Multi-asset view ready: {asset_text}."
                    )

            elif agent_type == "heatmap":
                final_response["heatmap"] = result

                if result.get("status") == "success":
                    assets = result.get("assets", [])
                    title = result.get("sector_title", "Sector Heatmap")

                    positives = [
                        asset for asset in assets
                        if asset.get("daily_change_percent", 0) > 0
                    ]

                    summary_parts.append(
                        f"{title} ready: {len(positives)}/{len(assets)} tracked assets are positive today."
                    )

            elif agent_type == "screener":
                final_response["screener"] = result

                if result.get("status") == "success":
                    assets = result.get("assets", [])
                    title = result.get("basket_title", "Market Screener")

                    if assets:
                        leader = assets[0]

                        summary_parts.append(
                            f"{title} ready: {leader['ticker']} currently leads with a momentum score of {leader.get('momentum_score', 0)}/100."
                        )

            elif agent_type == "comparison":
                final_response["comparison"] = result

                if result.get("status") == "success":
                    assets = [
                        asset for asset in result.get("assets", [])
                        if asset.get("status") == "success"
                    ]

                    if len(assets) == 2:
                        left = assets[0]
                        right = assets[1]

                        summary_parts.append(
                            f"Comparison ready: {left['ticker']} is at ${left['current_price']} with a {left['trend']} trend, while {right['ticker']} is at ${right['current_price']} with a {right['trend']} trend."
                        )

            elif agent_type == "stock":
                final_response["stock"] = result

                if result.get("status") == "success":
                    summary_parts.append(
                        f"{result['ticker']} is currently at ${result['current_price']} with a {result['trend']} trend."
                    )

            elif agent_type == "news":
                final_response["news"] = result

                if result.get("status") == "success":
                    article_count = len(
                        result.get("articles", [])
                    )

                    sentiment_label = (
                        result.get("sentiment", {})
                        .get("label", "neutral")
                    )

                    summary_parts.append(
                        f"Found {article_count} high-relevance news articles with overall {sentiment_label} sentiment."
                    )

            elif agent_type == "product":
                final_response["product"] = result

                if result.get("status") == "success":
                    summary_parts.append(
                        f"Product trend appears {result['trend']} with an average interest score of {result['average_interest']}."
                    )

        if not summary_parts:
            final_response["status"] = "error"
            final_response["summary"] = (
                "No meaningful market data could be gathered."
            )
            return final_response

        final_response["summary"] = " ".join(summary_parts)

        final_response["strategy"] = StrategistAgent.generate(
            stock_data=final_response["stock"],
            news_data=final_response["news"],
            product_data=final_response["product"]
        )

        return final_response