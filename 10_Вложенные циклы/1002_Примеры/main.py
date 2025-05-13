start = int(input())
end = int(input())
step = int(input())

numbers = []
current = start
while current <= end:
    numbers.append(current)
    current += step

for a in numbers:
    examples = [f"{a} + {b} = {a + b}" for b in numbers]
    print('\t'.join(examples))