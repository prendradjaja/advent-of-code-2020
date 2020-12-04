import fileinput, collections, itertools, math, random, sys, re
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    tot = 0
    for line in fileinput.input():
        line = line.strip()
        l,w,h = (int(x) for x in line.split('x'))
        a = l*w
        b = l*h
        c = w*h
        s = min(a,b,c)
        z = 2*(a+b+c) + s
        tot += z
    print(tot)

if __name__ == '__main__' and not sys.flags.inspect: main()
