def allocation(arr):
    fails = []
    for r, c in arr:
        if places[r - 1][c - 1] == 0:
            places[r - 1][c - 1] = 1
        else:
            fails.append((r, c))
    return fails