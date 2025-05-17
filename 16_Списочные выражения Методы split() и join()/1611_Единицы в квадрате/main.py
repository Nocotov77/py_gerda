import math

n = int(input())
if n < 1:
    print()
else:
    k_max = math.floor(math.log10(9 * n + 1))
    numbers = [(10**i - 1) // 9 for i in range(1, k_max + 1) if (10**i - 1) // 9 <= n]
    squares = [x**2 for x in numbers]
    print(', '.join(map(str, squares)))