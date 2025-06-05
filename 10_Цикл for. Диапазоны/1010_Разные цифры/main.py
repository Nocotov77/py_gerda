n = int(input())
m = int(input())

for num in range(n, m + 1):
    a = num // 1000
    b = (num // 100) % 10
    c = (num // 10) % 10
    d = num % 10

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(num)