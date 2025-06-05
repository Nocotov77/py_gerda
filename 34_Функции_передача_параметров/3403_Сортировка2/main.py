def sorting_bis(key, reverse):
    if key == "abc":
        data.sort(reverse=reverse)
    elif key == "len":
        data.sort(key=len, reverse=reverse)