import fileinput
import collections
import itertools
import math
import random

from grid import griddigital as grid

verbose = False
verbose = True

k = [
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  ',
]

pos = (1, 1)

def log(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

def addvec(a, b):
    return [max(min(x+y, 4), 0) for x,y in zip(a,b)]

for line in fileinput.input():
    line = line.strip()
    for c in line:
        v = grid.tovec[c]
        maybepos = addvec(pos, v)
        if grid.index(k, maybepos) != ' ':
            pos = maybepos
    print(grid.index(k, pos), end='')
print()
