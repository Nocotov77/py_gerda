import math

n = int(input())
divisors = []
stack = []

sqrt_n = math.isqrt(n)
for d in range(1, sqrt_n + 1):
    if n % d == 0:
        divisors.append(d)
        if d != (pair := n // d):
            stack.append(pair)

divisors += reversed(stack)
print(' '.join(map(str, divisors)))