from math import floor
from sys import exit


def hours_to_min(h, m):
    return m + h * 60


minutes = hours_to_min(int(input()), int(input()))
way = 60 * 12
stops = int(input())

if way < minutes:
    print("Не останавливаемся!")
    exit()

stops_time = (way - minutes) / stops

print(f"{floor(stops_time)} минут")