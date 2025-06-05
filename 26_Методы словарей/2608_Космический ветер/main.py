data = input().split()
intervals = {"до 10": [], "от 10 до 100": [], "от 100 до 1000": [], "свыше 1000": []}
for num in map(float, data):
    if num < 10:
        intervals["до 10"].append(num)
    elif num < 100:
        intervals["от 10 до 100"].append(num)
    elif num < 1000:
        intervals["от 100 до 1000"].append(num)
    else:
        intervals["свыше 1000"].append(num)
for k in ["до 10", "от 10 до 100", "от 100 до 1000", "свыше 1000"]:
    if intervals[k]:
        cnt = len(intervals[k])
        avg = sum(intervals[k]) / cnt
        print(f"{k}: {cnt}, {avg:.1f}")
