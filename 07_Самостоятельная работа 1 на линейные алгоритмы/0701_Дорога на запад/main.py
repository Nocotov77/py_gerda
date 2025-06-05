n = int(input())
s1 = input()
s2 = input()

if len(s1) <= n and len(s2) <= n:
    print(n)
elif len(s1) > n and len(s2) > n:
    if len(s1) > len(s2):
        print(s2)
    else:
        print(s1)
elif len(s1) > n:
    print(s1)
elif len(s2) > n:
    print(s2)
