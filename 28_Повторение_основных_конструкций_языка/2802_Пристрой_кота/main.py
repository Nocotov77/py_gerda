n = int(input())
min_age = int(input())
min_count = 1
for _ in range(n - 1):
    age = int(input())
    if age < min_age:
        min_age = age
        min_count = 1
    elif age == min_age:
        min_count += 1
print(min_count)