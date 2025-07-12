"""
This module provides response functions for interacting with Google Gemini and OpenAI APIs.
"""

# different ways to load response module
import requests
import json

from google import genai
from google.genai import types
from typing import List, Dict


def integrate_message(original_content: str, history: List[Dict[str, str]]):
    """
    Integrate conversation history and the current user input into a single string for model input.

    Args:
        original_content (str): The current user input.
        history (List[Dict[str, str]]): The conversation history, each item is a dict with 'role' and 'content'.

    Returns:
        str: The integrated message string.
    """
    lines = []
    for msg in history:
        # Format: [role]: content
        lines.append(f"{msg['role']}: {msg['content']}")
    # Add the current user input as the last line
    lines.append(f"user: {original_content}")
    return "\n".join(lines)


def _response_google_sdk(
    original_content: str,
    history: List[Dict[str, str]],
    api_key,
    base_url,
    system_prompt=None,
) -> types.GenerateContentResponse:
    """
    Sends a request to the Google Gemini API using the provided content, API key, and base URL.

    Args:
        content (str): The user input or prompt to send to the model.
        api_key (str): The API key for authenticating with the Google Gemini API.
        base_url (str): The base URL for the Google Gemini API endpoint.
        system_prompt (str, optional): The system prompt to guide the model's behavior.

    Returns:
        types.GenerateContentResponse: The response object from the Gemini API.
    """
    content = integrate_message(original_content, history)
    if system_prompt:
        # Prepend system prompt to content, or use as per Gemini API's requirements
        content = f"{system_prompt}\n{content}"

    client = genai.Client(
        api_key=api_key,
        http_options={"base_url": str(base_url).strip()},
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=content,
        config=types.GenerateContentConfig(),
    )

    return response


def _response_openai_sdk(
    content,
    history: List[Dict[str, str]],
    api_key,
    base_url,
    model_name,
    system_prompt=None,
):
    """
    Sends a request to the OpenAI API using the provided content, API key, base URL, and model name.

    Args:
        content (str): The user input or prompt to send to the model.
        api_key (str): The API key for authenticating with the OpenAI API.
        base_url (str): The base URL for the OpenAI API endpoint.
        model_name (str): The name of the OpenAI model to use.
        system_prompt (str, optional): The system prompt to guide the model's behavior.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": content})

    payload = {
        "model": model_name,
        "messages": messages,
    }

    try:
        response = requests.post(base_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Failed to load json files")
    except Exception as e:
        print(f"Error: {e}")
