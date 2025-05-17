best = None
while True:
    s = input()
    if s == "Алиса, привет!":
        break
    if "Алиса" in s:
        if best is None or len(s) < len(best) or (len(s) == len(best) and s < best):
            best = s
print(best)
