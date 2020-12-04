import fileinput, collections, itertools, math, random
# from grid import griddigital as grid
from grid import make_grid_class
# *, gridnatural, gridcardinal, griddigital
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

keypad = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9,]
]

grid = make_grid_class('RDLU', 1)  # rotdir arbitrary

pos = (1, 1)

def clamp(lo, hi, n):
    return max(min(n, hi), lo)

def clampvec(v):
    return tuple(clamp(0, 2, x) for x in v)

for line in fileinput.input():
    line = line.strip()
    for c in line:
        v = grid.tovec[c]
        pos = grid.addvec(pos, v)
        pos = clampvec(pos)
    print(grid.index(keypad, pos), end='')
print()
