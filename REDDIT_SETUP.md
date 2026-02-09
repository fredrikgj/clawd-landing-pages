# Reddit Automation Setup Guide

## Option 1: Run the Bot (Python)

### Step 1: Get Reddit API Credentials

1. Go to **https://www.reddit.com/prefs/apps**
2. Click **"Create Application"** → Select **"script"**
3. Fill in:
   - **name:** GaudiBot
   - **App type:** script
   - **description:** Bot for posting gaudit.io
   - **about uri:** https://github.com/fredrikgj/clawd-landing-pages
   - **redirect uri:** http://localhost:8080
4. Click **"Create app"**
5. Copy:
   - **client ID** (under the app name)
   - **client secret** (click "secret")

### Step 2: Configure the Bot

```bash
cd /home/particle/.openclaw/workspace
nano reddit-bot.py
```

Replace these lines with your credentials:
```python
REDDIT_CONFIG = {
    "client_id": "YOUR_CLIENT_ID",        # Paste here
    "client_secret": "YOUR_CLIENT_SECRET",  # Paste here
    "username": "YOUR_REDDIT_USERNAME",
    "password": "YOUR_REDDIT_PASSWORD",
    ...
}
```

### Step 3: Run the Bot

```bash
# One-time run
python3 reddit-bot.py

# Run in background (with cron)
nohup python3 reddit-bot.py > reddit-bot.log 2>&1 &
```

### Step 4: Schedule Automatic Posts

```bash
# Add to crontab
crontab -e

# Add this line to run bot every hour
0 * * * * cd /home/particle/.openclaw/workspace && python3 reddit-bot.py >> /home/particle/.openclaw/workspace/bot.log 2>&1
```

---

## Option 2: Use IFTTT (No Coding)

### Connect Reddit to Auto-Post

1. Go to **https://ifttt.com**
2. Create account (free)
3. **Create Applet**:
   - **IF** "RSS Feed updates" → Enter: `https://gaudit.io/feed.xml` (create this!)
   - **THEN** "Reddit" → "Submit a new link post"

### Alternative: Use Buffer/Hootsuite

1. **Buffer** (buffer.com) - Free tier, schedule posts
2. Connect Reddit account
3. Queue posts from `campaign-feb8.md`

---

## Quick Setup (5 min)

### For Reddit:
1. Create Reddit app → 2 min
2. Edit `reddit-bot.py` with credentials → 1 min
3. Run `python3 reddit-bot.py` → 1 min

### For LinkedIn:
LinkedIn API is restricted. Use:
- **OpenSocial.app** (free)
- **Buffer** (has LinkedIn)
- Manual posting (copy from `campaign-feb8.md`)

---

## Verification

Check if posts were made:
```bash
cat /home/particle/.openclaw/workspace/posted_posts.json
```

Check Railway for traffic:
```bash
curl https://clawd-landing-pages-production.up.railway.app/api/signups
```

---

## Troubleshooting

**"HTTP 403"**: Wait 10-15 min after creating Reddit app

**"Rate limited"**: Reddit allows 1 post per 10 min per subreddit

**"Invalid credentials"**: Double-check client_id and client_secret
