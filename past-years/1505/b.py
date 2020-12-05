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
    # print(haspair2('elrlnndorggmmhmx'))
    # exit()
    f = open(sys.argv[1])
    nices = 0
    for line in f:
        line = line.strip()
        if isnice2(line):
            nices += 1
    print(nices)

def haspair(line):
    for pair in consecutives(line):
        pair = ''.join(pair)
        foo = line.replace(pair, '')
        if len(foo) <= len(line) - 4:
            return True
    return False
def hassand(line):
    for triple in consecutives(line, 3):
        triple = ''.join(triple)
        if triple[0] == triple[2]:
            return True
    return False

def isnice(line):
    return haspair(line) and hassand(line)

def haspair2(line):
    print(line, len(line))
    for i in range(len(line) - 1):
        pair = line[i:i+2]
        foo = line[:i] + '_' + line[i+2:]
        print(i, pair, foo)
        if pair in foo:
            return True
    return False
def hassand2(line):
    for i in range(len(line) - 2):
        triple = line[i:i+3]
        # print(triple)
        if triple[0] == triple[2]:
            return True
    return False
def isnice2(line):
    return haspair2(line) and hassand2(line)

if __name__ == '__main__' and not sys.flags.inspect: main()
