a, b, *r = input().split() 
print(*filter(lambda x: len(set(x.lower()) & set(b.lower())) >= 6, [a, b] + r), sep=", ")