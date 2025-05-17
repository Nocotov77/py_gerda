def supercargo(load, capacity):
    cap_top, cap_mid, cap_low = capacity
    unassigned = []
    for cargo in load:
        d = len(str(abs(cargo)))
        if d == 1:
            if cap_top:
                cap_top -= 1
            else:
                unassigned.append(cargo)
        elif d == 2:
            if cap_mid:
                cap_mid -= 1
            else:
                unassigned.append(cargo)
        elif d == 3:
            if cap_low:
                cap_low -= 1
            else:
                unassigned.append(cargo)
        else:
            unassigned.append(cargo)
    full = (cap_top == 0 and cap_mid == 0 and cap_low == 0)
    return (tuple(unassigned), full)

loads_data = (23, 12, 1, 345, 123, 3, 9999)
capacity_data = (2, 1, 0)
res = supercargo(loads_data, capacity_data)
print(res[0], res[-1], sep="\n")
loads_data = (23, 12, 1, 345, 123, 3)
capacity_data = (2, 2, 3)
res = supercargo(loads_data, capacity_data)
print(res[0], res[-1], sep="\n")