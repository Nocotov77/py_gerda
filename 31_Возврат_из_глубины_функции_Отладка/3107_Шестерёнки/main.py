def gears(data, n, m):
    flat = []
    for box in data:
        flat.extend(box)
    freq = {}
    for gear in flat:
        if gear <= 0:
            continue
        freq[gear] = freq.get(gear, 0) + 1
    candidates = sorted(freq.keys(), reverse=True)
    for a in candidates:
        if a % n:
            continue
        k = a // n
        b = m * k
        if b in freq:
            if a == b and freq[a] < 2:
                continue
            return (a, b)
    return (None, None)