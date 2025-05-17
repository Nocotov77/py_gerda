matrix = []
while True:
    line = input().strip()
    if not line:
        break
    row = list(map(int, line.split()))
    matrix.append(row)

n = len(matrix)
m = len(matrix[0]) if n > 0 else 0
crystal = chr(int('0x1F48E', 16))

for i in range(n):
    for j in range(m):
        if not isinstance(matrix[i][j], int):
            continue
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < n - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < m - 1:
            neighbors.append((i, j + 1))
        if any(not isinstance(matrix[ni][nj], int) for ni, nj in neighbors):
            continue
        neighbor_values = [matrix[ni][nj] for ni, nj in neighbors]
        if all(matrix[i][j] > val for val in neighbor_values):
            salt_added = 0
            for ni, nj in neighbors:
                if isinstance(matrix[ni][nj], int) and matrix[ni][nj] > 0:
                    matrix[ni][nj] -= 1
                    salt_added += 1
            matrix[i][j] += salt_added
            if matrix[i][j] > 9:
                matrix[i][j] = crystal

for row in matrix:
    print('\t'.join(map(str, row)))