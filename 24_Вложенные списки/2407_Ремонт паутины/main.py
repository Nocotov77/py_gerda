n = int(input())
original = []
for _ in range(n):
    row = list(map(int, input().split()))
    original.append(row)

modified = [row.copy() for row in original]

for i in range(n):
    m = len(original[i])
    for j in range(m):
        if modified[i][j] == 0:
            neighbors = []
            if i > 0:
                neighbors.append(modified[i - 1][j])
            if j > 0:
                neighbors.append(modified[i][j - 1])
            if j < m - 1:
                neighbors.append(original[i][j + 1])
            if i < n - 1:
                neighbors.append(original[i + 1][j])
            if neighbors:
                avg = sum(neighbors) // len(neighbors)
                modified[i][j] = avg

for row in modified:
    print(row)