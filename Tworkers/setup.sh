#!/bin/bash

echo "Starting Tworkers setup..."

# Update and upgrade Termux packages
echo "Updating and upgrading packages..."
pkg update && pkg upgrade -y

# Install essential packages
echo "Installing essential packages..."
pkg install git python nodejs nano curl wget -y

# Install additional development packages
echo "Installing additional development packages..."
pkg install php ruby go rust clang make cmake openssh -y

# Setup storage access
echo "Setting up storage access..."
termux-setup-storage

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create the tworker shortcut
echo "Creating the 'tworker' shortcut..."
echo "python3 \$HOME/Tworkers/agent/agent.py \"\$@\"" > \$PREFIX/bin/tworker
chmod +x \$PREFIX/bin/tworker

echo "Tworkers setup complete!"
echo "You can now run the agent by typing 'tworker' in your terminal."
