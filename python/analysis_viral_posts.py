# -----------------------------------------------
# Top 10 Viral Posts
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")

top_posts = df.sort_values(by="score", ascending=False).head(10)

print("\nTop 10 Viral Posts:")
print(top_posts[["subreddit", "title", "score", "num_comments"]])

plt.figure(figsize=(12,6))

plt.barh(top_posts["title"].str[:50], top_posts["score"], color="green")

plt.title("Top 10 Viral Reddit Posts")
plt.xlabel("Score")
plt.ylabel("Post Title")

plt.tight_layout()

plt.show()