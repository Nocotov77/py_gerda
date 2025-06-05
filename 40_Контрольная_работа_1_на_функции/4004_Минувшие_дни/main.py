def bygone_days(*args, **kwargs):
    number = kwargs.get("number")
    letters = kwargs.get("letters")
    to_upper = kwargs.get("to_upper")

    res = []
    for s in args:
        if number is not None:
            s = s[::number]
        if letters is not None:
            for char in letters:
                s = s.replace(char, '')
        if to_upper is not None:
            s_list = list(s)
            for i in to_upper:
                if i < len(s_list):
                    s_list[i] = s_list[i].upper()
            s = ''.join(s_list)
        res.append(s)
    return res