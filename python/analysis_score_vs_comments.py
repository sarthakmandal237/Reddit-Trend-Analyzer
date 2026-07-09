# -----------------------------------------------
# Relationship Between Score and Comments
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")

plt.figure(figsize=(8,6))

plt.scatter(df["score"], df["num_comments"])

plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.grid(True)

plt.show()