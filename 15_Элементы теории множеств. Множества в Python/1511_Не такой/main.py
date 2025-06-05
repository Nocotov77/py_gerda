control = input().strip()
n = int(input())
max_chars = -1
best_set = set()

for _ in range(n):
    line = input().strip()
    filtered = line.replace(control, '')
    unique = set(filtered)
    count = len(unique)
    if count > max_chars:
        max_chars = count
        best_set = unique

if max_chars == 0:
    print(-1)
else:
    print(''.join(sorted(best_set)))