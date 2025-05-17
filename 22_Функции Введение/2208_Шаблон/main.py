import math


def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("None")
        return
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Периметр:", perimeter)
    print("Площадь:", area)
    print("Равнобедренный:", "да" if a == b or a == c or b == c else "нет")
    print("Равносторонний:", "да" if a == b == c else "нет")