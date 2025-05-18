def sorting_bis(key, reverse):
    if key == "abc":
        data.sort(reverse=reverse)
    elif key == "len":
        data.sort(key=len, reverse=reverse)

data = ["one", "two", "three"]
sorting_bis("abc", False)
print(data)
