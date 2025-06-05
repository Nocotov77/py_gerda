n = int(input())
start = n - 2
evens = [i for i in range(start, 11) if i % 2 == 0]
print(*evens)