import json
import sys

lines = sys.stdin.read().splitlines()
fname = lines[0].strip()
query = lines[1].strip()
with open(fname, "r", encoding="utf-8") as f:
    data = json.load(f)
result = {}
for rec in data:
    key = rec[query]
    result.setdefault(key, []).append(rec["youtuber"])
print(result)