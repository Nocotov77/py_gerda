count_all = 0.0
count_yes = 0.0

while True:
    s = input()
    if s == "":
        break
    count_all += 1.0
    if s == "да":
        count_yes += 1.0


if count_yes / count_all * 100 >= 80.0:
    print("Достигли")
else:
    print("Пока нет")