from agent.utils import log_action, log_error
import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')

def _get_api_key(service_name):
    """Retrieves an API key from the config file."""
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        key = config.get(f"{service_name}_api_key")
        if not key or key.startswith("YOUR_"):
            log_error(f"{service_name.capitalize()} API key not configured in config.json.")
            return None
        return key
    except FileNotFoundError:
        log_error(f"Configuration file not found at {CONFIG_PATH}")
        return None
    except json.JSONDecodeError:
        log_error(f"Error decoding JSON from {CONFIG_PATH}")
        return None

def send_telegram_notification(message: str, chat_id: str) -> str:
    """
    Sends a message to a specific Telegram chat.

    Args:
        message: The message content to send.
        chat_id: The ID of the Telegram chat to send the message to.

    Returns:
        A message indicating success or failure.
    """
    log_action(f"Attempting to send Telegram notification to chat_id {chat_id}")
    api_key = _get_api_key("telegram")
    if not api_key:
        return "Error: Telegram API key not configured."

    # Placeholder for actual API call
    log_action("Mocked Telegram notification sent successfully.")
    return "Mocked notification sent successfully."

def post_x_notification(message: str) -> str:
    """
    Posts a notification (tweet) to X (formerly Twitter).

    Args:
        message: The content of the tweet.

    Returns:
        A message indicating success or failure.
    """
    log_action(f"Attempting to post notification to X.")
    api_key = _get_api_key("x")
    if not api_key:
        return "Error: X API key not configured."

    # Placeholder for actual API call
    log_action(f"Mocked X notification posted: '{message}'")
    return "Mocked X notification posted successfully."
