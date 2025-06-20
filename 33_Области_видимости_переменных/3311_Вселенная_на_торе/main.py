def research_universe(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    res = []
    for i in range(n):
        row = []
        for j in range(m):
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni = (i + di) % n
                    nj = (j + dj) % m
                    if key(matrix[ni][nj]):
                        cnt += 1
            row.append(cnt)
        res.append(row)
    return res