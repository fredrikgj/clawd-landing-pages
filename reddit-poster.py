#!/usr/bin/env python3
"""
Reddit Poster - Copy this to your local machine and run
Requires: pip3 install requests
Usage: python3 reddit_poster.py
"""

import requests
import json

# EDIT THESE:
REDDIT_USERNAME = "your_reddit_username"
REDDIT_PASSWORD = "your_reddit_password"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

# Posts to make
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
    }
]

def post_to_reddit(post):
    """Post to Reddit using API"""
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    data = {
        "grant_type": "password",
        "username": REDDIT_USERNAME,
        "password": REDDIT_PASSWORD
    }
    headers = {"User-Agent": "GaudiApp/1.0"}
    
    try:
        r = requests.post("https://www.reddit.com/api/v1/access_token", 
                         auth=auth, data=data, headers=headers)
        token = r.json()["access_token"]
        headers["Authorization"] = f"bearer {token}"
        
        # Post
        payload = {
            "sr": post["subreddit"],
            "title": post["title"],
            "text": post["text"],
            "kind": "self"
        }
        response = requests.post("https://oauth.reddit.com/api/submit", 
                                headers=headers, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    print("Reddit Poster - Fill in your credentials at the top of this file")
    print("1. Go to https://www.reddit.com/prefs/apps")
    print("2. Create a 'script' app")
    print("3. Copy client_id and client_secret")
    print("\nPosts prepared:")
    for p in POSTS:
        print(f"  - r/{p['subreddit']}: {p['title']}")
