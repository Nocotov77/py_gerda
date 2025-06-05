n = int(input())
d = {}
for _ in range(n):
    parts = input().split(maxsplit=2)
    day = int(parts[0])
    month = parts[1]
    event = parts[2]
    if month in d:
        if day < d[month][0]:
            d[month] = (day, event)
    else:
        d[month] = (day, event)
q = input()
print(d[q][1])
