import sys
data = sys.stdin.read().split()
res = []
for i, num in enumerate(data, 1):
    if int(num) == i:
        res.append(str(i))
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(res) if res else "0")