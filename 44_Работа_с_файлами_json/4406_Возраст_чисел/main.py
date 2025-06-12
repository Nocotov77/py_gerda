import sys
import json


def age_of_number(num_str):
    if len(num_str) == 1:
        return 1
    steps = 0
    current = num_str
    while len(current) > 1:
        prod = 1
        for ch in current:
            prod *= int(ch)
        steps += 1
        current = str(prod)
    return steps


data = sys.stdin.read().splitlines()
result = {}
for line in data:
    num = line.strip()
    if num:
        a = age_of_number(num)
        result.setdefault(str(a), []).append(num)
with open("numbers_age.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)