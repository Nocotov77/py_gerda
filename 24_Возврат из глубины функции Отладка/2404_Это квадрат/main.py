import math


def is_it_square(a, b, c, d):
    points = [a, b, c, d]
    dists = []
    for i in range(4):
        for j in range(i + 1, 4):
            dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if dist == 0:
                return None
            dists.append(dist)
    s = sorted(set(dists))
    if len(s) != 2:
        return None
    side_sq = min(s)
    diag_sq = max(s)
    if dists.count(side_sq) != 4 or dists.count(diag_sq) != 2 or diag_sq != 2 * side_sq:
        return None
    return int(math.sqrt(side_sq))

data = [(0, 0), (0, 1), (1, 0), (1, -1)]
print(is_it_square(*data))