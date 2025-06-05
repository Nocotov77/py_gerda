n = int(input())
words = [i for i in range(n, -1, -1)]
print(*words, sep=' -> ', end='')