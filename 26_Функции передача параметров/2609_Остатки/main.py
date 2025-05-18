def rests(x):
    return [n % x for n in lst]

lst = [42, 17, 34, 100501]
print(*rests(3))
print(*lst)
