import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    twos, threes = 0, 0
    for line in f:
        line = line.strip()
        cts = collections.Counter(line)
        if 2 in cts.values():
            twos += 1
        if 3 in cts.values():
            threes += 1
    print(twos*threes)

if __name__ == '__main__' and not sys.flags.inspect: main()
