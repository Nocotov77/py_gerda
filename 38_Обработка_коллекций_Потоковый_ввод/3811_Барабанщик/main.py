import sys


vowels = set("аяоёуюэеиы")
data = sys.stdin.read().strip()
if not data:
    exit()
lines = list(map(str.strip, data.split("! ")))
groups = {}
for line in lines:
    cnt = sum(1 for ch in line.lower() if ch in vowels)
    groups.setdefault(cnt, []).append(line)
keys = sorted([k for k, v in groups.items() if len(v) > 1], reverse=True)
out = []
for i, k in enumerate(keys):
    out.extend(groups[k])
    if i < len(keys) - 1:
        out.append("")
print("\n".join(out))