# -----------------------------------------------
# Average Score by Posting Day
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")

avg_day_score = df.groupby("post_day")["score"].mean()

# Arrange days in correct order
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

avg_day_score = avg_day_score.reindex(days)

print("\nAverage Score by Posting Day:")
print(avg_day_score)

plt.figure(figsize=(10,5))

avg_day_score.plot(kind="bar", color="orange")

plt.title("Average Score by Posting Day")
plt.xlabel("Day")
plt.ylabel("Average Score")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.show()