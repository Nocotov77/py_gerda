import sys
lines = list(filter(lambda s: s, sys.stdin.read().splitlines()))
print("EVERGREEN TOMATOES"
      if all(map(lambda row: sum(1 for x in row.split() if "0" not in x)
                 >= sum(1 for x in row.split() if "0" in x), lines)) else "ALUMINUM CUCUMBERS")
