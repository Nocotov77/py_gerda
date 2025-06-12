import random
import string


def name(n):
    L1 = random.randint(2, n - 2)
    L2 = n - 1 - L1
    used = set()
    first = []
    ch = random.choice(string.ascii_letters)
    first.append(ch)
    used.add(ch.lower())
    digit_pos = random.choice(range(1, L1))
    for i in range(1, L1):
        if i == digit_pos:
            pool = [d for d in string.digits if d not in used]
            if not pool:
                return name(n)
            d = random.choice(pool)
            first.append(d)
            used.add(d)
        else:
            pool = []
            for ch in string.ascii_letters + string.digits:
                if ch.isalpha():
                    if ch.lower() not in used:
                        pool.append(ch)
                else:
                    if ch not in used:
                        pool.append(ch)
            if not pool:
                return name(n)
            c = random.choice(pool)
            first.append(c)
            used.add(c.lower() if c.isalpha() else c)
    first_part = "".join(first)
    second = []
    pool = [ch for ch in "ABCDEFGHIJKLM" if ch.lower() not in used]
    if not pool:
        return name(n)
    ch = random.choice(pool)
    second.append(ch)
    used.add(ch.lower())
    for _ in range(1, L2):
        pool = [ch for ch in string.ascii_lowercase if ch not in used]
        if not pool:
            return name(n)
        c = random.choice(pool)
        second.append(c)
        used.add(c)
    second_part = "".join(second)
    return first_part + " " + second_part


def little_green_men_names(m, n):
    names = set()
    res = []
    while len(res) < m:
        candidate = name(n)
        if candidate not in names:
            names.add(candidate)
            res.append(candidate)
    return res