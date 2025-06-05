n = int(input())
if n == 0:
    print("0 0")
else:
    sets = [set(input().strip()) for _ in range(n)]
    common = sets[0].copy()
    for s in sets[1:]:
        common &= s
    union = sets[0].copy()
    for s in sets[1:]:
        union |= s
    print(f"{len(common)} {len(union)}")