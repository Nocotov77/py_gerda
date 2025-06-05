s = input()
d = {}
res = []
for c in s:
    d[c] = d.get(c, 0) + 1
    res.append(str(d[c]))
print(" ".join(res))
