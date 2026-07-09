"""
Reddit Trend Analyzer - Data Collection Script
Uses PullPush.io (free public mirror of Reddit data) - NO API KEY NEEDED.

HOW TO RUN:
1. Install requirements:  pip install requests pandas
2. Edit the SUBREDDITS list below with subreddits you want to analyze
3. Run:  python collect_reddit_data.py
4. It will save a CSV file (reddit_data.csv) in the same folder
"""

import requests
import pandas as pd
import time

# ---- SETTINGS: edit these ----
SUBREDDITS = [
    "Python", 
    "datascience", 
    "finance", 
    "machinelearning", 
    "learnprogramming", 
    "artificial",
    "tech",
    "programming",
    "technology"
]  
POSTS_PER_SUBREDDIT = 200   # how many posts to collect per subreddit
# --------------------------------

BASE_URL = "https://api.pullpush.io/reddit/search/submission/"

def fetch_posts_with_retry(subreddit, size=200, max_retries=3):
    """Fetch recent posts from a subreddit with auto-retry on 429 errors."""
    params = {
        "subreddit": subreddit,
        "size": size,
        "sort": "desc",
        "sort_type": "created_utc"
    }
    
    backoff_time = 30  # Start with a 30-second wait if rate-limited
    
    for attempt in range(max_retries):
        try:
            response = requests.get(BASE_URL, params=params, timeout=30)
            
            # If we hit a 429 rate limit, handle it gracefully without crashing
            if response.status_code == 429:
                print(f"  !! Hit rate limit (429). Retrying in {backoff_time} seconds (Attempt {attempt + 1}/{max_retries})...")
                time.sleep(backoff_time)
                backoff_time *= 2  # Double the wait time for the next attempt if it fails again
                continue
                
            response.raise_for_status()
            json_data = response.json()
            return json_data.get("data", [])
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                print(f"  !! Failed for r/{subreddit} after {max_retries} attempts: {e}")
                return []
            time.sleep(5)
            
    return []

def main():
    all_posts = []

    for sub in SUBREDDITS:
        print(f"Fetching posts from r/{sub} ...")
        posts = fetch_posts_with_retry(sub, POSTS_PER_SUBREDDIT)
        
        if not posts:
            print(f"  -> No data collected for r/{sub}.")
            continue

        for p in posts:
            all_posts.append({
                "subreddit": p.get("subreddit"),
                "title": p.get("title"),
                "author": p.get("author"),
                "score": p.get("score"),
                "num_comments": p.get("num_comments"),
                "created_utc": p.get("created_utc"),
                "url": p.get("full_link"),
                "selftext": p.get("selftext", "")[:500],  # first 500 chars only
            })
        print(f"  -> Got {len(posts)} posts")
        
        # A baseline polite wait between successful requests
        time.sleep(10)  

    if all_posts:
        df = pd.DataFrame(all_posts)

        # Convert unix timestamp to readable datetime
        df["created_datetime"] = pd.to_datetime(df["created_utc"], unit="s")
        df["post_hour"] = df["created_datetime"].dt.hour
        df["post_day"] = df["created_datetime"].dt.day_name()

        df.to_csv("reddit_data.csv", index=False)
        print(f"\nDone! Saved {len(df)} total posts to reddit_data.csv")
    else:
        print("\nNo data was collected at all. Please try again later.")

if __name__ == "__main__":
    main()