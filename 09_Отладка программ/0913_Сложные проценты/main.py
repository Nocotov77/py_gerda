summa = int(input())
percent = float(input())
years = float(input())

whole_years = int(years)
fractional_part = years - whole_years

current = summa * (1 + percent / 100) ** whole_years

if fractional_part > 0:
    current *= (1 + 0.01 * fractional_part)

if current.is_integer():
    print(f"{int(current)}.0")
else:
    print(current)