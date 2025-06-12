
import sys
from PIL import Image

angle = int(sys.stdin.readline().strip())
rgb_str = sys.stdin.readline().strip().split(',')
new_bg_color = (int(rgb_str[0]), int(rgb_str[1]), int(rgb_str[2]))
img = Image.open("sunflower.png").convert("RGBA")
bg_color = img.getpixel((0, 0))
newData = []
for item in img.getdata():
    if item[0] == bg_color[0] and item[1] == bg_color[1] and item[2] == bg_color[2]:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
rotated_img = img.rotate(angle)
final_canvas = Image.new("RGB", img.size, new_bg_color)
final_canvas.paste(rotated_img, (0, 0), rotated_img)
final_canvas.save("turned_sunflower.png")