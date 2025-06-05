def prompter(s):
    if not hasattr(prompter, "mem"):
        prompter.mem = []
    for full in prompter.mem:
        if s in full:
            return full
    prompter.mem.append(s)
    return s