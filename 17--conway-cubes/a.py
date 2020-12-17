import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
# from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    active = set()
    for x, line in enumerate(f):
        for y, c in enumerate(line.strip()):
            if c == '#':
                active.add((x, y, 0))
    def extent():
        res = []
        for d in range(3):
            lo = min(x[d] for x in active) - 1
            hi = max(x[d] for x in active) + 2
            res.append((lo, hi))
        return res
    def tick():
        newa = set()
        ext = extent()
        xr, yr, zr = extent()
        for x in range(*xr):
            for y in range(*yr):
                for z in range(*zr):
                    n = livenei(x, y, z)
                    if (x, y, z) in active:
                        if n in [2,3]:
                            newa.add((x, y, z))
                    else:
                        if n == 3:
                            newa.add((x, y, z))
        return newa
    def neighbors(x, y, z):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if not (dx == dy == dz == 0):
                        yield (dx + x, dy + y, dz + z)
    def livenei(x, y, z):
        r = 0
        for pos in neighbors(x, y, z):
            if pos in active:
                r += 1
        return r
    for i in range(6):
        active = tick()
    print(len(active))


main() # if __name__ == '__main__' and not sys.flags.inspect: main()
