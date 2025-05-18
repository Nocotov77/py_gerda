import sys
print(min(sys.stdin.read().splitlines(), key=lambda x: (sum(map(int, x)), -len(x), int(x))))
