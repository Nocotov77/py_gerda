char = input().strip()
n = int(input())

for i in range(n):
    row = [' '] * n
    row[i] = char
    row[n - 1 - i] = char
    print(' '.join(row))