periods = {}
parts = input().split()
for i in range(0, len(parts), 2):
    periods[parts[i]] = int(parts[i + 1])
dist = input().split()
acts = list(map(float, input().split()))
limit = float(input())


def total(T):
    s = 0
    for i, el in enumerate(dist):
        s += acts[i] / (2 ** (T // periods[el]))
    return s


if total(0) <= limit:
    T_min = 0
else:
    lo = 0
    hi = 1
    while total(hi) > limit:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if total(mid) <= limit:
            hi = mid
        else:
            lo = mid + 1
    T_min = lo
final = []
for i, el in enumerate(dist):
    final.append(acts[i] / (2 ** (T_min // periods[el])))
print(T_min)
print(" ".join(str(x) for x in final))
