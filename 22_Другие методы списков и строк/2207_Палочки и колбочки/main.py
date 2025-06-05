s = input().strip()
light = int(input())

if light > 100:
    s = s.replace("0000", "|||")
else:
    s = s.replace("|||", "00", 3)

s = s.replace("|0|", "|00|", 1)

print(s)