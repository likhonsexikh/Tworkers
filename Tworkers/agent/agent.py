import argparse
import sys
import os

# Adjust path to make sibling modules importable
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from agent.tools.shell_tools import generate_shell_script
from agent.tools.website_tools import generate_static_website
from agent.tools.notification_tools import send_telegram_notification, post_x_notification
from agent.utils import log_action, log_error

# --- Agent Definition and Instantiation ---
log_action("Initializing Tworkers agent components...")

# --- Sub-Agent Definitions ---
script_agent = LlmAgent(
    model="gemini-1.5-flash",
    name="ScriptAgent",
    description="A specialized agent that generates and saves shell scripts for Termux.",
    instruction="Your task is to generate safe and correct shell scripts based on user requests. Use the provided tool to save the script.",
    tools=[FunctionTool(generate_shell_script)]
)

website_agent = LlmAgent(
    model="gemini-1.5-flash",
    name="WebsiteAgent",
    description="A specialized agent that generates and saves static websites.",
    instruction="Your task is to generate the HTML, CSS, and JS for a static website based on a user's description. Use the provided tool to save the website files.",
    tools=[FunctionTool(generate_static_website)]
)

notification_agent = LlmAgent(
    model="gemini-1.5-flash",
    name="NotificationAgent",
    description="A specialized agent for sending notifications.",
    instruction="Your task is to send notifications to platforms like Telegram or X based on user requests.",
    tools=[
        FunctionTool(send_telegram_notification),
        FunctionTool(post_x_notification)
    ]
)

# --- Root Agent Definition ---
TworkersRootAgent = LlmAgent(
    model="gemini-1.5-pro",
    name="TworkersRootAgent",
    description="The main Tworkers agent that orchestrates tasks by delegating to specialized sub-agents.",
    instruction=(
        "You are the root agent for Tworkers on Termux. Your job is to understand the user's request "
        "and delegate it to the appropriate sub-agent (ScriptAgent, WebsiteAgent, or NotificationAgent). "
        "Clearly state which agent you are delegating to and why. If the request is ambiguous, ask for clarification."
    ),
    sub_agents=[script_agent, website_agent, notification_agent]
)

def run_inference(prompt: str) -> str:
    """
    Runs inference on the TworkersRootAgent with a given prompt.
    This is the main entry point for external scripts like the web server.
    """
    log_action(f"Running inference for prompt: '{prompt}'")
    try:
        # This is a placeholder for the actual inference call.
        # response = TworkersRootAgent.infer(prompt)
        response = f"This is a mocked response for the prompt: '{prompt}'"
        log_action(f"Agent Response: {response}")
        return response
    except Exception as e:
        error_message = f"An error occurred during inference: {e}"
        log_error(error_message)
        return error_message

def main():
    """The main entry point for command-line execution."""
    parser = argparse.ArgumentParser(description="Tworkers AI Agent for Termux")
    parser.add_argument("query", type=str, nargs="*", help="The user's query for the agent.")
    args = parser.parse_args()

    if not args.query:
        # Interactive mode
        log_action("Entering interactive mode. Type 'exit' to quit.")
        while True:
            try:
                query_text = input("Tworkers> ")
                if query_text.lower() in ['exit', 'quit']:
                    break
                if query_text:
                    response = run_inference(query_text)
                    print(f"Agent Response: {response}")
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                break
    else:
        # Command-line mode
        query_text = " ".join(args.query)
        response = run_inference(query_text)
        print(f"Agent Response: {response}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(f"An unexpected error occurred: {e}")
        sys.exit(1)
