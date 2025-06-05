def placeholder(*lines, **holders):
    def gen_pattern(sentence):
        tokens = sentence.split()
        res_tokens = []
        for token in tokens:
            if token and not token[-1].isalpha():
                word, punct = token[:-1], token[-1]
            else:
                word, punct = token, ""
            res_tokens.append(("|_" if word and word[0].isupper() else "_") + punct)
        return " ".join(res_tokens)
    out = {}
    for line in lines:
        pat = gen_pattern(line)
        for scheme in holders.values():
            if pat == scheme:
                out.setdefault(scheme, []).append(line)
    for scheme in out:
        out[scheme].sort()
    return out