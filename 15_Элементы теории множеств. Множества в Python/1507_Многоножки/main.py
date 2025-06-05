n = int(input())
result = set()

for _ in range(n):
    num = int(input())
    count = 0
    if num > 40:
        count += 1
    if num % 2 == 0:
        count += 1
    if num % 3 == 0:
        count += 1
    if count == 2:
        result.add(num)

print(' '.join(map(str, sorted(result))))