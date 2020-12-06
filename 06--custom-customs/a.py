import fileinput, collections, collections as cl, itertools, math, random, sys, re
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
# from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tot = 0
    for line in f.read().split('\n\n'):
        tot += len(set(line.strip().replace('\n','')))
    print(tot)

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
