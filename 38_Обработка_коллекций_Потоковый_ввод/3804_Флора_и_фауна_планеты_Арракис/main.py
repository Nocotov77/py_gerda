import sys
lines = sys.stdin.read().splitlines()
target = lines[-1].strip()
entries = []
for line in lines[:-1]:
    parts = list(map(str.strip, line.split("//")))
    if parts[1] == target:
        entries.append((parts[0], f"{parts[0]} ({parts[2]});"))
for _, entry in sorted(entries, key=lambda x: x[0], reverse=True):
    print(entry)