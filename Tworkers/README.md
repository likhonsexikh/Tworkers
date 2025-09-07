# Tworkers 🤖 (Termux Edition)

An AI agent powered by Google's ADK, designed to run securely in a sandboxed Ubuntu environment on Termux.

### ✨ Features

-   **Termux-Native:** No Docker required. Uses `proot-distro` for a userland sandbox.
-   **Security First:** All file and command operations are sandboxed within a guest Ubuntu OS and controlled by a secure API layer.
-   **API-Driven Tools:** The AI agent cannot directly access the system. It uses hardened API endpoints for all actions, preventing unsafe behavior.
-   **Web Interface:** A clean, browser-based UI to interact with the agent and view the sandboxed file system.

---

### 🚀 Installation in Termux

This script will automatically set up a sandboxed Ubuntu environment and install the Tworkers agent inside it.

1.  **Clone the repository in Termux:**
    ```bash
    pkg install git -y
    git clone https://github.com/likhonsexikh/Tworkers.git
    cd Tworkers
    ```

2.  **Run the setup script:**
    This will install all dependencies, create the Ubuntu sandbox, and deploy the agent.
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

---

### ⚙️ How to Run

After the setup is complete, follow these steps:

1.  **Login to the Sandbox:**
    ```bash
    proot-distro login ubuntu-tworkers
    ```

2.  **Navigate to the Agent Directory:**
    ```bash
    cd /root/Tworkers
    ```

3.  **Add Your API Key:**
    Open `config.json` with a text editor and add your Gemini API key.
    ```bash
    nano config.json
    ```

4.  **Start the Web Server:**
    ```bash
    python3 webapp/server.py
    ```

5.  **Access the Interface:**
    Open your phone's web browser and navigate to `http://localhost:5000`.

---

### 🏛️ Architecture

Tworkers runs a Flask web server inside a `proot-distro` Ubuntu instance. The ADK-based AI agent is loaded by the server. When a user sends a prompt through the web UI, the agent reasons and decides which tools to use. These "tools" are secure Python functions that perform the requested actions strictly within the sandboxed environment.
