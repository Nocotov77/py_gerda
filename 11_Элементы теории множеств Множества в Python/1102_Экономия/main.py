n = int(input())
digits = set()
for _ in range(n):
    number = input().strip()
    for ch in number:
        digits.add(ch)
print(len(digits))