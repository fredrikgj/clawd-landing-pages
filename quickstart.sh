#!/bin/bash
# 🚀 Quick Start - Get Traffic Today
# Run this to launch your campaigns

echo "============================================"
echo "  🚀 TRAFFIC CAMPAIGN - QUICK START"
echo "============================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}📊 Current Status:${NC}"
echo "   Sites: ✅ gaudit.io | dentalrecall.io"
echo "   Signups: $(curl -s https://clawd-landing-pages-production.up.railway.app/api/signups | grep -o '"email"' | wc -l)"
echo ""

echo -e "${YELLOW}🎯 ACTION ITEMS (5 min):${NC}"
echo ""
echo "1️⃣  POST ON REDDIT (Most Impact)"
echo "   → Copy from: campaign-feb8.md"
echo "   → Post to: r/googleworkspace, r/sysadmin, r/dentistry"
echo ""
echo "2️⃣  SETUP REDDIT BOT (Automation)"
echo "   → Edit: reddit-bot.py"
echo "   → Add your Reddit API credentials"
echo "   → Run: python3 reddit-bot.py"
echo ""
echo "3️⃣  SUBMIT TO DIRECTORIES"
echo "   → Go to: alternativeto.net/submit/"
echo "   → Submit: gaudit.io"
echo ""
echo "4️⃣  LINKEDIN"
echo "   → Copy from: campaign-feb8.md"
echo "   → Post your building-in-public story"
echo ""

echo -e "${GREEN}📁 FILES:${NC}"
ls -la *.md *.py 2>/dev/null | awk '{print "   " $9}'

echo ""
echo -e "${BLUE}🔗 QUICK LINKS:${NC}"
echo "   Railway: https://railway.app/project/..."
echo "   GitHub:  https://github.com/fredrikgj/clawd-landing-pages"
echo ""

echo "============================================"
echo "  💪 LET'S GET TRAFFIC!"
echo "============================================"
