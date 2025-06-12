
from PIL import Image

n = int(input())
canvas = Image.new("RGB", (1000, 2000), "white")
book = Image.open("book.png").convert("RGBA")
w, h = book.size
x, y = 1000 - w, 2000 - h

for _ in range(n):
    current = book.resize((w, h), Image.LANCZOS)
    canvas.paste(current, (x, y), current)
    w = int(0.9 * w)
    h = int(0.9 * h)
    y -= h

canvas.save("stack.png")