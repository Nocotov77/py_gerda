from PIL import Image

oasis = Image.open("desert.png")
camel = Image.open("camel.png").convert("RGBA")

x, y = map(int, input().split())
reflect = input()

if reflect.lower() == "reflect":
    camel = camel.transpose(Image.FLIP_LEFT_RIGHT)

mask = camel.split()[3]
oasis.paste(camel, (x, y), mask)

oasis.save("happy_camel.png")
print("Верблюд успешно перемещён в оазис!")
