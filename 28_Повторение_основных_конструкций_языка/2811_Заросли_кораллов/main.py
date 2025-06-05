coral = input()
sea = input()
result = ""
i = 0
in_non = False
while i < len(sea):
    if sea[i:i + len(coral)] == coral:
        result += coral
        i += len(coral)
        in_non = False
    else:
        if not in_non:
            result += sea[i]
            in_non = True
        else:
            result += "-" + sea[i]
        i += 1
print(result)