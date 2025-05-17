d = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'к': 9}
grid = [["0"] * 10 for _ in range(10)]
ships = [4] + [3] * 2 + [2] * 3 + [1] * 4
for s in ships:
    a, orient = input().split()
    col = d[a[0]]
    row = int(a[1:]) - 1
    dr, dc = (1, 0) if orient == 'в' else (0, 1)
    for i in range(s):
        grid[row + i * dr][col + i * dc] = "\u25A1"
for r in grid:
    print(" ".join(r))
