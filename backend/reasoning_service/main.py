import os
from flask import Flask, request, jsonify
from jinja2 import Environment, FileSystemLoader
import requests

app = Flask(__name__)

# --- Setup Jinja2 Environment ---
prompt_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
prompt_env = Environment(loader=FileSystemLoader(prompt_dir))

EXECUTION_SERVICE_URL = "http://localhost:5003"

def get_rendered_prompt(template_name: str, context: dict) -> str:
    """Renders a Jinja2 template with the given context."""
    try:
        template = prompt_env.get_template(template_name)
        return template.render(context)
    except Exception as e:
        print(f"Error rendering template {template_name}: {e}")
        return f"Error: Could not render prompt template. Details: {e}"

@app.route('/orchestrate', methods=['POST'])
def orchestrate():
    """
    Receives a prompt, generates a plan (mocked), and sends it to the
    execution service to be carried out.
    """
    data = request.get_json()
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # In a real implementation, we would call the LLM here.
    # For now, we generate a fixed, mocked plan.
    mock_plan = {
        "plan": [
            {"service": "filesystem_server", "endpoint": "/write", "method": "POST", "body": {"path": "example.txt", "content": "Hello from Tworkers!"}},
            {"service": "filesystem_server", "endpoint": "/read", "method": "GET", "params": {"path": "example.txt"}},
        ]
    }

    try:
        # Forward the plan to the execution service
        response = requests.post(f"{EXECUTION_SERVICE_URL}/execute", json=mock_plan)
        response.raise_for_status()
        # Return the final result from the execution service to the API gateway
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect to execution service: {e}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
