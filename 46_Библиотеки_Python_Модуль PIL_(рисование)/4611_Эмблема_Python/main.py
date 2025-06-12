from PIL import Image, ImageDraw

s = int(input())
x0 = y0 = 70 * s / 2
img = Image.new('RGB', (70 * s, 70 * s), (255, 255, 255))  # White background
draw = ImageDraw.Draw(img)

draw.ellipse((x0 - (35 * s), y0 - (35 * s), x0 + (35 * s), y0 + (35 * s)), (0, 112, 192))

draw.rectangle((14 * s, 24 * s, 24 * s, 44 * s), 'white')
draw.rectangle((14 * s, 24 * s, 45 * s, 34 * s), 'white')
draw.rectangle((26 * s, 12 * s, 45 * s, 22 * s), 'white')
draw.rectangle((x0, 12 * s, 45 * s, 34 * s), 'white')
draw.ellipse((28 * s, 14 * s, 34 * s, 20 * s), (0, 112, 192))

draw.rectangle((47 * s, 26 * s, 57 * s, 46 * s), (255, 192, 0))
draw.rectangle((26 * s, 36 * s, 57 * s, 46 * s), (255, 192, 0))
draw.rectangle((26 * s, 36 * s, 35 * s, 58 * s), (255, 192, 0))
draw.rectangle((26 * s, 48 * s, 45 * s, 58 * s), (255, 192, 0))

draw.ellipse((37 * s, 50 * s, 43 * s, 56 * s), (0, 112, 192))

img.save("python_logo.png")
