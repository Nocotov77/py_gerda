def to_bytes(value, unit):
    conv = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
    return value * conv[unit]


def in_largest_units(value):
    for unit, factor in (("GB", 1024**3), ("MB", 1024**2), ("KB", 1024), ("B", 1)):
        if value >= factor:
            return f"{round(value / factor)} {unit}"