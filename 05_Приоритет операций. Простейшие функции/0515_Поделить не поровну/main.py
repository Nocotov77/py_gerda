n = int(input())
n1 = n // 1000
n2 = n % 1000 // 100
n3 = n % 100 // 10
n4 = n % 10

if n1 != 0 and n2 != 0 and n3 != 0 and n4 != 0:
    n1, n2, n3, n4 = sorted((n1, n2, n3, n4))
    min = int(str(n1) + str(n2))
    max = int(str(n4) + str(n3))
    print(min, max)

else:
    n1, n2, n3, n4 = sorted((n1, n2, n3, n4))
    min = int(str(n2) + str(0))
    max = int(str(n4) + str(n3))
    print(min, max)
