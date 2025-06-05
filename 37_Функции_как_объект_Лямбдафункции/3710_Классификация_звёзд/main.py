def stars(m, t):
    return f"This is a star of {m} solar masses and {t} K."


def black_hole(m):
    return f"This is black hole of {m} solar masses."


def non_type(t):
    return f"This is an unidentified object of {t} K."


def star_type(m, t=None, determinant=lambda m, t: (m, t)):
    if t is None:
        return black_hole(m)
    if m == 0:
        return non_type(t)
    m, t = determinant(m, t)
    return stars(m, t)