import requests
import time
import json
import os
from datetime import datetime

# Create folder
os.makedirs("data", exist_ok=True)

# API URLs
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Categories
categories = {
    "technology": ["AI", "software", "tech", "code", "cloud", "API", "LLM"],
    "worldnews": ["war", "government", "election", "president"],
    "sports": ["NFL", "NBA", "FIFA"],
    "science": ["research", "NASA", "space"],
    "entertainment": ["movie", "Netflix", "game"]
}

def classify(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word.lower() in title:
                return category
    return "other"

# Fetch top IDs
ids = requests.get(top_stories_url).json()[:50]

data = []

for i, id in enumerate(ids):
    try:
        res = requests.get(item_url.format(id)).json()
        if res:
            data.append({
                "post_id": res.get("id"),
                "title": res.get("title", ""),
                "category": classify(res.get("title", "")),
                "score": res.get("score", 0),
                "num_comments": res.get("descendants", 0),
                "author": res.get("by", ""),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        time.sleep(0.5)
    except:
        continue

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print(f"Collected {len(data)} stories. Saved to {filename}")