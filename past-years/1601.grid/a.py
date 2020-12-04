import fileinput, collections, itertools, math, random
from grid import gridsource as grid
# from grid import make_grid_class
# *, gridnatural, gridcardinal, griddigital
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

for line in fileinput.input():
    f = line.strip()
    break

# grid = make_grid_class('ABCD', 1)  # both arbitrary

pos = (0, 0)
curdir = grid.dirs[0]

for inst in f.split(', '):
    r, *n = inst
    n = int(''.join(n))
    curdir = grid.rot(curdir, r)
    v = grid.mulvec(curdir, n)
    pos = grid.addvec(pos, v)
print(grid.absmanhattan(pos))
