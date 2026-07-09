import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")
avg_score = df.groupby("subreddit")["score"].mean()
print(avg_score)
plt.figure(figsize=(12, 6))
avg_score.sort_values(ascending=False).plot(kind="bar", color="skyblue")
plt.title("Average Score by Subreddit", fontsize=16)
plt.xlabel("Subreddit")
plt.ylabel("Average Score")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

