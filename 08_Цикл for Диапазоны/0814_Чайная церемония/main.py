size_teapot = int(input())
size_cup = int(input())
qty_cup = int(input())

for i in range(qty_cup):
    size_teapot -= size_cup
    if size_teapot > 0 or size_teapot == 0:
        string = "полная"
    elif size_teapot <= 0 - size_cup:
        string = "пустая"
    else:
        string = "неполная"
    if size_teapot < 0:
        print(f"Чашечка {i + 1} {string}. В чайнике осталось 0.")
    else:
        print(f"Чашечка {i + 1} {string}. В чайнике осталось {size_teapot}.")