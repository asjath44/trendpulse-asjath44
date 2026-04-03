import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")

os.makedirs("outputs", exist_ok=True)

# ----------------------------
# Chart 1
# ----------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"].str[:40], top10["score"])
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.gcf().set_size_inches(10, 6)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart_top_stories.png")
plt.show()

# ----------------------------
# Chart 2
# ----------------------------
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar", color="skyblue")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/chart_categories.png")
plt.show()

# ----------------------------
# Chart 3
# ----------------------------
colors = df["is_popular"].map({True: "green", False: "red"})

plt.figure()
plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/chart_scatter.png")
plt.show()

# ----------------------------
# BONUS DASHBOARD
# ----------------------------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].barh(top10["title"].str[:30], top10["score"])
axs[0, 0].set_title("Top Stories")
axs[0, 0].invert_yaxis()

axs[0, 1].bar(category_counts.index, category_counts.values)
axs[0, 1].set_title("Categories")

axs[1, 0].scatter(df["score"], df["num_comments"], c=colors)
axs[1, 0].set_title("Score vs Comments")

axs[1, 1].axis("off")

plt.suptitle("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()

print("✅ All charts saved in outputs/")