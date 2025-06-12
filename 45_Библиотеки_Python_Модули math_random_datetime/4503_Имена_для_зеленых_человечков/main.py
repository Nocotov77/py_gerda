import random
import string


def name(n):
    L1 = random.randint(2, n - 2)
    L2 = n - 1 - L1
    first_part = [random.choice(string.ascii_letters)]
    for _ in range(L1 - 1):
        first_part.append(random.choice(string.ascii_letters + string.digits))
    if not any(ch in string.digits for ch in first_part[1:]):
        pos = random.randint(1, L1 - 1)
        first_part[pos] = random.choice(string.digits)
    first_part = "".join(first_part)
    allowed_upper = "ABCDEFGHIJKLM"
    second_part = [random.choice(allowed_upper)]
    for _ in range(L2 - 1):
        second_part.append(random.choice(string.ascii_lowercase))
    second_part = "".join(second_part)
    return first_part + " " + second_part