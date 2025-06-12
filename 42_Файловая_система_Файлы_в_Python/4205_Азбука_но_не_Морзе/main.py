import sys
lines = sys.stdin.read().splitlines()
filename = lines[0].strip()
with open(filename, "r", encoding="utf-8") as f:
    mapping_lines = f.read().splitlines()
mapping = {}
for mapping_line in mapping_lines:
    parts = mapping_line.strip().split()
    if parts:
        mapping[parts[1]] = parts[0]
decoded = []
for code_line in lines[1:]:
    if code_line.strip():
        codes = code_line.split()
        decoded.append("".join(mapping[c] for c in codes))
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(decoded))