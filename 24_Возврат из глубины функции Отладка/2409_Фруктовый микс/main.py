def search_fruit(shops, fruit):
    target = fruit.lower()
    for shop, departments in shops.items():
        for dept, fruits in departments.items():
            for item in fruits:
                if target in item.lower():
                    return (shop, dept)
    return (None, None)

shops = {'Шестёрочка': {'Консервы': ['Ананасы кусочками', 'Ананасы колечками'], 'Сухофрукты': ['Тропические ананасы', 'Дуриан вяленый'], 'Фрукты': ['Бананы', 'Манго']}, 'Микси': {'Овощи-фрукты': ['Яблоки', 'Груши', 'Личи']}}
fruit = "Дуриан"
print(*search_fruit(shops, fruit))

shops = {'Шестёрочка': {'Консервы': ['Ананасы кусочками', 'Ананасы колечками'], 'Сухофрукты': ['Тропические ананасы', 'Дуриан вяленый'], 'Фрукты': ['Бананы', 'Манго']}, 'Микси': {'Овощи-фрукты': ['Яблоки', 'Груши', 'Личи']}}
fruit = "Личи"
print(*search_fruit(shops, fruit))