def allocation(arr):
    fails = []
    for r, c in arr:
        if places[r - 1][c - 1] == 0:
            places[r - 1][c - 1] = 1
        else:
            fails.append((r, c))
    return fails


places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = [(2, 3), (1, 4), (3, 1), (2, 3), (3, 3)]
print(allocation(data))