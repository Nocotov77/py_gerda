import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
parts = [tuple(line.split(", ")) for line in data[1: n + 1]]
parts = [(t, int(s), float(nom)) for t, s, nom in parts]
parts = sorted(parts, key=lambda x: (-x[1], x[0], x[2]))
for t, s, nom in parts:
    print(f"{t}: {nom}; {s}")