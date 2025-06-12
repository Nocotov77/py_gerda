from PIL import Image
import sys

s = int(sys.stdin.readline().strip())
frame_color = "#208d80"
border_width = s // 10
tile = Image.new("RGB", (s, s), frame_color)
ornament = Image.open("ornament.png").convert("RGBA")
ornament_size = s - 2 * border_width
resized_ornament = ornament.resize((ornament_size, ornament_size), Image.BICUBIC)
paste_position = (border_width, border_width)
tile.paste(resized_ornament, paste_position, resized_ornament)
tile.save("tile.png")
