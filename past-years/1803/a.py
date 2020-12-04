import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

Claim = collections.namedtuple('Claim', 'idnum x y w h')

def main():
    f = open(sys.argv[1])
    claims = []
    nclaims = cl.defaultdict(int)
    for line in f:
        line = line.strip()
        line = (line
            .replace('#', '')
            .replace(' @ ', ' ')
            .replace(',', ' ')
            .replace('x', ' ')
            .replace(':', '')
        )
        claims.append(Claim(*[int(x) for x in line.split()]))
    log(claims[0])
    log(claims[-1])
    for c in claims:
        for i in range(c.w):
            for j in range(c.h):
                pos = (c.x + i, c.y + j)
                nclaims[pos] += 1
    print(len(list(None for n in nclaims.values() if n >= 2)))

if __name__ == '__main__' and not sys.flags.inspect: main()
