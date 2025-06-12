import csv
import json

with open("state.txt", "r", encoding="utf-8") as f:
    state = f.read().strip()
results = []
with open("world_university_ranking.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["location"].strip() == state:
            results.append({"institution": row["institution"], "rank": row["rank"], "ar score": row["ar score"]})
with open("state.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False)