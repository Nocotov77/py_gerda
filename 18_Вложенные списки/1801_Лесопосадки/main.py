rows = []
while True:
    line = input().strip()
    if not line:
        break
    parts = line.split(' : ')
    numbers = list(map(int, parts))
    rows.append(numbers)

critical = int(input())

for row in rows:
    processed = [str(num) if num >= critical else '0' for num in row]
    print('\t'.join(processed))