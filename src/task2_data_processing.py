import pandas as pd
import glob
import os

# Load latest JSON file
files = glob.glob("data/*.json")
latest = max(files, key=os.path.getctime)

df = pd.read_json(latest)

print(f"Loaded {len(df)} stories from {latest}")

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove nulls
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Fix types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low scores
df = df[df["score"] > 5]
print(f"After removing low scores: {len(df)}")

# Clean text
df["title"] = df["title"].str.strip()

# Save CSV
output = "data/trends_clean.csv"
df.to_csv(output, index=False)

print(f"\nSaved {len(df)} rows to {output}")

# Summary
print("\nStories per category:")
print(df["category"].value_counts())