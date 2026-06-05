"""
base_agent.py
-------------
Abstract base class for all specialized agents.

Purpose:
- Standardize structure
- Force validation
- Force process pipeline
"""

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Abstract parent class for all agents.
    """

    def __init__(self, query: str):
        """
        Store user query.
        """
        self.query = query

    @abstractmethod
    def validate_input(self) -> bool:
        """
        Validate user input.
        """
        pass

    @abstractmethod
    def fetch_data(self) -> dict:
        """
        Fetch external or processed data.
        """
        pass

    @abstractmethod
    def process(self) -> dict:
        """
        Main execution pipeline.
        """
        pass