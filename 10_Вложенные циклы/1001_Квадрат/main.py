n = int(input())
for i in range(n):
    start = i * n + 1
    end = (i + 1) * n
    row = list(map(str, range(start, end + 1)))
    print('\t'.join(row))