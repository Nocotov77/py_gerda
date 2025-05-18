import sys
data = sys.stdin.read().split()
a, b = map(int, data)
print(" ".join(map(str, sorted(filter(lambda x: x % 3 == 0, range(a, b + 1)),
                               key=lambda x: (x % 2, -x)))))
