import math

w = int(input())
h = int(input())
cx = int(input())
cy = int(input())
v0 = int(input())


def propagate(d, v):
    if d == 0:
        return v
    new_v = v
    for _ in range(d):
        if new_v == 1:
            return 0
        r = int(math.sqrt(new_v))
        if r * r != new_v:
            return 0
        new_v = r
    return new_v


for y in range(h):
    row = []
    for x in range(w):
        d = max(abs(x - cx), abs(y - cy))
        row.append(str(propagate(d, v0)))
    print("\t".join(row))
