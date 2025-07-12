"""
This module provides functions to manage conversation history using a JSON file.
"""

import json
import os
from typing import List


def load_history(file_path: str) -> List:
    """
    Load conversation history from the specified JSON file.

    Args:
        file_path (str): The path to the JSON file containing the conversation history.

    Returns:
        List: A list of message dictionaries representing the conversation history.
    """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_history(file_path, history):
    """Save conversation history to the JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def append_message(file_path, role, content):
    """
    Append a message to the conversation history and save it to the JSON file.

    Args:
        file_path (str): The path to the JSON file for storing the conversation history.
        role (str): The role of the message sender (e.g., "user", "assistant", "system").
        content (str): The content of the message.

    Returns:
        None
    """
    history: List = load_history(file_path)
    history.append({"role": role, "content": content})
    save_history(file_path, history)


if __name__ == "__main__":
    file_path = "history/2025-07-12-12-18-15_793cdd.json"
    append_message(file_path, "system", "You are a helpful assistant.")
    append_message(file_path, "user", "Hello!")
    append_message(file_path, "assistant", "Hi! How can I help you?")
    print(load_history(file_path))
