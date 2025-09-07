#!/bin/bash

# Tworkers Final Architecture Setup for Termux

echo "🚀 Starting Tworkers Setup..."
echo "This will install an Ubuntu environment via proot-distro for sandboxing."

# === Part 1: Setup Base Termux Environment ===
echo "[1/3] Updating Termux packages and installing proot-distro..."
pkg update -y && pkg upgrade -y
pkg install proot-distro python git -y

# === Part 2: Setup Ubuntu Sandbox ===
DISTRO_NAME="tworkers-final"
if proot-distro list | grep -q "$DISTRO_NAME"; then
    echo "[2/3] Ubuntu sandbox ('$DISTRO_NAME') already exists. Skipping installation."
else
    echo "[2/3] Installing Ubuntu sandbox ('$DISTRO_NAME')... This may take a few minutes."
    proot-distro install --distro-name "$DISTRO_NAME" ubuntu-22.04
fi

# A login shell to run commands inside the distro
PD_LOGIN="proot-distro login $DISTRO_NAME --shared-tmp"

# === Part 3: Deploy Tworkers Backend into the Sandbox ===
echo "[3/3] Deploying Tworkers backend services into the Ubuntu sandbox..."

# Update Ubuntu and install dependencies inside the proot
$PD_LOGIN -- bash -c "apt-get update && apt-get install -y python3-pip git"

# Copy the Tworkers backend directory into the sandbox's /app
$PD_LOGIN -- bash -c "rm -rf /app && mkdir -p /app"
cp -r ./backend/* $($PD_LOGIN -- bash -c "echo /app")

# Install Python requirements inside the sandbox
$PD_LOGIN -- bash -c "cd /app && pip3 install -r requirements.txt"

# === Final Instructions ===
echo ""
echo "✅ Tworkers setup is complete!"
echo "--------------------------------------------------"
echo "To run the system, you will need to start all backend microservices."
echo "We recommend using a tool like 'tmux' to manage multiple sessions."
echo ""
echo "1. Login to the sandbox:"
echo "   proot-distro login $DISTRO_NAME"
echo ""
echo "2. Start the Filesystem Tool Server (Port 5002):"
echo "   (In a new tmux window/pane)"
echo "   cd /app/tool_servers/filesystem_server && python3 main.py"
echo ""
echo "3. Start the Execution Service (Port 5003):"
echo "   (In a new tmux window/pane)"
echo "   cd /app/execution_service && python3 main.py"
echo ""
echo "4. Start the Reasoning Service (Port 5001):"
echo "   (In a new tmux window/pane)"
echo "   cd /app/reasoning_service && python3 main.py"
echo ""
echo "5. Start the API Gateway (Port 5000):"
echo "   (In a new tmux window/pane)"
echo "   cd /app/api_gateway && python3 main.py"
echo ""
echo "The system is now running. The API Gateway at http://localhost:5000 is the main entry point."
echo "--------------------------------------------------"
