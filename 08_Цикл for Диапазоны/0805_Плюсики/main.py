sep = input().strip()
words = [input().strip() for _ in range(3)]
print(*words, sep=sep)