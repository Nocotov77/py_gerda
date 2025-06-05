from math import cos, pi


def latitude(phi):
    print(round(6370 * cos(phi * pi / 180)))