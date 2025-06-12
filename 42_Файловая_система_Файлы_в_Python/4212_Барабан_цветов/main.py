import re


def color_search(*args, filename="output.txt"):
    colors = []
    with open("flower_drum.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"^(.*?)\s+(#[A-Fa-f0-9]+)\s+(\d+)\s+(\d+)\s+(\d+)", line)
            if m:
                name = m.group(1)
                hex_code = m.group(2)
                r = int(m.group(3))
                g = int(m.group(4))
                b = int(m.group(5))
                colors.append((name, hex_code, r, g, b))
    by_name = {entry[0]: entry for entry in colors}
    by_hex = {entry[1]: entry for entry in colors}
    by_rgb = {(entry[2], entry[3], entry[4]): entry for entry in colors}
    output_lines = []
    if args:
        first_arg = args[0]
        if isinstance(first_arg, str):
            if first_arg.startswith("#"):
                for query in args:
                    entry = by_hex.get(query)
                    if entry:
                        output_lines.append(f"{entry[1]}\t{entry[0]}\t{entry[2]}\t{entry[3]}\t{entry[4]}")
            else:
                for query in args:
                    entry = by_name.get(query)
                    if entry:
                        output_lines.append(f"{entry[0]}\t{entry[1]}\t{entry[2]}\t{entry[3]}\t{entry[4]}")
        else:
            for query in args:
                entry = by_rgb.get(tuple(query))
                if entry:
                    output_lines.append(f"{entry[2]}\t{entry[3]}\t{entry[4]}\t{entry[0]}\t{entry[1]}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))