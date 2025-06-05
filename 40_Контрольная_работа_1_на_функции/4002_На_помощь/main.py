def to_rescue(arg, additional='-'):
    global need_help
    length = len(arg)
    result = []
    chars = set(arg)
    for i in range(len(need_help)):
        word = set(need_help[i])
        word = list(word)
        word = "".join(word)
        filchar = [char for char in word if char not in chars]
        filchar.sort()
        filchar = ''.join(filchar)
        if len(filchar) < length:
            num = length - len(filchar)
            filchar = filchar + additional * num
        result.append(filchar)
    need_help = result