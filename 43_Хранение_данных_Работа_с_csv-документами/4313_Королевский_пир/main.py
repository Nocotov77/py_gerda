import sys

data = sys.stdin.read().splitlines()
recipes = {}
products = set()
for line in data:
    if line.strip():
        parts = [x.strip() for x in line.split("\t")]
        r, p, q = parts[0], parts[1], int(parts[2])
        products.add(p)
        recipes.setdefault(r, {})
        recipes[r][p] = recipes[r].get(p, 0) + q
sorted_products = sorted(products)
sorted_recipes = sorted(recipes.keys())
with open("recipes.csv", "w", encoding="utf-8") as f:
    f.write("recipe;" + ";".join(sorted_products) + "\n")
    for rec in sorted_recipes:
        f.write(rec + ";" + ";".join(str(recipes[rec].get(p, 0)) for p in sorted_products) + "\n")