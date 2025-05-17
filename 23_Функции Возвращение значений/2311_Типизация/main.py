def typification(data):
    d = {}
    for item in data:
        if type(item) is bool:
            key = 'bool'
        elif type(item) is int:
            key = 'int'
        elif type(item) is float:
            key = 'float'
        elif type(item) is str:
            key = 'str'
        elif type(item) is tuple:
            key = 'tuple'
        elif type(item) is list:
            key = 'list'
        elif type(item) is dict:
            key = 'dict'
        elif type(item) is set:
            key = 'set'
        else:
            continue
        if key in d:
            d[key].append(item)
        else:
            d[key] = [item]
    return d

data = eval(input())
print(typification(data))
