from PIL import Image, ImageDraw

col = tuple(map(int, (input()).split()))
k = int(input())
img = Image.new('RGB', (20 * k, 22 * k), col)
draw = ImageDraw.Draw(img)

draw.ellipse((7 * k, 7 * k, 13 * k, 21 * k), (255, 250, 235))
draw.rectangle((3 * k, 20 * k, 17 * k, 21 * k), col)

draw.rectangle((3 * k, 20 * k, 17 * k, 21 * k), (146, 208, 80))
draw.chord((3 * k, 3 * k, 17 * k, 17 * k), 180, 0, (192, 0, 0))

draw.ellipse((5 * k, 7 * k, 7 * k, 9 * k), (255, 255, 255))
draw.ellipse((13 * k, 7 * k, 15 * k, 9 * k), (255, 255, 255))
draw.ellipse((9 * k, 4 * k, 11 * k, 6 * k), (255, 255, 255))

img.save('mushroom.png')
