from itertools import combinations, product

def edit_expand(seq, edits = 2, ins = True, alphabet = ['A', 'G', 'C', 'T']):
    """ Compute the shell of related sequences to seed
    i: number of edits
    ins: allow insertions (bulges)
    alphabet: sequence alphabet
    
    Returns:
    generator of neighbor sequences
    """
    insalphabet_dict = {l: [] for l in alphabet}
    seq = seq
    seqlist = list(seq)
    if ins:
        for nuc in alphabet + [' ']:
            insalphabet = [l + nuc for l in alphabet]
            insalphabet += ['']
            insalphabet_dict[nuc] = insalphabet
    
    for d in range(edits + 1):
        for locs in combinations(range(len(seq)), d):
            thisseq = seqlist.copy()
            for loc in locs:
                origchar = seq[loc]
                if loc:
                    thisseq[loc] = [l for l in alphabet + insalphabet_dict[origchar] if l != origchar]
                else:
                    thisseq[loc] = [l for l in alphabet + [''] if l != origchar]
            for poss in product(*thisseq):
                yield "".join(poss)

def expand_sequences(*args, **kwargs):
    return list(set(filter(None, edit_expand(*args, **kwargs))))

results = expand_sequences('GT', edits = 1)
