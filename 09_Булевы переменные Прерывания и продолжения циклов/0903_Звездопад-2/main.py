wish = False
i = 0
string = 0

while True:
    s = input()
    i += 1
    if s == "ВСЁ":
        break
    if "Звезд" in s or "звезд" in s:
        if not wish:
            string = i
        wish = True

if wish:
    print(string)
else:
    print("НЕТ")