#!/bin/bash
# deploy.sh: Pull latest code and restart data pipeline
# Place this script on your VM in your project directory

echo "Pulling latest code from main..."
git pull origin main

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Restarting data pipeline..."
# Replace the following line with your actual pipeline start command
pkill -f main.py || true
nohup python main.py &

echo "Deployment complete."
