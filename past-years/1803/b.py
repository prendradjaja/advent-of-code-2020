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
    pclaims = cl.defaultdict(set)
    inters = set()
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
                if pclaims[pos]:
                    for prior in pclaims[pos]:
                        inters.add(tuple(repr(str(x)) for x in sorted([c.idnum, prior])))
                pclaims[pos].add(c.idnum)

    s = str(inters)
    log(s[:100])
    for c in claims:
        if f"'{c.idnum}'" not in s:
            print(c.idnum)

    # print(len(list(None for n in nclaims.values() if n >= 2)))

if __name__ == '__main__' and not sys.flags.inspect: main()
