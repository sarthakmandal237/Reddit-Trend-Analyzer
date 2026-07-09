import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")

avg_hour_score = df.groupby("post_hour")["score"].mean().sort_index()

print("\nAverage Score by Posting Hour:")
print(avg_hour_score)

plt.figure(figsize=(10,5))

avg_hour_score.plot(kind="line", marker="o")

plt.title("Average Score by Posting Hour")
plt.xlabel("Posting Hour (24-Hour Format)")
plt.ylabel("Average Score")

plt.grid(True)

plt.tight_layout()

plt.show()