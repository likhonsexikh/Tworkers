from agent.utils import log_action, log_error, save_file
import os

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')

def generate_shell_script(task: str, filename: str) -> str:
    """
    Generates a safe shell script for a given task in Termux and saves it.

    Args:
        task: The description of the task the script should perform.
        filename: The name of the script file (e.g., 'update_packages.sh').

    Returns:
        A message indicating success or failure.
    """
    log_action(f"Received task to generate shell script '{filename}' for: {task}")

    # This is a placeholder for the actual LLM call.
    # In a real implementation, you would use an LLM to generate the script.
    script_content = f"#!/bin/bash\n# Auto-generated script for: {task}\n\necho \"Executing task: {task}\""

    filepath = os.path.join(SCRIPTS_DIR, filename)
    if save_file(filepath, script_content):
        os.chmod(filepath, 0o755) # Make the script executable
        log_action(f"Made script executable: {filepath}")
        return f"Successfully generated and saved script to {filepath}"
    else:
        log_error(f"Failed to save script: {filepath}")
        return f"Error: Failed to generate or save script to {filepath}"
