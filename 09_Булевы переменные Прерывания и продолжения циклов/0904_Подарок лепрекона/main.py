good = 0
evil = 0
prev = ""

while True:
    s = input()
    if s == "":
        break
    if s == "добрый":
        good += 1
        prev = 'добрый'
    elif s == "злой":
        evil += 1
        prev = 'злой'
    elif s == "Какой подарок?":
        if good > evil and prev == "добрый":
            print("серебряный шиллинг")
        elif good < evil and prev == "злой":
            print("золотой")
        else:
            print("Ах, не знаю!")
            break
        good = 0
        evil = 0
        prev = None