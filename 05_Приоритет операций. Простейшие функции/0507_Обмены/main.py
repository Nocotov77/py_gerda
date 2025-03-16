a = int(input())
b = int(input())
c = int(input())

largest = max(a, b, c)
medium = 0
smallest = min(a, b, c)

if smallest < a < largest or a == b or a == c:
    medium = a
elif smallest < b < largest or b == a or b == c:
    medium = b
elif smallest < c < largest or c == a or c == b:
    medium = c

print(largest, medium, smallest, sep='\n')