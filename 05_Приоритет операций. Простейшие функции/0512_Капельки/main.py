s_r = int(input())
amt = int(input())

s_v = 4 / 3 * 3.14 * s_r ** 3
b_v = s_v * amt
b_r = ((3 * b_v) / (4 * 3.14)) ** (1 / 3)
b_r = round(b_r, 2)

print(b_r)