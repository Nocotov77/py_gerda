def defense(*points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    return max(xs) - min(xs), max(ys) - min(ys)

points = [(1, 1), (-1, 2), (-3, -1)]
print(*defense(*points))