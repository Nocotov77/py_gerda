wishes = []
while True:
    s = input().strip()
    if s == 'разбитое корыто':
        break
    wishes.append(s)

for i in range(len(wishes)):
    min_idx = i
    for j in range(i + 1, len(wishes)):
        if len(wishes[j]) < len(wishes[min_idx]):
            min_idx = j
    wishes[i], wishes[min_idx] = wishes[min_idx], wishes[i]

for wish in wishes:
    print(wish)