def quarters(*points):
    d = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for x, y in points:
        if x == 0 or y == 0:
            continue
        if x > 0 and y > 0:
            d["I"] += 1
        elif x < 0 and y > 0:
            d["II"] += 1
        elif x < 0 and y < 0:
            d["III"] += 1
        elif x > 0 and y < 0:
            d["IV"] += 1
    return d