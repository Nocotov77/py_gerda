m = int(input())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

n = len(matrix[0])
center_i, center_j = m // 2, n // 2

total = 0

total += sum(matrix[0])

if m > 1:
    total += sum(matrix[-1])

for i in range(1, m - 1):
    total += matrix[i][0]
    if n > 1:
        total += matrix[i][-1]

matrix[center_i][center_j] = total

for row in matrix:
    print("\t".join(map(str, row)))
