# Верхние широты

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Напишите функцию `latitude(phi)`, которая находит радиус `R` окружности, образованной параллелью на широте ϕ местности. Радиус Земли `r = 6370` км. Полученное значение округлить до целых километров.

Тригонометрические функции можно получить из встроенного модуля `math`:

```python
from math import sin, cos, radians
```

Широта передается в градусах, в тригонометрические функции значение передается в радианах.

**Пример**

| Ввод        | Вывод |
|-------------|-------|
| `latitude(55)` | `3654` |