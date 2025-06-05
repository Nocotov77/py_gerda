import sys

lines = sys.stdin.read().splitlines()
amb_parts = lines[-1].split()
amb = float(amb_parts[0]) + 273.15 if amb_parts[1] == "C" else float(amb_parts[0])
liquid = {
    line.split()[0] for line in lines[:-1] if (float(line.split()[1]) + 273.15 
                                               if line.split()[2] == "C" else float(line.split()[1])) 
    < amb}
print("\n".join(liquid))