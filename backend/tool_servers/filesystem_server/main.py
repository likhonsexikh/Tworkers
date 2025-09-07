import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# This would be the root of the secure sandbox for this server
SANDBOX_PATH = os.environ.get("TWORKERS_SANDBOX_PATH", "/tmp/tworkers_sandbox")

def _get_safe_path(path: str) -> str | None:
    """
    Resolves a relative path to an absolute path inside the sandbox.
    Returns None if the path is unsafe.
    """
    base_path = os.path.abspath(SANDBOX_PATH)
    full_path = os.path.abspath(os.path.join(base_path, path))

    if os.path.commonpath([base_path, full_path]) != base_path:
        return None

    return full_path

@app.route('/write', methods=['POST'])
def write_file():
    data = request.get_json()
    path = data.get('path')
    content = data.get('content')

    if not all([path, content]):
        return jsonify({"error": "path and content are required"}), 400

    safe_path = _get_safe_path(path)
    if not safe_path:
        return jsonify({"error": "Path is outside the allowed sandbox directory."}), 403

    try:
        os.makedirs(os.path.dirname(safe_path), exist_ok=True)
        with open(safe_path, 'w') as f:
            f.write(content)
        return jsonify({"success": True, "message": f"Wrote {len(content)} bytes to {path}"})
    except Exception as e:
        return jsonify({"error": f"Failed to write file: {e}"}), 500

@app.route('/read', methods=['GET'])
def read_file():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "path is required"}), 400

    safe_path = _get_safe_path(path)
    if not safe_path:
        return jsonify({"error": "Path is outside the allowed sandbox directory."}), 403

    try:
        with open(safe_path, 'r') as f:
            content = f.read()
        return jsonify({"success": True, "content": content})
    except FileNotFoundError:
        return jsonify({"error": f"File not found: {path}"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to read file: {e}"}), 500

if __name__ == '__main__':
    # This service runs on its own port
    app.run(host='0.0.0.0', port=5002, debug=True)
