def refinement(lst):
    if not hasattr(refinement, "data"):
        refinement.data = []
    refinement.data += lst
    s = sum(refinement.data)
    p = s % 2
    filt = [x for x in refinement.data if x % 2 == p]
    return sum(filt) / len(filt) if filt else 0