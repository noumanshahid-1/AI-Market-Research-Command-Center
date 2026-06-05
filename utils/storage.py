"""
storage.py
----------
Simple local JSON storage utilities.

Purpose:
- Persist watchlist
- Persist search history
"""

import json
import os


DATA_DIR = "data"
WATCHLIST_FILE = os.path.join(DATA_DIR, "watchlist.json")
HISTORY_FILE = os.path.join(DATA_DIR, "search_history.json")


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def load_json_list(file_path: str) -> list:
    ensure_data_dir()

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except Exception:
        return []


def save_json_list(file_path: str, data: list):
    ensure_data_dir()

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_watchlist() -> list:
    return load_json_list(WATCHLIST_FILE)


def save_watchlist(watchlist: list):
    save_json_list(WATCHLIST_FILE, watchlist)


def load_search_history() -> list:
    return load_json_list(HISTORY_FILE)


def save_search_history(history: list):
    save_json_list(HISTORY_FILE, history)