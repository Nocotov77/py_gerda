import sys
from math import floor

disc = int(input())

if disc == 0:
    disc = 50
    print(disc)
    sys.exit()

if disc <= 30:
    disc += disc / 2
    print(floor(disc))
    sys.exit()

if 30 < disc <= 70:
    disc += disc / 100 * 10
    print(floor(disc))
    sys.exit()

if disc > 70:
    print(disc)
