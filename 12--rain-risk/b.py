import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridcardinal as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    pos = (0, 0)
    wp = (-1, 10)
    for line in f:
        line = line.strip()
        c = line[0]
        n = int(line[1:])
        if c in 'NSEW':
            wp = grid.move(wp, c, n)
        elif c in 'RL':
            for i in range(n // 90):
                wp = grid.rotvec(wp, c)
        elif c == 'F':
            pos = grid.move(pos, wp, n)
        else: 1/0
    p(grid.absmanhattan(pos))

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
