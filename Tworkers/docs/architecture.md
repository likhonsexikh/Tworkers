# Architecture Overview

This document describes the technical architecture of the Tworkers AI Agent.

## Core Technology

Tworkers is built using the **Google Agent Development Kit (ADK)** in Python. The ADK provides the core framework for defining and running agents.

## Agent Structure

The system employs a hierarchical, multi-agent structure.

<p align="center">
  <img src="../assets/octodex1.png" alt="Tworkers Architecture" width="400"/>
</p>

### RootAgent

*   **Role**: The central orchestrator.
*   **Model**: Typically a powerful model like `gemini-1.5-pro`.
*   **Function**: It receives all user queries, analyzes the intent, and delegates the task to the most appropriate sub-agent. It does not perform tasks itself, but rather manages the workflow.

### Sub-Agents

These are specialized agents designed for specific tasks.

1.  **ScriptAgent**
    *   **Role**: Generates Termux-compatible shell scripts.
    *   **Tools**: Uses the `ShellScriptTool` to write and save the generated script files to the `/scripts` directory.

2.  **WebsiteAgent**
    *   **Role**: Generates static websites.
    *   **Tools**: Uses the `WebsiteGenerationTool` to create HTML, CSS, and JS files and save them in a new subdirectory within the `/websites` directory.

3.  **NotificationAgent**
    *   **Role**: Sends notifications.
    *   **Tools**: Uses the `TelegramNotificationTool` and `XNotificationTool` to interact with external messaging APIs.

## Tooling

Each sub-agent is equipped with one or more tools. A tool is a Python function that gives the agent the ability to interact with the environment (e.g., write a file, call an API). All tools are defined in the `agent/tools/` directory.

## Data Flow

1.  User runs `tworker "query"`.
2.  The `agent.py` script starts and passes the query to the `RootAgent`.
3.  `RootAgent` decides which sub-agent should handle the query (e.g., `ScriptAgent`).
4.  `RootAgent` invokes the chosen sub-agent with the original query.
5.  The sub-agent uses its LLM and available tools to perform the task.
6.  The result (e.g., a path to a new script) is returned up the chain.

### Frontend: Xterm.js Terminal Interface

To provide a powerful and user-friendly experience, Tworkers uses a web-based terminal built with **Xterm.js**.

#### Why Xterm.js?

Xterm.js is a front-end component written in TypeScript that allows us to embed a fully-featured terminal emulator directly in the browser. It was chosen for its performance, rich feature set, and widespread adoption in professional development tools like **Microsoft Visual Studio Code**.

Key features include high compatibility, a GPU-accelerated renderer, rich Unicode support, and an extensible API, which we use to implement our custom retro theme.

#### Stability and Development

Xterm.js is generally stable. For advanced testing of new features or bug fixes, beta builds are available. For details on how to set up a development environment with these beta builds, please see our **[Contribution Guide](../CONTRIBUTING.md)**.

#### License and Attribution

Tworkers gratefully acknowledges the work of the Xterm.js authors. For detailed copyright and license information, please see the **[NOTICE.md](../NOTICE.md)** file in the root of this project.
