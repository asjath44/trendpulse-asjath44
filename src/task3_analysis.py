import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")

print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score: {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# NumPy stats
scores = df["score"].values

print("\n--- NumPy Stats ---")
print(f"Mean score: {np.mean(scores):.2f}")
print(f"Median score: {np.median(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")
print(f"Max score: {np.max(scores)}")
print(f"Min score: {np.min(scores)}")

# Most category
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()
print(f"\nMost stories in: {top_category} ({count} stories)")

# Most commented
top_comment = df.loc[df["num_comments"].idxmax()]
print(f"\nMost commented story: \"{top_comment['title']}\" - {top_comment['num_comments']} comments")

# New columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Save
output = "data/trends_analysed.csv"
df.to_csv(output, index=False)

print(f"\nSaved to {output}")