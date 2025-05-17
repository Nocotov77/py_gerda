def graph(func):
    xs = list(range(-10, 11))
    y_values = []
    for x in xs:
        y_values.append(str(eval(func)))
    print("x\t" + "\t".join(str(x) for x in xs))
    print("y\t" + "\t".join(y_values))