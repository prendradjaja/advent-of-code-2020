import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridcardinal as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    pos = (0, 0)
    d = (0, 1)
    for line in f:
        line = line.strip()
        c = line[0]
        n = int(line[1:])
        if c in 'NSEW':
            pos = grid.move(pos, c, n)
        elif c in 'RL':
            n = n // 90
            for _ in range(n):
                d  = grid.rot(d, c)
        elif c == 'F':
            pos = grid.move(pos, d, n)
        else: 1/0
    p(grid.absmanhattan(pos))


main() # if __name__ == '__main__' and not sys.flags.inspect: main()
