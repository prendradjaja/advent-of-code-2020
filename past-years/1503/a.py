import fileinput, collections, itertools, math, random, sys, re
from grid import make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    # counts = collections.defaultdict(lambda: collections.defaultdict(int))
    counts = collections.defaultdict(int)
    grid = make_grid_class('^<v>', 1)
    pos = (0, 0)
    for line in fileinput.input():
        line = line.strip()
        break
    counts[pos] += 1
    for c in line:
        pos = grid.move(pos, c, 1)
        counts[pos] += 1
    print(len(counts))



if __name__ == '__main__' and not sys.flags.inspect: main()
