from agent.utils import log_action, log_error, save_file
from google.adk.agents import LlmAgent
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
    log_action(f"Generating shell script for task: {task}")

    try:
        # Use a dedicated, single-purpose agent to generate the script content
        script_generator_agent = LlmAgent(
            model="gemini-1.5-flash",
            instruction=f"""
You are a shell script generator for Termux on Android.
Your sole purpose is to generate a clean, safe, and correct shell script that performs a specific task.
Do not include any explanations, markdown formatting, or anything other than the raw script code.
The script should start with `#!/bin/bash`.

Generate a script to perform the following task: {task}
""",
        )
        script_content = script_generator_agent.infer(f"Generate the script for the task: {task}")

        if not script_content.strip().startswith("#!/bin/bash"):
            log_error("Generated script content is invalid.")
            return "Error: Failed to generate a valid script."

    except Exception as e:
        log_error(f"LLM call failed during script generation: {e}")
        return f"Error: Could not generate script content due to an API error: {e}"


    filepath = os.path.join(SCRIPTS_DIR, filename)
    if save_file(filepath, script_content):
        os.chmod(filepath, 0o755) # Make the script executable
        log_action(f"Made script executable: {filepath}")
        return f"Successfully generated and saved script to {filepath}"
    else:
        log_error(f"Failed to save script: {filepath}")
        return f"Error: Failed to generate or save script to {filepath}"
