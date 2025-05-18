divisors = {}


def number_of_divisors(n):
    if n in divisors:
        return divisors[n]
    cnt = 0
    r = int(n ** 0.5)
    for i in range(1, r + 1):
        if n % i == 0:
            cnt += 1 if i * i == n else 2
    divisors[n] = cnt
    return cnt

print(number_of_divisors(2000000000))
print(number_of_divisors(6))
print(number_of_divisors(6))
print(number_of_divisors(2000000000))
print(divisors)