#!/bin/bash

# Tworkers Agent Setup for Termux with Proot-Distro Sandbox

echo "🚀 Starting Tworkers Setup for Termux..."
echo "This will install an Ubuntu environment via proot-distro for sandboxing."

# === Part 1: Setup Base Termux Environment ===
echo "[1/4] Updating Termux packages and installing proot-distro..."
pkg update -y && pkg upgrade -y
pkg install proot-distro python git -y

# === Part 2: Setup Ubuntu Sandbox ===
DISTRO_NAME="ubuntu-tworkers"
if proot-distro list | grep -q "$DISTRO_NAME"; then
    echo "[2/4] Ubuntu sandbox ('$DISTRO_NAME') already exists. Skipping installation."
else
    echo "[2/4] Installing Ubuntu sandbox ('$DISTRO_NAME')... This may take a few minutes."
    proot-distro install --distro-name "$DISTRO_NAME" ubuntu-22.04
fi

# === Part 3: Deploy Tworkers into the Sandbox ===
echo "[3/4] Deploying Tworkers agent and web UI into the Ubuntu sandbox..."

# A login shell to run commands inside the distro
PD_LOGIN="proot-distro login $DISTRO_NAME --shared-tmp"

# Update Ubuntu and install dependencies inside the proot
$PD_LOGIN -- bash -c "apt-get update && apt-get install -y python3-pip git"

# Copy the Tworkers project directory into the sandbox's /root
# Note: This copies the current state of the folder.
$PD_LOGIN -- bash -c "rm -rf /root/Tworkers && mkdir -p /root/Tworkers"
cp -r ./* $($PD_LOGIN -- bash -c "echo /root/Tworkers")

# Install all Python requirements for agent AND webapp
$PD_LOGIN -- bash -c "cd /root/Tworkers && pip3 install -r requirements.txt"

# === Part 4: Final Instructions ===
echo ""
echo "✅ Tworkers Agent setup is complete!"
echo "--------------------------------------------------"
echo "To run the agent:"
echo "1. Login to the sandbox:"
echo "   proot-distro login $DISTRO_NAME"
echo ""
echo "2. Navigate to the agent directory:"
echo "   cd /root/Tworkers"
echo ""
echo "3. Add your Gemini API key:"
echo "   nano config.json"
echo ""
echo "4. Start the web server:"
echo "   python3 webapp/server.py"
echo ""
echo "Then, open http://localhost:5000 in your browser."
echo "--------------------------------------------------"
