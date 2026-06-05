"""
logger.py
---------
Simple logging system for debugging and monitoring.

Purpose:
- Track execution
- Debug failures
- Maintain readable logs
"""

import logging
import os


# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message: str):
    """
    Log informational messages.
    """
    logging.info(message)


def log_error(message: str):
    """
    Log error messages.
    """
    logging.error(message)