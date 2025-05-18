def dried_apricots(new_weights):
    for i, nw in enumerate(new_weights):
        if nw <= apricots[i] / 2:
            apricots[i] = 0
        elif nw > apricots[i]:
            apricots[i] = nw

apricots = [3, 5, 7.5, 18]
dried_apricots([1.5, 5.1, 3.74, 15])
print(apricots)
dried_apricots([0, 2.6, 0, 8])
print(apricots)
dried_apricots([0, 2.45, 0, 0])
print(apricots)
