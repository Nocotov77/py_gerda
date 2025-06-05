def search_fruit(shops, fruit):
    target = fruit.lower()
    for shop, departments in shops.items():
        for dept, fruits in departments.items():
            for item in fruits:
                if target in item.lower():
                    return (shop, dept)
    return (None, None)