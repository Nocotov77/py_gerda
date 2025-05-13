max_valid = 0
has_violation = False

n = int(input())

for _ in range(n):
    m = int(input())
    speeds = [int(input()) for _ in range(m)]
    is_valid = True
    current_max = 0
    for speed in speeds:
        if speed > 60:
            is_valid = False
        if speed > current_max:
            current_max = speed
    if is_valid:
        if current_max > max_valid:
            max_valid = current_max
    else:
        has_violation = True

print(max_valid)
print("ДА" if has_violation else "НЕТ")