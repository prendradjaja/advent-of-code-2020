import fileinput, collections, collections as cl, itertools, math, random, sys, re
from string import ascii_lowercase
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

doubles = [x*2 for x in ascii_lowercase]
taboos = ['ab', 'cd', 'pq', 'xy']

def main():
    print(isnice('qjhvhtzxzqqjkmpb'))
    print(isnice('xxyxx'))
    print(isnice('uurcxstgmygtbstg'))
    print(isnice('ieodomkazucvgmuy'))

    f = open(sys.argv[1])
    nices = 0
    for line in f:
        line = line.strip()
        if isnice(line):
            nices += 1
    print(nices)

def isnice(line):
    # vows = list(c for c in line if c in 'aeiou')
    # hasdouble = any(d in line for d in doubles)
    # notaboo = all(t not in line for t in taboos)
    # return len(vows) >= 3 and hasdouble and notaboo
    return haspair(line) and hassand(line)

def haspair(line):
    for i in range(len(line) - 1):
        pair = line[i:i+2]
        foo = line[:i] + line[i+2:]
        if pair in foo:
            return True
    return False

def hassand(line):
    for i in range(len(line) - 2):
        triple = line[i:i+3]
        # print(triple)
        if triple[0] == triple[2]:
            return True
    return False

if __name__ == '__main__' and not sys.flags.inspect: main()
