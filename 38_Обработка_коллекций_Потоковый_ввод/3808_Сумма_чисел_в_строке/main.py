import sys
import re

lines = sys.stdin.read().splitlines()
data = [(len(nums := list(map(int, re.findall(r'-?\d+', line)))), sum(nums)) for line in lines]
data = list(filter(lambda t: t[0] > 0, data))
print(-1 if not data else min(t[1] for t in data if t[0] == max(map(lambda t: t[0], data))))