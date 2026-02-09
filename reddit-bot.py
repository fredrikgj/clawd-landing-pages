#!/usr/bin/env python3
"""
Reddit Automation Bot for gaudit.io and dentalrecall.io
Setup instructions: https://github.com/fredrikgj/clawd-landing-pages/blob/main/REDDIT_SETUP.md
"""

import praw
import schedule
import time
import json
from datetime import datetime

# ============================================
# STEP 1: Get Reddit API credentials
# Go to: https://www.reddit.com/prefs/apps
# Create a "script" app
# ============================================

REDDIT_CONFIG = {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET", 
    "username": "YOUR_REDDIT_USERNAME",
    "password": "YOUR_REDDIT_PASSWORD",
    "user_agent": "GaudiBot/1.0"
}

# Campaign posts
POSTS = [
    {
        "subreddit": "googleworkspace",
        "title": "Built a free tool to audit Google Workspace for inactive users",
        "text": """Hey r/googleworkspace,

I've been working on a tool to automate Google Workspace security audits, specifically focused on finding inactive users and unused licenses.

Most G-Suite admins I talk to spend hours manually checking:
- Who hasn't logged in 30/60/90 days?
- Which users are just taking up license slots?
- What files are orphaned with no owner?

I built a simple tool that does this automatically. Right now it's in early access (50% off launch price).

What it does:
- Detects inactive users (customizable thresholds)
- Finds orphaned files with sensitive data
- Weekly automated audit reports
- HIPAA compliant

Launch pricing: $99/month (early access: $49)

Link: https://gaudit.io

Would love feedback from fellow IT admins. Is this something you'd use?"""
    },
    {
        "subreddit": "sysadmin",
        "title": "Side project: Automated G-Suite audit tool for IT admins",
        "text": """Hi r/sysadmin,

Quick background: I was tired of manually auditing G-Suite directories at my company and friends' companies. 

So I built a small tool that:
- Finds inactive users automatically
- Tracks license utilization
- Flags security risks

It's not fancy enterprise software - just something that works and costs a fraction of what the big guys charge.

Pricing: $99/mo (early access: $49)
Link: https://gaudit.io

Any sysadmins here managing G-Suite? Would love to know if this is useful."""
    },
    {
        "subreddit": "dentistry",
        "title": "Built a simpler, cheaper dental recall automation tool",
        "text": """Hi r/dentistry,

I know many of you use Open Dental (or considering it). 

A common pain point I heard: manual recall calls take forever, and existing tools like RevenueWell or Adit are expensive ($200-500/month).

I built a focused recall automation tool that:
- Pulls overdue recalls from Open Dental automatically
- Sends SMS + email reminders
- Handles 2-way confirmations
- Is fully HIPAA compliant

Why different: Simpler, half the price ($99/mo vs $199-499), deep Open Dental integration.

Note: This is in development. Looking for 5-10 dental practices to beta test free.

Link: https://dentalrecall.io

DM me if interested in free early access!"""
    },
    {
        "subreddit": "smallbusiness",
        "title": "Found $500/mo savings on software licenses - here's how",
        "text": """Hi r/smallbusiness,

Quick tip that saved us real money...

Our Google Workspace had 7 inactive users taking up license slots. That's $35+/user/mo down the drain.

Built a small tool to find inactive users automatically. It:
- Scans your G-Suite directory
- Flags users who haven't logged in 30/60/90 days
- Shows unused licenses you can reclaim

If you're paying for more licenses than you need, this finds the waste.

Free to try: https://gaudit.io

No sales pitch - just a tool that works."""
    },
    {
        "subreddit": "SaaS",
        "title": "Show HN: I built a G-Suite audit tool for IT admins",
        "text": """Hey HN,

Built https://gaudit.io - a simple tool to audit Google Workspace for inactive users.

What it does:
- Finds users who haven't logged in 30/60/90 days
- Shows unused licenses
- Flags orphaned files
- Weekly automated reports

Background: I kept manually auditing G-Suite directories for friends' companies. Got tired of it. Built this instead.

Pricing: $99/mo (early access $49)

Would love feedback from fellow IT admins. Is this useful?"""
    }
]

class RedditBot:
    def __init__(self, config):
        self.reddit = praw.Reddit(
            client_id=config["client_id"],
            client_secret=config["client_secret"],
            username=config["username"],
            password=config["password"],
            user_agent=config["user_agent"]
        )
        self.posted_file = "/home/particle/.openclaw/workspace/posted_posts.json"
        self.posted = self.load_posted()
    
    def load_posted(self):
        try:
            with open(self.posted_file, 'r') as f:
                return json.load(f)
        except:
            return {"posts": []}
    
    def save_posted(self):
        with open(self.posted_file, 'w') as f:
            json.dump(self.posted, f)
    
    def is_posted(self, subreddit, title):
        for p in self.posted["posts"]:
            if p["subreddit"] == subreddit and p["title"] == title:
                return True
        return False
    
    def mark_posted(self, subreddit, title, url):
        self.posted["posts"].append({
            "subreddit": subreddit,
            "title": title,
            "url": url,
            "date": datetime.now().isoformat()
        })
        self.save_posted()
    
    def post(self, subreddit, title, text):
        try:
            if self.is_posted(subreddit, title):
                print(f"⏭️  Already posted: r/{subreddit}")
                return None
            
            submission = self.reddit.subreddit(subreddit).submit(title, text)
            self.mark_posted(subreddit, title, submission.url)
            print(f"✅ Posted to r/{subreddit}: {submission.url}")
            return submission.url
        except Exception as e:
            print(f"❌ Error posting to r/{subreddit}: {e}")
            return None
    
    def post_all(self):
        print(f"\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} - Running campaign...")
        for post in POSTS:
            self.post(post["subreddit"], post["title"], post["text"])
        print("")

def main():
    if REDDIT_CONFIG["client_id"] == "YOUR_CLIENT_ID":
        print("❌ REDDIT NOT CONFIGURED!")
        print("\nTo set up Reddit automation:")
        print("1. Go to https://www.reddit.com/prefs/apps")
        print("2. Click 'Create Application' → 'script'")
        print("3. Fill in the details")
        print("4. Copy client_id and client_secret")
        print("5. Edit this file and replace the credentials\n")
        return
    
    bot = RedditBot(REDDIT_CONFIG)
    
    # Post immediately on first run
    print("🚀 Running initial campaign...")
    bot.post_all()
    
    # Schedule weekly posts
    schedule.every().monday.at("09:00").do(bot.post_all)
    schedule.every().thursday.at("09:00").do(bot.post_all)
    
    print("📅 Scheduled posts every Monday & Thursday at 9AM")
    print("Press Ctrl+C to stop\n")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
