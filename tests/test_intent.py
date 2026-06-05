import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orchestrator.intent_detector import IntentDetector

def run_tests():
    """
    Runs multiple query tests and compares
    expected vs detected intents.
    """

    test_queries = {
        "Tesla stock price": ["stock"],
        "Latest AI news": ["news"],
        "Trending products": ["product"],
        "Apple stock and news": ["stock", "news"],
        "Bitcoin price today": ["stock"],
        "Top gadgets trending": ["product"]
    }

    print("=" * 60)
    print("INTENT DETECTOR TEST RESULTS")
    print("=" * 60)

    for query, expected in test_queries.items():
        detector = IntentDetector(query)

        # Detect intents
        result = detector.detect()

        # Extract active intents only
        detected = [
            intent
            for intent, is_detected in result.items()
            if is_detected
        ]

        # Pass/fail check
        status = (
            "PASS"
            if set(expected) == set(detected)
            else "FAIL"
        )

        print(f"\nQuery: {query}")
        print(f"Expected: {expected}")
        print(f"Detected: {detected}")
        print(f"Status: {status}")
        print("-" * 60)


if __name__ == "__main__":
    run_tests()