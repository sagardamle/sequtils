#!/usr/bin/env python

import argparse as ap
from collections import defaultdict
from itertools import combinations, product

def edit_expand(seq, edits = 2, ins = True, alphabet = ['A', 'G', 'C', 'T']):
    """ Compute the shell of related sequences to seed
    edits: number of edits
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

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument('sequence', help = 'Sequence you want to expand')
    parser.add_argument('-e', '--edits', default = 1, help = 'Number of edits you want to expand')
    parser.add_argument('-b', '--allowbulges', dest = 'allowbulges', action = 'store_true', help = 'allow bulges in edit expansions')
    args = parser.parse_args()

    print('\n'.join(expand_sequences(args.sequence, edits = int(args.edits), ins = args.allowbulges)))
