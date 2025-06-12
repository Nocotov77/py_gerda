import json

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
total = len(lines)
counts = {}
for line in lines:
    d = line[0]
    counts[d] = counts.get(d, 0) + 1
result = {k: round(v / total * 100, 2) for k, v in counts.items()}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)