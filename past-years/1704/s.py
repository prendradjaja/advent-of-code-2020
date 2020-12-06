import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    v = 0
    for line in f:
        line = line.strip()
        words = line.split()
        if len(words) == len(set(words)):
            if len(words) == len(set(''.join(sorted(w)) for w in words)):
                v+=1
    print(v)

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
