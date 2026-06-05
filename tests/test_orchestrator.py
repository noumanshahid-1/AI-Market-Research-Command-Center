"""
test_orchestrator.py
--------------------
End-to-end system test
"""

from orchestrator.core import Orchestrator


def run_tests():

    queries = [
        "Tesla stock price",
        "Latest AI news",
        "Trending gadgets",
        "Apple stock and latest news"
    ]

    print("=" * 70)
    print("ORCHESTRATOR TEST RESULTS")
    print("=" * 70)

    for query in queries:
        print(f"\nQuery: {query}")

        try:
            system = Orchestrator(query)
            result = system.execute()

            print("Status:", result.get("status"))
            print("Summary:", result.get("summary"))

        except Exception as error:
            print("ERROR:", str(error))

        print("-" * 70)


if __name__ == "__main__":
    run_tests()