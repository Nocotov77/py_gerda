from PIL import Image, ImageDraw

try:
    width_str, height_str, stripe_width_str = input().split()
    width = int(width_str)
    height = int(height_str)
    stripe_width = int(stripe_width_str)

    gap_width = stripe_width // 4

    img = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(img)

    white = (255, 255, 255)
    yellow = (255, 192, 0)
    colors = [white, yellow]

    current_x = 0
    color_index = 0

    while current_x < width:
        current_color = colors[color_index]
        box = (current_x, 0, current_x + stripe_width, height)
        draw.rectangle(box, fill=current_color)
        current_x += stripe_width + gap_width
        color_index = (color_index + 1) % 2

    img.save('crossing.png')
    print("Изображение 'crossing.png' успешно создано.")

except ValueError:
    print("Ошибка: пожалуйста, вводите три числовых значения, разделенные пробелом.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
