# Сердитый Йода

Когда Йода хмурится, темнеет вокруг и собираются тучи. Когда Йода спокоен, и вокруг светло и весело.

Напишите программу, которая изменяет яркость пикселей в соответствии с введенным числом `n`.

## Правило

Для каждого пикселя нужно:

1.  Найти максимальную разность компонент цвета.
2.  Разделить эту разность на `n`, округлив до целого вниз.
3.  Прибавить полученное значение к каждой компоненте.

Если `n` отрицательное, то получится вычитание, а не сложение.

## Входные данные

Файл с Йодой `yoda.png` доступен вашему решению.
![alt text](image.png)
## Выходные данные

Преобразованное изображение сохраните в файл `sense.png`.

## Примеры

### Пример 1

**Ввод:**

```
-2
```

**Результат:**

![alt text](image-1.png)

### Пример 2

**Ввод:**

```
3
```

**Результат:**

![alt text](image-2.png)