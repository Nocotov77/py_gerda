n = int(input())
words = [input().strip() for _ in range(n)]
print(*words, sep='_', end='')