import sys
print(max(sys.stdin.read().split(), key=lambda w: (w.count('a'), len(w), w)))