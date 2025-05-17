n = int(input())
m = int(input())
names = [input().strip() for _ in range(n * m)]
grid = [names[i * m: (i + 1) * m] for i in range(n)]

result = []

for i in range(n):
    for j in range(m):
        current = grid[i][j]
        vertical_violation = False

        if i > 0:
            upper = grid[i - 1][j]
            if len(upper) == len(current) or upper[0] == current[0]:
                vertical_violation = True
        if i < n - 1:
            lower = grid[i + 1][j]
            if len(lower) == len(current) or lower[0] == current[0]:
                vertical_violation = True

        horizontal_violation = False
        left_ok = True
        right_ok = True

        if j > 0:
            left = grid[i][j - 1]
            left_ok = (len(left) == len(current)) or (left[0] == current[0])
        if j < m - 1:
            right = grid[i][j + 1]
            right_ok = (len(right) == len(current)) or (right[0] == current[0])

        if not left_ok or not right_ok:
            horizontal_violation = True

        if vertical_violation or horizontal_violation:
            result.append((i, j))

for coord in sorted(result):
    print(coord)