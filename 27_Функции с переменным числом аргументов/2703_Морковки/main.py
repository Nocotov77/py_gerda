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

data = [1, 2, 3, 4, 5]
print(carrots(3, 9, *data))
