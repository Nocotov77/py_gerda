# Плакаты-2

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** in_file.txt

**Вывод:** sorted.csv

Теперь вашей программе нужно будет отсортировать данные по нескольким ключам.

Напомним условие.

Интернет-магазин продаёт плакаты по разным темам. В файле posters.csv записан прайс-лист, в котором указаны id постера, раздел, к которому он относится, размеры по горизонтали и вертикали, цена, дата добавления.

Вашей программе будет доступен файл posters.csv файл.

Напишите программу, которая считает из входного файла in_file.txt названия полей, по которым нужно отсортировать данные, каждое название с новой строки, отсортирует и запишет в файл sorted.csv. В случае, если сортировку надо производить по целочисленным полям, они сравниваются как числа, а не как строки. Даты – это строки.

Заголовки файла posters.csv:
`id;section;h_dimension;v_dimension;price;date`

Разделитель точка с запятой.

Пример начала файла с данными:
```
id;section;h_dimension;v_dimension;price;date
1216077;Пионы;816;1007;8067;2004-10-26
1704116;Графика;979;426;5861;2000-12-28
1545917;Абстракции;648;457;4545;2015-09-02
1384281;Животные;1900;1383;7006;2009-03-26
1503102;Мосты;556;1270;6781;2020-03-03
1687854;Природа;137;1134;2141;2011-11-16
1401867;Графика;689;754;1998;2007-06-19
1187989;Индия;1428;977;6418;2018-11-07
```

Пример файла in_file.txt:
```
v_dimension
price
date