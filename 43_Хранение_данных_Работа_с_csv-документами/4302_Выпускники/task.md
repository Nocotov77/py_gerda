# Выпускники

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Не все выпускники учебных заведений работают по приобретённой специальности. В файле `vps.csv`, который будет доступен вашему решению, находятся сведения о том, сколько выпускников работают или не работают по полученной специальности. Вот несколько первых строк этого файла:

```
Специальность;численность выпускников в тыс. человек;соответствует в тыс. человек;не соответствует в тыс. человек;соответствует в %;не соответствует в %
Математика и механика;29.3;20.6;8.7;70;30
Компьютерные и информационные науки;8.3;6.1;2.2;74;27
Физика и астрономия;8.4;5.8;2.6;69;31
```

Напишите программу, которая получит из стандартного ввода число – у скольких процентов (не менее указанного числа) выпускников специальность работы соответствует полученной, и выведет названия этих специальностей. Каждое с новой строки.

## Формат ввода

Число – не менее такого количества процентов должно быть в поле `соответствует в %`.

## Формат вывода

Названия специальностей, по которым соответствующий % выпускников не меньше введенного числа, каждое с новой строки.

## Пример

**Ввод**
```
90
```

**Вывод**
```
Клиническая медицина
Науки о здоровье и профилактическая медицина
Фармация