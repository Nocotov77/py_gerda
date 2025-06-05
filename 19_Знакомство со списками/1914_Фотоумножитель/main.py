m = int(input())
n = int(input())
matches = {}

for _ in range(n):
    num = int(input())
    index = num % m
    if index not in matches:
        matches[index] = [num]
    else:
        matches[index].append(num)
        matches[index].sort(reverse=True)
        matches[index] = matches[index][:2]

res = []
for i in matches:
    if i == 0:
        if len(matches[i]) >= 2:
            res.append([matches[i][0], matches[i][1]])
    elif i * 2 == m:
        if len(matches[i]) >= 2:
            res.append([matches[i][0], matches[i][1]])
    else:
        if i in matches and (m - i) in matches:
            res.append([matches[i][0], matches[m - i][0]])


if not res:
    print("0 0")
else:
    res = sorted(res, key=lambda x: x[0] * x[1])
    print(f"{res[-1][0]} {res[-1][1]}")