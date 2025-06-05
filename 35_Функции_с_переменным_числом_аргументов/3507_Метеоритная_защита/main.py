def defense(*points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    return max(xs) - min(xs), max(ys) - min(ys)