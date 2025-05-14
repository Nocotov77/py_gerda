number = input().strip()
present = set(number)
all_digits = set("0123456789")
missing = all_digits - present
print(" ".join(sorted(missing)))