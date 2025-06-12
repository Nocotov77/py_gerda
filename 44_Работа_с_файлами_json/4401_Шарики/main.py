import json

with open("input.json", "r", encoding="utf-8") as f:
    balls = json.load(f)
balls.sort(key=lambda b: (-len(b["colors"]), -b["radius"], -((b["x"] ** 2) + (b["y"] ** 2)), b["id"]))
print(" ".join(str(b["id"]) for b in balls))