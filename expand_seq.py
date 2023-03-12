from itertools import combinations, product
from collections import defaultdict

def edit_expand(seq, edits = 2, ins = True, alphabet = ['A', 'G', 'C', 'T']):
    """ Compute the shell of related sequences to seed
    i: number of edits
    ins: allow insertions (bulges)
    alphabet: sequence alphabet
    
    Returns:
    generator of neighbor sequences
    """
    seqlist = list(seq)
    insalphabet_dict = defaultdict(list)
    
    if ins:
        for nuc in alphabet:
            insalphabet_dict[nuc] += [l + nuc for l in alphabet] + ['']
    
    for d in range(edits + 1):
        for locs in combinations(range(len(seq)), d):
            thisseq = seqlist.copy()
            for loc in locs:
                origchar = seq[loc]
                if loc == 0:
                    if ins:
                        thisseq[loc] = [l for l in alphabet + [''] if l != origchar]
                    else:
                        thisseq[loc] = [l for l in alphabet if l != origchar]
                else:
                    thisseq[loc] = [l for l in alphabet + insalphabet_dict[origchar] if l != origchar]
                    
            for poss in product(*thisseq):
                yield "".join(poss)

def expand_sequences(*args, **kwargs):
    return list(set(filter(None, edit_expand(*args, **kwargs))))

gg = expand_sequences('GTC', edits = 1, ins = False)
