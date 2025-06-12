from PIL import Image

sl = input()

im = Image.open('fruits.png')
fly = Image.open('fruits.png')

x, y = im.size
v = fly.crop((0, 0, x / 2, y / 2))
m = fly.crop((x / 2, 0, x, y / 2))
k = fly.crop((0, y / 2, x / 2, y))
s = fly.crop((x / 2, y / 2, x, y))

bbox = [(0, 0), (x // 2, 0), (0, y // 2), (x // 2, y // 2)]

for i in range(4):
    if sl[i] == '1':
        im.paste(v, bbox[i])
    if sl[i] == '2':
        im.paste(m, bbox[i])
    if sl[i] == '3':
        im.paste(k, bbox[i])
    if sl[i] == '4':
        im.paste(s, bbox[i])


im.save('cycle.png')
