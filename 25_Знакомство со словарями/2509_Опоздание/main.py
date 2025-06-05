def to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


d = {}
while True:
    s = input()
    if s == "":
        break
    num, time = s.split()
    d.setdefault(num, []).append(to_minutes(time))
cur = to_minutes(input())
nums = input().split()
cand = []
for num in nums:
    if num in d:
        for t in d[num]:
            et = t - 6
            if et >= cur:
                cand.append(et)
if cand:
    print(min(cand) - cur)
else:
    print("None")
