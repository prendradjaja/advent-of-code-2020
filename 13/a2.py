import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    start = int(f.readline().strip())
    buses = findints(f.readline().strip())
    waits = [(wait(b, start), b) for b in buses]
    b = min(waits)
    print(b[0] * b[1])

def wait(bid, start):
    return bid - (start % bid)

def nextbus(bid, start):
    return wait(bid, start) + start

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
