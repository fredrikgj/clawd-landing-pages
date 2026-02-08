#!/bin/bash
# Signup Monitor - checks every 30 minutes for new signups
# Run with: while true; do bash monitor-signups.sh; sleep 1800; done

API_URL="https://clawd-landing-pages-production.up.railway.app/api/signups"
LOG_FILE="/home/particle/.openclaw/workspace/signup-log.txt"

echo "=== $(date) ===" >> $LOG_FILE
curl -s $API_URL >> $LOG_FILE
echo "" >> $LOG_FILE

# Also show to stdout
echo "Current signups:"
curl -s $API_URL

# Check for new (simple check - count lines)
TOTAL=$(curl -s $API_URL | grep -o '"email"' | wc -l)
echo ""
echo "Total signups: $TOTAL"
