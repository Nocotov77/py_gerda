import random
import string


def name(n):
    L1 = random.randint(2, n - 2)
    L2 = n - L1 - 1
    used = set()
    first = []
    pool = [c for c in string.ascii_letters if c.lower() not in used]
    ch = random.choice(pool)
    first.append(ch)
    used.add(ch.lower())
    digit_index = random.randint(1, L1 - 1)
    for i in range(1, L1):
        if i == digit_index:
            pool = [c for c in string.digits if c not in used]
            if not pool:
                return name(n)
            ch = random.choice(pool)
            first.append(ch)
            used.add(ch)
        else:
            pool = [c for c in (string.ascii_letters + string.digits) if c.lower() not in used]
            if not pool:
                return name(n)
            ch = random.choice(pool)
            first.append(ch)
            if ch.isalpha():
                used.add(ch.lower())
            else:
                used.add(ch)
    first_part = "".join(first)
    second = []
    pool = [c for c in "ABCDEFGHIJKLM" if c.lower() not in used]
    if not pool:
        return name(n)
    ch = random.choice(pool)
    second.append(ch)
    used.add(ch.lower())
    for i in range(1, L2):
        pool = [c for c in string.ascii_lowercase if c not in used]
        if not pool:
            return name(n)
        ch = random.choice(pool)
        second.append(ch)
        used.add(ch)
    second_part = "".join(second)
    return first_part + " " + second_part