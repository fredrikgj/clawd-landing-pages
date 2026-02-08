#!/bin/bash
# Directory Submission Script
# Submit gaudit.io and dentalrecall.io to free directories

echo "=== Directory Submission Started - $(date) ==="

# List of directories to submit to (free ones)
DIRECTORIES=(
    "https://www.producthunt.com/post/127673"
    "https://alternativeto.net/submit/"
    "https://www.betapage.co/startup/gaudit-io"
    "https://www.capterra.com/free-trial/"
    "https://www.g2.com/products/gaudit-io"
    "https://www.saaslogic.com/submit/"
    "https://www.saasgenius.com/submit/"
    "https://www.saashub.com/submit"
    "https://www.trustpilot.com/business"
    "https://www.similarweb.com/corp/register"
)

echo "Manual submission URLs:"
for url in "${DIRECTORIES[@]}"; do
    echo "  - $url"
done

echo ""
echo "=== Quick Actions ==="
echo "1. Post on Reddit (see campaign-feb8.md)"
echo "2. Post on LinkedIn (see campaign-feb8.md)"
echo "3. Post on Twitter/X (see campaign-feb8.md)"
echo "4. Submit to Product Hunt for launch day"
echo ""
echo "Current signups:"
curl -s https://clawd-landing-pages-production.up.railway.app/api/signups
echo ""
