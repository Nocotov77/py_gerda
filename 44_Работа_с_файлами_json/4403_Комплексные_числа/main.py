import sys
import json
import re

pattern = re.compile(r"z\s*=\s*([+-]?\d+(?:\.\d+)?)\s*([+-])\s*(\d+(?:\.\d+)?)\s*\*\s*i")
lines = sys.stdin.read().splitlines()
result = {"complex": []}
for line in lines:
    line = line.strip()
    if line:
        m = pattern.match(line)
        if m:
            re_val = float(m.group(1))
            im_val = float(m.group(3))
            if m.group(2) == "-":
                im_val = -im_val
            result["complex"].append({"Re": re_val, "Im": im_val})
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)