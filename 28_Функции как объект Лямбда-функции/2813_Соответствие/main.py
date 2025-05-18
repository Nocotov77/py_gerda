
def trend(*data, **funcs):
    return next((name for name, f in funcs.items()
                 if all(map(lambda d: abs(f(d[0]) - d[1]) <= 0.01, data))), None)
