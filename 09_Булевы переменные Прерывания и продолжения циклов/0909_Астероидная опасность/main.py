current_trend = None
prev = None
current_length = 0
results = []
alarm_triggered = False

while True:
    try:
        line = input().strip()
        if not line:
            continue
        num = int(line)
        if num < 0:
            break
        if num < 35:
            alarm_triggered = True
            break
        if prev is None:
            prev = num
            continue
        if num == prev:
            continue
        new_trend = 'up' if num > prev else 'down'
        if current_trend is None:
            current_trend = new_trend
            current_length = 2
        else:
            if new_trend == current_trend:
                current_length += 1
            else:
                results.append(current_length)
                current_trend = new_trend
                current_length = 2
        prev = num
    except EOFError:
        break

if current_length >= 2 and not alarm_triggered:
    results.append(current_length)

if alarm_triggered:
    for res in results:
        print(res)
    print("ALARM")
else:
    for res in results:
        print(res)