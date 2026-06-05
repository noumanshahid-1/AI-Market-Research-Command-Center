"""
helpers.py
-----------
Utility helper functions used across the project.

Purpose:
- Query cleaning
- Keyword matching
- Safe formatting
- Shared reusable logic
"""

import re
from typing import List


def clean_query(query: str) -> str:
    """
    Clean and normalize user query.

    Example:
    ' Tesla STOCK Price!!! ' -> 'tesla stock price'
    """
    if not query:
        return ""

    # Lowercase
    query = query.lower()

    # Remove special characters
    query = re.sub(r"[^a-zA-Z0-9\s]", "", query)

    # Remove extra spaces
    query = " ".join(query.split())

    return query


def contains_keywords(query: str, keywords: List[str]) -> bool:
    """
    Check if query contains any keyword from a category.

    Args:
        query (str)
        keywords (List[str])

    Returns:
        bool
    """
    return any(keyword.lower() in query.lower() for keyword in keywords)


def format_currency(value: float) -> str:
    """
    Format number as USD currency.

    Example:
    1500.5 -> $1,500.50
    """
    try:
        return f"${value:,.2f}"
    except (ValueError, TypeError):
        return "N/A"


def safe_get(dictionary: dict, key: str, default=None):
    """
    Safely get dictionary value.

    Prevents KeyError crashes.
    """
    return dictionary.get(key, default)