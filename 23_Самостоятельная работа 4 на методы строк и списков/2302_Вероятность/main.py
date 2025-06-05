list1 = []

while True:
    s = input()
    if "Калле" in s or "калле" in s or len(s) > 50:
        break
    line = s.split(" ")
    line = "".join(line)
    if line.isupper():
        list1.append(s.lower())
        continue
    if line.isalpha():
        line = s.split(" ")
        for i in range(len(line)):
            line[i] = line[i].capitalize()
        list1.append(" ".join(line))
        continue
    if line.isalnum():
        list1.append(s.upper())
        continue


print(*list1, sep="\n")