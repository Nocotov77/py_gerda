# Фруктовый микс

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Представьте, что вы пришли домой и решили побаловать себя любимым фруктовым миксом. А тут вдруг выясняется, то ваш любимый дуриан закончился. Набираете в поисковике ближайшие продуктовые магазины и получаете словарь `отдел: список товаров` для каждого из них. Осталось найти, в каком из них продают любимый фрукт!

Напишите функцию `search_fruit(shops, fruit)`, которая принимает аргументы — словарь магазинов (ключ: название, значение: словарь отделов (ключ: название отдела, значение: список фруктов)) и любимый фрукт (без учёта регистра), а возвращает кортеж: `(название магазина, название отдела)`, в котором он есть, или `(None, None)`, если его нигде не нашлось.

**Пример 1**

**Ввод**
```python
shops = {'Шестёрочка': {'Консервы': ['Ананасы кусочками', 'Ананасы колечками'], 'Сухофрукты': ['Тропические ананасы', 'Дуриан вяленый'], 'Фрукты': ['Бананы', 'Манго']}, 'Микси': {'Овощи-фрукты': ['Яблоки', 'Груши', 'Личи']}}
fruit = "Дуриан"
print(*search_fruit(shops, fruit))
```

**Вывод**
```
Шестёрочка Сухофрукты
```

**Пример 2**

**Ввод**
```python
shops = {'Шестёрочка': {'Консервы': ['Ананасы кусочками', 'Ананасы колечками'], 'Сухофрукты': ['Тропические ананасы', 'Дуриан вяленый'], 'Фрукты': ['Бананы', 'Манго']}, 'Микси': {'Овощи-фрукты': ['Яблоки', 'Груши', 'Личи']}}
fruit = "Личи"
print(*search_fruit(shops, fruit))
```

**Вывод**
```
Микси Овощи-фрукты
```

**Примечания**

В тестирующую систему сдайте только функцию, но не код, её вызывающий.