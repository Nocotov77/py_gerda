with open("rating.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
scores = {}
for line in lines:
    if line.strip():
        nickname, result = line.split(":", 1)
        nickname = nickname.strip()
        result = int(result.strip())
        scores[nickname] = scores.get(nickname, 0) + result
max_score = max(scores.values())
winners = sorted(n for n, score in scores.items() if score == max_score)
for winner in winners:
    print(winner)