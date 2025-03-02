str1 = input()
str2 = input()
if str1 == "" or str2 == "":
    print("Пусто!")
else:
    if str1 < str2:
        print(str1 * 5)
    else:
        print(str2 * 5)