def sorting_triple(key, reverse):
    if key == "abc":
        data.sort(reverse=reverse)
    elif key == "len":
        if data and isinstance(data[0], str):
            data.sort(key=len, reverse=reverse)
        else:
            data.sort(key=lambda x: len(str(x)), reverse=reverse)

data = [5, 16, 148, 2]
sorting_triple("len", True)
print(data)
