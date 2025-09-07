from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# In a real system, this would be a service discovery mechanism
TOOL_SERVER_URLS = {
    "filesystem_server": "http://localhost:5002",
    # "playwright_server": "http://localhost:5004", # etc.
}

@app.route('/execute', methods=['POST'])
def execute():
    """
    Receives a plan and executes each step by calling the appropriate tool server.
    """
    data = request.get_json()
    plan = data.get('plan')

    if not plan or not isinstance(plan, list):
        return jsonify({"error": "A valid 'plan' array is required"}), 400

    execution_results = []
    for step in plan:
        service_name = step.get("service")
        endpoint = step.get("endpoint")
        method = step.get("method", "GET")

        if not all([service_name, endpoint]):
            execution_results.append({"error": "Each step must have a 'service' and 'endpoint'"})
            continue

        base_url = TOOL_SERVER_URLS.get(service_name)
        if not base_url:
            execution_results.append({"error": f"Unknown service: {service_name}"})
            continue

        url = f"{base_url}{endpoint}"

        try:
            if method.upper() == 'POST':
                response = requests.post(url, json=step.get("body"))
            else: # Default to GET
                response = requests.get(url, params=step.get("params"))

            response.raise_for_status()
            execution_results.append(response.json())

        except requests.exceptions.RequestException as e:
            execution_results.append({"error": f"Failed to execute step on {service_name}: {e}"})

    return jsonify({"execution_summary": execution_results})


if __name__ == '__main__':
    # This service runs on its own port
    app.run(host='0.0.0.0', port=5003, debug=True)
