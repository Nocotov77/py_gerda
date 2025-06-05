import sys
import math


def sort_key(beacon):
    return (beacon[2], -beacon[3])


def format_val(v):
    return str(int(v)) if v == int(v) else str(v)


lines = sys.stdin.read().splitlines()
observer_x, observer_y = map(float, lines[0].split())
n = int(lines[1])
beacons = []
for i in range(n):
    x, y, intensity = map(float, lines[i + 2].split())
    distance_sq = (x - observer_x) ** 2 + (y - observer_y) ** 2
    if distance_sq == 0:
        brightness = float('inf')
    else:
        brightness = intensity / distance_sq
    distance = math.sqrt(distance_sq)
    beacons.append((x, y, brightness, distance))
best = max(beacons, key=sort_key)
print(f"{format_val(best[0])} {format_val(best[1])}")