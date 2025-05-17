def groundhog_day(data):
    for i in range(1, len(data)):
        diffs = []
        for j in range(len(data[i])):
            if data[i][j] != data[i - 1][j]:
                diffs.append(j)
        if len(diffs) > 2:
            return (i, *diffs)
    return (0, 0)