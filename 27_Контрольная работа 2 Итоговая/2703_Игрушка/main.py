line = input()

list1 = line.split(", ")
result = []

for i in range(len(list1)):
    if "i" in list1[i] or "I" in list1[i]:
        result.append(list1[i].upper())

result.sort(reverse=True)
print("With letter:", "@".join(result))
result.clear()

for i in range(len(list1)):
    if len(list1[i]) % 2 == 0:
        result.append(list1[i].capitalize())
result.sort(reverse=True)
print("Even length:", "@".join(result))
result.clear()

seen = set()
for i in range(len(list1)):
    for ch in list1[i]:
        if ch in seen:
            result.append(list1[i].lower())
            break
        else:
            seen.add(ch)
    seen.clear()

result.sort(reverse=True)
print("Repeated:", "@".join(result))