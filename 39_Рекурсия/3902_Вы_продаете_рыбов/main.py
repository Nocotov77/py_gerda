def change(line, sub, symb):
    if line == "":
        return ""
    return (symb if line[0] == sub else line[0]) + change(line[1:], sub, symb)