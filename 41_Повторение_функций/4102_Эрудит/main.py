from collections import Counter
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
for line in lines:
    if not line.strip():
        print("")
        continue
    parts = line.split()
    src = parts[0]
    src_count = Counter(src)
    valid = []
    for i, word in enumerate(parts[1:]):
        cnt = Counter(word)
        if all(cnt[ch] <= src_count.get(ch, 0) for ch in cnt):
            valid.append((word, i))
    valid.sort(key=lambda x: (-len(x[0]), x[1]))
    print(" ".join(word for word, _ in valid))