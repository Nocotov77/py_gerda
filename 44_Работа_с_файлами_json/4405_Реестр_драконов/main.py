import csv
import json

with open("dragons.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    dragons = list(reader)
result = {"dragons": dragons}
with open("dragons.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)