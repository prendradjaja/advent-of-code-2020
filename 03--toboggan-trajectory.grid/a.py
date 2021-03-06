import fileinput, collections, itertools, math, random
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

g = []

for line in fileinput.input():
    g.append(line.strip())

h = len(g)
w = len(g[0])

def index(g, r, c):
    return g[r][c % w]

slope = (1, 3)
pos = (0, 0)
trees = 0

while pos[0] < h:
    trees += index(g, *pos) == '#'
    pos = grid.addvec(pos, slope)

print(trees)
