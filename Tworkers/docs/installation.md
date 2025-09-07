# Installation Guide

This guide provides detailed instructions for installing Tworkers on Termux.

## Prerequisites

*   An Android device.
*   The [F-Droid app store](https://f-droid.org/) installed on your device.

## Step 1: Install Termux

1.  Open F-Droid on your Android device.
2.  Search for "Termux".
3.  Install the main "Termux" app.
4.  It is also recommended to install the "Termux:API" add-on for extra functionality.

## Step 2: Clone the Tworkers Repository

Open Termux and run the following command:
```bash
pkg install git -y
git clone https://github.com/likhonsexikh/Tworkers.git
```

## Step 3: Run the Setup Script

Navigate into the Tworkers directory and run the setup script. This will install all required packages and dependencies.

```bash
cd Tworkers
bash setup.sh
```

The script will ask for storage permissions. Please grant them.

## Step 4: Configure API Keys

You need to provide your own API keys for the AI models and notification services.

1.  Open the `config.json` file in a text editor like `nano`:
    ```bash
    nano config.json
    ```
2.  Replace the placeholder values (`"YOUR_..._KEY"`) with your actual keys.
3.  Save the file (in `nano`, press `Ctrl+X`, then `Y`, then `Enter`).

## Installation Complete

You are now ready to use Tworkers! See the [Usage Guide](usage.md) for details on how to run the agent.
