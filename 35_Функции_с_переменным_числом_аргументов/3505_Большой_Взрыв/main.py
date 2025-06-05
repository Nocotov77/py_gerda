def future(*masses, **constants):
    prod = 1
    for v in constants.values():
        prod *= v
    total = sum(masses) * prod
    if total > VIN:
        return "ACCELERATION"
    elif total < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"