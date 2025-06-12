with open("in_file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
d = int(lines[0])
text = lines[1:]
avg = sum(len(line) for line in text) // len(text) if text else 0
res = [str(avg)]
for line in text:
    if abs(len(line) - avg) <= d:
        res.append(line)
with open("out_file.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(res))
