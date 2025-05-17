n = int(input())
matrix = []
for _ in range(n):
    line = input().strip().split(', ')
    row = list(map(int, line))
    matrix.append(row)

for i in range(n):
    j = n - 1 - i
    matrix[i][i], matrix[i][j] = matrix[i][j], matrix[i][i]

for row in matrix:
    print(' '.join(map(str, row)))

sum_main = sum(matrix[i][i] for i in range(n))
sum_secondary = sum(matrix[i][n - 1 - i] for i in range(n))
print(sum_main + sum_secondary)