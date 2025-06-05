def dried_apricots(new_weights):
    for i, nw in enumerate(new_weights):
        if nw <= apricots[i] / 2:
            apricots[i] = 0
        elif nw > apricots[i]:
            apricots[i] = nw