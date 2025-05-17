def positions(arg):
    if isinstance(arg, (list, tuple, set)):
        return max(arg) if arg else None
    elif isinstance(arg, (int, float)):
        n = int(arg) + 1
        if n % 2 != 0:
            n += 1
        return n
    elif isinstance(arg, str):
        return len(arg)

print(positions(11.3))


