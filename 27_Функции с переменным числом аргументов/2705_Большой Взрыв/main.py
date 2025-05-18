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

VIN = 3
mass = [1, 2, 3, 4]
const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
print(future(*mass, **const))