from math import ceil

n = int(input())

mm = ceil(n / 20)
dd = n - (mm - 1) * 20 - 1
print(f'Месяц {mm}, день {dd}.')