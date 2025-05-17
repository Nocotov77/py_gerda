def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime_number():
    if not hasattr(next_prime_number, "current"):
        next_prime_number.current = 2
    p = next_prime_number.current
    print(p)
    candidate = p + 1
    while True:
        if is_prime(candidate):
            next_prime_number.current = candidate
            break
        candidate += 1

next_prime_number()
next_prime_number()
next_prime_number()
next_prime_number()
next_prime_number()
next_prime_number()