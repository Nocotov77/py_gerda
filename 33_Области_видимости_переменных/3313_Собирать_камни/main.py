from math import sin, radians, sqrt


def collect_stones():
    global L, ALPHA
    v = sqrt(L * 9.8 / sin(radians(2 * ALPHA)))
    L += 0.5
    return v