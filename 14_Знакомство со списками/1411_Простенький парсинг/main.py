lines = []
while True:
    line = input().strip()
    if line == '</html>':
        break
    lines.append(line)

paragraphs = []
current_paragraph = []
inside_p = False

for line in lines:
    if inside_p:
        if '</p>' in line:
            parts = line.split('</p>', 1)
            part_before = parts[0].strip()
            if part_before:
                current_paragraph.append(part_before)
            if current_paragraph:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
            inside_p = False
            remaining = parts[1]
            if '<p>' in remaining:
                p_parts = remaining.split('<p>')
                for p_part in p_parts[1:]:
                    if '</p>' in p_part:
                        sub_p = p_part.split('</p>', 1)[0].strip()
                        if sub_p:
                            paragraphs.append(sub_p)
                    else:
                        stripped = p_part.strip()
                        if stripped:
                            current_paragraph.append(stripped)
                        inside_p = True
        else:
            stripped_line = line.strip()
            if stripped_line:
                current_paragraph.append(stripped_line)
    else:
        if '<p>' in line:
            p_parts = line.split('<p>')
            for p_part in p_parts[1:]:
                if '</p>' in p_part:
                    sub_parts = p_part.split('</p>', 1)
                    content = sub_parts[0].strip()
                    if content:
                        paragraphs.append(content)
                    remaining = sub_parts[1]
                    if '<p>' in remaining:
                        new_parts = remaining.split('<p>')
                        for new_part in new_parts[1:]:
                            if '</p>' in new_part:
                                sub_new = new_part.split('</p>', 1)[0].strip()
                                if sub_new:
                                    paragraphs.append(sub_new)
                            else:
                                stripped = new_part.strip()
                                if stripped:
                                    current_paragraph.append(stripped)
                                inside_p = True
                else:
                    stripped = p_part.strip()
                    if stripped:
                        current_paragraph.append(stripped)
                    inside_p = True

for p in reversed(paragraphs):
    print(p)