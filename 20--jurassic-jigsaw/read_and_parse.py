import sys
import collections
from helpers import *

def read_and_parse():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tiles = [parse(t) for t in f.read().split('\n\n')]
    tids_by_border = collections.defaultdict(set)
    for t in sorted(tiles):
        bs = get_borders(t.lines, True)
        for b in sorted(bs):
            tids_by_border[b].add(t.tid)
    return tiles, tids_by_border
