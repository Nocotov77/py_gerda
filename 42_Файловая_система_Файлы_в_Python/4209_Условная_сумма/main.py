with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
N = int(lines[0].strip())
divs = list(map(int, lines[1].split()))
print(sum(i for i in range(1, N) if any(i % d == 0 for d in divs)))