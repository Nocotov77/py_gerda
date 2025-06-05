nums = input().split()
d = {}
for num in nums:
    for ch in num:
        d[ch] = d.get(ch, 0) + 1
m = max(d.values())
res = [k for k, v in d.items() if v == m]
print(" ".join(sorted(res, key=int)))
