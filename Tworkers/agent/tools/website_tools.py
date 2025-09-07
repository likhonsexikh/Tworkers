from agent.utils import log_action, log_error, save_file
from google.adk.agents import LlmAgent
import os

WEBSITES_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'websites')

def generate_static_website(description: str, dirname: str) -> str:
    """
    Generates a static website (HTML/CSS/JS) for a given description and saves it.

    Args:
        description: A description of the website to generate.
        dirname: The name of the directory to store the website files (e.g., 'my-portfolio').

    Returns:
        A message indicating success or failure.
    """
    log_action(f"Generating static website for: {description}")

    try:
        # Use a dedicated, single-purpose agent to generate the HTML content
        website_generator_agent = LlmAgent(
            model="gemini-1.5-flash",
            instruction=f"""
You are a web developer that generates a single, self-contained HTML file for a static website.
The HTML file should include inline CSS and JavaScript if necessary.
Do not include any explanations, markdown formatting, or anything other than the raw HTML code.
The code should start with `<!DOCTYPE html>`.

Generate a website for the following description: {description}
""",
        )
        html_content = website_generator_agent.infer(f"Generate the website for the description: {description}")

        if not html_content.strip().lower().startswith("<!doctype html>"):
            log_error("Generated website content is invalid.")
            return "Error: Failed to generate valid HTML."

    except Exception as e:
        log_error(f"LLM call failed during website generation: {e}")
        return f"Error: Could not generate website content due to an API error: {e}"

    site_dir = os.path.join(WEBSITES_DIR, dirname)
    filepath = os.path.join(site_dir, 'index.html')

    if save_file(filepath, html_content):
        return f"Successfully generated and saved website to {filepath}"
    else:
        log_error(f"Failed to save website: {filepath}")
        return f"Error: Failed to generate or save website to {filepath}"
