import pandas as pd

# Load the dataset
df = pd.read_csv("reddit_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nShape of Dataset:", df.shape)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# ----------------------------------------------------
# DATA CLEANING
# ----------------------------------------------------

# Remove the 'url' column because all values are missing
df.drop(columns=["url"], inplace=True)

# Replace missing values in selftext with an empty string
df["selftext"] = df["selftext"].fillna("")

# Check for duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Display new dataset shape
print("\nNew Shape of Dataset:", df.shape)

# Save cleaned dataset
# Remove unsupported Unicode characters

df["title"] = (
    df["title"]
    .astype(str)
    .str.encode("ascii", "ignore")
    .str.decode("ascii")
)

df["selftext"] = (
    df["selftext"]
    .astype(str)
    .str.encode("ascii", "ignore")
    .str.decode("ascii")
)

# Save cleaned dataset
df.to_csv(
    "reddit_data_clean.csv",
    index=False,
    encoding="utf-8"
)

print("✅ Cleaned dataset saved as 'reddit_data_clean.csv'")