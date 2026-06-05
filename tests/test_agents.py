"""
test_agents.py
--------------
Basic agent execution tests.
"""
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.stock_agent import StockAgent
from agents.news_agent import NewsAgent
from agents.product_agent import ProductAgent

def run_tests():
    agents = [
        StockAgent("Tesla stock"),
        NewsAgent("AI news"),
        ProductAgent("smartphones")
    ]

    for agent in agents:
        print(f"Testing {agent.__class__.__name__}")
        result = agent.process()
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    run_tests()