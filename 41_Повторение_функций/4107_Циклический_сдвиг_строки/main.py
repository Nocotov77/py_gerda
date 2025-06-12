import sys
data = sys.stdin.read().splitlines()
s = int(data[0])
for line in data[1:]:
    n = len(line)
    if n:
        k = s % n
        print(line[k:] + line[:k])
    else:
        print("")