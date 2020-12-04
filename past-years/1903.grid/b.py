import fileinput, collections, itertools, math, random
# from grid import griddigital as grid
from grid import make_grid_class
# *, gridnatural, gridcardinal, griddigital
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

seen = set()

grid = make_grid_class('RDLU', 1)
vals = {}

f = [line.strip() for line in fileinput.input()]

pos = (0, 0)
val = 0
for inst in f[0].split(','):
    d, *n = inst
    n = int(''.join(n))
    v = grid.tovec[d]
    for i in range(n):
        pos = grid.addvec(pos, v)
        val += 1
        seen.add(pos)
        vals[pos] = val

inters = []

pos = (0, 0)
val = 0
for inst in f[1].split(','):
    d, *n = inst
    n = int(''.join(n))
    v = grid.tovec[d]
    for i in range(n):
        pos = grid.addvec(pos, v)
        val += 1
        if pos in seen:
            inters.append(vals[pos] + val)

# dists = [grid.absmanhattan(inter) for inter in inters]
print(min(inters))
