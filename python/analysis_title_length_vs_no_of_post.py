# -----------------------------------------------
# Distribution of Reddit Title Length
# -----------------------------------------------

# Create a new column for title length

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_data_clean.csv")
df["title_length"] = df["title"].apply(len)

# Display first 5 title lengths
print("\nTitle Length:")
print(df[["title", "title_length"]].head())

# Plot histogram
plt.figure(figsize=(10,6))

plt.hist(df["title_length"],
         bins=20,
         edgecolor="black",
         color="purple")

plt.title("Distribution of Reddit Post Title Length")
plt.xlabel("Title Length (Characters)")
plt.ylabel("Number of Posts")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.show()