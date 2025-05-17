r = int(input())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))
c = len(matrix[0])
for i in range(r):
    if i % 2 == 1:
        matrix[i] = matrix[i][::-1]
for j in range(0, c, 2):
    for i in range(r // 2):
        matrix[i][j], matrix[r - 1 - i][j] = matrix[r - 1 - i][j], matrix[i][j]
for row in matrix:
    print("\t".join(str(x) for x in row))
