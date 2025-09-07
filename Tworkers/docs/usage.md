# Usage Guide

This guide explains how to use the Tworkers AI Agent.

## Running the Agent

The `tworker` command is a shortcut to run the agent script. You can use it in two modes.

### 1. Interactive Mode

For an interactive session, run the command without any arguments:

```bash
tworker
```

You will be greeted with a `Tworkers>` prompt. You can type your requests here and press Enter.

**Example Session:**

```
$ tworker
Tworkers> create a script to show my current directory
Agent Response: Delegating to ScriptAgent... Successfully generated script...
Tworkers> exit
$
```

### 2. Command-Line Mode

You can also pass your request directly as a command-line argument. This is useful for single tasks or for use in scripts.

**Example:**

```bash
tworker "generate a portfolio website named 'my-site'"
```

The agent will execute the task and then exit.

## Available Tasks

You can ask Tworkers to perform a variety of tasks, including:

*   **"Create a shell script to..."**: Generates a shell script.
*   **"Generate a website for..."**: Creates a static website.
*   **"Send a Telegram message to..."**: Sends a notification via Telegram.
*   **"Post a tweet saying..."**: Posts a notification to X.

The agent understands natural language, so you can phrase your requests in different ways.
