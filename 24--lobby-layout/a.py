import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    decode = {
        'e': (0, 2),
        'ne': (-1, 1),
        'nw': (-1, -1),
        'w': (0, -2),
        'se': (1, 1),
        'sw': (1, -1),
    }
    black = set()
    for line in f:
        line = line.strip()
        moves = parse(line)
        pos = (0, 0)
        for m in moves:
            pos = grid.addvec(pos, decode[m])
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)
    print(len(black))

def parse(line):
    res = []
    while line:
        if line.startswith('ne'):
            res.append('ne')
            line = line[2:]
        elif line.startswith('nw'):
            res.append('nw')
            line = line[2:]
        elif line.startswith('se'):
            res.append('se')
            line = line[2:]
        elif line.startswith('sw'):
            res.append('sw')
            line = line[2:]
        elif line.startswith('e'):
            res.append('e')
            line = line[1:]
        elif line.startswith('w'):
            res.append('w')
            line = line[1:]
        else: 1/0
    return res

main() # if __name__ == '__main__' and not sys.flags.inspect: main()

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
