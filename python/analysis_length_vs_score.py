# -----------------------------------------------
# Do Longer Titles Receive More Upvotes?
# -----------------------------------------------

# Create title length column (if not already created)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")
df["title_length"] = df["title"].apply(len)

plt.figure(figsize=(10,6))

plt.scatter(df["title_length"],
            df["score"],
            alpha=0.6)

plt.title("Title Length vs Reddit Score")
plt.xlabel("Title Length (Characters)")
plt.ylabel("Reddit Score")

plt.grid(True)

plt.tight_layout()

plt.show()