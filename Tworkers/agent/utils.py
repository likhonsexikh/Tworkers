import os
from datetime import datetime

LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
AGENT_LOG = os.path.join(LOGS_DIR, 'agent.log')
ERROR_LOG = os.path.join(LOGS_DIR, 'errors.log')

def _log(log_file, message):
    """Helper function to write to a log file."""
    os.makedirs(LOGS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def log_action(message):
    """Logs a general agent action."""
    print(message)
    _log(AGENT_LOG, message)

def log_error(message):
    """Logs an error."""
    print(f"ERROR: {message}")
    _log(ERROR_LOG, message)

def save_file(filepath, content):
    """Saves content to a file, creating directories if they don't exist."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        log_action(f"Successfully saved file: {filepath}")
        return True
    except Exception as e:
        log_error(f"Failed to save file {filepath}: {e}")
        return False
