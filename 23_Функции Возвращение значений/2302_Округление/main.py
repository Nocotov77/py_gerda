def rounding(data):
    s_int = 0
    s_frac = 0
    for num in data:
        s_int += int(num)
        s_frac += num - int(num)
    return (s_int, round(s_frac, 2))

data = [1.52, 12.64, 6.46, 9.4]
print(rounding(data))
