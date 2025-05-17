import math
words = input().split()
d = {}
for w in words:
    d.setdefault(len(w), set()).add(w)
p = 1
for s in d.values():
    p *= math.factorial(len(s))
print(p if len(d) == 1 else 2 * p)
