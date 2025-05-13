wish = False

while True:
    s = input()
    if s == "ВСЁ":
        break
    if "Звезд" in s or "звезд" in s:
        wish = True

if wish:
    print("Загадывай!")
else:
    print("НЕТ")