def molecule_assembly(*args, overwrite=False):
    global dna_chain, molecule_dna
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    if not args:
        return [x + y for x, y in molecule_dna]
    available = args[0]
    if len(args) == 2:
        new_chain = args[1]
        if overwrite:
            dna_chain = new_chain
        else:
            dna_chain += new_chain
    while dna_chain:
        nuc = dna_chain[0]
        if nuc not in comp:
            dna_chain = dna_chain[1:]
            continue
        needed = comp[nuc]
        if needed in available:
            dna_chain = dna_chain[1:]
            available.remove(needed)
            molecule_dna.append((nuc, needed))
        else:
            break
    return [x + y for x, y in molecule_dna]