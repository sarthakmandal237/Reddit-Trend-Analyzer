# -----------------------------------------------
# Business Question:
# Which subreddit receives the highest average
# number of comments?
# -----------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("reddit_data_clean.csv")

# Calculate average comments for each subreddit
avg_comments = (
    df.groupby("subreddit")["num_comments"]
    .mean()
    .sort_values(ascending=False)
)

# Display results
print("\nAverage Number of Comments by Subreddit:\n")
print(avg_comments)

# Create bar chart
plt.figure(figsize=(10,6))

avg_comments.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Average Number of Comments by Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Average Comments", fontsize=12)

plt.xticks(rotation=45, ha="right")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.show()