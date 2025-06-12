import json

with open("russian_words.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]
d = {}
for word in words:
    key = word[0]
    d.setdefault(key, []).append(word)
with open("russian_words.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)