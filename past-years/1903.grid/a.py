import fileinput, collections, itertools, math, random
from grid import gridsource as grid
# from grid import make_grid_class
# *, gridnatural, gridcardinal, griddigital
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

seen = set()

# grid = make_grid_class('RDLU', 1)

f = [line.strip() for line in fileinput.input()]

pos = (0, 0)
for inst in f[0].split(','):
    d, *n = inst
    n = int(''.join(n))
    v = grid.tovec[d]
    for i in range(n):
        pos = grid.addvec(pos, v)
        seen.add(pos)

inters = []

pos = (0, 0)
for inst in f[1].split(','):
    d, *n = inst
    n = int(''.join(n))
    v = grid.tovec[d]
    for i in range(n):
        pos = grid.addvec(pos, v)
        if pos in seen:
            inters.append(pos)

dists = [grid.absmanhattan(inter) for inter in inters]
print(min(dists))
