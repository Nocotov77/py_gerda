import sys
from collections import Counter

data = sys.stdin.read().splitlines()
freq = Counter()
terminals = ("UAA", "UGA", "UAG")
for line in data:
    start_idx = line.find("AUG")
    if start_idx == -1:
        continue
    region = line[start_idx + 3:]
    pos = [region.find(t) for t in terminals if region.find(t) != -1]
    if pos:
        term_offset = min(pos)
        coding = region[:term_offset]
    else:
        coding = region
    coding = coding[:(len(coding) // 3) * 3]
    for i in range(0, len(coding), 3):
        freq[coding[i: i + 3]] += 1
result = sorted(freq.items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]
for codon, count in result:
    print(f"{codon}: {count}")