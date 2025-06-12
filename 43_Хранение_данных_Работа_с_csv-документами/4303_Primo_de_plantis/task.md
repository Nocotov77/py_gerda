# Primo de plantis

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод

**Вывод:** plantis.csv

Среди учёных-ботаников принято называть растения по их латинским наименованиям. Они состоят из двух слов: собственно название и определение, которое может указывать на какие-либо отличительные особенности растения, на время цветения или место обитания.

Напишите программу, которая составит справочник по введённым растениям, записав в файл plantis.csv следующие их характеристики:

название, определение, характеристика, русское название, семейство, русское название семейства
(nomen, definitio, pluma, Russian nomen, familia, Russian nomen familia)

## Формат ввода

Вводятся строки, каждая соответствует одному растению. Все характеристики разделены символом табуляции.

## Формат вывода

В файл вывести строку заголовков, затем все данные о растениях, разделитель – точка с запятой.

## Пример

**Ввод:**
```
Adonis	sibirica	Patrin ex Ledeb	Стародубка сибирская	Ranunculaceae	Лютиковые
Artemisia	laciniata	Willd.	Полынь рассеченная	Asteraceae	Астровые
Cypripedium	guttatum	Sw.	Башмачок капельный	Orchidaceae	Орхидные
Galium	uliginosum	L.	Подмаренник топяной	Rubiaceae	Мареновые
Geum	rivale	L.	Гравилат речной	Rosaceae	Розоцветные
```

**Вывод:**
```
nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia
Adonis;sibirica;Patrin ex Ledeb;Стародубка сибирская;Ranunculaceae;Лютиковые
Artemisia;laciniata;Willd.;Полынь рассеченная;Asteraceae;Астровые
Cypripedium;guttatum;Sw.;Башмачок капельный;Orchidaceae;Орхидные
Galium;uliginosum;L.;Подмаренник топяной;Rubiaceae;Мареновые
Geum;rivale;L.;Гравилат речной;Rosaceae;Розоцветные