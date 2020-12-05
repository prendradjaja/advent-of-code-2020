import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    poss = 0
    for line in f:
        line = line.strip()
        sides = ints(line.split())
        a, b, c = sides
        if ineq(a, b, c) and ineq(a, c, b) and ineq(c, b, a):
            poss += 1
    print(poss)

def ineq(a, b, c):
    return a + b > c

if __name__ == '__main__' and not sys.flags.inspect: main()
