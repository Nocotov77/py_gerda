k = int(input())
b = int(input())
counter_up = 0
counter_low = 0
counter_on = 0

while True:
    try:
        x = int(input())
        y = int(input())
        if k * x - y + b < 0:
            counter_up += 1
        elif k * x - y + b == 0:
            counter_on += 1
        elif k * x - y + b > 0:
            counter_low += 1
    except ValueError:
        break

if counter_up > 0:
    print(f"Выше прямой: {counter_up}")
if counter_low > 0:
    print(f"Ниже прямой: {counter_low}")
if counter_on > 0:
    print(f"На прямой: {counter_on}")
