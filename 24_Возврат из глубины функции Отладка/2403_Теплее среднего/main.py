def warmer_day(temperatures):
    flat = [x for week in temperatures for x in week]
    avg = sum(flat) / len(flat)
    for i, t in enumerate(flat):
        if t > avg:
            return i + 1
    return 0

temperature = [[1, 1, 2, -3], [0, 5, 11, -10], [14, -2, 4]]
print(warmer_day(temperature))