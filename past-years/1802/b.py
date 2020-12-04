import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    twos, threes = 0, 0
    boxes = [l.strip() for l in f]
    for (a, b) in itertools.combinations(boxes, 2):
        if similar(a, b):
            print(similar(a, b))
            exit()

def similar(a, b):
    for i in range(len(a)):
        ax = list(a)
        bx = list(b)
        ax[i] = '_'
        try:
            bx[i] = '_'
        except:
            print(bx, i)
            print(len(a), len(b))
            print(a)
            print(b)
            raise
        if ax == bx:
            return a[:i] + a[i+1:]
    return False

if __name__ == '__main__' and not sys.flags.inspect: main()
