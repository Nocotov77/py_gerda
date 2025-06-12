from PIL import Image, ImageDraw

try:
    width_str, height_str = input().split()
    width = int(width_str)
    height = int(height_str)

    if height % 2 != 0:
        print("Ошибка: высота должна быть четным числом.")
    else:
        r_str, g_str, b_str = input().split()
        r = int(r_str)
        g = int(g_str)
        b = int(b_str)

        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)

        for y in range(0, height, 2):
            current_color = (min(255, r), min(255, g), min(255, b))
            draw.rectangle([(0, y), (width, y + 1)], fill=current_color)
            r += 2
            g += 2
            b += 2

        img.save('sunrise.png')
        print("Изображение 'sunrise.png' успешно создано.")

except ValueError:
    print("Ошибка: пожалуйста, вводите числовые значения, разделенные пробелом.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

