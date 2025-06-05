def defender(lines):
    list1 = []
    d1 = dict()
    for i in range(len(lines)):
        list1.append(len(lines[i]))
    list1 = list(dict.fromkeys(list1))
    for i in range(len(list1)):
        for j in range(len(lines)):
            if list1[i] == len(lines[j]):
                d1[list1[i]] = d1.get(list1[i], []) + [lines[j]]
    return d1