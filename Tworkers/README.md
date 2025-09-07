# Tworkers: Your AI-Powered Termux Assistant

<p align="center">
  <img src="assets/hello.gif" alt="Tworkers Greeting" width="300"/>
</p>

<p align="center">
  <strong>An intelligent agent for Termux that generates scripts, builds websites, and automates tasks, all powered by Google's ADK and Gemini.</strong>
</p>

<p align="center">
  <a href="https://github.com/likhonsexikh/Tworkers/stargazers"><img src="https://img.shields.io/github/stars/likhonsexikh/Tworkers?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/likhonsexikh/Tworkers/network/members"><img src="https://img.shields.io/github/forks/likhonsexikh/Tworkers?style=social" alt="GitHub Forks"></a>
  <a href="https://t.me/likhonsheikh"><img src="https://img.shields.io/badge/Telegram-Likhon%20Sheikh-blue?logo=telegram" alt="Telegram"></a>
  <a href="https://x.com/likhonymous"><img src="https://img.shields.io/badge/X-Likhonymous-black?logo=x" alt="X"></a>
</p>

---

**Tworkers** is a multi-agent AI system designed to run directly on your Android device via [Termux](https://termux.dev/en/). It leverages the Agent Development Kit (ADK) to provide a powerful, extensible, and intelligent assistant that can understand your needs and take action.

## ✨ Features

*   **🤖 Multi-Agent Orchestration**: A `RootAgent` delegates tasks to specialized agents for script generation, website creation, and notifications.
*   **🐚 Script Generation**: Automatically create safe and effective shell scripts for Termux.
*   **🌐 Website Generation**: Generate static HTML/CSS/JS websites from a simple description.
*   **🔔 Smart Notifications**: Send updates to Telegram or X.
*   **🧠 Powered by Gemini**: Utilizes Google's state-of-the-art Gemini models for reasoning and generation.
*   **📦 Local-First**: Runs entirely on your device, but is Cloud-ready for future scaling.
*   **🔧 Extensible**: Easily add new tools, agents, and prompts to expand its capabilities.

## 🚀 Getting Started

### Prerequisites

*   [Termux](https://f-droid.org/en/packages/com.termux/) installed on your Android device.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/likhonsexikh/Tworkers.git
    cd Tworkers
    ```

2.  **Run the setup script:**
    This will install all necessary packages, dependencies, and set up the environment.
    ```bash
    bash setup.sh
    ```

3.  **Configure API Keys:**
    Edit the `config.json` file to add your API keys for Gemini, Telegram, and X.
    ```bash
    nano config.json
    ```

### Usage

You can run Tworkers in two modes:

1.  **Command-Line Mode:**
    Pass your request directly as an argument.
    ```bash
    tworker "create a script to update my packages"
    ```

2.  **Interactive Mode:**
    Start the agent without arguments to enter an interactive shell.
    ```bash
    tworker
    ```
    Then, type your requests at the `Tworkers>` prompt.

### 🚀 Web UI (New!)

Tworkers now includes a web-based terminal interface powered by Xterm.js.

1.  **Install Web Dependencies:**
    The main `setup.sh` script should handle this, but if you've already run it, make sure the new web dependencies are installed:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Web Server:**
    ```bash
    python Tworkers/webapp/server.py
    ```

3.  **Access the Terminal:**
    Open your web browser and navigate to `http://127.0.0.1:5000`. If you are running this in Termux, you can access it from a browser on the same WiFi network by using your phone's local IP address (e.g., `http://192.168.1.10:5000`).

## 🏛️ Architecture

<p align="center">
  <img src="assets/octodex1.png" alt="Tworkers Architecture" width="400"/>
</p>

Tworkers uses a hierarchical agent structure:

*   **RootAgent**: The central orchestrator that analyzes user requests.
*   **ScriptAgent**: Generates shell scripts.
*   **WebsiteAgent**: Builds static websites.
*   **NotificationAgent**: Handles all outgoing notifications.

For more details, please see the [Architecture documentation](docs/architecture.md).

## 📚 Developer Resources

To extend Tworkers or integrate it with other systems, refer to the official **Agent Development Kit (ADK)** documentation.

*   **[ADK API Reference](docs/api_reference.md)**: A centralized hub for Python, Java, CLI, and REST API documentation.

## 🤝 Contributing

Contributions are welcome! Please read our [contributing guidelines](docs/contributing.md) to get started.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <img src="assets/octodex2.png" alt="Octodex" width="200"/>
</p>
