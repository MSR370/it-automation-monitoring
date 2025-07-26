#!/bin/bash

# Get the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Go to the project root (one level up)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$PROJECT_ROOT/logs"

# Ensure logs folder exists
mkdir -p "$LOG_DIR"

# Log file with current date
LOG_FILE="$LOG_DIR/$(date +%F).log"
{
echo "-----System Information-----"
echo "Date and Time: $(date)"
echo ""

#CPU usage
echo "CPU Usage:"
top -l 1 | grep "CPU"
echo ""

# Memory usage
echo "Memory Usage:"
vm_stat | grep "pages active"
vm_stat | grep "pages free"
echo ""

# Disk usage
echo "Disk Usage:"
df -h /
echo ""

#Uptime
echo "Uptime:"
Uptime
echo "_______________"
} >> "$LOG_FILE"

# Print the log file path
echo "System information logged to: $LOG_FILE"