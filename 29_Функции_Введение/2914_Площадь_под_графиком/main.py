def square(data):
    total = 0
    for a, b, h in data:
        total += ((a + b) / 2) * h
    print(total)