def carrots(n, m, *seq):
    L = len(seq)
    if L < n:
        return 0
    acc = [0]
    for x in seq:
        acc.append(acc[-1] + x)
    for i in range(L - n + 1):
        if acc[i + n] - acc[i] == m:
            return i + 1
    return 0