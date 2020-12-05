import fileinput, collections, collections as cl, itertools, math, random, sys, re
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

Command = cl.namedtuple('C', 'which x1 y1 x2 y2')

def main():
    f = open(sys.argv[1])
    g = cl.defaultdict(int)
    for line in f:
        line = line.strip()
        line = line.replace(',', ' ').replace('through', ' ').replace('turn ', 'turn')
        cmd = Command(*ints(line.split()))
        for x in range(cmd.x1, cmd.x2 + 1):
            for y in range(cmd.y1, cmd.y2 + 1):
                if cmd.which == 'turnon':
                    g[(x, y)] += 1
                elif cmd.which == 'turnoff':
                    g[(x, y)] = max(0, g[(x, y)] - 1)
                else:
                    g[(x, y)] += 2
    print(sum(v for v in g.values()))


if __name__ == '__main__' and not sys.flags.inspect: main()
