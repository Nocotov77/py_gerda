def without_copies():
    found = False
    i = 0
    while i < len(cow):
        if cow[i] is cow:
            if not found:
                found = True
                i += 1
            else:
                del cow[i]
        else:
            i += 1