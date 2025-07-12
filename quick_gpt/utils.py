"""
Utility functions for loading API configuration from environment variables.
"""

import dotenv
import os
from datetime import datetime
import random
import string


def load_config(model_type: str):
    """
    Load API key and base URL from environment variables based on the specified model type.

    Args:
        model_type (str): The type of model to use ("openai" or "gemini").

    Returns:
        tuple: A tuple containing the API key and base URL as strings.

    Raises:
        ValueError: If the model_type is not "openai" or "gemini".
    """
    # you need to write into .env file or ~/.bashrc or ~/.zshrc, etc.
    dotenv.load_dotenv()
    if model_type == "openai":
        return os.getenv("OPENAI_API_KEY"), os.getenv("BASE_URL")

    elif model_type == "gemini":
        return os.getenv("GEMINI_API_KEY"), os.getenv("GOOGLE_GEMINI_BASE_URL")

    else:
        raise ValueError("Error, supports openai and gemini model only.")


def generate_filename() -> str:
    """
    Generate a filename with the current timestamp and a random 6-character string.

    Returns:
        str: The generated filename, e.g., '2024-05-03-12-34-22_g4om0d'
    """
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    rand_str = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{timestamp}_{rand_str}"


if __name__ == "__main__":
    print(load_config(model_type="gemini"))
    print(generate_filename())
