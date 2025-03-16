hours = int(input())
minutes = int(input())

if 12 <= hours <= 23:
    hours -= 12

angle = abs((hours + (minutes / 60)) * 30 - minutes * 6)

print(angle)