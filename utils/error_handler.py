"""
error_handler.py
----------------
Centralized error handling utilities.

Purpose:
- Prevent crashes
- Standardize error responses
- Improve debugging clarity
"""


def format_error(agent_name: str, error: Exception) -> dict:
    """
    Standardized error response for all agents/services.

    Args:
        agent_name (str): Name of agent/service
        error (Exception): Exception object

    Returns:
        dict
    """
    return {
        "agent": agent_name,
        "status": "error",
        "message": str(error)
    }