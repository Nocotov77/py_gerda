n = int(input())
d = {}
for _ in range(n):
    for pixel in input().split("\t"):
        t = tuple(map(int, pixel.split()))
        d[t] = d.get(t, 0) + 1
m = max(d.values())
for k, v in d.items():
    if v == m:
        print(" ".join(map(str, k)))
