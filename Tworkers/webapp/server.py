from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sys
import os
import logging

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# This is crucial to allow the server to import the 'agent' module from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import the refactored inference function
    from agent.agent import run_inference
    logger.info("Successfully imported agent inference function.")
except ImportError as e:
    logger.error(f"Could not import the agent. Make sure agent/agent.py is structured correctly. Details: {e}")
    sys.exit(1)

app = Flask(__name__)
# In a production environment, you should set a secret key.
app.config['SECRET_KEY'] = 'a_very_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    """Serves the main HTML page that hosts the terminal."""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handles a new client connection."""
    logger.info("Web client connected")
    emit('agent_response', {'output': '[Connection established with Tworkers backend]\r\n'})

@socketio.on('user_input')
def handle_user_input(data):
    """
    Receives input from the user's terminal, runs the agent,
    and sends the response back.
    """
    prompt = data.get('input', '').strip()
    if not prompt:
        return

    logger.info(f"Received web prompt: '{prompt}'")
    emit('agent_response', {'output': f"\r\n> {prompt}\r\n"}) # Echo user input

    try:
        # Call the refactored agent inference function
        response = run_inference(prompt)
        logger.info(f"Agent response: '{response}'")
        # Emit the whole response at once. For streaming, this would be a loop.
        emit('agent_response', {'output': response})
    except Exception as e:
        error_message = f"An error occurred while running the agent: {e}"
        logger.error(error_message)
        emit('agent_response', {'output': f"\r\n[ERROR] {error_message}"})

if __name__ == '__main__':
    logger.info("Starting Tworkers Flask web server...")
    logger.info("Access the terminal at http://127.0.0.1:5000")
    # Use 0.0.0.0 to make it accessible on your local network (useful for Termux)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
