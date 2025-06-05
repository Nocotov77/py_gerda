import sys
lines = list(filter(None, sys.stdin.read().splitlines()))
print("FAIL" if all(map(lambda line: any(map(lambda x: int(x) % 5 == 0, line.split("; "))), lines)) 
      else "OK")