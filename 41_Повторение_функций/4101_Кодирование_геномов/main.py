def genome(line_1, line_2):
    n = len(line_1)
    comp = 0
    for i in range(n):
        a = line_1[i]
        b = line_2[i]
        if (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or (a == 'C' and b == 'G') or (a == 'G' and b == 'C'):
            comp += 1
    tot = 2 * n
    non_comp = tot - 2 * comp
    return comp, non_comp < 0.3 * tot