from datasets import load_dataset
import pandas as pd

# Load dataset
dataset = load_dataset("mltrev23/financial-sentiment-analysis")

# Chỉ có train
df = pd.DataFrame(dataset["train"])

# 🔥 Rename đúng cột
df = df.rename(columns={
    "Sentence": "text",
    "Sentiment": "label"
})

# (Dataset này label đã là text: positive/negative/neutral nên KHÔNG cần map)

# Nếu muốn bỏ neutral:
# df = df[df["label"] != "neutral"]

# Giữ đúng format
df = df[["text", "label"]]

# Xuất CSV
df.to_csv("sentiment.csv", index=False, encoding="utf-8")

print("✅ Done!")