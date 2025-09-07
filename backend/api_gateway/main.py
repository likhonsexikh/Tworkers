from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# In a real microservice architecture, these would be discovered or loaded from config
REASONING_SERVICE_URL = "http://localhost:5001"

@app.route('/chat', methods=['POST'])
def chat():
    """
    Receives a prompt from the frontend and forwards it to the reasoning service.
    """
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Forward the request to the reasoning service
        response = requests.post(f"{REASONING_SERVICE_URL}/orchestrate", json={"prompt": prompt})
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect to reasoning service: {e}"}), 500

if __name__ == '__main__':
    # Port 5000 will be the main entry point for the frontend
    app.run(host='0.0.0.0', port=5000, debug=True)
