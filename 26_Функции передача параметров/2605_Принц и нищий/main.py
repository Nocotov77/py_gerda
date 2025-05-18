def change():
    prince[:], pauper[:] = pauper[:], prince[:]

prince = [1, 2, 3]
pauper = ["one", "two", "three"]
old_prince = prince.copy()
old_pauper = pauper.copy()
change()
print(prince, old_pauper, prince == old_pauper)
print(pauper, old_prince, pauper == old_prince)
