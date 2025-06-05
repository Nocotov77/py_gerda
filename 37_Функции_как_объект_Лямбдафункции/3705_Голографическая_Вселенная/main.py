def hologram(*strings, transformation=1):
    funcs = {
        1: lambda s: " ".join(map(lambda w: w.title(), s.split())),
        2: lambda s: s[::2],
        3: lambda s: str(len(s)),
        4: lambda s: "".join(sorted(set(s))) if len(s) % 2 != 0 else s
    }
    return list(map(funcs[transformation], strings))