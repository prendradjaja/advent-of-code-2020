import fileinput, collections, collections as cl, itertools, math, random, sys, re, string
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    for line in f:
        line = line.strip()

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
