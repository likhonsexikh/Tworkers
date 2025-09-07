#!/bin/bash

# This is an example cron script for Tworkers.
# To use it in Termux, you might use the 'termux-job-scheduler' API
# or a package like 'cronie'.

# Example: Run 'tworker' every day at 3 AM to perform a cleanup task.
# 0 3 * * * /data/data/com.termux/files/home/Tworkers/cron/tworker_cron.sh

# Ensure we are running from the project's root directory
# This helps ensure that relative paths to logs, etc., work correctly.
cd "$(dirname "$0")/.." || exit

# The command/query you want to automate
QUERY="Generate a daily summary report and save it to scripts/daily_report.txt"

# Path to the tworker executable
# Note: $PREFIX is a Termux-specific variable. This script assumes a Termux environment.
TWORKER_CMD="$PREFIX/bin/tworker"

# Log file for this cron job
LOG_FILE="logs/cron_jobs.log"

echo "---" >> "$LOG_FILE"
echo "Running scheduled task at $(date)" >> "$LOG_FILE"
"$TWORKER_CMD" "$QUERY" >> "$LOG_FILE" 2>&1
echo "Task finished at $(date)" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"
