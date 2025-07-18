# Стопка книг

Напишите программу, которая из книг составит стопку, причем каждая следующая меньше предыдущей на 10% и по ширине, и по высоте. Количество книг в стопке вводится, все книги выравниваются по правому краю, первая (нижняя) книга вставляется так, чтобы располагаться снизу справа картинки.

Размер картинки для вставки книг 1000х2000 пикселей, фон белый.

Файл с книгой `book.png` доступен вашему решению.
![alt text](image.png)
Готовое изображение сохраните в файл `stack.png`.

## Пример

**Ввод:**

```
4
```

**Результат работы:**

![alt text](image-1.png)

## Примечание

Из-за округления размеров при умножении на вещественные числа, могут получаться существенно разные значения. Поэтому в данной задаче при вычислении следующих размеров книги в цикле лучше использовать одну из следующих конструкций:

```
a = a * 9 // 10
```

или

```
a = int(0.9 * a)
```