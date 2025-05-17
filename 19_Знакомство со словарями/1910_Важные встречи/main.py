n = int(input())
d = {}
for _ in range(n):
    name, day, month = input().split(", ")
    day = int(day)
    d.setdefault(month, []).append((day, name))
m = input()
if m in d:
    for day, name in sorted(d[m], key=lambda x: (x[0], x[1])):
        print(name)
