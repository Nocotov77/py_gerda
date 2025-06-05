n = int(input())
m = int(input())
k = int(input())

total = k * 120
max_sum = 0
best_x, best_y = 0, 0

for y in range((total - n) // m, 0, -1):
    remaining = total - m * y
    if remaining <= 0:
        continue
    if remaining % n == 0:
        x = remaining // n
        if x >= 1:
            current_sum = 2 * x + 5 * y
            if current_sum > max_sum:
                max_sum = current_sum
                best_x, best_y = x, y

print(max_sum)
print(f"({best_x}, {best_y})")