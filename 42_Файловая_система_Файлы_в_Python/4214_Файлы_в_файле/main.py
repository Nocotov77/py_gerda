multipliers = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4}
units = [("TB", 1024**4), ("GB", 1024**3), ("MB", 1024**2), ("KB", 1024), ("B", 1)]
groups = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            fname = parts[0]
            vol = float(parts[1])
            unit = parts[2]
            ext = fname.split(".")[-1].lower()
            bytes_val = vol * multipliers[unit]
            groups.setdefault(ext, []).append((fname, bytes_val))
output_blocks = []
for ext in sorted(groups.keys()):
    files = sorted(groups[ext], key=lambda x: x[0])
    total_bytes = sum(data[1] for data in files)
    for u, factor in units:
        if total_bytes / factor >= 1:
            value = round(total_bytes / factor)
            chosen = u
            break
    block = [file[0] for file in files]
    block.append("----------")
    block.append(f"Summary: {value} {chosen}")
    output_blocks.append("\n".join(block))
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(output_blocks))